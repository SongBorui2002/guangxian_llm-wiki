---
name: wiki-ingest
description: "Ingest sources into the Obsidian wiki vault. Reads a source, extracts entities, concepts, and workflows, creates or updates wiki pages, cross-references, and logs the operation. Supports files, URLs, and batch mode. Triggers on: ingest, process this source, add this to the wiki, read and file this, batch ingest, ingest all of these, ingest this url."
---

# wiki-ingest: Source Ingestion

Ingest is not a summary pass. It is a wiki compilation pass. The goal is to turn a source into wiki pages that answer future questions without repeatedly falling back to raw material.

**Syntax standard**: Write all Obsidian Markdown using proper Obsidian Flavored Markdown. Wikilinks as `[[Note Name]]`, callouts as `> [!type] Title`, embeds as `![[file]]`, properties as YAML frontmatter. If the kepano/obsidian-skills plugin is installed, prefer its canonical obsidian-markdown skill for Obsidian syntax reference. Otherwise, follow the guidance in this skill.

---

## Transport (v1.7+)

Before mutating any vault file, consult `.vault-meta/transport.json` (auto-created by `bash scripts/detect-transport.sh`). Use the `preferred` transport per the fallback chain:

- **cli** — `obsidian-cli write "$VAULT" "$NOTE" < content.md` (or `append`, `property:set`); see [`skills/wiki-cli/SKILL.md`](../wiki-cli/SKILL.md)
- **mcp-obsidian** / **mcpvault** — `mcp__obsidian-vault__write_note` and friends; see [`skills/wiki/references/mcp-setup.md`](../wiki/references/mcp-setup.md)
- **filesystem** — Claude's `Write`/`Edit` tools with absolute vault-rooted paths (final floor; always works)

Full decision tree: [`wiki/references/transport-fallback.md`](../../wiki/references/transport-fallback.md).

---

## Raw Source Conventions

Preferred raw-source layout:

- `.raw/documents/` — document extracts, normalized PDF or DOCX markdown, local HTML bundle markdown
- `.raw/images/` — screenshots, diagrams, scans, OCR-derived source notes
- `.raw/code-data/` — code snippets, config exports, structured data extracts
- `.raw/repos/` — git repositories used as source material

Legacy `.raw/*.md` files remain valid ingest inputs. Do not force a migration before reading them.

`wiki-ingest` is the single user-facing entry point. When the user says `ingest <path-or-url>`, do this:

1. Detect the source kind from the path, extension, or URL form.
2. If the source is outside `.raw/`, first copy, move, or clone it into the appropriate `.raw/...` location.
3. If the source is already ingest-ready Markdown, ingest it directly.
4. If the source is a complex local format, call the appropriate helper script internally.
5. Continue with the standard single-source ingest flow on the produced Markdown.

Default internal routing:

- `pdf`, `doc`, `docx`, `rtf`, `odt`, `txt`, `md` → `scripts/normalize-pdf.py`
- local `.html` file or `html + attachments` directory → `scripts/normalize-html-bundle.py`
- local git repository path or repository URL → `scripts/normalize-repo.py`
- image files → use the image / vision flow below
- direct `https://` documentation/article URL → use the URL flow below

Important classification rule:

- A plain local folder is **not** a repository source unless it is an actual git work tree.
- A local HTML file, or a folder whose primary purpose is to hold `html + attachments`, is a document source and should go to `.raw/documents/`.
- Do not classify a source as `repo` merely because the user passed a directory path.

Internal helpers for this vault:

- `python3 scripts/normalize-pdf.py .raw/documents/manual.pdf`
- `python3 scripts/normalize-pdf.py .raw/documents/guide.docx`
- `python3 scripts/normalize-html-bundle.py .raw/documents/help-site/`
- `python3 scripts/normalize-repo.py .raw/repos/internal-platform/`

Users should not need to run these helpers manually during ordinary use.

---

## Core Workflow

For every non-trivial ingest, follow this order:

1. **Intake** — land the source in the correct `.raw/...` folder.
2. **Normalize** — convert complex local formats into ingest-ready Markdown if needed.
3. **Read** — read the source fully enough to understand its real structure. Do not stop at the table of contents.
4. **Interrogate** — ask what future users will actually ask about this source.
5. **Compile** — create or update source, entity, concept, workflow, and domain pages that answer those questions.
6. **Cross-link** — update indexes, hot cache, overview, and log so the new knowledge is discoverable.
7. **Verify** — check whether common questions can now be answered from the wiki without repeatedly reopening raw sections.

---

## Hard Constraints

