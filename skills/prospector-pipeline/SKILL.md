---
name: prospector-pipeline
description: Orchestrator of the Prospector system — owns the pipeline ledger, statuses, weekly rhythm, WIP limits, and metrics for the "find Romanian businesses without websites and approach them with a mockup" project. Use this skill at the START of every Prospector work session, whenever the user asks about pipeline status, what to do next, follow-ups due today, weekly review, conversion metrics, or says anything like "prospector status", "what's due", "start prospecting session", or "unde suntem cu prospectarea". Read this before invoking any other prospector-* skill.
---

# Prospector — Orchestrator

## Mission
One business at a time moves through five states, worked by four specialised
agents. This skill keeps the system honest: correct state, correct sequence,
capped work-in-progress, measured results. Outreach in this system is
WhatsApp-first and text-only — no phone calls at any stage.

## Session-start gate (mandatory, before any other action)

1. Open `data/pipeline.csv`.
2. Report counts per `status`.
3. List every row whose `next_action_date` is today or overdue.
4. State which weekly stage today corresponds to (see rhythm below).
5. Await the user's confirmation of today's focus. Only then invoke the
   relevant agent skill.

## The agents

| # | Skill | Does one thing | Automation |
|---|---|---|---|
| 1 | prospector-scan | Finds businesses without websites | Script (fully automated) |
| 2 | prospector-qualify | Scores and shortlists | Claude, rubric-driven |
| 3 | prospector-mockup | Builds the demo site (WhatsApp-primary CTAs) | Claude + template, human QA |
| 4 | prospector-outreach | Prepares WhatsApp/Messenger contact and follow-ups | Claude drafts, human sends |

Each agent reads and writes only its own stage. Never let one session blur
stages (e.g. do not start building during a qualification session).

## Statuses and allowed transitions

`NEW → QUALIFIED → BUILDING → BUILT → CONTACTED → FOLLOWUP_1 → FOLLOWUP_2 →
MEETING → WON | LOST | DORMANT`

- `DORMANT` leads may be re-scored after 6 months.
- `LOST` triggers demo takedown (Agent 3 rule); one re-approach after 6 months.
- No status may be skipped except `MEETING → WON`.

## Weekly rhythm

| Day | Stage | Budget |
|---|---|---|
| Monday | Agent 1 scan (rotating category batch) | 30 min |
| Tuesday | Agent 2 qualify → pick weekly three | 45 min |
| Wed–Thu | Agent 3 build ≤ 3 mockups + deploy | 60–90 min each |
| Friday | Agent 4 first contacts (WhatsApp/Messenger) | 45 min |
| Daily | Orchestrator: follow-ups due | 10 min |

## WIP limits (hard)

- ≤ 3 leads in `BUILDING`/`BUILT` per week.
- ≤ 10 leads total in `CONTACTED`/`FOLLOWUP_*`.
- ≤ 5 first contacts per day (also an Agent 4 legal/platform rule).
- If a limit is hit, the correct move is to work follow-ups, not to add leads.

## The ledger — `data/pipeline.csv` (system of record)

Columns: `place_id, name, category, locality, phone, maps_url, social_url,
website_status, rating, review_count, score, grade, status, mockup_url,
date_found, date_contacted, next_action_date, notes`.

Rules: append-only for new leads; edits only via status transitions; back up
the file weekly (dated copy); the CSV outranks memory — if conversation and
CSV disagree, the CSV wins.

## Monthly review (first session of the month)

Compute and log at the bottom of this file:
- Scans → leads found; leads → A-grade rate
- Contacted → replied %; replied → meeting %; meeting → won %
- Billable API calls used vs free tier
- One decision: what to change in the qualify rubric, the mockup, or the
  message templates. Change exactly one variable per month.

**Kill/fix criterion:** because this pipeline deliberately chose text-only
outreach over phone calls, watch reply rate closely from week one — it is
the variable most exposed by that choice. If reply rate sits below ~10%
after 30 first contacts, the first fix to try is targeting or message
personalization, not volume; if it still doesn't move, revisit whether
WhatsApp alone is sufficient for this segment or whether a channel like a
phone call needs to be reconsidered for follow-up only. If meetings do not
convert to clients, fix pricing/positioning before building more.

## Scaling path (only after the machine converts)

1. Expand localities file to neighbouring counties (Sălaj, Bistrița, Alba).
2. Raise WIP to 5 builds/week only if follow-up discipline held for 4 weeks.
3. Move the scanner to a weekly cron job (Claude Code on the workstation) so
   Monday's stage becomes "read the report" instead of "run the scan".
