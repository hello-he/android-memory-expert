# Day 14：Generational GC 在 ART 中的实现
> 系列第 14 篇。目标不是把 ART 套进 HotSpot 的 Young/Old 模型，而是用 **space、collector、年龄假设、写屏障、日志证据** 来判断：目标设备上到底有没有、怎么运行、是否值得排查。

---

## 一句话结论

- **Generational GC 的核心收益来自“多数对象很快死亡”的年龄假设：先回收年轻对象，减少全堆扫描成本。**
- **在 ART 里不能直接套用 HotSpot 的 Eden/Survivor/Old 话术；必须回到 `RegionSpace`、collector 类型、read/write barrier、GC cause 和目标 Android 分支。**
- **排查时先证明目标运行时真的走了 generational 路径，再看年轻代回收是否降低 pause、total time 和 For Alloc 压力。**
- **如果 GC 后 freed 很少，问题通常不在 generational 策略本身，而在 retained path、LOS、大对象或 Native/Graphics 压力。**

---

## 图 1：ART generational GC 的结构视角

```mermaid
flowchart TD
  A["Java/Kotlin allocation"] --> B{"对象大小与分配路径"}
  B -->|普通对象| C["Bump pointer / TLAB\n进入可移动 space"]
  B -->|大对象| D["Large Object Space\n通常不按年轻代快速搬迁"]

  C --> E["RegionSpace / moving space\n按 region 承载对象"]
  E --> F{"年龄假设成立吗？"}

  F -->|大量短命对象| G["Young / partial collection\n优先处理年轻 region"]
  F -->|存活对象多| H["Full / whole-heap collection\n扩大扫描与移动范围"]

  G --> I["Remembered set / card table\n记录老对象指向年轻对象"]
  H --> J["Root scan + heap graph\n完整可达性判断"]

  I --> K["collector phase\ncopy / mark / reference processing"]
  J --> K
  K --> L["logcat / Perfetto\ncause + freed + paused + total"]
  D --> M["meminfo / maps / heap dump\n检查 LOS 压力"]
  L --> N["工程判断\n降低分配率或查 retained path"]
  M --> N
```

### 读图规则

| 结构 | 工程含义 | 证据入口 |
|---|---|---|
| young / partial collection | 只处理一部分年轻对象区域，期待短命对象快速死亡 | GC 日志 cause、freed、paused、total |
| remembered set / card table | 老对象指向年轻对象时，年轻代 GC 不能只扫年轻对象 | AOSP `card_table`、`remembered_set` 搜索 |
| RegionSpace | ART CC 常见空间表达，比 Eden/Survivor 更贴近源码 | `art/runtime/gc/space/region_space.*` |
| Large Object Space | 大对象压力通常不会被“年轻代更快”直接解决 | `dumpsys meminfo`、heap dump、`/proc/<pid>/maps` |
| full collection | 年轻代回收无法满足目标时，仍要回到全堆可达性 | Perfetto GC slice + heap dump |

---

## 先立边界：不要把 ART 讲成 HotSpot

| 容易误用的话 | 更严谨的 ART 表达 |
|---|---|
| “ART 一定有 Eden、Survivor、Old” | “目标分支可能有 generational CC，但应以 RegionSpace、collector 和日志字段确认。” |
| “Young GC 一定 pause 更短” | “只在短命对象多、跨代引用少、调度不拥塞时更可能降低成本。” |
| “Full GC 就是 Old GC” | “ART 日志和源码要按 collector/cause/space 看，不能直接套 HotSpot 名称。” |
| “freed 少说明 generational GC 无效” | “freed 少通常先查强可达链、LOS、Native/Graphics，而不是先怪 collector。” |

---

## 版本与源码入口

Day 13 留下的浅点是：pause phase、collector 默认组合、日志字段都没有绑定目标分支。这里直接把 Day 14 的讲法收窄为 **需要目标 Android 分支验证**。

