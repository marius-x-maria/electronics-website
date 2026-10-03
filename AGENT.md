# Agent Briefing — West Point Europe Website

Read this file at the start of every session. It is the single source of truth for the agent's role, current state, and rules for this project.

---

## Your Role

You maintain and build the marketing website for **West Point Europe BV**, a B2B electronics sales company (Eindhoven HQ, offices in Hangzhou, Bucharest, Düsseldorf). Requested on behalf of the client by Stefan (2026-09-17). Not yet published or handed off — this is still in design review with the client.

---

## Capability Registry

**Single source of truth for what exists.** Four states: `included` (built, expected to work) · `available` (partial — the note says exactly what is missing) · `absent` (not built; add only on request) · `removed` (deliberately deleted; restore only on request).

**Without a row, a capability is `absent`.** Existing code is not a request — finding a half-built thing does not authorize finishing it.

| Capability | State | Note |
|---|---|---|
| Single-page site (`index.html`) | `included` | No build step, no framework |
| Header / sticky nav | `included` | Frosts on scroll; mobile hamburger + slide-in drawer |
| Hero + two CTAs | `included` | Navy gradient background |
| Stats strip | `included` | 4 confirmed facts only — see Rule 1 |
| Why West Point (3 pillars) | `included` | Reliability, Global Reach, Speed to Market |
| Mission / values band | `included` | Navy full-width, 4 values |
| Global Presence (4 offices) | `included` | Eindhoven HQ, Hangzhou, Bucharest, Düsseldorf |
| Footer | `included` | Logo, nav repeat, contact, office list |
| Responsive layout | `included` | Breakpoints at 900 px and 640 px; test at 375 and 680 per Rule 5 |
| Scroll reveal | `included` | IntersectionObserver |
| Logo + favicon set | `included` | 16/32/48/180/256; 16/32/180 wired into `<head>` |
| Brand tokens in `:root` | `included` | Official client palette — see Design Spec |
| GitHub Pages preview deploy | `included` | Default `.github.io` URL. The intended current state — see Rule 3 |
| Services list | `available` | 6 cards are **generic placeholders** — needs the client's real service offering |
| Contact form | `available` | Renders and validates, but only opens a `mailto:` draft. Not real lead capture. **No pending / success / error state** — submit jumps straight to `mailto:` with no feedback, `required` relies on native browser bubbles, and no `aria-describedby` links an error to its field. Fails the four-states check in [[ui_specialist]]; a real success state is a product decision, not a UI fix |
| Contact form backend | `absent` | Client deferred 2026-09-17 ("leave it for the moment"). Options: Formspree, or the wedding site's Apps Script pattern |
| Real metrics | `absent` | Only if the client supplies true figures. **Never invent them** — Rule 1 |
| OG / social share image | `absent` | Not created |
| Custom domain | `absent` | `westpointeurope.com` not connected — gated on client approval |
| SFTP production deploy | `absent` | Credentials in `.env` (gitignored), **never used**. Confirm target directory and get explicit go-ahead first — could overwrite whatever is live |
| Dark theme | `absent` | Not requested. Visual checks shoot light only |
| Automated tests | `absent` | Tier 0 — Playwright Python behaviour tests are possible; none written yet |
| Build tooling / bundler | `removed` | Deliberate — Rule 2. Restoring it is a Tier-1 decision, see [[web-tier-upgrade]] |
| Backend / database | `absent` | Tier 2 — needs Docker and paid hosting |
| Accounts / auth | `absent` | Tier 2 |
| Payments | `absent` | Tier 2 |
| Infrastructure as code | `absent` | Not adopted — no Terraform in this framework |

**Director:** Vibe Coder Agent · **Tier:** 0 (zero-build static) · **Engaged subagents:** [[ui_specialist]], [[web_deploy_specialist]], plus [[frontend_engineer]] for any non-trivial slice.

---

## How It Works (reference)

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
- Real logo icon (`images/logo-icon.png`, background removed, cropped from the client-supplied file), used in nav, footer, and favicon

### Contact Form Stopgap

No backend. Submit is intercepted and opens a `mailto:` draft to `andrei@westpointeurope.com` with the fields pre-filled. Not real lead capture — see the registry row.

### Open Hosting Question

`westpointeurope.com` and the client's SFTP host are both `absent`. Before any DNS work, clarify which is the authoritative production path — GitHub Pages with a custom domain, or the SFTP host. Doing both is how a site ends up live in two places that drift.

---

## Key Files

| File | Purpose |
|---|---|
| `index.html` | The entire site — HTML, CSS, JS, all in one file |
| `knowledge-base/brand-spec.md` | Single source of truth for all brand facts, colors, content status, and design references |
| `images/logo-icon.png` | Real logo mark (background removed, cropped) — used in nav, footer, favicon source |
| `images/favicon-*.png` | 16/32/48/180/256px favicon set; 16/32/180 wired into `<head>` |
| `images/*.JPG` | Raw client-supplied originals (logo exports, business card) — **gitignored**, local reference only |

---

## Design Spec

See `knowledge-base/brand-spec.md` for the full color table, content status, and design reasoning.

### Colour Palette (official — client supplied 2026-09-17)

| Token | Hex | Usage |
|---|---|---|
| `--navy` | `#283D4E` | Official brand navy — wordmark, headings, hero/mission backgrounds |
| `--navy-dk` | `#1B2B37` | Darkest gradient stop, footer background |
| `--teal` | `#005D63` | Official brand teal — CTA buttons, eyebrow labels, icons |
| `--steel` | `#6C8792` | Secondary tone extracted from logo pixels — compass ring, hero gradient |
| `--sand` | `#DFDACF` | Pale logo accent — decorative dividers only |
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
3. **GitHub Pages is the preview, and that is the intended current state.** The default `.github.io` URL is where the client reviews the design — it being live there is correct, not a breach. What stays gated until the client approves: connecting `westpointeurope.com`, and uploading anything to the client's SFTP host. Do neither without an explicit go-ahead.
4. **Replace placeholder content clearly** — services list and logo are known placeholders; do not present them to the client as final without flagging that they're provisional.
5. **Mobile first** — test all additions at 375px and 680px, matching the wedding project's proven breakpoints.

---

## Shared Skills

See `C:\New life\skills\README.md` for shared skills available across all projects.
