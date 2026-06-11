# claude-obsidian — Claude + Obsidian Wiki Vault

This folder is both a Claude Code plugin and an Obsidian vault.

**Plugin name:** `claude-obsidian`  
**Skills:** `/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/wiki-cli`, `/wiki-retrieve`, `/wiki-mode`  
**Vault path:** This directory (open in Obsidian directly)

## What This Vault Is For

This fork is being adapted into an enterprise-internal knowledge base prototype. Its main job is to turn software manuals, platform instructions, process notes, troubleshooting writeups, internal technical documents, screenshots, and repositories into a maintained Obsidian wiki.

The project follows the LLM Wiki pattern:

1. `.raw/` is the immutable source layer
2. `wiki/` is the maintained synthesis layer
3. `AGENTS.md` and `CLAUDE.md` are the schema layer

## Vault Structure

```text
.raw/
  documents/     document extracts, local HTML bundle markdown, imported text
  images/        screenshots, diagrams, scans, OCR notes
  code-data/     code snippets, configs, structured extracts
  repos/         git repositories used as source material

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

_templates/     Obsidian templates for wiki page types
_attachments/   images and PDFs referenced by wiki pages
```

Legacy `.raw/*.md` pages from older versions remain valid inputs, but new ingest work should prefer the typed subfolders under `.raw/`.

## How to Use

Put or normalize source material into `.raw/`, then tell the agent to ingest it.

`wiki-ingest` should treat ingest as a compilation pass, not a summary pass. For large manuals, platform guides, and operational documents, it should actively identify likely future questions, stable workflows, recurring settings, and key concepts, then write wiki pages that reduce future fallback to raw sections.

The expected query behavior is **Wiki-first by default, with user-driven escalation**:

1. Read `wiki/hot.md`
2. Read `wiki/index.md`
3. Read relevant `_index.md` pages and target wiki pages
4. If the answer is still thin, say so and offer a deeper source-grounded pass
5. Only when the user explicitly asks to go deeper, run raw locate against normalized raw material
6. Use retrieval after raw locate only if multiple candidate sections still need reranking

Run `/wiki` to scaffold or repair vault structure.

Run `lint the wiki` every 10-15 ingests to catch orphans, stale claims, missing workflow pages, and weak cross-links.

## Cross-Project Access

To reference this wiki from another Claude Code project, add to that project's CLAUDE.md:

```markdown
## Wiki Knowledge Base
Path: /path/to/this/vault

When you need context not already in this project:
1. Read wiki/hot.md first (recent context, ~500 words)
2. If not enough, read wiki/index.md
3. If you need domain specifics, read wiki/<domain>/_index.md
4. Only then read individual wiki pages
5. If the user explicitly asks for more detail or original evidence, search normalized raw material first
6. Use retrieval from raw sources only after raw locate if the candidate set is still broad

Do NOT read the wiki for general coding questions or things already in this project.
```

## Plugin Skills

| Skill | Trigger |
|-------|---------|
| `/wiki` | Setup, scaffold, route to sub-skills |
| `ingest [source]` | Single or batch source ingestion |
| `query: [question]` | Answer from wiki content |
| `lint the wiki` | Health check |
| `/save` | File the current conversation as a structured wiki note |
| `/autoresearch [topic]` | Autonomous research loop: search, fetch, synthesize, file |
| `/canvas` | Visual layer: add images, PDFs, notes to Obsidian canvas |
| `/wiki-cli` (v1.7) | Obsidian CLI transport wrapper; default mutation path on desktop |
| `/wiki-retrieve` (v1.7) | Hybrid contextual + BM25 + cosine-rerank retrieval (opt-in via `bash bin/setup-retrieve.sh`) |
| `/wiki-mode` (v1.8) | Methodology modes (LYT / PARA / Zettelkasten / Generic). Set via `bash bin/setup-mode.sh`; consumed by wiki-ingest / save / autoresearch for routing new pages |
| `/think` (v1.9) | The 10-principle thinking loop (OBSERVE-OBSERVE-LISTEN-THINK-CONNECT-CONNECT-FEEL-ACCEPT-CREATE-GROW) as an invocable workflow. Apply to architectural decisions, audits, post-mortems, ambiguous user requests. Every other skill has a "How to think" appendix mapping this framework to its specific work |

