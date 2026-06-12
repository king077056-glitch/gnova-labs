#!/usr/bin/env python3
"""Validate local links and assets in the static site."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
LOCATION_HREF_RE = re.compile(
    r"""window\.location\.href\s*=\s*['"]([^'"]+)['"]""",
    re.IGNORECASE,
)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value is None:
                continue
            if name.lower() in {"href", "src"}:
                self.references.append((name.lower(), value))


def is_local_reference(value: str) -> bool:
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return False
    return not value.startswith(("#", "mailto:", "tel:", "javascript:"))


def target_path(source: Path, value: str) -> Path:
    parsed = urlparse(value)
    raw_path = unquote(parsed.path)
    if raw_path.startswith("/"):
        return ROOT / raw_path.lstrip("/")
    return source.parent / raw_path


def collect_references(html_file: Path) -> list[tuple[str, str]]:
    parser = LinkParser()
    text = html_file.read_text(encoding="utf-8")
    parser.feed(text)

    references = list(parser.references)
    for match in LOCATION_HREF_RE.finditer(text):
        references.append(("window.location.href", match.group(1)))

    return references


def main() -> int:
    failures: list[str] = []
    html_files = sorted(
        path
        for path in ROOT.rglob("*.html")
        if ".git" not in path.relative_to(ROOT).parts
    )

    for html_file in html_files:
        for attr, value in collect_references(html_file):
            if not is_local_reference(value):
                continue
            target = target_path(html_file, value)
            if not target.exists():
                rel_source = html_file.relative_to(ROOT)
                failures.append(f"{rel_source}: missing {attr} target {value!r}")

    if failures:
        print("Broken static-site references:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print(f"Checked {len(html_files)} HTML file(s); all local references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
