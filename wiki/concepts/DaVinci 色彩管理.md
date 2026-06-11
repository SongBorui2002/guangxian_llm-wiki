---
type: concept
title: "DaVinci 色彩管理"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - color-management
  - aces
  - color-science
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 色彩空间与 ACES]]"
  - "[[DaVinci 调色流程]]"
  - "[[DaVinci HDR 工作流]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "DaVinci YRGB Color Science"
  - "DaVinci 色彩科学"
---

# DaVinci 色彩管理

DaVinci Resolve 的色彩管理（Color Management）是项目的核心设置，决定了从摄影机原始素材到最终显示的整个色彩管线。

## 色彩科学

DaVinci Resolve 使用 **DaVinci YRGB** 色彩科学，基于 32 位浮点处理管线：

- **YRGB**：亮度（Y）和色彩（RGB）分量独立处理，调节亮度时不影响色度
- **32 位浮点**：全管线浮点处理精度，避免量化误差

## 色彩管理方式

### 1. DaVinci YRGB（默认）
- 非色彩管理方式
- 适合手动控制色彩管线的每个环节
- 灵活性最高，但需要手动设置色彩空间转换

### 2. DaVinci YRGB Color Managed
- DaVinci 内置的自动色彩管理
- 自动处理输入色彩空间 → 时间线色彩空间 → 输出色彩空间的转换
- 适合大多数标准工作流

### 3. ACES（Academy Color Encoding System）
- 学院色彩编码系统，行业标准
- 标准化的色彩管线，跨系统色彩一致性
- 适合需要跨多个软件协作的工作流

## 关键设置

| 设置 | 说明 |
|------|------|
| **Input Color Space** | 摄影机素材的色彩空间（LogC、S-Log3、REDWideGamut 等） |
| **Timeline Color Space** | 调色工作空间的色彩空间（通常为 DaVinci Wide Gamut Intermediate） |
| **Output Color Space** | 监看输出的色彩空间（Rec.709、Rec.2020、DCI-P3 等） |
| **Tone Mapping** | 高动态范围到标准动态范围的映射方式 |
| **Gamut Mapping** | 色域映射方式 |

## 数据级别

| 级别 | 范围 | 典型用途 |
|------|------|----------|
| **Video** | 64-940（10-bit） | 广播和视频交付 |
| **Full** | 0-1023（10-bit） | 数字电影、VFX 工作流 |

## 相关章节

- 用户手册第 9 章：Data Levels, Color Management, and ACES
- 用户手册第 10 章：HDR Setup and Grading