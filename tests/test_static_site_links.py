#!/usr/bin/env python3
"""Validate local static-site links resolve to tracked files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL_HTML_REFERENCE = re.compile(
    r"""(?:href|src)=["']([^"']+)["']|window\.location\.href\s*=\s*["']([^"']+)["']"""
)


def referenced_path(raw_reference: str) -> Path | None:
    if (
        raw_reference.startswith(("http://", "https://", "mailto:", "tel:", "#"))
        or raw_reference == ""
    ):
        return None

    clean_reference = raw_reference.split("#", 1)[0].split("?", 1)[0]
    if not clean_reference or clean_reference.startswith("#"):
        return None

    return Path(clean_reference)


def main() -> int:
    missing: list[str] = []

    for html_file in sorted(ROOT.glob("*.html")):
        html = html_file.read_text(encoding="utf-8")
        for match in LOCAL_HTML_REFERENCE.finditer(html):
            raw_reference = next(group for group in match.groups() if group)
            relative_path = referenced_path(raw_reference)
            if relative_path is None:
                continue

            target = (html_file.parent / relative_path).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                missing.append(f"{html_file.name}: {raw_reference} escapes site root")
                continue

            if not target.exists():
                missing.append(f"{html_file.name}: {raw_reference}")

    if missing:
        print("Missing local static-site references:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("All local static-site references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