1. **Wiki-first goal**
   The goal of ingest is to reduce future query-time fallback to raw material. A successful ingest creates wiki pages that carry the answer, not just pages that describe the source.

2. **Self-interrogation required**
   Large manuals, user guides, platform docs, and process documents must not stop at overview pages. Use the checklist in [`references/self-interrogation-checklist.md`](./references/self-interrogation-checklist.md) and turn the answers into pages.

3. **Operational usefulness over overview**
   For procedural or product documentation, prefer pages that answer real questions such as "how do I do X?", "where is Y set?", "what does field Z mean?", and "what breaks if I skip this?" Use [`references/page-quality-rubric.md`](./references/page-quality-rubric.md).

4. **Section-grounded synthesis**
   When a source has meaningful internal sections, the key wiki pages should cite the specific section sources that support them, not just the top-level bundle or whole-manual page.

5. **Manual-first compilation mode**
   For software manuals, technical guides, and internal runbooks, apply the rules in [`references/manual-ingest-rubric.md`](./references/manual-ingest-rubric.md). Default to extracting workflows, settings, field meanings, prerequisites, outputs, and failure points.

---

## Mode Awareness (v1.8+)

Before creating any new wiki page, consult the vault's methodology mode via `python3 scripts/wiki-mode.py route <type> "<name>"`. The router returns the vault-relative path where the page should be filed.

```bash
SRC_PATH=$(python3 scripts/wiki-mode.py route source "Karpathy 2025 LLM Wiki essay")
# generic:      wiki/sources/Karpathy-2025-LLM-Wiki-essay.md
# lyt:          wiki/notes/Karpathy-2025-LLM-Wiki-essay.md  (also update relevant MOC)
# para:         wiki/resources/incoming/Karpathy-2025-LLM-Wiki-essay.md
# zettelkasten: wiki/20260517123456-Karpathy-2025-LLM-Wiki-essay.md

ENT_PATH=$(python3 scripts/wiki-mode.py route entity "Andrej Karpathy")
CON_PATH=$(python3 scripts/wiki-mode.py route concept "Compounding Vault Pattern")
WF_PATH=$(python3 scripts/wiki-mode.py route workflow "3D DCP Packaging")
```

If `.vault-meta/mode.json` is absent, the router returns mode=generic paths (identical to v1.7 behavior). No special-casing needed in this skill.

Mode-specific follow-up:
- **LYT**: after filing the atomic note, update the relevant MOC (`wiki/mocs/<topic>-moc.md`) to link the new note. If no MOC exists for the topic, create one using `skills/wiki-mode/templates/lyt/moc-template.md`.
- **Zettelkasten**: filename already includes the timestamp ID. Populate the `id:` frontmatter field to match.
- **PARA**: new ingests land in `wiki/resources/incoming/` by default. Do NOT auto-guess the topic; leave in incoming/ for user review.

## Concurrency (v1.7+)

**Multi-writer is safe in v1.7.** Every wiki page write MUST be preceded by `wiki-lock acquire <path>`.

```bash
if bash scripts/wiki-lock.sh acquire wiki/concepts/Foo.md; then
  # ... write via the selected transport ...
  bash scripts/wiki-lock.sh release wiki/concepts/Foo.md
else
  sleep 2
  bash scripts/wiki-lock.sh acquire wiki/concepts/Foo.md && {
    # write …
    bash scripts/wiki-lock.sh release wiki/concepts/Foo.md
  } || echo "skipped wiki/concepts/Foo.md (locked); logged to wiki/log.md"
fi
```

Properties:
- **Per-file granularity.** Locks key on `sha1(<vault-relative-path>)`; concurrent writes to different pages run in parallel.
- **Age-based staleness.** Default `STALE_AFTER_SEC=60`. A crashed holder unblocks in ≤60 seconds.
- **Cross-process release.** Release is `rm -f` by design.
- **Auto-commit guard.** PostToolUse defers `git add` if any locks are currently held.

Sub-agents may write pages, but must acquire locks first. See `agents/wiki-ingest.md`.

---

## Delta Tracking

Before ingesting any file, check `.raw/.manifest.json` to avoid re-processing unchanged sources.

```bash
[ -f .raw/.manifest.json ] && echo "exists" || echo "no manifest yet"
```

Before ingesting a file:

1. Compute a hash: `md5sum [file] | cut -d' ' -f1` (or `sha256sum` on Linux).
2. Check if the path exists in `.manifest.json` with the same hash.
3. If hash matches, skip. Report: "Already ingested (unchanged). Use `force` to re-ingest."
4. If missing or hash differs, proceed with ingest.

After ingesting a file:

1. Record `{hash, ingested_at, pages_created, pages_updated}` in `.manifest.json`.
2. Write the updated manifest back.

Skip delta checking if the user says "force ingest" or "re-ingest".

---

## URL Ingestion

Trigger: user passes a URL starting with `https://`.

1. Fetch the page using WebFetch.
2. Optionally clean with `defuddle` if available.
3. Save to `.raw/documents/[slug]-[YYYY-MM-DD].md`.
4. Proceed with the standard single-source ingest flow.

## Local Document Normalization

Trigger: local `pdf/doc/docx/rtf/odt/txt/md` material that is not yet an ingest-ready wiki source page.

1. If the file is outside `.raw/documents/`, copy it into `.raw/documents/`.
2. Normalize with `python3 scripts/normalize-pdf.py <source>`.
3. Save the normalized output under `.raw/documents/`.
4. Ingest the produced Markdown file.

## Local HTML Bundle Normalization

Trigger: a local HTML file or `html + attachments` directory.

1. If the source is outside `.raw/documents/`, copy or mirror it into `.raw/documents/`.
2. Run `python3 scripts/normalize-html-bundle.py <bundle-path>`.
3. Preserve the generated path hierarchy so later citations can trace back to the original page set.
4. Ingest the generated bundle entry page or the relevant section pages depending on scope.

## Repository Source Normalization

Trigger: a local git repository or repository URL.

1. If the source is remote, shallow-clone it into `.raw/repos/`.
2. If the source is local, first confirm it is a git work tree.
3. If the source is local and outside `.raw/repos/`, copy or mirror it into `.raw/repos/` when feasible.
4. Run `python3 scripts/normalize-repo.py <repo-path>`.
5. Ingest the produced repository snapshot page.

---

## Image / Vision Ingestion

