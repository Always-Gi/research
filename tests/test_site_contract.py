import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class SiteContentContractTests(unittest.TestCase):
    def test_single_page_site_has_no_global_navigation_items(self):
        navigation = read("_data/navigation.yml")
        titles = re.findall(r'^\s*- title:\s*["\']([^"\']+)["\']', navigation, re.M)
        self.assertEqual(titles, [])

    def test_home_has_identity_and_only_the_approved_sections(self):
        home = read("_pages/about.md")
        self.assertIn("Research Interests", home)
        self.assertIn("Publications", home)
        self.assertNotIn("Academic Pages is a ready-to-fork", home)
        self.assertIn("profile.png", home)
        self.assertRegex(home, r'alt="(?!profile(?: image)?")[^"]{8,}"')
        self.assertIn("undergraduate student", home.lower())
        self.assertIn("Yonsei University", home)
        self.assertIn("dabicho33@gmail.com", home)
        self.assertIn("github.com/Always-Gi", home)
        self.assertIn("linkedin.com/in/hanggi-cho-268119409", home)
        self.assertIn("'/output/pdf/hanggi-cho-cv.pdf' | relative_url", home)
        self.assertIn("Does a Larger Sample Size Always Lead to Shorter Confidence Intervals?", home)

    def test_research_interests_preserve_the_existing_four_labels(self):
        home = read("_pages/about.md")
        for interest in (
            "Operations Research",
            "Optimization",
            "Applied Probability",
            "Quantitative Finance",
        ):
            self.assertIn(interest, home)
        self.assertNotIn("Statistics and Statistical Inference", home)

    def test_publications_lists_the_verified_manuscript(self):
        publications = read("_pages/about.md")
        self.assertIn(
            "Does a Larger Sample Size Always Lead to Shorter Confidence Intervals?",
            publications,
        )
        self.assertIn(
            "Jinwoong Park and <strong>Hanggi Cho*</strong>", publications
        )
        self.assertIn("Statistics &amp; Probability Letters", publications)
        self.assertIn("under review", publications.lower())
        self.assertIn("Corresponding author", publications)
        self.assertIn("'/files/cho-confidence-interval-manuscript.pdf' | relative_url", publications)

    def test_cv_link_opens_a_versioned_pdf_directly(self):
        home = read("_pages/about.md")
        self.assertIn("'/output/pdf/hanggi-cho-cv.pdf' | relative_url", home)
        self.assertFalse((ROOT / "_pages/cv.md").exists())
        self.assertFalse((ROOT / "_pages/cv-json.md").exists())

        cv = ROOT / "output/pdf/hanggi-cho-cv.pdf"
        self.assertTrue(cv.exists())
        self.assertEqual(cv.read_bytes()[:4], b"%PDF")

    def test_public_name_spelling_is_consistently_hanggi(self):
        public_sources = "\n".join(
            read(path)
            for path in (
                "_config.yml",
                "_pages/about.md",
                "_includes/footer.html",
            )
        )
        self.assertNotIn("HangGi Cho", public_sources)
        self.assertIn("Hanggi Cho", public_sources)

    def test_repository_paths_remain_github_pages_safe(self):
        config = read("_config.yml")
        self.assertRegex(config, r'(?m)^baseurl\s*:\s*["\']/research["\']')
        self.assertRegex(config, r'(?m)^repository\s*:\s*["\']Always-Gi/research["\']')
        self.assertNotIn('href="/images/favicon.ico"', read("_includes/head/custom.html"))

    def test_visible_pages_do_not_contain_template_demo_people(self):
        visible = "\n".join(
            read(path)
            for path in ("_pages/about.md",)
        )
        for fake in ("GitHub University", "Professor Hub", "Professor Git"):
            self.assertNotIn(fake, visible)

    def test_demo_collection_entries_are_removed(self):
        for directory in ("_publications", "_talks", "_teaching", "_portfolio", "_posts"):
            entries = [path for path in (ROOT / directory).glob("*") if path.is_file()]
            self.assertEqual(entries, [], f"demo entries remain in {directory}: {entries}")

    def test_versioned_manuscript_is_a_pdf(self):
        manuscript = ROOT / "files/cho-confidence-interval-manuscript.pdf"
        self.assertTrue(manuscript.exists())
        self.assertEqual(manuscript.read_bytes()[:4], b"%PDF")


