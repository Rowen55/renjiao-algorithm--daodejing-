#!/usr/bin/env python3
"""密卷加解密工具：零依赖，只调用系统自带的 openssl。

## 约定

    internal/<名>          明文，永不入库（.gitignore 已排除）
    internal/<名>.enc      密文，提交进仓库

## 用法

    python scripts/nrcrypt.py lock   internal/正魔辨.md
    python scripts/nrcrypt.py unlock internal/正魔辨.md.enc
    python scripts/nrcrypt.py status
    python scripts/nrcrypt.py check

## 口令

优先读环境变量 ``NRCRYPT_PASSPHRASE``；没有则交互式输入（不回显）。
口令经 ``-pass env:`` 传给 openssl，不进命令行参数，``ps`` 里看不到。

算法：AES-256-CBC + PBKDF2-HMAC-SHA256（600000 轮）+ 随机盐。
密文是二进制，``.gitattributes`` 里的 ``*.enc binary`` 禁止 git 做换行转换，
否则密文会被改坏。
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from getpass import getpass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTERNAL = ROOT / "internal"
ENC_SUFFIX = ".enc"
ENV_VAR = "NRCRYPT_PASSPHRASE"
ITERATIONS = "600000"
SALTED_HEADER = b"Salted__"

# internal/ 里允许明文入库的例外（只有说明文件）
ALLOWED_PLAIN = {"README.md"}


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def find_openssl() -> str:
    found = shutil.which("openssl")
    if found:
        return found
    for guess in (
        r"C:\Program Files\Git\usr\bin\openssl.exe",
        r"C:\Program Files (x86)\Git\usr\bin\openssl.exe",
        r"C:\Program Files\Git\mingw64\bin\openssl.exe",
    ):
        if Path(guess).exists():
            return guess
    sys.exit(
        "找不到 openssl。Windows 上它随 Git for Windows 一起装（Git Bash 里敲 "
        "`openssl version` 可验证）；Linux/macOS 一般自带。"
    )


def ask_passphrase(confirm: bool) -> str:
    value = os.environ.get(ENV_VAR)
    if value:
        return value
    if not sys.stdin.isatty():
        sys.exit(f"非交互环境，请先设置环境变量 {ENV_VAR}。")
    first = getpass("口令：")
    if not first:
        sys.exit("口令不能为空。")
    if confirm:
        again = getpass("再输一次：")
        if first != again:
            sys.exit("两次输入不一致。")
    return first


def run_openssl(base_args: list[str], secret: str, out_path: Path) -> None:
    """执行 openssl，成功后原子替换 out_path；失败则不留任何残迹。

    不能直接把 ``-out`` 指向目标路径：openssl 在解密失败前已经把部分字节写出去了
    （口令错时实测留下 80 字节乱码），那样会凭空多出一个"看起来已经解密好"的文件。
    """
    tmp = out_path.with_name(out_path.name + ".part")
    tmp.unlink(missing_ok=True)

    env = dict(os.environ)
    env[ENV_VAR] = secret
    proc = subprocess.run(
        [find_openssl(), *base_args, "-out", str(tmp), "-pass", f"env:{ENV_VAR}"],
        env=env,
        capture_output=True,
    )
    if proc.returncode != 0:
        tmp.unlink(missing_ok=True)
        detail = proc.stderr.decode("utf-8", "replace").strip()
        sys.exit(f"openssl 执行失败：\n{detail}\n（没有写出任何文件，原有文件未被动过。）")

    os.replace(tmp, out_path)


def as_plain_path(raw: str) -> Path:
    """把用户给的写法归一到明文路径。"""
    path = Path(raw)
    if not path.is_absolute():
        candidate = ROOT / path
        if candidate.exists():
            path = candidate
        else:
            path = INTERNAL / path.name
    return path


def cmd_lock(raw: str, force: bool) -> None:
    plain = as_plain_path(raw)
    if plain.name.endswith(ENC_SUFFIX):
        sys.exit("lock 的目标是明文，不是 .enc。")
    if not plain.is_file():
        sys.exit(f"明文不存在：{rel(plain)}")

    out = plain.with_name(plain.name + ENC_SUFFIX)
    if out.exists() and not force:
        sys.exit(f"密文已存在：{rel(out)}（确实要覆盖，请加 --force）")

    secret = ask_passphrase(confirm=True)
    run_openssl(
        [
            "enc",
            "-aes-256-cbc",
            "-pbkdf2",
            "-iter",
            ITERATIONS,
            "-salt",
            "-in",
            str(plain),
        ],
        secret,
        out,
    )

    digest = hashlib.sha256(plain.read_bytes()).hexdigest()
    print(f"已加密：{rel(plain)} → {rel(out)}")
    print(f"  明文 {plain.stat().st_size} 字节，密文 {out.stat().st_size} 字节")
    print(f"  明文 SHA-256：{digest}")
    print("明文由 .gitignore 挡在仓库外，只有密文会被提交。")


def cmd_unlock(raw: str, force: bool) -> None:
    enc = Path(raw)
    if not enc.is_absolute():
        candidate = ROOT / enc
        enc = candidate if candidate.exists() else INTERNAL / enc.name
    if not enc.name.endswith(ENC_SUFFIX):
        sys.exit(f"unlock 的目标应是 {ENC_SUFFIX} 文件。")
    if not enc.is_file():
        sys.exit(f"密文不存在：{rel(enc)}")

    out = enc.with_name(enc.name[: -len(ENC_SUFFIX)])
    if out.exists() and not force:
        sys.exit(
            f"明文已存在：{rel(out)}\n"
            "为避免覆盖您可能更新的明文，默认不动作。确实要用密文盖掉它，请加 --force。"
        )

    secret = ask_passphrase(confirm=False)
    run_openssl(
        [
            "enc",
            "-d",
            "-aes-256-cbc",
            "-pbkdf2",
            "-iter",
            ITERATIONS,
            "-in",
            str(enc),
        ],
        secret,
        out,
    )

    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"已解密：{rel(enc)} → {rel(out)}")
    print(f"  明文 SHA-256：{digest}")
    print("此明文被 .gitignore 排除，不会误提交。")


def tracked_internal() -> list[str]:
    """列出索引里 internal/ 下的文件。

    必须用 ``-z``：默认输出会把非 ASCII 路径转义成 ``"internal/\\346\\255\\243..."``，
    后缀判断会因此失配，把每一份中文名的密文都误判成明文。
    """
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z", "--", "internal"],
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.exit("无法读取 git 索引，请确认在仓库内运行。")
    return [
        chunk.decode("utf-8", "replace")
        for chunk in proc.stdout.split(b"\0")
        if chunk
    ]


def cmd_check() -> None:
    """校验入库的 internal/ 里没有明文，且每个密文都像是真密文。"""
    if not INTERNAL.is_dir():
        print("internal/ 不存在，跳过。")
        return

    files = tracked_internal()
    if not files:
        print("internal/ 尚无入库文件。")
        return

    leaked: list[str] = []
    counterfeit: list[str] = []

    for name in files:
        base = Path(name).name
        if base in ALLOWED_PLAIN:
            continue
        if not base.endswith(ENC_SUFFIX):
            leaked.append(name)
            continue
        blob = (ROOT / name).read_bytes()
        if len(blob) <= len(SALTED_HEADER) + 8 or not blob.startswith(SALTED_HEADER):
            counterfeit.append(name)

    if leaked:
        print("密卷明文入库了——这是最严重的一类失误：")
        for name in leaked:
            print(f"  {name}")
        print()
        print("补救：先把它从索引里摘掉（保留本地文件），再重新加密。")
        print("    git rm --cached <上面的路径>")
        print("    python scripts/nrcrypt.py lock <上面的路径>")
        print("    然后提交")
        sys.exit(1)

    if counterfeit:
        print("下列文件以 .enc 结尾，但内容不像 openssl 加密产物：")
        for name in counterfeit:
            print(f"  {name}")
        print()
        print("可能是直接改了后缀、或密文被换行转换损坏。请重新加密。")
        sys.exit(1)

    print(f"密卷校验通过：internal/ 共 {len(files)} 个入库文件，全部为密文。")


def cmd_status() -> None:
    if not INTERNAL.is_dir():
        print("internal/ 不存在。")
        return

    encs = sorted(INTERNAL.rglob(f"*{ENC_SUFFIX}"))
    plains = [
        p
        for p in sorted(INTERNAL.rglob("*"))
        if p.is_file() and not p.name.endswith(ENC_SUFFIX) and p.name not in ALLOWED_PLAIN
    ]

    if not encs and not plains:
        print("internal/ 是空的。把明文放进来，再跑 lock 即可。")
        return

    print("明文（只在您本机，不入库）：")
    if plains:
        for p in plains:
            print(f"  {rel(p)}  {p.stat().st_size} 字节")
    else:
        print("  （无）")

    print("密文（入库）：")
    if encs:
        for p in encs:
            print(f"  {rel(p)}  {p.stat().st_size} 字节")
    else:
        print("  （无）")

    stale = [
        p
        for p in encs
        if (p.with_name(p.name[: -len(ENC_SUFFIX)])).exists()
        and p.stat().st_mtime
        < p.with_name(p.name[: -len(ENC_SUFFIX)]).stat().st_mtime
    ]
    if stale:
        print()
        print("下列明文比对应的密文更新，说明改了之后忘了重新加密：")
        for p in stale:
            print(f"  {rel(p.with_name(p.name[: -len(ENC_SUFFIX)]))}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="密卷加解密工具（只调用系统自带的 openssl）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_lock = sub.add_parser("lock", help="加密：明文 → 密文")
    p_lock.add_argument("path", help="明文路径，如 internal/正魔辨.md")
    p_lock.add_argument("--force", action="store_true", help="覆盖已存在的密文")

    p_unlock = sub.add_parser("unlock", help="解密：密文 → 明文")
    p_unlock.add_argument("path", help="密文路径，如 internal/正魔辨.md.enc")
    p_unlock.add_argument("--force", action="store_true", help="覆盖已存在的明文")

    sub.add_parser("check", help="校验入库的 internal/ 内无明文")
    sub.add_parser("status", help="查看明文与密文的对应情况")

    args = parser.parse_args()

    if args.command == "lock":
        cmd_lock(args.path, args.force)
    elif args.command == "unlock":
        cmd_unlock(args.path, args.force)
    elif args.command == "check":
        cmd_check()
    elif args.command == "status":
        cmd_status()


if __name__ == "__main__":
    main()
