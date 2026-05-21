# 自我进化账本

这个文件记录学习系统如何从前一天的反思中改进下一篇文章。它不是文章正文的一部分，而是给后续自动化读取的约束：每次生成前必须先看这里和最近的 `dayXX.json`，生成后必须更新这里。

## 当前问题

- Day 01 到 Day 03 已经生成了结构化反思，但反思没有形成强制执行项。
- 文章之间有主题延续，但读者很难看出“上一篇发现的薄弱点，下一篇如何补上”。
- GitHub Issues 反馈链路尚未打通，`gh` 未认证时只能记录 blocker。
- 用户反馈：文章需要多图、少文字，减少长段解释，提升扫读和复盘效率。

## 已形成的长期约束

- 后续文章不能只复述概念，必须把结论落到可观察证据：GC 日志、`dumpsys meminfo`、heap dump、Allocation 视图或 AOSP 路径。
- 涉及 ART 内存时，优先使用 `space + collector + allocator` 组合解释，不直接套 HotSpot 的年轻代/老年代模型。
- 每篇文章至少承接一个历史反思里的 `shallow_points`、`knowledge_gaps` 或 `suggest_future_topics`，并在新的 reflection 中写明承接点。
- 遇到无法验证的版本差异、厂商 ROM 差异或工具权限问题，必须明确记录边界，不假装已经确认。
- 每篇文章至少包含 2 张 Mermaid 图：一张解释核心结构或运行路径，一张解释排查/判断流程。
- 长段文字必须拆短；能用图、表格、对照清单表达的内容，不写成连续段落。

## 运行记录

### Day 01 -> Day 02

- Day 01 发现：需要减少 HotSpot 分代术语带来的误导，转向 ART 的 space/collector 视角。
- Day 02 应用：用 Dalvik/ART 对照框架强化“执行模型 -> 堆组织 -> 分配快路径 -> 整理能力”的解释路径。
- 仍未解决：不同 Android 大版本默认 collector 和 space 组合尚未系统化梳理。

### Day 02 -> Day 03

- Day 02 发现：Day 03 应把“分配快路径”写成可执行的排查清单。
- Day 03 应用：补充 TLAB、bump pointer、Large Object Space 与 Allocation/GC 日志/heap dump 的观测关系。
- 仍未解决：TLAB refill、LOS 阈值、region space 默认配置仍需要按 Android 版本核对。

## 下一次必须执行

- Day 04《栈内存与帧结构》需要承接 Day 03 的分配路径主题，解释“栈帧、局部变量表、引用可达性”和 GC Roots 的关系。
- Day 04 不能只写 JVM 栈概念，必须说明 ART 线程栈、JNI 栈、本地调用和 Java 对象引用之间的边界。
- Day 04 必须使用多图少文字结构：至少画出“线程栈/栈帧/局部引用/managed heap”的关系图，以及“局部引用如何成为 GC Root”的判断流程图。
- Day 04 的 reflection 必须新增字段：
  - `applied_reflections`
  - `visible_changes`
  - `next_run_instructions`
