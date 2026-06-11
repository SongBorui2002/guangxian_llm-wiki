---
type: workflow
title: "DaVinci YRGB CST 手动色彩管理"
created: 2026-06-08
updated: 2026-06-08
tags:
  - davinci-resolve
  - color-management
  - cst
  - yrgb
  - workflow
status: developing
related:
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 色彩空间与 ACES]]"
  - "[[DaVinci 节点调色]]"
  - "[[DaVinci 调色流程]]"
  - "[[DaVinci HDR 工作流]]"
  - "[[DaVinci Resolve 20.2 参考手册]]"
sources:
  - "[[DaVinci Resolve 20.2 参考手册]]"
workflow_type: procedure
domain: "davinci-resolve"
prerequisites:
  - "DaVinci Resolve 项目色彩科学设置为 DaVinci YRGB（非 RCM）"
  - "了解素材的摄影机色彩空间和 Gamma"
  - "推荐：已校准的参考监视器"
outputs:
  - "色彩管理正确的调色项目，可渲染或导出"
---

# DaVinci YRGB CST 手动色彩管理

在 DaVinci YRGB（非色彩管理）模式下，使用 CST（Color Space Transform）节点手动搭建完整的色彩管理管线。

## 核心概念

DaVinci YRGB 使用 **Display Referred（显示参考）** 色彩管理。Resolve **不知道**素材"应该长什么样"——它只是把原始 RGB 值送到显示器。**你就是色彩管理**，校准广播监视器是唯一的色彩准确性判断依据。

RCM（YRGB Color Managed）自动做的事——识别输入色彩空间、映射到时间线工作空间、输出转换——在 YRGB 下，用 CST 节点手动逐一替代。

> "this sort of thing can also be done manually in a more conventional Display Referred workflow, by assigning LUTs that are specific to each type of media, or using Color Space Transform Resolve FX in order to transform each clip from the source color space to the destination color space that you require."
>
> — DaVinci Resolve 20.2 参考手册 第 9 章

## CST 节点

CST 节点使用与 RCM **完全相同的数学运算**执行色彩转换，但不依赖项目级自动设置——你手动将其放入节点树。

### 四个核心参数

| 参数 | 含义 |
|------|------|
| **Input Color Space** | 源素材的色彩空间（ARRI LogC、S-Gamut3.Cine 等） |
| **Input Gamma** | 源素材的 Gamma（LogC3、S-Log3 等） |
| **Output Color Space** | 目标色彩空间（DaVinci Wide Gamut、Rec.709 等） |
| **Output Gamma** | 目标 Gamma（Gamma 2.4、Linear 等） |

（Source: DaVinci Resolve 20.2 参考手册 第 94 章）

### Tone Mapping 选项

| 选项 | 行为 | 适用场景 |
|------|------|----------|
| **None** | 简单 1:1 映射，不做任何压缩 | Input 阶段（保留全部数据） |
| **DaVinci** | 平滑亮度滚降 + 最亮/最暗处可控去饱和 | 多机混编首选 |
| **Luminance Mapping** | 比 DaVinci 更精确，适合单一标准色彩空间 | 全是 Rec.709 或全是 Rec.2020 |
| **Saturation Preserving** | 不丢失饱和度，可调 rolloff 参数 | 追求强烈色彩风格 |
| **Adaptation** | 补偿人眼 HDR vs SDR 视觉适应差异 | 极亮场景 HDR→SDR |
| **Clip** | 硬切所有超范围值 | 不需要 tone mapping 时的防御性设置 |

### Gamut Mapping 选项

| 选项 | 行为 |
|------|------|
| **None** | 不做色域映射，超色域值可能被硬切 |
| **Saturation Mapping** | 通过 Saturation Knee + Saturation Max 滑块手动控制 |
| **Clip** | 硬切所有超色域值 |

## 完整节点树结构

```
[Shared Node: CST Input]  →  [Node 2: 降噪]  →  [Node 3: 一级调色]
                                                       ↓
                                               [Node 4: 二级调色]
                                                       ↓
                                               [Node 5: 风格化/Look]
                                                       ↓
                                           [Shared Node: CST Output]
                                                       ↓
                                                    输出
```

## 第一步：Input CST

将素材从摄影机原始色彩空间转换到统一的工作空间。放在节点树**最前端**。

