#!/usr/bin/env python3
"""Validate local static-site links without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(REPO_ROOT.glob("*.html"))

ATTRIBUTE_TARGET_RE = re.compile(
    r"""\b(?:href|src|action)\s*=\s*(?P<quote>["'])(?P<target>.*?)(?P=quote)""",
    re.IGNORECASE,
)
JS_NAV_TARGET_RE = re.compile(
    r"""(?:window\.)?location(?:\.href|\.assign|\.replace)?\s*(?:=|\()\s*(?P<quote>["'])(?P<target>.*?)(?P=quote)""",
    re.IGNORECASE,
)
IGNORED_SCHEMES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "sms:",
    "data:",
    "javascript:",
)


def is_local_target(target: str) -> bool:
    stripped = target.strip()
    return bool(stripped) and not stripped.startswith("#") and not stripped.lower().startswith(IGNORED_SCHEMES)


def normalize_target(source: Path, target: str) -> Path:
    clean_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if clean_target.startswith("/"):
        return REPO_ROOT / clean_target.lstrip("/")
    return source.parent / clean_target


def collect_targets(source: Path) -> list[tuple[str, str]]:
    html = source.read_text(encoding="utf-8")
    targets: list[tuple[str, str]] = []
    for label, pattern in (("attribute", ATTRIBUTE_TARGET_RE), ("script", JS_NAV_TARGET_RE)):
        for match in pattern.finditer(html):
            target = match.group("target")
            if is_local_target(target):
                targets.append((label, target))
    return targets


def main() -> int:
    failures: list[str] = []

    for html_file in HTML_FILES:
        for label, target in collect_targets(html_file):
            path = normalize_target(html_file, target)
            if not path.exists():
                failures.append(f"{html_file.relative_to(REPO_ROOT)}: missing {label} target {target!r}")

    if failures:
        print("Broken local static-site targets found:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print(f"Checked {len(HTML_FILES)} HTML file(s); all local static targets exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
