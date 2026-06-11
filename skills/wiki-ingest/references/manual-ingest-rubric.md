# Manual Ingest Rubric

Use this rubric when the source is a software manual, user guide, platform guide, technical handbook, or internal runbook.

## Goal

Do not treat manuals like articles. Treat them like operational knowledge surfaces that future users will query for procedures, settings, field meanings, prerequisites, and failure cases.

## Default Extraction Priorities

Prioritize these knowledge shapes:

1. Installation, deployment, or environment setup
2. Configuration entry points, windows, menus, fields, and parameters
3. Standard operating procedures and packaging flows
4. Validation, QA, verification, or delivery steps
5. Troubleshooting paths, constraints, warnings, and failure modes
6. Terminology or domain concepts that recur across multiple sections

## Preferred Page Shapes

- `source` — one source page for the whole manual or bundle
- `workflow` — for repeatable task flows and operational sequences
- `concept` — for stable terms, settings, field meanings, system mechanics, and architectural ideas
- `entity` — for products, systems, platforms, teams, vendors, services, or repositories
- `question` or question seeds — for high-frequency user questions that should not require re-reading the manual

## Manual-Specific Rules

- A large manual should usually generate multiple workflow pages.
- A workflow page should map to a real task, not to a chapter title alone.
- If the manual was split into section sources, key pages should cite those sections directly.
- Prefer extracting answers to likely user questions over producing a single polished overview.

## Signals That More Compilation Is Needed

- The wiki can say what the product is, but not how to perform a task.
- The query path keeps going back to raw sections for field names, shortcuts, or window names.
- The domain page carries details that should really live in workflow or concept pages.
- The main source page is doing too much explanatory work by itself.
