# Prospector — Status (read this first, every session)

This file is a snapshot, not a log — it gets **overwritten** at the end of
every session (or the moment Calin says he has to go) with a fresh
"Where we left off" and "Next session starts here." It never accumulates;
that's what CLAUDE.md's "Session log" section is for. If you want the full
history of a decision, look there. If you just want to know what to do
right now, this file is enough on its own — Calin should never have to
paste anything to continue.

---

**Last updated:** 2026-08-17 (end of session)

## Where we left off

- **First outreach is done.** The WhatsApp number switch to +40 741 181 795
  is complete and verified everywhere. Calin sent Template 1 (first
  contact) by hand, via WhatsApp, to all three built leads:
  - **Depozit Cherestea Vâlcele** (0747 470 637) — sent, no reply yet.
  - **Agrofarm Marius** (0770 202 324) — sent, **replied same-day**: "Ma uit
    consult si daca doresc revin multumesc" (will look it over, consult,
    come back if interested). Soft-positive, not a rejection, not yet a
    meeting ask. No call made or offered — per house rules a call is now an
    allowed next step for this lead only if *they* initiate or invite one.
  - **Sabo ITP & SERVICE** (0756 221 704) — sent, no reply yet.
  - All three logged in `data/pipeline.csv`: `status=CONTACTED`,
    `date_contacted=2026-08-17`, `next_action_date=2026-08-20` (the
    Template 2 / +3 day follow-up window).
  - Pilot count: **3 of ~30** Offer A first contacts done (see CLAUDE.md's
    "Current phase — PILOT" section).
- **Fixed a real privacy gap.** `data/pipeline.csv` (lead names, phone
  numbers, outreach notes) had been silently tracked in this *public* repo
  since before its `.gitignore` rule existed, and was being served live and
  directly downloadable via GitHub Pages. Untracked it properly
  (`git rm --cached`, kept on disk) and confirmed the URL now 404s. Full
  detail and the lesson (a `.gitignore` rule alone doesn't untrack an
  already-committed file) is in CLAUDE.md's session log, 2026-08-17.
- **GitHub had a multi-hour outage tonight** (confirmed via
  githubstatus.com, roughly 13:40–19:00 UTC) that broke the "Deploy static
  content to Pages" workflow for several pushes in a row — not a repo
  problem, nothing needed to change in the workflow file or settings. The
  three live mockups stayed up (200 OK) throughout every failed deploy
  regardless. Retried until it succeeded; confirmed working by end of
  session.
- Everything from tonight is committed and pushed to `main` (latest commit
  `dd225a3` — a successful Pages deploy — at end of session; check
  `git log` if this file is stale).

## Next session starts here

1. **Check for replies** on Depozit and Sabo — nothing needed if they've
   replied; if still silent by **2026-08-20**, that's the Template 2
   follow-up date logged in `data/pipeline.csv` for all three leads
   (including Agrofarm, as a safety net in case they don't come back on
   their own as promised).
2. If Agrofarm circles back first, read `skills/prospector-outreach/prospector-outreach.md`'s
   objection-handling section before replying — stay text-only unless
   Agrofarm invites a call.
3. Otherwise, resume the normal weekly rhythm: read
   `skills/prospector-pipeline/prospector-pipeline.md`'s session-start gate
   for what's due and current WIP status. No new mockups need building
   right now — all three built leads are already contacted.

## Open items / need Calin's input

- None blocking right now.

## Standing rule for whoever is reading this (Claude Code / Codex / Cowork)

At the end of a session — or the moment Calin says he needs to go —
rewrite this file (not CLAUDE.md's session log, this one) with a current
"Where we left off" and "Next session starts here" before ending. This is
what lets Calin open a brand-new chat, paste nothing, and continue exactly
where things stopped.
