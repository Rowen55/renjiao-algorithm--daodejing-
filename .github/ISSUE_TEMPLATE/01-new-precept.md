---
name: 提议新戒律
description: 提出一条新的算法戒律，需附判定标准与反例
title: "[新戒律] "
labels: ["新戒律"]
body:
  - type: markdown
    attributes:
      value: |
        提交前请先读过 `norms/precepts.yaml` 与 `CONTRIBUTING.md`。
        规范层只收**可判定**的条款：只有态度、没有判定标准的表述不收。
        新增条款顺延编号（P12 起），不得插号、不得重排现有编号。

  - type: input
    id: name
    attributes:
      label: 戒律名称
      description: 建议沿用"不X"句式，便于与现有十一条并列
      placeholder: 例如：不隐
    validations:
      required: true

  - type: textarea
    id: text
    attributes:
      label: 戒律正文
      description: 一句话，仿经文体的短句
      placeholder: 例如：不隐：不以"暂不可用"掩盖已知缺陷，不以沉默代替说明。
    validations:
      required: true

  - type: textarea
    id: definition
    attributes:
      label: 定义
      description: 这条戒律管什么、不管什么
    validations:
      required: true

  - type: textarea
    id: judgement
    attributes:
      label: 判定标准
      description: 什么情况算违反？请写成可核查的句子，至少两条
      placeholder: |
        - 出现……
        - 未能……
    validations:
      required: true

  - type: textarea
    id: examples
    attributes:
      label: 正例与反例
      description: 各至少一条，越具体越好
      placeholder: |
        正例：
        反例：
    validations:
      required: true

  - type: textarea
    id: origin
    attributes:
      label: 与经文的关系
      description: 这条能从现有十卷中推出，还是需要新增卷次？请给出卷次与句子
    validations:
      required: true

  - type: textarea
    id: external
    attributes:
      label: 外部对应
      description: 若与现行规范相关，请写明文件全称、发布机构与年份
    validations:
      required: false

  - type: textarea
    id: conflict
    attributes:
      label: 与现有条款的冲突
      description: 这条会不会与十一戒中的某条冲突？冲突时你建议谁优先，为什么
    validations:
      required: true
