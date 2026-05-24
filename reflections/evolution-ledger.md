# 自我进化账本

这个文件记录系统如何从“前一天的反思”改进到“下一篇文章”。它不是文章正文的一部分，而是给后续自动化读取的约束：**生成前必须先读这里 + 最近的 dayXX.json；生成后必须更新这里**。

---

## 当前问题（会被持续追踪，直到被解决/降级为边界）

- GitHub Issues 反馈链路尚未打通：`gh` 未认证时只能记录 blocker（不要假装读到了 Issues）。
- 发布链路不稳定：历史上出现过 `.git/index.lock: Permission denied` 导致无法 `git add/commit`（需要在每次运行时优先验证）。
- 用户反馈偏好明确：**多图少文字**，减少长段解释，提高可扫读与复盘效率。

---

## 已形成的长期约束（写作与工程证据）

- 结论必须落到“可观测证据链”：`dumpsys meminfo`、`/proc/<pid>/maps`、GC 日志、heap dump、allocation 视图、AOSP 路径等。
- 涉及 ART 内存时优先使用 `space + collector + allocator` 的解释视角，不直接套 HotSpot 术语。
- 每篇文章至少承接一个历史 reflection 中的 `shallow_points` / `knowledge_gaps` / `suggest_future_topics`，并在新 reflection 的 `applied_reflections` 与 `visible_changes` 写清楚“怎么落地的”。
- 每篇文章至少 2 张 Mermaid：一张讲核心结构/执行路径；一张讲排障决策流。
- 遇到无法验证的版本差异、ROM 差异或工具权限问题，必须明确记录边界与 blocker。

---

## 运行记录（Day N-1 → Day N）

### Day 01 → Day 02

- 应用的前一日反思：减少 HotSpot 分代术语的误导，转向 ART 的 space/collector 视角。
- 可见变化：加入 Dalvik/ART 对照框架，把“现象”落到“可验证的约束与拆账口径”。
- 未解决：不同 Android 大版本默认 collector/space 组合仍未系统梳理。

### Day 02 → Day 03

- 应用的前一日反思：把“分配快路径”写成可执行排查清单，而不是概念解释。
- 可见变化：围绕 TLAB / bump pointer / LOS 结构化输出，并补上 Allocation/GC/heap dump 的观测关系。
- 未解决：TLAB refill、LOS 阈值、region space 默认配置仍需按 Android 版本核对。

### Day 03 → Day 04

- 应用的前一日反思：承接“分配路径”，补齐“可达性/GC Roots”与栈/JNI 边界，并强化“多图少文”。
- 可见变化：新增结构图（Thread 栈/帧/JNI refs → managed heap）+ 决策流（怀疑栈持有导致不回收时的排障路径）+ 多张短表替代长段解释。
- 未解决：不同 Android 版本下 stack map 与 root 枚举的差异仍未按版本核对；Issues 仍未可读；历史上出现过 `.git/index.lock` 权限问题。

### Day 04 → Day 05

- 应用的前一日反思：继续坚持“证据链写法”，把 dex/oat/vdex/class metadata/JIT code cache 的可观测信号对齐到 `meminfo/maps/对比实验`。
- 可见变化：Day 05 新增两张 Mermaid（结构图 + 决策流），并新增“现象→机制→证据→结论句式”的对照表，以及 `maps` 两次采样 diff 的可执行命令（明显减少纯概念段落）。
- 未解决：`gh auth` 仍未完成（无法读 open Issues）；发布链路需验证 `.git/index.lock` 是否仍会阻塞 `git add/commit/push`。

### Day 05 → Day 06

- 应用的前一日反思：继续用证据链解释 String/intern，把判断落到 heap dump、Allocation 视图、retained size、重复内容和生命周期。
- 可见变化：Day 06 新增两张 Mermaid（InternTable 结构图 + 是否值得 intern 的决策流），并用适用场景表、heap dump 证据表、A/B 实验表替代长段概念解释。
- 未解决：`gh auth` 仍未完成；String backing storage、InternTable 与 GC 的交互边界仍需按 Android 版本核对。

---

## 下一次必须执行（面向 Day 07）

- Day 07（对象头结构与 Mark Word）：继续多图少文字，至少画出对象头、klass 指针、锁状态、GC 标记/移动相关信息之间的关系图。
- 必须明确 Android ART 与 HotSpot Mark Word 术语的边界，避免把 HotSpot 对象头模型硬套到 ART。
- 如果 `gh` 仍未认证：在 reflection 的 `issue_feedback` 和 automation memory 里明确记录 blocker（包含建议的解决方式：`gh auth login` / `GH_TOKEN`）。
- 生成后务必先跑一遍 JSON 校验，再尝试 `git status/add/commit/push`；若仍被 `.git/index.lock` 阻塞，记录“具体错误 + 需要的修复动作”。
