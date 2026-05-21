# Android 内存专家养成计划

每天自动生成一篇深度技术文档，60 天系统覆盖 Android 内存核心知识体系。

由 Codex 自动化任务驱动，无需手动操作，每天北京时间 08:00 自动更新。

**有想法？在这里开一个 [Issue](../../issues/new)，第二天的文档会融入你的反馈。**

---

## 学习进度

| 文章 | 主题 | 状态 |
|------|------|------|
| Day 01 | Java 堆结构：Young/Old Generation 在 ART 上的实现 | ✅ [2026-05-19](docs/week-01/day01-art-heap-structure.md) |
| Day 02 | ART 与 Dalvik 的内存分配差异 | ✅ [2026-05-20](docs/week-01/day02-art-vs-dalvik-memory.md) |
| Day 03 | 对象分配路径：TLAB、bump pointer、Large Object Space | ✅ [2026-05-21](docs/week-01/day03-object-allocation-path.md) |
| Day 04 | 栈内存与帧结构 | ⏳ 待生成 |
| Day 05 | 方法区与元数据空间（Metaspace） | ⏳ 待生成 |
| Day 06 | String 常量池与 intern() 机制 | ⏳ 待生成 |
| Day 07 | 对象头结构与 Mark Word | ⏳ 待生成 |
| Day 08 | 引用类型：强引用、软引用、弱引用、虚引用 | ⏳ 待生成 |
| Day 09 | ART GC 算法：CMS 与 CC（Concurrent Copying） | ⏳ 待生成 |
| Day 10 | GC Roots 枚举与可达性分析 | ⏳ 待生成 |
| Day 11 | ART GC 源码：gc/collector/ 目录关键路径 | ⏳ 待生成 |
| Day 12 | GC 触发时机：alloc gc、background gc、explicit gc | ⏳ 待生成 |
| Day 13 | GC pause 的来源与优化思路 | ⏳ 待生成 |
| Day 14 | Generational GC 在 ART 中的实现 | ⏳ 待生成 |
| Day 15 | 内存泄漏的本质：GC Roots 持有链分析 | ⏳ 待生成 |
| Day 16 | Activity/Fragment 泄漏的常见模式 | ⏳ 待生成 |
| Day 17 | Handler 泄漏：消息队列与生命周期的冲突 | ⏳ 待生成 |
| Day 18 | 静态持有、单例泄漏的排查路径 | ⏳ 待生成 |
| Day 19 | Listener 未注销与匿名内部类泄漏 | ⏳ 待生成 |
| Day 20 | Cursor、Stream 等资源未关闭的泄漏场景 | ⏳ 待生成 |
| Day 21 | LeakCanary 源码：如何检测泄漏引用链 | ⏳ 待生成 |
| Day 22 | Android Studio Memory Profiler 核心操作 | ⏳ 待生成 |
| Day 23 | Heap Dump 分析：hprof 文件结构 | ⏳ 待生成 |
| Day 24 | MAT（Memory Analyzer Tool）入门与实战 | ⏳ 待生成 |
| Day 25 | MAT Dominator Tree 与 Retained Heap 解读 | ⏳ 待生成 |
| Day 26 | Allocation Tracker 与对象分配热点定位 | ⏳ 待生成 |
| Day 27 | dumpsys meminfo 输出字段解读：PSS/RSS/VSS | ⏳ 待生成 |
| Day 28 | adb shell procrank 与系统内存全局视图 | ⏳ 待生成 |
| Day 29 | JNI 内存管理：Local Reference 与 Global Reference | ⏳ 待生成 |
| Day 30 | NewByteArray / NewDirectByteBuffer 的内存归属 | ⏳ 待生成 |
| Day 31 | Native Heap：malloc/free 与 jemalloc | ⏳ 待生成 |
| Day 32 | AddressSanitizer（ASan）检测 Native 内存错误 | ⏳ 待生成 |
| Day 33 | /proc/<pid>/maps 解读：内存映射全貌 | ⏳ 待生成 |
| Day 34 | mmap 与匿名映射：ByteBuffer.allocateDirect() 的底层 | ⏳ 待生成 |
| Day 35 | Native 内存泄漏的排查工具链 | ⏳ 待生成 |
| Day 36 | Bitmap 内存模型：Android 8.0 前后的变化 | ⏳ 待生成 |
| Day 37 | Bitmap 像素数据在 Native 堆的存储机制 | ⏳ 待生成 |
| Day 38 | BitmapFactory.Options：inSampleSize、inBitmap 的内存影响 | ⏳ 待生成 |
| Day 39 | Glide 内存缓存架构：LruCache + BitmapPool | ⏳ 待生成 |
| Day 40 | 大图加载策略：BitmapRegionDecoder 分块解码 | ⏳ 待生成 |
| Day 41 | 硬件加速与 Bitmap 的 GPU 内存占用 | ⏳ 待生成 |
| Day 42 | 图片内存泄漏场景与 Weak Reference 的正确使用 | ⏳ 待生成 |
| Day 43 | Android 进程内存限制：ActivityManager.getMemoryClass() | ⏳ 待生成 |
| Day 44 | LMK（Low Memory Killer）机制与 adj 值 | ⏳ 待生成 |
| Day 45 | onTrimMemory() 回调等级与响应策略 | ⏳ 待生成 |
| Day 46 | onLowMemory() 与系统内存压力信号 | ⏳ 待生成 |
| Day 47 | Zram 与内存压缩在 Android 上的应用 | ⏳ 待生成 |
| Day 48 | 共享内存：Ashmem 与 MemoryFile | ⏳ 待生成 |
| Day 49 | 进程间内存隔离：每个 App 的内存视图 | ⏳ 待生成 |
| Day 50 | 内存优化全局方法论：观测 → 定位 → 验证 | ⏳ 待生成 |
| Day 51 | 启动阶段内存控制：冷启动内存峰值分析 | ⏳ 待生成 |
| Day 52 | RecyclerView 内存优化：ViewHolder 复用机制 | ⏳ 待生成 |
| Day 53 | 多进程架构的内存收益与代价 | ⏳ 待生成 |
| Day 54 | ProGuard/R8 对内存的影响 | ⏳ 待生成 |
| Day 55 | 面试高频：GC 机制、内存泄漏、OOM 排查 | ⏳ 待生成 |
| Day 56 | 面试高频：Bitmap 内存、LMK、Native 内存 | ⏳ 待生成 |
| Day 57 | AOSP 源码阅读路径：内存相关核心模块索引 | ⏳ 待生成 |
| Day 58 | 综合实战：一次完整的内存问题排查复盘 | ⏳ 待生成 |
| Day 59 | Android 版本演进中的内存变化（5.0→15） | ⏳ 待生成 |
| Day 60 | 总结：Android 内存专家的知识图谱 | ⏳ 待生成 |

