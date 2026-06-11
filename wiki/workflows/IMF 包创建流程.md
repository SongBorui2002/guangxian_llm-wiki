---
type: workflow
title: "IMF 包创建流程"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - imf
  - mastering
  - workflow
status: seed
related:
  - "[[IMF 母版制作]]"
  - "[[DCP 包创建流程]]"
  - "[[Transkoder 渲染流程]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
workflow_type: procedure
domain: "transkoder"
prerequisites:
  - "包含图像和音频内容的完整时间线（无需 reel 约束）"
outputs:
  - "IMF 包（IMP），含视频/音频 MXF、XML 文件和符号链接"
---

# IMF 包创建流程

在 Transkoder 中通过 Finalize 窗口生成 IMF 包（IMP）的完整流程。

## 前置条件

1. 时间线已包含图像和音频内容
2. IMF 视频编码为 GPU 加速，推荐多高性能 GPU

> [!note] 与 DCP 的区别
> IMF 没有 DCP 那样严格的 reel 约束——音视频片段无需按 reel 结构对齐。

## 操作步骤

### 1. 配置全局 IMF 设置

在 **Settings Page → IMF** 部分配置全局参数，这些将影响所有新创建的 IMF 包。

### 2. 打开 IMF Finalize 窗口

按 **Shift+D** 打开 Finalize 窗口（根据时间线配置自动识别为 IMF 模式）。

### 3. 配置 Settings 选项卡

| 参数 | 说明 |
|------|------|
| **Package** | OV（原始版本）或 VF（版本文件） |
| **Source** | V1 track 或 V1 + 已选轨道 |
| **Strategy** | 渲染策略（同 DCP：Per Event / Per Reel / Composition） |
| **Reels** | 需要 reel 标记时设为 On |
| **Audio** | 音频渲染策略 |
| **Layout** | 音频布局（由 Audio Tab 控制） |
| **Movie Title** | 驱动 AnnotationText 和 ContentTitle |
| **Issuer** | 包发行方 |
| **Content Originator** | 内容原创方 |
| **Content Title** | 包标识符（自动生成但可手动修改） |
| **Annotation** | 注解文本 |
| **Subtitle** | 定时文字轨道数量（1 或 2） |
| **Version** | 版本号：1-9、A-H 或无 |

### 4. 配置 Encode 选项卡

- **Application 选择**：App 2 / 2E+ / 4 / 5 / ProRes
- **编码配置**：色彩编码（YUV/RGB）、位深（10/12/16-bit）
- **压缩配置**：Lossy / Lossless
- **分辨率**：HD / QHD / 4K
- **帧率**

### 5. 配置 Audio 选项卡

- 声道布局映射
- 音频格式
- 语言标识

### 6. 配置 Subtitle 选项卡（如需要）

- 添加 IMSC、SMPTE-TT 字幕
- 字幕语言设置

### 7. 配置 Metadata 选项卡

- 内容类型（Content Type）：feature / trailer / short 等
- 目标地区（Territory）
- 内容评级（Rating）

### 8. 配置 Naming 选项卡

- 文件命名约定
- IMF 命名规范参数

### 9. 生成 IMF 包

点击 **Generate** 按钮。

生成输出位置：
```
ProjectBasePath\generated\IMF\IMP\
```

输出包括：
- XML 文件：PKL、CPL、OPL、Assetmap、Volindex
- 视频和音频 MXF 的符号链接

> [!note] 自动导入
> 生成完成后，Transkoder 会自动导入 CPL 时间线以供验证。

## 常见的 IMF 应用场景

| 应用 | 典型用途 |
|------|----------|
| **App 2** | 基础 HD IMF 母版 |
| **App 2E+** | QHD/UHD IMF 母版，扩展色彩空间 |
| **App 4** | 影院级 IMF 母版 |
| **App 5** | ACES 色彩空间 IMF 母版 |
| **ProRes IMF** | 基于 ProRes 的 IMF（非 J2K） |

## CPL 导入（从已有 IMF/DCP）

### 从 AssetMap 导入

1. `Timeline → Import CPL from ASSETMAP`
2. 选择 Assetmap XML 文件
3. 等待元数据解析
4. 从下拉列表中选择 CPL
5. 点击 **Import CPL** 将包加载为新时间线

> [!tip] 云端导入
> 可以从 AWS S3 存储桶导入 AssetMap XML。需在 **AWS Cloud Storage Settings** 中配置 Bucket、access-key 和 secret-key，重启后生效。

## 后续验证

- 播放验证导入的 CPL 时间线
- 使用 QC 工具检查 IMP 完整性
- 验证元数据与平台交付规范（Netflix/Disney 等）匹配