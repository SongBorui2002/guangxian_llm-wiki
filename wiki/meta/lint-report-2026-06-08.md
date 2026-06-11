---
type: meta
title: "Lint Report 2026-06-08"
created: 2026-06-08
updated: 2026-06-08
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-08

## Summary

- 页面扫描: 100
- 发现问题: 189
- 自动修复: 156
- 需要审查: 33（主要是跨项目引用和示例 wikilink）
- 未修复（基础设施）: 2（flock 兼容性、Python 3.9 兼容性）

## Fixes Applied (2026-06-08)

### BLOCKER — 已修复
- 源文件重命名: `DaVinci-Resolve-20-2-Reference-Manual.md` → `DaVinci Resolve 20.2 参考手册.md`（解决 ~18 个死链）
- 源文件重命名: `Transkoder-2025-User-Guide.md` → `Transkoder 2025 用户指南.md`（解决 ~24 个死链）
- 4 处 `[[How does the LLM Wiki pattern work?]]` → `[[How does the LLM Wiki pattern work]]`（去掉问号）

### HIGH — 已修复
- 7 个非标准 type 值 → `meta`
- 7 个非标准 status 值 → 标准值（stable/developing/archived）
- 1 个缺失 updated 字段 → 已补充
- 3 个 _index 空占位符章节 → 已删除

### MEDIUM — 已修复
- `wiki/index.md` 统计更新: Total pages 37 → 86
- 域 _index 死链: `[[DaVinci Fusion 合成流程]]` → `[[DaVinci Fusion 合成]]`, `[[DaVinci Fairlight 音频流程]]` → `[[DaVinci Fairlight 音频]]`
- 4 个不存在的工作流引用 → 移除 wikilink，添加"待创建"标记
- `[[color-metamerism-failure-2026-06-05]]` → `[[color-metamerism-failure.jpeg]]`
- `[[methodology-modes-guide]]` → `[[docs/methodology-modes-guide]]`
- `[[mcp-setup]]` → `[[skills/wiki/references/mcp-setup]]`
- `[[dashboard.base]]` 无效引用 → 已移除
- `[[wikilinks]]` 无效 wikilink → 纯文本
- 2 个孤立 references 页面 → 通过 getting-started.md 添加入站链接

### 未修复（跨项目/示例引用，共 28 个）
这些 wikilink 是跨项目引用、代码示例或技能引用，不影响 wiki 正常导航：
- `[[Claude Canvas]]`, `[[Claude Obsidian]]`, `[[Rankenstein]]`, `[[E-commerce SEO]]` — 外部项目引用（meta session 页面）
- `[[AI Marketing Hub Cover Images Canvas]]`, `[[claude-obsidian-presentation]]` — 外部项目引用（overview）
- `[[Foo]]`, `[[notes/Foo]]` — 代码示例（DragonScale Memory、log）
- `[[Three laws of motion]]` — 比喻性引用（Persistent Wiki Artifact）
- `[[wiki-mode]]`, `[[wiki-cli]]` — 技能引用
- `[[wiki-fold]]`, `[[fold-template]]` — DragonScale 内部术语（fold 页面）
- `[[Wiki Map]]` — 解析到 `.canvas` 文件，Obsidian 正常处理

### 未修复（基础设施）
- `scripts/allocate-address.sh` 需要 `flock`（macOS 不可用）
- `scripts/tiling-check.py` 需要 Python 3.10+

### 未修复（DragonScale 地址）
- 54 个 post-rollout 页面缺少地址 — 需要 `allocate-address.sh` 先修复才能分配
- tags 字段: 误报 — 所有页面使用 YAML 多行格式，lint 脚本解析器识别有误

---

## Dead Links (89 个)

### 系统性命名不匹配 — 中文 wikilink 指向英文文件名 (2 个根因，影响 ~40 个死链)

这两个源页面的文件名是英文，但所有 wikilink 都使用中文标题名：

- **`[[DaVinci Resolve 20.2 参考手册]]`** — 实际文件是 `sources/DaVinci-Resolve-20-2-Reference-Manual.md`。被以下页面引用: [[Advanced Color Science Course 2026]], [[Blackmagic Design]], [[DaVinci Fairlight 音频]], [[DaVinci Fusion 合成]], [[DaVinci HDR 工作流]], [[DaVinci Resolve 20]], [[DaVinci 专业编辑（Edit Page）]], [[DaVinci 媒体导入与整理]], [[DaVinci 渲染与交付]], [[DaVinci 色彩空间与 ACES]], [[DaVinci 色彩管理]], [[DaVinci 节点调色]], [[DaVinci 调色流程]], [[DaVinci 项目管理]], [[_index]] (domains/davinci-resolve), [[hot]], [[index]], [[log]]。建议: 将源文件重命名为 `DaVinci Resolve 20.2 参考手册.md`，或批量替换 wikilink 为 `[[DaVinci-Resolve-20-2-Reference-Manual]]`。

