#!/usr/bin/env python3
"""Validate local static-site links and assets.

This lightweight check intentionally avoids external network requests. It catches
same-directory HTML, image, and script targets that would otherwise deploy as
404s in this static site.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}

ATTRIBUTE_URL_RE = re.compile(
    r"""(?:href|src)\s*=\s*(?:"([^"]+)"|'([^']+)')""",
    re.IGNORECASE,
)
JS_LOCATION_RE = re.compile(
    r"""window\.location\.href\s*=\s*(?:"([^"]+)"|'([^']+)')""",
    re.IGNORECASE,
)


def iter_local_references(html_path: Path) -> list[tuple[str, str]]:
    html = html_path.read_text(encoding="utf-8-sig")
    refs: list[tuple[str, str]] = []

    for match in ATTRIBUTE_URL_RE.finditer(html):
        refs.append(("attribute", match.group(1) or match.group(2)))

    for match in JS_LOCATION_RE.finditer(html):
        refs.append(("window.location.href", match.group(1) or match.group(2)))

    local_refs: list[tuple[str, str]] = []
    for source, ref in refs:
        parsed = urlparse(ref)
        if parsed.scheme in EXTERNAL_SCHEMES or ref.startswith("#"):
            continue
        if parsed.netloc:
            continue
        local_refs.append((source, unquote(parsed.path)))

    return local_refs


def main() -> int:
    if not HTML_FILES:
        print("No top-level HTML files found", file=sys.stderr)
        return 1

    missing: list[str] = []
    for html_path in HTML_FILES:
        for source, ref in iter_local_references(html_path):
            if not ref:
                continue
            target = (html_path.parent / ref).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                missing.append(f"{html_path.name}: {source} escapes root: {ref}")
                continue
            if not target.exists():
                missing.append(f"{html_path.name}: {source} target missing: {ref}")

    if missing:
        print("Missing local static-site targets:", file=sys.stderr)
        for item in missing:
            print(f"- {item}", file=sys.stderr)
        return 1

    checked = ", ".join(path.name for path in HTML_FILES)
    print(f"All local static-site references resolve for: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
