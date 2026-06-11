---
type: concept
title: "DaVinci Fusion 合成"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - fusion
  - compositing
  - vfx
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci Fusion 合成流程]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "Fusion Page"
  - "Fusion 合成"
---

# DaVinci Fusion 合成

**Fusion** 是 DaVinci Resolve 内置的节点式 2D/3D 合成引擎，用于视觉特效、运动图形、合成和高级图像处理。

## 核心概念

### 节点式工作流
- 每个工具是一个节点，连接节点构建处理管线
- 数据从输入节点流向输出节点（Saver/MediaOut）
- 支持 2D 和 3D 节点类型

### 分辨率无关性
- 所有操作基于浮点坐标
- 支持任意分辨率的输入和输出
- DoD（Domain of Definition）自动优化处理范围

## 主要工具类别

| 类别 | 典型工具 |
|------|----------|
| **合成** | Merge、Matte Control、Channel Booleans |
| **变换** | Transform、Crop、Resize、Corner Positioner |
| **色彩** | Color Corrector、Brightness/Contrast、Color Space |
| **滤镜** | Blur、Sharpen、Glow、Depth of Field |
| **遮罩** | Polygon、BSpline、Rectangle、Ellipse、Paint |
| **跟踪** | Tracker、Planar Tracker、Camera Tracker |
| **3D** | 3D Merge、Renderer 3D、Shape 3D、Text 3D |
| **粒子** | pEmitter、pRender、Forces |
| **键控** | Delta Keyer、Ultra Keyer、Chroma Keyer |
| **光流** | Optical Flow、Time Stretcher、Vector Motion Blur |

## 关键节点

| 节点 | 功能 |
|------|------|
| **Merge** | 合成两个输入（前景 + 背景），支持混合模式 |
| **Loader** | 加载素材到 Fusion 中 |
| **Saver** | 渲染输出到文件 |
| **MediaIn** | 从 DaVinci 时间线接收素材 |
| **MediaOut** | 将结果送回 DaVinci 时间线 |
| **Background** | 生成纯色或渐变背景 |
| **Tracker** | 点跟踪，输出运动数据 |
| **Planar Tracker** | 平面跟踪，适合替换屏幕/标志 |

## 3D 合成

Fusion 拥有完整的 3D 环境：
- **3D 节点**：3D Merge、Camera 3D、Light、Renderer 3D
- **材质系统**：支持 Blinn、Phong、Cook-Torrance 等
- **3D 文字**：Text 3D、Shape 3D
- **3D 跟踪**：Camera Tracker（3D 摄像机反求）

## 与 Edit Page 的集成

- **Fusion Clip**：在 Edit 时间线上创建 Fusion 合成片段
- **MediaIn/MediaOut**：时间线素材自动传入/传出 Fusion
- **VFX Connect**：与外部 VFX 软件（如 Nuke、After Effects）的往返工作流