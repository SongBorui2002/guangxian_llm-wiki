#!/usr/bin/env python3
"""Create an ingestable Markdown snapshot of a repository source."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


NOISE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".obsidian",
    ".cursor",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "out",
    "coverage",
    ".next",
    ".nuxt",
    ".cache",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
}

TEXT_PRIORITY = [
    "README.md",
    "README",
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "build.gradle",
    "Makefile",
    "Dockerfile",
    "docker-compose.yml",
]

BINARY_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".pdf",
    ".zip",
    ".gz",
    ".tar",
    ".tgz",
    ".jar",
    ".war",
    ".so",
    ".dylib",
    ".dll",
    ".exe",
    ".bin",
    ".mp4",
    ".mov",
    ".avi",
    ".mp3",
    ".wav",
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize a repository into a Markdown snapshot for ingest."
    )
    parser.add_argument(
        "repo",
        nargs="?",
        help="Path to a local repository. If omitted, --clone-url is required.",
    )
    parser.add_argument(
        "--clone-url",
        help="Optional git URL to shallow-clone before scanning.",
    )
    parser.add_argument(
        "--clone-dir",
        help="Destination directory for --clone-url. Default: .raw/repos/<repo-name>",
    )
    parser.add_argument(
        "--output",
        help="Output markdown path. Default: <repo>/__repo_index__.md",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=400,
        help="Maximum number of text files to enumerate in the snapshot.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output file.",
    )
    return parser.parse_args()


def shallow_clone(url: str, clone_dir: Path) -> Path:
    clone_dir.parent.mkdir(parents=True, exist_ok=True)
    if clone_dir.exists():
        return clone_dir
    subprocess.run(
        ["git", "clone", "--depth", "1", url, str(clone_dir)],
        check=True,
    )
    return clone_dir


def is_binary(path: Path) -> bool:
    if path.suffix.lower() in BINARY_SUFFIXES:
        return True
    try:
        with path.open("rb") as fh:
            chunk = fh.read(4096)
    except OSError:
        return True
    return b"\x00" in chunk


def should_skip(path: Path) -> bool:
    return path.name == "__repo_index__.md" or any(part in NOISE_DIRS for part in path.parts)


def is_git_repo(path: Path) -> bool:
    if (path / ".git").exists():
        return True
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return False
    return result.returncode == 0 and result.stdout.strip() == "true"


def collect_files(repo: Path, max_files: int) -> tuple[list[Path], list[Path]]:
    text_files: list[Path] = []
    skipped: list[Path] = []
    for path in sorted(repo.rglob("*")):
        if not path.is_file():
            continue
        if should_skip(path.relative_to(repo)):
            skipped.append(path)
            continue
        if is_binary(path):
            skipped.append(path)
            continue
        text_files.append(path)
        if len(text_files) >= max_files:
            break
    return text_files, skipped


def pick_priority_files(repo: Path, files: list[Path]) -> list[Path]:
    by_name = {path.name: path for path in files}
    chosen = [by_name[name] for name in TEXT_PRIORITY if name in by_name]
    if not chosen:
        chosen = files[:5]
    return chosen


def read_excerpt(path: Path, limit: int = 5000) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = text.strip()
    if len(text) > limit:
        return text[:limit].rstrip() + "\n\n[truncated]"
    return text


def build_markdown(repo: Path, files: list[Path], skipped: list[Path]) -> str:
    normalized_at = datetime.now().strftime("%Y-%m-%d")
    chosen = pick_priority_files(repo, files)
    top_dirs = sorted({path.relative_to(repo).parts[0] for path in files if len(path.relative_to(repo).parts) > 1})
    lines = [
        "---",
        "type: source",
        f'title: "{repo.name} Repository Snapshot"',
        "source_type: repository",
        'author: ""',
        f"date_published: {normalized_at}",
        'url: ""',
        "confidence: medium",
        "key_claims:",
        '  - "Repository snapshot prepared for wiki ingest."',
        f'original_file: "{repo.as_posix()}"',
        f"normalized_at: {normalized_at}",
        f"scanned_text_files: {len(files)}",
        f"skipped_files: {len(skipped)}",
        f"created: {normalized_at}",
        f"updated: {normalized_at}",
        "tags:",
        "  - source",
        "  - repository",
        "status: seed",
        "related: []",
        "sources: []",
        "---",
        "",
        f"# Source: {repo.name} Repository Snapshot",
        "",
        "**Type**: Repository source snapshot",
        f"**Date**: {normalized_at}",
        f"**Repository path**: `{repo.as_posix()}`",
        "",
        "## Summary",
        "",
        "Machine-generated repository source snapshot prepared for ingest. It captures the repo structure, the text-like files scanned, and a small set of key file excerpts so the wiki can synthesize concepts, entities, and workflows from code and documentation sources.",
        "",
        "## Key Claims",
        "",
        "- Pending ingest synthesis.",
        "",
        "## Notes",
        "",
        "- Scan mode: full tree walk over text-like files; noisy directories and binary-heavy files skipped",
        f"- Text files scanned: `{len(files)}`",
        f"- Files skipped: `{len(skipped)}`",
        "",
        "## Top-Level Overview",
        "",
    ]
    if top_dirs:
        for directory in top_dirs:
            lines.append(f"- `{directory}/`")
    else:
        lines.append("- _No subdirectories found._")
    lines.extend(["", "## Scanned Files", ""])
    for file_path in files:
        rel = file_path.relative_to(repo)
        lines.append(f"- `{rel.as_posix()}`")
    lines.extend(["", "## Key File Excerpts", ""])
    for file_path in chosen:
        rel = file_path.relative_to(repo)
        lines.extend(
            [
                f"### `{rel.as_posix()}`",
                "",
                "```text",
                read_excerpt(file_path),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def infer_clone_dir(url: str) -> Path:
    name = url.rstrip("/").rsplit("/", 1)[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return Path(".raw/repos") / name


def main() -> int:
    args = parse_args()
    repo_path: Path | None = None
    if args.clone_url:
        clone_dir = Path(args.clone_dir) if args.clone_dir else infer_clone_dir(args.clone_url)
        repo_path = shallow_clone(args.clone_url, clone_dir.expanduser().resolve())
    elif args.repo:
        repo_path = Path(args.repo).expanduser().resolve()
    else:
        raise SystemExit("ERR: provide either a repo path or --clone-url")

    if not repo_path.is_dir():
        raise SystemExit(f"ERR: repository directory not found: {repo_path}")
    if not args.clone_url and not is_git_repo(repo_path):
        raise SystemExit(
            "ERR: local path is not a git repository. "
            "Use normalize-html-bundle.py for HTML manuals or normalize-pdf.py for document-like files."
        )

    output = (
        Path(args.output).expanduser().resolve()
        if args.output
        else (repo_path / "__repo_index__.md")
    )
    if output.exists() and not args.force:
        raise SystemExit(f"ERR: output exists, pass --force to overwrite: {output}")

    files, skipped = collect_files(repo_path, args.max_files)
    output.write_text(build_markdown(repo_path, files, skipped), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
