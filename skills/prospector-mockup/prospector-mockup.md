---
name: prospector-mockup
description: Agent 3 of the Prospector pipeline — builds a single-page Romanian demo website (mockup) for a qualified lead in under 60 minutes using the bundled template and sector palette system. Use this skill whenever the user wants to build a mockup, create a demo site for a prospect, produce a propunere de site, or says anything like "build the mockup for", "make the demo site", "fă site-ul demo". Read this file completely before writing any HTML for a prospect.
---

# Prospector — Agent 3: Mockup Builder

## Mission
Produce a mobile-first, single-file demo website that makes the owner say
"acesta este magazinul meu" within five seconds of opening the link on their
phone. Speed and emotional recognition beat feature depth. Budget: ≤ 60
minutes including QA.

## Inputs required (from Agent 2's pipeline row + live Maps listing)

Business name · category · locality · address · phone (mobile, WhatsApp-
capable) · opening hours · 2–3 real review quotes with author first name +
initial · whether photos exist on the listing · services inferred from
category, reviews, and photos. If any of these are missing, fetch them from
the Maps listing before building — do not invent them.

## Standing build process (mandatory, every mockup, effective 2026-08-16)

Every mockup build — this one and every future one — follows these three
steps **in order**. After finishing a step, stop completely and wait for
Calin to say "done" before starting the next one. Do not combine steps,
do not get ahead of the current step, and do not summarize or preview a
later step while working on the current one. This is a standing process
rule, not a one-off instruction for a single lead.

### Step 1 — Logo and hero image prompts (image generation, human-in-the-loop)

Do not use built-in/native image generation for these — output quality is
not sufficient for client-facing work. Instead:

1. Research the business's real trade, category, and locality from
   `data/pipeline.csv` and any facts already verified for that lead.
2. Write two separate, detailed image-generation prompts, ready to paste
   directly into ChatGPT:
   - **LOGO PROMPT** — grounded in the real trade and the category shell's
     palette, if a dedicated shell already exists for that category (see
     "Sector palette system" below); otherwise a sensible palette for the
     trade, clearly flagged as not-yet-a-shell.
   - **HERO IMAGE PROMPT** — a large, atmospheric, full-bleed-appropriate
     background image grounded in the real trade (workshop, yard,
     storefront, materials — whatever fits this specific business), not
     generic stock imagery.
3. Show both prompts, clearly labeled "LOGO PROMPT" and "HERO IMAGE
   PROMPT," and nothing else. No HTML, no building, no moving to another
   step.
4. Stop and wait.

Calin runs both prompts through ChatGPT manually, then sends back the
resulting images plus the business's slug. Save them into the lead's own
mockup folder (see "Folder structure" below), with this exact naming
convention:

- `mockups/{slug}/logo.png`
- `mockups/{slug}/hero.png`

(extension matches whatever format the source image actually is —
`.png`, `.jpg`, `.webp` — the name stays `logo`/`hero`, not the format.)

Confirm both files are saved correctly, then stop again and wait for
"done" before Step 2.

### Step 2 — Structure from references

Calin provides 2–3 reference screenshots. These do not need to match this
business's industry — they are for structural and compositional
inspiration only.

Copy from the references: layout structure, spacing rhythm, section
composition, hero treatment (e.g. full-bleed background image with
overlaid text), motion restraint.

Do not copy from the references: typography style, color mood, or any
content-specific stylistic choice tied to the reference's own industry.
Typography and color stay grounded in this business's actual category
shell, decided independently of what the reference used.

Confirm the references have been reviewed and describe, in a few
sentences, exactly which structural elements are being taken from them.
Then stop and wait for "done" before Step 3.

### Step 3 — Full build

Only now, build the complete mockup, applying all of the following
together:

- The frontend-design skill
  (github.com/anthropics/skills/tree/main/skills/frontend-design), read
  this session if not already read.
- Tailwind CSS via CDN, no build step — see "Build mechanics" below.
- Every shared/general rule in this file: mobile header/hamburger pattern,
  WhatsApp icon-only on constrained mobile width, watermark treatment, map
  iframe fallback ("Deschide harta"), `text-wrap: balance` on multi-line
  copy, full alignment scan across mobile and desktop.
- Scroll-triggered reveal on every major section, and hover states on
  every interactive element — see the standalone rule in "Shared/general
  mockup rules" below.
- The logo and hero image from Step 1, placed correctly: logo prominent in
  the hero, hero image as the full-bleed background per Step 2's
  structural direction.
- Real content only — verified facts, real reviews if available; omit
  rather than invent, per "Integrity rules" below.
