---
type: source
title: "YYHG_gallery"
created: 2026-06-05
updated: 2026-06-05
tags:
  - davinci-resolve
  - powergrade
  - gallery
  - drx
  - color-grading
  - workflow-integration
  - source
  - repository
status: seed
related:
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci PowerGrade Gallery]]"
  - "[[DRX Grade File]]"
  - "[[DaVinci PowerGrade DRX 工作流]]"
  - "[[DaVinci 调色流程]]"
sources: []
source_type: repository
author: "SongBorui2002"
date_published: 2026-06-05
url: "https://github.com/SongBorui2002/YYHG_gallery"
confidence: high
key_claims:
  - "DaVinci Resolve 工作流集成插件，用于自动化 PowerGrade 画廊的 DRX 导出和应用操作。"
  - "通过 DaVinci Resolve 脚本 API（Lua/fuscript）实现从 PowerGrade 相册批量导出静帧为 DRX 文件，并应用到时间线片段。"
  - "跨平台支持（Windows/macOS），提供一键安装脚本。"
---

# 源：YYHG_gallery

**类型**：Git 仓库快照（DaVinci Resolve Workflow Integration Plugin）
**仓库作者**：SongBorui2002
**来源**：`git@github.com:SongBorui2002/YYHG_gallery.git`（SSH 克隆）
**插件名称**：ProjectInfoPlugin（菜单显示为 "YYHG Gallery Plugin"）

## 摘要

YYHG_gallery 是一个 DaVinci Resolve 工作流集成插件，用于自动化 PowerGrade 画廊管理。它利用 DaVinci Resolve 的 Lua 脚本 API，实现从 PowerGrade 相册导出调色静帧为 DRX 文件，并将 DRX 调色应用到时间线片段的批量化操作。

## 仓库结构

| 组件 | 说明 |
|------|------|
| `main.js` | Electron 主进程 |
| `manifest.xml` | 插件清单文件 |
| `WorkflowIntegration_mac.node` | macOS 原生模块 |
| `WorkflowIntegration_win.node` | Windows 原生模块 |
| `core.asar` | Electron 打包核心 |
| `install.sh` | macOS 安装脚本 |
| `install.bat` | Windows 批处理安装脚本 |
| `install.ps1` | Windows PowerShell 安装脚本 |
| `scripts/` | Lua 脚本集（8 个脚本） |

## Lua 脚本清单

| 脚本 | 功能 |
|------|------|
| `export_selected_powergrade.lua` | 从 PowerGrade 相册导出选中静帧为 DRX |
| `export_and_apply_powergrade.lua` | 导出 DRX 并自动应用到当前片段 |
| `apply_drx_to_selected_clip.lua` | 将 DRX 文件应用到当前 playhead 片段 |
| `export_drx_diagnostics.lua` | 导出诊断信息和日志 |
| `grab_powergrade.lua` | 从 Gallery 抓取 PowerGrade 数据 |
| `list_albums.lua` | 列出所有 PowerGrade 相册 |
| `get_current_clipname.lua` | 获取当前片段名称 |
| `test.lua` | 测试脚本 |

## 安装

### macOS
```bash
./install.sh
# 或手动复制到：
# /Library/Application Support/Blackmagic Design/DaVinci Resolve/Workflow Integration Plugins/ProjectInfoPlugin
```

### Windows
```cmd
install.bat
REM 或手动复制到：
REM %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Workflow Integration Plugins\ProjectInfoPlugin
```

安装后重启 DaVinci Resolve，通过 `Workspace → Workflow Integrations → YYHG Gallery Plugin` 调用。

## 核心 API 说明

文档 `README_apply_drx.md` 详细记录了 DaVinci Resolve 脚本 API 中与 Gallery 操作相关的对象和方法：

- **Project → Gallery → GalleryStillAlbum → GalleryStill** 对象层级
- `ExportStills()` 导出（支持 `drx`/`jpg`/`png`/`dpx` 格式）
- `ApplyGradeFromDRX()` 应用调色（3 种 gradeMode：无关键帧/源时间码对齐/起始帧对齐）