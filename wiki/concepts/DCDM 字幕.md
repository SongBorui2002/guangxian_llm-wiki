---
type: concept
title: "DCDM 字幕"
created: 2026-06-05
updated: 2026-06-05
tags:
  - dcdm
  - subtitle
  - dcp
  - smpte
  - xml
status: seed
related:
  - "[[立体 3D 字幕]]"
  - "[[DCP 母版制作]]"
  - "[[StereoscopicSubtitlePlugin]]"
  - "[[立体 3D 字幕工作流]]"
sources:
  - "[[StereoscopicSubtitlePlugin]]"
complexity: intermediate
domain: "davinci-resolve"
aliases:
  - "DCDM Subtitle"
  - "SMPTE DCDM Subtitle"
---

# DCDM 字幕

**DCDM 字幕**（Digital Cinema Distribution Master Subtitle）是符合 SMPTE ST 428-7 标准的数字电影字幕 XML 格式，用于 DCP 封装中的字幕轨道。

## 格式特征

- **XML 格式**：基于 XML 的标准化字幕描述
- **SMPTE 标准**：ST 428-7 D-Cinema Subtitle
- **兼容性**：Interop 和 SMPTE DCP 标准均支持

## 立体字幕扩展

DCDM 字幕标准包含对立体 3D 字幕的支持：

| 元素 | 说明 |
|------|------|
| **Zposition** | 字幕的 Z 轴（深度）位置 |
| **VariableZ** | 允许每个字幕事件指定不同的 Z 位置（可选参数） |

## 字幕类型

DCP 支持多种字幕格式：

| 格式 | 说明 |
|------|------|
| **MXF SMPTE Timed Text** | MXF 封装的定时文本字幕 |
| **PNG 字幕** | 基于图像的 PNG 字幕（支持动画） |
| **XML InterOp** | Texas Instruments CineCanvas 格式 |
| **XML SMPTE** | D-Cinema SMPTE 428-7 格式 |

## DCDM 立体字幕的 Z 位置生成

在 StereoscopicSubtitlePlugin 工作流中：

1. 在 DaVinci Resolve Color Page 上对字幕视频轨进行立体调整
2. 使用 Anaglyph（红蓝立体）预览模式确认深度效果
3. 通过关键帧设置不同时间点的汇聚值（Convergence）
4. 导出时将汇聚值换算为 DCDM 字幕的 Zposition 值

## 验证工具

- **DCDMSubtitle-2014.xsd**：DCDM 字幕 XML Schema 验证文件
- **DCDM_3DSUB_XSLT**：XSLT 转换和格式验证工具集
- **DCP-o-Matic**（v2.18.15+）：支持含 VariableZ 的 DCDM 字幕封装