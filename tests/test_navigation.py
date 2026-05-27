from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "gnova_metal_console.html").read_text(encoding="utf-8")


class NavigationTests(unittest.TestCase):
    def test_sales_cta_uses_existing_in_page_category(self):
        self.assertNotIn('window.location.href="gnova_sales_suite.html"', HTML)
        self.assertIn(
            'document.getElementById("goSalesBtn").onclick=()=>{activeCategory="무료 프롬프트"',
            HTML,
        )

    def test_no_missing_local_html_targets(self):
        targets = set(re.findall(r"(?:href|src)=[\"']([^\"']+\.html)[\"']", HTML))
        targets.update(re.findall(r"window\.location\.href=[\"']([^\"']+\.html)[\"']", HTML))

        missing = sorted(target for target in targets if not (ROOT / target).exists())

        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
