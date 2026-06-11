---
type: source
title: "Transkoder 2025 用户指南"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - source
  - manual
  - colorfront
  - mastering
status: seed
related:
  - "[[COLORFRONT]]"
  - "[[Transkoder 2025]]"
sources: []
source_type: manual
author: "COLORFRONT"
date_published: 2025-05-06
url: "http://www.transkoder.com"
confidence: high
key_claims:
  - "Transkoder 2025 是 COLORFRONT 的旗舰级数字电影和 UHDTV 母版制作系统，支持 DCP/IMF 母版制作、JPEG2000 编解码、HDR 和 Dolby Vision 工作流。"
  - "支持 Windows 和 macOS 平台，基于 GPU 加速的混合 CPU/GPU 架构，4K DCP/UHD IMF 编码速度可达 100+ fps。"
  - "支持 Dolby Atmos 音频、Dolby Vision HDR、Nagra NexGuard 取证水印、远程参考质量流媒体和 REST API 自动化。"
  - "覆盖安装配置、项目管理、Bin 媒体管理、时间线编辑、Node Page 图像处理管线、调色、渲染、DCP/IMF 封装、QC 工具和云端部署。"
---

# 源：Transkoder 2025 用户指南

**类型**：软件用户手册（HTML 规范化）
**日期**：2026-06-05（规范化处理日期）
**原始文件**：`TKD/TKDUserGuide_dark.html`
**规范化输出**：`TKDUserGuide_dark_normalized/`

## 摘要

Transkoder 2025 用户指南是 COLORFRONT 公司的官方软件手册，涵盖 Transkoder 2025 数字电影母版制作系统的全部功能。手册共 27 章 + 14 个附录，约 17.7 万字，包含 1038 个标题节点和 893 幅参考图片。

核心内容包括：
- **安装与配置**：Windows/macOS 系统要求、安装流程、许可管理、显示校准、视频输出配置（SDI/HDMI/NDI/CDI）
- **项目与媒体管理**：项目创建/管理、Bin 窗口、时间线编辑、元数据处理
- **图像处理管线**：Node Page 节点管线、Grade Template 与 Viewing Template 体系、RAW 解码（ARRI/Sony/RED/BMD）
- **音频处理**：多声道音频、混音、Dolby Atmos 支持
- **调色与 HDR**：CDL/LUT 调色、ACES 色彩空间、Dolby Vision HDR 工作流
- **渲染**：多编码器并行渲染、混合 CPU/GPU 架构、自定义渲染路径
- **DCP 母版制作**：Interop/SMPTE 标准、加密、KDM 生成、3D 立体
- **IMF 母版制作**：Application 2/2E+/4/5、Netflix/Disney/HBO 等交付规范
- **远程工作流**：参考质量流媒体、REST API、云端部署（AWS）
- **QC 与分析**：验证工具、PSNR 分析、位率分析

## 章节结构

| 章节 | 内容 |
|------|------|
| 引言 | Transkoder 2025 概述、关键功能、COLORFRONT 公司介绍 |
| 第1章 | 安装与配置（系统要求、安装、许可、显示校准、视频输出） |
| 第2章 | 项目管理（创建、加载、删除、克隆、模板） |
| 第3章 | Bin（媒体资源管理、导入、搜索、排序） |
| 第4章 | 时间线（创建、编辑、音视频同步） |
| 第5章 | 图像源格式（ARRI/Sony/RED/Blackmagic RAW 等） |
| 第6章 | 音频处理 |
| 第7章 | 元数据 |
| 第8章 | 字幕与隐藏字幕 |
| 第9章 | 视频输出配置 |
| 第10章 | 图像处理管线（Node Page、Grade/Viewing Template） |
| 第11章 | 调色（CDL、LUT、ACES） |
| 第12章 | Node Page 工具详解 |
| 第13章 | 渲染（渲染页面、编码器表、配置面板） |
| 第14章 | DCP 和 IMF 基础（CPL 导入、Reel 创建） |
| 第15章 | DCP 母版制作（Finalize 窗口、加密、KDM） |
| 第16章 | IMF 母版制作（Finalize 窗口、OV/VF 包） |
| 第17章 | Analyzer 分析器 |
| 第18章 | QC 工具 |
| 第19章 | HDR 工作流 |
| 第20章 | Dolby Vision 工作流 |
| 第21章 | 远程流媒体 |
| 第22章 | 远程和云端工作流 |
| 第23章 | Colorfront Web UI |
| 第24章 | 安全加固 |
| 第25章 | 第三方系统对接 |
| 第26章 | 自定义 Transkoder |
| 附录A | 验证 |
| 附录B | 设置页面参考 |
| 附录C | 支持的输入格式 |
| 附录D | 键盘快捷键 |
| 附录E | 编码配置文件 |
| 附录F | 中央数据库配置 |
| 附录G | AWS 单节点部署 |
| 附录H | AWS 多节点部署 |
| 附录I | Bin 窗口搜索查询 |
| 附录J | 控制面板 |
| 附录K | 故障排查 |
| 附录L | Avid Interplay 设置 |
| 附录M | XAMPP 指南 |
| 附录N | 版权与商标声明 |

## 规范化分页文件

- `TKDUserGuide_dark.md` — 完整提取正文（约 3.7 万行）
- `TKDUserGuide_dark__sections/` — 42 个章节分页文件，便于按主题摄取

## 备注

- 原始 HTML 由 Asciidoctor 2.0.10 生成
- 图片资源位于 `images/TKD2025/`（844 个文件）
- 手册版权：(C) COLORFRONT 2025