import re
import unittest
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))


def local_html_targets(source: str) -> set[str]:
    targets = set()
    targets.update(
        re.findall(r"""(?:href|src)=["']([^"']+\.html(?:[#?][^"']*)?)["']""", source)
    )
    targets.update(
        re.findall(
            r"""window\.location(?:\.href)?\s*=\s*["']([^"']+\.html(?:[#?][^"']*)?)["']""",
            source,
        )
    )
    return {
        target
        for target in targets
        if not urlparse(target).scheme and not target.startswith(("/", "#"))
    }


class StaticSiteLinksTest(unittest.TestCase):
    def test_local_html_targets_exist(self):
        self.assertTrue(HTML_FILES, "expected at least one HTML page")

        missing = []
        for html_file in HTML_FILES:
            for target in sorted(local_html_targets(html_file.read_text(encoding="utf-8"))):
                target_path = html_file.parent / target.split("#", 1)[0].split("?", 1)[0]
                if not target_path.exists():
                    missing.append(f"{html_file.name} -> {target}")

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
