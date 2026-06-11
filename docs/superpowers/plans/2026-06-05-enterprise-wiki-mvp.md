# Enterprise Wiki MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adapt `claude-obsidian` into an enterprise-internal wiki MVP that keeps the Obsidian vault workflow, adds `workflows/`, adopts typed raw-source folders, and defaults to Wiki-first with retrieval as fallback.

**Architecture:** Keep the mother template intact where possible. Update the schema and skill layer first so the vault rules, ingest/query/lint behavior, and setup scripts all agree on one structure. Add only the minimum new page type and raw folder conventions needed for the enterprise prototype.

**Tech Stack:** Markdown, Obsidian vault structure, shell setup scripts, Python routing helper, Agent Skills.

---

### Task 1: Lock the schema

**Files:**
- Modify: `AGENTS.md`
- Modify: `CLAUDE.md`
- Modify: `skills/wiki/SKILL.md`
- Modify: `skills/wiki/references/frontmatter.md`

- [x] Rewrite the vault-level instructions so `AGENTS.md` and `CLAUDE.md` define the same three-layer architecture, raw folder layout, wiki page types, and `Wiki-first + RAG fallback` query policy.
- [x] Update the wiki orchestration skill so scaffolded vaults create the enterprise folder map and emit both `AGENTS.md` and `CLAUDE.md` for cross-agent compatibility.
- [x] Extend the documented frontmatter schema with `workflow` and with generalized raw-source references instead of the old `.raw/articles/...` convention.

### Task 2: Update the core wiki operations

**Files:**
- Modify: `skills/wiki-ingest/SKILL.md`
- Modify: `skills/wiki-query/SKILL.md`
- Modify: `skills/wiki-lint/SKILL.md`
- Modify: `agents/wiki-ingest.md`

- [x] Change ingest rules so raw inputs prefer `.raw/documents/`, `.raw/images/`, `.raw/code-data/`, and `.raw/repos/`, while still tolerating legacy `.raw/*.md` files already in the sample vault.
- [x] Add `workflow` as a first-class knowledge page in ingest and batch-ingest instructions, including `_index.md` maintenance and log examples.
- [x] Change query rules so the agent reads `hot.md`, `index.md`, domain or type indexes, and relevant wiki pages before invoking retrieval; retrieval is only used when wiki coverage is insufficient.
- [x] Extend lint guidance so health checks include workflow coverage, workflow orphans, and workflow dashboard visibility.

### Task 3: Align routing, templates, and setup

**Files:**
- Create: `_templates/workflow.md`
- Create: `wiki/workflows/_index.md`
- Create: `wiki/domains/_index.md`
- Modify: `scripts/wiki-mode.py`
- Modify: `bin/setup-vault.sh`
- Modify: `bin/setup-mode.sh`

- [x] Add a `workflow` route type to `scripts/wiki-mode.py` so generic mode files to `wiki/workflows/` and other modes preserve their existing conventions.
- [x] Add the new folder structure to setup scripts, including typed `.raw/` subfolders and `wiki/workflows/`.
- [x] Add workflow and domain index seed files so the sample vault matches the declared structure.

### Task 4: Align navigation and Obsidian presentation

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/meta/dashboard.md`
- Modify: `wiki/meta/dashboard.base`
- Modify: `.obsidian/graph.json`
- Modify: `.obsidian/app.json`
- Modify: `.obsidian/snippets/vault-colors.css`
- Modify: `skills/wiki/references/css-snippets.md`

- [x] Add workflow and domain navigation to the sample wiki index and dashboards.
- [ ] Update graph colors, CSS snippet guidance, and ignored-files settings so the new folders are visible in the right places and hidden in the wrong ones.

### Task 5: Verify consistency

**Files:**
- Review: all files touched above

- [x] Search for stale `.raw/articles/` references in the files modified by this change and replace them with the new conventions or explicit legacy-compatibility wording.
- [x] Search for stale assumptions that only `sources/entities/concepts` exist and patch the affected instructions to include `workflows` where appropriate.
- [x] Run a final read-through of the modified files to confirm the schema, skills, setup scripts, and sample vault now describe the same structure.
