#!/usr/bin/env python3
"""Contract checks for the v2.0 Thin-Muscle Operating System."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILL = ROOT / "SKILL.md"
THEORY = ROOT / "references" / "thin-muscle-theory.md"
MANUAL = ROOT / "references" / "operating-manual.md"


def require(text: str, phrase: str, owner: str) -> None:
    if phrase not in text:
        raise SystemExit(f"FAIL: {owner} is missing {phrase!r}")


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    skill = SKILL.read_text(encoding="utf-8")
    theory = THEORY.read_text(encoding="utf-8")
    manual = MANUAL.read_text(encoding="utf-8")

    core = "薄肌是身体版本答案，AI 是时代版本答案。"
    for owner, text in [
        ("README.md", readme),
        ("SKILL.md", skill),
        ("thin-muscle-theory.md", theory),
    ]:
        require(text, core, owner)

    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not frontmatter or 'version: "2.0.0"' not in frontmatter.group(1):
        raise SystemExit("FAIL: metadata.version must be 2.0.0")

    public_docs = {
        "README.md": readme,
        "SKILL.md": skill,
        "thin-muscle-theory.md": theory,
    }
    for owner, text in public_docs.items():
        for exposed_debate in [
            "支持者的最强观点",
            "批评者的最强观点",
            "为什么有人支持，也有人反对",
        ]:
            if exposed_debate in text:
                raise SystemExit(
                    f"FAIL: {owner} still exposes raw debate section {exposed_debate!r}"
                )

    headings = re.findall(r"^##\s+(.+)$", readme, re.MULTILINE)
    if not headings or "薄肌理论 2.0" not in headings[0]:
        raise SystemExit("FAIL: README must open with 薄肌理论 2.0")

    for phrase in [
        "最小充分能力",
        "真肌肉",
        "系统脂肪",
        "结果线条",
        "代谢循环",
        "版本环境",
        "肌薄",
        "脂包肌",
        "镜头肌",
        "过度增肌",
        "薄肌态",
        "薄肌化七步",
        "定性公式",
    ]:
        require(theory, phrase, "thin-muscle-theory.md")

    for domain in ["身体薄肌", "AI 薄肌", "学习薄肌", "职业薄肌", "内容薄肌"]:
        require(theory, domain, "thin-muscle-theory.md")

    for phrase in [
        "薄肌体检",
        "当前体型",
        "版本答案",
        "真正的肌肉",
        "需要减掉的系统脂肪",
        "维护成本",
        "7 天显形动作",
        "版本失效条件",
        "电子减脂",
        "一块肌肉挑战",
    ]:
        require(manual, phrase, "operating-manual.md")

    require(skill, "最小充分能力", "SKILL.md")
    require(skill, "references/operating-manual.md", "SKILL.md")
    require(skill, "薄肌化", "SKILL.md")
    for owner, text in [
        ("README.md", readme),
        ("SKILL.md", skill),
        ("thin-muscle-theory.md", theory),
        ("operating-manual.md", manual),
    ]:
        for phrase in ["## 当前体型", "## 版本答案", "## 维护成本", "## 版本失效条件"]:
            require(text, phrase, owner)
    require(skill, "暂不定型", "SKILL.md")
    require(manual, "暂定组合", "operating-manual.md")

    print("PASS: v2.0 Thin-Muscle Operating System contract")


if __name__ == "__main__":
    main()
