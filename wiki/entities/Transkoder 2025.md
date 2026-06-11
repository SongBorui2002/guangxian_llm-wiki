---
type: entity
title: "Transkoder 2025"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - entity
  - software
  - mastering
  - dcp
  - imf
status: seed
related:
  - "[[COLORFRONT]]"
  - "[[Transkoder 2025 用户指南]]"
  - "[[DCP 母版制作]]"
  - "[[IMF 母版制作]]"
  - "[[Node Page 图像处理管线]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
entity_type: product
role: "数字电影与 UHDTV 母版制作系统"
first_mentioned: "[[Transkoder 2025 用户指南]]"
---

# Transkoder 2025

**Transkoder 2025**（简称 TKD）是 COLORFRONT 的旗舰级数字电影和超高清电视（UHDTV）母版制作系统。它基于 COLORFRONT 获奖的 On-Set Dailies 架构，利用通用硬件实现超实时处理速度。

## 核心定位

Transkoder 是 DCP 和 IMF 母版制作的终极工具，提供业界最高的 JPEG2000 编解码性能、多 GPU 32 位浮点处理、MXF 封装、加速校验和、加密/解密以及包编辑功能。

## 关键能力

| 领域 | 能力 |
|------|------|
| **DCP 母版** | Interop/SMPTE 标准、加密、KDM 生成、2D/3D 立体、4K 120fps |
| **IMF 母版** | App 2/2E+/4/5、ProRes、Netflix/Disney/HBO 等交付规范 |
| **性能** | 4K DCP/UHD IMF 和 HEVC 编码 100+ fps |
| **RAW 支持** | ARRI ALEXA 65、Varicam 35、Red Weapon 8K 等最高质量去马赛克 |
| **色彩引擎** | 32 位/通道管理色彩管线，兼容 ACES |
| **HDR** | Dolby Vision 支持，行业领先 HDR 母版工具 |
| **音频** | Dolby Atmos 认证，多声道处理 |
| **水印** | Nagra NexGuard 取证水印（4K 高性能） |
| **远程** | 参考质量安全流媒体，REST API 自动化 |
| **平台** | Windows、macOS、AWS 云实例 |

## 平台差异

| 功能 | Windows | macOS |
|------|---------|-------|
| 核心母版制作 | 完整 | 完整 |
| Dailies 功能集 | 完整 | 不可用 |
| OpenFX 插件接口 | 可用 | 不可用 |
| 双视频输出 | 可用 | 不可用 |
| NexGuard 水印 | 可用 | 不可用 |
| Dolby Vision HEVC (DEE) | 可用 | 不可用 |
| Dolby Digital Plus / DDPA | 可用 | 不可用 |
| Avid Interplay 入库 | 可用 | 不可用 |
| 网络存储硬链接 | 可用 | 不可用 |

> [!note]
> Mac 硬件平台性能低于 Windows 配置。推荐使用 Supermicro GPU SuperServer 或 HP Z8 G5 工作站以获得最佳性能。

## 系统要求摘要

- **GPU**：推荐 NVIDIA RTX 系列（多卡可扩展性能）
- **内存**：64GB+（推荐 128GB+）
- **存储**：高速 NVMe SSD
- **操作系统**：Windows 10/11 Pro 或 macOS Ventura+