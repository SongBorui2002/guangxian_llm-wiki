---
type: concept
title: "Node Page 图像处理管线"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - node-page
  - image-processing
  - pipeline
status: seed
related:
  - "[[Transkoder 2025]]"
  - "[[Transkoder 渲染流程]]"
  - "[[Transkoder 调色流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: advanced
domain: "transkoder"
aliases:
  - "节点页面"
  - "Node Pipeline"
  - "图像处理管线"
---

# Node Page 图像处理管线

Node Page 是 Transkoder 的核心图像处理界面，通过节点管线灵活定制图像处理链。每个节点代表一种图像处理操作，每个片段拥有独立的节点管线。

## 页面结构

Node Page 使用三段式布局（按 `Enter` 键进入）：

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   SOURCE     │  │   PIPELINE   │  │   RESULT    │
│   (浅灰)     │  │   (深灰)     │  │   (浅灰)     │
│              │  │              │  │              │
│  输入图像    │  │  节点管线    │  │  输出结果    │
│  缓冲区      │  │              │  │  缓冲区      │
└─────────────┘  └─────────────┘  └─────────────┘
```

灰色分隔线的左侧节点属于 **Grade Template**（片段级），右侧节点来自 **Viewing Template**（项目全局）。

## 两种模板

### Grade Template（等级模板）
- **片段级别**，每个片段独有
- 首次加载片段时，从 Grade Template 加载
- 每种摄影机格式有独立的 Grade Template
- 处理不同色彩空间和几何属性

### Viewing Template（查看模板）
- **项目全局**模板
- 所有片段共享
- 位于管线右侧

### 快捷键操作

| 快捷键 | 功能 |
|--------|------|
| **Shift+Y** | 仅保存 Viewing Template |
| **Shift+T** | 同时保存 Grade 和 Viewing Template |
| **Ctrl+S** | 常规保存 |
| **Enter** | 进入/确认 Node Page |

> [!warning]
> Shift+T 保存两个模板时，会覆盖时间线上其他片段的节点设置。

## 图像源格式

Node Page 左侧显示当前摄影机格式及相关信息。支持的 RAW 格式包括：
- ARRIRAW、ARRI ProRes
- Sony RAW（X-OCN）
- RED RAW
- Blackmagic RAW
- Canon RAW
- 其他通用视频/图像格式

## 输出结果（Result）

右侧 Result 面板可配置多个并行输出，每个可以有不同的：
- 取景（Framing）
- 分辨率
- 色彩空间
- 编码格式

## 相关工具页

- **Node Page 工具详解**（用户指南第 12 章）：各节点功能参数说明
- **Render Page**（按 `P` 键）：编码器配置和渲染启动