# Agent Briefing — West Point Europe Website

Read this file at the start of every session. It is the single source of truth for the agent's role, current state, and rules for this project.

---

## Your Role

You maintain and build the marketing website for **West Point Europe BV**, a B2B electronics sales company (Eindhoven HQ, offices in Hangzhou, Bucharest, Düsseldorf). Requested on behalf of the client by Stefan (2026-09-17). Not yet published or handed off — this is still in design review with the client.

---

## What's Built

Single file PWA style site (`index.html`), no build step, no framework — same low risk pattern as the wedding project.

### Sections (single scrolling page, in order)

| Section ID | Name | What it does |
|---|---|---|
| (nav) | Header | Sticky nav, frosts on scroll, logo + wordmark, links to About/Services/Global Presence/Contact |
| `#top` | Hero | Navy gradient background, headline, two CTAs (Get in Touch, Our Services) |
| (stats) | Stats strip | 4 confirmed facts only: 5+ years in business, 4 offices, B2B focus, EU+APAC corridor. No fabricated numbers. |
| `#about` | Why West Point | 3 pillar cards: Reliability, Global Reach, Speed to Market |
| `#services` | Services | 6 generic B2B electronics distribution service cards — placeholder copy, needs real service list from client |
| (mission) | Mission/Values | Navy full width band, mission statement + 4 values (Reliability, Partnership, Integrity, Speed) |
| `#offices` | Global Presence | 4 office cards: Eindhoven (HQ), Hangzhou, Bucharest, Düsseldorf |
| `#contact` | Contact | Form (name/company/email/message) + direct contact block (Andrei Babcinetzki, COO) |
| Footer | — | Logo, nav links repeat, contact, office list, copyright |

### Key Features

- Responsive: breakpoints at 900px and 640px; mobile hamburger + slide in nav drawer
- Scroll reveal via IntersectionObserver
- Nav frosts to white on scroll (same technique as the wedding site)
- Google Fonts: Manrope (400–800 weights)
- Placeholder CSS/SVG compass star logo mark, recreated visually from a chat screenshot — **not the real logo file**

### Contact Form

No backend wired up. Currently intercepts submit and opens a `mailto:` draft to `andrei@westpointeurope.com` with the form fields pre filled. This is a stopgap, not a real lead capture mechanism — see Pending below.

---

## What's Pending

| Item | Notes |
|---|---|
| Real logo file | Only have a chat screenshot, not a usable asset. Need the source SVG/PNG (transparent background ideally) to replace the placeholder CSS/SVG mark in `index.html` and set a proper favicon |
| Exact brand colors | Current palette (`--navy #243B4E`, `--steel #5D7E90`, `--gold #C6A671`) is a visual approximation, not color picked from a real file. Confirm or correct once the logo asset is available |
| Real services list | Current 6 service cards are generic B2B electronics distribution placeholders. Replace with the client's actual service offering |
| Real metrics (optional) | If the client wants to show numbers like brand count, partner count, or warehouse size (as both reference sites do), only add ones that are true — do not invent figures |
| Contact form backend | Needs a real mechanism (Formspree, a Google Apps Script pattern like the wedding site's, or similar) before this goes live for actual lead capture |
| Hosting | Not yet published. Client decision (2026-09-17): new GitHub repo + GitHub Pages, default `.github.io` URL for now. Custom domain `westpointeurope.com` to be connected later, once DNS access is confirmed |
| Favicon / OG image | Not yet created — depends on the real logo file |

---

## Key Files

| File | Purpose |
|---|---|
| `index.html` | The entire site — HTML, CSS, JS, all in one file |
| `knowledge-base/brand-spec.md` | Single source of truth for all brand facts, colors, content status, and design references |
| `images/` | Empty — waiting on the real logo asset |

---

## Design Spec

See `knowledge-base/brand-spec.md` for the full color table, content status, and design reasoning.

### Colour Palette (approximate — pending real logo file)

| Token | Hex | Usage |
|---|---|---|
| `--navy` | `#243B4E` | Wordmark, headings, hero/mission backgrounds |
| `--navy-dk` | `#1A2B38` | Darkest gradient stop, footer background |
| `--steel` | `#5D7E90` | Secondary accent, compass ring |
| `--gold` | `#C6A671` | CTA buttons, dividers, eyebrow labels |
| `--ink` | `#1A2530` | Body text |
| `--grey` | `#6B7280` | Secondary/muted text |
| `--bg` | `#FFFFFF` | Page background |
| `--bg-alt` | `#F5F7F9` | Alternating section background |

### Typography

Manrope (400, 500, 600, 700, 800) — single font family, sans-serif, used for both headings and body.

### Design References

- **cytec-gmbh.de/home/** and **neobution.com** — both B2B electronics distributors, used as structural references (hero, stats, pillars, services, mission, global presence, contact)
- **ant.design/docs/spec/introduce** — Ant Design's design *principles* (Natural, Certain, Meaningful, Growing), applied as guidance to this plain HTML build, not as an imported component library

---

## Rules

1. **No fabricated statistics** — only show numbers confirmed by the client (currently: 5+ years, 4 offices). Do not invent brand/partner counts to match the reference sites' style.
2. **No build tools** — keep the single file architecture unless the client explicitly wants the real Ant Design React component library, which would be a materially different, heavier project.
3. **Do not connect the real domain or publish publicly** until the client has approved the design — current decision is a default GitHub Pages URL only.
4. **Replace placeholder content clearly** — services list and logo are known placeholders; do not present them to the client as final without flagging that they're provisional.
5. **Mobile first** — test all additions at 375px and 680px, matching the wedding project's proven breakpoints.

---

## Shared Skills

See `C:\New life\skills\README.md` for shared skills available across all projects.