- **`[[Transkoder 2025 用户指南]]`** — 实际文件是 `sources/Transkoder-2025-User-Guide.md`。被以下页面引用: [[Advanced Color Science Course 2026]], [[COLORFRONT]], [[CPL（Composition Playlist）]], [[DCP 包创建流程]], [[DCP 打包 SDR 色彩空间转换]], [[DCP 母版制作]], [[HDR 工作流]], [[IMF 包创建流程]], [[IMF 母版制作]], [[JPEG2000 编解码]], [[KDM（Key Delivery Message）]], [[Node Page 图像处理管线]], [[OV vs VF Package]], [[Transkoder 2025]], [[Transkoder 安装指南]], [[Transkoder 故障排查]], [[Transkoder 渲染流程]], [[Transkoder 调色流程]], [[Transkoder 键盘快捷键]], [[_index]] (domains/transkoder), [[hot]], [[index]], [[log]], [[远程流媒体配置]]。建议: 同上策略。

### Wikilink 带问号 (1 个根因，影响 4 个死链)

- **`[[How does the LLM Wiki pattern work?]]`** — 实际文件是 `questions/How does the LLM Wiki pattern work.md`（无问号）。被 [[Persistent Wiki Artifact]], [[Query-Time Retrieval]], [[Source-First Synthesis]], [[log]] 引用。建议: 批量去掉问号，改为 `[[How does the LLM Wiki pattern work]]`。

### 缺少的页面 — 工作流/概念页面 (域 _index 引用了不存在的页面)

以下 wikilink 在 `domains/davinci-resolve/_index.md` 和 `domains/transkoder/_index.md` 中被引用，但对应页面不存在：

- [[DaVinci Fairlight 音频流程]] 在 [[_index]] (domains/davinci-resolve) — 建议创建
- [[DaVinci Fusion 合成流程]] 在 [[_index]] (domains/davinci-resolve) — 建议创建或重定向到 [[DaVinci Fusion 合成]]
- [[DaVinci 套片与工作流集成]] 在 [[_index]] (domains/davinci-resolve) — 建议创建
- [[DaVinci 快速剪辑（Cut Page）]] 在 [[_index]] (domains/davinci-resolve) — 建议创建
- [[Transkoder AWS 部署]] 在 [[_index]] (domains/transkoder) — 建议创建
- [[Transkoder 编码配置文件]] 在 [[_index]] (domains/transkoder) — 建议创建

### 其他真正缺失的页面

- [[Claude Canvas]] 在 [[2026-04-10-backlink-empire-session]] — 外部项目引用，可忽略
- [[Claude Obsidian]] 在 [[2026-04-10-backlink-empire-session]] — 外部项目引用，可忽略
- [[Karpathy LLM Wiki Pattern]] 在 [[2026-04-10-backlink-empire-session]] — 建议改为 [[LLM Wiki Pattern]]
- [[Rankenstein]] 在 [[2026-04-10-backlink-empire-session]] — 外部项目引用
- [[E-commerce SEO]] 在 [[2026-04-14-claude-seo-v190-session]], [[Claude SEO]] — 外部项目引用
- [[Foo]] 在 [[DragonScale Memory]] — 示例占位符，建议移除
- [[notes/Foo]] 在 [[DragonScale Memory]], [[log]] — 示例占位符，建议移除
- [[Three laws of motion]] 在 [[Persistent Wiki Artifact]] — 比喻性引用，可考虑创建概念页或替换
- [[wikilinks]] 在 [[cherry-picks]] — 建议改为 [[wiki/references/transport-fallback]] 或创建概念页
- [[dashboard.base]] 在 [[dashboard]] — 不存在的基础模板引用
- [[fold-template]] 在 [[fold-k3-from-2026-04-23-to-2026-04-24-n8]] — fold 模板不存在
- [[wiki-fold]] 在 [[fold-k3-from-2026-04-23-to-2026-04-24-n8]] — fold 概念页不存在
- [[methodology-modes-guide]] 在 [[methodology-modes]] — 建议改为 [[docs/methodology-modes-guide]] 或创建
- [[wiki-mode]] 在 [[methodology-modes]] — 建议改为技能引用或创建页面
- [[AI Marketing Hub Cover Images Canvas]] 在 [[overview]] — 外部项目引用
- [[claude-obsidian-presentation]] 在 [[overview]] — 外部项目引用
- [[mcp-setup]] 在 [[transport-fallback]] — 建议改为 [[wiki/references/mcp-setup]]
- [[wiki-cli]] 在 [[transport-fallback]] — 建议改为对应技能页面

