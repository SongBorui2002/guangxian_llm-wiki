#!/usr/bin/env python3
"""Normalize a local HTML page or HTML bundle into Markdown files.

Behavior:
- each HTML page becomes one Markdown file
- a bundle index page is generated
- large single-page manuals can also emit section pages
- relative path structure is preserved under the output directory
"""

from __future__ import annotations

import argparse
import html
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "section"


class HtmlExtractor(HTMLParser):
    BLOCK_TAGS = {
        "p",
        "div",
        "section",
        "article",
        "main",
        "header",
        "footer",
        "li",
        "ul",
        "ol",
        "br",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "table",
        "tr",
        "td",
        "th",
        "pre",
        "code",
    }
    HEADING_LEVELS = {
        "h1": 1,
        "h2": 2,
        "h3": 3,
        "h4": 4,
        "h5": 5,
        "h6": 6,
    }
    IGNORE_TAGS = {"script", "style", "noscript", "svg"}

    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_body = False
        self.ignore_depth = 0
        self.title = ""
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.images: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.current_heading_level: int | None = None
        self.current_heading_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "body":
            self.in_body = True
        if tag in self.IGNORE_TAGS:
            self.ignore_depth += 1
            return
        attr_map = dict(attrs)
        if tag == "title":
            self.in_title = True
        if not self.in_body and tag != "title":
            return
        if tag == "a" and attr_map.get("href"):
            href = urldefrag(attr_map["href"] or "")[0]
            if href:
                self.links.append(href)
        if tag == "img" and attr_map.get("src"):
            self.images.append(attr_map["src"] or "")
        if tag in self.HEADING_LEVELS:
            self.text_parts.append("\n\n")
            self.current_heading_level = self.HEADING_LEVELS[tag]
            self.current_heading_parts = []
        if tag in self.BLOCK_TAGS:
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.IGNORE_TAGS:
            self.ignore_depth = max(0, self.ignore_depth - 1)
            return
        if tag == "title":
            self.in_title = False
        if tag == "body":
            self.in_body = False
        if not self.in_body and tag != "body":
            return
        if tag in self.HEADING_LEVELS and self.current_heading_level is not None:
            heading = re.sub(r"\s+", " ", "".join(self.current_heading_parts)).strip()
            if heading:
                self.headings.append((self.current_heading_level, heading))
                self.text_parts.append(f'{"#" * self.current_heading_level} {heading}\n\n')
            self.current_heading_level = None
            self.current_heading_parts = []
        if tag in self.BLOCK_TAGS:
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.ignore_depth:
            return
        if self.in_title and not self.title.strip():
            self.title = data.strip()
        if not self.in_body:
            return
        text = data.strip()
        if text:
            if self.current_heading_level is not None:
                self.current_heading_parts.append(text)
            else:
                self.text_parts.append(text)

    def as_text(self) -> str:
        text = "".join(self.text_parts)
        text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" *\n *", "\n", text)
        return text.strip()


def split_large_page_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    sections: list[tuple[str, str]] = []
    current_title = "Overview"
    current_lines: list[str] = []

    for line in lines:
        if re.match(r"^##\s+", line):
            if current_lines:
                content = "\n".join(current_lines).strip()
                if content:
                    sections.append((current_title, content))
            current_title = re.sub(r"^##\s+", "", line).strip()
            current_lines = []
            continue
        current_lines.append(line)

    if current_lines:
        content = "\n".join(current_lines).strip()
        if content:
            sections.append((current_title, content))

    if len(sections) < 4:
        return []

    total_chars = sum(len(content) for _, content in sections)
    if total_chars < 15000:
        return []

    return sections


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize local HTML bundles into Markdown files."
    )
    parser.add_argument("source", help="Path to an HTML file or bundle directory")
    parser.add_argument(
        "--output-dir",
        help="Output directory. Default: <bundle>/_normalized or <file-stem>_normalized",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing markdown outputs.",
    )
    return parser.parse_args()


