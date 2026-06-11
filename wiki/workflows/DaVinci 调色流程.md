---
type: workflow
title: "DaVinci 调色流程"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - color-grading
  - workflow
  - color-page
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 节点调色]]"
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci HDR 工作流]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "DaVinci Resolve 项目已设置色彩管理"
  - "素材已导入时间线"
  - "可选：参考监视器已校准"
outputs:
  - "调色完成的片段，可渲染或导出"
---

# DaVinci 调色流程

DaVinci Resolve Color Page 的完整调色工作流，从设置到最终输出。

## 1. 项目色彩管理设置

在开始调色前，配置项目色彩管理：
- 设置 **Color Science**：DaVinci YRGB / DaVinci YRGB Color Managed / ACES
- 配置 **Input Color Space**（摄影机色彩空间）
- 设置 **Timeline Color Space**（工作空间）
- 配置 **Output Color Space**（监看输出）

## 2. Color Page 界面

按工作区分为：
- **Gallery**（左上）：静帧库和调色参考
- **Viewer**（中央）：节目监视器
- **Node Editor**（右上）：节点树
- **Color Tools**（右下）：色轮、曲线、限定器等
- **Timeline**（底部）：时间线缩略图

## 3. 典型调色节点序列

```
节点1: 降噪（NR）       → 可选，处理噪点
节点2: 一级调色（Primary） → Lift/Gamma/Gain 平衡
节点3: 二级调色（Secondary）→ 限定器/窗口特定区域
节点4: 风格化（Look）     → LUT/Creative 风格
节点5: 锐化/输出          → 最终锐化或 KOF
```

## 4. 一级调色（Primary Grading）

| 工具 | 快捷键 | 功能 |
|------|--------|------|
| **Lift** | 色轮 | 阴影区域调整 |
| **Gamma** | 色轮 | 中间调区域调整 |
| **Gain** | 色轮 | 高光区域调整 |
| **Offset** | 色轮 | 整体色彩偏移 |
| **Contrast/Pivot** | 滑块 | 对比度和中心点 |
| **Saturation** | 滑块 | 饱和度 |

## 5. 二级调色（Secondary Grading）

### 限定器（Qualifier）
- **HSL Qualifier**：基于色相/饱和度/亮度选取
- **3D Qualifier**：三维色彩空间选取
- **Luminance Qualifier**：基于亮度选取

### Power Windows
- 圆形、矩形、多边形、曲线/PowerCurve
- 支持渐变羽化
- 可跟踪到运动对象

## 6. 常用调色技巧

| 技巧 | 操作 |
|------|------|
| **肤色校正** | 限定器选取肤色区域 → 单独调整 |
| **天空增强** | Window 限定天空 → 降低 Lift、增加饱和度 |
| **画面平衡** | 使用 Waveform 示波器确保曝光一致 |
| **色彩匹配** | 使用 Gallery 静帧作为参考 → 匹配画面色彩 |
| **节点拷贝** | 选中节点 → 拖拽到其他片段 |

## 7. 调色示波器

| 示波器 | 用途 |
|--------|------|
| **Waveform** | 亮度分布（IRE 0-100） |
| **Parade** | RGB 分量亮度分布 |
| **Vectorscope** | 色彩和饱和度 |
| **Histogram** | 像素亮度分布统计 |
| **C.I.E. Chromaticity** | 色域覆盖范围 |

## 8. 保存和导出

- **静帧保存**：右键 → Grab Still → 保存到 Gallery
- **PowerGrade**：保存为可跨项目共享的调色预设
- **LUT 导出**：导出为 3D LUT 用于其他系统
- **CDL 导出**：导出 ASC CDL 值用于跨系统交换