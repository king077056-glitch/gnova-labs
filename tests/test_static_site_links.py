#!/usr/bin/env python3
"""Validate local static-site references.

The site is deployed as loose HTML files, so a missing local target becomes a
production 404. This check intentionally avoids external URLs and only verifies
files that should exist in the repository.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))

HTML_ATTRS = {"href", "src", "poster"}
JS_LOCATION_RE = re.compile(
    r"(?:window\.)?location(?:\.href)?\s*=\s*['\"]([^'\"]+)['\"]|"
    r"(?:window\.)?location\.(?:assign|replace)\(\s*['\"]([^'\"]+)['\"]\s*\)"
)


class LocalReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []
        self._in_script = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "script":
            self._in_script = True

        for name, value in attrs:
            if value and name.lower() in HTML_ATTRS:
                self.references.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script":
            self._in_script = False

    def handle_data(self, data: str) -> None:
        if not self._in_script:
            return

        for match in JS_LOCATION_RE.finditer(data):
            target = next(group for group in match.groups() if group)
            self.references.append(target)


def is_local_file_reference(reference: str) -> bool:
    parsed = urlparse(reference)
    if parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}:
        return False
    if parsed.netloc or parsed.path in {"", "/"}:
        return False
    return not parsed.path.startswith("/")


def resolve_reference(source: Path, reference: str) -> Path:
    parsed = urlparse(reference)
    path = unquote(parsed.path)
    return (source.parent / path).resolve()


def main() -> int:
    missing: list[str] = []

    for html_file in HTML_FILES:
        parser = LocalReferenceParser()
        parser.feed(html_file.read_text(encoding="utf-8-sig"))

        for reference in parser.references:
            if not is_local_file_reference(reference):
                continue

            target = resolve_reference(html_file, reference)
            if not target.exists():
                missing.append(f"{html_file.name} -> {reference}")

    if missing:
        print("Missing local static-site targets:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Checked {len(HTML_FILES)} HTML file(s); all local references exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
