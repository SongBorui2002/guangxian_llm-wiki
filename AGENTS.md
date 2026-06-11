# claude-obsidian: Agent Instructions

This repo is an Obsidian vault and cross-agent skill pack for building persistent, compounding knowledge bases using Andrej Karpathy's LLM Wiki pattern. This fork is being adapted as an **enterprise internal wiki MVP** for software manuals, platform guides, operational procedures, and internal technical notes.

It is intended to work with any AI coding agent that supports the Agent Skills standard, including Codex CLI, Claude Code, OpenCode, and similar tools.

The core rule is simple: **raw sources stay immutable, the wiki is LLM-maintained, and the schema files (`AGENTS.md` / `CLAUDE.md`) define the maintenance discipline.**

## Skills Discovery

All skills live in `skills/<name>/SKILL.md`. Codex / OpenCode / other Agent Skills compatible agents will auto-discover them when you symlink the directory:

```bash
# Codex CLI
ln -s "$(pwd)/skills" ~/.codex/skills/claude-obsidian

# OpenCode
ln -s "$(pwd)/skills" ~/.opencode/skills/claude-obsidian
```

Or run the bundled installer:

```bash
bash bin/setup-multi-agent.sh
```

## Available Skills

| Skill | Trigger phrases |
|---|---|
| `wiki` | `/wiki`, set up wiki, scaffold vault |
| `wiki-ingest` | ingest, ingest this url, ingest this image, batch ingest |
| `wiki-query` | query, what do you know about, query quick:, query deep: |
| `wiki-lint` | lint the wiki, health check, find orphans |
| `wiki-fold` | fold the log, run a fold, log rollup (DragonScale Mechanism 1, opt-in) |
| `save` | /save, file this conversation |
| `autoresearch` | autoresearch, autonomous research loop |
| `canvas` | /canvas, add to canvas, create canvas |
| `defuddle` | clean this url, defuddle |
| `obsidian-markdown` | obsidian syntax, wikilink, callout |
| `obsidian-bases` | obsidian bases, .base file, dynamic table |

## Architecture

Three layers:

1. **Raw sources**: `.raw/` stores the source of truth. Agents read from it but do not rewrite the underlying source material.
2. **Wiki**: `wiki/` stores synthesized Markdown pages maintained by the agent.
3. **Schema**: `AGENTS.md` and `CLAUDE.md` define structure, naming, ingest/query/lint behavior, and filing conventions.

## Vault Structure

```text
.raw/
  documents/     normalized document sources, exported HTML bundles, text extracts
  images/        screenshots, diagrams, scans, OCR-derived source notes
  code-data/     code snippets, configs, structured data extracts
  repos/         shallow-cloned repositories treated as raw source material

wiki/
  index.md
  overview.md
  log.md
  hot.md
  sources/
  entities/
  concepts/
  workflows/
  domains/
  comparisons/
  questions/
  meta/
  canvases/
```

Legacy `.raw/*.md` files in older vaults are still readable and ingestible. New source normalization should prefer the typed subfolders above.

## Page Semantics

- `sources/`: one wiki page per ingested source or normalized source bundle
- `entities/`: people, teams, orgs, products, services, repositories, platforms
- `concepts/`: terms, mechanisms, rules, abstractions, standards, recurring technical ideas
- `workflows/`: repeatable how-to knowledge, procedures, runbooks, task flows, packaging steps, troubleshooting flows
- `domains/`: top-level business or platform entry points for navigation
- `comparisons/`: cross-system or cross-version analyses
- `questions/`: durable answers and analyses worth keeping
- `meta/`: dashboards, lint reports, conventions, maintenance artifacts
- `canvases/`: optional Obsidian canvas views tied to the wiki

## Operating Rules

- **Wiki-first query path**: answer from `wiki/hot.md`, `wiki/index.md`, sub-indexes, and relevant wiki pages first.
- **User-driven escalation**: if the user explicitly wants more detail, stronger evidence, exact source grounding, or a return to the original material, escalate from wiki-only answering to raw locate in normalized raw sources.
- **Retrieval after raw locate**: after raw locate narrows the candidate sections, use retrieval against raw or chunked material only if the narrowed set is still broad enough to need reranking.
- **Ingest is compilation, not summary**: the goal of ingest is to compile source material into wiki pages that reduce future query-time fallback to raw sections.
- **Self-interrogation on large sources**: manuals, platform guides, and process documents should be interrogated for likely future questions, stable workflows, and recurring settings or concepts, not only summarized.
- **Automatic write-back**: high-value ingest and query results should update the wiki directly rather than waiting for manual confirmation.
- **Source immutability**: do not rewrite the user's underlying documents, images, or repositories. Normalized markdown derivatives are allowed as ingest inputs inside `.raw/`.
- **Repository sources**: treat `.raw/repos/` as first-class sources, but only when the source is an actual git repository. Do not classify a plain local folder as `repo`; local HTML bundles belong under `.raw/documents/`. Repositories may be shallow-cloned and scanned broadly, but noisy directories and binary-heavy assets should usually be skipped during synthesis.
- **HTML bundles**: local `html + asset directory` source sets should be treated as document bundles. Preserve path traceability in the normalized markdown.
- **Section-grounded synthesis**: when a source is split into meaningful sections, key workflow and concept pages should cite the specific section pages that support them, not only the top-level source page.
- **Manifest**: `.raw/.manifest.json` tracks deltas and page updates per source.

## Bootstrap

When the user opens this project for the first time:

1. Read this file (`AGENTS.md`) and the project `CLAUDE.md` for full context
2. Read `skills/wiki/SKILL.md` for the orchestration pattern
3. If `wiki/hot.md` exists, read it silently to restore recent context
4. If the user types `/wiki` (or "set up wiki"), follow the wiki skill's scaffold workflow

## Reference

- Plugin homepage (public canonical): https://github.com/AgriciDaniel/claude-obsidian
- Community early-access mirror (Pro): https://github.com/AI-Marketing-Hub
- Pattern source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Cross-reference: https://github.com/kepano/obsidian-skills (authoritative Obsidian-specific skills)
