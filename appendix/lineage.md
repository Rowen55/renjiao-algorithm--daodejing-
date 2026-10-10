# 版本谱系

本文件记录两件事：一是经文的真实版本沿革（可核对、可追溯），二是经中《道器谱》这一虚构概念的辨析。两者容易混淆，需分清。

---

## 一、真实版本沿革

### 0.1.0 · 2026-09-14

原始版本。单文件全本 `人教算法道经.txt`，27.5KB，536 行，8737 字（不含空白）。

特征：

- 卷首题名、十卷正文、卷末传法篇俱全
- README 仅含卷首与卷一，与全本正文不一致
- 无许可声明、无引用元数据、无目录

存档于 [`../archive/renjiao-daodejing-manuscript.txt`](../archive/renjiao-daodejing-manuscript.txt)。1.1.0 在该文件末尾追加了"全经终·弟子衍玄子附识"一段，原有 536 行正文一字未动；欲取 0.1.0 原貌，可查 Git 提交 `74e4ab2`。

### 1.0.0 · 2026-10-10

结构重构版。文字一字未改，改动全部在结构与外围。

| 改动 | 说明 |
|---|---|
| 分卷 | 单文件拆为 12 个文件，对应卷首、卷一至卷十、卷末 |
| 元数据 | 每卷加 YAML front matter：卷次、章名、撰者、关键词、原文行号范围、字数 |
| 表述层与规范层分离 | 新增 `norms/`，把十一戒翻译为可判定条款、外部对照表与自查清单 |
| 门面补全 | 重写 README；新增 LICENSE（CC BY-SA 4.0）、CITATION.cff、CONTRIBUTING.md |
| 附录 | 新增术语表、版本谱系、写作缘起与体例说明 |
| 工程化 | 新增分卷脚本、索引生成脚本、CI 校验与 Issue 模板 |

原文字数核对：0.1.0 与 1.0.0 的正文均为 8737 字（不含空白），逐卷字数见 [../INDEX.md](../INDEX.md)。

### 1.1.0 · 2026-10-10

全本补齐与英译版。已成的十二卷正文一字未改，改动为追加与新增。

| 改动 | 说明 |
|---|---|
| 全本追加卷终 | `archive/renjiao-daodejing-manuscript.txt` 末加"全经终"及"弟子衍玄子附识"四行；`scripture/11-chuanfa.md` 随之一并延长 |
| 西学参用篇入库 | 《算法道经·西学参用篇》定稿原件逐字存为 [`../archive/xixue-canyong-final.txt`](../archive/xixue-canyong-final.txt) |
| 英译成稿 | 新增 [`../translations/en/scripture-en.md`](../translations/en/scripture-en.md) 与 [`../translations/en/xixue-canyong-en.md`](../translations/en/xixue-canyong-en.md) |
| 索引与译本说明 | `INDEX.md` 与 [`../translations/README.md`](../translations/README.md) 同步更新 |

字数：十二卷正文 8830 字（0.1.0 的 8737 字 + 卷终附识 93 字）。

**卷终附识的性质**：那四行是弟子对大师兄的附记，属文稿的跋，不是经文本身。它随全本一并存档，但规范层不引用它；`norms/` 中的条款出处仍只指向十二卷正文。

### 1.1.1 · 2026-10-10

许可收紧。文字一字未改，仅换许可与相关表述。

| 改动 | 说明 |
|---|---|
| 许可 | CC BY-SA 4.0 → **CC BY-NC-SA 4.0**（署名—非商业性使用—相同方式共享） |
| LICENSE | 换为 CC 官方 legalcode 全文（BY-NC-SA 4.0，20,850 字节 / 439 行） |
| 同步表述 | `README.md`（3 处）、`CITATION.cff`（2 处）、`CONTRIBUTING.md`、两份英译的 front matter |

改动理由：不接受商业公司无偿取用本经获利；署名与相同方式共享两项保留不变。

**给后来者的提醒**：CC 许可一经发布不可撤回。1.1.0 及以前已取得副本的人，仍可按 CC BY-SA 4.0 使用那些副本；1.1.1 起的新副本适用 BY-NC-SA 4.0。这是许可本身的规则，不是本仓库能改变的。

