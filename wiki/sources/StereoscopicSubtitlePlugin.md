---
type: source
title: "StereoscopicSubtitlePlugin"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - subtitle
  - stereoscopic-3d
  - dcdm
  - workflow-integration
  - source
  - repository
status: seed
related:
  - "[[3dResolveSubtitle]]"
  - "[[DaVinci Resolve 20]]"
  - "[[Alaric Hamacher]]"
  - "[[立体 3D 字幕工作流]]"
  - "[[DCDM 字幕]]"
  - "[[DCP 母版制作]]"
sources: []
source_type: repository
author: "Alaric Hamacher (stereo3d)"
date_published: 2024-02-01
url: "https://github.com/stereo3d/StereoscopicSubtitlePlugin"
confidence: high
key_claims:
  - "DaVinci Resolve Studio 的工作流集成插件，用于创建符合 SMPTE 标准的立体 3D 数字电影字幕。"
  - "从调色页面的汇聚值（Convergence）关键帧导出 DCDM 立体字幕的 VariableZ 位置信息。"
  - "已在釜山国际短片电影节（BISFF）的立体 3D 放映中得到实际应用。"
---

# 源：StereoscopicSubtitlePlugin

**类型**：Git 仓库快照（DaVinci Resolve Workflow Integration Plugin）
**仓库作者**：Alaric Hamacher（stereo3d）
**来源**：`git@github.com:stereo3d/StereoscopicSubtitlePlugin.git`（SSH 克隆）
**版本**：v1.1.0

## 摘要

StereoscopicSubtitlePlugin 是一个基于 Electron 的 DaVinci Resolve 工作流集成插件，用于创建符合 SMPTE DCDM 标准的立体 3D 字幕。该插件填补了数字电影立体字幕制作工具的空白，利用 DaVinci Resolve 的脚本功能实现了从 2D 字幕到立体 3D 字幕的高效工作流。

## 技术栈

| 层面 | 技术 |
|------|------|
| **框架** | Electron |
| **XML 生成** | xmlbuilder2 (npm) |
| **时间码** | 自定义 smpte-timecode.js |
| **字幕 XML** | subtitlexml.js（DCDM 立体字幕格式） |
| **平台** | DaVinci Resolve Studio (Workflow Integration) |
| **安装路径** | `/Library/Application Support/Blackmagic Design/Davinci Resolve/Workflow Integration Plugins/` |

## 安装

```bash
# 复制插件到 DaVinci Resolve 工作流集成目录
cp -r StereoscopicSubtitlePlugin/ \
  "/Library/Application Support/Blackmagic Design/Davinci Resolve/Workflow Integration Plugins/"
```

重启 DaVinci Resolve 后，通过菜单 `Workspace → Workflow Integrations` 调用。

## 限制

- 处于早期开发阶段，结果需仔细验证
- VariableZ 位置信息从关键帧汇聚值导出，在 SMPTE 规范中为可选参数
- DCP-o-Matic（v2.18.15+）支持 DCDM 字幕中的 VariableZ
- EasyDCP Player 和 DCP-o-Matic Player 在播放时忽略 VariableZ 参数

## 学术参考

- 论文：Hamacher, A. (2024). "Digital Cinema Stereoscopic Subtitle Workflow". IJLEMR, 9(2), 51-59.
- DOI: [10.56581/IJLEMR.9.02.51-59](https://doi.org/10.56581/IJLEMR.9.02.51-59)
- 相关仓库：[DCDM_3DSUB_XSLT](https://github.com/stereo3d/DCDM_3DSUB_XSLT)（XSLT 转换和验证工具）