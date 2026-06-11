---
type: concept
title: "DaVinci PowerGrade Gallery"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - color-grading
  - powergrade
  - gallery
  - still
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 调色流程]]"
  - "[[DRX Grade File]]"
  - "[[YYHG_gallery]]"
sources:
  - "[[YYHG_gallery]]"
complexity: intermediate
domain: "davinci-resolve"
aliases:
  - "PowerGrade 相册"
  - "Gallery Still Album"
---

# DaVinci PowerGrade Gallery

**PowerGrade Gallery** 是 DaVinci Resolve Color Page 中用于存储和管理调色预设的相册系统，允许调色师保存、组织和跨项目共享调色方案。

## Gallery 类型

| 类型 | 说明 |
|------|------|
| **Still** | 普通静帧，保存特定片段的调色快照 |
| **PowerGrade** | 跨项目可用的调色预设相册，可在任意项目中访问 |
| **Timeline** | 当前时间线范围内的静帧集合 |

## 对象层级

DaVinci Resolve 脚本 API 中的 Gallery 对象层级：

```
Project                  # 当前项目
  └── Gallery            # 画廊对象
        └── GalleryStillAlbum  # 相册（Still 或 PowerGrade 集合）
              └── GalleryStill      # 单个静帧引用
```

## 关键 API 方法

| 方法 | 说明 |
|------|------|
| `project:GetGallery()` | 获取 Gallery 对象 |
| `gallery:GetGalleryPowerGradeAlbums()` | 获取所有 PowerGrade 相册 |
| `gallery:GetAlbumName(album)` | 获取相册名称 |
| `album:GetStills()` | 获取相册内所有静帧 |
| `album:GetLabel(still)` | 获取静帧标签名 |
| `album:ExportStills([stills], path, prefix, format)` | 导出静帧为文件 |

## 支持的导出格式

| 格式 | 说明 |
|------|------|
| **drx** | DaVinci Resolve 调色交换格式 |
| **jpg/png** | 图像预览 |
| **dpx** | 电影级图像序列格式 |

## 使用场景

- 保存调色模板（如"日间外景"、"夜间内景"等预设）
- 在多个项目间共享调色风格
- 批量导出调色方案为 DRX 文件
- 通过脚本 API 自动化画廊管理（如 YYHG_gallery 插件）