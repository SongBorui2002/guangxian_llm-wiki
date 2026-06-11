---
type: concept
title: "DFTT 时间码库"
created: 2026-06-05
updated: 2026-06-05
tags:
  - timecode
  - python
  - smpte
  - library
  - film
status: seed
related:
  - "[[dftt_timecode]]"
  - "[[DaVinci Resolve 20]]"
  - "[[DaVinci 渲染与交付]]"
sources:
  - "[[dftt_timecode]]"
complexity: intermediate
domain: "davinci-resolve"
aliases:
  - "dftt-timecode"
  - "DfttTimecode"
---

# DFTT 时间码库

**dftt_timecode**（PyPI: `dftt-timecode`）是一个面向影视行业的 Python 时间码库，专注于高帧率（HFR，0.01-999.99 fps）支持和多格式时间码转换。

## 核心类

### DfttTimecode（`dtc`/`Timecode`）
核心时间码类，提供所有时间码操作：
- **格式转换**：7 种时间码格式互转
- **算术运算**：`+`、`-`、`*`、`/`
- **比较运算**：`==`、`!=`、`<`、`>`、`<=`、`>=`
- **高精度存储**：内部使用 `fractions.Fraction`，避免浮点误差

### DfttTimeRange（`dtr`/`Timerange`）
时间区间类：
- 区间运算：交集（intersection）、并集（union）
- 包含判断：`timecode in timerange`
- 时长和帧数计算

## 格式参考

| 输出格式 | 示例 | 典型场景 |
|----------|------|----------|
| `smpte` | `01:23:45:12` | NLE 编辑、广播 |
| `srt` | `01:23:45,678` | 字幕文件 |
| `ffmpeg` | `01:23:45.67` | FFmpeg 命令行 |
| `fcpx` | `1/24s` | Final Cut Pro X |
| `dlp` | `01:23:45:102` | DLP Cinema (DCP) |
| `frame` | `1000f` | 帧计数 |
| `time` | `3600.0s` | 秒时间戳 |

## 基本用法

```python
from dftt_timecode import dtc, dtr

# 创建时间码
tc = dtc('01:00:00:00', fps=24)

# 格式转换
tc.timecode_output('srt')   # '01:00:00,000'
tc.timecode_output('ffmpeg') # '01:00:00.00'

# 算术
result = tc + 100   # 增加 100 帧
result = tc + 1.0   # 增加 1 秒

# 时间范围
tr = dtr('01:00:00:00', '02:00:00:00', fps=24)
tc in tr  # True
```

## 适用场景

- DaVinci Resolve 脚本中的时间码计算
- 字幕时间码格式转换（SRT ↔ SMPTE）
- DCP/IMF 母版制作中的帧-时间码换算
- FFmpeg 自动化管线中的时间码处理
- 剪辑软件间的项目套片和转换