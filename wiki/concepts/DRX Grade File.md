---
type: concept
title: "DRX Grade File"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - drx
  - color-grading
  - grade
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci PowerGrade Gallery]]"
  - "[[DaVinci 调色流程]]"
  - "[[YYHG_gallery]]"
sources:
  - "[[YYHG_gallery]]"
complexity: basic
domain: "davinci-resolve"
aliases:
  - "DRX 调色文件"
  - "DaVinci Resolve Exchange"
---

# DRX Grade File

**DRX**（DaVinci Resolve Exchange）是 DaVinci Resolve 的调色交换格式，用于在不同项目或系统之间传输调色数据。

## 格式特性

- **专有格式**：DaVinci Resolve 的调色数据交换文件
- **包含数据**：节点树、色轮参数、曲线、LUT 引用、关键帧等完整调色信息
- **跨项目**：可在不同项目和系统间共享

## DRX 导出

从 PowerGrade Gallery 导出 DRX：

```lua
-- DaVinci Resolve 脚本 API
galleryStillAlbum:ExportStills(
    {galleryStill},  -- 要导出的静帧列表
    folderPath,      -- 目标文件夹
    filePrefix,      -- 文件名前缀
    "drx"            -- 格式
)
```

> [!note]
> 导出文件名可能包含额外后缀（如 `prefix_1.2.1.drx`），脚本中应使用前缀匹配查找。

## DRX 应用

将 DRX 应用到时间线片段：

```lua
-- 获取当前片段
local timeline = project:GetCurrentTimeline()
local clip = timeline:GetCurrentVideoItem()

-- 应用 DRX
local graph = clip:GetNodeGraph()
graph:ApplyGradeFromDRX(drx_path, gradeMode)
```

### gradeMode 参数

| 值 | 模式 | 说明 |
|----|------|------|
| `0` | No keyframes | 不应用关键帧，仅应用静态调色值 |
| `1` | Source Timecode aligned | 按源时间码对齐关键帧 |
| `2` | Start Frames aligned | 按起始帧对齐关键帧 |

## 与其他格式的对比

| 格式 | 用途 | 包含 |
|------|------|------|
| **DRX** | 调色交换 | 完整节点树和参数 |
| **LUT**（.cube/.3dl） | 色彩转换 | 仅色彩映射（无节点信息） |
| **CDL**（.cdl） | 基础调色 | Slope/Offset/Power/Saturation |
| **DPX/TIFF** | 静帧导出 | 渲染后的图像数据 |