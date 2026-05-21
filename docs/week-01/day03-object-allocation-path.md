# Day 3：对象分配路径：TLAB、bump pointer、Large Object Space

> 系列第 3 篇。前两篇把 ART 的堆结构和 Dalvik/ART 差异讲清楚后，今天进入对象真正落地的路径：一次 `new` 如何从线程快路径走到 allocator，什么时候进入 TLAB 或 bump pointer，什么时候被分流到 Large Object Space。

## 背景：分配路径决定你看到的内存现象

Android 内存排查里，“对象太多”“GC 太频繁”“Java Heap 还没满却 OOM”这些描述都不够精确。真正有用的问题是：

- 对象是不是短时间内高频创建，压垮了分配快路径？
- 对象大小是否超过阈值，被分流到了 Large Object Space？
- 分配失败是总量压力、连续空间压力，还是特定 space 的约束？
- GC 日志里的 freed objects 和 freed bytes，能不能解释当前分配模式？

这些问题都要回到对象分配路径。应用层写一行 `Foo()`，ART 内部会根据对象大小、线程状态、当前 collector、space 配置和分配器策略，选择不同路径。路径越快，越依赖简单指针移动和线程本地缓存；路径越慢，越可能触发锁竞争、space 扩容、GC，甚至 OOM。

## 核心机制：从 `new` 到 space

### 1. 普通对象先争取走线程快路径

对象分配的理想情况是线程自己完成，不进入全局锁，也不立刻触发 GC。ART 会尽量把小对象分配压到快路径：

- 已知类元数据后，运行时可以计算对象大小和布局。
- 小对象优先走当前线程可用的分配缓冲或普通 alloc space。
- 分配成功后，对象头、klass 指针和必要字段会被初始化。
- 如果当前分配区域不够，才进入慢路径处理 refill、GC 或 OOM。

这个设计解释了一个工程现象：短命对象不一定会让内存最终很高，但会让分配速率、GC 频率和 CPU 时间变差。很多滚动卡顿、列表刷新抖动，不是因为对象泄漏，而是因为每帧创建了太多临时对象。

### 2. TLAB：把分配竞争移到线程本地

TLAB（Thread Local Allocation Buffer）可以理解为线程私有的一小段分配缓冲。线程拿到一段可用空间后，分配小对象时只需要移动当前线程的指针：

```text
thread TLAB:

base          current                  end
 |--------------|----------------------|
                ^
                分配一个小对象后 current 向后移动
```

它解决的是并发分配竞争。如果所有线程都在同一个全局 allocator 上抢锁，小对象高频创建会把锁竞争放大。TLAB 让大多数小对象分配变成线程本地操作，只在缓冲耗尽、需要 refill 时进入较慢路径。

TLAB 的边界也很清楚：

- 它适合小对象和高频分配。
- 它不负责长期保存对象；对象是否存活仍由 GC 和引用链决定。
- 它不是“年轻代”的同义词，只是年轻对象常经过的分配快路径。
- TLAB 过小会频繁 refill，过大可能增加未使用空间和统计噪声。

### 3. Bump pointer：顺序移动指针的分配模型

Bump pointer 分配器的核心动作更直接：当前位置满足对象大小和对齐要求，就把指针向后推进。这个模型常见于移动式 GC 或 region 化空间中，因为这些空间可以在 GC 后形成较规整的可分配区域。

```text
region / bump space:

start        top                         limit
 |------------|--------------------------|
              ^
              top += aligned_object_size
```

它的优势是极快：不需要复杂空闲链表搜索，不需要在分配时处理大量碎片。代价是它依赖后续 GC 整理空间。如果对象大量存活，或者某些对象不可移动，bump pointer 的优势会被存活集和非移动约束削弱。

在 ART 语境下，bump pointer 要和 collector 一起看。Concurrent Copying 这类移动式 collector 能把存活对象复制/搬迁到新的区域，让后续分配继续保持顺序分配的优势。没有整理能力时，单纯移动指针无法解决碎片。

### 4. Large Object Space：大对象单独处理

大对象不适合混在普通小对象空间里。原因很朴素：一个几 MiB 的数组或 Bitmap 包装对象，如果塞进普通 alloc space，会放大碎片、移动成本和连续空间要求。ART 因此会把超过阈值的大对象分流到 Large Object Space（LOS）。

LOS 的特点是：

- 分配对象少，但单个对象占用大。
- 回收收益可能很高，但必须等引用链断开。
- 连续空间或映射成本更敏感。
- 它经常和 Bitmap、大数组、DirectByteBuffer 包装对象、缓存策略一起出现。

所以看到 OOM 时，不能只盯 `Java Heap` 总量。一个大对象分配失败，可能不是普通对象太多，而是 LOS 或进程整体地址/内存约束无法满足这次分配。

### 5. 慢路径：分配失败之后发生什么

快路径失败不等于立刻 OOM。ART 通常会进入慢路径，按条件尝试：

1. refill 线程本地缓冲。
2. 从目标 space 申请更多空间。
3. 触发不同原因的 GC，例如 allocation GC。
4. 在 GC 后重试分配。
5. 仍失败时抛出 `OutOfMemoryError`。

这也是为什么 OOM 日志前常常能看到密集 GC。GC 不是 OOM 的原因，它通常是运行时在 OOM 前最后几次自救。

## 代码示例

