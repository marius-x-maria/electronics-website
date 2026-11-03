---
name: electronics-website-readme
description: Map of Content for the West Point Europe BV website - what each file is for, how to preview and test it
tags: [electronics-website, moc, index]
---

# West Point Europe BV — Website

Single-page marketing site for a B2B electronics sales company. Plain HTML, CSS and JavaScript in one file, with no build step. Preview: https://marius-x-maria.github.io/electronics-website/

| File | What it answers |
|---|---|
| [[AGENT]] | Project state: capability registry, sections, rules, design spec |
| `index.html` | The whole site: markup, styles and scripts |
| [[brand-spec]] | Brand facts, palette, content status and design references (`knowledge-base/brand-spec.md`) |
| `tools/test_contact_form.py` | Behaviour tests for the contact form and mobile menu (Playwright, Python) |
| `images/` | Logo mark and favicon set |
| [[MAP]] | Generated map of files and links |

## Test

```bash
python tools/test_contact_form.py
```
