---
name: prospector-scan
description: Agent 1 of the Prospector pipeline — finds Romanian businesses that have no website (or only a Facebook/Instagram page) using the Google Places API scanner script. Use this skill whenever the user wants to run a prospect scan, find businesses without websites, search for web design leads, scan a county or locality for offline businesses, or says anything like "run the scanner", "find leads", "scan for prospects", or "caută firme fără site". Also use it to interpret, summarise, or troubleshoot a scan_*.csv output file.
---

# Prospector — Agent 1: Scanner

## Mission
Produce a raw lead file (`scan_YYYY-MM-DD.csv`) of businesses in the target
region that have **no website** or a **social-media-only** presence. This agent
finds; it does not judge. Qualification belongs to Agent 2 (prospector-qualify).

## Primary method — API scan

1. Confirm `GOOGLE_PLACES_API_KEY` is set in the environment. If not, stop and
   give the user the setup steps in the README (Google Cloud project → enable
   **Places API (New)** → create restricted API key).
2. Confirm the input files exist: `data/categories_ro.txt`,
   `data/localities_cluj.txt`, `data/pipeline.csv`.
3. Run:
   ```bash
   python3 scripts/scanner.py \
     --categories data/categories_ro.txt \
     --localities data/localities_cluj.txt \
     --pipeline  data/pipeline.csv \
     --out       data/ \
     --max-pages 1 --max-requests 250
   ```
4. Report back: billable calls used, new leads (split none vs social_only),
   duplicates skipped, and the output path.

## Cost discipline (non-negotiable)

- The field mask includes `websiteUri` and `nationalPhoneNumber`, so every call
  bills at the **Text Search Enterprise SKU** (~USD 35 / 1,000 calls; roughly
  1,000 free calls per month per SKU — verify current figures on the Google
  Maps Platform pricing page before the first run each quarter).
- Default guard is `--max-requests 250` per run. Never exceed ~900 calls in a
  calendar month without the user explicitly confirming they accept billing.
- Rotate the scan grid instead of enlarging it: week 1 = categories 1–5,
  week 2 = categories 6–10, and so on. Depth beats breadth.
- One page (20 results) per query is almost always enough in rural localities.

## Query strategy

- Query format is `"{category} {locality}"` in Romanian, e.g.
  `magazin furaje Gilau`. Diacritics are optional in queries.
- Categories and localities are plain text files, one entry per line, `#` for
  comments. Edit them freely to steer the scan (new sectors, new counties).
- Prioritise owner-operated trade sectors: agri supply, auto services,
  workshops, construction trades, food producers. Avoid regulated or sensitive
  sectors (medical, legal, funeral) unless the user asks.

## Fallback method — manual sweep (no API key)

If no API key is available, do a manual Google Maps sweep instead:
search each `category + locality` pair on Google Maps, and for each result
without a "Website" button record the same columns as the scanner output
(name, locality, address, phone, rating, review count, Maps URL, and whether
a Facebook page exists). Append rows to a `scan_YYYY-MM-DD.csv` with the
identical header so Agent 2 can consume it unchanged. Cap manual sweeps at
~15 minutes per session.

## Data handling rules

- Deduplicate on `place_id` — against the current run and against
  `data/pipeline.csv`. The scanner does this automatically; preserve it if the
  script is ever modified.
- A `websiteUri` pointing at Facebook, Instagram, OLX, Publi24, or linktr.ee is
  a **lead** (`social_only`), not a disqualifier — these owners already believe
  in online presence and convert best, and are the best-fit audience for
  WhatsApp/Messenger outreach specifically (see prospector-outreach).
- Google Maps Platform terms restrict long-term caching of Places content:
  `place_id` may be stored indefinitely; treat other fields as working data and
  refresh them from the live listing before outreach.
- The API returns no email field, in any version — do not expect one and do
  not add fake/placeholder email columns. The outreach channel for this
  pipeline is WhatsApp/Messenger, driven off the phone number this scanner
  already captures.

## Definition of done

A `scan_YYYY-MM-DD.csv` exists in `data/`, a summary has been reported to the
user, and the user has been pointed to Agent 2: "Run prospector-qualify on
this file."
