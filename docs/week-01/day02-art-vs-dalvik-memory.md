# Day 2：ART 与 Dalvik 的内存分配差异

> 系列第 2 篇。Day 1 我们把 ART 的 Java Heap 拆成了多个 space，并强调“看证据而不是背概念”。今天把同一件事放到历史对照里：**Dalvik 的内存分配/回收模型到底和 ART 哪里不一样**，以及这些差异如何影响你在 `dumpsys meminfo`、Profiler、GC 日志里看到的现象。

## 背景：为什么 2026 年还要谈 Dalvik

Dalvik 早已退出主流（Android 5.0 之后系统运行时进入 ART 时代），但你仍然会在这些场景里遇到“Dalvik 语境”的残留：

- 旧文章、旧面试题、旧排障手册里大量使用 Dalvik 的术语（例如“mspace”、“Zygote heap / active heap”）。
- 一些现象在 ART 上仍然成立，但**原因变了**：比如“看起来 Java Heap 还没满却 OOM”在 Dalvik 更常由碎片/连续性导致，在 ART 则可能更偏向 space 限制、LOS/非移动区压力，或 Java/Native/Graphics 归因混淆。
- 你需要把“术语翻译”成今天可操作的证据链：**看到某个曲线/日志 → 推断底层 allocator/collector 的约束**。

这篇文章不追求复古细节，而是给出一套可迁移的对照框架：从“分配器（allocator）”和“收集器（collector）”两条线，把差异讲到能用于排障。

## 核心差异一览：从“堆是啥”到“怎么分配”

把问题拆成四个层次，几乎所有差异都能落在这四层：

1) **代码执行与内存形态**（AOT/JIT、代码缓存、image/oat 布局）  
2) **堆组织方式**（一段连续内存 vs 多个 space；是否按 region 管理）  
3) **分配快路径**（是否有 bump pointer/TLAB；小对象 allocator 策略）  
4) **回收与整理能力**（是否 moving；碎片的长期命运是什么）

下面按这四层展开。

## 核心机制

### 1）运行时执行模型不同，决定了“除了 Java Heap 之外你还会看到什么”

Dalvik 时代主要依赖解释执行 + JIT（不同版本策略有变化），而 ART 时代从 Android 5.0 的偏 AOT 到后续引入更强的 JIT/profile-guided compilation，整体呈现为“混合编译”。

这件事对内存排障的直接影响是：

- **代码相关内存**更值得被你显式纳入“进程内存账本”。  
  在 ART 上，oat/vdex、image，以及 JIT 代码缓存（Code Cache）/profile 等，会让你看到更多“看起来不像 Java Heap”的占用。
- 你遇到“安装包升级后内存形态变化”、“冷启动后第一次进入某页面内存峰值更高”等现象时，要把“编译产物与缓存”的波动考虑进去，而不是只盯着 Java Heap 曲线。

实践上：当 Java Heap 曲线平稳但 PSS 仍持续上升时，优先分解 Java/Native/Graphics/Code 的归因，而不是立刻怀疑“泄漏”。

### 2）堆组织方式：Dalvik 更强调连续堆与碎片风险；ART 更强调 space 约束与可移动性

在 Day 1 我们已经建立了 ART 的基本视角：heap 由多个 space 组合而成，space 的“可移动性 + 分配策略”决定了现象。

把 Dalvik 放进来对照，你可以记住一句话：

> Dalvik 更像“在若干连续堆上做分配/回收，长期碎片会成为主要矛盾”；  
> ART 更像“在多个 space 上做分配/回收，约束来自 space 的用途、可移动性与 collector 的选择”。

这会带来两个非常现实的差异：

- **在 Dalvik 上，“剩余总量足够但没有足够大的连续块”更容易直接变成失败。**  
  你在排查“大对象分配失败”（尤其是当时常见的大数组、Bitmap 像素缓冲等）时，碎片/连续性是绕不开的关键词。
- **在 ART 上，大对象更倾向进入 LOS/非移动相关空间，失败更像“某类空间被打满/受限”。**  
  你更需要问“对象为什么会去这个 space、这个 space 的回收/整理能力是什么、它和 collector 的组合是什么”。

换句话说：同样是 OOM，Dalvik 更像“allocator 过不去”，ART 更像“space/collector 的组合过不去”（当然两者并不绝对，版本/配置都会影响）。

### 3）分配快路径：ART 更“为吞吐设计”，这会改变你对短命对象的预期

只看“语言层”的 `new` 很容易误判。真正决定吞吐与碎片趋势的，是运行时的分配快路径。

典型对照是：

- **ART 的分配常见有更激进的快路径**（例如 bump pointer、线程本地缓冲（TLAB）等思想在不同实现中以不同形态出现）。  
  这意味着：短命对象的制造速度可以非常高，GC 的触发更像“为了跟上分配速率”。
- **Dalvik 的分配策略更容易受通用 allocator 行为影响**，在高频分配 + 多尺寸对象混合的情况下，碎片趋势更早显现。  
  所以你会在旧文档里看到更多围绕“堆碎片、连续块、分配失败”的讨论。

排障落点：