Trigger: an image file path (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.avif`).

1. Read the image file using the Read tool.
2. Describe the image contents: OCR, key concepts, entities, diagrams, and data.
3. Save the description to `.raw/images/[slug]-[YYYY-MM-DD].md`.
4. Copy the image to `_attachments/images/[slug].[ext]` if needed.
5. Proceed with the standard single-source ingest flow on the saved description file.

Use cases: whiteboard photos, screenshots, diagrams, infographics, document scans.

---

## Single Source Ingest

Trigger: user drops a file into `.raw/` or pastes content.

1. **Read** the source completely. Do not skim.
2. **Discuss** emphasis with the user if needed. Skip this if the user says "just ingest it."
3. **Create** or update the source page in `wiki/sources/`. Use the source frontmatter schema from [`skills/wiki/references/frontmatter.md`](../wiki/references/frontmatter.md).
4. **Run self-interrogation** using [`references/self-interrogation-checklist.md`](./references/self-interrogation-checklist.md).
5. **Create or update** entity pages for people, orgs, products, teams, services, repos, and platforms that matter.
6. **Create or update** concept pages for stable terminology, mechanisms, rules, settings, field meanings, and abstractions.
7. **Create or update** workflow pages for repeatable procedural knowledge, operational sequences, troubleshooting steps, packaging flows, and high-frequency how-to tasks.
8. **Create or update** domain page(s) and `_index.md` files so the new knowledge is discoverable.
9. **Update** `wiki/overview.md` if the big picture changed.
10. **Update** `wiki/index.md`.
11. **Update** `wiki/hot.md`.
12. **Append** to `wiki/log.md` at the top:
    ```markdown
    ## [YYYY-MM-DD] ingest | Source Title
    - Source: `.raw/documents/filename.md`
    - Summary: [[Source Title]]
    - Pages created: [[Page 1]], [[Page 2]]
    - Pages updated: [[Page 3]], [[Page 4]]
    - Key insight: One sentence on what is new.
    ```
13. **Check for contradictions.** If new info conflicts with existing pages, add `> [!contradiction]` callouts on both pages.
14. **Verify done criteria** before treating the ingest as complete.

Do not stop at a domain page plus a few broad summaries if the source clearly supports more operational pages.

---

## Batch Ingest

Trigger: user drops multiple files or says "ingest all of these."

1. List all files to process. Confirm with the user before starting.
2. Process each source following the single-source ingest flow. Defer cross-referencing between sources until the end.
3. After all sources: do a cross-reference pass. Look for shared entities, overlapping workflows, contradictions, and concepts that now deserve dedicated pages.
4. Update index, hot cache, and log once at the end.
5. Report what was created, what was updated, and what still needs deeper compilation.

For 30+ sources, check in with the user after every 10.

---

## Done Criteria

An ingest is complete only if most of the following are true:

- Common questions about the source can be answered from the wiki without repeatedly reopening raw sections.
- The key workflow pages support real tasks, not just chapter overviews.
- The key concept pages contain field meanings, setting names, window names, constraints, or operational context when the source provides them.
- The important wiki pages cite the specific section sources that support them when the source was sectioned.
- The main user-facing navigation path now runs through wiki pages, not through raw normalized pages.

Treat the ingest as incomplete if the likely next query would still require broad raw searching for parameter names, window names, shortcuts, or configuration entry points.

---

## Context Window Discipline

Token budget matters. Follow these rules during ingest:

- Read `wiki/hot.md` first. If it contains the relevant context, don't re-read full pages.
- Read `wiki/index.md` to find existing pages before creating new ones.
- Read only 3-5 existing pages per ingest unless the source clearly spans multiple workflows or domains.
- Use PATCH for surgical edits.
- Keep wiki pages short. If a page grows beyond 300 lines, split it.
- Use search to find precise content without reading full files.

---

## Contradictions

> [!note] Custom callout dependency
> The `[!contradiction]` callout type used below is a custom callout defined in `.obsidian/snippets/vault-colors.css`. See [[skills/wiki/references/css-snippets.md]].

When new info contradicts an existing wiki page:

On the existing page, add:
```markdown
> [!contradiction] Conflict with [[New Source]]
> [[Existing Page]] claims X. [[New Source]] says Y.
> Needs resolution. Check dates, context, and primary sources.
```

On the new source summary, reference it:
```markdown
> [!contradiction] Contradicts [[Existing Page]]
> This source says Y, but existing wiki says X. See [[Existing Page]] for details.
```

Do not silently overwrite old claims.

---

## What Not to Do

- Do not modify source files under `.raw/` other than the maintained `.raw/.manifest.json`.
- Do not create duplicate pages. Always check the index and search before creating.
- Do not skip the log entry.
- Do not skip the hot cache update.
- Do not call an ingest complete merely because a few broad pages were created.

---

## Address Assignment (DragonScale Mechanism 2 MVP)

**Opt-in feature.** DragonScale address assignment runs only if `scripts/allocate-address.sh` is present and `.vault-meta/` exists. Otherwise, skip this section.

```bash
if [ -x ./scripts/allocate-address.sh ] && [ -d ./.vault-meta ]; then
  DRAGONSCALE_ADDRESSES=1
else
  DRAGONSCALE_ADDRESSES=0
fi
```

When enabled, every new non-meta wiki page gets a stable address in frontmatter:

```yaml
address: c-000042
```

Format: `c-<6-digit-counter>`.

Required helper:

```bash
ADDR=$(./scripts/allocate-address.sh)
```

Rules:

1. Call the helper before writing a new non-meta page.
2. Include `address: c-XXXXXX` in frontmatter.
3. Record the path-to-address mapping in `.raw/.manifest.json` under `address_map`.
4. Reuse an existing address if the page already has one or if `address_map` already knows it.

Exclusions:

- `_index.md`, `index.md`, `log.md`, `hot.md`, `overview.md`, `dashboard.md`, `getting-started.md`
- fold pages under `wiki/folds/`
- pre-rollout legacy pages (`created:` earlier than `2026-04-23`)

Concurrency policy:

- Single-writer only for address assignment.
- Sub-agents must not call the allocator.

---

## How to Think (10-Principle Mapping)

When working on this skill, apply the 10-principle loop. See [`skills/think/SKILL.md`](../think/SKILL.md) for the canonical framework.

| # | Principle | Application here |
|---|-----------|-------------------|
| 1 | OBSERVE (ext) | Read the source deeply enough to see structure, not just headings. |
| 2 | OBSERVE (int) | Watch for the temptation to stop at broad summaries because they are cheap to write. |
| 3 | LISTEN | What will future users actually ask about this source? |
| 4 | THINK | Which pages would prevent future raw fallback: entities, concepts, workflows, question seeds? |
| 5 | CONNECT (lat) | Link new pages to existing concepts, workflows, and domains. |
| 6 | CONNECT (sys) | `wiki-mode.py route` for paths + `wiki-lock.sh` for safety + index/log/hot for discoverability. |
| 7 | FEEL | Favor pages that are useful six months from now, not pages that merely sound complete today. |
| 8 | ACCEPT | If the wiki still cannot answer likely questions, the ingest is not finished. |
| 9 | CREATE | Write pages that carry answers forward: source, workflow, concept, domain, and sometimes question-level artifacts. |
| 10 | GROW | Every query that still falls back to raw should tighten the next ingest. |
