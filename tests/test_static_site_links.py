#!/usr/bin/env python3
"""Validate local static references in shipped HTML files."""

from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.references.append((name, value))


SCRIPT_NAVIGATION_RE = re.compile(
    r"""(?:window\.)?location(?:\.href)?\s*=\s*["']([^"']+)["']"""
)


def is_local_file_reference(value: str) -> bool:
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return False

    lowered = value.lower()
    if lowered.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return False

    return bool(parsed.path)


class StaticSiteLinkTests(unittest.TestCase):
    def test_html_files_exist(self) -> None:
        self.assertTrue(HTML_FILES, "Expected at least one top-level HTML file")

    def test_local_static_references_exist(self) -> None:
        missing: list[str] = []

        for html_file in HTML_FILES:
            parser = ReferenceParser()
            text = html_file.read_text(encoding="utf-8")
            parser.feed(text)

            references = [value for _, value in parser.references]
            references.extend(SCRIPT_NAVIGATION_RE.findall(text))

            for reference in references:
                if not is_local_file_reference(reference):
                    continue

                target = (html_file.parent / urlsplit(reference).path).resolve()
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    missing.append(f"{html_file.name}: {reference} escapes repository")
                    continue

                if not target.exists():
                    missing.append(f"{html_file.name}: {reference}")

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
