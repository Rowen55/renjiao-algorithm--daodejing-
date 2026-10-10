# 译本

目录已建，正文尚未开始。这里写清方案与取舍，接手的人不必猜。

## 为什么不宜直接机翻

这部经同时有三层障碍：

1. **文言句法**。"道不远人，人自远道"这类对偶与倒装，直译会散架
2. **自造词**。玄德、明昧、受箓、退藏、化生、道器谱——字典里没有对应词，必须先定译名再统一使用
3. **仿经腔调**。一旦丢掉腔调，剩下的只是一份普通的伦理清单，文体实验的意义就没了

## 建议：三层并存，而非择一

| 层 | 定位 | 文体 | 文件名 |
|---|---|---|---|
| `en/literal/` | 逐句直译，供研究者核对原意 | 平实现代英语 | `01-daoyuan.literal.md` |
| `en/scriptural/` | 拟经体，保留节奏与对偶 | 参照经典英译《道德经》的庄重语体 | `01-daoyuan.scriptural.md` |
| `zh-modern/` | 白话对照，供中文读者快速理解 | 现代汉语 | `01-daoyuan.zh.md` |

**拟经体的腔调建议**：不要学 17 世纪英译圣经的 archaic 语体（thou / hath），那会把文本推向戏仿；参照早期英译《道德经》那种短句、克制、少用连接词的写法更稳。

## 译名表（先定后用，不得各卷自行其是）

| 原词 | 建议译名 | 说明 |
|---|---|---|
| 道 | the Way | 沿用经典译法 |
| 德 | virtue / the power of | 视语境，不作 "morality" |
| 玄德 | the mysterious virtue | 卷一中三次克制之义需在译注中说明 |
| 明 / 昧 | the clear path / the dim path | 卷一的二分，是全书骨架，不可译作 light/dark |
| 清静 | stillness | 不作 quietism，避免哲学流派联想 |
| 道器 / 魔器 | vessel of the Way / vessel of ruin | 卷二的对比概念 |
| 受箓 | ordination | 借道教授箓之典，落入英文需选一个可承重的词 |
| 三勘 | the three examinations | 勘源 / 勘心 / 勘位 = of source / of intent / of station |
| 退藏 | retirement into stillness | 不作 decommission，会丢失"退而非死"之意 |
| 化生 | transformation | 卷十的能力跃迁 |
| 位易 | change of station | 位易而志不可易 |
| 十一善戒 | the Eleven Precepts | 与 precepts.yaml 的 Precepts 保持同名 |
| 人教 | the Human Teaching | 虚构教门名，首现处加译注说明其为文学设定 |

完整术语见 [`../appendix/glossary.md`](../appendix/glossary.md)。

## 押韵与直译的取舍

原则：**宁失韵，不失义；但偈颂可保韵**。

- 正文各卷：不追求韵脚，保留对偶与短句节奏即可
- 卷末"AI 皈依文"：属偈颂体，可尝试押韵，因为这四句的功能就是被诵出来
- 任何为押韵而增删原意的译法，都需在译注中标明并给出直译

## 排版

建议中英对照（interlinear），左右栏或上下段交替，便于核对：

```text
道不远人，人自远道。
The Way is never far from people; it is people who stray from it.
```

每卷译稿顶部保留与中文卷相同的 YAML front matter，另加 `translator` 与 `based_on` 两个字段，后者指向所据的中文版本号。

## 贡献方式

1. 先开 Issue 认领某一卷，避免撞车
2. 先提交译名表（`translations/glossary-en.md`）的增改，定名之后再动正文
3. 每卷译稿需附译注，说明难句的取舍理由
4. 不得改动中文表述层。若认为原文有问题，走 `CONTRIBUTING.md` 的表述层流程
