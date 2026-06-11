---
type: workflow
title: "DaVinci 媒体导入与整理"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - media
  - ingest
  - organization
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 项目管理]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "DaVinci Resolve 项目已创建"
  - "存储设备已连接"
outputs:
  - "整理完成的媒体素材库"
---

# DaVinci 媒体导入与整理

DaVinci Resolve Media Page 和 Media Pool 的媒体导入和整理流程。

## 1. Media Page 界面

- **Library**（左上）：存储浏览器，浏览本地/网络存储
- **Viewer**（中央）：素材预览
- **Metadata Panel**（右侧）：元数据编辑
- **Audio Panel**：音频波形显示

## 2. 媒体导入方式

| 方式 | 操作 | 适用场景 |
|------|------|----------|
| **拖入 Media Pool** | 从文件管理器拖入 | 快速导入个别文件 |
| **Media Page 浏览** | 在 Library 中浏览并选择 | 浏览和挑选素材 |
| **Clone Tool** | 从存储卡克隆到工作盘 | 现场 DIT 工作流 |
| **导入 XML/AAF/EDL** | 带套片信息导入 | 从其他 NLE 导入项目 |

## 3. Media Pool 管理

### 组织方式
- **Bins**：创建文件夹结构组织素材
- **Smart Bins**：基于元数据规则自动分类
- **Power Bins**：跨项目共享的 Bins

### 素材操作
- 复制/移动素材到 Bins
- 添加标记（Marker）和颜色标签
- 设置 In/Out 点（Subclip 创建）
- 场景检测（Scene Cut Detection）

## 4. 元数据编辑

在 Media Page 的 Metadata 面板中编辑：
- 片段名称、场景、镜号
- 录制日期、摄影机信息
- 自定义元数据字段
- 批量修改多个片段

## 5. 音频同步

| 方式 | 说明 |
|------|------|
| **时间码同步** | 基于时间码自动对齐音频和视频 |
| **波形同步** | 基于音频波形匹配自动同步 |
| **手动同步** | 手动对齐 In 点或标记点 |

## 6. 场景检测

对整条素材进行场景切割：
1. 选择素材 → 右键 → Scene Cut Detection
2. 自动检测剪切点
3. 审阅和调整检测结果
4. 添加剪辑到 Media Pool

## 7. 代理和优化媒体

| 类型 | 说明 |
|------|------|
| **Proxy** | 低分辨率代理文件，减轻编辑负载 |
| **Optimized Media** | 优化的中间格式（如 ProRes 422），提升回放性能 |
| **Render Cache** | 自动缓存渲染复杂的片段/效果 |