def find_html_files(source: Path) -> tuple[Path, list[Path]]:
    if source.is_file():
        if source.suffix.lower() not in {".html", ".htm"}:
            raise ValueError("source file must be .html or .htm")
        return source.parent, [source]
    if source.is_dir():
        html_files = sorted(
            p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in {".html", ".htm"}
        )
        if not html_files:
            raise ValueError("no HTML files found in directory")
        return source, html_files
    raise ValueError("source path does not exist")


def default_output_dir(source: Path) -> Path:
    if source.is_dir():
        return source / "_normalized"
    return source.parent / f"{source.stem}_normalized"


def md_target(output_dir: Path, root: Path, html_path: Path) -> Path:
    rel = html_path.relative_to(root)
    return (output_dir / rel).with_suffix(".md")


def build_page_markdown(
    root: Path,
    html_path: Path,
    extractor: HtmlExtractor,
    section_targets: list[Path] | None = None,
) -> str:
    normalized_at = datetime.now().strftime("%Y-%m-%d")
    title = extractor.title or html_path.stem
    rel_source = html_path.relative_to(root.parent if root.parent.exists() else root)
    extracted_text = extractor.as_text()
    word_count = len(extracted_text.split())
    section_count = len(extractor.headings)
    lines = [
        "---",
        "type: source",
        f'title: "{title}"',
        "source_type: html-bundle-page",
        'author: ""',
        f"date_published: {normalized_at}",
        'url: ""',
        "confidence: medium",
        "key_claims:",
        '  - "Normalized local HTML page prepared for wiki ingest."',
        f'original_file: "{rel_source.as_posix()}"',
        f"normalized_at: {normalized_at}",
        f"word_count: {word_count}",
        f"heading_count: {section_count}",
        f"created: {normalized_at}",
        f"updated: {normalized_at}",
        "tags:",
        "  - source",
        "  - html",
        "status: seed",
        "related: []",
        "sources: []",
        "---",
        "",
        f"# Source: {title}",
        "",
        "**Type**: Local HTML bundle page",
        f"**Date**: {normalized_at}",
        f"**Original file**: `{rel_source.as_posix()}`",
        "",
        "## Summary",
        "",
        "Machine-normalized HTML page prepared for ingest. Relative links and image references are preserved below so later wiki pages can trace back to the original local help bundle.",
        "",
        "## Key Claims",
        "",
        "- Pending ingest synthesis.",
        "",
        "## Notes",
        "",
        f"- Source HTML: `{html_path.as_posix()}`",
        f"- Extracted words: `{word_count}`",
        f"- Headings captured: `{section_count}`",
        f"- Referenced images: `{len(extractor.images)}`",
        f"- Referenced links: `{len(extractor.links)}`",
        "",
    ]
    if extractor.headings:
        lines.extend(["## Heading Outline", ""])
        for level, heading in extractor.headings:
            indent = "  " * max(0, level - 1)
            lines.append(f"{indent}- `{heading}`")
        lines.append("")
    if section_targets:
        lines.extend(["## Section Pages", ""])
        for target in section_targets:
            lines.append(f"- `{target.as_posix()}`")
        lines.append("")
    lines.extend(
        [
            "## Extracted Content",
            "",
            extracted_text or "_No extractable text found._",
            "",
        ]
    )
    if extractor.images:
        lines.extend(["## Referenced Images", ""])
        for image in extractor.images:
            lines.append(f"- `{image}`")
        lines.append("")
    if extractor.links:
        lines.extend(["## Referenced Links", ""])
        for link in extractor.links:
            lines.append(f"- `{link}`")
        lines.append("")
    return "\n".join(lines)


