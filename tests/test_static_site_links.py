#!/usr/bin/env python3
"""Validate local static-site references that would otherwise become 404s."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urldefrag, urlparse


ROOT = Path(__file__).resolve().parents[1]


class LocalReferenceParser(HTMLParser):
    ATTRS = {
        "a": ("href",),
        "link": ("href",),
        "script": ("src",),
        "img": ("src",),
        "source": ("src", "srcset"),
        "iframe": ("src",),
    }

    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        wanted = self.ATTRS.get(tag, ())
        for name, value in attrs:
            if name in wanted and value:
                self.references.append(value)


def is_local_reference(value):
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or value.startswith(("mailto:", "tel:", "data:", "#")):
        return False
    return True


def normalize_path(value):
    value, _fragment = urldefrag(value)
    parsed = urlparse(value)
    return parsed.path


def references_for(html_path):
    text = html_path.read_text(encoding="utf-8")
    parser = LocalReferenceParser()
    parser.feed(text)
    script_targets = re.findall(r"(?:window\.)?location\.href\s*=\s*['\"]([^'\"]+)['\"]", text)
    return parser.references + script_targets


def main():
    missing = []
    for html_path in ROOT.glob("*.html"):
        for raw_ref in references_for(html_path):
            if not is_local_reference(raw_ref):
                continue

            ref_path = normalize_path(raw_ref)
            if not ref_path or ref_path.startswith("/"):
                continue

            target = (html_path.parent / ref_path).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                missing.append((html_path.name, raw_ref, "escapes repository root"))
                continue

            if not target.exists():
                missing.append((html_path.name, raw_ref, "missing target"))

    if missing:
        for source, ref, reason in missing:
            print(f"{source}: {ref} -> {reason}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
