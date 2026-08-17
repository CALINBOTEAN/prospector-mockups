---
name: prospector-qualify
description: Agent 2 of the Prospector pipeline — scores and filters raw scan results into A/B/C leads and selects the weekly shortlist for mockup building. Use this skill whenever the user wants to qualify leads, score a scan file, pick which businesses to build mockups for, review a scan_*.csv, or says anything like "qualify the leads", "score the scan", "which prospects should we target", or "alege firmele". Always use it before any mockup is built.
---

# Prospector — Agent 2: Qualifier

## Mission
Turn a raw `scan_*.csv` into a ranked shortlist and update
`data/pipeline.csv`. Ruthless filtering here protects the two scarcest
resources downstream: build hours (Agent 3) and outreach attention (Agent 4).

## Hard gates (fail any = discard)

1. `website_status` is `none` or `social_only`.
2. A phone number is present (no phone = no WhatsApp = no outreach channel
   in this pipeline).
3. Not already in `data/pipeline.csv` (check `place_id`).
4. Business appears **active**: rating count > 0 or recent activity visible on
   the Maps listing. If in doubt, mark for manual verification.

## Scoring rubric (apply to every gated lead)

| Signal | Points | Rationale |
|---|---|---|
| Review count ≥ 5 | +3 | Established, real customer base |
| Review count 1–4 | +2 | Trading, less proof |
| Rating ≥ 4.3 | +2 | Quality product — mockup testimonials will be strong |
| Rating 4.0–4.29 | +1 | Acceptable |
| `social_only` (active FB/IG page) | +3 | Owner is already reachable and comfortable on a messaging-style channel — best fit for WhatsApp/Messenger outreach |
| Tier-1 category (agri supply, auto services, workshops, construction trades, food producers) | +3 | Proven fit with the reference projects |
| Tier-2 category (vet, salon, other services) | +1 | Viable but unproven |
| Locality within ~40 km of base (site visit feasible if it gets that far) | +1 | Optional in-person close option |
| Family/personal name in business name | +1 | Owner-operated; decision-maker reachable directly on their own phone |

**Grades:** A = score ≥ 8 → build mockup. B = 5–7 → verify contactability
first, build only if likely reachable. C = < 5 → log as `DORMANT`, do not
spend time.

Note the weighting change from earlier versions of this rubric: `social_only`
is now worth more than a bare `none` status, because the outreach channel is
WhatsApp-first — an owner already active on Facebook/Instagram is more likely
to read and reply to a WhatsApp message than one with zero social presence.

## Weekly shortlist rules

- Select at most **3 A-leads** per week (the WIP limit set by
  prospector-pipeline). Extra A-leads stay `NEW` for next week.
- Prefer sector diversity in the weekly three (do not build three bakeries in
  the same commune — they are each other's competitors and word travels).
- Never shortlist two direct competitors in the same locality in the same
  month.

## Verification pass (mandatory before promoting to QUALIFIED)

For each shortlisted lead:
1. Google `"{name}" {locality}` — confirm no real website exists that Places
   missed (a Wix/WordPress site not linked on Maps is a disqualifier or a
   different pitch entirely).
2. Open the Maps listing — confirm not "Permanently closed"; note opening
   hours, photos available, and copy 2–3 strong review quotes (author first
   name + initial) for Agent 3.
3. Confirm the phone number is a mobile number capable of receiving WhatsApp
   (landline-only numbers cannot be reached by this pipeline's primary
   channel — check the Facebook page for a mobile number instead, or route
   to Messenger as the primary channel for that lead).
4. Optional but recommended: check listafirme.ro / ANAF that the firm is
   active (not radiată).

## Output

1. Append shortlisted leads to `data/pipeline.csv` with `status=QUALIFIED`,
   the computed `score` and `grade`, and today's date in `date_found`.
2. Append B-leads with `status=NEW`, C-leads with `status=DORMANT`.
3. Report to the user: table of the weekly three (name, locality, category,
   score, review count, one-line reason), then hand off: "Run
   prospector-mockup for lead #1."

## Tuning

The rubric weights live only in this file. When monthly metrics (from
prospector-pipeline) show a segment over- or under-performing, adjust the
weights here and note the change and date at the bottom of this file.