| 要确认的问题 | AOSP 搜索入口 | 运行时信号 | 命令 |
|---|---|---|---|
| 是否启用 generational collector | `art/runtime/gc/heap.*`、`collector_type`、`generational` | GC reason / collector 名称 | `rg -n "generational|young|CollectorType|kCollectorType" art/runtime/gc` |
| young collection 如何选 region | `art/runtime/gc/space/region_space.*` | freed 对象多、pause 较短 | `rg -n "RegionSpace|young|age|evac" art/runtime/gc/space art/runtime/gc/collector` |
| 跨代引用如何维护 | `card_table`、`remembered_set`、write barrier | young GC 仍能找到老到新的引用 | `rg -n "CardTable|RememberedSet|write barrier|mod-union" art/runtime` |
| 何时退回 full collection | `CollectGarbageInternal`、`GcCause`、footprint/growth limit | For Alloc 后仍紧张或 freed 少 | `rg -n "CollectGarbageInternal|GcCause|footprint|growth_limit" art/runtime/gc/heap.*` |
| 是否撞到 LOS | `large_object_space.*` | Java Heap/LOS 高，普通 young GC 不解压 | `adb shell dumpsys meminfo <package>` |

```bash
cd <aosp>

# 1. 不先背概念，先确认目标分支有没有 generational 相关路径
rg -n "generational|young generation|young|tenuring|age" art/runtime/gc

# 2. 看 collector 与 heap 入口
rg -n "CollectorType|GcCause|CollectGarbage|CollectGarbageInternal" art/runtime/gc/heap.cc art/runtime/gc/heap.h

# 3. 看 RegionSpace / LOS / remembered set
rg -n "RegionSpace|LargeObject|RememberedSet|CardTable|ModUnion" art/runtime/gc art/runtime
```

---

## 图 2：从分配峰值到 young / full GC 的执行路径

```mermaid
sequenceDiagram
  participant App as App threads
  participant Alloc as Allocator
  participant Heap as ART heap.cc
  participant YG as Young / partial GC
  participant FG as Full GC
  participant Log as logcat / Perfetto

  App->>Alloc: 高频创建短命对象
  Alloc->>Heap: space 或 footprint 接近阈值
  Heap->>YG: 尝试年轻区域回收
  YG->>YG: 扫 roots + remembered set
  YG->>Log: freed / paused / total / cause
  YG-->>Heap: 回收足够？
  alt 足够
    Heap-->>Alloc: 分配恢复
    Log->>Log: 记录为分配峰值问题
  else 不足
    Heap->>FG: 扩大为 full / whole-heap work
    FG->>FG: 扫更多对象与 reference
    FG->>Log: 更高 total 或 pause 风险
    Log->>Log: 转 retained path / LOS / Native 排查
  end
```

### 观察矩阵

| 现象组合 | 更可能说明 | 下一步 |
|---|---|---|
| For Alloc 高频 + young GC freed 多 | 分配 churn，短命对象多 | Allocation Profiler 找热点，削峰 |
| young GC pause 短但 total 偶尔长 | 并发阶段或调度竞争 | Perfetto 看 GC thread runnable/blocked |
| young GC freed 少 + heap 持续涨 | 年轻代不是根因 | heap dump 看 retained path |
| full GC 频繁出现 | young 回收不足或堆压力过大 | 查存活率、LOS、大对象、Native/Graphics |
| Java Heap 不高但 RSS 高 | GC 策略解释不了主压力 | 看 Native Heap、Graphics、maps |

---

## 图 3：排障决策流

```mermaid
flowchart TD
  A["看到 GC 频繁 / pause / OOM"] --> B["先确认目标分支和日志字段"]
  B --> C{"日志或源码能证明 generational/young 路径吗？"}

  C -->|不能| D["不要声称是年轻代问题\n按普通 GC trigger/pause 流程排查"]
  C -->|能| E["抓 logcat + Perfetto + meminfo"]

  E --> F{"young GC freed 多吗？"}
  F -->|是| G["分配峰值 / churn\nAllocation Profiler 定位热点"]
  F -->|否| H["heap dump\nDominator / Path To GC Roots"]

  G --> I{"pause 或 total 仍影响帧吗？"}
  I -->|是| J["Perfetto 对齐 MainThread / RenderThread / GC thread"]
  I -->|否| K["优化分配率\n记录收益即可"]

  H --> L{"LOS 或 Native/Graphics 高吗？"}
  L -->|是| M["转大对象 / Bitmap / native 内存路径"]
  L -->|否| N["查长生命周期引用链\n静态、单例、JNI Global、listener"]

  J --> O["验证优化前后\npaused / total / frame miss / allocation rate"]
  K --> O
  M --> O
  N --> O
```

