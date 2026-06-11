---
name: wiki-query
description: "Answer questions using the Obsidian wiki vault. Reads hot cache first, then index, then relevant pages. Synthesizes answers with citations. Files good answers back as wiki pages. Supports quick, standard, and deep modes. Triggers on: what do you know about, query:, what is, explain, summarize, find in wiki, search the wiki, based on the wiki, wiki query quick, wiki query deep."
allowed-tools: Read Glob Grep Bash
---

# wiki-query: Query the Wiki

The wiki has already done the synthesis work. Read strategically, answer precisely, and file good answers back so the knowledge compounds.

---

## Transport (v1.7+)

Reads should prefer the same transport the rest of the plugin uses. Consult `.vault-meta/transport.json` (auto-created by `bash scripts/detect-transport.sh`) and use the `preferred` entry:

- **cli** — `obsidian-cli read "$VAULT" "$NOTE"` and `obsidian-cli search "$VAULT" "<query>"` (Obsidian-native ranking); see [`skills/wiki-cli/SKILL.md`](../wiki-cli/SKILL.md)
- **mcp-obsidian** / **mcpvault** — `mcp__obsidian-vault__read_note`, `search_notes`; see [`skills/wiki/references/mcp-setup.md`](../wiki/references/mcp-setup.md)
- **filesystem** — Claude's `Read` and `Glob`/`Grep` tools (final floor; always works)

Full decision tree: [`wiki/references/transport-fallback.md`](../../wiki/references/transport-fallback.md). Quick mode (hot.md only) is transport-agnostic — always uses `Read`.

---

## Retrieval Escalation (v1.7+)

This vault follows **Wiki-first by default**. The default query path is:

1. `wiki/hot.md`
2. `wiki/index.md`
3. relevant `_index.md` pages
4. relevant wiki pages

Do not escalate automatically just because the wiki answer is brief. If the user wants more detail, more evidence, or a return to the source material, treat that as an explicit escalation request. Typical user signals include:

- "这个不够全面"
- "继续深挖"
- "回原文找"
- "给出处"
- "给完整步骤"

On explicit escalation, first run **raw locate** against normalized raw material, then optionally use `wiki-retrieve` if it is feature-detected — `[ -x scripts/retrieve.py ] && [ -d .vault-meta/chunks ] && [ -f .vault-meta/bm25/index.json ]`.

Raw locate means:

1. Search `.raw/documents/**/_normalized/**` and `.raw/repos/**` with `rg`/`grep`
2. Prefer the smallest understandable section that contains the hit
3. If no section structure exists, fall back to roughly 20 lines before and after the hit
4. Keep each candidate block around ~600-1200 tokens
5. Send at most 5 candidate blocks into retrieval
6. If only 1-2 candidate blocks are already clear, read them directly and skip retrieval

If retrieval is needed after raw locate, use:

```bash
python3 scripts/retrieve.py "<the user's question verbatim>" --top 5
```

Output is JSON with a `candidates` array. Each candidate has `absolute_path` to the source page, a `snippet`, and `bm25_score` + `rerank_score`. Read the cited pages (using the transport selector from §Transport above) and synthesize with chunk-level citation.

If `retrieve.py` exits 10 (feature not provisioned), or any step in the pipeline errors, stay on the wiki + raw-locate path and report the coverage gap rather than pretending the fallback succeeded.

Quick mode always skips escalation and retrieval (hot.md only — keeps the ~1,500 token budget intact).

Full spec: [`skills/wiki-retrieve/SKILL.md`](../wiki-retrieve/SKILL.md). Setup: `bash bin/setup-retrieve.sh`. The wiki-first workflows below remain authoritative unless the user explicitly asks to go deeper.

---

## Query Modes

Three depths. Choose based on the question complexity.

| Mode | Trigger | Reads | Token cost | Best for |
|------|---------|-------|------------|---------|
| **Quick** | `query quick: ...` or simple factual Q | hot.md + index.md only | ~1,500 | "What is X?", date lookups, quick facts |
| **Standard** | default (no flag) | hot.md + index + 3-5 pages | ~3,000 | Most questions |
| **Deep** | `query deep: ...` or "thorough", "comprehensive" | Full wiki + optional web | ~8,000+ | "Compare A vs B across everything", synthesis, gap analysis |

---

## Quick Mode

Use when the answer is likely in the hot cache or index summary.

1. Read `wiki/hot.md`. If it answers the question, respond immediately.
2. If not, read `wiki/index.md`. Scan descriptions for the answer.
3. If found in index summary, respond and do not open any pages.
4. If not found, say "Not in quick cache. Run as standard query?"

Do not open individual wiki pages in quick mode.

---

## Standard Query Workflow

