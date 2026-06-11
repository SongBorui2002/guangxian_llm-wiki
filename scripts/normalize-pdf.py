#!/usr/bin/env python3
"""Normalize document-like raw sources into ingestable Markdown.

Supports:
- .pdf      via pdftotext when available
- .doc/.docx/.rtf/.odt via textutil on macOS when available
- .txt/.md  as pass-through smoke-test / fallback inputs

The output is a Markdown file with frontmatter that can be ingested by
wiki-ingest as a normal `.raw/documents/*.md` source.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize PDF/DOC/DOCX-style sources into Markdown."
    )
    parser.add_argument("source", help="Source file path")
    parser.add_argument(
        "--output",
        help="Output markdown path. Default: source file with .md suffix beside the source.",
    )
    parser.add_argument(
        "--title",
        help="Optional title override. Default: source stem.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output file.",
    )
    return parser.parse_args()


def run_command(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"command failed: {' '.join(cmd)}")
    return proc.stdout


def extract_pdf(path: Path) -> tuple[str, str]:
    if shutil.which("pdftotext"):
        text = run_command(["pdftotext", "-layout", "-nopgbrk", str(path), "-"])
        return text, "pdftotext"
    return "", "unavailable"


def extract_with_textutil(path: Path) -> tuple[str, str]:
    if shutil.which("textutil"):
        text = run_command(["textutil", "-convert", "txt", "-stdout", str(path)])
        return text, "textutil"
    return "", "unavailable"


def extract_text(path: Path) -> tuple[str, str]:
    ext = path.suffix.lower()
    if ext in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="replace"), "read_text"
    if ext == ".pdf":
        return extract_pdf(path)
    if ext in {".doc", ".docx", ".rtf", ".odt"}:
        return extract_with_textutil(path)
    raise ValueError(f"unsupported extension: {ext}")


def default_output_path(source: Path) -> Path:
    return source.with_suffix(".md")


def frontmatter_value(value: str) -> str:
    return value.replace("\\", "/")


def build_markdown(source: Path, title: str, text: str, extractor: str) -> str:
    normalized_at = datetime.now().strftime("%Y-%m-%d")
    size_bytes = source.stat().st_size
    source_rel = frontmatter_value(str(source))
    lines = [
        "---",
        "type: source",
        f'title: "{title}"',
        "source_type: document",
        'author: ""',
        f"date_published: {normalized_at}",
        'url: ""',
        "confidence: medium",
        "key_claims:",
        '  - "Normalized document extract prepared for wiki ingest."',
        f'original_file: "{source_rel}"',
        f'normalized_by: "{extractor}"',
        f"normalized_at: {normalized_at}",
        f"source_size_bytes: {size_bytes}",
        f"created: {normalized_at}",
        f"updated: {normalized_at}",
        "tags:",
        "  - source",
        "  - document",
        "status: seed",
        "related: []",
        "sources: []",
        "---",
        "",
        f"# Source: {title}",
        "",
        "**Type**: Normalized document extract",
        f"**Date**: {normalized_at}",
        f"**Original file**: `{source_rel}`",
        f"**Extractor**: `{extractor}`",
        "",
        "## Summary",
        "",
        "Machine-normalized source prepared for ingest. This file preserves provenance and extracted text so the ingest step can synthesize concepts, entities, and workflows without editing the original document.",
        "",
        "## Key Claims",
        "",
        "- Pending ingest synthesis.",
        "",
        "## Notes",
        "",
        f"- Source size: `{size_bytes}` bytes",
        "- If extraction quality is poor, re-export to text or OCR before ingest.",
        "",
        "## Extracted Content",
        "",
    ]
    if text.strip():
        lines.append(text.strip())
    else:
        lines.extend(
            [
                "> [!gap] Extraction unavailable",
                "> Automatic text extraction did not succeed on this machine.",
                "> Ingest may require manual export to text or OCR before synthesis.",
            ]
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    if not source.is_file():
        print(f"ERR: source file not found: {source}", file=sys.stderr)
        return 2

    output = (
        Path(args.output).expanduser().resolve()
        if args.output
        else default_output_path(source)
    )
    if output.exists() and not args.force:
        print(f"ERR: output exists, pass --force to overwrite: {output}", file=sys.stderr)
        return 3

    try:
        text, extractor = extract_text(source)
    except Exception as exc:
        text = ""
        extractor = f"failed: {exc}"

    title = args.title or source.stem
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_markdown(source, title, text, extractor), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
