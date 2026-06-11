---
type: workflow
title: "DaVinci 渲染与交付"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - rendering
  - deliver
  - export
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 调色流程]]"
  - "[[Transkoder 2025]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "时间线编辑和调色完成"
  - "音频混音完成"
outputs:
  - "最终渲染的交付文件"
---

# DaVinci 渲染与交付

DaVinci Resolve Deliver Page 的渲染和交付流程，支持多种格式和输出目标。

## 1. Deliver Page 界面

按工作区分为：
- **Render Settings**（左侧）：渲染参数配置
- **Render Queue**（右侧）：渲染队列管理
- **Timeline**（底部）：时间线范围选择

## 2. 渲染设置

### 输出格式

| 格式 | 典型用途 |
|------|----------|
| **QuickTime** | ProRes/DNxHR 中间格式、H.264/H.265 交付 |
| **MXF OP-Atom** | Avid 兼容交付 |
| **MXF OP1a** | 广播和归档交付 |
| **MP4** | H.264/H.265 网络分发 |
| **IMF** | 流媒体母版（Studio 版） |
| **DCP** | 数字电影包（Studio 版） |
| **Image Sequence** | TIFF/DPX/EXR 序列（VFX/归档） |
| **Audio Only** | WAV/BWF 音频导出 |

### 编码器

| 编码器 | 说明 |
|--------|------|
| **H.264** | 通用网络分发 |
| **H.265/HEVC** | 4K/HDR 网络分发 |
| **Apple ProRes** | 专业中间格式（422/422HQ/4444/4444XQ） |
| **Avid DNxHR** | Avid 兼容中间格式（LB/SQ/HQ/HQX） |
| **JPEG2000** | DCP/IMF 编码 |
| **Uncompressed** | 无压缩/YUV/RGB |

### 渲染范围

- **Entire Timeline**：整条时间线
- **In/Out Range**：I/O 标记范围
- **Selected Clips**：选中片段

## 3. 渲染队列

- 添加多个渲染任务到队列
- 支持批量渲染到不同格式
- 可设置渲染后操作（如验证、上传到 Frame.io）

## 4. 常见交付场景

### 网络分发（YouTube/Vimeo）
- 格式：MP4 (H.264)
- 分辨率：1920x1080 或 3840x2160
- 比特率：20-50 Mbps（1080p）/ 50-100 Mbps（4K）
- 音频：AAC 320 kbps

### 电视台交付
- 格式：MXF OP1a (XDCAM HD 422 或 AVC-Intra)
- 分辨率：1920x1080
- 帧率：25/29.97 fps
- 音频：PCM 24-bit 48kHz

### 影院/DCP 母版
- 格式：DCP（JPEG2000 MXF）
- 分辨率：2K (1998x1080) 或 4K (3996x2160)
- 色彩空间：DCI-P3 / XYZ
- Studio 版支持 DCP 封装

### VFX 输出
- 格式：DPX 序列 或 OpenEXR 序列
- 分辨率：原始分辨率
- 色彩空间：ACES 或 Linear
- 包含元数据（时间码、Reel 名）

## 5. 数据烧录（Data Burn-In）

在渲染时添加烧录信息：
- 源文件名和时间码
- 自定义文字
- 录制日期、卷号、片名
- 可自定义字体、大小和位置

## 6. 与 Transkoder 的协作

DaVinci Resolve 和 Transkoder 2025 的典型协作流程：
1. DaVinci 输出 TIFF/DPX 序列或 ProRes 4444 中间格式
2. 在 Transkoder 中进行最终 DCP/IMF 封装
3. Transkoder 提供更专业的 JPEG2000 编码和 KDM 生成