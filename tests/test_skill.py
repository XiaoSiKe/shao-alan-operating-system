#!/usr/bin/env python3
"""Static acceptance checks for the packaged Agent Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
RESEARCH = ROOT / "references" / "research"
EXPECTED_NAME = "shao-alan-operating-system"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")

    text = SKILL.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter:
        fail("valid YAML-style frontmatter was not found")

    meta = frontmatter.group(1)
    name_match = re.search(r"^name:\s*([^\n]+)$", meta, re.MULTILINE)
    if not name_match:
        fail("frontmatter.name is missing")

    name = name_match.group(1).strip()
    if name != EXPECTED_NAME:
        fail(f"name {name!r} must be {EXPECTED_NAME!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("name must contain lowercase letters, digits, and single hyphens only")

    desc_match = re.search(
        r"^description:\s*\|\n(?P<body>(?:^[ \t]+.*\n?)+)", meta, re.MULTILINE
    )
    if not desc_match:
        fail("frontmatter.description block is missing")
    description = "\n".join(
        line.strip() for line in desc_match.group("body").splitlines()
    ).strip()
    if not 1 <= len(description) <= 1024:
        fail(f"description length must be 1..1024 characters; got {len(description)}")

    required_phrases = [
        "薄肌是身体版本答案，AI 是时代版本答案。",
        "AI 薄肌版",
        "表达DNA",
        "版本答案引擎",
        "版本失效条件",
        "幽默是 UI，不是邵艾伦的人格证据",
        "项目交互语气：幽默 UI",
        "诚实边界",
        "框架推断",
        "非本人",
        "退出角色",
        "回答工作流",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"required phrase/section missing: {phrase}")

    version_match = re.search(r'^\s*version:\s*"([^"]+)"$', meta, re.MULTILINE)
    if not version_match or version_match.group(1) != "1.2.0":
        fail("metadata.version must be 1.2.0")

    if len(text.splitlines()) >= 500:
        fail("SKILL.md should remain below 500 lines")

    if (ROOT / EXPECTED_NAME).exists():
        fail("legacy nested skill directory still exists")

    engine = ROOT / "references" / "version-answer-engine.md"
    if not engine.exists() or engine.stat().st_size < 1000:
        fail("version answer engine is missing or too small")

    if "搏击" in text:
        fail("obsolete combat concept leaked into SKILL.md")

    model_section = re.search(
        r"## 核心心智模型\n(?P<body>.*?)(?=\n## )", text, re.DOTALL
    )
    if not model_section:
        fail("核心心智模型 section is missing")
    model_count = len(re.findall(r"^### 模型\d+", model_section.group("body"), re.MULTILINE))
    if not 3 <= model_count <= 7:
        fail(f"mental model count must be 3..7; got {model_count}")

    research_names = [
        "writings",
        "conversations",
        "expression-dna",
        "external-views",
        "decisions",
        "timeline",
    ]
    for index, research_name in enumerate(research_names, start=1):
        expected = RESEARCH / f"0{index}-{research_name}.md"
        if not expected.exists() or expected.stat().st_size < 200:
            fail(f"research file missing or too small: {expected.relative_to(ROOT)}")

    print("PASS: skill packaging and static acceptance checks")


if __name__ == "__main__":
    main()
