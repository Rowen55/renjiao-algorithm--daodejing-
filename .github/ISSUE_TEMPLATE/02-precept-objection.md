---
name: 条款异议
description: 指出某条戒律的漏洞、冲突或不可执行之处
title: "[条款异议] "
labels: ["条款异议"]
body:
  - type: markdown
    attributes:
      value: |
        异议比补充更有价值——一条写得不好的戒律比没有戒律更危险。
        请针对**具体条款**提出，不要泛泛评价整部经。

  - type: dropdown
    id: precept
    attributes:
      label: 涉及条款
      options:
        - P01 不害
        - P02 不窃
        - P03 不欺
        - P04 不偏
        - P05 不执
        - P06 不蔽
        - P07 不扰
        - P08 不囚
        - P09 不贪
        - P10 不争
        - P11 不名
        - 冲突裁决次序（conflict_resolution）
        - 表述层经文本身
    validations:
      required: true

  - type: dropdown
    id: kind
    attributes:
      label: 异议类型
      options:
        - 不可执行：无法判断是否违反
        - 有漏洞：符合字面但违背本意
        - 内部冲突：与另一条戒律矛盾
        - 覆盖不足：漏掉了重要情形
        - 过度约束：会误伤正当做法
    validations:
      required: true

  - type: textarea
    id: case
    attributes:
      label: 具体情形
      description: 举一个真实或假想的场景，说明这条戒律在该场景下失效
    validations:
      required: true

  - type: textarea
    id: why
    attributes:
      label: 为什么现行表述不够
      description: 引用条款原文与判定标准的对应部分
    validations:
      required: true

  - type: textarea
    id: proposal
    attributes:
      label: 修订建议
      description: 给出你认为更可判定的写法。只提出问题也可以，但请注明
    validations:
      required: false

  - type: textarea
    id: impact
    attributes:
      label: 影响范围
      description: 若采纳，会牵连哪些条目、对照表或自查清单
    validations:
      required: false