def build_section_markdown(
    root: Path,
    html_path: Path,
    page_title: str,
    section_title: str,
    section_content: str,
) -> str:
    normalized_at = datetime.now().strftime("%Y-%m-%d")
    rel_source = html_path.relative_to(root.parent if root.parent.exists() else root)
    lines = [
        "---",
        "type: source",
        f'title: "{page_title} - {section_title}"',
        "source_type: html-bundle-section",
        'author: ""',
        f"date_published: {normalized_at}",
        'url: ""',
        "confidence: medium",
        "key_claims:",
        '  - "Normalized section extracted from a local HTML page for wiki ingest."',
        f'original_file: "{rel_source.as_posix()}"',
        f"normalized_at: {normalized_at}",
        f"created: {normalized_at}",
        f"updated: {normalized_at}",
        "tags:",
        "  - source",
        "  - html",
        "  - section",
        "status: seed",
        "related: []",
        "sources: []",
        "---",
        "",
        f"# Source: {page_title} - {section_title}",
        "",
        "**Type**: Local HTML section",
        f"**Date**: {normalized_at}",
        f"**Original file**: `{rel_source.as_posix()}`",
        "",
        "## Summary",
        "",
        "Section-level extract from a larger local HTML help page. Use this when the full manual is too large to ingest in one pass and you need tighter provenance around one workflow or topic.",
        "",
        "## Key Claims",
        "",
        "- Pending ingest synthesis.",
        "",
        "## Extracted Content",
        "",
        section_content or "_No extractable text found._",
        "",
    ]
    return "\n".join(lines)


def build_index_markdown(source: Path, output_dir: Path, generated: list[Path]) -> str:
    normalized_at = datetime.now().strftime("%Y-%m-%d")
    lines = [
        "---",
        "type: source",
        f'title: "{source.stem} Bundle Index"',
        "source_type: html-bundle-index",
        'author: ""',
        f"date_published: {normalized_at}",
        'url: ""',
        "confidence: medium",
        "key_claims:",
        '  - "Normalized HTML bundle entry page prepared for ingest."',
        f'original_file: "{source.as_posix()}"',
        f"normalized_at: {normalized_at}",
        f"created: {normalized_at}",
        f"updated: {normalized_at}",
        "tags:",
        "  - source",
        "  - html",
        "status: seed",
        "related: []",
        "sources: []",
        "---",
        "",
        f"# Source: {source.stem} Bundle Index",
        "",
        "**Type**: Local HTML bundle index",
        f"**Date**: {normalized_at}",
        f"**Original bundle**: `{source.as_posix()}`",
        "",
        "## Summary",
        "",
        "Bundle entry page for a local HTML help set. Each source page below was normalized separately so ingest can preserve page-level provenance and path traceability.",
        "",
        "## Key Claims",
        "",
        "- Pending ingest synthesis.",
        "",
        "## Pages Created",
        "",
    ]
    for page in generated:
        rel = page.relative_to(output_dir)
        lines.append(f"- `{rel.as_posix()}`")
    lines.extend(["", "## Notes", "", "- Ingest this index page when you want bundle-level context.", "- Ingest individual page files when you want narrower provenance.", ""])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    root, html_files = find_html_files(source)
    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else default_output_dir(source)
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    generated: list[Path] = []
    for html_file in html_files:
        target = md_target(output_dir, root, html_file)
        if target.exists() and not args.force:
            raise SystemExit(f"ERR: output exists, pass --force to overwrite: {target}")
        parser = HtmlExtractor()
        parser.feed(html.unescape(html_file.read_text(encoding="utf-8", errors="replace")))
        extracted_text = parser.as_text()
        sections = split_large_page_sections(extracted_text)
        section_targets: list[Path] = []
        if sections:
            section_dir = target.parent / f"{target.stem}__sections"
            section_dir.mkdir(parents=True, exist_ok=True)
            for idx, (section_title, section_content) in enumerate(sections, start=1):
                section_target = section_dir / f"{idx:02d}-{slugify(section_title)}.md"
                if section_target.exists() and not args.force:
                    raise SystemExit(
                        f"ERR: output exists, pass --force to overwrite: {section_target}"
                    )
                section_target.write_text(
                    build_section_markdown(
                        root=root,
                        html_path=html_file,
                        page_title=parser.title or html_file.stem,
                        section_title=section_title,
                        section_content=section_content,
                    ),
                    encoding="utf-8",
                )
                generated.append(section_target)
                section_targets.append(section_target.relative_to(output_dir))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            build_page_markdown(root, html_file, parser, section_targets=section_targets),
            encoding="utf-8",
        )
        generated.append(target)

    index_path = output_dir / "index.md"
    index_path.write_text(build_index_markdown(source, output_dir, generated), encoding="utf-8")
    print(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
