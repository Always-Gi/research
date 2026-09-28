# Academic Homepage Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Academic Pages demo content with a restrained three-page academic website for HangGi Cho.

**Architecture:** Keep the existing Jekyll and GitHub Pages foundation, but introduce one focused `academic` layout and scoped SCSS for all visible pages. Store verified content in the existing `_pages` files, keep site-wide identity in `_config.yml`, and make the manuscript a versioned file under `files/`.

**Tech Stack:** Jekyll, Liquid, Markdown/HTML, SCSS, Python 3 standard-library tests

**Spec:** `docs/superpowers/specs/2026-09-28-academic-homepage-redesign.md`

## Global Constraints

- Navigation contains exactly `Home`, `Publications`, and `CV`.
- Home contains exactly the substantive sections `About` and `Research Interests` below the identity header.
- Preserve `baseurl: "/research"` and `repository: "Always-Gi/research"`.
- Preserve the existing portrait and the existing public repository contact email.
- List the manuscript with its real author order and the status `Under review at Statistics & Probability Letters`.
- Do not invent dates, GPA, awards, employment, teaching, service, or technical skills.
- Do not publish an individual contribution claim without coauthor-approved wording.
- Preserve the four existing research interests exactly: `Operations Research`, `Optimization`, `Applied Probability`, and `Quantitative Finance`.
- Keep the confidence-interval manuscript on Publications; do not add statistics as a separate research-interest label.
- Remove visible Academic Pages sample content and sample navigation.

## Review Focus

- Repository-project paths: every internal link and image must work under `/research`, not only at the domain root.
- Mobile layout: the identity block and three navigation items must fit without horizontal scrolling at 375 CSS pixels.
- Publication integrity: title, author order, corresponding-author marker, journal status, and PDF path must match the supplied manuscript and confirmed status.
- Sample cleanup: no visible page may contain `GitHub University`, template guide copy, fake publications, fake talks, fake teaching, or fake portfolio entries.
- Build output: Jekyll must generate `/`, `/publications/`, `/cv/`, the portrait, and the manuscript PDF without Liquid or Sass errors.

---

### Task 1: Replace Demo Content with Verified Academic Content

**Files:**
- Create: `tests/test_site_contract.py`
- Modify: `_config.yml`
- Modify: `_data/navigation.yml`
- Modify: `_pages/about.md`
- Modify: `_pages/publications.html`
- Modify: `_pages/cv.md`
- Copy: `/Users/hanggi-cho/Downloads/manuscript.pdf` to `files/cho-confidence-interval-manuscript.pdf`
- Delete: demo entries under `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`, and `_posts/`

**Interfaces:**
- Consumes: confirmed profile details from `_config.yml`, the supplied manuscript, and the approved design spec.
- Produces: Jekyll pages with permalinks `/`, `/publications/`, and `/cv/`; manuscript asset `/files/cho-confidence-interval-manuscript.pdf`.

- [ ] **Step 1: Write contract tests for verified content and absent demo content**

Create `tests/test_site_contract.py` with `unittest.TestCase` tests that assert:

- navigation titles equal `Home`, `Publications`, `CV` in that order;
- Home contains `About` and `Research Interests`, and does not contain the Academic Pages template introduction;
- Home identity content includes `profile.png`, meaningful portrait alt text, `Undergraduate Student`, `Yonsei University`, the existing public email, GitHub, LinkedIn, and CV links;
- Publications contains the exact manuscript title, `Jinwoong Park`, `Hanggi Cho`, `Statistics & Probability Letters`, `Under review`, and the versioned PDF path;
- CV contains `Yonsei University`, `Mathematics`, `Applied Statistics`, and the manuscript title;
- `_config.yml` retains `/research` and `Always-Gi/research`;
- none of the visible page sources contain `GitHub University`, `Professor Hub`, or `Professor Git`;
- the manuscript file exists and starts with the PDF magic bytes `%PDF`.

- [ ] **Step 2: Run the contract tests and verify RED**

Run: `python3 -m unittest tests/test_site_contract.py -v`

Expected: failures for the current seven-item navigation, template Home copy, fictional CV, and absent versioned manuscript.

- [ ] **Step 3: Replace configuration, navigation, and page content**

Set the site title to `HangGi Cho`, retain the approved description and repository paths, and replace the multi-line sidebar biography with the confirmed undergraduate identity. Replace navigation with the exact three items. Rewrite Home, Publications, and CV with only the approved sections and verified facts; use `{{ '/path/' | relative_url }}` for internal links and assets.

- [ ] **Step 4: Add the manuscript and remove demo content**

Copy the supplied PDF to the exact versioned path. Remove only the demo Markdown/HTML entries in the five sample content collections; retain their directories and Jekyll collection support for future real entries.

- [ ] **Step 5: Run the contract tests and verify GREEN**

Run: `python3 -m unittest tests/test_site_contract.py -v`

Expected: all content-contract tests pass.

- [ ] **Step 6: Commit the content migration**

Run:

```bash
git add _config.yml _data/navigation.yml _pages/about.md _pages/publications.html _pages/cv.md files/cho-confidence-interval-manuscript.pdf tests/test_site_contract.py _publications _talks _teaching _portfolio _posts
git commit -m "content: replace academic pages demo content"
```

