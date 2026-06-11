---
type: workflow
title: "DaVinci 项目管理"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - project-management
  - database
  - collaboration
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 媒体导入与整理]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "DaVinci Resolve 20 安装完成"
outputs:
  - "配置好的项目库和项目结构"
---

# DaVinci 项目管理

DaVinci Resolve 的项目管理、项目库和协作工作流。

## 1. 项目库（Project Library）

DaVinci Resolve 使用基于数据库的项目管理系统：

### 数据库类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| **本地数据库** | 存储在本地磁盘的 PostgreSQL 数据库 | 单用户工作 |
| **网络数据库** | 存储在共享服务器的 PostgreSQL 数据库 | 协作工作流 |

### 项目库操作

- 创建/删除项目库
- 连接/断开网络数据库
- 备份和恢复项目库

## 2. 项目管理

### 创建项目

1. 打开 Project Manager（项目管理器）
2. 右键项目库 → New Project
3. 设置项目名称和基本参数

### 项目操作

| 操作 | 说明 |
|------|------|
| **保存** | Ctrl+S，自动保存到此项目库 |
| **另存为** | 创建项目副本 |
| **导出项目** | 导出 .drp 项目文件（可跨系统迁移） |
| **导入项目** | 导入 .drp 文件 |
| **归档** | 打包项目及所有素材到指定位置 |

## 3. 项目设置

### 主设置（Master Settings）
- **Timeline Resolution**：时间线分辨率（如 3840x2160）
- **Pixel Aspect Ratio**：像素宽高比（通常 Square）
- **Timeline Frame Rate**：项目帧率（23.976/24/25/29.97/30/48/50/59.94/60）
- **Video Monitoring**：视频监看输出配置

### 色彩管理（Color Management）
- **Color Science**：DaVinci YRGB / DaVinci YRGB Color Managed / ACES
- **Timeline Color Space**：时间线色彩空间
- **Output Color Space**：输出色彩空间

### 音频设置
- 采样率（48kHz/96kHz/192kHz）
- 音频位深（16-bit/24-bit/32-bit float）
- 音频输出配置

## 4. 协作工作流

DaVinci Resolve Studio 支持多用户协作：

| 功能 | 说明 |
|------|------|
| **共享项目库** | 使用 PostgreSQL 网络数据库 |
| **同时协作** | 多用户同时在同一项目上工作 |
| **角色锁定** | 防止多人同时编辑同一片段 |
| **聊天** | 内置聊天功能 |

## 5. 偏好设置

DaVinci Resolve → Preferences：
- **System**：内存使用、GPU 配置、媒体存储
- **User**：UI 设置、键盘快捷键、控制面板
- **Media**：代理和优化媒体设置
- **Playback**：回放质量和性能设置