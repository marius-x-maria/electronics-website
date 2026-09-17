---
name: brand-spec
description: Single source of truth for West Point Europe BV brand facts, colors, content sources, and design references. All agents must read this before making any content or design change.
tags: [electronics-website, spec, source-of-truth, branding]
---

# Brand Spec — West Point Europe BV

This file is the canonical record of brand and content facts for the West Point Europe website project. When in doubt, this file wins.

---

## The Company

| | |
|---|---|
| **Name** | West Point Europe BV |
| **Industry** | B2B electronics sales / distribution |
| **Years in business** | 5+ (confirmed by client, 2026) |
| **HQ** | Eindhoven, Netherlands |
| **Other offices** | Hangzhou (China), Bucharest (Romania), Düsseldorf (Germany) |
| **COO** | Andrei Babcinetzki |
| **Phone** | +31 6 8735 1156 |
| **Email** | andrei@westpointeurope.com |
| **Domain (not yet connected)** | www.westpointeurope.com |

**Project contact:** Stefan (site requested on his behalf, per brief 2026-09-17).

---

## Brand Colors (official, client supplied 2026-09-17 — supersedes the earlier logo-extracted approximation)

| Token | Hex | Usage |
|---|---|---|
| `--navy` | `#283D4E` | Official brand navy. Wordmark, headings, nav background, hero gradient |
| `--teal` | `#005D63` | Official brand teal. Primary UI accent — buttons, eyebrow labels, icons, values row |
| `--steel` | `#6C8792` | Secondary tone (extracted from logo pixels) — compass ring, hero gradient endpoint |
| `--sand` | `#DFDACF` | Pale logo accent (extracted from logo pixels) — reserved for thin decorative dividers |
| `--ink` | `#1A2530` | Body text |
| `--grey` | `#6B7280` | Secondary/muted text |
| `--bg` | `#FFFFFF` | Page background |
| `--bg-alt` | `#F5F7F9` | Alternating section background |

`--navy` and `--teal` are the two official hex codes given directly by the client (2026-09-17), replacing the earlier logo-extracted navy approximation (`#2F4A55`, close but not exact) and the invented bronze accent (`#A79162`, a stand in used before the real teal was known). `--steel` and `--sand` remain logo-extracted supporting tones, unchanged.

## Logo

Client supplied the real logo files on 2026-09-17: `LOGO WestPoint.JPG`, `1.JPG`, `4.JPG` (full lockup: icon + wordmark + "Eindhoven, Netherlands"), `3.JPG` (icon only, clean), `2.JPG` (business card, used only to confirm contact details already in this file).

