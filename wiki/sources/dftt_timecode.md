---
type: source
title: "dftt_timecode"
created: 2026-06-05
updated: 2026-06-05
tags:
  - timecode
  - python
  - film
  - smpte
  - library
  - source
  - repository
status: seed
related:
  - "[[DFTT 时间码库]]"
  - "[[DaVinci Resolve 20]]"
sources: []
source_type: repository
author: "You Ziyuan (OwenYou), Wheheo Hu"
date_published: 2025-01-01
url: "https://github.com/OwenYou/dftt_timecode"
confidence: high
key_claims:
  - "影视行业 Python 时间码库，支持 0.01-999.99 fps 高帧率范围，基于 Fraction 的高精度内部存储。"
  - "支持 SMPTE（含丢帧）、SRT、FFMPEG、FCPX、DLP、帧计数和时间戳等 7 种时间码格式。"
  - "完整的时间范围运算（交集、并集、包含判断）和算术/比较操作符重载。"
  - "中英文双语 Sphinx 文档，已发布至 PyPI（dftt-timecode v1.0.0）。"
---

# 源：dftt_timecode

**类型**：Git 仓库快照（Python 库）
**仓库作者**：You Ziyuan (OwenYou)、Wheheo Hu
**来源**：`git@github.com:OwenYou/dftt_timecode.git`（SSH 克隆）
**版本**：v1.0.0（PyPI: `dftt-timecode`）

## 摘要

dftt_timecode 是一个面向影视行业的 Python 时间码库，专注于高帧率（HFR）支持和多格式互转。内部基于 `fractions.Fraction` 实现无损精度的时间戳存储，避免了浮点误差。适合用于 DaVinci Resolve 脚本、字幕处理、DCP/IMF 母版制作等涉及时间码转换和运算的场景。

## 代码结构

```
dftt_timecode/
├── core/
│   ├── dftt_timecode.py    # 核心 DfttTimecode 类
│   └── dftt_timerange.py   # DfttTimeRange 时间区间类
├── pattern.py              # 所有时间码格式的正则模式
├── error.py                # 自定义异常体系
├── logging_config.py       # 分支感知的日志配置
└── __init__.py             # 包导出和便捷别名
test/
├── test_dftt_timecode.py
├── test_dftt_timerange.py
└── conftest.py
docs/                       # Sphinx 双语文档（中文/英文）
```

## 支持的时间码格式

| 格式 | 示例 | 说明 |
|------|------|------|
| **SMPTE** | `01:23:45:12` 或 `01:23:45;12` | 含丢帧（DF）/非丢帧（NDF） |
| **SRT** | `01:23:45,678` | SubRip 字幕格式 |
| **FFMPEG** | `01:23:45.67` | FFmpeg 格式 |
| **FCPX** | `1/24s` | Final Cut Pro X 格式 |
| **DLP** | `01:23:45:102` | DLP Cinema 格式 |
| **Frame** | `1000f` | 帧计数 |
| **Time** | `3600.0s` | 秒时间戳 |

## 技术要点

- **高精度**：Fraction 内部存储，无损运算
- **高帧率**：0.01-999.99 fps 全范围支持
- **不可变性**：运算返回新实例，不修改原值
- **严格模式**：24 小时时间码循环（广播工作流）
- **便利别名**：`dtc`/`Timecode`、`dtr`/`Timerange`

## CI/CD

- **文档**：push to main → GitHub Pages 自动部署
- **发布**：GitHub Release → PyPI 自动发布
- **测试**：pytest 参数化测试覆盖

## 许可证

LGPL-2.1-only

## 相关链接

- 文档：https://owenyou.github.io/dftt_timecode/
- PyPI：https://pypi.org/project/dftt-timecode/