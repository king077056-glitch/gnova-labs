from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
LOCAL_LINK_PATTERN = re.compile(
    r"""(?:href|src)=["']([^"']+)["']|location\.href\s*=\s*["']([^"']+)["']"""
)


def _local_targets(html: str):
    for attr_ref, js_ref in LOCAL_LINK_PATTERN.findall(html):
        target = attr_ref or js_ref
        if not target or target.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*://", target):
            continue
        yield target.split("#", 1)[0]


class StaticSiteLinkTests(unittest.TestCase):
    def test_local_html_references_exist(self):
        missing = []
        for html_file in ROOT.glob("*.html"):
            html = html_file.read_text(encoding="utf-8")
            for target in _local_targets(html):
                if not (html_file.parent / target).exists():
                    missing.append(f"{html_file.name} -> {target}")

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
