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

## Build procedure

1. Copy `assets/template.html` to a working file named `{slug}.html`
   (slug = lowercase business name, hyphens, no diacritics).
2. Load Tailwind CSS by CDN in the page head, after Google Fonts and before
   the custom `<style>` block. No build step, account, package install, or
   framework setup is needed.
3. Pick the sector palette from the table below and replace the `:root`
   palette block (the template marks it clearly).
4. Replace every `{{TOKEN}}` in the file. Then verify none remain:
   `grep -o '{{[A-Z_0-9]*}}' {slug}.html` must return nothing.
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

If a free mockup uses a newly generated logo, apply a visible `DEMO` watermark
to the logo asset with Python's Pillow library before inserting it in the page.
The watermark must stay visible, but make it visually restrained: prefer a
small corner ribbon or reduced-opacity stamp. Never remove it from a free
mockup, and never make it so heavy-handed that the logo looks ugly or unusable.

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
- If a free mockup uses a newly generated logo, follow the shared logo
  watermark rule above: visible but subtle `DEMO` watermark applied with
  Python's Pillow library before the logo is inserted. Keep the clean logo
  version out of the free mockup; it is reserved for delivery only after the
  client signs.
- If a lead has zero real listing photos, generic atmospheric imagery for the
  trade is acceptable as decorative mood-setting content (for example feed
  sacks, fields, workshop materials, or tools). It must never be captioned or
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

## Output

Deliver `{slug}.html`, state the chosen palette and any facts you could not
verify (and therefore omitted), give the deployment step (drag the file into
Netlify Drop or upload to the demo subdomain), and instruct: update the
pipeline row to `status=BUILT` with the `mockup_url`, then run
prospector-outreach.
