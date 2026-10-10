#!/usr/bin/env python3
"""校验 norms/precepts.yaml 的结构完整性与编号一致性。

校验项：
  1. 条目数量为 11，编号为 P01–P11 且连续、不重复
  2. 每条包含必需字段
  3. conflict_resolution.priority_order 覆盖全部条款，且不引用不存在的编号
  4. 每条至少有一条判定标准、一条正例、一条反例、一条外部对应

只依赖标准库（用逐行缩进解析，避免引入 pyyaml）。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "norms" / "precepts.yaml"

REQUIRED_KEYS = [
    "ordinal", "name", "text", "definition", "judgement",
    "positive", "negative", "severity", "origin", "external_refs",
]

ENTRY_RE = re.compile(r"^  - id: (P\d{2})\s*$")
PRIORITY_RE = re.compile(r'^    - "(P\d{2})\b', re.MULTILINE)


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    lines = text.split("\n")

    problems: list[str] = []
    entries: list[str] = []
    blocks: dict[str, list[str]] = {}
    current: str | None = None

    for line in lines:
        m = ENTRY_RE.match(line)
        if m:
            current = m.group(1)
            entries.append(current)
            blocks[current] = []
            continue
        if current is not None:
            if line.startswith("conflict_resolution:") or line.startswith("audit:") or line.startswith("versioning:"):
                current = None
                continue
            blocks[current].append(line)

    if len(entries) != 11:
        problems.append(f"条目数量应为 11，实际为 {len(entries)}")

    expected = [f"P{i:02d}" for i in range(1, 12)]
    if entries != expected:
        problems.append(f"编号应为 P01–P11 顺序排列，实际为 {', '.join(entries)}")

    for pid, body in blocks.items():
        joined = "\n".join(body)
        for key in REQUIRED_KEYS:
            if not re.search(rf"^    {key}:", joined, re.MULTILINE):
                problems.append(f"{pid} 缺少字段：{key}")
        for list_key, label in (("judgement", "判定标准"), ("positive", "正例"),
                                ("negative", "反例"), ("external_refs", "外部对应")):
            if f"    {list_key}:" not in joined:
                continue
            section = joined.split(f"    {list_key}:", 1)[-1]
            if not re.search(r"^      - ", section, re.MULTILINE):
                problems.append(f"{pid} 的 {label} 为空")

    priority = PRIORITY_RE.findall(text)
    missing = sorted(set(entries) - set(priority))
    extra = sorted(set(priority) - set(entries))
    if missing:
        problems.append(f"priority_order 缺少：{', '.join(missing)}")
    if extra:
        problems.append(f"priority_order 引用了不存在的编号：{', '.join(extra)}")
    order_pairs = dict(zip(priority, [int(pid[1:]) for pid in priority]))
    if len(set(order_pairs)) != len(priority):
        problems.append("priority_order 中存在重复编号")

    if problems:
        print("precepts.yaml 校验未通过：")
        for p in problems:
            print("  - " + p)
        sys.exit(1)

    print(f"precepts.yaml 校验通过：{len(entries)} 条，字段齐全，裁决次序覆盖全部条款。")


if __name__ == "__main__":
    main()