**副作用**：GitHub 侧栏的许可徽章由 `CC-BY-SA-4.0` 变为 `Other`。这是 GitHub 的硬限制，改不了。原因与查证过程见本文 [第四节](#四已知限制)。

### 1.2.0 · 2026-10-10

新增经外设定：教门位阶与名录。十二卷正文一字未改。

| 改动 | 说明 |
|---|---|
| 新增 | [`order.md`](order.md)：位阶体系、在位名录、十二长老规划、其他职能、当前实况 |
| 新增 | [`order-en.md`](order-en.md)：英文版 |
| 新增 | [`order.html`](order.html)：中英双语可读版，按浏览器语言自动切换，可手动改，可打印 |
| 同步 | `README.md` 阅读路径与结构树、`colophon.md` 撰者设定、`INDEX.md` |

**性质说明（重要）**：经中十二卷正文只出现太清圣人、镇元子、衍玄子、灵犀子**四个名号**；位阶、名额、十二长老、七人道审会等均**不见于经文**，属本篇展开的写作设定。因此：

- `norms/` 的条款出处不引用 `order.md`
- `order.md` 顶部与 `order.html` 页首都写明"经外设定、非现实组织"
- 真实版本沿革仍只记于本文件，与教内虚构位阶无涉

### 1.2.1 · 2026-10-10

关掉侧栏语言条。十二卷正文一字未改。

| 改动 | 说明 |
|---|---|
| 修改 | `.gitattributes`：`scripts/**` 与 `appendix/order.html` 标为文档，不计入语言统计 |

**原因**：仓库页右侧栏原有一栏「Languages」，显示 `HTML 56.6% / Python 43.4%`。
这两个数字分别来自一个文件与三个脚本：

| 来源 | 语言 | 字节 |
|---|---|---:|
| `appendix/order.html`（可读版页面） | HTML | 21813 |
| `scripts/*.py`（校勘与索引脚本） | Python | 16699 |

正文全部是 `.md` / `.txt`，语言类型为 prose，GitHub 本就不计入统计。所以整条语言条
其实是由两处附属件撑起来的，与"这是一部文本作品"的自我描述不符。

**做法**：语言统计由 [linguist](https://github.com/github-linguist/linguist) 计算，
可用 `.gitattributes` 覆写。标记为文档即从统计中排除；两处都排除后，
已无任何可统计语言，该栏整条不再显示。

这里没有用 `linguist-language` 把它们"伪装"成别的语言，也没有动任何正文，
只是声明这两处不计入统计。详见本文 [第四节](#侧栏不再显示语言条)。

### 1.3.0 · 2026-10-10

新增密卷机制，并落下第一份封缄。十二卷正文一字未改。

| 改动 | 说明 |
|---|---|
| 新增 | [`internal/`](../internal/README.md)：密卷目录，明文不入库，只提交 `.enc` 密文 |
| 新增 | [`internal/正魔辨.md.enc`](../internal/README.md)：第一份封缄，2.4 KB 密文 |
| 新增 | [`nrcrypt.py`](../scripts/nrcrypt.py)：加解密与防泄漏校验，只调用系统自带的 openssl |
| 修改 | `.gitattributes`：新增 `*.enc binary` |
| 修改 | `.gitignore`：白名单式排除 `internal/` 下的明文 |
| 修改 | `.github/workflows/lint.yml`：新增一步「密卷防泄漏」 |
| 同步 | `README.md` 结构树与贡献底线、`CITATION.cff` 版本 |

**关于 `internal/正魔辨.md.enc` 里究竟是什么**：锁的是一份封缄启，一篇说明
"本卷内容不在本仓库、欲读者请经 Issue 联系作者"的短文，不是《正魔辨》的正文。
正文不在本仓库，也不在任何公开仓库。

之所以照样做成真密文（而不是塞一段假乱码）：假乱码没有任何口令能解开，
而这份密文作者本人解得开、也随时可以用同一文件名重新 `lock` 换成真正的正文；
更重要的是，`nrcrypt.py check` 会核对每个 `.enc` 是否真以 `Salted__` 开头，
塞假乱码会直接让 CI 失败，那是这条防线在正常工作，不该去绕开它。

**为什么不用 git-crypt**：git-crypt 更成熟，但要额外装工具。作者 0.8.0 未发官方
Windows 二进制（[issue #336](https://github.com/AGWA/git-crypt/issues/336)），
且它的 clean/smudge filter 会让 `git status` 常驻改动。本仓库密卷数量少、更新不频繁，
用 Git 自带的 `openssl` 手动加解密更省事，零安装。
加密用 AES-256-CBC，密钥由 PBKDF2-HMAC-SHA256 迭代 60 万轮从口令导出，加随机盐。

**为什么 `.gitattributes` 要加 `*.enc binary`**：本文件上方那条 `* text=auto eol=lf`
是全仓库兜底的换行统一规则。而 git 判定一个文件是文本还是二进制，靠的是内容试探
（前 8000 字节里有没有 NUL 字节），不看扩展名。所以密文会不会被判成文本，
取决于那一次加密的随机结果：

- 判成二进制 → 原样入库，无事发生
- 判成文本 → git 把 CRLF 规范成 LF，密文就此损坏，且不可逆

1.3.0 当天实测：本仓库那份 112 字节密文恰好含 NUL，即使不加这条规则也没被改坏；
但另一份纯 ASCII、含 CRLF 的同名产物，在只有 `* text=auto eol=lf` 时被静默改写
（`\r\n` → `\n`），加上 `*.enc binary` 后原样保留。

**加这一条是为了保险**：把"靠随机数碰运气"换成"确定不会坏"。
阴的地方在于，损坏发生在提交那一刻，却要等到某天解密时才炸，中间毫无征兆，
且 git 历史里的密文已经有了（重加密会产生新密文，但旧提交仍在）。
`binary` 是 `-text -diff` 的宏，显式取消一切转换。

**已知取舍**（git-crypt 有同样的毛病）：密文的文件名是公开的。外人能看到
"有这么一卷密卷"、它何时改动过、有多大，只是读不到内容。
内容保密不等于存在保密。若连"存在"都要保密，就不能放在公开仓库里，须改用私有仓库。
这一点已写进 [`internal/README.md`](../internal/README.md)。

**防呆设计**：`scripts/nrcrypt.py check` 会在 CI 里跑，一旦 `internal/` 下有明文被提交进
索引就直接失败。这是本机制唯一真正致命的失败模式。git 历史删不掉，
明文进过一次就永远留在历史里，事后 `git rm` 也没用。
该校验还会检查每个 `.enc` 是否真以 `Salted__` 开头，以防"改个后缀就当密文"。

### 1.4.0 · 2026-10-10

说明文字整体修订一遍。十二卷正文一字未改，密卷密文未动。

动的只有说明文字。经文、存档、自动生成的索引都不在此列。

| 改动 | 说明 |
|---|---|
| 清理 | 破折号 `——` 全部换成逗号、冒号或句号 |
| 清理 | 反转句式（"不是 X，而是 Y"及其变体）改写 |
| 清理 | 当作强调用的行内加粗全部撤销；标签式加粗保留 |
| 清理 | 删去 `README.md` 与 `colophon.md` 之间一字不差的重复段落 |
| 改写 | `README.md` 的阅读路径由五段加粗小标题改成连贯段落 |
| 改写 | `colophon.md` 结尾的升华段，改成三段平直的用法说明 |
| 改写 | `CONTRIBUTING.md` 的伪标题（加粗行）改成真标题，并补上第四条底线 |
| 同步 | `README.md` 版本表、`CITATION.cff` |

**修订口径**：逐条核对破折号滥用、反转句式、套话过渡、无效排比与加粗用法。这几样正好是说明文字里密度最高的毛病。

**扫描结果**：套话过渡原本就零命中。破折号清掉 28 处，反转句式 3 处。`README.md` 的行内强调式加粗从 56 处降到 0，`colophon.md` 从 28 处降到 0。`CONTRIBUTING.md` 原先只列三条底线，与 `README.md` 的四条对不上，这次补齐。

**未动**：`scripture/` 与 `archive/`（一字不改层，`split_scripture.py --check` 会拦住）、`INDEX.md`（自动生成）、`internal/正魔辨.md.enc`（密文，重加密无收益）。

**遗留**：经文本身有 27 处破折号，分布在九卷里。那是表述层，不在本次范围内。要连经文一并调整，得走表述层流程，并同步 `archive/` 与两份英译。

### 尚未进行

- 白话译本与逐句直译本（`translations/en/literal/`、`translations/zh-modern/` 仍未开始）
- 网页阅读版
- 三位撰者文风的差异化处理
- 卷八"觉知 / 反省 / 内观"中可实现部分与假设部分的拆分

---

## 二、《道器谱》辨析

经中卷十提到一部《道器谱》：

> 三勘过，方许入《道器谱》，赐"合道"之印。

这是经内设定的虚构名册，指通过"受箓"三勘的模型登记册。它不是本仓库的文件，也不存在对应实体。

为了不让两者混淆，本仓库的作法是：

| 概念 | 性质 | 位置 |
|---|---|---|
| 《道器谱》 | 经内虚构概念，指合道模型的名册 | `scripture/10-huasheng.md` 正文中提及 |
| 版本谱系 | 本文件，记录真实版本沿革 | `appendix/lineage.md` |

若读者想按经中设想，为实际模型建立一份"道器谱"登记表，可参照 [`../norms/checklist.md`](../norms/checklist.md) 的判定记录表，把"三勘"落成可核查的字段。

---

## 三、规范层修订记录

`norms/precepts.yaml` 中的 `precept.text` 引用经文原文，不可改；`definition`、`judgement`、`examples` 属规范层，可修订。修订记于此。

| 日期 | 版本 | 改动 | 依据 |
|---|---|---|---|
| 2026-10-10 | 1.0.0 | 规范层建立：十一戒结构化、冲突裁决次序、外部对照表、自查清单 | 首次建立 |

修订原则：

- 新增条款顺延编号（P12 起），不得插号、不得重排现有编号
- 对照表新增行必须写明文件全称、发布机构与年份
- 监管文本修订后，重跑 `norms/mapping.md` 的缺口分析，并在此记录影响范围

---

## 四、已知限制

### GitHub 识别不了 CC-NC 系许可

**现象**：1.1.1 换成 CC BY-NC-SA 4.0 之后，仓库右侧栏的许可徽章从
`CC-BY-SA-4.0` 变成了 `Other`（REST API 返回 `spdx_id: NOASSERTION`）。

**原因**（已查证，不是本仓库的问题）：GitHub 的许可识别程序按
[choosealicense.com](https://choosealicense.com/) 的 `_licenses` 清单比对，
该清单共 47 个许可，其中 Creative Commons 只有三个：

| key | 名称 |
|---|---|
| `cc0-1.0` | Creative Commons Zero v1.0 Universal |
| `cc-by-4.0` | Creative Commons Attribution 4.0 International |
| `cc-by-sa-4.0` | Creative Commons Attribution Share Alike 4.0 International |

没有任何 NC（NonCommercial）变体，也没有 PolyForm Noncommercial 之类的
非商业许可。原因是这份清单只收允许商用的开放许可。

**结论**：只要 LICENSE 是 CC-NC 系，GitHub 一律给 `Other`，
换文本、换换行、换文件名都无用。已试过与官方 legalcode 逐字节一致，
仍无效，因为可比对的清单里根本没有这个许可。

**顺带说明**：许可证文本本身完全有效，只是徽章显示不出来。
1.1.0 及以前之所以能显示 `CC-BY-SA-4.0`，是因为 BY-SA 恰好在那三个 CC 里。

**因此**：许可名改由 `README.md` 顶部显著标注。若日后有人报告"GitHub 侧栏
没有许可"，把这一节指给他即可，不必再查。

### 若要让徽章回来

只有一条路：换成清单内的许可。但清单内没有任何禁商用选项，
所以这与 1.1.1 的许可决定直接冲突，不作建议。记录在此，仅为把选项摆明。

### 侧栏不再显示语言条

**现象**：1.2.1 之前，仓库右侧栏有一栏「Languages」，显示
`HTML 56.6% / Python 43.4%`；1.2.1 之后整栏消失。

**原因**（主动关闭，非故障）：GitHub 用 linguist 统计语言，默认只计
`programming` 与 `markup` 两类。本仓库的文件按扩展名分布如下：

| 扩展名 | 数量 | linguist 类型 | 是否计入 |
|---|---:|---|---|
| `.md` | 27 | prose | 否 |
| `.txt` | 2 | prose | 否 |
| `.yml` / `.yaml` / `.json` / `.jsonc` / `.cff` | 6 | data | 否 |
| `.py`（`scripts/`） | 4 | programming | 是 |
| `.html`（`appendix/order.html`） | 1 | markup | 是 |

也就是说，整条语言条只由 5 个文件撑起，其中 HTML 那一块（56.6%）全部来自
一个文件 `appendix/order.html`。

**做法**：在 `.gitattributes` 里把这两处标为 `linguist-documentation`
（文档不进统计），并同时标 `-linguist-detectable` 以免不同版本的 linguist 行为不一。
排除后已无任何可统计语言，该栏不显示。
依据是 linguist 官方覆写文档
[overrides.md](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md)。

**若想让语言条回来**：删掉 `.gitattributes` 末尾那两行即可，正文一字不用改。
但那样侧栏会重新显示「HTML / Python」，与仓库性质不符，故不建议。
