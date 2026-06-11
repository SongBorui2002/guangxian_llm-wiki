---
type: meta
title: "Hot Cache"
updated: 2026-06-08T10:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Wiki Map]]"
  - "[[getting-started]]"
  - "[[DragonScale Memory]]"
---

# Recent Context

Navigation: [[index]] | [[log]] | [[overview]]

## Last Updated

2026-06-08: **DaVinci YRGB CST 手动色彩管理工作流已创建.** YRGB（非 RCM）模式下使用 CST 节点手动搭建完整色彩管理管线的工作流页面。覆盖 Input/Output CST 配置、Tone Mapping/Gamut Mapping 选项对比、Shared Node 管理策略。从 query "达芬奇色彩管理" 深化而来。

2026-06-05: **Advanced Color Science Course 2026 教学材料导入完成.** 来自智能成像工程学院的高阶色彩科学课程，涵盖同色异谱失效、观察者差异、CIE 标准。1 个源页面、2 个概念页面。交叉链接到 DaVinci 色彩管理与 ACES 工作流。

2026-06-05: **YYHG_gallery 导入完成.** DaVinci Resolve PowerGrade DRX 自动化插件（Lua 脚本 + Electron）| 1 个源页面、2 个概念、1 个工作流。覆盖 PowerGrade 相册对象层级、DRX 导出/应用 API 和自动化工作流。

2026-06-05: **3 个 Git 仓库批量导入完成.** 立体字幕和时间码工具链：StereoscopicSubtitlePlugin（Electron 插件）、3dResolveSubtitle（Python 脚本扩展）、dftt_timecode（Python 时间码库 v1.0.0） | 3 个源页面、1 个实体、3 个概念、1 个工作流。覆盖了立体 3D 字幕 DCDM 格式、SMPTE ST 428-7 标准和 HFR 时间码多格式转换。

2026-06-05: **DaVinci Resolve 20.2 参考手册 ingestion complete.** Blackmagic Design DaVinci Resolve 20 官方参考手册（199MB PDF，100+ 章）已从 PDF 规范化并导入 wiki。创建了 1 个源页面、2 个实体页面、1 个领域页面、6 个概念页面、5 个工作流页面。覆盖编辑、调色、Fusion 合成、Fairlight 音频、色彩管理/ACES、HDR/Dolby Vision 和渲染交付。

2026-06-05: **DCP 打包 SDR 色彩空间转换 问答存档.** 将 Rec.709 Gamma 2.4 → DCP 的 CSC 节点配置、XYZRGB Conversion 位置和 On/Off 判断逻辑整理为结构化问答页面。

2026-06-05: **Transkoder 2025 用户指南 ingestion complete.** COLORFRONT Transkoder 2025 官方用户手册（177k 字，27 章 + 14 附录）已从 HTML bundle 规范化并导入 wiki。HTML 源 -> `python3 scripts/normalize-html-bundle.py` 生成 42 个章节分页 + 主页面。创建了 1 个源页面、2 个实体页面（COLORFRONT、Transkoder 2025）、1 个领域页面（domains/transkoder/）、8 个概念页面、6 个工作流页面。涵盖了 DCP/IMF 母版制作、Node Page 图像处理管线、JPEG2000 编解码、HDR/Dolby Vision、渲染流程、调色流程、安装指南、远程流媒体、键盘快捷键和故障排查等核心主题。

## Key Recent Facts

- 新增概念页面：[[Color Metamerism]] 与 [[CIE Color Matching Functions]] — 色彩科学基础，与 ACES/DaVinci 色彩管理交叉链接
- 新增源页面：[[Advanced Color Science Course 2026]] — 教学材料涵盖观察者差异与同色异谱失效
- 新增问答页面：[[DCP 打包 SDR 色彩空间转换]] — 覆盖 Rec.709 SDR → DCP 色彩管线完整配置
- Transkoder 2025 Wiki 知识库现包含 17 个专用页面，覆盖 DCP/IMF 母版制作全流程
- DragonScale Mechanism 4 shipped in Phase 4 as an opt-in Topic Selection mode in `skills/autoresearch/`
- v1.6.0 not yet pushed to GitHub (local commits only). User controls push and tag timing.

## Recent Changes

- Added workflows: [[DaVinci YRGB CST 手动色彩管理]] — YRGB + CST 手动色彩管理管线
- Added source: [[Advanced Color Science Course 2026]] (teaching material)
- Added concepts: [[Color Metamerism]], [[CIE Color Matching Functions]]
- Added image attachment: `_attachments/images/color-metamerism-failure.jpeg` (246KB)
- Added sources: [[3dResolveSubtitle]], [[StereoscopicSubtitlePlugin]], [[dftt_timecode]]
- Added entities: [[Alaric Hamacher]]
- Added concepts: [[立体 3D 字幕]], [[DCDM 字幕]], [[DFTT 时间码库]]
- Added workflows: [[立体 3D 字幕工作流]]
- Updated: [[domains/davinci-resolve/_index]] (plugin/tools section)
- Added: [[DaVinci Resolve 20.2 参考手册]], [[Blackmagic Design]], [[DaVinci Resolve 20]], [[domains/davinci-resolve/_index]]
- Added concepts: [[DaVinci 色彩管理]], [[DaVinci 节点调色]], [[DaVinci Fusion 合成]], [[DaVinci HDR 工作流]], [[DaVinci 色彩空间与 ACES]], [[DaVinci Fairlight 音频]]
- Added workflows: [[DaVinci 调色流程]], [[DaVinci 渲染与交付]], [[DaVinci 媒体导入与整理]], [[DaVinci 项目管理]], [[DaVinci 专业编辑（Edit Page）]]
- Added: [[Transkoder 2025 用户指南]], [[COLORFRONT]], [[Transkoder 2025]], [[domains/transkoder/_index]]
- Added concepts: [[DCP 母版制作]], [[IMF 母版制作]], [[Node Page 图像处理管线]], [[JPEG2000 编解码]], [[HDR 工作流]], [[CPL（Composition Playlist）]], [[KDM（Key Delivery Message）]], [[OV vs VF Package]]
- Added workflows: [[Transkoder 安装指南]], [[Transkoder 渲染流程]], [[Transkoder 调色流程]], [[DCP 包创建流程]], [[IMF 包创建流程]], [[远程流媒体配置]], [[Transkoder 故障排查]], [[Transkoder 键盘快捷键]]
- Updated: [[index]], [[log]]
- Normalized source: `.raw/documents/TKD/TKDUserGuide_dark_normalized/`

## Active Threads

- 如需更深层的 Transkoder 知识提取，可进一步为 Audio、Metadata、Subtitles、QC Tools、Security Hardening 等章节创建独立页面
- 当前以 DCP/IMF/渲染/调色为优先级最高的编译维度，覆盖最常见的工作流查询