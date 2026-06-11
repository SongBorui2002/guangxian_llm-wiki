---
type: concept
title: "DaVinci 节点调色"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - color-grading
  - nodes
  - color
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 调色流程]]"
  - "[[DaVinci HDR 工作流]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "节点式调色"
  - "Color Node Tree"
---

# DaVinci 节点调色

DaVinci Resolve 的调色系统基于**节点式管线**，每个节点代表一个调色操作，节点按连线顺序处理图像。

## 节点类型

| 节点类型 | 功能 | 快捷键 |
|----------|------|--------|
| **Corrector（校正器）** | 标准调色节点，含色轮、曲线、限定器等 | Alt+S |
| **Parallel Mixer（并行混合器）** | 并行处理多个分支后合并 | Alt+P |
| **Layer Mixer（图层混合器）** | 按图层顺序叠加，支持混合模式 | Alt+L |
| **Key Mixer（键混合器）** | 合并多个键/遮罩输出 | Alt+K |
| **Splitter/Combiner** | 分离/合并 RGB 或其他通道 | - |

## 节点序列

典型的调色节点树结构：

```
输入 → [节点1: 降噪] → [节点2: 一级调色] → [节点3: 二级调色]
                                                      ↓
                                              [节点4: 风格化]
                                                      ↓
                                              [节点5: 锐化/KOF] → 输出
```

## 常用节点操作

| 操作 | 说明 |
|------|------|
| **串行节点** | 标准前后连接，每个节点累积效果 |
| **并行节点** | 多个分支同时处理不同区域，最终合并 |
| **图层节点** | 按图层混合，支持不透明度和混合模式 |
| **外部节点** | 对键/遮罩以外的区域调色 |
| **共享节点** | 多个片段共享同一节点，修改一处全部生效 |

## 调色工具（每个 Corrector 节点内）

- **Primary Wheels**：Lift/Gamma/Gain 色轮
- **Curves**：自定义曲线、色相 vs 色相/饱和度/亮度
- **Qualifiers**：基于 HSL/3D/亮度 的限定器抠像
- **Windows**：Power Window（圆形、矩形、多边形、曲线）
- **Trackers**：跟踪 Window 到运动对象
- **Keyframes**：动态调色变化的关键帧
- **Magic Mask**：AI 驱动的自动遮罩（Studio 版）

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| Alt+S | 添加串行节点 |
| Alt+P | 添加并行节点 |
| Alt+L | 添加图层节点 |
| Ctrl+D | 禁用/启用当前节点 |
| Shift+Ctrl+D | 禁用/启用所有节点 |