**使用 Shared Node**，同一摄影机类型共享一个 CST（手册第 142 章建议 "Add a Color Space Transform Resolve FX or a LUT to the beginning of every clip from a particular source"）。

### 推荐配置：DaVinci Wide Gamut 中间空间

```
CST Input Node:
  Input Color Space:  [根据素材实际选择，如 ARRI Wide Gamut 3]
  Input Gamma:        [根据素材实际选择，如 ARRI LogC3]
  Output Color Space: DaVinci Wide Gamut
  Output Gamma:       DaVinci Intermediate
  Tone Mapping:       None（Input 阶段不做 Tone Map，保留全部信息）
  Gamut Mapping:      None
```

### 素材适配表

| 摄影机 | Input Color Space | Input Gamma |
|--------|-------------------|-------------|
| ARRI Alexa | ARRI Wide Gamut 3 | ARRI LogC3 |
| RED (IPP2) | REDWideGamutRGB | RED Log3G10 |
| Sony | S-Gamut3.Cine | S-Log3 |
| Blackmagic | Blackmagic Design | Blackmagic Film |
| Canon | Canon Cinema Gamut | Canon Log 2 / Canon Log 3 |

**一种摄影机类型 = 一个 Input CST Shared Node。** 混编多种摄影机素材时，每种需要独立的 Input CST。

## 第二步：调色（中间节点）

在统一的工作色彩空间（DWG Intermediate）中操作。所有调色工具手感一致。

## 第三步：Output CST

从工作空间转换到监看/交付格式。放在节点树**末端**。

### 监看用（校准 Rec.709 监视器）

```
CST Output Node (Monitoring):
  Input Color Space:  DaVinci Wide Gamut
  Input Gamma:        DaVinci Intermediate
  Output Color Space: Rec.709
  Output Gamma:       Gamma 2.4
  Tone Mapping:       DaVinci
  Gamut Mapping:      Saturation Mapping
```

### 交付用（按需切换）

| 交付目标 | Output Color Space | Output Gamma |
|----------|-------------------|--------------|
| SDR 广播 / Web | Rec.709 | Gamma 2.4 |
| DCP 数字电影 | DCI-P3 | Gamma 2.6 |
| HDR (HDR10/HLG) | Rec.2020 | ST 2084 / HLG |
| Dolby Vision | Rec.2020 | ST 2084 |

渲染前切换 Output CST 的 Output Color Space 和 Output Gamma，渲染完成后恢复监看配置。

## 关键技术注意事项

### CST 不做 ACES

手册明确指出 CST 节点输出 ACES 色彩空间是 colorimetric 方式，**不是正确的 ACES 管线**。如果需要 ACES，使用 **ACES Transform** 节点。

### Shared Node 管理

不要让每个 clip 都有独立 CST——用 Shared Node：
- 同一摄影机类型的 Input CST 共享，修改一处全部生效
- 同一交付格式的 Output CST 共享

创建方式：右键 Corrector 节点 → **Save as Shared Node**。

### Data Levels 独立管理

CST 只做色彩转换，不更改 Data Levels。素材的 Auto/Video/Full 设置在 Media Pool → Clip Attributes 中独立管理。

### YRGB + CST vs YRGB Color Managed 对比

| | YRGB + CST（手动） | YRGB Color Managed（RCM） |
|---|---|---|
| 设置位置 | 节点树 | 项目设置面板 |
| 自动识别摄影机色彩空间 | 否，手动选择 | 元数据自动读取 |
| 混合素材管理 | 需要多个 Shared Node | 自动 |
| 灵活性 | 最高 | 中等 |
| 错误风险 | 高（忘记加 CST 则裸奔） | 低 |
| 影响因素追踪 | 明确可见（节点树中） | 隐藏在项目设置中 |

## 错误排查

| 症状 | 可能原因 | 解决 |
|------|----------|------|
| 素材灰、低对比、色彩偏移 | CST Input 缺失或配置不正确 | 检查 Shared Node 是否应用、色彩空间是否匹配素材 |
| 输出与监视器不一致 | CST Output 不匹配交付格式 | 渲染前检查 Output CST 设置 |
| 高光被切 | Tone Mapping 设为 None 或 Clip | 改用 DaVinci 或 Saturation Preserving |
| 饱和度异常 | Gamut Mapping 设为 None | 启用 Saturation Mapping 并调节 Knee/Max |