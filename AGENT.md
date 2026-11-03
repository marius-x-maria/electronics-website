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
| Hero + two CTAs | `included` | Navy gradient background; no eyebrow label (generic-defaults check, 2026-11-03) |
| Confirmed facts ledger | `included` | 4 confirmed facts only (Rule 1), a ruled row on the hero's base edge since 2026-11-03 (was a separate big-number band) |
| Why West Point (3 pillars) | `included` | Reliability, Global Reach, Speed to Market — ruled list beside the intro, no numbered icon cards |
| Mission / values band | `included` | Navy full-width, statement left, 4 values as a ruled list right |
| Global Presence (4 offices) | `included` | Eindhoven HQ, Hangzhou, Bucharest, Düsseldorf |
| Footer | `included` | Logo, nav repeat, contact, office list |
| Responsive layout | `included` | Breakpoints at 900 px and 640 px; test at 375 and 680 per Rule 5 |
| Scroll reveal | `included` | IntersectionObserver |
| Logo + favicon set | `included` | 16/32/48/180/256; 16/32/180 wired into `<head>` |
| Brand tokens in `:root` | `included` | Official client palette — see Design Spec. Every derived tint is a token too; `web_audit` 0 errors (only the `theme-color` meta literal remains) |
| Browser surfaces | `included` | Selection, caret, scrollbar, accent colour and focus ring themed from the palette; tabular numerals for phone numbers |
| GitHub Pages preview deploy | `included` | Default `.github.io` URL. The intended current state — see Rule 3 |
| Services list | `available` | 6 services as a two-column ruled list (no glyph icons). Copy is still **generic placeholder** — needs the client's real service offering |
| Contact form | `included` | `mailto:` hand-off with all states (Marius 2026-11-03): inline field errors linked by `aria-describedby`, pending button, a "your email is ready to send" status with a fallback address, "write another" reset. Fields are URL-encoded (an `&` in the company used to cut the body). Still not lead capture — see the backend row |
| Contact form backend | `absent` | Client deferred 2026-09-17 ("leave it for the moment"). Options: Formspree, or the wedding site's Apps Script pattern |
| Real metrics | `absent` | Only if the client supplies true figures. **Never invent them** — Rule 1 |
| OG / social share image | `absent` | Not created |
| Custom domain | `absent` | `westpointeurope.com` not connected — gated on client approval |
| SFTP production deploy | `absent` | Credentials in `.env` (gitignored), **never used**. Confirm target directory and get explicit go-ahead first — could overwrite whatever is live |
| Dark theme | `absent` | Not requested. Visual checks shoot light only |
| Automated tests | `included` | `tools/test_contact_form.py`: 6 Playwright behaviour tests (form states, mailto content, mobile menu + Escape). Run `python -I tools/test_contact_form.py` |
| Build tooling / bundler | `removed` | Deliberate — Rule 2. Restoring it is a Tier-1 decision, see [[web-tier-upgrade]] |
| Backend / database | `absent` | Tier 2 — needs Docker and paid hosting |
| Accounts / auth | `absent` | Tier 2 |
| Payments | `absent` | Tier 2 |
| Infrastructure as code | `absent` | Not adopted — no Terraform in this framework |

Surface modes: `index.html` = Persuade (B2B lead generation: bold but precise, familiar patterns for the form).

**Director:** Vibe Coder Agent · **Tier:** 0 (zero-build static) · **Engaged subagents:** [[ui-specialist]], [[web-deploy-specialist]], plus [[frontend-engineer]] for any non-trivial slice.

---

## How It Works (reference)

Single file PWA style site (`index.html`), no build step, no framework — same low risk pattern as the wedding project.

### Sections (single scrolling page, in order)

| Section ID | Name | What it does |
|---|---|---|
| (nav) | Header | Sticky nav, frosts on scroll, logo + wordmark, links to About/Services/Global Presence/Contact |
| `#top` | Hero | Navy gradient background, headline, two CTAs (Get in touch, Our services), then the confirmed-facts ledger: 5+ years, 4 offices, B2B focus, EU+APAC corridor. No fabricated numbers. |
| `#about` | Why West Point | Intro left, 3 ruled pillars right: Reliability, Global reach, Speed to market |
| `#services` | Services | 6 generic B2B electronics services as a two-column ruled list — placeholder copy, needs real service list from client |
| (mission) | Mission/Values | Navy full width band, mission statement + 4 values (Reliability, Partnership, Integrity, Speed) |
| `#offices` | Global Presence | 4 offices on top rules (teal rule = HQ): Eindhoven, Hangzhou, Bucharest, Düsseldorf |
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
| `tools/test_contact_form.py` | Behaviour tests for the contact form and mobile menu |
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
| `--teal` | `#005D63` | Official brand teal — CTA buttons, office roles, HQ rule, links, focus ring |
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
