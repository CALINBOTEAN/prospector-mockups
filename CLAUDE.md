> Keep this file identical to `AGENTS.md` — apply every edit to both files in the same turn.

# Prospector — Project Instructions

This project runs the Prospector pipeline: finding Cluj-area businesses,
building them demo assets, and managing WhatsApp-first, text-first outreach.
No cold calls anywhere in this system — first contact and all outreach to a
lead that hasn't engaged yet stays text-only. Once a lead has replied
positively on WhatsApp, a phone call from that point forward is a normal,
allowed next step, not an exception to apologize for.

## Always start here

At the start of every session, read `skills/prospector-pipeline/SKILL.md`
first and follow its session-start gate: open `data/pipeline.csv`, report
status counts, list anything due today, and confirm today's focus before
doing anything else.

## Two offers, one ledger

- **Offer A** (`skills/prospector-scan`, `prospector-qualify`,
  `prospector-mockup`, `prospector-outreach`): no-website businesses, free
  mockup site, WhatsApp outreach.
- **Offer B** (`skills/prospector-gbp`): Google Business Profile audit +
  optimisation retainer, for businesses with web presence that underperform
  in the Local Pack.
- Both share `data/pipeline.csv`. The `offer` column (`A` or `B`) on each row
  says which track that lead belongs to — never let a lead qualify for both.

## Current phase — PILOT (read this before running Offer B)

Offer A is in its pilot: the first ~30 first contacts, run at the normal
weekly rhythm and WIP limits in prospector-pipeline. Offer B
(`prospector-gbp`) is built and ready, but should only run at token scale —
about 1 lead/week — until Offer A's pilot produces real reply-rate and
close-rate numbers. Do not scale Offer B to full weekly capacity, and do not
let combined weekly builds across both offers exceed the WIP limits in
prospector-pipeline, until the pilot review says otherwise.

**When the pilot review happens:** after 30 Offer A first contacts, or after
4 weeks, whichever comes first. At that point, revisit this file and update
this section with the actual numbers and the decision on scaling Offer B.

## Phase 2 — sector expansion (not yet)

At the pilot review, revisit whether to add non-trade categories (e.g. salons,
personal care) to `data/categories_ro.txt`. Do not expand the category list
before then — wait until Offer A conversion data exists so the decision is
based on real reply/close numbers, not a guess.

## Offer C — vacation rentals (idea, not built)

Not started. A future category to test later, not a new offer track to
build in parallel with A and B right now.

Businesses on Booking.com/Airbnb with high occupancy but no direct-booking
website of their own are a strong lead category — they're already proven to
convert bookings, but lose money to OTA commissions, last-minute
cancellations, and have no direct guest relationship.

No new API needed — this reuses the existing Places API scanner. When ready
to test this, add `cabana`, `pensiune agroturistica`, `casa de vacanta` to
`data/categories_ro.txt`, along with relevant mountain-area localities (not
yet in the current Cluj-area locality list).

## Flagged for pilot review (not implemented — do not act on these yet)

Outside critique received 2026-08-14, not acted on. Captured here so it
isn't lost, and to be weighed at the pilot review alongside the actual
reply/close numbers — none of the below should be implemented before then:

- Consider a paid diagnostic/audit-first model instead of a free mockup as
  the primary Offer A hook, if reply rates underperform.
- Consider raising the retainer price floor above the current €25–40/month
  range (see `skills/prospector-gbp/SKILL.md`) once there are 2–3 real case
  studies to justify it.
- Consider adding a light negative or neutral rubric weight in
  `prospector-qualify` for categories that are already heavily represented
  in the pipeline, to avoid over-concentrating in one sector.

## Later

- WhatsApp outreach currently uses a UK number as a stopgap. Set up WhatsApp
  Business on the Romanian number before scaling outreach volume — same
  phone is fine (regular WhatsApp + WhatsApp Business can coexist as
  separate apps), the Romanian number just needs to be usable on that phone
  during the one-time verification step (dual-SIM, eSIM, or a temporary SIM
  swap). Once that's done, replace the UK number in agency contact details
  with the Romanian one.
- Sector expansion (salons, personal care, other non-trade categories) was
  raised and deliberately deferred — revisit adding them to
  `data/categories_ro.txt` at the pilot review, once Offer A conversion data
  exists. (Full detail in "Phase 2 — sector expansion" above.)

## Google Cloud console — org gotcha (read before touching billing/APIs)

This Google account has two separate org contexts: `calinbotean-work-org`
and `No organization`. The PROSPECTOR project (`prospector-505411`) and its
billing account both live under `No organization`.

Always use this direct URL, never the generic `console.cloud.google.com`
(which defaults to the wrong org and will show an empty/unrelated project
list, or the wrong Google account entirely):

```
https://console.cloud.google.com/home/dashboard?project=prospector-505411
```

This was misdiagnosed once already (2026-08-14 session) as a billing
problem when it was actually an org/account mismatch — checked the wrong
org, then the wrong Google account, before finding PROSPECTOR under
`calinbotean.work` / `No organization`. Check this note first next time
billing or API access looks broken.

## House rules (apply regardless of offer)

- WhatsApp/Messenger first, text-only for every lead that hasn't engaged
  yet. No cold calls, no cold-call scripts, ever. Once a lead has replied
  positively on WhatsApp, a phone call from that point forward is fine and
  can be a natural next step — the ban is on cold calling, not on calls in
  general.
- Every ledger update happens in `data/pipeline.csv` directly — it is the
  source of truth, not the conversation.
- No bulk sending, no outreach automation. Every message is drafted here and
  sent by hand.
- Do not set `ANTHROPIC_API_KEY` in this environment — Claude Code should
  authenticate with the Pro subscription login, not API billing.
