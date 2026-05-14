#!/usr/bin/env python3
"""
Daily Android memory learning document generator with self-evolution.

Each run:
1. Reads all past reflections to build accumulated knowledge context
2. Fetches GitHub Issues for user feedback
3. Calls Claude API to generate a deep technical document
4. Generates a structured reflection that feeds into future runs
5. Commits everything and updates progress
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import anthropic
from github import Github

REPO_ROOT = Path(__file__).parent.parent
PROGRESS_FILE = REPO_ROOT / "progress.json"
DOCS_DIR = REPO_ROOT / "docs"
REFLECTIONS_DIR = REPO_ROOT / "reflections"
README_FILE = REPO_ROOT / "README.md"

WRITING_STYLE = """
你是一位深耕 Android 系统多年的工程师，正在撰写一篇供同行阅读的深度技术文章。

写作规范（必须严格遵守）：
1. 工程师视角先于情绪视角：先讲问题、系统、路径，不讲感受。
2. 技术表达敢写实：类名、方法名、源码路径、AOSP 模块名、参数版本都要具体。
3. 结构感强，标题自己会说话：读者扫标题就知道全文骨架。
4. 判断明确，必须交代依据和边界：给出结论后跟适用条件和范围。
5. 代码块前必须有用途句（这段代码证明什么），代码块后必须有解释句（哪里是关键，如何和上文对应）。
6. 列表项必须自带信息增量，不能只写名词。
7. 结尾克制：压缩结论、补边界、给延伸阅读，不做空洞升华。

