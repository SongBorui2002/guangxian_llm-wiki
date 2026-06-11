---
type: concept
title: "DCP 母版制作"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - mastering
  - cinema
  - jpeg2000
status: seed
related:
  - "[[IMF 母版制作]]"
  - "[[JPEG2000 编解码]]"
  - "[[Transkoder 2025]]"
  - "[[DCP 包创建流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: advanced
domain: "transkoder"
aliases:
  - "Digital Cinema Package"
  - "数字电影包"
---

# DCP 母版制作

**DCP**（Digital Cinema Package，数字电影包）是发送到影院的一组数字文件集合，是数字电影分发的行业标准格式。

## 核心概念

DCP 包含以下关键组件：

| 组件 | 说明 |
|------|------|
| **MXF 视频** | JPEG2000 压缩的视频轨道（2K 或 4K） |
| **MXF 音频** | 24-bit PCM WAV 音频轨道 |
| **MXF 字幕** | 支持 MXF、PNG、XML InterOp、XML SMPTE 等格式 |
| **CPL**（Composition Playlist） | 定义播放顺序和资源组合的 XML |
| **PKL**（Packing List） | 列出包中所有文件及其校验和 |
| **AssetMap** | 记录每个文件的 UUID 和路径映射 |
| **KDM**（Key Delivery Message） | 加密影片的解密密钥 |

## Transkoder 支持的 DCP 格式

- **标准**：Interop、SMPTE A/B2.0/B2.1(RDD52)/C/D
- **加密**：加密/非加密
- **分辨率**：2K / 4K
- **宽高比**：Flat（1.85:1）/ Scope（2.39:1）/ Full
- **帧率**：标准帧率和高帧率（最高 120fps）
- **立体**：2D / 3D 立体
- **包类型**：OV（Original Version，原始版本）/ VF（Version File，版本文件）
- **音频**：多种配置 + Dolby Atmos
- **字幕**：含动画字幕和隐藏字幕（SMPTE Timed Text）

## 关键设置（Finalize 窗口）

### DCP Settings 选项卡

| 参数 | 说明 |
|------|------|
| **Standard** | Interop（推荐新手/电影节）/ SMPTE A/B2.0/B2.1/C/D |
| **Encrypt** | 启用 DCI 内容加密 |
| **Stereo** | 启用 3D 立体标志（支持 4K 3D 120fps） |
| **Package** | OV（原始版本）或 VF（版本文件） |
| **Strategy** | 渲染策略：单片段 / 整条时间线 / 按 Reel 标记 |
| **Atmos** | Dolby Atmos 项目自动开启 |
| **Content** | 内容类型：feature/trailer/short 等 |
| **Territory** | 目标地区/国家 |

### DCP Encode 选项卡

- JPEG2000 编码配置（质量、比特率）
- 自适应 J2K 编码与 PSNR/比特率目标定位

### DCP KDM 选项卡

- KDM 生成，支持取证水印
- 可选择特定设备的解密密钥

## 渲染策略

| 策略 | 适用场景 |
|------|----------|
| **Per Event** | 时间线上每个视频事件单独渲染为一个 reel |
| **Per Reel** | 按 Reel 标记渲染，需在时间线上设置 In/Out 标记点 |
| **Composition** | 整条时间线作为一个渲染单元 |

## 相关概念

- [[CPL（Composition Playlist）]]
- [[KDM（Key Delivery Message）]]
- [[OV vs VF Package]]
- [[JPEG2000 编解码]]