class AcademicLayoutContractTests(unittest.TestCase):
    def test_visible_pages_share_the_academic_layout(self):
        for path in ("_pages/about.md",):
            self.assertRegex(read(path), r"(?m)^layout:\s*academic\s*$")

    def test_home_hides_the_template_masthead(self):
        self.assertRegex(read("_pages/about.md"), r"(?m)^hide_masthead:\s*true\s*$")
        self.assertIn("page.hide_masthead", read("_layouts/default.html"))

    def test_layout_and_masthead_supply_semantic_landmarks(self):
        layout = read("_layouts/academic.html")
        masthead = read("_includes/masthead.html")
        self.assertIn('<main class="academic-main"', layout)
        self.assertIn("{{ content }}", layout)
        self.assertIn("<nav", masthead)

    def test_academic_styles_are_loaded_last(self):
        imports = read("assets/css/main.scss")
        self.assertRegex(imports, r'"layout/academic"\s*;\s*$')

    def test_main_stylesheet_is_cache_busted_per_deployment(self):
        head = read("_includes/head.html")
        self.assertIn("site.github.build_revision", head)
        self.assertRegex(head, r"main\.css\?v=\{\{\s*asset_version\s*\}\}")

    def test_academic_styles_cover_accessible_responsive_layout(self):
        styles = read("_sass/layout/_academic.scss")
        self.assertIn(".simple-profile", styles)
        self.assertIn(".simple-portrait", styles)
        self.assertIn(".simple-section", styles)
        self.assertIn(".simple-publication", styles)
        self.assertIn(":focus-visible", styles)
        self.assertRegex(styles, r"@media\s*(?:screen\s*and\s*)?\(max-width:\s*700px\)")
        self.assertNotIn("gradient(", styles)

    def test_masthead_does_not_expose_a_theme_toggle(self):
        self.assertNotIn("theme-toggle", read("_includes/masthead.html"))

    def test_footer_is_concise_and_personal(self):
        footer = read("_includes/footer.html")
        self.assertIn("Hanggi Cho", footer)
        self.assertIn("Yonsei University", footer)
        self.assertNotIn("Powered by", footer)
        self.assertNotIn("sitemap", footer.lower())


@unittest.skipUnless((ROOT / "_site").is_dir(), "generated site has not been built")
class GeneratedSiteContractTests(unittest.TestCase):
    def test_expected_public_files_are_generated(self):
        expected = (
            "_site/index.html",
            "_site/profile.png",
            "_site/files/cho-confidence-interval-manuscript.pdf",
            "_site/output/pdf/hanggi-cho-cv.pdf",
        )
        for path in expected:
            self.assertTrue((ROOT / path).is_file(), f"missing generated file: {path}")

    def test_generated_pages_use_repository_safe_internal_urls(self):
        for path in (
            "_site/index.html",
        ):
            html = read(path)
            self.assertRegex(html, r'href="(?:https?://[^"/]+)?/research/"')
            self.assertRegex(
                html,
                r'href="(?:https?://[^"/]+)?/research/output/pdf/hanggi-cho-cv\.pdf"',
            )
        self.assertIn('src="/research/profile.png"', read("_site/index.html"))
        self.assertIn('href="/research/images/favicon.ico"', read("_site/index.html"))
        self.assertIn(
            'href="/research/files/cho-confidence-interval-manuscript.pdf"',
            read("_site/index.html"),
        )

    def test_generated_visible_pages_have_no_demo_identity(self):
        generated = "\n".join(
            read(path)
            for path in (
                "_site/index.html",
            )
        )
        for fake in (
            "GitHub University",
            "Professor Hub",
            "Professor Git",
            "Academic Pages is a ready-to-fork",
        ):
            self.assertNotIn(fake, generated)


if __name__ == "__main__":
    unittest.main()
