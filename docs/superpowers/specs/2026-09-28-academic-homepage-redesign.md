# Hanggi Cho Academic Homepage Redesign

## Purpose

Transform the current Academic Pages starter site into a restrained academic homepage inspired by Dabeen Lee's site. The result should present Hanggi Cho as an undergraduate researcher without imitating faculty titles, lab sections, teaching history, or publication volume that do not apply.

## Information Architecture

The top navigation contains exactly three items:

1. Home
2. Publications
3. CV

The Home page contains exactly two substantive sections below the identity header:

1. About
2. Research Interests

The Publications page contains the current manuscript. The CV page replaces all Academic Pages sample content with a concise web CV based only on confirmed information.

## Visual Direction

- Use a white or warm-white page background with dark charcoal text.
- Use a compact top navigation with the site name on the left and page links on the right.
- Remove the Academic Pages left sidebar from the primary pages.
- Use a centered reading column with generous whitespace and thin blue-gray rules.
- Use a restrained serif display face for headings and a highly readable sans-serif face for body text.
- Keep decoration minimal: no gradients, glass cards, animated backgrounds, or social-link tiles.
- Preserve the existing portrait as the profile image.
- On mobile, stack the identity block and collapse the navigation without horizontal overflow.

## Home Page

### Identity Header

Show:

- Portrait
- Hanggi Cho
- Undergraduate Student in Mathematics and Applied Statistics
- Yonsei University
- Existing public contact email from the repository
- Links to GitHub, LinkedIn, and CV

Do not display a faculty title, office, laboratory, group, teaching role, or institutional affiliation beyond the confirmed undergraduate status at Yonsei University.

### About

Use a short first-person biography stating that Hanggi Cho is an undergraduate student at Yonsei University studying Mathematics and Applied Statistics. Avoid unsupported claims, awards, dates, or positions.

### Research Interests

Preserve the four existing research interests exactly:

- Operations Research
- Optimization
- Applied Probability
- Quantitative Finance

Do not add statistics or statistical inference as a separate research-interest label. The confidence-interval manuscript belongs on the Publications page rather than in this section.

## Publications Page

List one manuscript:

**Does a Larger Sample Size Always Lead to Shorter Confidence Intervals?**  
Jinwoong Park and **Hanggi Cho***  
Under review at *Statistics & Probability Letters*  
*Corresponding author*

Provide a link to the manuscript PDF. Preserve the author order shown in the manuscript. Bold Hanggi Cho's name and identify the corresponding-author role.

Do not publish a detailed first-person contribution claim unless both authors have agreed to that wording. Describe the paper's result in one neutral sentence.

## CV Page

Remove all fictional Academic Pages example entries. Include only confirmed items:

- Education: undergraduate study in Mathematics and Applied Statistics at Yonsei University
- Research interests
- Manuscript listed above
- Existing public contact and profile links

Do not invent enrollment dates, expected graduation dates, GPA, awards, employment, teaching, technical skills, or service activities. The page can be expanded later when verified information is supplied.

## Content Cleanup

- Remove sample navigation items for Talks, Teaching, Portfolio, Blog Posts, and Guide.
- Remove or stop rendering the sample publications, talks, teaching entries, portfolio items, and blog posts shipped with Academic Pages.
- Replace the template introduction currently shown on the Home page.
- Replace the fictional CV content.
- Retain the Jekyll/GitHub Pages deployment structure and existing repository URL settings.

## Accessibility and Verification

- Use semantic headings and navigation landmarks.
- Provide meaningful alt text for the portrait.
- Maintain visible keyboard focus and sufficient text contrast.
- Verify Home, Publications, and CV on desktop and mobile widths.
- Build the Jekyll site locally when dependencies allow.
- Confirm there are no template sample names, fake institutions, or fake publications in generated visible pages.

## Deployment Constraint

Local editing and preview are available. Pushing to GitHub requires the user to authenticate because this machine currently has no working HTTPS credential or GitHub SSH key.
