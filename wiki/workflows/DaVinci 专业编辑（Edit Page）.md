---
type: workflow
title: "DaVinci 专业编辑（Edit Page）"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - editing
  - edit-page
  - workflow
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 媒体导入与整理]]"
  - "[[DaVinci 渲染与交付]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "媒体素材已导入 Media Pool"
  - "项目设置已配置"
outputs:
  - "完成编辑的时间线"
---

# DaVinci 专业编辑（Edit Page）

DaVinci Resolve Edit Page 的完整非线性编辑（NLE）工作流。

## 1. Edit Page 界面

- **Source Viewer**（左上）：源素材监视器
- **Timeline Viewer**（右上）：时间线节目监视器
- **Media Pool**（左侧）：素材库
- **Timeline**（底部）：主时间线编辑区
- **Inspector**（右上）：片段属性检查器
- **Effects Library**（左侧）：效果和转场库

## 2. 创建时间线

1. 右键 Media Pool 空白处 → New Timeline
2. 设置时间线名称、分辨率、帧率
3. 拖入素材开始编辑

## 3. 三点/四点编辑

- **三点编辑**：源素材设 In/Out → 时间线设 In 点 → 插入/覆盖
- **四点编辑**：源素材设 In/Out → 时间线设 In/Out → 自动适配

## 4. 常用编辑操作

| 操作 | 快捷键 | 说明 |
|------|--------|------|
| **插入编辑** | F9 | 在时间线插入片段，后续片段后移 |
| **覆盖编辑** | F10 | 覆盖时间线该位置 |
| **替换编辑** | F11 | 替换片段但保持时长 |
| **波纹删除** | Shift+Delete | 删除片段并闭合间隙 |
| **刀片工具** | B | 切分片段 |
| **修剪工具** | T | 精确修剪片段边界 |

## 5. 修剪模式

| 模式 | 说明 |
|------|------|
| **Ripple** | 单个轨道修剪，后续片段跟随移动 |
| **Roll** | 两个相邻片段间的编辑点滚动 |
| **Slip** | 修剪片段的 In/Out 但保持位置和时长 |
| **Slide** | 移动片段位置但保持时长 |
| **Dynamic Trim** | 实时播放时修剪 |

## 6. 关键帧和效果

- **Inspector** 中所有参数可设关键帧
- 支持位置、缩放、旋转、不透明度等变换
- 支持速度变化（Speed Change）：变速、倒放、冻结帧
- 支持复合片段（Compound Clip）和嵌套时间线

## 7. 多机位编辑

1. 选择所有机位片段
2. 右键 → Create Multicam Clip
3. 在 Multicam Viewer 中实时切换机位
4. 完成后可重新调整切点

## 8. 字幕和隐藏字幕

- 支持 STL、SRT、VTT 等格式导入
- 内置字幕编辑器
- 支持 TTML/IMSC 格式（Netflix 等交付规范）
- 支持隐藏字幕（Closed Captioning）

## 9. 与 Color Page 的衔接

- 编辑完成后切换到 Color Page 开始调色
- 编辑调整（如替换片段）会自动同步到调色节点