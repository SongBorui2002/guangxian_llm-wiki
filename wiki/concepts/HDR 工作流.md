---
type: concept
title: "HDR 工作流"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - hdr
  - dolby-vision
  - mastering
status: seed
related:
  - "[[Transkoder 2025]]"
  - "[[Transkoder 调色流程]]"
  - "[[DCP 母版制作]]"
  - "[[IMF 母版制作]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: advanced
domain: "transkoder"
aliases:
  - "High Dynamic Range"
  - "高动态范围"
---

# HDR 工作流

**HDR**（High Dynamic Range，高动态范围）是 Transkoder 2025 的核心竞争力之一，提供行业领先的 HDR 母版制作工具。

## Transkoder 的 HDR 能力

| 功能 | 说明 |
|------|------|
| **Dolby Vision 支持** | 完整的 Dolby Vision HDR QC 和编码工作流 |
| **HDR Analyzer** | 高级 Second Head HDR 分析器 |
| **MaxFALL/MaxCLL** | 计算和可视化显示，符合 SMPTE ST 2086:2014 |
| **HDR 元数据** | 逐帧元数据嵌入 OpenEXR |
| **HDR IMF** | IMF App 4/5 支持 HDR 输出 |
| **色彩管线** | 32 位/通道浮点处理，兼容 ACES |

## HDR 标准

- **SMPTE ST 2084**（PQ）：感知量化电光转换函数
- **SMPTE ST 2086**：静态 HDR 元数据（MaxFALL/MaxCLL）
- **SMPTE ST 2094**：动态 HDR 元数据（Dolby Vision 等方案使用）

## 指标含义

| 指标 | 全称 | 定义 |
|------|------|------|
| **MaxFALL** | Maximum Frame Average Light Level | 画面中所有帧的平均亮度最大值 |
| **MaxCLL** | Maximum Content Light Level | 整个内容中单个像素的最大亮度值 |

## 相关章节

- 用户指南第 19 章：HDR Workflows
- 用户指南第 20 章：Dolby Vision Workflow
- 用户指南第 1.9 节：Display Calibration（HDR 显示校准前提）