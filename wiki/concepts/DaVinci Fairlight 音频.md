---
type: concept
title: "DaVinci Fairlight 音频"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - fairlight
  - audio
  - sound
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 渲染与交付]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "Fairlight Audio"
  - "Fairlight 音频后期"
---

# DaVinci Fairlight 音频

**Fairlight** 是 DaVinci Resolve 内置的专业音频后期制作工具，提供完整的录音、编辑、混音和母版制作功能。

## 核心组件

| 组件 | 功能 |
|------|------|
| **Fairlight Timeline** | 音频轨道编辑，支持无限轨道 |
| **Fairlight Mixer** | 专业调音台界面，支持 EQ、动态、插件 |
| **Fairlight Effects** | 内置音频效果器（EQ、压缩、混响、延迟等） |
| **Fairlight Meters** | 专业音频测量（LUFS、RMS、True Peak） |
| **ADR** | 自动对白替换工具 |
| **Foley** | 拟音录制和编辑 |
| **Automation** | 自动控制：音量、声像、插件参数 |

## 轨道类型

| 类型 | 说明 |
|------|------|
| **Mono** | 单声道 |
| **Stereo** | 立体声 |
| **5.1** | 环绕声 |
| **7.1** | 高级环绕声 |
| **7.1.4** | 3D 沉浸式音频（含高度声道） |
| **Dolby Atmos** | 杜比全景声对象音频 |

## 混音台（Mixer）

- 每个轨道有独立的通道条
- 支持 EQ、Dynamics、插件
- 发送/返回（Send/Return）效果
- 编组（Group）和 VCA 控制
- 总线（Bus）路由

## 主要效果器

| 类别 | 效果器 |
|------|--------|
| **EQ** | 6 段参数 EQ、图形 EQ |
| **动态** | 压缩器、限制器、扩展器、门限、De-Esser |
| **混响** | 板式、厅堂、房间等 |
| **延迟** | 延时、回声 |
| **调制** | 合唱、镶边、相位 |
| **修复** | 降噪、去嗡嗡声、去咔哒声 |

## 响度标准

| 标准 | 目标响度 | 说明 |
|------|----------|------|
| **EBU R128** | -23 LUFS | 欧洲广播标准 |
| **ATSC A/85** | -24 LKFS | 北美广播标准 |
| **Netflix** | -27 LKFS | 流媒体平台标准 |
| **YouTube** | -14 LUFS | 网络分发标准 |

## 音频交付

- 支持多声道 WAV/BWF 导出
- 支持嵌入到视频文件中
- 支持 Dolby Atmos ADM 导出（Studio 版）