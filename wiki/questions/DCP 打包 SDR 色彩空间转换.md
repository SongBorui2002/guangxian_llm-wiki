---
type: question
title: "DCP 打包 SDR 色彩空间转换"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - color-space
  - rec709
  - p3
  - xyz
status: developing
question: "利用 Rec.709 Gamma 2.4 源素材打包 DCP，都需要哪些节点？XYZRGB Conversion 应该开还是关？"
answer_quality: solid
related:
  - "[[DCP 母版制作]]"
  - "[[Node Page 图像处理管线]]"
  - "[[DCP 包创建流程]]"
  - "[[Transkoder 渲染流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: intermediate
domain: "transkoder"
---

# DCP 打包 SDR 色彩空间转换

将 Rec.709 / Gamma 2.4 的 SDR 源素材打包为 DCP 时，核心问题是色彩空间转换：**DCP 的交付色彩空间是 DCI-XYZ，而 SDR 素材通常工作在 Rec.709 / Gamma 2.4**。Transkoder 提供了两条路径完成这个转换。

## 核心节点：CSC（Color Space Converter）

无论选择哪条路径，都需要在 Node Page 管线中插入 **CSC 节点**。CSC 节点是一个纯技术性的色彩空间转换工具，只改变色彩空间表示，像素值本身不变（Source: [[Transkoder 2025 用户指南]] 第 12 章 §12.2.11）。

CSC 节点支持的曲线（Curve）和色域（Color Space）：

| 方向 | 选项（部分） |
|------|-------------|
| **Curve** | Gamma 2.2、Gamma 2.4、Gamma 2.6、HLG (BT.2100)、PQ、Linear、LogC、SLog3、V-Log 等 |
| **Color Space** | BT.709、P3-DCI、P3-D65、XYZ DCI、XYZ D65、BT.2020、ACES-AP0、ARRIWideGamut 等 |

## 关键设置：XYZRGB Conversion

**位置：Settings Page → Advanced DCI Settings → Validation and QC → XYZRGB Conversion**

默认 **Off（关闭）**。

| 状态 | 工作色彩空间 | DCP 解码时 | DCP 编码时 |
|------|-------------|-----------|-----------|
| **On** | P3 RGB | DCI XYZ → P3 RGB | P3 RGB → DCI XYZ |
| **Off** | DCI XYZ | 不做转换 | 不做转换 |

用户手册原文（第 14 章 §14.9.2、第 15 章 §15.6）：

> *If set to On, Transkoder makes conversion from DCI XYZ to P3 RGB in case of DCP decoding and from P3 RGB to DCI XYZ in case of DCP encoding.*

DCP Finalize 窗口 → DCP Encode 选项卡的 **Working Colorspace** 参数提供两个选项：**DCI XYZ** 或 **P3 RGB**，与 XYZRGB Conversion 联动。

## 两条路径，二选一

### 方案 A：P3 工作流（推荐，适合 Rec.709 源素材）

```
XYZRGB Conversion    ON
Working Colorspace   P3 RGB
CSC 节点配置         InputCurve:  Gamma 2.4
                    InputColor:  Rec709
                    OutputCurve: Gamma 2.6
                    OutputColor: P3-DCI
管线工作域            P3 RGB
DCP 编码时            自动 P3 RGB → DCI XYZ
```

这是 Transkoder 用户手册推荐的默认方式。在 RGB 域做调色（CDL/LUT）手感自然，监视器监看正常。编码时自动完成 P3→XYZ。

### 方案 B：XYZ 原生工作流（适合已预母版的 DCDM 素材）

```
XYZRGB Conversion    OFF（默认）
Working Colorspace   DCI XYZ
CSC 节点配置         InputCurve:  Gamma 2.4
                    InputColor:  Rec709
                    OutputCurve: Gamma 2.6
                    OutputColor: XYZ-DCI
管线工作域            DCI XYZ
DCP 编码时            直通, 不做额外转换
```

适用于源素材已经母版为 DCI-XYZ 色彩空间的场景（如 Digital Cinema Distribution Master）。

## XYZRGB Conversion 开启 / 关闭的判断

| 场景 | 设置 |
|------|------|
| 从 Rec.709 / RAW / Log 素材新建 DCP | **ON** |
| 已有 DCDM（DCI-XYZ 母版）直出 DCP | OFF |
| Dolby Cinema HDR DCP | **OFF**（强制） |
| 导入现成 DCP 做 QC / 分析 / 转码 | OFF |

> [!warning] ON 和 XYZ 不能混搭
> 如果 XYZRGB Conversion = ON，编码器期望 P3 RGB 输入并自动转 XYZ。此时若 CSC 输出为 XYZ 且 Working Colorspace 也设为 XYZ，会导致 XYZ 数据被当成 P3 做二次转换，色彩错误。

## 最少所需节点

针对 Rec.709 Gamma 2.4 → DCP 的最简管线：

```
SOURCE              PIPELINE               RESULT
Rec.709 / 2.4  →   [CSC 节点]         →   P3-DCI / Gamma 2.6
源素材              Rec709→P3-DCI           ↓
                     2.4→2.6           Shift+D Finalize
                                         自动编码 DCP
```

最少只需 **1 个 CSC 节点**。如果需要调色，可在 CSC 前后添加 CDL、LUT 或 CFE 节点。