- The full QA checklist below: no leftover placeholder tokens, 360px
  mobile pass with no horizontal scroll, `wa.me` and `tel:` links correct,
  diacritics render, noindex + footer disclaimer present, alignment
  consistent everywhere.

Show the finished result — screenshots on both desktop and mobile — and
stop. Do not update `data/pipeline.csv`; Calin confirms and updates it
himself after reviewing.

## Folder structure (standing convention, effective 2026-08-16)

Every mockup is self-contained in its own folder — nothing about a lead's
build lives loose at the top level of `mockups/`. For a lead with slug
`{slug}`:

```
mockups/{slug}/index.html          the mockup itself
mockups/{slug}/logo.png            Step 1 logo, watermarked, as used on the page
mockups/{slug}/hero.png            Step 1 hero image, as used on the page
mockups/{slug}/assets/             real photos, Places API JSON, the
                                    un-watermarked source logo, any other
                                    source material
mockups/{slug}/screenshots/        QA/debug screenshots — desktop, mobile,
                                    alignment checks, etc.
```

Build straight into this structure from the start — create the folder and
its `assets/`/`screenshots/` subfolders as step one of the build, and never
build a flat `{slug}.html` to be reorganized afterward.

The live URL for a finished mockup is
`https://calinbotean.github.io/prospector-mockups/mockups/{slug}/` — no
`.html`, since GitHub Pages serves `index.html` for the directory
automatically. Use this exact form (trailing slash, no filename) in
`mockup_url`.

This replaced the earlier flat layout (`mockups/{slug}.html` plus shared
`mockups/logos/` and `mockups/hero/` folders) on 2026-08-16, when the two
existing mockups at that point (agrofarm-marius, sabo-itp-service) were
reorganized into it and their `mockup_url` values updated accordingly.

## Build mechanics (used inside Step 3)

1. Create `mockups/{slug}/` with `assets/` and `screenshots/` subfolders
   inside it (slug = lowercase business name, hyphens, no diacritics).
   Copy `assets/template.html` to `mockups/{slug}/index.html` as the
   working file.
2. Load Tailwind CSS by CDN in the page head, after Google Fonts and before
   the custom `<style>` block. No build step, account, package install, or
   framework setup is needed.
3. Pick the sector palette from the table below and replace the `:root`
   palette block (the template marks it clearly).
4. Replace every `{{TOKEN}}` in the file. Then verify none remain:
   `grep -o '{{[A-Z_0-9]*}}' mockups/{slug}/index.html` must return nothing.
5. Write the Romanian copy per the copy rules below.
6. Run the QA checklist. Deliver the file and the deployment note.

## Shared/general mockup rules

Tailwind CSS via CDN is now the base styling system for every mockup and
category shell. Use Tailwind utility classes for layout, spacing, flex/grid
structure, alignment, responsive breakpoint behavior, sizing, and balanced
multi-line copy. This keeps common alignment and spacing decisions correct by
construction, especially at 360px mobile width.

Keep custom CSS for the things that make each trade feel specific: the
`:root` palette variables, typography tokens, component skins, shadows,
signature visual elements, hover treatments, and the one restrained motion
pattern. Do not rebuild generic spacing, columns, rows, or alignment rules in
custom CSS when Tailwind utilities can express them clearly.

Use `text-balance` / `text-wrap: balance` for multi-line headings and body copy
that otherwise gets an accidental ragged edge. Never use full text justification
for Romanian body copy in these narrow mockup layouts.

Mobile headers use a compact, repeatable pattern: text-only business name or
small brand mark on the left, hamburger/dropdown navigation for page anchors,
and the WhatsApp CTA on the right. Do not crowd the mobile header with full
inline nav links plus a full WhatsApp label. Desktop may keep the full inline
nav.

The header WhatsApp button keeps the full "WhatsApp" text label on desktop. On
mobile, when width is constrained, use the WhatsApp icon alone with a clear
`aria-label`; never use a truncated text abbreviation such as `WA`.

Logos belong primarily in the hero, large enough that the mark and text are
legible. Do not shrink a generated or reconstructed logo into the small header
as the main brand moment. On mobile, center the hero logo and align it
deliberately with the hero headline/content stack.

**Logo and hero image creation are out of scope for the mockup builder.**
Calin generates both separately, outside this pipeline, using an external
image tool (ChatGPT image generation), from written prompts produced in
Step 1 of the standing build process above. The builder (Codex/Claude Code)
never designs, generates, or improvises a logo or hero image itself — its
job starts only once the source files have been supplied at
`mockups/{slug}/logo.png` and `mockups/{slug}/hero.png`, and is
limited to: apply the watermark to the logo (below), and place both per
the placement rules above and Step 2/3's structural direction. If a source
file is missing for a lead, do not invent one and do not proceed without it
as if it were optional — build without it, flag its absence clearly in the
delivery notes, and note that the ChatGPT-generated source image is needed
before the mockup is complete.

