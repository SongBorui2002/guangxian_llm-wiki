---
type: workflow
title: "DCP 包创建流程"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - mastering
  - workflow
status: seed
related:
  - "[[DCP 母版制作]]"
  - "[[IMF 包创建流程]]"
  - "[[Transkoder 渲染流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
workflow_type: procedure
domain: "transkoder"
prerequisites:
  - "包含同步视频、音频和可选字幕的完整时间线"
  - "视频事件需与对应音频事件对齐（DCP 要求按 reel 结构对齐）"
outputs:
  - "DCP 包（OV 或 VF），含 MXF 资源和 XML 元数据文件"
---

# DCP 包创建流程

在 Transkoder 中通过 Finalize 窗口创建 DCP（Digital Cinema Package）包的完整操作流程。

## 前置条件

1. 时间线已包含同步的画面和音频元素
2. 所有视频事件有对应的音频事件（DCP 要求）
3. 音频切点与视频事件对齐
4. 如需要，字幕文件已导入主 Bin 并拖入时间线

> [!tip]
> 时间线上的画面和音频可以已经是编码好的 DCP 资产（如 TIFF/DPX 序列、WAV 文件），Finalize 过程会自动编码不符合 DCP 规范的部分。

## 操作步骤

### 1. 设置 Reel 标记点（需要时）

如果不使用 Reel 标记，DCP 的 reel 将对应时间线上的视频事件。

- 按 **I** 键设置 In 点（开始标记）
- 按 **O** 键设置 Out 点（结束标记）
- 或使用菜单：`Timeline → Markers → Set Reel Marker In/Out`
- 删除 Reel：选中后按 `Ctrl+Backspace`
- 自定义 Reel 名：双击 Reel 标记名或通过 Markers Table 编辑

### 2. 打开 DCP Finalize 窗口

按 **Shift+D** 打开 DCP Finalize 窗口。

### 3. 配置 DCP Settings 选项卡

| 参数 | 推荐设置 |
|------|----------|
| **Standard** | Interop（通用）或 SMPTE B2.1/RDD52（高级需求） |
| **Encrypt** | 如需加密，设为 On |
| **Stereo** | 3D 立体项目设为 On |
| **Package** | 首次创建选 OV，后续版本选 VF |
| **Strategy** | 按需选择：Per Event / Per Reel / Composition |
| **Reels** | 使用 Reel 标记时设为 On |
| **Atmos** | Dolby Atmos 项目自动 On |
| **Content** | feature / trailer / short 等 |
| **Territory** | 目标地区 |

### 4. 配置 DCP Encode 选项卡

- JPEG2000 编码参数设置
- 自适应编码策略（如需要）
- PSNR 和比特率目标

### 5. 配置 DCP Audio 选项卡

- 音频格式配置
- 声道映射
- 音频语言标识

### 6. 配置 DCP Subtitle 选项卡（如需要）

- 字幕格式选择：MXF / PNG / XML InterOp / XML SMPTE
- 字体和渲染设置
- 隐藏字幕（SMPTE Timed Text）配置

### 7. 配置 DCP Metadata 选项卡

- 影片标题（Content Title）
- 发行方（Issuer）
- 内容原创方（Content Originator）
- 注解文本（Annotation）
- 内容评级

### 8. 配置 DCP KDM 选项卡（加密时）

- KDM 生成设置
- 目标设备证书
- 取证水印选项（NexGuard）

### 9. 配置 DCP Naming 选项卡

- 文件命名约定
- DCI 命名规范参数

### 10. 生成 DCP 包

点击 **Finalize** 按钮开始生成。生成的包位于：
```
ProjectBasePath\generated\DCP\
```

生成完成后，Transkoder 会自动导入 CPL 时间线供验证。

## 全局 DCP 设置

在 **Settings Page** → **DCI Settings** 部分可调整全局 DCP 参数，影响所有新创建的包。

## 常见包类型

| 包类型 | 场景 |
|--------|------|
| **Interop OV** | 电影节度映、通用分发 |
| **SMPTE RDD52 OV** | 专业影院分发（支持 HI/VI 音轨、MCA 标签） |
| **SMPTE VF (VF)** | 在现有 OV 基础上添加字幕/语言版本 |
| **Encrypted OV + KDM** | 需要安全分发的内容 |

## 后续验证

- 使用 Transkoder 重新导入 CPL 播放验证
- 运行 QC 工具检查包完整性
- 使用 Analyzer 进行位率和 PSNR 分析