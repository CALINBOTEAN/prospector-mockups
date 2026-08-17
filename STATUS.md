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

- All three mockups built so far are **BUILT, live, and on the same
  standing architecture** (full-bleed hero + neutral scrim, services
  carousel, scroll-reveal, sticky mobile bar): Depozit Cherestea Vâlcele,
  Agrofarm Marius, Sabo ITP & SERVICE. **None has been contacted yet.**
- Live URLs:
  - https://calinbotean.github.io/prospector-mockups/mockups/depozit-cherestea-valcele/
  - https://calinbotean.github.io/prospector-mockups/mockups/agrofarm-marius/
  - https://calinbotean.github.io/prospector-mockups/mockups/sabo-itp-service/
- The standing mockup template (`skills/prospector-mockup/assets/template.html`)
  was rewritten today to match Depozit's proven architecture, and
  `prospector-mockup.md` now documents it as mandatory (hero-scrim color
  rule, dark-logo contrast check, the Tailwind RGB-triplet opacity
  pitfall, the services carousel as a reusable component). The next new
  lead's mockup should need far less iteration than these three did.
- A new `romanian-copywriting-style.md` guide now governs mockup copy —
  read it before writing any Romanian copy, it replaced the old rules that
  were producing AI-sounding, templated text.
- Repo housekeeping done: fixed a corrupted (UTF-16) `.gitignore`,
  completed a half-finished skills-file rename (`SKILL.md` →
  `prospector-*.md`), untracked personal Claude Code settings that had no
  business being in a publicly-deployed repo.
- Everything above is committed and pushed to `main` (latest commit
  `47d3e28` at end of session — check `git log` if this file is stale).

## Next session starts here

1. **Switch WhatsApp outreach to the Romanian number** (see "Later" in
   CLAUDE.md for the how — dual-SIM/eSIM/temporary swap for the one-time
   WhatsApp Business verification step, same phone is fine).
2. **Send the first outreach messages** for Depozit, Agrofarm, and Sabo.
   Read `skills/prospector-outreach/prospector-outreach.md` first — this
   pipeline is WhatsApp-first, text-only, no cold calls.
3. Then resume the normal weekly rhythm: read
   `skills/prospector-pipeline/prospector-pipeline.md`'s session-start
   gate for what's due and the current WIP status.

## Open items / need Calin's input

- None blocking right now.

## Standing rule for whoever is reading this (Claude Code / Codex / Cowork)

At the end of a session — or the moment Calin says he needs to go —
rewrite this file (not CLAUDE.md's session log, this one) with a current
"Where we left off" and "Next session starts here" before ending. This is
what lets Calin open a brand-new chat, paste nothing, and continue exactly
where things stopped.
