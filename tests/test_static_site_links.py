from pathlib import Path
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))

ATTRIBUTE_LINK_RE = re.compile(r"""(?:href|src|action)=["']([^"']+)["']""", re.IGNORECASE)
SCRIPT_NAV_RE = re.compile(
    r"""(?:window\.)?(?:location\.href\s*=\s*|location\.assign\(|window\.open\()["']([^"']+)["']""",
    re.IGNORECASE,
)


def _is_local_target(target: str) -> bool:
    if not target or target.startswith(("#", "//")):
        return False

    parsed = urlsplit(target)
    if parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}:
        return False

    return True


def _resolve_local_target(source: Path, target: str) -> Path:
    parsed = urlsplit(target)
    path = parsed.path
    if path.startswith("/"):
        return ROOT / path.lstrip("/")
    return source.parent / path


def test_local_static_targets_exist():
    missing = []

    for html_file in HTML_FILES:
        html = html_file.read_text(encoding="utf-8")
        targets = ATTRIBUTE_LINK_RE.findall(html) + SCRIPT_NAV_RE.findall(html)

        for target in targets:
            if not _is_local_target(target):
                continue

            resolved = _resolve_local_target(html_file, target)
            if not resolved.exists():
                missing.append(f"{html_file.name} -> {target}")

    assert not missing, "Missing local static targets:\n" + "\n".join(missing)


if __name__ == "__main__":
    test_local_static_targets_exist()
