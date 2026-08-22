# Prospector — Status (read this first, every session)

This is a snapshot, not a log. It is overwritten at the end of every
session; `CLAUDE.md` holds the detailed history and lessons.

---

**Last updated:** 2026-08-20 (later same day — Cowork session, wedding-venue scan + hedge pick)

## Where we left off

- **This week's build queue is now finalized (3 leads, all `QUALIFIED`):**
  1. **Cabana lui Ianis** (Valea Ierii) — vacation rental, pipeline-validation
     build #1. First target for the automated batch pipeline's mandatory
     first-run-of-1 test.
  2. **Casa Pleșa** (Rasca) — vacation rental, pipeline-validation build #2.
  3. **La Foret** (Florești Cluj, LA FORET EVENTS SRL, CUI 48536128) —
     wedding venue, this week's hedge-slot lead (swapped from construction
     to wedding venues per Calin's explicit call). 376 reviews, 4.9 rating,
     social_only (Facebook + wedding-directory listings, no independent
     site). Verified as a genuine, active, legitimately registered firm.
  - Casa Eden, Pensiunea Larix, Cabana Trofeul Munților remain `QUALIFIED`
    but HELD until the pipeline is proven on the validation pair (unchanged
    from earlier today).
  - Confecții Metalice Cluj and BUSU Building Cluj remain `QUALIFIED`,
    deferred — no longer this week's hedge pick, but not abandoned.
- **Wedding-venue scan run this session** (Calin supplied the Google Places
  API key directly into this Cowork session; it was not stored anywhere).
  60 billable calls (`sala evenimente` / `sala nunti` / `domeniu evenimente`
  × the existing 20 Cluj-county localities) →
  `data/scan_wedding_2026-08-20.csv`, 72 raw leads (56 no-website, 16
  social-only), 97 had real websites, 1 already in pipeline. Qualified: 49
  passed the gates (44 A / 5 B), 2 discarded to `DORMANT` under the
  low-engagement gate. **Lesson for future wedding-venue scans:** these
  query terms pulled a lot of noise — generic restaurants, bars, and even
  a balloon-decoration shop matched the text search. Had to manually
  cross-check the `types` field and business name for genuine venue fit
  before trusting the top-scored results; worth tightening the query terms
  or adding a stricter `types` filter next time this category is scanned.
- **Important catch during verification:** the top-scoring wedding-venue
  lead by review count, **Vararea Events** (Florești), was disqualified
  after a web search turned up Gazeta de Cluj coverage reporting it
  operates without authorization and that Florești city hall is trying to
  demolish it, allegedly run in the shadows by a local police officer.
  Logged in `data/pipeline.csv` as `DORMANT`/grade `DQ` with a **DO NOT
  CONTACT** note, so it can't get re-selected by a future qualify pass on
  this category. This is exactly the kind of catch the mandatory
  verification pass exists for (same pattern as the SANTECHSTEEL/Instalis
  false-positive catch from the 2026-08-17 session).
- **Outreach timing confirmed:** send as soon as builds are ready, not
  holding for September, per Calin's explicit call (overriding Grok's
  seasonality caution).
- **Blocking item unchanged:** `reference-library.md` still has zero
  filled-in references, and now needs design/motion direction for **two**
  categories (vacation rental + wedding venue) before any of this week's
  three builds can start. Calin is sourcing reference websites to send.
- Everything else unchanged: Sabo Template 2 sent, Template 3 window
  2026-08-27; Agrofarm untouched; Depozit closed `LOST`; AVA follow-up
  window 2026-08-21.

## Next session starts here

1. **Waiting on Calin:** reference website(s) — now needed for both vacation
   rentals and wedding venues before `prospector-mockup` can start on any
   of the three queued leads.
2. Once references exist and Calin gives the explicit trigger phrase, run
   the Automated batch pipeline pre-flight — target is 1 lead
   (first-run-of-1 rule), starting with **Cabana lui Ianis** (not Casa
   Eden, not La Foret — the validation pair leads first).
3. **2026-08-21:** check AVA for a reply to the offer.
4. **2026-08-27:** Sabo's Template 3 window, if still silent.
5. Do not message Agrofarm unless Calin explicitly says so, or Agrofarm
   replies again first.
6. Do not contact Vararea Events, ever — see disqualification note above.

## Open items / need Calin's input

- Reference website(s) for both category shells (vacation rental, wedding
  venue).
- Optional: rotate the Google Places API key (transited this Cowork chat
  twice now — 2026-08-18 and 2026-08-20 — restricted to Places API (New),
  limited exposure, but worth rotating given repeat exposure).

## Standing rule

At the end of a session, rewrite this file with a current "Where we left
off" and "Next session starts here" so the next chat can continue without
recovering context manually.
