# 原型评估记录

本文档记录当前企业级 `LLM-Wiki` 原型在真实资料上的阶段性观察。它不是最终结论，更不是产品承诺；它的作用是把已经看到的行为、收益和限制沉淀下来，避免后续讨论只停留在聊天记录里。

---

## 1. 当前原型关注什么

当前原型验证的重点不是“能不能做一次问答”，而是下面三件事：

1. 原始资料能否被稳定编译进 `wiki/`，而不是每次从头读原文。
2. 查询时能否优先依赖 wiki 层完成综合，而不是默认退化成普通 RAG。
3. 当 wiki 首轮总结不够时，系统能否在用户显式要求下回到 raw source 做更深取证。

换句话说，这个原型强调的是：

- `wiki-first`
- `source-grounded fallback`
- `可持续演化`

而不是“一次性检索命中率”本身。

---

## 2. 当前三层结构

### Raw sources

原始资料层已经按 typed intake 拆分，而不是全部混在一起：

- `.raw/documents/`：说明书、用户手册、HTML bundle、导出的文本
- `.raw/images/`：截图、流程图、扫描件
- `.raw/code-data/`：代码片段、配置、结构化数据
- `.raw/repos/`：git 仓库源码资料

这一层仍然是事实源。允许在 `.raw/` 内生成 normalized Markdown 作为后续 ingest 和检索的中间产物，但不改写原始资料本身。

### Wiki

`wiki/` 是 LLM 维护的知识层，目前重点页面类型包括：

- `sources/`：每个来源的来源页
- `entities/`：产品、平台、团队、仓库、服务等实体
- `concepts/`：术语、机制、字段含义、规则
- `workflows/`：步骤、流程、runbook、troubleshooting、制作流程
- `domains/`：业务、产品、平台维度的入口
- `questions/`：值得沉淀的问题与答案
- `comparisons/`：对比分析和决策页面
- `meta/`、`canvases/`：维护、导航和 Obsidian 辅助层

这里最重要的调整之一，是把 `workflows/` 作为独立页面类型，而不是把流程类知识继续混进 `concepts/`。

### Schema

规则层由 `AGENTS.md`、`CLAUDE.md`、各个 `skills/` 文档和辅助脚本共同组成。当前最关键的约束包括：

- ingest 是“知识编译”，不是“简单摘要”
- 大型手册需要自我追问并产出可复用页面
- query 默认 `wiki-first`
- 只有用户显式要求更深、更全、给出处、回原文时，才升级到 raw locate 和 retrieval

---

## 3. 当前看到的收益

### 3.1 第二次查询可能比第一次更接近真实操作路径

在实际实验中可以观察到：

- 首次提问时，LLM 并没有优先关注 `XYZRGB Conversion` 和交付界面的 `working colorspace`
- 在第二次提出相近但实质不同的问题后，回答开始聚焦 `XYZRGB Conversion` 和交付界面的 `working colorspace`
- 从后续人工核验来看，这条路径更接近正确的打包路径

这说明当前系统已经有一定的“通过 wiki 与追问逐渐收敛”的能力，但也说明首轮 ingest 和首轮 query 仍可能漏掉关键操作点。

### 3.2 workflow 类型比大而泛的 summary 更适合操作类资料

对于软件说明书、平台使用手册、制作流程、内部 runbook 这类资料，真正有价值的页面往往不是“这份文档讲了什么”，而是：

- 某个设置在哪里改
- 某个输出流程怎么走
- 某一步跳过会有什么影响
- 某个字段只是 metadata 还是会真正改变结果

因此把知识落成 `workflow` 页面，比只写一篇 overview 更符合后续查询价值。

### 3.3 LLM-Wiki 的优势不是“更会找”，而是“更会积累”

当前原型最明显的优势仍然在于：

- 可以把问答结果继续沉淀回 `questions/`、`comparisons/`、`workflows/`
- 可以随着 ingest 和 query 反复迭代，让 wiki 越来越贴近真实工作问题
- 可以逐步把“原文里散落的点”编译成更稳定的操作知识