---

## 最小证据链

| 步骤 | 命令/工具 | 目标 |
|---|---|---|
| 1 | `adb logcat -v time \| rg -n "GC\|young\|freed\|paused\|Alloc\|Concurrent"` | 读取 cause、freed、paused、total |
| 2 | `adb shell dumpsys meminfo <package>` | 判断 Java Heap、Native Heap、Graphics 谁是主压力 |
| 3 | Android Studio Allocation Profiler | 找短命对象和分配峰值 |
| 4 | Perfetto `sched + dalvik + gfx + view` | 判断 GC 是否与帧 deadline 重叠 |
| 5 | `adb shell am dumpheap <package> /data/local/tmp/app.hprof` | freed 少时查 retained path |
| 6 | AOSP `rg` | 绑定目标分支的 collector、space、barrier 事实 |

```bash
# GC 日志：先拿到 cause、freed、pause、total
adb logcat -v time | rg -n "GC|young|freed|paused|Alloc|Concurrent|Explicit|Background"

# 内存归属：确认是否真是 Java heap
adb shell dumpsys meminfo <package> | head -n 180

# Perfetto：把 GC、调度、帧放在同一时间线上
adb shell perfetto -o /data/misc/perfetto-traces/gc-gen.perfetto-trace -t 20s sched freq idle am wm gfx view dalvik --txt
adb pull /data/misc/perfetto-traces/gc-gen.perfetto-trace .

# freed 少：转 retained path，不要反复手动 GC
adb shell am dumpheap <package> /data/local/tmp/app.hprof
adb pull /data/local/tmp/app.hprof .
```

---

## 优化动作表：按证据选战场

| 证据 | 不要先做 | 应该先做 |
|---|---|---|
| young GC 高频且 freed 多 | 调 collector 参数 | 降低分配率、复用对象、拆峰 |
| young GC 高频但 freed 少 | 继续期待年轻代回收 | heap dump 查存活链 |
| full GC 紧跟 young GC | 只看 pause 字段 | 查堆增长、LOS、retained path |
| total 长但 paused 短 | 说“主线程被 GC 卡住” | Perfetto 查调度竞争和 GC thread |
| Java Heap 低、RSS 高 | 优化 Java GC | 查 Native Heap、Graphics、mmap |
| Explicit GC 混入 | 把它当优化手段 | 搜索调用方，删除或移出关键路径 |

---

## 一张跨主题连接表

| 前序文章 | Day 14 复用点 | 为什么重要 |
|---|---|---|
| Day 11：源码路径 | `heap.cc -> collector -> space -> reference_processor` | generational 结论必须能落到源码路径 |
| Day 12：触发时机 | For Alloc / Background / Explicit | young GC 高频常常是分配触发，不是 collector 结论 |
| Day 13：pause 优化 | paused / total / Perfetto 对齐 | generational 是否有收益要看帧和调度证据 |
| Day 10：可达性 | retained path | freed 少时回到引用链，而不是调 GC |
| Day 3：分配路径 | TLAB / bump pointer / LOS | young GC 优化经常从分配率和大对象开始 |

---

## 这篇要记住的 5 句工程话术

| 场景 | 更好的表达 |
|---|---|
| 讨论 ART generational GC | “先确认目标分支的 collector、space 和日志字段。” |
| 看到 young GC 高频 | “先量分配率和对象存活率。” |
| young GC freed 少 | “转 heap dump，看 retained path。” |
| full GC 频繁 | “年轻代回收不足只是现象，继续拆 Java Heap、LOS、Native、Graphics。” |
| 评价优化收益 | “用 paused、total、frame miss、allocation rate 四个指标前后对比。” |

---

## 边界记录

| 边界 | 本文处理方式 |
|---|---|
| Android 分支差异 | 不声称所有 ART 版本都有相同 generational 行为；必须用目标 AOSP 分支验证。 |
| ROM 差异 | 厂商可能改日志、调度和 GC 策略；只用一台设备不能外推。 |
| 工具证据缺口 | 没有真实 Perfetto trace 时，只能给证据链模板，不能声称已验证具体 pause 阶段。 |
| GitHub Issues | 本次 `gh issue list` 因未认证被阻塞，不能声称吸收了 open Issue 反馈。 |
