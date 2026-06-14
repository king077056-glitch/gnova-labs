from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re


ROOT = Path(__file__).resolve().parents[1]
JS_LOCATION_RE = re.compile(
    r"""(?:window\.)?location\.href\s*=\s*["']([^"']+)["']"""
)


class LocalReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.references.append(value)


def is_local_reference(reference):
    if reference.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return False

    parsed = urlparse(reference)
    return not parsed.scheme and not parsed.netloc


def target_path(source_file, reference):
    parsed = urlparse(reference)
    clean_path = parsed.path
    if not clean_path:
        return None
    return (source_file.parent / clean_path).resolve()


def collect_references(html_file):
    contents = html_file.read_text(encoding="utf-8-sig")
    parser = LocalReferenceParser()
    parser.feed(contents)
    parser.references.extend(JS_LOCATION_RE.findall(contents))
    return parser.references


def test_local_static_references_exist():
    missing = []

    for html_file in ROOT.glob("*.html"):
        for reference in collect_references(html_file):
            if not is_local_reference(reference):
                continue

            resolved = target_path(html_file, reference)
            if resolved is not None and not resolved.exists():
                missing.append(
                    f"{html_file.relative_to(ROOT)} references missing {reference}"
                )

    assert missing == []