1. **Read** `wiki/hot.md` first. It may already have the answer or directly relevant context.
2. **Read** `wiki/index.md` to find the most relevant pages (scan for titles and descriptions).
3. **Read** those pages. Follow wikilinks to depth-2 for key entities, concepts, workflows, and domains. No deeper.
4. **Synthesize** the answer in chat if the wiki is sufficient. Cite sources with wikilinks: `(Source: [[Page Name]])`.
5. **If the answer is still thin**, say so explicitly, but do not escalate on your own. Offer the user a deeper pass back to the source material.
6. **Only if the user explicitly asks to go deeper**, run raw locate against normalized raw material with `rg`/`grep`, read the matched sections, and use retrieval only if the candidate set is still broad and `wiki-retrieve` is provisioned.
7. **If raw locate already narrows the answer to 1-2 clear source sections**, read them directly and answer without calling retrieval.
8. **Offer to file** the answer. Use `wiki/questions/` for synthesis, `wiki/comparisons/` for side-by-side analysis, and `wiki/workflows/` when the answer is mainly a reusable procedure.
9. If the question reveals a **gap** after wiki, raw locate, and retrieval fallback: say "I don't have enough on X. Want to ingest or research a source?"

---

## Deep Mode

Use for synthesis questions, comparisons, or "tell me everything about X."

1. Read `wiki/hot.md` and `wiki/index.md`.
2. Identify all relevant sections (concepts, entities, workflows, sources, comparisons, domains).
3. Read every relevant wiki page first. No skipping.
4. If wiki coverage is still thin, state the limit clearly and offer a deeper source-grounded pass. Do not escalate unless the user explicitly asks for it.
5. On explicit user escalation, run raw locate first, then use retrieval only if raw locate leaves multiple plausible candidate sections.
6. If the vault is still thin after that, offer to supplement with web search or additional ingest.
7. Synthesize a comprehensive answer with full citations.
8. Suggest filing the result back as a wiki page. Prefer `workflows/` when the result is an end-to-end procedure.

---

## Token Discipline

Read the minimum needed:

| Start with | Cost (approx) | When to stop |
|------------|---------------|--------------|
| hot.md | ~500 tokens | If it has the answer |
| index.md | ~1000 tokens | If you can identify 3-5 relevant pages |
| 3-5 wiki pages | ~300 tokens each | Usually sufficient |
| 10+ wiki pages | expensive | Only for synthesis across the entire wiki |

If hot.md has the answer, respond without reading further.

---

## Index Format Reference

The master index (`wiki/index.md`) looks like:

```markdown
## Domains
- [[Domain Name]]: description (N sources)

## Entities
- [[Entity Name]]: role (first: [[Source]])

## Concepts
- [[Concept Name]]: definition (status: developing)

## Sources
- [[Source Title]]: author, date, type

## Workflows
- [[Workflow Name]]: what task or procedure it covers

## Questions
- [[Question Title]]: answer summary
```

Scan the section headers first to determine which sections to read.

---

## Domain Sub-Index Format

Each domain folder has a `_index.md` for focused lookups:

```markdown
---
type: meta
title: "Entities Index"
updated: YYYY-MM-DD
---
# Entities

## People
- [[Person Name]]: role, org

## Organizations
- [[Org Name]]: what they do

## Products
- [[Product Name]]: category
```

Use sub-indexes when the question is scoped to one domain. Avoid reading the full master index for narrow queries.

---

## Filing Answers Back

Good answers compound into the wiki. Don't let insights disappear into chat history.

When filing an answer:

```yaml
---
type: question
title: "Short descriptive title"
question: "The exact query as asked."
answer_quality: solid
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [question, <domain>]
related:
  - "[[Page referenced in answer]]"
sources:
  - "[[wiki/sources/relevant-source.md]]"
status: developing
---
```

Then write the answer as the page body. Include citations. Link every mentioned concept, entity, workflow, or domain.

After filing, add an entry to `wiki/index.md` under Questions and append to `wiki/log.md`.

---

## Gap Handling

If the question cannot be answered from the wiki:

1. Say clearly: "I don't have enough in the wiki to answer this well."
2. Identify the specific gap: "I have nothing on [subtopic]."
3. If the user explicitly wants a deeper answer, run raw locate first and use retrieval only if needed after that.
4. Suggest: "Want to find or ingest a source on this? I can help process one."
5. Do not fabricate. Do not answer from training data if the question is about the specific domain in this wiki.

---

## How to think (10-principle mapping)

When working on this skill, apply the 10-principle loop. See [`skills/think/SKILL.md`](../think/SKILL.md) for the canonical framework.

| # | Principle | Application here |
|---|-----------|-------------------|
| 1 | OBSERVE (ext) | Read `wiki/hot.md` first, then `wiki/index.md`, then specific pages. Don't skip the cache. |
| 2 | OBSERVE (int) | Am I synthesizing from training-data memory when I should be citing wiki pages? Check the source of each claim. |
| 3 | LISTEN | What is the user's REAL question? The surface query is often a proxy for a deeper need. |
| 4 | THINK | Quick / standard / deep mode? Match depth to question complexity, not eagerness. |
| 5 | CONNECT (lat) | Are there pages I missed that would CHANGE the answer? Cross-check related pages before answering. |
| 6 | CONNECT (sys) | Hot cache + index + wiki-retrieve (when provisioned) layer into a single retrieval pipeline. |
| 7 | FEEL | Cite specific pages, not vague references. Future-me wants traceability back to the source page. |
| 8 | ACCEPT | When the wiki doesn't have the answer, say so explicitly. Don't fabricate from training data. |
| 9 | CREATE | The answer with citations + an offer to file the answer if it's worth keeping. |
| 10 | GROW | Questions the wiki can't answer are content gaps — log them as autoresearch inputs. |
