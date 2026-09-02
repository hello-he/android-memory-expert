# Android 内存专家养成计划

每天自动生成一篇深度技术文章，80 天系统覆盖 Android 内存核心知识体系。

由 Codex 自动化任务驱动：无需手动操作（默认北京时间 08:00 自动更新）。

有想法/反馈：欢迎在这里开一个 [Issue](../../issues/new)，后续文章会自然融入你的问题与场景。

---

## 专项目标

这套计划新增一个低端机系统内存专项：围绕 **内存水位增长来源追查**、**内存水位过低导致卡顿** 与 **lmkd 查杀看似优先级更高的进程** 三类真实问题，建立从 `meminfo / vmstat / slab / dma-buf / memcg / watermark / kswapd / direct reclaim / PSI / lmkd / oom_score_adj / ZRAM / mmd` 到 Perfetto、logcat、`/proc`、statsd 的完整证据链。

详细路线见：[低端机系统内存学习规划](docs/learning-plan-low-end-memory.md)。

---

## 学习进度

| 文章 | 主题 | 状态 |
|------|------|------|
| Day 01 | Java 堆结构：Young/Old Generation 在 ART 上的实现 | ✅[2026-05-19](docs/week-01/day01-art-heap-structure.md) |
| Day 02 | ART 与 Dalvik 的内存分配差异 | ✅[2026-05-20](docs/week-01/day02-art-vs-dalvik-memory.md) |
| Day 03 | 对象分配路径：TLAB、bump pointer、Large Object Space | ✅[2026-05-21](docs/week-01/day03-object-allocation-path.md) |
| Day 04 | 栈内存与帧结构（ART 视角）：从局部引用到 GC Roots | ✅[2026-05-22](docs/week-01/day04-stack-memory-and-frames.md) |
| Day 05 | 方法区与元数据空间（ART 视角）：ClassLinker、DEX/OAT/VDEX、JIT Code Cache | ✅[2026-05-24](docs/week-01/day05-metaspace-and-method-area.md) |
| Day 06 | String 常量池与 intern() 机制（ART 视角） | ✅[2026-05-24](docs/week-01/day06-string-pool-and-intern.md) |
| Day 07 | 对象头结构与 Mark Word | ✅[2026-05-25](docs/week-01/day07-object-header-and-mark-word.md) |
| Day 08 | 引用类型：强引用、软引用、弱引用、虚引用 | ✅[2026-05-26](docs/week-02/day08-reference-types.md) |
| Day 09 | ART GC 算法：CMS 与 CC（Concurrent Copying） | ✅[2026-05-28](docs/week-02/day09-art-gc-algorithms.md) |
| Day 10 | GC Roots 枚举与可达性分析 | ✅[2026-05-31](docs/week-02/day10-gc-roots-and-reachability.md) |
| Day 11 | ART GC 源码：gc/collector/ 目录关键路径 | ✅[2026-06-28](docs/week-02/day11-art-gc-source-code.md) |
| Day 12 | GC 触发时机：alloc gc、background gc、explicit gc | ✅[2026-06-29](docs/week-02/day12-gc-trigger-timing.md) |
| Day 13 | GC pause 的来源与优化思路 | ✅[2026-06-30](docs/week-02/day13-gc-pause-and-optimization.md) |
| Day 14 | Generational GC 在 ART 中的实现 | ✅[2026-07-15](docs/week-02/day14-generational-gc-in-art.md) |
| Day 15 | 内存泄漏的本质：GC Roots 持有链分析 | ✅[2026-08-09](docs/week-03/day15-memory-leak-essence.md) |
| Day 16 | Activity/Fragment 泄漏的常见模式 | ✅[2026-08-12](docs/week-03/day16-activity-fragment-leak.md) |
| Day 17 | Handler 泄漏：消息队列与生命周期的冲突 | ✅[2026-08-16](docs/week-03/day17-handler-leak.md) |
| Day 18 | 静态持有、单例泄漏的排查路径 | ✅[2026-08-17](docs/week-03/day18-static-singleton-leak.md) |
| Day 19 | Listener 未注销与匿名内部类泄漏 | ✅[2026-08-19](docs/week-03/day19-listener-and-inner-class-leak.md) |
| Day 20 | Cursor、Stream 等资源未关闭的泄漏场景 | ✅[2026-08-20](docs/week-03/day20-resource-not-closed-leak.md) |
| Day 21 | LeakCanary 源码与泄漏引用链检测 | ✅[2026-08-23](docs/week-03/day21-leakcanary-source-code.md) |
| Day 22 | Android Studio Memory Profiler 核心工作流 | ✅[2026-08-25](docs/week-04/day22-memory-profiler-core.md) |
| Day 23 | Heap Dump 与 HPROF 文件结构 | ✅[2026-08-25](docs/week-04/day23-heap-dump-hprof.md) |
| Day 24 | MAT 入门与泄漏分析实战 | ✅[2026-08-25](docs/week-04/day24-mat-intro.md) |
| Day 25 | MAT Dominator Tree 与 Retained Heap 解读 | ✅[2026-08-25](docs/week-04/day25-mat-dominator-tree.md) |
| Day 26 | Allocation Tracker 与对象分配热点定位 | ✅[2026-08-25](docs/week-04/day26-allocation-tracker.md) |
| Day 27 | dumpsys meminfo 输出字段解读：PSS/RSS/USS | ✅[2026-08-25](docs/week-04/day27-dumpsys-meminfo.md) |
| Day 28 | procrank、showmap 与系统内存全局视图 | ✅[2026-08-25](docs/week-04/day28-procrank-showmap-system-memory.md) |
| Day 29 | JNI Local/Global Reference 与跨边界泄漏 | ✅[2026-08-25](docs/week-05/day29-jni-local-global-reference.md) |
| Day 30 | NewByteArray、GetPrimitiveArrayCritical 与 DirectByteBuffer 内存归属 | ✅[2026-08-25](docs/week-05/day30-jni-byte-array-direct-buffer.md) |
| Day 31 | Native Heap 分配器：jemalloc、Scudo 与 malloc 调试 | ✅[2026-08-25](docs/week-05/day31-native-heap-allocator.md) |
| Day 32 | /proc/&lt;pid&gt;/maps、smaps 与 native 内存映射全貌 | ✅[2026-08-25](docs/week-05/day32-proc-maps-smaps-layout.md) |
| Day 33 | mmap、ashmem、memfd 与 dma-buf 的内存账单 | ✅[2026-08-25](docs/week-05/day33-mmap-ashmem-dmabuf.md) |
| Day 34 | Native 内存泄漏工具链：heapprofd、malloc_debug、Perfetto | ✅[2026-08-25](docs/week-05/day34-native-memory-leak-tools.md) |
| Day 35 | Native Crash 与 tombstone：从 signal 到 backtrace | ✅[2026-08-25](docs/week-05/day35-native-crash-tombstone.md) |
| Day 36 | 内存越界、内存踩踏、UAF 与 double free 问题模型 | ✅[2026-08-25](docs/week-06/day36-memory-corruption-model.md) |
| Day 37 | ASan 检测 Native 内存错误：构建、运行与报告解读 | ✅[2026-08-25](docs/week-06/day37-asan-native-memory-error.md) |
| Day 38 | HWASan 与 Android 整机内存错误定位 | ✅[2026-08-25](docs/week-06/day38-hwasan-native-memory-error.md) |
| Day 39 | GWP-ASan、Scudo 与 MTE：低开销检测和运行时防护 | ✅[2026-08-25](docs/week-06/day39-gwp-asan-scudo-mte.md) |
| Day 40 | KASAN 与 KFENCE：Kernel 内存越界和 UAF 定位 | ✅[2026-08-25](docs/week-06/day40-kasan-kfence-kernel-memory.md) |
| Day 41 | Bitmap 内存模型：Android 8.0 前后的变化 | ✅[2026-08-25](docs/week-06/day41-bitmap-memory-model.md) |
| Day 42 | Bitmap 像素数据、Native Heap 与 Graphics 归因 | ✅[2026-08-25](docs/week-06/day42-bitmap-pixel-native-heap.md) |
| Day 43 | BitmapFactory.Options：inSampleSize、inBitmap 与解码峰值 | ✅[2026-08-25](docs/week-07/day43-bitmapfactory-options.md) |
| Day 44 | Glide 内存缓存架构：LruCache、BitmapPool 与生命周期 | ✅[2026-08-25](docs/week-07/day44-glide-memory-cache.md) |
| Day 45 | 大图加载策略：Region Decode、Tile 与峰值控制 | ✅[2026-08-25](docs/week-07/day45-large-image-region-decoder.md) |
| Day 46 | 硬件加速、RenderThread、GPU 内存与 dma-buf | ✅[2026-08-25](docs/week-07/day46-hardware-acceleration-gpu-memory.md) |
| Day 47 | Android 进程内存限制：memoryClass、largeHeap 与进程上限 | ✅[2026-08-25](docs/week-07/day47-process-memory-limit.md) |
| Day 48 | Android 低内存全景：RAM、ZRAM、kswapd、PSI 与 LMKD | ✅[2026-08-25](docs/week-07/day48-android-low-memory-overview.md) |
| Day 49 | Linux Page Reclaim：file/anon 页、LRU 与 MGLRU | ✅[2026-08-25](docs/week-07/day49-linux-page-reclaim-lru-mglru.md) |
| Day 50 | 内存水位机制：zone、min/low/high watermark 与保留页 | ✅[2026-08-25](docs/week-08/day50-memory-watermark-zone.md) |
| Day 51 | 低端机卡顿根因：kswapd、direct reclaim、compaction 与 UI 抖动 | ✅[2026-08-25](docs/week-08/day51-kswapd-direct-reclaim-jank.md) |
| Day 52 | PSI 内存压力：some/full、avg10/60/300 与 thrashing 判断 | ✅[2026-08-25](docs/week-08/day52-psi-memory-pressure.md) |
| Day 53 | 内存水位增长来源追查：meminfo、vmstat、slab、dma-buf、memcg | ✅[2026-09-03](docs/week-08/day53-memory-waterline-growth-attribution.md) |
| Day 54 | lmkd 架构：PSI/vmpressure、kill strategy 与关键属性 | ✅[2026-09-03](docs/week-08/day54-lmkd-architecture-psi-vmpressure.md) |
| Day 55 | ActivityManager OomAdjuster：进程状态到 oom_score_adj | ⏳待生成 |
| Day 56 | 为什么 lmkd 会杀看似优先级更高的进程：证据链与误判拆解 | ⏳待生成 |
| Day 57 | lmkd 日志、statsd 与 victim 分析：从 kill reason 到 adj/RSS | ⏳待生成 |
| Day 58 | ZRAM 与 swap 路径：压缩、换入换出、mm_stat 与延迟代价 | ⏳待生成 |
| Day 59 | mmd、ZRAM writeback/recompression 与厂商内存拓展 | ⏳待生成 |
| Day 60 | App Compaction、CachedAppOptimizer、onTrimMemory 与缓存释放 | ⏳待生成 |
| Day 61 | 低内存复现实验室：stress、trace、logcat 与可重复场景 | ⏳待生成 |
| Day 62 | 水位与 lmkd 调参：min_free_kbytes、watermark_scale_factor、lmkd 属性与风险 | ⏳待生成 |
| Day 63 | 关键进程保护：adj 设计、绑定关系、前台服务与滥用边界 | ⏳待生成 |
| Day 64 | 案例复盘：低端机内存水位过低导致卡顿 | ⏳待生成 |
| Day 65 | 案例复盘：lmkd 查杀高优先级进程的根因定位 | ⏳待生成 |
| Day 66 | 共享内存与 IPC 内存账单：ashmem、memfd、Binder、dma-buf | ⏳待生成 |
| Day 67 | memcg 与 cgroup：每个 App 的内存隔离和系统视图 | ⏳待生成 |
| Day 68 | Native/System 内存归因：smaps、showmap、heapprofd、memcg 交叉验证 | ⏳待生成 |
| Day 69 | 启动阶段内存控制：冷启动峰值、预加载与缓存时机 | ⏳待生成 |
| Day 70 | RecyclerView 内存优化：ViewHolder、Prefetch、Pool 与图片峰值 | ⏳待生成 |
| Day 71 | 多进程架构的内存收益、账单代价与 lmkd 风险 | ⏳待生成 |
| Day 72 | ProGuard/R8 对 dex、类加载、JIT 与运行时内存的影响 | ⏳待生成 |
| Day 73 | 内存优化全局方法论：观测、归因、干预、验证 | ⏳待生成 |
| Day 74 | AOSP 内存源码阅读路径：ART、AMS、lmkd、kernel、mmd | ⏳待生成 |
| Day 75 | Android 版本演进中的内存变化：5.0 到 17 | ⏳待生成 |
| Day 76 | 面试高频：GC、泄漏、OOM 与 Native 内存 | ⏳待生成 |
| Day 77 | 面试高频：Bitmap、LMKD、PSI、水位与 ZRAM | ⏳待生成 |
| Day 78 | 综合实战：一次低端机卡顿和误杀进程的完整排查 | ⏳待生成 |
| Day 79 | Android 内存评审清单：上线前、灰度中、事故后 | ⏳待生成 |
| Day 80 | 总结：Android 内存专家知识图谱 | ⏳待生成 |

