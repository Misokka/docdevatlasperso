import json
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_generated_docs():
    source = (ROOT / "public/assets/docs-data.js").read_text(encoding="utf-8")
    match = re.match(r"window\.DOCS=(.*);\nwindow\.DOC_GROUPS=", source, re.DOTALL)
    if not match:
        raise AssertionError("Le format de docs-data.js est inattendu")
    return json.loads(match.group(1))


class DevAtlasBuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, "scripts/build.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.docs = load_generated_docs()

    def test_generated_site_contains_all_existing_pages_and_native_mvc_page(self):
        self.assertEqual(51, len(self.docs))
        mvc = next(
            (doc for doc in self.docs if doc["slug"] == "php/mvc-php-natif"),
            None,
        )
        self.assertIsNotNone(mvc)
        self.assertEqual("PHP", mvc["group"])

    def test_native_mvc_page_is_searchable_by_requested_keywords(self):
        mvc = next(doc for doc in self.docs if doc["slug"] == "php/mvc-php-natif")
        searchable = " ".join(
            [mvc["title"], mvc["summary"], " ".join(mvc["tags"]), mvc["text"]]
        ).lower()
        for keyword in (
            "mvc",
            "php natif",
            "routeur",
            "pdo",
            "controller",
            "model",
            "view",
            "front controller",
        ):
            with self.subTest(keyword=keyword):
                self.assertIn(keyword, searchable)

    def test_static_navigation_targets_existing_documents(self):
        slugs = {doc["slug"] for doc in self.docs}
        app = (ROOT / "public/assets/app.js").read_text(encoding="utf-8")
        references = set(re.findall(r"href\('([^']+)'\)", app))

        highlighted = re.search(r"const highlighted=\[(.*?)\]", app)
        self.assertIsNotNone(highlighted)
        references.update(re.findall(r"'([^']+)'", highlighted.group(1)))

        suggested = re.search(
            r"if\(!terms\.length\)return docs\.filter\(d=>\[(.*?)\]\.includes",
            app,
        )
        self.assertIsNotNone(suggested)
        references.update(re.findall(r"'([^']+)'", suggested.group(1)))

        self.assertEqual(set(), references - slugs)

    def test_native_mvc_code_blocks_have_copy_controls_and_toc_sections(self):
        mvc = next(doc for doc in self.docs if doc["slug"] == "php/mvc-php-natif")
        self.assertGreaterEqual(len(mvc["sections"]), 12)
        self.assertGreaterEqual(mvc["html"].count('class="code-block"'), 12)
        self.assertEqual(
            mvc["html"].count('class="code-block"'),
            mvc["html"].count('class="copy-code"'),
        )

    def test_published_copy_has_no_interview_positioning(self):
        visible_sources = [
            ROOT / "README.md",
            ROOT / "public/index.html",
            ROOT / "public/assets/app.js",
            ROOT / "public/assets/docs-data.js",
        ]
        corpus = "\n".join(path.read_text(encoding="utf-8") for path in visible_sources)
        banned = re.compile(
            r"entretien|recruteur|examinateur|embauche|checklist-demain|"
            r"questions du cv|juste avant.*(?:test|épreuve)",
            re.IGNORECASE,
        )
        self.assertIsNone(banned.search(corpus))

    def test_vercel_still_serves_the_public_directory(self):
        config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
        self.assertEqual("public", config["outputDirectory"])
        self.assertIsNone(config["buildCommand"])


if __name__ == "__main__":
    unittest.main()
