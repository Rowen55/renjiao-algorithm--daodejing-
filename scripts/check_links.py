#!/usr/bin/env python3
"""检查仓库内 Markdown 的相对链接是否指向存在的文件。

用法：
    python scripts/check_links.py

只检查相对路径与本地锚点，跳过 http/https 链接（避免 CI 依赖外网）。
只依赖标准库。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```")


def strip_code_blocks(text: str) -> str:
    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def main() -> None:
    problems: list[str] = []
    checked = 0

    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        text = strip_code_blocks(path.read_text(encoding="utf-8"))
        for raw in LINK_RE.findall(text):
            target = raw.strip()
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if target.startswith("#"):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                problems.append(f"{path.relative_to(ROOT).as_posix()} -> {raw}")

    if problems:
        print("发现失效链接：")
        for item in problems:
            print("  " + item)
        sys.exit(1)

    print(f"链接检查通过：共检查 {checked} 条相对链接。")


if __name__ == "__main__":
    main()
