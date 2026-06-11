---
type: concept
title: "CPL（Composition Playlist）"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - imf
  - mastering
status: seed
related:
  - "[[DCP 母版制作]]"
  - "[[IMF 母版制作]]"
  - "[[KDM（Key Delivery Message）]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: intermediate
domain: "transkoder"
aliases:
  - "Composition Playlist"
  - "合成播放列表"
---

# CPL（Composition Playlist）

**CPL**（Composition Playlist，合成播放列表）是一个 XML 文档，定义了 DCP 或 IMF 包中各个资源（音频、视频、字幕）的播放序列。

## 核心功能

- **播放顺序定义**：指定哪个音视频资源以什么顺序播放
- **Reel 结构**：定义 DCP 的 reel 分段
- **语言版本**：在 VF 包中指定替换哪些资源
- **同步信息**：确保音视频和字幕的对应关系

## CPL 导入流程

在 Transkoder 中有两种方式导入 CPL：

### 1. 直接导入 CPL

- 从 Project Load Page 或 `Timeline → Import DCI or IMP CPL`
- 导入后创建新时间线，时间线名称继承自 PKL 的 Content Title 元数据
- 也可导入到已有空时间线中

### 2. 从 AssetMap 导入

- `Timeline → Import CPL from ASSETMAP`
- 选择 Assetmap XML 文件
- 解析元数据后选择目标 CPL
- 支持从 AWS S3 云端导入

## 相关概念

- DCP 的 CPL 和 IMF 的 CPL 结构相似但各有细节差异
- CPL 通过 UUID 引用资源文件（而非直接文件名）
- VF 包的 CPL 引用 OV 包的资源