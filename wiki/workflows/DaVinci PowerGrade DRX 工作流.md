---
type: workflow
title: "DaVinci PowerGrade DRX 工作流"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - powergrade
  - drx
  - color-grading
  - automation
status: seed
related:
  - "[[YYHG_gallery]]"
  - "[[DaVinci PowerGrade Gallery]]"
  - "[[DRX Grade File]]"
  - "[[DaVinci 调色流程]]"
sources:
  - "[[YYHG_gallery]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "DaVinci Resolve Studio"
  - "YYHG_gallery 插件已安装"
  - "PowerGrade 相册中包含目标调色静帧"
outputs:
  - "DRX 文件导出或调色应用到时间线片段"
---

# DaVinci PowerGrade DRX 工作流

利用 YYHG_gallery 插件自动化管理 PowerGrade 画廊的 DRX 导出和应用流程。

## 工作流概览

```
PowerGrade 相册 → 选择目标静帧 → 导出 DRX → 应用到时间线片段
```

## 两步流程

### 1. 从 PowerGrade 导出 DRX（Export）

1. 在 DaVinci Resolve 中打开目标项目
2. 通过 `Workspace → Workflow Integrations → YYHG Gallery Plugin` 打开插件
3. 选择目标 PowerGrade 相册（如 `YYHG_before2`）
4. 选择要导出的静帧（匹配标签名，如 `B_0039C025_240525_112432_a1D2J.mov`）
5. 执行导出 → 静帧以 DRX 格式保存到指定目录

**API 调用链：**
```
Project → GetGallery()
Gallery → GetGalleryPowerGradeAlbums()
Gallery → GetAlbumName(album)        # 匹配相册名
Album  → GetStills()                 # 获取静帧列表
Album  → GetLabel(still)             # 匹配静帧标签
Album  → ExportStills([stills], path, prefix, "drx")
```

### 2. 将 DRX 应用到片段（Apply）

1. 在 Color Page 上，将 playhead 定位到目标片段
2. 选择之前导出的 DRX 文件
3. 执行应用 → 调色数据加载到当前片段的节点图

**API 调用链：**
```
Project → GetCurrentTimeline()
Timeline → GetCurrentVideoItem()     # 获取 playhead 所在片段
Clip    → GetNodeGraph()             # 获取节点图
Graph   → ApplyGradeFromDRX(path, gradeMode)
```

### 3. 一体化工作流（Export + Apply）

使用 `export_and_apply_powergrade.lua` 脚本可一键完成：
1. 从 PowerGrade 相册导出指定静帧为 DRX
2. 自动定位桌面上最新导出的 DRX 文件
3. 将 DRX 应用到当前时间线的 playhead 片段

## 常见问题排查

| 问题 | 解决方法 |
|------|----------|
| **ExportStills 返回 true 但找不到文件** | 导出文件名可能包含额外后缀，使用前缀匹配搜索 `.drx` 文件 |
| **无法获取 Gallery** | 优先使用 `project:GetGallery()`；确保当前项目已打开 |
| **无法找到 clip** | 确保在 Color 页面且 playhead 位于目标片段 |
| **权限不足** | macOS 使用 `sudo` 运行安装脚本；Windows 以管理员身份运行 |

## 批量处理场景

- 将一套调色风格批量应用到多个镜头
- 从模板项目导出调色预设，在新项目中批量应用
- 跨项目复制 PowerGrade 调色方案