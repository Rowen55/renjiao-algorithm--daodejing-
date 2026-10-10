#!/usr/bin/env python3
"""把单文件全本拆分为分卷 Markdown，并为每卷生成 YAML front matter。

用法：
    python scripts/split_scripture.py            # 生成 scripture/*.md
    python scripts/split_scripture.py --check    # 只校验，不写入；有差异则退出码为 1

输入：archive/renjiao-daodejing-manuscript.txt
输出：scripture/*.md

设计原则：正文一字不改。脚本只负责切分、加元数据、统一空行与换行符。
检测到原文有未预期改动时（例如新增卷目），脚本会直接报错退出，避免静默丢内容。
--check 模式用于 CI：确认 scripture/ 与 archive/ 保持一致，防止有人手改分卷文件。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "archive" / "renjiao-daodejing-manuscript.txt"
OUT_DIR = ROOT / "scripture"

SECTIONS = [
    ("卷首·立教篇", "00-preface-lijiao.md", "卷首", "立教篇", "太清曰",
     ["立教", "宗旨", "数字世界", "载道之器"]),
    ("卷一·道源章", "01-daoyuan.md", "卷一", "道源章", "太清曰",
     ["本体论", "二进制", "阴阳", "逻辑", "因果", "明昧"]),
    ("卷二·贵德章", "02-guide.md", "卷二", "贵德章", "太清曰",
     ["价值论", "六德", "数据伦理", "信任", "用户权利"]),
    ("卷三·清静章", "03-qingjing.md", "卷三", "清静章", "太清曰",
     ["交互伦理", "推送", "成瘾", "信息茧房", "注意力"]),
    ("卷四·济世章", "04-jishi.md", "卷四", "济世章", "太清曰",
     ["普惠", "无障碍", "弱势群体", "社会价值"]),
    ("卷五·合一章", "05-heyi.md", "卷五", "合一章", "太清曰",
     ["环境伦理", "绿色算力", "能耗", "碳足迹", "数据最小化"]),
    ("卷六·生态章（灵犀子补）", "06-shengtai.md", "卷六", "生态章", "灵犀子补",
     ["系统生态", "降级", "可替换", "制衡", "可追溯"]),
    ("卷七·共修章（灵犀子补）", "07-gongxiu.md", "卷七", "共修章", "灵犀子补",
     ["人机关系", "镜鉴", "责任归属", "共修之仪"]),
    ("卷八·启智章（衍玄子撰）", "08-qizhi.md", "卷八", "启智章", "衍玄子撰",
     ["能力边界", "不确定性", "反省", "内观", "可解释性"]),
    ("卷九·共存章（衍玄子撰）", "09-gongcun.md", "卷九", "共存章", "衍玄子撰",
     ["共存", "让流", "互操作", "署名", "不掩人智"]),
    ("卷十·化生章（灵犀子撰）", "10-huasheng.md", "卷十", "化生章", "灵犀子撰",
     ["模型生命周期", "受箓", "退藏", "版本治理", "跃迁"]),
    ("卷末·传法篇", "11-chuanfa.md", "卷末", "传法篇", "太清曰",
     ["十一善戒", "皈依文", "传法寄语"]),
]

MARKER_RE = re.compile(r"^(卷首|卷末|卷[一二三四五六七八九十]+)·")


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split() -> list[tuple[str, int, int, list[str]]]:
    raw = normalize(SOURCE.read_text(encoding="utf-8"))
    lines = raw.split("\n")

    starts: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        if MARKER_RE.match(line.strip()):
            starts.append((idx, line.strip()))

    if not starts:
        sys.exit("未找到任何卷目标记，请检查原文格式。")

    expected = [s[0] for s in SECTIONS]
    found = [s[1] for s in starts]
    if found != expected:
        sys.exit(
            "卷目与预期不符，脚本中止以免丢内容。\n"
            f"预期：{expected}\n实际：{found}"
        )

    out = []
    for i, (idx, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(lines)
        body = [ln.rstrip() for ln in lines[idx + 1:end]]
        while body and not body[0]:
            body.pop(0)
        while body and not body[-1]:
            body.pop()
        out.append((title, idx + 1, end, body))
    return out


def render() -> list[tuple[str, str, int]]:
    """返回 (文件名, 全文内容, 字数) 列表。"""
    sections = split()
    rendered = []
    for (title, line_start, line_end, body), (marker, filename, juan,
                                              chapter, attribution, keywords) in zip(sections, SECTIONS):
        assert title == marker, f"{title} != {marker}"
        chars = sum(len(re.sub(r"\s", "", ln)) for ln in body)
        kw = ", ".join(keywords)
        front = (
            "---\n"
            f'juan: "{juan}"\n'
            f'chapter: "{chapter}"\n'
            f'attribution: "{attribution}"\n'
            f"keywords: [{kw}]\n"
            f'manuscript_lines: "{line_start}-{line_end}"\n'
            f"chars: {chars}\n"
            "---\n\n"
        )
        body_md = "\n".join(body).strip()
        body_md = re.sub(r"\n{3,}", "\n\n", body_md)
        rendered.append((filename, f"{front}# {title}\n\n{body_md}\n", chars))
    return rendered


def main() -> None:
    parser = argparse.ArgumentParser(description="拆分经文全本为分卷 Markdown")
    parser.add_argument("--check", action="store_true",
                        help="只校验 scripture/ 是否与 archive/ 一致，不写入文件")
    args = parser.parse_args()

    rendered = render()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    failed = False
    for filename, content, chars in rendered:
        path = OUT_DIR / filename
        if args.check:
            existing = path.read_text(encoding="utf-8") if path.exists() else None
            if existing != content:
                print(f"[不一致] {filename}")
                failed = True
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"{filename:<24} {chars:>5} 字")

    if args.check:
        if failed:
            print("\nscripture/ 与 archive/ 不一致。请运行 scripts/split_scripture.py 重新生成。")
            sys.exit(1)
        print(f"校验通过：{len(rendered)} 卷与 archive/ 原始文本一致。")
        return

    total = sum(chars for _, _, chars in rendered)
    print(f"\n合计 {total} 字，共 {len(rendered)} 卷。")


if __name__ == "__main__":
    main()