---

## 系统架构

```
Codex 自动化任务（每天 08:00 北京时间）
    ↓
读取 progress.json → 今日主题
    ↓
读取 reflections/ → 已有积累与待补强点
    ↓
读取 open Issues → 用户反馈（若可用）
    ↓
生成深度文章 + 自我反思（reflection）
    ↓
commit & push →（可选）关闭已处理 Issues
```

---

## 自我进化机制

每次生成后都会写入 `reflections/dayXX.json`，并维护 `reflections/evolution-ledger.md`。

长期约束：
- 每篇文章必须承接至少一个历史反思里的 `shallow_points` / `knowledge_gaps` / `suggest_future_topics`，并在新 reflection 的 `applied_reflections` 与 `visible_changes` 中写清楚“怎么落地的”。  
- 遇到无法验证的版本差异、ROM 差异或工具权限问题，必须明确记录边界与 blocker（不假装已经确认）。  

写作规范（视觉优先）：
- 多图少文字：优先 Mermaid 图、表格、对照矩阵、短 checklist；长段落必须拆短。  
- 每篇文章至少 2 张 Mermaid：一张讲核心结构/执行路径；一张讲排障决策流。  
- 结论必须落到可观测证据：`dumpsys meminfo`、`/proc/<pid>/maps`、GC 日志、heap dump、allocation 视图、AOSP 路径等。  
