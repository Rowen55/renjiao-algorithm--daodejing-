#!/usr/bin/env python3
"""从 scripture/ 的 front matter 生成 INDEX.md。

用法：
    python scripts/build_index.py           # 写入 INDEX.md
    python scripts/build_index.py --check   # 只校验 INDEX.md 是否为最新，过期则退出码 1

只依赖标准库。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTURE = ROOT / "scripture"
INDEX = ROOT / "INDEX.md"


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key.strip()] = value
    return data


def collect() -> list[dict[str, str]]:
    rows = []
    for path in sorted(SCRIPTURE.glob("*.md")):
        fm = parse_front_matter(path.read_text(encoding="utf-8"))
        rows.append({
            "file": path.name,
            "juan": fm.get("juan", ""),
            "chapter": fm.get("chapter", ""),
            "attribution": fm.get("attribution", ""),
            "keywords": fm.get("keywords", ""),
            "chars": fm.get("chars", "0"),
            "lines": fm.get("manuscript_lines", ""),
        })
    return rows


def render(rows: list[dict[str, str]]) -> str:
    total = sum(int(r["chars"] or 0) for r in rows)
    out = [
        "# 目录",
        "",
        "> 本文件由 `scripts/build_index.py` 自动生成，请勿手工修改。",
        "> 重新生成：`python scripts/build_index.py`",
        "",
        f"全经 **{len(rows)} 卷**，正文合计 **{total} 字**（不含空白）。",
        "",
        "## 经文",
        "",
        "| 卷次 | 章名 | 撰者 | 字数 | 关键词 |",
        "|---|---|---|---:|---|",
    ]
    for r in rows:
        link = f"[{r['chapter']}](scripture/{r['file']})"
        kws = r["keywords"].strip("[]").replace(", ", " · ")
        out.append(
            f"| {r['juan']} | {link} | {r['attribution']} | {r['chars']} | {kws} |"
        )
    out += [
        f"| | **合计** | | **{total}** | |",
        "",
        "## 规范层",
        "",
        "| 文件 | 内容 |",
        "|---|---|",
        "| [precepts.yaml](norms/precepts.yaml) | 十一善戒结构化：定义、判定标准、正反例、出处、外部对应 |",
        "| [mapping.md](norms/mapping.md) | 本经主张与现行人工智能伦理规范的逐条对照，含缺口分析 |",
        "| [checklist.md](norms/checklist.md) | 按生命周期分段的发布前自查清单 |",
        "",
        "## 附录与译本",
        "",
        "| 文件 | 内容 |",
        "|---|---|",
        "| [glossary.md](appendix/glossary.md) | 术语表：教门撰者、经文体术语、自造条目 |",
        "| [lineage.md](appendix/lineage.md) | 版本谱系，以及《道器谱》概念辨析 |",
        "| [colophon.md](appendix/colophon.md) | 写作缘起、体例来源与边界声明 |",
        "| [translations/](translations/README.md) | 译本方案与译名表 |",
        "",
        "## 存档",
        "",
        "| 文件 | 内容 |",
        "|---|---|",
        "| [archive/renjiao-daodejing-manuscript.txt](archive/renjiao-daodejing-manuscript.txt) | 0.1.0 原始单文件全本，不再修改 |",
        "",
    ]
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 INDEX.md")
    parser.add_argument("--check", action="store_true", help="只校验是否为最新")
    args = parser.parse_args()

    content = render(collect())

    if args.check:
        existing = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
        if existing != content:
            print("INDEX.md 已过期。请运行 scripts/build_index.py 重新生成。")
            sys.exit(1)
        print("校验通过：INDEX.md 为最新。")
        return

    INDEX.write_text(content, encoding="utf-8", newline="\n")
    print("已生成 INDEX.md")


if __name__ == "__main__":
    main()
