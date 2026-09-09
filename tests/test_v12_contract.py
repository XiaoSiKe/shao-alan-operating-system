#!/usr/bin/env python3
"""Contract checks for the v1.2 README and version-answer engine."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, phrase: str, owner: str) -> None:
    if phrase not in text:
        raise SystemExit(f"FAIL: {owner} is missing {phrase!r}")


def check_relative_links(text: str, source: Path) -> None:
    # Match both ordinary links and the outer link around badge images.
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_text = unquote(target.split("#", 1)[0]).strip("<>")
        if not path_text:
            continue
        resolved = (source.parent / path_text).resolve()
        if not resolved.exists():
            raise SystemExit(
                f"FAIL: broken relative link in {source.name}: {target!r}"
            )


def main() -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    engine = (ROOT / "references" / "version-answer-engine.md").read_text(
        encoding="utf-8"
    )
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    core = "薄肌是身体版本答案，AI 是时代版本答案。"
    for owner, text in [("SKILL.md", skill), ("engine", engine), ("README", readme)]:
        require(text, core, owner)

    for phrase in [
        "环境 E",
        "角色 R",
        "目标 G",
        "约束 C",
        "证据 K",
        "时代顺风",
        "角色适配",
        "反馈速度",
        "复利价值",
        "可逆性",
        "版本失效条件",
    ]:
        require(engine, phrase, "version-answer-engine.md")

    for phrase in [
        "六个人物心智模型",
        "AI 模块",
        "版本答案引擎",
        "幽默 UI",
        "项目是否好笑由下面的幽默 UI 决定",
    ]:
        require(skill, phrase, "SKILL.md")

    if readme.count("img.shields.io") < 5:
        raise SystemExit("FAIL: README should expose at least five badges")
    if not readme.startswith('<div align="center">'):
        raise SystemExit("FAIL: README hero is not centered")
    for icon in ["💪", "🧬", "🩻", "🧭", "⚙️", "🎮", "🎬", "🤖", "🧠", "🎭", "🛡️", "📦", "🧪", "🔎"]:
        require(readme, icon, "README.md")

    old_paths = re.findall(r"shao-alan-operating-system/(?:SKILL|references|scripts|tests)", readme)
    if old_paths:
        raise SystemExit(f"FAIL: README still contains legacy nested paths: {old_paths}")

    require(readme, "npx skills add XiaoSiKe/shao-alan-operating-system", "README.md")
    require(readme, "FIDELITY.md", "README.md")

    check_relative_links(readme, ROOT / "README.md")
    check_relative_links(skill, ROOT / "SKILL.md")

    print("PASS: v1.2 version-answer and README contracts")


if __name__ == "__main__":
    main()