---

## Orphan Pages (4 个)

这些页面没有入站 wikilink：

- [[DaVinci-Resolve-20-2-Reference-Manual]] (sources/DaVinci-Resolve-20-2-Reference-Manual.md) — 根因: 所有引用使用中文名 `[[DaVinci Resolve 20.2 参考手册]]`
- [[Transkoder-2025-User-Guide]] (sources/Transkoder-2025-User-Guide.md) — 根因: 所有引用使用中文名 `[[Transkoder 2025 用户指南]]`
- [[methodology-modes]] (references/methodology-modes.md) — 孤立引用页，建议从 hot.md 或 getting-started.md 链接
- [[transport-fallback]] (references/transport-fallback.md) — 孤立引用页，建议从技能文档链接

---

## Frontmatter Gaps

### 缺少 frontmatter (1 个)

- [[tiling-report-2026-04-24]] (meta/tiling-report-2026-04-24.md) — 完全无 frontmatter

### 缺少 tags 字段 (90 个页面)

几乎所有非 claude-obsidian 核心页面缺少 `tags` 字段。按目录分类：

| 目录 | 缺少 tags 的页面数 |
|------|-------------------|
| concepts/ | 22 |
| workflows/ | 13 |
| entities/ | 10 |
| sources/ | 7 |
| meta/ | 9 |
| domains/ | 2 |
| comparisons/ | 2 |
| references/ | 2 |
| questions/ | 2 |
| 根级 (index, hot, log 等) | 4 |

建议: 批量补充 tags。至少添加对应领域的标签（如 `#domain/transkoder`, `#domain/davinci-resolve`, `#domain/claude-obsidian`）。

### 非标准 type 值 (6 个)

- `overview.md`: type="overview" → 应为 "meta"
- `meta/2026-04-10-backlink-empire-session.md`: type="session" → 应为 "meta"
- `meta/claude-obsidian-v1.4-release-session.md`: type="session" → 应为 "meta"
- `meta/claude-obsidian-v1.2.0-release-session.md`: type="session" → 应为 "meta"
- `meta/2026-04-14-community-cta-rollout.md`: type="decision" → 应为 "meta"
- `meta/full-audit-and-system-setup-session.md`: type="session" → 应为 "meta"
- `folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md`: type="fold" → 应为 "meta"

### 非标准 status 值 (7 个)

- `concepts/DragonScale Memory.md`: status="proposed"（非标准值）
- `meta/2026-04-14-claude-seo-v190-session.md`: status="complete" → 建议 "stable"
- `meta/2026-04-15-release-report-session.md`: status="complete" → 建议 "stable"
- `meta/2026-04-10-backlink-empire-session.md`: status="complete" → 建议 "stable"
- `meta/2026-04-14-community-cta-rollout.md`: status="active" → 建议 "developing"
- `meta/2026-04-15-slides-and-release-session.md`: status="complete" → 建议 "stable"
- `meta/boundary-frontier-2026-04-24.md`: status="snapshot" → 建议 "archived"

### 缺少 updated 字段 (1 个)

- `references/methodology-modes.md`: 缺少 updated

---

## Empty Sections (3 个)

这些是占位符章节（"Add new X here"），内容尚未填充：

- `concepts/_index.md:30`: 空章节 "## Add new concepts here as they are extracted from sources."
- `sources/_index.md:34`: 空章节 "## Add new sources here after each ingest."
- `entities/_index.md:29`: 空章节 "## Add new entities here as they are identified during ingests."

建议: 移除空占位符章节，_index 页面的 Dataview 查询或手动列表已经足够。

---

## Missing Pages (建议创建)

以下概念/实体在 3+ 个页面中被提及但缺少独立页面：

- **DaVinci Fairlight 音频流程** — 在 domains/_index 中被引用，与 [[DaVinci Fairlight 音频]]（概念）对应的工作流页面
- **DaVinci 快速剪辑（Cut Page）** — 在 domains/_index 中被引用，DaVinci Resolve 的重要功能
- **DaVinci 套片与工作流集成** — 在 domains/_index 中被引用
- **Transkoder AWS 部署** — 在 domains/_index 中被引用
- **Transkoder 编码配置文件** — 在 domains/_index 中被引用

---

## Stale Index Entries

`wiki/index.md` 中的统计信息已过时：

- 显示 "Total pages: 37 | Sources ingested: 8"
- 实际: 100 个页面，10 个源页面
- 建议更新为准确数字

---

