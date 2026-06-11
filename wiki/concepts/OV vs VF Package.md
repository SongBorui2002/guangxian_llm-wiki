---
type: concept
title: "OV vs VF Package"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - imf
  - mastering
status: seed
related:
  - "[[DCP 母版制作]]"
  - "[[IMF 母版制作]]"
  - "[[CPL（Composition Playlist）]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: basic
domain: "transkoder"
aliases:
  - "原始版本包与版本文件包"
---

# OV vs VF Package

在 DCP 和 IMF 母版制作中，包分为两种类型：**OV**（Original Version，原始版本包）和 **VF**（Version File，版本文件包）。

## OV 包

- **完整包**：包含全部音视频和字幕资源
- **独立播放**：不依赖任何其他包即可完整播放
- **首次创建**：制作 DCP/IMF 的第一步总是先创建 OV

## VF 包

- **增量包**：仅包含与 OV 的差异部分
- **依赖 OV**：必须配合对应的 OV 使用
- **典型用途**：
  - 添加新语言的字幕或配音
  - 替换字幕版本
  - 添加替代音轨
  - 在不重新渲染全部内容的前提下创建区域性版本

## 实际场景

```
DCP 包结构：
  OV: MOVIE_FTR-1_F_EN-XX_INTL_51_2K_CS_20250605_CSR_IOP_OV
      └── 完整视频 + 英文音频 + 无字幕

  VF (法语字幕): MOVIE_FTR-1_F_FR-FR_INTL_51_2K_CS_20250605_CSR_IOP_VF
      └── 仅包含法语字幕 MXF + 新 CPL（引用 OV 的视频音频）
```

## 关键点

- OV 一旦发布不应修改
- VF 可通过新增字幕/音频而不触及原版画面资产
- IMF 的 VF 概念与 DCP 类似，但更灵活（支持音频/字幕/画面替换）