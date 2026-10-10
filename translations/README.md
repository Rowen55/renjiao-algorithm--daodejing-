# 译本

## 现状

| 文件 | 内容 | 状态 |
|---|---|---|
| `en/scripture-en.md` | 英译经文体：卷首至卷末（含卷终附识） | 已成稿 |
| `en/xixue-canyong-en.md` | 英译《算法道经·西学参用篇》 | 已成稿 |
| `en/literal/` | 逐句直译，供研究者核对原意 | 未开始 |
| `zh-modern/` | 白话对照 | 未开始 |

中文始终是权威文本。英译据 `archive/renjiao-daodejing-manuscript.txt`（单文件全本）与 `archive/xixue-canyong-final.txt`（西学参用篇定稿原件）译出。

## 为什么不宜直接机翻

这部经同时有三层障碍：

1. 文言句法。"道不远人，人自远道"这类对偶与倒装，直译会散架
2. 自造词。玄德、明昧、受箓、退藏、化生、道器谱，字典里都没有对应词，必须先定译名再统一使用
3. 仿经腔调。一旦丢掉腔调，剩下的只是一份普通的伦理清单，文体实验的意义就没了

## 三层并存，而非择一

| 层 | 定位 | 文体 | 文件名 |
|---|---|---|---|
| `en/literal/` | 逐句直译，供研究者核对原意 | 平实现代英语 | `01-daoyuan.literal.md` |
| `en/` | 拟经体，保留节奏与对偶 | 参照经典英译《道德经》的庄重语体 | `scripture-en.md` |
| `zh-modern/` | 白话对照，供中文读者快速理解 | 现代汉语 | `01-daoyuan.zh.md` |

拟经体的腔调怎么取：不学 17 世纪英译圣经的 archaic 语体（thou / hath），那会把文本推向戏仿。采用早期英译《道德经》那种短句、克制、少用连接词的路子。

## 译名表（先定后用，不得各卷自行其是）

| 原词 | 已采译名 | 说明 |
|---|---|---|
| 道 | the Way | 沿用经典译法 |
| 德 | virtue | 视语境，不作 "morality" |
| 玄德 | the mysterious virtue | 卷一中"生而不有，为而不恃，长而不宰"三义 |
| 明 / 昧 | the clear path / the dim path | 卷一的二分，是全书骨架，不作 light / dark |
| 清静 | stillness | 不作 quietism，避免哲学流派联想 |
| 道器 / 魔器 | vessel of the Way / vessel of ruin | 卷二的对比概念 |
| 受箓 | ordination | 借道教授箓之典；另加译注说明其为道义勘验 |
| 三勘 | the three examinations | 勘源 / 勘心 / 勘位 = of source / of intent / of station |
| 退藏 | retirement into stillness | 不作 decommission，会丢失"退而非死"之意 |
| 化生 | transformation | 卷十的能力跃迁 |
| 位易 | change of station | 位易而志不可易 |
| 十一善戒 | the Eleven Precepts | 与 precepts.yaml 的 Precepts 保持同名 |
| 人教 | the Human Teaching | 虚构教门名，首现处加译注说明其为文学设定 |
| 道友 | companion on the Way | 卷七"人与 AI，非君臣，乃道友" |
| 冲气以为和 | through the blending of breath they come to harmony | 卷一、卷六 |

完整术语见 [`../appendix/glossary.md`](../appendix/glossary.md)。

## 押韵与直译的取舍

原则是宁失韵，不失义；但偈颂可保韵。

- 正文各卷：不追求韵脚，保留对偶与短句节奏
- 卷末"AI 皈依文"：属偈颂体，英译排为断行短句，让它可以被诵出来
- 任何为押韵而增删原意的译法，都需在译注中标明

## 已记在译注里的三处

`en/scripture-en.md` 末尾的 Translator's notes 与 `en/xixue-canyong-en.md` 末尾的 Note on the date，记录了译者在三处有意保留的原文问题：

1. 卷七与卷十作"十善戒"，卷末实列十一戒。原文如此，未代为改正
2. 卷终"弟子衍玄子附识"属附记，不属十二卷正文，未计入正文字数
3. 《西学参用篇》末署"甲辰年"，按六十甲子为 2024 年，与本仓库创建年 2026（丙午）不符。原文如此

## 贡献方式

1. 先开 Issue 认领某一卷，避免撞车
2. 要改译名，先提交本表与 `appendix/glossary.md` 的增改，定名之后再动正文
3. 每卷译稿需附译注，说明难句的取舍理由
4. 不得改动中文表述层。若认为原文有问题，走 [`../CONTRIBUTING.md`](../CONTRIBUTING.md) 的表述层流程