- **`images/logo-icon.png`** — the real compass icon (from `3.JPG`), background removed programmatically (alpha threshold on near white pixels) and cropped tight. Used in the nav header, footer, and as the favicon source. Verified to read cleanly on both white and navy backgrounds.
- **`images/favicon-16.png`, `favicon-32.png`, `favicon-180.png`, `favicon-48.png`, `favicon-256.png`** — generated from `logo-icon.png` at standard sizes; 16/32/180 are wired into `<head>`.
- The raw client-supplied JPGs (`1.JPG`, `2.JPG`, `3.JPG`, `4.JPG`, `LOGO WestPoint.JPG`) are kept locally in `images/` for reference but excluded from git via `.gitignore` — the business card in particular has no reason to sit in a public repo, and none of the raw files are actually referenced by the page (only the processed `logo-icon.png` and favicons are).
- The header still uses HTML text for "WEST POINT / EUROPE BV" (styled to match the logo's typography) rather than embedding the full raster lockup, so it scales cleanly at nav size — the icon image supplies the mark, the text supplies the wordmark.

---

## Design References

- **cytec-gmbh.de/home/** — B2B electronics distributor (IT/mobile devices). Structure: hero → value props → strengths grid (6 cards) → timeline → logistics stats → brand logo grid → testimonials → contact form → footer.
- **neobution.com** — B2B consumer electronics distributor, multi-region (Dortmund/Miami/Dubai hubs). Structure: hero → metrics strip → 3-pillar about → category grid → services → mission/values → founder quote → global presence cards → contact form → footer.
- **Common pattern used for this site:** hero, metrics strip, 3-pillar "why us", services grid, mission/values, global presence cards (mapped to our 4 real offices), contact form, footer. Single scrolling page (client decision, 2026-09-17), not multi-page.
- **ant.design/docs/spec/introduce** — Ant Design's design *principles* page (not the React component library). Four core values: Natural, Certain, Meaningful, Growing; plus compositional principles (proximity, alignment, contrast, repetition) and interaction principles (make it direct, stay on the page, keep it lightweight). Applied here as design guidance to a plain HTML/CSS build, not as an imported component library — no build step, matching the low-risk, no-CI deploy pattern already proven on the wedding site.

---

## Content Status

- **Confirmed facts:** B2B electronics sales, 5+ years in business, 4 office locations (Eindhoven, Hangzhou, Bucharest, Düsseldorf), COO name and direct contact details.
- **Confirmed company description (client provided, 2026-09-17), used verbatim in the About section:** "West Point Europe is a premier B2B global distributor specializing in a comprehensive portfolio of electronic components, enterprise hardware, and consumer technology. We bridge the gap between world class manufacturers and businesses worldwide. Backed by a robust logistics network spanning multiple continents, we provide seamless supply chain solutions, guaranteed authenticity, and scalable inventory management tailored to the dynamic needs of OEMs, ODMs, and enterprise clients."
- **Placeholder / needs real copy:** services list only (currently generic B2B electronics distribution services — distribution, sourcing/procurement, logistics/warehousing, QA/testing, market access, after sales support), mission statement wording, any real metrics (brand count, partner count, warehouse size — none fabricated; only confirmed facts are shown as stats).
- **No fabricated numbers:** unlike the reference sites (which show brand/partner/country counts), no invented statistics have been added. Only the 4 confirmed facts above appear as stat cards. Add real numbers once provided.
- **Contact form backend:** explicitly deferred by the client (2026-09-17) — "leave it for the moment, we will do it later." Current `mailto:` stopgap stays as is until requested.

---

## Design Decisions (Rationale)

| Decision | Rationale |
|---|---|
| Single HTML file, no build step | Matches the proven low-risk deploy pattern from the wedding site — push to GitHub Pages, no CI, no framework |
| Single scrolling page, not multi-page | Client decision (2026-09-17) — matches neobution.com's structure over cytec's multi-page nav |
| Ant Design *principles* applied, not the React library | The user's link was to the design spec/values page, not the component docs. A full antd + React setup would require a build step for a simple marketing site — not worth the added complexity here. Flag to reconsider if the user wants literal antd components. |
| No fabricated stats | Reference sites use invented-sounding numbers (50+ brands, 250+ partners); only confirmed facts about West Point Europe are shown as stats, to avoid misrepresenting the business |
| Contact form has no backend yet | No Apps Script or form service set up yet — form currently uses a `mailto:` fallback. Needs a proper backend (e.g., Formspree, or an Apps Script pattern like the wedding site's) before launch |
| Hosting: new GitHub repo + Pages, default URL | Client decision (2026-09-17) — hold off on connecting westpointeurope.com until design is approved |

---

## Production Hosting (SFTP)

Client provided real SFTP credentials for a production webspace on 2026-09-17. These are stored **only** in `.env` at the project root, which is excluded from git via `.gitignore` — this repo is public, so neither the host, username, nor password may appear in any tracked file, commit, or this document. See `.env.example` for the expected variable names (values live in `.env` only).

**Not yet used.** No files have been uploaded to this host. Deploying there would go live on real production infrastructure and was not yet explicitly confirmed as "do this now" — check with the client before the first upload, and confirm the target directory won't overwrite anything already live at that host.

## Links

- [[../AGENT.md]] — agent rules and current build state
