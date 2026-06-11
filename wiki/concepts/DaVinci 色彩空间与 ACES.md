---
type: concept
title: "DaVinci 色彩空间与 ACES"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - aces
  - color-space
  - color-management
status: seed
related:
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 调色流程]]"
  - "[[DaVinci HDR 工作流]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
complexity: advanced
domain: "davinci-resolve"
aliases:
  - "ACES in DaVinci Resolve"
---

# DaVinci 色彩空间与 ACES

DaVinci Resolve 支持 ACES（Academy Color Encoding System）作为色彩管理管线，提供标准化的跨系统色彩一致性。

## ACES 的核心理念

- **IDT**（Input Device Transform）：将摄影机原始色彩空间转换到 ACES
- **ACES 工作空间**：线性光照色彩空间，所有操作在此进行
- **RRT**（Reference Rendering Transform）：参考渲染变换
- **ODT**（Output Device Transform）：将 ACES 转换到目标显示设备

## ACES 版本

DaVinci Resolve 20 支持：
- **ACES 1.3**：当前主流版本
- **ACES 2.0**：最新版本（手册为 2025 年 7 月版）

## 设置 ACES 工作流

1. 在项目设置中设置 Color Science 为 ACES
2. 选择 ACES 版本
3. 配置 ACES Input Transform（摄影机 IDT）
4. 配置 ACES Output Transform（监看 ODT）
5. 设置 ACES Working Space

## 常用色彩空间

| 色彩空间 | 说明 |
|------|------|
| **Rec.709** | 标准高清电视色彩空间 |
| **Rec.2020** | 超高清电视（含 HDR）色彩空间 |
| **DCI-P3** | 数字电影色彩空间 |
| **ACES AP0** | ACES 原始色彩空间（超宽色域） |
| **ACES AP1** | ACES 工作色彩空间 |
| **DaVinci Wide Gamut** | DaVinci 自己的宽色域中间空间 |
| **ARRI Wide Gamut** | ARRI 摄影机色彩空间 |
| **S-Gamut3.Cine** | Sony 摄影机色彩空间 |

## 色彩空间转换

DaVinci 支持在节点级别进行色彩空间转换：
- **Color Space Transform（CST）** 节点
- 输入/输出色彩空间和 Gamma 转换
- 支持自定义 Tone Mapping 和 Gamut Mapping 方法