### Task 2: Implement the Professor-Style Academic Layout

**Files:**
- Create: `_layouts/academic.html`
- Create: `_sass/layout/_academic.scss`
- Modify: `assets/css/main.scss`
- Modify: `_includes/masthead.html`
- Modify: `_includes/footer.html`
- Modify: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: page front matter and content produced by Task 1, plus existing `head.html`, `base_path`, and Jekyll `relative_url` support.
- Produces: `.academic-main`, `.academic-hero`, `.academic-section`, `.publication-entry`, and `.academic-cv` rendering contracts shared by all three pages.

- [ ] **Step 1: Extend the contract tests for layout and responsive styling**

Add tests asserting:

- all three pages use `layout: academic`;
- `academic.html` uses semantic navigation/main landmarks, renders `{{ content }}`, and preserves heading order;
- `main.scss` imports `layout/academic` after the base theme imports;
- `_academic.scss` contains an explicit `@media (max-width: 700px)` rule, visible `:focus-visible` styles, portrait styling, navigation styling, and no gradient background declaration;
- masthead has no theme-toggle control;
- footer does not render the template's `Powered by` or sitemap text.

- [ ] **Step 2: Run the layout tests and verify RED**

Run: `python3 -m unittest tests/test_site_contract.py -v`

Expected: failures because the academic layout and scoped stylesheet do not exist.

- [ ] **Step 3: Create the academic layout and scoped SCSS**

Create a layout that extends `default`, wraps content in a centered semantic main region, and exposes the class contracts above. Style the top navigation, identity header, portrait, readable content column, publication metadata, CV lists, normal-flow footer, focus states, and mobile stacking. Use charcoal text, a warm-white background, a muted blue accent, serif headings, sans-serif body text, thin rules, and generous whitespace.

- [ ] **Step 4: Simplify masthead and footer, then import the stylesheet**

Remove the theme-toggle list item from the masthead while preserving the greedy mobile navigation. Replace the template footer with a concise copyright and Yonsei University affiliation. Import `layout/academic` last in `assets/css/main.scss` so the scoped design wins without rewriting vendor theme files.

- [ ] **Step 5: Run the contract tests and verify GREEN**

Run: `python3 -m unittest tests/test_site_contract.py -v`

Expected: all content and layout contract tests pass.

- [ ] **Step 6: Commit the academic layout**

Run:

```bash
git add _layouts/academic.html _sass/layout/_academic.scss assets/css/main.scss _includes/masthead.html _includes/footer.html tests/test_site_contract.py _pages
git commit -m "feat: add professor-style academic layout"
```

### Task 3: Build, Inspect, and Remove Deployment Risks

**Files:**
- Modify if required by build evidence: the files changed in Tasks 1-2
- Verify: `_site/`

**Interfaces:**
- Consumes: the complete Jekyll source from Tasks 1-2.
- Produces: a locally built site ready for GitHub Pages and screenshots at desktop and 375-pixel mobile widths.

- [ ] **Step 1: Install project-local Jekyll dependencies**

Run: `bundle config set --local path vendor/bundle && bundle install`

Expected: dependencies install under `vendor/bundle` without modifying global Ruby gems. If the system Bundler is incompatible with the lock resolution, install a Ruby-2.6-compatible Bundler locally and rerun with that version.

- [ ] **Step 2: Build the Jekyll site**

Run: `bundle exec jekyll build --trace`

Expected: exit code 0 and generated `_site/index.html`, `_site/publications/index.html`, `_site/cv/index.html`, `_site/profile.png`, and `_site/files/cho-confidence-interval-manuscript.pdf`.

- [ ] **Step 3: Add generated-output checks to the contract test**

Add tests that, when `_site/` exists, assert all five generated files above exist; generated HTML uses `/research/`-safe URLs; and generated visible text contains no demo-content markers from Review Focus.

- [ ] **Step 4: Run the full automated verification**

Run:

```bash
python3 -m unittest tests/test_site_contract.py -v
bundle exec jekyll build --trace
python3 -m unittest tests/test_site_contract.py -v
```

Expected: all tests pass before and after a clean build, and Jekyll exits 0.

- [ ] **Step 5: Serve and visually inspect desktop and mobile**

Run: `bundle exec jekyll serve --host 127.0.0.1 --port 4000`

Inspect `http://127.0.0.1:4000/research/` and the Publications and CV routes at desktop width and 375 CSS pixels. Verify no horizontal scrolling, readable line length, visible focus states, correct portrait crop, working PDF link, and consistent navigation.

- [ ] **Step 6: Fix only evidence-backed defects and rerun verification**

For each visual or build defect, add or tighten the relevant test when automatable, make the smallest source change, rerun the full verification from Step 4, and reinspect the affected viewport.

- [ ] **Step 7: Commit verified build fixes**

Run:

```bash
git add _config.yml _data _includes _layouts _pages _sass assets files tests
git commit -m "test: verify academic site build and responsive layout"
```

Skip the commit if Step 6 produced no source changes.

## Deployment Handoff

After all checks pass, show the user the local desktop and mobile result. Do not push until GitHub authentication is configured. Once authenticated, push `master` to `origin` and verify the public GitHub Pages deployment at `https://always-gi.github.io/research/`.