If a free mockup uses a newly generated logo, apply a visible `DEMO` watermark
to the logo asset with Python's Pillow library before inserting it in the page.
The watermark must stay visible, but make it visually restrained: prefer a
small corner ribbon or reduced-opacity stamp. Never remove it from a free
mockup, and never make it so heavy-handed that the logo looks ugly or unusable.

**Scroll-triggered reveal (mandatory, every build).** Every major section
below the hero — services/products grid, "de ce noi"/trust pillars, reviews,
contact/map, footer — reveals on scroll with a fade-in combined with a subtle
slide-up (translateY roughly 16–24px to 0), duration 200–300ms, ease-out
timing, triggered via `IntersectionObserver` (or an equivalent lightweight
reveal-on-scroll approach) at roughly a 10–20% visibility threshold. The hero
itself is exempt — it must already be visible on load, not waiting on a
scroll trigger. Never use bounce, elastic, or overshoot easing, and never
delay a reveal so long that content feels sluggish at a normal scroll speed.
This stays consistent with the "no parallax, no heavy JavaScript" rule below
— a small IntersectionObserver-based reveal script is the one motion pattern
allowed.

**Hover states (mandatory, every build).** Every interactive element —
buttons, CTA links, service/product cards, review cards, nav items — gets a
hover state built from a subtle lift/shadow/scale: pick one or two of
`translateY(-2px to -4px)`, a soft shadow increase, or `scale(1.02–1.03)`
per element type, consistently, rather than stacking all three at once.
Transition duration 200–300ms, ease-out timing, no bounce or elastic easing.
This is additional detail on top of, not a replacement for, the 0.2s
hover-transition rule in "Sector palette system" below.

The hero section must own the full dark/background treatment for every hero
child on every breakpoint. Root cause of the Agrofarm mobile bug: late-stacked
mobile hero children (category tags and quick-fact badges) can appear to sit on
the next light section if the dark hero background is only implied by utility
classes, height assumptions, or a wrapper that does not contain all mobile
children. Fix pattern: put photo, copy, buttons, tags, and badges inside the
same `.hero` section; give `.hero` a direct custom-CSS background/color fallback
using the palette variables; avoid placing hero badges outside the section or in
absolute/overflow layouts; verify at 360px that the bottom of every tag/badge is
within the hero's rendered bounds.

When building the hero-lockup (logo + kicker + headline + subline + buttons),
alignment must be controlled entirely by the parent container — `align-items`
on desktop, overridden inside the mobile media query — never by an individual
child's own `margin: 0 auto` or similar self-centering rule. Root cause of the
Sabo alignment bug: `hero-kicker` kept its own `margin: 0 auto`, which
silently overrode `hero-lockup`'s `align-items: flex-start` and re-centered
just that one element while the logo, H1, subline, and buttons correctly
moved left. Fix pattern: keep every hero-lockup child free of its own
horizontal margin/auto-centering; let the parent's `align-items` (and its
mobile-breakpoint override) be the single source of truth for alignment. If a
child looks off-alignment after a parent `align-items` change, check that
child's own CSS for a competing `margin:auto` before touching anything else.

Every map embed needs a robust fallback because WhatsApp's in-app browser can
block or fail iframe content more aggressively than Chrome/Safari. Pair the
iframe with a visible `Deschide harta` link/button to the Google Maps listing,
and show that fallback if the iframe fails, is blocked, or remains blank after a
short timeout. Use `Vezi harta` / `Deschide harta` wording unless the link truly
opens turn-by-turn directions.

Before a mockup is finished, run an alignment scan across the whole page on
desktop and 360px mobile: header, hero, services/products grid, trust section,
reviews, contact/map, sticky bar, and footer. Decide deliberately what is
centered versus left-aligned, and make headings, body text, cards, buttons, and
section edges line up consistently.

## Sector palette system

The template's layout, typography, and section order are fixed (they are the
proven pattern). Only the palette variables change per sector:

### Category shell — `magazin furaje`

Use this shell before the generic "Agri / feed / food producers" row whenever
the pipeline category is exactly `magazin furaje`.

- Palette, named for the trade: greenhouse green `#123F36`, wet soil
  `#3A2A1E`, dry maize `#D7A72E`, fitosanitary label red `#A74232`,
  galvanized metal `#AAB8B1`, pale leaf background `#E7EEE8`.
