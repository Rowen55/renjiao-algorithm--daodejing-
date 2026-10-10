# internal/ · 密卷

这里放的是不入正文的教内密卷。经文体例上属"密"字一脉，所以单独存放，并且加密。

## 规矩

| 文件 | 是否入库 | 说明 |
|---|---|---|
| `<名>.md` | 不入库 | 明文。只在本机，由 `.gitignore` 挡住 |
| `<名>.md.enc` | 入库 | 密文。AES-256-CBC 加 PBKDF2，没有口令就是乱码 |
| `README.md` | 入库 | 本说明文件，不含任何密卷内容 |

明文永远不进仓库，只进密文。这条没有例外。git 的历史删不掉，明文进过一次，后来即使把文件删了，它仍留在历史里，谁 clone 下来都能翻出来。

## 怎么用

只需要 Git 自带的 `openssl`。Windows 上装了 Git for Windows 就有，不必另装工具。

加密，然后提交密文：

```bash
python scripts/nrcrypt.py lock internal/正魔辨.md
git add internal/正魔辨.md.enc
git commit -m "密卷：正魔辨"
git push
```

解密，把仓库里的密文还原到本机：

```bash
python scripts/nrcrypt.py unlock internal/正魔辨.md.enc
```

看现状：

```bash
python scripts/nrcrypt.py status
```

校验。CI 每次都会跑这一步，防止明文误入库：

```bash
python scripts/nrcrypt.py check
```

口令优先从环境变量 `NRCRYPT_PASSPHRASE` 读，没有则交互式输入，不回显。口令经 `-pass env:` 传给 openssl，不进命令行参数，`ps` 看不到。

## 挡得住什么，挡不住什么

内容挡得住。仓库是公开的，但没口令的人拿到的只是密文。加密用 AES-256-CBC，密钥由 PBKDF2-HMAC-SHA256 迭代 60 万轮从口令导出，另加随机盐。

"存在"挡不住。密文的文件名是公开的，`internal/正魔辨.md.enc` 这个路径谁都能看见，也知道它哪天改过、有多大。外人会知道教内有这么一卷密卷，只是读不到里面的字。连"有没有"都要保密，这个目录就不该出现在公开仓库里，得改用私有仓库。

口令丢了，密文就废了，没有找回的余地。请把口令抄进密码管理器，并自己留一份明文备份在仓库之外。

密文不防篡改。谁都能把仓库里的 `.enc` 换掉，换了之后要么解密失败，要么解出错字。以本机的明文为准。解出来读不通，先怀疑密文被动过。

改了就忘会出岔子。明文改了没重新 lock，仓库里还是旧版本。`status` 会列出"明文比密文新"的文件，提交前扫一眼。
