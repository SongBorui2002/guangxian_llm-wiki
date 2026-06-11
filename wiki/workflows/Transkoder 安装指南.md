---
type: workflow
title: "Transkoder 安装指南"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - installation
  - setup
  - licensing
status: seed
related:
  - "[[Transkoder 2025]]"
  - "[[COLORFRONT]]"
  - "[[Transkoder 2025 用户指南]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
workflow_type: procedure
domain: "transkoder"
prerequisites:
  - "兼容的 Windows 10/11 Pro 或 macOS Ventura+ 工作站"
  - "NVIDIA RTX GPU 驱动"
  - "管理员权限"
  - "有效的 Transkoder 许可证或 Demo 许可"
outputs:
  - "Transkoder 2025 安装完成并可启动"
---

# Transkoder 安装指南

在 Windows 或 macOS 上安装和配置 Transkoder 2025 的完整流程。

## 1. 系统要求

### 推荐 Windows 配置

| 配置 | Supermicro GPU SuperServer 741GE-TNRT | HP Z8 G5 |
|------|--------------------------------------|----------|
| **GPU** | 多 NVIDIA RTX GPU | 多 NVIDIA RTX GPU |
| **内存** | 128GB+ | 128GB+ |
| **存储** | NVMe SSD | NVMe SSD |

### 推荐 Mac 配置

- Apple Mac Studio Ultra

> [!note]
> Mac 平台性能低于 Windows 配置，部分功能（如 NexGuard 水印、OpenFX 插件、双视频输出、Dolby Vision HEVC DEE）仅 Windows 可用。

## 2. Windows 安装流程

### 2.1 准备条件
1. 检查系统满足最低硬件要求
2. 确保操作系统为 Windows 10/11 Pro

### 2.2 下载安装组件
1. 访问 [COLORFRONT 下载中心](https://support.colorfront.com/hc/en-us/categories/115001258983-Download)
2. 下载 Transkoder 2025 安装包

### 2.3 安装驱动和第三方应用
1. 安装最新 NVIDIA RTX GPU 驱动
2. 安装任何必需的第三方组件

### 2.4 安装 Transkoder
1. 运行 Transkoder 安装程序
2. 按提示完成安装
3. 启动应用程序验证安装

## 3. macOS 安装流程

### 3.1 准备条件
- macOS Ventura 或更新版本

### 3.2 下载和安装
1. 下载 macOS 版安装包
2. 安装必需的驱动和第三方应用
3. 安装 Transkoder

## 4. 许可配置

### 4.1 获取 Host ID
启动 Transkoder 获取本机的 Host ID

### 4.2 申请许可证
- **Demo/评估许可**：联系 COLORFRONT 获取临时评估许可
- **正式许可**：通过 COLORFRONT 支持渠道申请

### 4.3 安装许可证
支持两种方式：
- **软件许可证**：直接导入密钥文件
- **Sentinel HASP 加密狗**：插入加密狗授权

### 4.4 许可证续期
按 COLORFRONT 许可协议定期续期

## 5. 显示校准

### 5.1 校准显示器
通过 Transkoder 内置的显示校准工具进行色彩校准

### 5.2 验证校准
使用 Measure Single Patch 或 Custom Patches 验证校准精度

### 5.3 校准预设和文件
- 保存/加载校准预设
- 支持自定义 LUT（视频输出和 Second Head Analyzer）

## 6. 视频输出配置

Transkoder 支持多种视频输出方式：

| 输出方式 | 说明 |
|----------|------|
| **直接显示** | 连接到显示器直接输出 |
| **SDI** | 通过 SDI 接口（Clean Output Controls 可用） |
| **HDMI** | 通过 HDMI 接口（需支持的显卡） |
| **NDI** | 网络设备接口 |
| **CDI** | Colorfront 专用接口 |
| **Tandem** | 双视频输出模式（Dual Video Out） |
| **远程桌面** | Microsoft Remote Desktop |

## 7. 背景渲染配置

可选配置自动调入渲染节点：
- **文件访问配置**（macOS 需额外设置）
- **渲染任务类型**
- **停滞任务超时**
- **强制顺序探针处理**

## 8. 卸载

### Windows 卸载
通过 Windows 控制面板或安装程序卸载

### macOS 卸载
删除 Transkoder 应用程序及相关支持文件