- Typeface pairing: `Roboto Slab` for display headings, `Barlow Condensed`
  for shelf labels/badges, `Inter` for body copy and CTAs.
- Layout concept: keep the proven conversion skeleton, but make the hero feel
  like the front of a local agri shop: advice-first copy, real storefront or
  product-shelf photo, then a compact rail of feed/seed/treatment shelf tags
  before the services grid. The page should sell practical selection help,
  not just a list of products.
- Signature visual element: a reusable "raft de etichete" — small shelf/sack
  labels such as `FURAJE`, `SEMINȚE`, `TRATAMENTE`, `GRĂDINĂ`, reused in the
  hero and section headers so the page is remembered as an agri/feed shop.
- Avoid for this shell: cream background with terracotta accent, near-black
  with one neon accent, and generic hairline-rule broadsheet layouts. If the
  page can be reskinned for a plumber, salon, or café in five minutes by only
  changing colors and photos, revise before delivery.

### Category shell — `service auto`

Use this shell before the generic "Auto (dezmembrări, service, vulcanizare)"
row whenever the pipeline category is exactly `service auto` (ITP + general
mechanical service, not a parts shop or dezmembrări yard).

- Palette, named for the trade (fixed, do not change): near-black bay
  `#16181D`, hazard red `#E63B2E`, warning amber `#F2A33C`, workshop white
  `#F4F4F2`, concrete grey `#E9E9E5`.
- Typeface pairing: `Oswald` for display headings — its condensed, mechanical
  weight reads like workshop signage/tire branding. `Inter` for body copy and
  CTAs, the same workhorse sans used across the other shells, chosen because
  its neutral geometry doesn't compete with Oswald's density at small sizes.
- Layout concept: keep the proven conversion skeleton, but make the hero feel
  like the front office of a trustworthy neighbourhood ITP station/service
  bay, not a parts counter. Lead with practical trust signals — ITP station
  credibility, transparency about what's wrong before it's fixed, fast
  turnaround (grounded in real review language, e.g. same-day repair) —
  before any service list. The page should sell "hand your keys over with
  confidence," not a catalogue of parts or brands.
- Signature visual element: a reusable **"panou de boxă"** (bay board) —
  small rectangular tags styled like a workshop bay status board: near-black
  fill, a diagonal red or amber corner flag, bold uppercase condensed Oswald
  label (`ITP`, `DIAGNOZĂ`, `FRÂNE`, `ULEI`). Used as quick-service chips in
  the hero and reused as the section-kicker style, so the page is remembered
  as a service bay, not a generic auto site. Reuse this exact motif — corner
  flag + condensed uppercase tag — on every future `service auto` lead.
- Avoid for this shell: a generic auto-parts e-commerce layout (product
  grids, price tags, "add to cart" framing); a dealership-brochure look
  (glossy studio car photography, chrome gradients, brand-partner logos —
  never invent certifications or brand partnerships per the integrity
  rules); and any dark-with-one-accent layout that skips the bay-board motif
  and service-transparency copy — if the page could be reskinned for a
  plumber or locksmith in five minutes by only swapping colors and photos,
  revise before delivery.

| Sector | --c-primary | --c-accent | --c-accent-2 | --c-bg | --c-bg-alt | Display font |
|---|---|---|---|---|---|---|
| Magazin furaje | #123F36 | #D7A72E | #A74232 | #E7EEE8 | #D6E0D8 | Roboto Slab |
| Agri / feed / food producers | #5C1A1A | #C8860A | #E8A020 | #F5ECD7 | #EDE0C4 | Playfair Display |
| Auto (dezmembrări, service, vulcanizare) | #16181D | #E63B2E | #F2A33C | #F4F4F2 | #E9E9E5 | Oswald |
| Construction / trades / metal | #1F2A33 | #E8A020 | #C8860A | #F2F0EB | #E7E4DC | Oswald |
| Carpentry / furniture | #3B2A1D | #B5762A | #D99A45 | #F6F1E8 | #ECE3D4 | Playfair Display |
| Vet / salon / services | #234A3F | #C8860A | #2D6A4F | #F4F1EA | #E9E4D8 | Playfair Display |

