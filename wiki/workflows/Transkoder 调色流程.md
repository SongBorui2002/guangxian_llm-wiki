---
type: workflow
title: "Transkoder 调色流程"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - color-grading
  - cdl
  - lut
  - aces
status: seed
related:
  - "[[Transkoder 2025]]"
  - "[[Node Page 图像处理管线]]"
  - "[[HDR 工作流]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
workflow_type: procedure
domain: "transkoder"
prerequisites:
  - "Node Page 中已加载需要调色的片段"
  - "已配置显示校准（如需准确预览）"
outputs:
  - "调色后的图像管线设置"
---

# Transkoder 调色流程

在 Transkoder 的 Node Page 中，通过 CDL、LUT、ACES 等节点进行专业调色的操作流程。

## 调色管线架构

```
摄影机 RAW → [CDL Node] → [LUT Node] → [ACES Node] → ... → 输出
```

每个调色节点位于 Node Page 管线的 Grade Template 部分（片段级），可根据需要灵活插入。

## CDL 调色

### CDL 节点功能

CDL（Color Decision List）节点支持标准的 ASC CDL 参数：
- **Slope**（斜率）— RGB 增益调整
- **Offset**（偏移）— RGB 整体偏移
- **Power**（Gamma）— RGB gamma 调整
- **Saturation**（饱和度）— 全局色彩饱和度

### CDL 工作流

1. 在 Node Page 中插入 CDL 节点
2. 调整 Slope/Offset/Power/Saturation 参数
3. CDL 值可导出为 `.cdl` 文件用于跨系统交换

## LUT 调色

### LUT 节点功能

支持 1D LUT 和 3D LUT 导入：
- **技术 LUT**：色彩空间转换（如 LogC → Rec.709）
- **创意 LUT**：风格化外观预设
- **校准 LUT**：显示器校准用

### 使用步骤

1. 在管线中插入 LUT 节点
2. 加载 `.cube` 或 `.3dl` 格式的 LUT 文件
3. 可叠加多个 LUT 节点
4. 支持自定义 LUT 用于视频输出和 Second Head Analyzer

## ACES 色彩空间

### ACES 节点功能

Transkoder 的 32 位/通道管线兼容 **ACES**（Academy Color Encoding System）：
- **ACES 输入转换**（IDT）：从摄影机色彩空间到 ACES
- **ACES 输出转换**（ODT/RRT）：从 ACES 到目标渲染色彩空间

### ACES 设置

- 在 Settings Page 配置 ACES 版本和参数
- 支持 ARRI ADA-5-SW ACES（ARRI 开发的去马赛克算法，输出 ACES 线性色彩空间）

## Dolby Vision HDR 调色

### Dolby Vision 配置

- 专用的 Dolby Vision 节点和工作流（用户指南第 20 章）
- 支持 Dolby Vision 元数据生成和嵌入
- HDR QC 工具：MaxFALL/MaxCLL 计算和可视显示

### 相关工具

- **Second Head HDR Analyzer**：在第二输出上显示 HDR 分析信息
- **MaxFALL**（Maximum Frame Average Light Level）
- **MaxCLL**（Maximum Content Light Level）
- 符合 SMPTE ST 2086:2014

## 调色快捷键

| 快捷键 | 功能 |
|--------|------|
| **Shift+T** | 保存 Grade 和 Viewing Template |
| **Shift+Y** | 仅保存 Viewing Template |
| **Ctrl+Z** | 撤销调色操作 |

## 相关调色节点

- **CDL Node**：ASC CDL 色彩决策列表
- **LUT Node**：1D/3D LUT 应用
- **ACES Node**：ACES 色彩空间管理
- **Gamut Mapping**：色域映射
- **Color Space Conversion**：色彩空间转换
- **ASC CDL Export**：导出 CDL 值用于跨系统协作