- 当你在 ART 上看到 GC 很频繁，第一反应不该是“调 GC”，而是把注意力放到**分配热源**（Allocation Profiler）与“是否存在不必要的短命对象洪峰”。
- 当你在更旧语境里看到“大对象分配失败 + heap 总量看似不足以解释”，碎片/连续性就会被摆在更靠前的位置。

### 4）回收与整理能力：moving collector 的存在，让 ART 更擅长“对抗碎片”，但也引入了新的边界

对碎片的态度，是 Dalvik vs ART 最重要的一条分水岭：

- Dalvik 时代的主流回收策略以标记/清理（mark/sweep）为核心（并发与否、细节随版本变化），它对“整理（compaction）”的能力与成本约束更强，碎片可能长期存在。
- ART 时代引入了更强的 moving/复制类策略（例如 Concurrent Copying 的思路），配合 region/space 设计，使得运行时更有机会在可移动空间内“顺手整理”。

但 moving 不是万能的：它的边界往往来自“可移动性”：

- 不是所有对象都能移动（例如某些需要地址稳定的对象、某些特殊空间里的对象）。
- 大对象往往不适合频繁搬迁，于是更容易进入专门的空间（如 LOS）并呈现出“非移动空间压力”。

因此在 ART 上你会更常做这样的判断链：

1. 这个对象类型/大小，倾向进入哪个 space？  
2. 这个 space 是否可移动、是否会被当前 collector 主动整理？  
3. 如果不整理，长期碎片/回收滞后会不会把这个 space 推到上限？  
4. 最终表现为：GC 频繁、停顿变长，还是直接分配失败？

## 观测与定位：把“对照框架”落到工具上

### 1）先把账拆开：Java / Native / Graphics / Code

不管你排的是 Dalvik 语境还是 ART 语境，第一步仍然是把“总量”拆成可行动的归因：

```bash
adb shell dumpsys meminfo <pid>
```

建议固定看这几类信号（字段名称随版本略有差异，但思路稳定）：

- Java Heap：是否真的是 Java 对象在增长？还是只是某次峰值后的残留？
- Native Heap：是否存在 JNI/第三方库缓存、malloc 堆增长？
- Graphics：是否存在 Bitmap/GPU 相关占用（尤其是界面切换/大图场景）？
- Code：是否存在 code cache / dex/oat 相关增长（升级、首次运行、热路径编译后）？

> Day 1 的结论在这里继续生效：**不要用“Java Heap 还没满”去否定 OOM 的可能性**，因为 OOM 往往来自“某类空间/某类归因”的硬约束，而不是总量。

### 2）把“短命对象洪峰”变成证据：Profiler 的 Allocation 视图

在 ART 上，短命对象的吞吐能力更强，导致“分配速率 → GC 节奏”更直接。你要用 Allocation 视图回答：

- 哪些调用路径在制造大量临时对象？
- 是否存在可避免的装箱/集合中间态/字符串拼接/重复解析？
- 峰值是否与某一段 UI 动画、列表滚动、图片解码强相关？

当你能把“GC 频繁”还原成“某个热源在制造对象”，排障就从玄学变成工程。

### 3）面对“大对象失败”：先确认是 Java 侧失败还是 Native/Graphics 侧失败

很多旧材料把“大对象 OOM”直接归为“Dalvik heap 不够”。在今天更稳的做法是：

- 先确认堆栈：是 `OutOfMemoryError: Failed to allocate a ... byte allocation` 的 Java 分配失败，还是 native 崩溃/被 LMK？
- 再确认归因：大对象来自 Java 数组？来自 Bitmap 像素缓冲？来自 native mmap/malloc？
- 最后才谈策略：降采样、分块、复用、缓存上限、分配位置（Java vs native）与生命周期控制。

## 面试/排障问答（用“可操作的判断链”回答）

1. “Dalvik 和 ART 的内存模型差异是什么？”  
   建议答法：差异不只在 GC 算法，而是“执行模型 → 堆组织 → 分配快路径 → 整理能力”的组合差异。Dalvik 更受连续堆/碎片影响；ART 通过 space + moving collector 在可移动区更能对抗碎片，但同时引入 LOS/非移动区等新的边界。

2. “为什么 Java Heap 看起来没满也会 OOM？”  
   建议答法：OOM 不是只由“总量”决定，而是由“某类空间/归因的约束”决定。Dalvik 语境里常见是碎片与连续块不足；ART 语境里常见是某个 space（如大对象/非移动相关）压力、或 Native/Graphics/Code 归因增长。

3. “在 ART 上看到 GC 很频繁你怎么做？”  
   建议答法：先用 Profiler 把分配热源定位出来，确认是否是短命对象洪峰；再看 `dumpsys meminfo` 拆分归因，避免把 Native/Graphics/Code 的问题误判为 Java 泄漏；最后才考虑 GC 行为与版本差异（collector/space 组合）。

## 参考路径（用于把概念落到源码与工具）

- AOSP（ART）：
  - `art/runtime/gc/heap.h`
  - `art/runtime/gc/heap.cc`
  - `art/runtime/gc/space/`
  - `art/runtime/gc/collector/`
- 工具：
  - `adb shell dumpsys meminfo`
  - Android Studio Memory Profiler（Allocation/Heap Dump）