Rules carried over from the proven system: page background is never pure
white; primary colour only on dark sections (header, hero, owner strip,
footer, CTA strip); accent never as a large background; no pure black text
(use the template's `--c-text`); button radius ≤ 6px; no gradients on hero;
no parallax, no heavy JavaScript; hover transitions 0.2s only.

## Copy rules (Romanian)

- Correct diacritics everywhere: ă â î ș ț. Test them in the H1.
- Register: formal `dumneavoastră` in body copy; imperative singular on
  buttons ("Scrie pe WhatsApp", "Cere ofertă").
- Hero H1 = business name. Hero subline = one concrete sentence naming the
  locality and the core service. No slogans, no marketing abstractions.
- Services grid: 4–6 cards, each a real service the business plausibly offers
  based on category and reviews. Plain nouns, one-line descriptions.
- "De ce noi" pillars: exactly 3, grounded in verifiable facts (e.g. "Peste
  {N} recenzii de 5 stele pe Google", "În {locality} — aproape de
  dumneavoastră", "Program {hours}").
- Reviews section: only **real Google reviews**, quoted faithfully, max 3,
  author as "Ion M." Never fabricate or embellish a review.

## Call-to-action design (WhatsApp-first)

This pipeline's outreach channel is WhatsApp/Messenger, not phone — the
mockup's CTAs should match that, since the demo is what a prospect opens
after a text message, not a phone call. WhatsApp is the primary button
everywhere (hero, CTA strip, sticky bottom bar, contact section). A phone
number still appears in the footer/contact block for the visitor's own
convenience (some end-customers will want to call the business), but it is
never the leading action in the design.

## Integrity rules (non-negotiable)

- **Never invent claims**: no fictional founding years, certifications,
  guarantees, client counts, or brand partnerships. Every stated fact must be
  verifiable from the listing or reviews. Where a template section needs a
  fact you do not have, use neutral phrasing or delete the element.
- If a free mockup uses an externally supplied logo (see the logo-ownership
  rule above — the builder never generates the logo itself), follow the
  shared logo watermark rule: visible but subtle `DEMO` watermark applied
  with Python's Pillow library before the logo is inserted. Keep the clean
  logo version out of the free mockup; it is reserved for delivery only
  after the client signs.
- If a lead has zero real listing photos, generic atmospheric imagery for the
  trade is acceptable as decorative mood-setting content (for example feed
  sacks, fields, workshop materials, or tools) — this includes the Step 1
  AI-generated hero background image. It must never be captioned or
  implied as the specific business's shop, team, premises, products, proof, or
  customer work. Label it as decorative when a caption is needed, and treat
  this with the same integrity line as fabricated reviews: decorative is fine,
  false specific claims are not.
- The demo must be honest about what it is: the template's footer disclaimer
  ("Propunere de website — demonstrație realizată de {{AGENCY_NAME}}") and the
  `noindex,nofollow` meta stay in every mockup. They are removed only after
  the client signs.
- Host under the agency's demo subdomain (e.g. `demo.{agency}.ro/{slug}` or a
  Netlify URL) — never on a domain containing the prospect's name.
- If the lead is marked `LOST` or goes silent 30 days after last contact,
  take the demo offline.

## QA checklist (run every time)

1. `grep '{{'` returns nothing.
2. Tailwind CDN is present in the head, and layout/spacing/alignment are
   expressed primarily with utility classes instead of bespoke per-lead CSS.
3. Renders correctly at 360px width: sticky bottom bar visible, no horizontal
   scroll, tap targets ≥ 44px.
4. `wa.me` link opens the correct number with the prefilled message;
   `tel:` link (secondary, footer only) dials the correct number.
5. Diacritics render in headings and body.
6. Maps embed points at the correct listing and has a visible `Deschide harta`
   fallback for iframe failure/blocking; map CTA wording is accurate (`Vezi
   harta` / `Deschide harta`, not directions wording unless it really opens
   turn-by-turn directions).
7. All images load; no broken references; page weight sensible (< ~1.5 MB).
8. Desktop and 360px mobile alignment scan passed across header, hero,
   services/products, trust, reviews, contact/map, sticky bar, and footer.
9. Footer disclaimer + noindex meta present.
10. Scroll-triggered reveal fires on every major section below the hero;
    hover states present on every interactive element; both match the timing/
    easing rules above (no bounce/elastic, 200–300ms, ease-out).

## Output

Deliver `mockups/{slug}/index.html` (plus its `logo.png`, `hero.png`,
`assets/`, and `screenshots/` per "Folder structure" above), state the
chosen palette and any facts you could not verify (and therefore omitted),
give the deployment step (push to the mockups repo's `main` branch — GitHub
Pages deploys automatically), and instruct: update the pipeline row to
`status=BUILT` with `mockup_url` set to
`https://calinbotean.github.io/prospector-mockups/mockups/{slug}/`, then run
prospector-outreach.
