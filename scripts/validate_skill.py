#!/usr/bin/env python3
"""Run the repository's deterministic release checks."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*command: str) -> None:
    print(f"\n$ {' '.join(command)}")
    subprocess.run(command, cwd=ROOT, check=True)


def check_text_hygiene() -> None:
    checked = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        checked += 1
        if text and not text.endswith("\n"):
            raise SystemExit(f"FAIL: missing final newline: {path.relative_to(ROOT)}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith((" ", "\t")):
                raise SystemExit(
                    f"FAIL: trailing whitespace: {path.relative_to(ROOT)}:{line_number}"
                )
    print(f"PASS: text hygiene ({checked} files)")


def main() -> None:
    check_text_hygiene()
    run(sys.executable, "tests/test_skill.py")
    run(sys.executable, "tests/test_v12_contract.py")
    run(sys.executable, "scripts/quality_check.py", "SKILL.md")
    run(sys.executable, "-m", "py_compile", *map(str, sorted((ROOT / "scripts").glob("*.py"))))
    run("bash", "-n", "scripts/download_subtitles.sh")
    print("\nPASS: all deterministic release checks")


if __name__ == "__main__":
    main()