下面的 Kotlin 代码分别制造三种压力：短命小对象、高频中等对象、长期持有的大对象。它不是为了模拟 ART 内部路径，而是让你在 Profiler 和 GC 日志里看到不同分配模式。

```kotlin
class AllocationPathDemo {
    private val retained = mutableListOf<ByteArray>()

    fun shortLivedSmallObjects(rounds: Int) {
        repeat(rounds) { round ->
            val names = ArrayList<String>(512)
            repeat(512) { index ->
                names += "item-$round-$index"
            }
        }
    }

    fun mediumObjectsBurst(rounds: Int) {
        repeat(rounds) {
            ByteArray(64 * 1024)
        }
    }

    fun retainLargeObjects(count: Int) {
        repeat(count) {
            retained += ByteArray(4 * 1024 * 1024)
        }
    }

    fun clearRetained() {
        retained.clear()
    }
}
```

`shortLivedSmallObjects()` 更容易表现为分配速率高、GC 频繁但回收也快。`mediumObjectsBurst()` 会让你观察到更明显的 allocation burst。`retainLargeObjects()` 会让 retained heap 和 LOS 压力更明显，因为对象被成员集合强引用持有，GC 不能回收。

## 常见问题与误判

### 把 TLAB 当成对象生命周期区域

TLAB 是分配优化，不是生命周期边界。对象从 TLAB 分配出来后，是否存活取决于引用链。一个从 TLAB 出生的对象可以立刻死亡，也可以被静态集合持有到进程结束。

### 只优化泄漏，忽略分配洪峰

没有泄漏也会卡。列表绑定、动画帧、日志拼接、JSON 解析都可能制造大量短命对象。GC 能回收它们，但回收本身占 CPU，并可能带来暂停或调度抖动。

### 看到大对象就怪 Bitmap

Bitmap 常见，但不是唯一大对象。`ByteArray`、`IntArray`、大字符串、解压缓冲、序列化缓存都可能进入大对象路径。排查时要看对象类型和引用链，不要按经验直接归因。

### 认为 GC 后内存应该完全归零

GC 只处理不可达对象。可达的大对象不会被回收；allocator 也不一定立刻把空闲页归还系统。meminfo、heap dump 和对象引用链要一起看。

## 观测方法

### 用 Allocation 视图看分配速率

Android Studio Memory Profiler 的 Allocation 记录适合回答：

- 哪些类创建次数最多。
- 哪些调用栈持续分配对象。
- 分配洪峰是否和 UI 操作、网络解析、图片加载对应。

如果对象数量很高但 retained heap 不高，优先优化分配路径：复用缓冲、减少装箱、避免循环里拼接字符串、避免每帧创建临时集合。

### 用 heap dump 看 retained 大对象

heap dump 适合回答：

- 大数组或大对象由谁持有。
- 缓存是否缺少上限或淘汰策略。
- Activity / Fragment / View 是否间接持有大对象。

如果一个大对象在 dominator tree 里 retained size 很高，优化重点不是减少创建次数，而是缩短持有链或调整缓存策略。

### 用 GC 日志区分分配洪峰和存活增长

观察 GC 日志时，重点看：

- GC 触发原因是否频繁出现 allocation 相关描述。
- freed objects 很多但内存水位回落，偏向短命对象洪峰。
- freed bytes 少且 heap 水位持续上涨，偏向存活对象增长。
- OOM 前是否有多次 GC 重试但仍无法满足分配。

### 用 `dumpsys meminfo` 做归因拆账

执行：

```bash
adb shell dumpsys meminfo <package-name>
```

先拆 Java Heap、Native Heap、Graphics、Code、Stack 等大类。Day 03 的对象分配路径主要解释 Java managed heap 和大对象路径，但实际 OOM 可能由 native 或 graphics 共同推动。

## 面试考点

### TLAB 为什么能提升分配性能？

TLAB 把小对象分配从全局竞争变成线程本地指针移动，减少锁竞争和 allocator 共享状态修改。它提升的是分配快路径性能，不改变对象生命周期，也不代表对象一定属于某个固定年轻代区域。

### bump pointer 为什么快？

bump pointer 只需要检查剩余空间、做对齐、移动指针。它不需要搜索空闲链表，也不需要在分配时处理复杂碎片。它依赖 GC 或 region 管理在后续提供规整空间。

### 大对象为什么要进入 Large Object Space？

大对象会放大普通空间的碎片和移动成本。单独进入 LOS 能让小对象空间保持更好的分配局部性，也让大对象回收和统计更清晰。代价是大对象生命周期过长时，内存压力会非常明显。

### 如何判断问题是分配太快还是对象泄漏？

分配太快通常表现为创建次数高、GC 频繁、GC 后可回收对象多；泄漏或长期持有表现为 full GC 后 retained heap 仍持续增长。要结合 Allocation 记录、GC 日志、heap dump 和 meminfo，而不是只看一次堆大小。

## 参考资料

- AOSP ART：`art/runtime/gc/heap.h`
- AOSP ART：`art/runtime/gc/heap.cc`
- AOSP ART：`art/runtime/thread.h`
- AOSP ART：`art/runtime/gc/space/bump_pointer_space.h`
- AOSP ART：`art/runtime/gc/space/region_space.h`
- AOSP ART：`art/runtime/gc/space/large_object_space.h`
- Android Studio Memory Profiler 官方文档