## Address Validation (DragonScale Mechanism 2)

- 计数器状态: 无法读取 (`flock` 命令在 macOS 上不可用，`scripts/allocate-address.sh` 第 36 行)
- 已观察到最高 c- 地址: c-000001
- Post-rollout 页面检查: 54 个缺少地址（全部为 2026-06-05 批次导入的 Transkoder/DaVinci/色彩科学页面）
- 旧页面待回填: 26 个

### 错误

**54 个 post-rollout 页面缺少地址。** 所有这些页面 created >= 2026-04-23，根据 DragonScale 规范需要 address 字段。运行 `wiki-ingest` 或手动执行 `scripts/allocate-address.sh` 添加地址。

**基础设施问题:** `scripts/allocate-address.sh` 依赖 `flock` 命令，macOS 默认不可用。需要安装 `flock`（如 `brew install flock`）或修改脚本使用 macOS 兼容的锁机制（如 `shlock` 或 `mkdir` 方式）。

### 待回填（信息性）

26 个旧页面没有地址（created < 2026-04-23 或属于 claude-obsidian 核心页面）。这是预期状态，不需要立即处理。

---

## Semantic Tiling (DragonScale Mechanism 3)

- 状态: **不可用**
- 根因: `scripts/tiling-check.py` 第 258 行使用 `Path | None` 联合类型语法，需要 Python 3.10+。当前环境 Python 3.9.6。
- 建议: 升级 Python 到 3.10+，或将类型注解改为 `Optional[Path]` 以兼容 Python 3.9。

---

## Naming Convention Check

### 文件名

绝大部分中文页面使用 Title Case 中文命名，合规。以下例外：

- `sources/DaVinci-Resolve-20-2-Reference-Manual.md` — 英文文件名，与中文 wikilink 体系不一致（见 Dead Links 部分）
- `sources/Transkoder-2025-User-Guide.md` — 同上
- `sources/dftt_timecode.md` — 小写开头（应为 `DFTT Timecode.md` 或 `DFTT 时间码库.md`）
- `sources/3dResolveSubtitle.md` — 数字开头 + camelCase
- `sources/StereoscopicSubtitlePlugin.md` — camelCase
- `sources/YYHG_gallery.md` — 混合命名
- `sources/claude-obsidian-ecosystem-research.md` — kebab-case（claude-obsidian 核心页面使用此风格，可接受）

### 文件夹

所有文件夹使用小写加连字符，合规。

### Wikilink 与文件名一致性

两个系统性不匹配（见 Dead Links），是本次 lint 最严重的发现问题。

---

## Writing Style Check

对 20 个代表性页面进行了抽查：

- **声明式现在时**: 总体良好。少数页面使用 "basically"、"essentially" 等模糊词（如 `concepts/LLM Wiki Pattern.md`）。
- **来源引用**: Transkoder/DaVinci 概念页使用 "Source:" 引用格式，但部分引用指向了中文 wikilink 名（死链）。
- **不确定性标记**: 未发现需要使用 `> [!gap]` 标记但未标记的内容。
- **矛盾标记**: 未发现未标记的矛盾。

---

## Cross-Reference Gaps

域 _index 页面引用了多个不存在的工作流页面和概念页面（见 Dead Links > 缺少的页面）。这些引用表明预期的 wiki 结构比实际创建的更完整，需要补充页面或调整 _index 中的链接。

---

## 建议修复优先级

### BLOCKER（阻碍 wiki 正常导航）

1. 修复 `[[DaVinci Resolve 20.2 参考手册]]` → 重命名文件或替换 18 个 wikilink
2. 修复 `[[Transkoder 2025 用户指南]]` → 重命名文件或替换 24 个 wikilink
3. 修复 `[[How does the LLM Wiki pattern work?]]` → 去掉问号（4 处）

### HIGH（大量页面受影响）

4. 为 54 个 post-rollout 页面分配 DragonScale 地址
5. 为 ~90 个页面补充 tags 字段
6. 修复 6 个非标准 type 值和 7 个非标准 status 值

### MEDIUM（功能缺失）

7. 创建 _index 中引用的 5 个缺失页面或更新 _index 链接
8. 修复 `scripts/allocate-address.sh` 的 macOS 兼容性（flock 问题）
9. 修复 `scripts/tiling-check.py` 的 Python 3.9 兼容性
10. 更新 `wiki/index.md` 的页面统计

### LOW（清理）

11. 移除 DragonScale Memory 和 log 中的 `[[Foo]]` / `[[notes/Foo]]` 占位符
12. 移除 3 个 _index 页面的空占位符章节
13. 处理 4 个 orphan 页面（添加入站链接或确认故意孤立）