# 自我进化账本

这个文件记录系统如何从“前一天的反思”改进到“下一篇文章”。它不是正文的一部分，而是给后续自动化读取的约束：**生成前必须先读这里 + 最近的 dayXX.json；生成后必须更新这里**。

---

## 当前问题（持续追踪，直到解决或明确降级为边界）

- GitHub Issues 反馈链路未打通：`gh` 未认证时只能记录 blocker，不能假装已经读到了 open Issues。
- 发布链路不稳定：历史上出现过 `.git/index.lock: Permission denied`，每次运行都要复核 `.git` 可写与 git 认证状态。
- 用户反馈长期偏好明确：**多图少文**，优先 Mermaid、表格、对照矩阵、短 checklist。

---

## 长期写作约束

- 结论必须落到可观测证据：`dumpsys meminfo`、`/proc/<pid>/maps`、GC 日志、heap dump、Allocation 视图、AOSP 路径。
- 涉及 ART 时优先使用 `space + collector + allocator + root path` 的解释视角，不直接套 HotSpot 术语。
- 每篇文章至少承接一个历史 reflection 中的 `shallow_points`、`knowledge_gaps`、`suggest_future_topics` 或 `next_run_instructions`，并在新 reflection 的 `applied_reflections` 与 `visible_changes` 里写清楚怎么落地。
- 每篇文章至少 2 张 Mermaid：一张讲核心结构或执行路径，一张讲排障/决策流。
- 遇到无法核实的版本差异、ROM 差异、权限问题，必须明确写成边界或 blocker。

---

## 运行记录（Day N-1 -> Day N）

### Day 01 -> Day 02
- 应用的前一日反思：减少 HotSpot 分代术语误导，转向 ART 的 `space / collector` 视角。
- 可见变化：加入 Dalvik / ART 对照框架，把现象落到可验证约束与内存拆账口径。
- 未解决：不同 Android 版本默认 collector / space 组合仍待系统梳理。

### Day 02 -> Day 03
- 应用的前一日反思：把“分配快路径”写成可执行排查清单，而不是概念解释。
- 可见变化：围绕 `TLAB / bump pointer / LOS` 输出结构图，并补了 Allocation / GC / heap dump 的观察关系。
- 未解决：TLAB refill、LOS 阈值、region space 默认配置仍需按 Android 版本核对。

### Day 03 -> Day 04
- 应用的前一日反思：承接“分配路径”，补齐“可达性 / GC Roots”与栈 / JNI 边界，并强化“多图少文”。
- 可见变化：新增结构图（Thread 栈帧 / JNI refs -> managed heap）和排障流，用多张短表替代长段解释。
- 未解决：不同 Android 版本中的 stack map / root 枚举差异仍未按版本核对；Issues 与 git 提交链路都存在历史 blocker。

### Day 04 -> Day 05
- 应用的前一日反思：继续坚持“证据链写法”，把 dex / oat / vdex / class metadata / JIT code cache 对齐到 `meminfo / maps / 对比实验`。
- 可见变化：新增 2 张 Mermaid（结构图 + 决策流），并补了 `maps` diff 的可执行命令。
- 未解决：`gh auth` 未完成，`.git/index.lock` 风险需要在提交阶段反复验证。

### Day 05 -> Day 06
- 应用的前一日反思：继续用证据链解释 String / intern，把判断落到 heap dump、Allocation 视图、retained size、生命周期。
- 可见变化：新增 InternTable 结构图和 “是否值得 intern” 决策流，并用短表替代长段解释。
- 未解决：`gh auth` 仍未完成；String backing storage、InternTable 与 GC 的版本边界仍待核对。

### Day 06 -> Day 07
- 应用的前一日反思：明确 ART 与 HotSpot Mark Word 的术语边界，把对象头问题落到 `mirror::Object`、class 信息、LockWord/Monitor、GC 扫描与证据链。
- 可见变化：新增 3 张 Mermaid（ART 对象模型、HotSpot/ART 边界、排障流），并补了 AOSP 入口表。
- 未解决：对象头字段、lock word 编码、read barrier 与 collector 组合仍需按目标 Android 分支核对。

### Day 07 -> Day 08
- 应用的前一日反思：承接“对象是否回收由可达性 + 引用链决定”，要求画出引用强度 / 可达性层级图与 `ReferenceQueue` 决策流。
- 可见变化：Day 08 新增 2 张 Mermaid（可达性层级 + `ReferenceQueue` 结构图、排障决策流），并用多张短表响应“多图少文”。
- 未解决：`gh issue list` 仍受阻；`reference_processor` 的版本差异与 A/B 数据仍未补齐。

### Day 08 -> Day 09
- 应用的前一日反思：严格执行“多图少字 + 证据链”，把 GC 算法讨论落到执行路径图、排障决策流、命令块和 AOSP 路径。
- 可见变化：Day 09 新增 2 张 Mermaid（CMS vs CC 执行路径、Troubleshooting 决策流），并新增对比矩阵与证据链表。
- 未解决：`gh issue list` 仍受阻；仓库可能仍有 `.git/index.lock: Permission denied` 风险，提交阶段必须复核。

### Day 09 -> Day 10
- 应用的前一日反思：把“回收少 -> 强可达链”真正落到 Day 10 的 root 证据链，新增 roots 分类结构图、MAT / heap dump 操作清单与 root 类型到修复动作的对照表。
- 可见变化：Day 10 新增 3 张 Mermaid（GC Roots 分类结构图、heap dump 证据流、Troubleshooting 决策流），并新增 roots 分类速查表、MAT 视图清单、排障矩阵，继续响应“多图少文”。
- 未解决：GitHub Issues 仍因 `gh` 未认证无法读取；具体 Android 分支上的 root 枚举实现细节仍需在后续源码篇按目标版本核对。

---

## 下一次必须执行（面向 Day 11）

- Day 11（ART GC 源码：`gc/collector/` 目录关键路径）继续保持“多图少文 + 工程入口表”，最好画出 `heap -> collector -> root visitor -> reference processor` 的目录关系图。
- 继续把结论落到可观测入口：日志字段、trace 线程、AOSP 文件路径、命令模板。
- 如果 `gh` 仍未认证：继续在 reflection 的 `issue_feedback` 与 automation memory 记录 blocker，并提示 `gh auth login` 或设置 `GH_TOKEN`。
- 生成后先校验 JSON，再尝试 `git status/add/commit/push`；若遇到 `.git/index.lock`、权限或远端鉴权问题，记录“具体命令 + 原始报错 + 可复现修复路径”。
