---
type: concept
title: "DaVinci HDR 工作流"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - hdr
  - dolby-vision
  - color-grading
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 调色流程]]"
  - "[[HDR 工作流]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "DaVinci HDR Grading"
---

# DaVinci HDR 工作流

DaVinci Resolve 20 提供完整的 HDR（高动态范围）调色和母版制作工具，涵盖从 HDR 设置到 Dolby Vision 母版制作的全流程。

## HDR 调色板

DaVinci Resolve 提供专用的 HDR 调色轮：

| 控制 | 说明 |
|------|------|
| **Global Wheel** | 整体曝光偏移，旋转 HDR 色轮 |
| **Zone Control** | 分区曝光控制，按亮度区域独立调整 |
| **Black Offset** | 黑电平偏移 |
| **Dark/Shadow/Light/Highlight/Specular** | 六个亮度区域独立控制 |

## HDR 标准

| 标准 | 说明 |
|------|------|
| **HDR10** | 基础 HDR 标准，静态元数据 |
| **HDR10+** | 动态元数据 HDR |
| **HLG**（Hybrid Log-Gamma） | 兼容 SDR 的广播 HDR 标准 |
| **Dolby Vision** | 高级动态 HDR，逐帧/逐场景元数据 |

## Dolby Vision 工作流

1. **设置 Dolby Vision 项目**：在 Color Management 中选择 Dolby Vision 色彩空间
2. **调色**：使用 HDR 调色板进行 HDR 调色
3. **分析**：运行 Dolby Vision 分析生成动态元数据
4. **CMU 导出**：导出 Dolby Vision CMU（Content Mapping Unit）数据
5. **交付**：渲染为 Dolby Vision 格式（Profile 5/8.1/8.4）

## HDR 监看

- 需要 HDR 参考监视器（如 Dolby PRM-4220）
- 支持 DeckLink 和 UltraStudio 通过 SDI/HDMI 输出HDR 信号
- 支持 HDR 示波器（HDR Waveform、HDR Histogram）

## HDR 设置

| 设置 | 说明 |
|------|------|
| **HDR Mastering Nits** | 母版峰值亮度（如 1000 nits） |
| **HDR Color Gamut** | HDR 色彩空间（Rec.2020、DCI-P3 D65） |
| **Tone Mapping** | 从 SDR 到 HDR 或 HDR 到 SDR 的色调映射 |
| **Dolby Vision Target** | CMU 目标显示设备参数 |