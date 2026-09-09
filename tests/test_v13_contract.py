#!/usr/bin/env python3
"""Contract checks for the v1.3 thin-muscle-centered release."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILL = ROOT / "SKILL.md"
THEORY = ROOT / "references" / "thin-muscle-theory.md"
ENGINE = ROOT / "references" / "version-answer-engine.md"


def require(text: str, phrase: str, owner: str) -> None:
    if phrase not in text:
        raise SystemExit(f"FAIL: {owner} is missing {phrase!r}")


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    skill = SKILL.read_text(encoding="utf-8")
    engine = ENGINE.read_text(encoding="utf-8")

    banned_readme_phrases = [
        "基于邵艾伦公开内容蒸馏的人物操作系统；AI 模块、版本答案引擎与幽默语气为项目原创。",
        "身体要有训练痕迹，AI 要有交付痕迹。",
        "保留不能外包的身体，掌握可以外接的智能。",
    ]
    for phrase in banned_readme_phrases:
        if phrase in readme:
            raise SystemExit(f"FAIL: deleted README copy returned: {phrase}")

    headings = re.findall(r"^##\s+(.+)$", readme, re.MULTILINE)
    if not headings or "薄肌理论" not in headings[0]:
        raise SystemExit("FAIL: README's first main module must explain 薄肌理论")

    if not THEORY.exists() or THEORY.stat().st_size < 2000:
        raise SystemExit("FAIL: references/thin-muscle-theory.md is missing or too small")
    theory = THEORY.read_text(encoding="utf-8")

    for phrase in [
        "本人主张",
        "支持者的最强观点",
        "批评者的最强观点",
        "薄肌理论修正版",
        "不能声称",
        "回答协议",
        "薄肌不是独立的生理学分类",
    ]:
        require(theory, phrase, "thin-muscle-theory.md")

    require(skill, "references/thin-muscle-theory.md", "SKILL.md")
    require(skill, "薄肌争议校准器", "SKILL.md")
    require(engine, "thin-muscle-theory.md", "version-answer-engine.md")

    ai_position = readme.find("## 🤖")
    theory_position = readme.find(headings[0])
    if ai_position != -1 and ai_position < theory_position:
        raise SystemExit("FAIL: README introduces AI before the thin-muscle theory")

    require(readme, "npx skills add XiaoSiKe/shao-alan-operating-system", "README.md")

    all_urls: set[str] = set()
    for research_file in (ROOT / "references" / "research").glob("*.md"):
        all_urls.update(
            re.findall(r"https?://[^\s\)]+", research_file.read_text(encoding="utf-8"))
        )
    expected_url_count = 144
    if len(all_urls) != expected_url_count:
        raise SystemExit(
            f"FAIL: expected exactly {expected_url_count} research URLs; got {len(all_urls)}"
        )
    require(readme, f"{expected_url_count} 个跨文件去重来源 URL", "README.md")

    for phrase in [
        "### 归属闸门",
        "🟠 外部观点",
        "⚪ 科学校准",
        "项目原创工作定义（不是邵艾伦本人原话）",
        "短答无法展开各层时",
        "健康与安全硬闸门",
    ]:
        require(skill, phrase, "SKILL.md")

    for index, name in [
        (8, "thin-muscle-primary-update"),
        (9, "thin-muscle-debate-update"),
        (10, "thin-muscle-evidence"),
    ]:
        path = ROOT / "references" / "research" / f"{index:02d}-{name}.md"
        if not path.exists() or path.stat().st_size < 1000:
            raise SystemExit(f"FAIL: incremental research missing: {path.name}")

    version = re.search(r'^\s*version:\s*"([^"]+)"$', skill, re.MULTILINE)
    if not version or version.group(1) != "1.3.0":
        raise SystemExit("FAIL: metadata.version must be 1.3.0")

    print("PASS: v1.3 thin-muscle-centered contract")


if __name__ == "__main__":
    main()