---

## 系统架构

```
Codex 自动化任务 (每天 08:00 北京时间)
    ↓
读取 progress.json → 今日主题
    ↓
读取 reflections/ → 已有知识积累与待深入点
    ↓
读取 open Issues → 用户反馈
    ↓
Codex 生成深度文档 + 自我反思记录
    ↓
commit & push → 关闭已处理 Issues
```

## 自我进化机制

每次生成后都会写入 `reflections/dayXX.json`，并维护 `reflections/evolution-ledger.md`。后续任务必须先读取最近反思和进化账本，再生成下一篇文章。

可见改进要求：

- 每篇文章至少承接一个历史反思中的薄弱点、知识缺口或未来主题建议。
- 每次反思必须写明 `applied_reflections`、`visible_changes` 和 `next_run_instructions`。
- 不能确认的版本差异、厂商差异、Issue 权限问题，必须作为边界记录下来。

## 写作规范

文档遵循 [gracker-writing](https://github.com/Gracker/gracker-writing) skill：工程师视角、技术精确、无 AI 套话、代码前后必须有说明句。

视觉表达优先：

- 多图少文字；优先用 Mermaid 图、表格、流程清单解释结构、路径和判断过程。
- 每篇文章至少包含 2 张 Mermaid 图，覆盖核心机制和排查路径。
- 长段落要拆短，避免连续大段文字；文字只补充图里表达不清的边界、依据和版本差异。
- 复杂流程优先画成 flowchart 或 sequence diagram，内存结构优先画成分层图或对照表。
