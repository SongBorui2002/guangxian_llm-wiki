---
type: source
title: "3dResolveSubtitle"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - subtitle
  - stereoscopic-3d
  - dcp
  - source
  - repository
status: seed
related:
  - "[[StereoscopicSubtitlePlugin]]"
  - "[[DaVinci Resolve 20]]"
  - "[[立体 3D 字幕工作流]]"
  - "[[DCDM 字幕]]"
  - "[[DCP 母版制作]]"
sources: []
source_type: repository
author: "SongBorui2002"
date_published: 2026-06-05
url: "https://github.com/SongBorui2002/3dResolveSubtitle"
confidence: high
key_claims:
  - "基于 StereoscopicSubtitlePlugin 的 DaVinci Resolve 立体 3D 字幕工作流扩展，增加了 Python 字幕 XML 生成、XML 转换和 Resolve 连接器脚本。"
  - "用于釜山国际短片电影节（BISFF）立体 3D 放映的字幕制作工作流。"
  - "通过 DaVinci Resolve 调色页面的汇聚值（Convergence）关键帧生成 DCDM 立体字幕 Z 位置信息。"
---

# 源：3dResolveSubtitle

**类型**：Git 仓库快照
**仓库作者**：SongBorui2002
**来源**：`git@github.com:SongBorui2002/3dResolveSubtitle.git`（SSH 克隆）

## 摘要

3dResolveSubtitle 是 DaVinci Resolve 立体 3D 字幕工作流的扩展仓库，在 Alaric Hamacher 的 [[StereoscopicSubtitlePlugin]] 基础上添加了自定义 Python 脚本，用于字幕 XML 生成、格式转换和 DaVinci Resolve API 集成。

## 仓库结构

| 组件 | 说明 |
|------|------|
| `StereoscopicSubtitlePlugin-master/` | 原始立体字幕插件（Electron 应用） |
| `SubtitleXMLGenerator.py` | 字幕 XML 生成器 |
| `convertXML.py` | XML 格式转换工具 |
| `resolveConnector.py` | DaVinci Resolve API 连接器 |
| `subtitles_track2_20260124_110129.xml` | 示例字幕输出文件 |
| `3dResolveSubtitle.code-workspace` | VS Code 工作区文件 |

## 与基础插件的关系

此仓库包含了 StereoscopicSubtitlePlugin 的完整副本，并在此基础上增加了：
- 自定义 XML 生成和转换逻辑
- DaVinci Resolve 脚本 API 集成
- 针对特定项目格式的字幕处理

## 备注

- 依托 DaVinci Resolve Studio 的工作流集成（Workflow Integration）机制
- 目标用途：数字电影立体 3D 放映的字幕制作
- 参考论文：Hamacher, "Digital Cinema Stereoscopic Subtitle Workflow" (IJLEMR, 2024)