## Page Types

- `wiki/sources/`: source summary pages with provenance
- `wiki/entities/`: named systems, teams, orgs, products, repos, services
- `wiki/concepts/`: concepts, principles, standards, abstractions
- `wiki/workflows/`: procedural knowledge, runbooks, operating steps, packaging flows, troubleshooting flows
- `wiki/domains/`: top-level navigation pages, aligned to business or platform areas
- `wiki/questions/`: durable query outputs
- `wiki/comparisons/`: side-by-side analyses

## Transport (v1.7+)

`scripts/detect-transport.sh` writes `.vault-meta/transport.json` on first run and refreshes weekly. Skills consult it before mutating the vault. Fallback chain: Obsidian CLI → mcp-obsidian → mcpvault → filesystem (always-available floor). Decision tree: [wiki/references/transport-fallback.md](wiki/references/transport-fallback.md).

## Concurrency (v1.7+)

`scripts/wiki-lock.sh` provides per-file advisory locks for safe multi-writer ingest. Every wiki page write should be guarded by `wiki-lock acquire`/`release`. Stale-after default is 60s; cross-process release allowed by design. The PostToolUse hook defers `git add` while locks are held. Closes the latent multi-writer corruption hole from v1.6.

## Methodology Modes (v1.8+)

Pick an organizational style for the vault via `bash bin/setup-mode.sh`. Four modes available: **generic** (default), **LYT**, **PARA**, **Zettelkasten**. The mode is written to `.vault-meta/mode.json` (gitignored by default; `git add -f` to commit). `wiki-ingest`, `save`, and `autoresearch` consult `python3 scripts/wiki-mode.py route <type> "<name>"` before filing new pages.

For this enterprise MVP, `generic` remains the primary target mode because it preserves the explicit `sources/entities/concepts/workflows/domains` layout we want to validate.

## Enterprise Rules

- Prefer `.raw/documents/`, `.raw/images/`, `.raw/code-data/`, and `.raw/repos/` for new source intake.
- Treat repositories as raw sources, not just URLs. Shallow clones are acceptable.
- Large manuals should not stop at overview pages. Ingest should proactively extract workflows, settings, field meanings, constraints, and likely user questions.
- When a source was split into section pages, important workflow and concept pages should point to those sections directly.
- Do not collapse procedural knowledge into `concepts/` when the page primarily answers "how do I do this?" That belongs in `workflows/`.
- If common questions still require broad raw searching after ingest, the ingest is not finished.
- Good answers should usually be written back into the wiki as `questions/`, `comparisons/`, or `workflows/` depending on their shape.
- Retrieval is a supplement, not the primary knowledge surface.
- Query-time escalation should prefer raw locate first, then retrieval only if raw locate still leaves too many plausible sections.

## Pre-commit verifier (v1.7.1+)

After staging changes for a non-trivial workstream but BEFORE running `git commit`, dispatch the `verifier` agent (`agents/verifier.md`). It reads `git diff --cached`, applies the /best-practices six-cut + agent kernel, and returns findings in four tiers (BLOCKER / HIGH / MEDIUM / LOW) with file:line citations. The agent has read-only tools (Read, Grep, Glob, Bash) — it can inspect but never modify, so its output is purely advisory. This closes the loop the v1.7 audit revealed: code went worker → commit with no separate verifier pass, which is how BLOCKER B1 (data-egress consent gap) slipped through. See `docs/audits/v1.7.0-audit-2026-05-17.md` §10 for the retrospective.

## MCP (Optional)

If you configured the MCP server, Claude can read and write vault notes directly.
See `skills/wiki/references/mcp-setup.md` for setup instructions.

## Release Blog Post

After cutting a new release (git tag + `gh release create`), run:

```
/release-blog
```

This generates a blog post on https://agricidaniel.com/blog/, handles cover image generation, SEO metadata, FAQ schema, internal linking, sitemap/llms.txt updates, Vercel deployment, and Google indexing.
