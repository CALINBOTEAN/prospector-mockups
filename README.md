# PROSPECTOR — Mockup-First Web Prospecting System (WhatsApp-first, text-only)

Finds Romanian businesses with no website (or Facebook-only presence),
qualifies them, builds each a single-page demo website, and manages
WhatsApp/Messenger outreach that converts demos into paying clients. Four
single-purpose agents, one ledger, weekly rhythm. **No phone calls anywhere
in this pipeline** — outreach is entirely text-based, by design.

## Contents

```
prospector/
├── README.md                     ← this file
├── scripts/
│   └── scanner.py                ← Agent 1 executable (Google Places API New)
├── data/
│   ├── categories_ro.txt         ← scan grid: sectors (editable)
│   ├── localities_cluj.txt       ← scan grid: localities (editable)
│   └── pipeline.csv              ← system of record (append-only ledger)
└── skills/
    ├── prospector-pipeline/      ← Orchestrator: states, rhythm, WIP, metrics
    ├── prospector-scan/          ← Agent 1: find
    ├── prospector-qualify/       ← Agent 2: score + shortlist
    ├── prospector-mockup/        ← Agent 3: build (WhatsApp-primary CTAs, incl. template.html)
    └── prospector-outreach/      ← Agent 4: WhatsApp/Messenger scripts + follow-ups
```

## One-time setup

1. **Google Cloud** — create a project → enable **Places API (New)** → create
   an API key → restrict it to Places API (New). Set a budget alert at a low
   figure (e.g. USD 10). Note: the API returns phone numbers, never email —
   this pipeline is built around that constraint rather than around email.
2. **API key** — on the machine running scans:
   `export GOOGLE_PLACES_API_KEY="..."` (or add to shell profile).
3. **Install the skills** — in Claude: Settings → Capabilities → Skills →
   upload each `.skill` file from `dist/`. Alternatively, in Claude Code,
   place the folders under `~/.claude/skills/`.
4. **Configure identity constants** — agency name, WhatsApp business number,
   demo subdomain, and price range are referenced by Agents 3 and 4; set them
   once in a note at the top of `data/pipeline.csv` or in your project
   instructions.
5. **First run** — say "start a prospector session"; the orchestrator gate
   takes over.

## Weekly operating rhythm

Mon scan (30 min) → Tue qualify, pick 3 (45 min) → Wed–Thu build ≤ 3 mockups →
Fri first contacts via WhatsApp/Messenger, manual, ≤ 5/day → daily 10-minute
follow-up check. Capacity at this cadence: ~12 mockups/month.

## Channel choice and its trade-off

This pipeline deliberately excludes phone calls. That removes the highest-
trust, highest-conversion channel in exchange for speed and lower personal
friction. Expect reply rates below general B2B cold-email benchmarks
(roughly 3–6% for well-targeted audiences) until your own numbers say
otherwise — the segment (no-website businesses) is defined by low digital-
adoption, and WhatsApp's higher open rate only partially offsets that.
Track reply rate from message 1 and treat sub-10% after 30 contacts as a
signal to fix targeting/messaging before adding volume (see
prospector-pipeline's monthly review).

## Cost model (verify quarterly)

The scanner requests `websiteUri`/phone/rating, billing every Text Search call
at the **Enterprise SKU**: as of mid-2026, roughly USD 35 per 1,000 calls with
approximately 1,000 free calls per month per SKU (Google replaced the pooled
USD 200 credit with per-SKU free tiers in March 2025). The default guard of
250 calls per run × 4 runs per month sits inside the free tier. Confirm
current figures at https://mapsplatform.google.com/pricing/ before scaling.

## Compliance summary

- WhatsApp-first, text-only outreach; no phone calls anywhere. Written first
  contacts always include an opt-out; no bulk sending, no WhatsApp
  automation (Law 506/2004 + WhatsApp ToS).
- Demos carry a visible disclaimer + `noindex`; hosted on the agency's demo
  subdomain; taken down 30 days after a lead is lost.
- Mockup copy states only verifiable facts; testimonials are real Google
  reviews quoted faithfully.
- Google Places content: retain `place_id` long-term; refresh other fields
  from the live listing before use.