禁止使用：
- 赋能、闭环、底座、抓手、落地、沉淀、打通、心智等大厂黑话
- 说实话、老实说、重要的是、有趣的是、值得注意的是等 AI 套话
- 随着技术的不断发展、在当今社会等填充开头
- 不是 A 而是 B 这种句式（全文最多 2 次）
- 接下来我将、让我们来探讨等元叙述
- 英文单词两侧必须有半角空格
"""


def load_progress() -> dict:
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(data: dict):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_reflections() -> list[dict]:
    """Load all past reflection files, sorted by day number."""
    REFLECTIONS_DIR.mkdir(exist_ok=True)
    reflections = []
    for path in sorted(REFLECTIONS_DIR.glob("day*.json")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                reflections.append(json.load(f))
        except Exception:
            pass
    return reflections


def build_knowledge_context(reflections: list[dict]) -> str:
    """Summarize accumulated knowledge from past reflections for the next generation."""
    if not reflections:
        return ""

    lines = ["已完成的学习记录（用于建立知识连贯性，避免重复，并深化已识别的薄弱点）：\n"]
    for r in reflections[-10:]:  # 最近 10 篇，避免 context 过长
        lines.append(f"Day {r['day']}《{r['title']}》：")
        if r.get("key_conclusions"):
            lines.append(f"  核心结论：{'; '.join(r['key_conclusions'][:3])}")
        if r.get("shallow_points"):
            lines.append(f"  覆盖较浅、值得后续深入：{'; '.join(r['shallow_points'])}")
        if r.get("discovered_connections"):
            lines.append(f"  发现的关联知识点：{'; '.join(r['discovered_connections'])}")
        lines.append("")

    # Collect all pending deep-dive suggestions
    pending_deep_dives = []
    for r in reflections:
        pending_deep_dives.extend(r.get("suggest_future_topics", []))
    if pending_deep_dives:
        lines.append(f"历史反思中建议未来深入的方向：{'; '.join(set(pending_deep_dives[-15:]))}")

    return "\n".join(lines)


def get_github_feedback(repo_name: str, token: str) -> list[dict]:
    g = Github(token)
    repo = g.get_repo(repo_name)
    feedback = []
    for issue in repo.get_issues(state="open"):
        if not issue.pull_request:
            feedback.append({
                "number": issue.number,
                "title": issue.title,
                "body": issue.body or "",
            })
    return feedback


def close_issues(repo_name: str, token: str, issue_numbers: list[int]):
    g = Github(token)
    repo = g.get_repo(repo_name)
    for num in issue_numbers:
        issue = repo.get_issue(num)
        issue.create_comment("已在今日文档中融入该反馈，感谢！")
        issue.edit(state="closed")


def generate_document_and_reflection(
    day_info: dict,
    knowledge_context: str,
    feedback: list[dict],
) -> tuple[str, dict]:
    """Generate document + structured reflection in a single API call."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    feedback_section = ""
    if feedback:
        lines = ['用户反馈（自然融入文章，不单列「用户反馈」节）：']
        for item in feedback:
            lines.append(f"- {item['title']}: {item['body'][:200]}")
        feedback_section = "\n".join(lines)

    prompt = f"""为《Android 内存专家养成计划》系列写第 {day_info['day']} 篇文章。

主题：{day_info['title']}
这是第 {day_info['week']} 周内容，系列第 {day_info['day']}/60 篇。

{knowledge_context}

{feedback_section}

---

请输出两个部分，用以下分隔符隔开：

===DOCUMENT===
（此处写正文文章，结构如下）

# Day {day_info['day']}：{day_info['title']}

> 系列第 {day_info['day']} 篇。[一句话说明本篇覆盖什么、读者能带走什么判断]

## 背景

[为什么这个主题值得单独讲；在 Android 内存体系中处于什么位置；与前面知识点的关联]

## 核心机制

[原理讲解：先给全景图，再下钻细节；附关键 AOSP 源码路径分析，写出具体类名和方法名]

## 代码示例

[可运行代码或明确说明是节选；代码前有用途句，代码后有解释句]

## 常见问题与误判

[实际工程中最容易踩的坑；给出判断依据]

## 观测方法

[用什么工具、看什么指标、执行什么命令能验证上述机制]

## 面试考点

[该主题在面试中的高频问法；给出有依据的答题思路]

## 参考资料

[AOSP 源码路径 / 官方文档 / 推荐延伸阅读]

===REFLECTION===
（此处输出结构化反思，严格 JSON 格式，用于指导后续文章）

{{
  "day": {day_info['day']},
  "title": "{day_info['title']}",
  "key_conclusions": ["本篇最重要的 3-5 个技术结论，一句话每条"],
  "shallow_points": ["本篇覆盖较浅、值得未来深入的子话题"],
  "discovered_connections": ["写作过程中发现的、与其他内存主题的关联点"],
  "suggest_future_topics": ["建议在后续文章中补充的相关知识点"],
  "knowledge_gaps": ["写这篇时发现自己还不够确定的技术细节"]
}}
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=WRITING_STYLE,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text

    # Split document and reflection
    if "===REFLECTION===" in raw:
        doc_part, reflection_part = raw.split("===REFLECTION===", 1)
        doc_part = doc_part.replace("===DOCUMENT===", "").strip()
    else:
        doc_part = raw.replace("===DOCUMENT===", "").strip()
        reflection_part = "{}"

    # Parse reflection JSON
    try:
        json_match = re.search(r'\{[\s\S]*\}', reflection_part)
        reflection_data = json.loads(json_match.group()) if json_match else {}
    except Exception:
        reflection_data = {"day": day_info["day"], "title": day_info["title"]}

    return doc_part, reflection_data


def save_document(day_info: dict, content: str) -> Path:
    week_dir = DOCS_DIR / f"week-{day_info['week']:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)
    filename = f"day{day_info['day']:02d}-{day_info['slug']}.md"
    filepath = week_dir / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def save_reflection(reflection_data: dict):
    REFLECTIONS_DIR.mkdir(exist_ok=True)
    day = reflection_data.get("day", 0)
    filepath = REFLECTIONS_DIR / f"day{day:02d}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(reflection_data, f, ensure_ascii=False, indent=2)


def update_readme(day_info: dict, doc_path: Path):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    relative_path = doc_path.relative_to(REPO_ROOT).as_posix()
    today = datetime.now().strftime("%Y-%m-%d")
    new_line = f"| Day {day_info['day']:02d} | {day_info['title']} | ✅ [{today}]({relative_path}) |"

    content = re.sub(
        rf"\| Day {day_info['day']:02d} \|.*",
        new_line,
        content,
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    gh_token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY", "hello-he/android-memory-expert")

    progress = load_progress()
    current_day = progress["current_day"]

    if current_day > progress["total_days"]:
        print("60 天课程已全部完成！")
        sys.exit(0)

    curriculum = progress["curriculum"]
    day_info = next((d for d in curriculum if d["day"] == current_day), None)
    if not day_info:
        print(f"找不到第 {current_day} 天的课程配置")
        sys.exit(1)

    print(f"生成第 {current_day} 天文档：{day_info['title']}")

    # Load accumulated knowledge from past reflections
    reflections = load_all_reflections()
    knowledge_context = build_knowledge_context(reflections)
    print(f"读取到 {len(reflections)} 篇历史反思记录")

    # Fetch user feedback from Issues
    feedback = []
    processed_issue_numbers = []
    if gh_token:
        try:
            feedback = get_github_feedback(repo_name, gh_token)
            processed_issue_numbers = [f["number"] for f in feedback]
            print(f"读取到 {len(feedback)} 条用户反馈")
        except Exception as e:
            print(f"读取 Issues 失败（跳过）：{e}")

    # Generate document + reflection
    content, reflection_data = generate_document_and_reflection(
        day_info, knowledge_context, feedback
    )

    # Save outputs
    doc_path = save_document(day_info, content)
    print(f"文档已保存：{doc_path}")

    save_reflection(reflection_data)
    print(f"反思记录已保存：reflections/day{current_day:02d}.json")

    # Update README progress
    update_readme(day_info, doc_path)

    # Update progress.json
    progress["current_day"] = current_day + 1
    progress["last_generated"] = datetime.now().isoformat()
    save_progress(progress)

    # Close processed Issues
    if gh_token and processed_issue_numbers:
        try:
            close_issues(repo_name, gh_token, processed_issue_numbers)
            print(f"已关闭 {len(processed_issue_numbers)} 个 Issues")
        except Exception as e:
            print(f"关闭 Issues 失败（跳过）：{e}")

    next_day = current_day + 1
    if next_day <= progress["total_days"]:
        next_topic = next((d["title"] for d in curriculum if d["day"] == next_day), "")
        print(f"完成。明天将生成：Day {next_day}《{next_topic}》")
    else:
        print("60 天全部完成！")


if __name__ == "__main__":
    main()