这和普通 RAG 的差异在于：RAG 更像一次性取片段，LLM-Wiki 更像持续编库。

---

## 4. 当前看到的限制

### 4.1 首轮 ingest 仍可能过于概括

如果 ingest 只生成“大而宽”的来源页和概念页，而没有深入拆出 `workflow`、字段说明、常见问题、章节级引用，那么后续 query 会显得像：

- 第一次回答偏泛
- 第二次才逐渐对准真正关键的操作点

这意味着 ingest skill 的约束虽然已经增强，但真实效果仍依赖：

- normalize 后的文档结构质量
- 模型是否真的执行了自我追问
- 是否把章节级细节转成可复用页面

### 4.2 当前 retrieval 基础设施已存在，但仍不是完整 raw-native retrieval

当前已经具备：

- `wiki-first` 查询路径
- `raw locate -> retrieve` 的 skill 规则
- BM25 + rerank 的 retrieval 基础设施
- `ollama / api / noop` 多后端 rerank

但当前实现里，chunk 与索引缓存仍主要围绕 wiki 层构建。也就是说：

- “回原文深挖”的规则已经有了
- “完全以 raw 为主的 retrieval 替换”还在继续收敛

这点必须和外部说明保持一致，不能写成已经彻底完成。

### 4.3 操作类问题对 section 级证据依赖很强

对于参数设置、导出流程、安装步骤、异常处理这类问题，如果不能落到具体章节或具体片段，仅凭来源总页很容易丢失关键上下文。

所以当前原型能否继续变强，关键不在于“多读几个 chunk”，而在于：

- 是否能先找准 section
- 是否能围绕 section 组织 workflow / question / comparison 页面

---

## 5. 深挖路径的当前理解

当前推荐的深挖路径不是“默认就上 RAG”，而是：

1. 先走 `wiki-first`
2. 如果用户明确说“不够全面 / 继续深挖 / 给出处 / 回原文找”
3. 先在 normalized raw material 上做 `rg/grep`
4. 如果已经缩到 1-2 个清晰片段，直接读片段
5. 只有候选段仍较多时，再进入 `retrieve.py`

这个顺序很重要，因为它避免了把 RAG 变成主流程，同时保留了对原文取证的能力。

---

## 6. lint 的作用

lint 在这个项目里不是语法检查，而是 wiki 健康检查。它的价值主要在于发现：

- 孤立页面
- 失效链接
- 过时断言
- 应该存在但尚未拆出的概念页
- 应该升级为 workflow 的流程型内容
- 应该补回原文证据的高风险页面

对当前原型而言，lint 的意义不仅是“清理”，更是暴露 wiki 编译还不够充分的地方。

---

## 7. embedding / rerank 后端的当前观察

当前代码层已经支持三种 rerank 后端路由：

- `ollama`
- `api`
- `noop`

当本地没有可用 `ollama` 时，可以改走 API embeddings；如果两者都不可用，则回退为 `noop`，保证主流程不断。

此外，在当前实验讨论中，也记录过一些可作为后续 API embedding 候选的模型写法。这些记录更适合作为“候选池”而不是稳定承诺，因为外部模型可用性和命名会变化：

- `qwen/qwen3-embedding-8b`
- `mistralai/codestral-embed-2505`
- `thenlper/gte-large`

如果后续要把这些模型正式写进面向外部的使用说明，应该在写入前再次核验提供方文档和实际接口兼容性。

---

## 8. 下一步最值得继续验证什么

当前最值得继续验证的不是“再加多少功能”，而是下面这些更贴近核心价值的点：

1. 首轮 ingest 是否能稳定拆出更好的 `workflow` / `question` / `comparison`
2. raw locate 是否能更稳定命中真正关键 section
3. retrieval 是否要从当前 wiki chunk 进一步收敛到 raw-native 路径
4. lint 是否能稳定指出“这页应该升级为 workflow”或“这页缺少原文依据”

如果这些点被验证清楚，这个原型才真正体现出它相对传统 RAG 的优势：不是更像搜索器，而是更像一个持续被 LLM 编译、维护和修正的知识库。
