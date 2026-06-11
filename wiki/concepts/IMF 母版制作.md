---
type: concept
title: "IMF 母版制作"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - imf
  - mastering
  - delivery
  - streaming
status: seed
related:
  - "[[DCP 母版制作]]"
  - "[[JPEG2000 编解码]]"
  - "[[Transkoder 2025]]"
  - "[[IMF 包创建流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: advanced
domain: "transkoder"
aliases:
  - "Interoperable Master Format"
  - "IMP"
---

# IMF 母版制作

**IMF**（Interoperable Master Format，互操作母版格式）是一种基于 J2K 压缩的单一可交换母版文件格式，旨在最小化存储需求并支持灵活的版本管理。一个 IMF 包（IMP）可以包含同一内容的多个版本：不同语言、宽高比或播放列表。

## 核心概念

IMF 基于 DCP 概念但更为灵活，专为流媒体和广播分发场景设计：

| 组件 | 说明 |
|------|------|
| **CPL**（Composition Playlist） | 定义播放序列和资源组合 |
| **OPL**（Output Profile List） | 定义输出色彩空间和分辨率映射 |
| **PKL**（Packing List） | 包文件清单和校验和 |
| **AssetMap** | 文件 UUID 和路径映射 |
| **VolIndex** | 卷索引文件 |

## Transkoder 支持的 IMF 规范

| 规范 | 说明 |
|------|------|
| **Application 2** | 基础 IMF 应用（HD） |
| **Application 2 Extended+** | 扩展的 App 2（QHD/UHD 支持） |
| **Application 4** | 影院级母版 |
| **Application 5** | ACES 色彩空间母版 |
| **ProRes IMF** | 基于 ProRes 编码的 IMF |

### 支持的参数范围

| 参数 | 可选值 |
|------|--------|
| **分辨率** | HD、QHD、4K |
| **色彩编码** | YUV、RGB |
| **位深** | 10-bit、12-bit、16-bit |
| **帧率** | 23.976、24、25、29.97、30、48、50、59.94、60 |
| **压缩** | Lossy（有损）/ Lossless（无损） |

### 流媒体平台交付规范

Transkoder 支持以下平台的 IMF 交付规范：
- **Netflix**、**Disney**、**Fox**、**Sony**、**HBO**、**Hulu**、**Warner**

## IMF vs DCP

| 维度 | IMF | DCP |
|------|-----|-----|
| **主要用途** | 流媒体/广播母版 | 影院放映 |
| **版本管理** | 单一包支持多版本 | 通过 VF 补充包 |
| **Reel 要求** | 无强制 reel 约束 | 音视频事件需按 reel 结构对齐 |
| **编码** | J2K（有损/无损） | J2K（仅无损可选） |
| **HDR 选项** | 支持 HDR | 标准动态范围为主 |

## 关键设置（Finalize 窗口）

| 参数 | 说明 |
|------|------|
| **Package** | OV（原始版本）或 VF（版本文件） |
| **Source** | V1 track 或 V1 + 已选轨道 |
| **Strategy** | 渲染策略（同 DCP 体系） |
| **Content Title** | 包标识符，自动生成但可手动修改 |
| **Issuer** | 包发行方（机构名称） |
| **Content Originator** | 内容原创方 |
| **Annotation** | 注解文本，点击 Calculate 刷新 |
| **Version** | 版本号：1-9、A-H 或无 |

## 渲染输出位置

IMF 包的 XML（PKL、CPL、OPL、Assetmap、Volindex）和视频/音频 MXF 的符号链接生成到：
```
ProjectBasePath\generated\IMF\IMP\
```