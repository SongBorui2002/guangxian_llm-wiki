---
type: workflow
title: "Transkoder 渲染流程"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - rendering
  - encoding
  - workflow
status: seed
related:
  - "[[Transkoder 2025]]"
  - "[[Node Page 图像处理管线]]"
  - "[[DCP 包创建流程]]"
  - "[[IMF 包创建流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
workflow_type: procedure
domain: "transkoder"
prerequisites:
  - "已配置好的 Node Page 管线"
  - "已设置 Result 输出"
outputs:
  - "编码完成的渲染文件（各种容器和编码格式）"
---

# Transkoder 渲染流程

Transkoder 采用混合 CPU/GPU 架构进行渲染。图像处理（浮点精度）和 JPEG2000 编解码由 GPU 加速，其他编码过程（如 Avid/ProRes）由 CPU 执行。支持多个并行 Result 同时渲染。

## 快速渲染

按 **Ctrl+R** 启动标准渲染。
- **P** 键：暂停
- **Esc** 键：中止

> [!note] DCP/IMF 渲染
> 对于 DCP 或 IMF 包的渲染，建议使用 **Finalize Window** 而非标准 Render Page。

## Render Page 操作流程

### 1. 进入 Render Page

按 **P** 键打开渲染页面。页面分为三栏：

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  左侧面板      │  │  中间面板      │  │  右侧面板      │
│  Output       │  │  Encoder     │  │  Configuration│
│  Results      │  │  Table       │  │  Pane         │
│  缩略图        │  │  编码器表      │  │  配置面板      │
└──────────────┘  └──────────────┘  └──────────────┘
```

### 2. 添加编码器

1. 点击 Encoder Table（编码器表）中的空行
2. 从两层结构化的编码器列表中选择需要的编码器
3. 可为一个 Result 添加多个编码器
4. 删除编码器：高亮后按 **Backspace**

### 3. 配置编码参数

选中编码器后，右侧 Configuration Pane 显示当前编码器的全部配置项：

| 常用参数 | 说明 |
|----------|------|
| **Bit Depth** | 位深 |
| **Profile** | 编码配置文件 |
| **Color Space** | 色彩空间 |
| **Resolution** | 输出分辨率 |
| **FPS** | 输出帧率 |
| **Bitrate** | 码率 |
| **Burn-in** | 烧录文字/时间码 |

### 4. 设置渲染路径

点击 **File** 列或 **FILE PATH** 参数：
- 编辑渲染路径
- 预览最终渲染文件名
- 使用 **Add Keyword** 插入变量关键字
- 零填充：默认 `%07d`（7 位数字）

### 5. 启动渲染

按 **Ctrl+R** 或 `Render → Render Timeline`。

## 编码器表（Encoder Table）列说明

| 列 | 说明 |
|----|------|
| **#** | 编码器编号 |
| **On** | 启用/禁用该编码器 |
| **Format** | 编码器名称（如 Avid DNxHR HQX） |
| **Container** | 容器格式（.mov、.mxf 等） |
| **Codec** | 编解码器名称 |
| **Resolution** | Auto / Project / 指定分辨率 |
| **Bitrate** | 编码比特率 |
| **FPS** | 帧率（23.976-120） |
| **Selected** | All Takes / Selected / All+Selected |
| **Files** | Per Timeline（单文件）或 Per Shot（每片段） |
| **Sound** | Normal / Pulldown / Pullup |
| **Mix** | Audio Mixdown：Source / No Audio / xml 预定义 |
| **Slate** | 是否包含自动生成的 Slate 片段 |
| **PostProcess** | 自定义后处理脚本 |
| **File** | 渲染输出路径 |

## 渲染预览

在 **Encode Settings** 中的 **Max Render Length** 参数可限制编码帧数（默认值 `-1` 表示全部），用于快速测试渲染设置。

## 时间码和 Reel Name 元数据

大多数编码器可在渲染文件中嵌入时间码和 Reel Name 元数据。支持多种时间码类型。

## 常见编码器

| 类别 | 编码器 |
|------|--------|
| **Avid** | DNxHR LB/SQ/HQ/HQX、DNxHD |
| **Apple** | ProRes 422/422HQ/4444/4444XQ |
| **JPEG2000** | DCP/IMF 用 J2K |
| **HEVC/H.265** | UHD 交付 |
| **H.264** | HD 交付 |
| **OpenEXR** | VFX 工作流 |
| **TIFF/DPX** | 图像序列 |