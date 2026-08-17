> Keep this file identical to `AGENTS.md` — apply every edit to both files in the same turn.

# Prospector — Project Instructions

This project runs the Prospector pipeline: finding Cluj-area businesses,
building them demo assets, and managing WhatsApp-first, text-first outreach.
No cold calls anywhere in this system — first contact and all outreach to a
lead that hasn't engaged yet stays text-only. Once a lead has replied
positively on WhatsApp, a phone call from that point forward is a normal,
allowed next step, not an exception to apologize for.

## Always start here

At the start of every session, read `STATUS.md` first — it is a short,
always-current snapshot of where the last session left off and what to do
next, overwritten (not appended to) at the end of every session. Then read
`skills/prospector-pipeline/prospector-pipeline.md` and follow its
session-start gate: open `data/pipeline.csv`, report status counts, list
anything due today, and confirm today's focus before doing anything else.

**End every session by rewriting `STATUS.md`** (not this file's session
log below) with a fresh "Where we left off" / "Next session starts here" —
the moment Calin says he needs to go, or naturally at a stopping point.
This is what lets him open a brand-new chat and continue without pasting
anything.

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
  range (see `skills/prospector-gbp/prospector-gbp.md`) once there are 2–3 real case
  studies to justify it.
- Consider adding a light negative or neutral rubric weight in
  `prospector-qualify` for categories that are already heavily represented
  in the pipeline, to avoid over-concentrating in one sector.

## Later

- **Next session priority (set 2026-08-17):** switch WhatsApp outreach from
  the UK stopgap number to the Romanian number, then send the first
  outreach messages — Depozit Cherestea Vâlcele, Agrofarm Marius, and Sabo
  ITP & SERVICE are all BUILT, live, and design/copy-approved (see session
  log below); none has been contacted yet. Read
  `skills/prospector-outreach/prospector-outreach.md` for the WhatsApp-first,
  text-only script before sending anything.
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

## Deploying changes from a Cowork session (PowerShell)

Cowork sessions reach this repo only through the desktop bridge: file
read/write, no shell, no network, no git. A Cowork session cannot commit or
push. When a Cowork session says changes are staged and ready, finish the
deploy locally in PowerShell:

```powershell
cd "C:\Users\calin\OneDrive\Desktop\PROSPECTOR\prospector"
git status
git commit -m "<message the session gave you>"
git push
```

GitHub Pages deploys `main` automatically — no separate build/deploy step.

**Known gotcha:** the desktop bridge can rename files but cannot delete
them (no `unlink` permission on the mount). Git locks (`.git/index.lock`)
briefly created during `git add`/`git status` from a Cowork session can be
left behind because of this — the session moves any stray lock it creates
into a `_to_delete/` folder at the repo root instead of removing it. If any
git command errors with `Unable to create '.git/index.lock': File exists`,
check `_to_delete/` first, delete the real `.git\index.lock` yourself, then
retry.

## Session log

Most recent first. Add a new dated entry at the end of any session with
meaningful progress or a real discovered issue — a few lines, key lessons
only, not a full transcript.

- **2026-08-17** — Switched agency WhatsApp outreach from the UK stopgap
  number (+44 7577 464619) to the Romanian number (+40 741 181 795) across
  all three live mockups, two stray experiment HTML files, and disclaimer
  text; verified zero remaining references repo-wide. Sent the first three
  Offer A outreach messages (Template 1, WhatsApp, by hand) to Depozit
  Cherestea Vâlcele, Agrofarm Marius, and Sabo ITP & SERVICE — Agrofarm
  replied same-day ("Ma uit consult si daca doresc revin multumesc" —
  soft-positive holding reply, not yet a meeting ask); Depozit and Sabo
  silent so far. Logged all three in `data/pipeline.csv` as CONTACTED,
  `date_contacted`=2026-08-17, `next_action_date`=2026-08-20 (Template 2
  follow-up window). Pilot count: 3 of ~30 first contacts done.
- **2026-08-17** — Found and fixed a real privacy gap: `data/pipeline.csv`
  (lead names, phone numbers, outreach notes) had been committed to this
  *public* repo once, before the `.gitignore` rule for it existed — that
  rule only blocks brand-new files, it does not retroactively untrack a
  file already committed, so it had kept being tracked and re-uploaded on
  every push since. Because the Pages workflow uploads the whole repo as
  the site (`path: '.'`), the leads file was being served live and directly
  downloadable at
  `https://calinbotean.github.io/prospector-mockups/data/pipeline.csv` —
  confirmed by fetching it. Fixed with `git rm --cached data/pipeline.csv`
  (kept on disk, stopped tracking going forward) and pushed; re-confirmed
  the URL now 404s. **Lesson: adding a `.gitignore` rule for a file that
  was already committed does nothing by itself — it also needs
  `git rm --cached`, or it silently keeps shipping every push.** Per the
  2026-08-14 decision, old copies possibly still in repo history were not
  scrubbed, only stopped from continuing.
- **2026-08-17** — Diagnosed a "Deploy static content to Pages" workflow
  failure Calin got emailed about as a live, ongoing GitHub-wide outage
  (confirmed via githubstatus.com: Actions/API/Webhooks/PRs/Issues all
  degraded, incident ran roughly 13:40–19:00 UTC that day), not a repo
  problem — workflow YAML, permissions, and Pages source were all
  unaffected; `codeload.github.com` and GitHub's own Pages deployment API
  were returning 502/503 mid-run. The three live mockups stayed up (200 OK)
  through every failed deploy, since Pages keeps serving the last
  successful build regardless of a failed one. Retried via empty commits as
  GitHub's status page showed progressive mitigation; the 5th retry
  succeeded. No `gh` CLI is installed on this machine — used the public
  GitHub REST API (unauthenticated, works fine for public repos) plus the
  in-app browser against the Actions UI as a fallback when the API itself
  was rate-limited/timing out from the same outage.
- **2026-08-17** — Diagnosed the reported 404s on Agrofarm Marius and Sabo
  ITP & SERVICE: from the Cowork cloud sandbox, all three live mockup URLs
  (`https://calinbotean.github.io/prospector-mockups/mockups/<slug>/`)
  return 200 right now; only legacy/incorrect forms (`.html`-suffixed paths,
  or the slug at the repo root instead of under `mockups/`) 404. Likely a
  stale/incorrect link on Calin's side rather than a live deploy problem --
  flagged for him to confirm the exact URL he used. Corrected a
  ledger/reality mismatch found while checking this: `data/pipeline.csv`
  still listed Depozit Cherestea Vâlcele as QUALIFIED with no `mockup_url`,
  even though the mockup was already built and live in
  `mockups/depozit-cherestea-valcele/` -- updated to BUILT with the live
  URL and a dated note; `next_action_date` cleared pending the design
  revision Calin is about to request. Diagnosed the "sounds very AI"
  complaint about mockup copy: the old `## Copy rules (Romanian)` section in
  `skills/prospector-mockup/prospector-mockup.md` mandated blanket formal
  `dumneavoastră` and an identical rating/address/hours "De ce noi" triad on
  every build, producing near-interchangeable copy across three unrelated
  businesses, plus calqued English section headers ("semne clare",
  "cuvântul clientului"). Wrote
  `skills/prospector-mockup/romanian-copywriting-style.md` (grounded in the
  actual flagged lines from all three live mockups) and updated the copy
  rules section to point to it instead of mandating the fixed formula. Also
  confirmed `mcp__remote-devices__device_bash` gives a live read-write mount
  of this repo (not just the older stage/commit-file bridge) -- `git
  status`/`diff`/`log` and direct file edits work straight from a Cowork
  session now, though push still needs no network and stays a
  PowerShell/local step; the known `.git/index.lock` gotcha still applies
  the same way (move it into `_to_delete/`, don't try to delete it).

- **2026-08-16** — Discovered the desktop bridge used by Cowork sessions can rename files but not delete them (no unlink permission on the mount). Running `git add`/`git status` through it leaves a stale `.git/index.lock` behind after every call, which would block all local git commands until removed. Fix pattern going forward: Cowork sessions move any stray lock into `_to_delete/` instead of trying to delete it, and hand off `git commit`/`git push` to PowerShell locally — see "Deploying changes from a Cowork session (PowerShell)" above.
- **2026-08-16** — Added the standing three-step, stop-after-each-step mockup build process (image-generation prompts → structural reference → full build) and a standalone scroll-reveal/hover-state rule to `skills/prospector-mockup/prospector-mockup.md`. While verifying the update, found `skills/prospector-mockup/SKILL.md` only exists inside the stale `skills.zip` bundle (2026-08-06 snapshot, missing weeks of accumulated fixes) — the live skill files on disk are all named `<foldername>.md`, not `SKILL.md`. Rebuilt `skills.zip` from the current on-disk files and fixed the stale `SKILL.md` filename references in this file (session-start gate, GBP pricing note, Jekyll note).
- **2026-08-14** — Hero-lockup alignment bug on the Sabo ITP & SERVICE
  mockup: after switching `hero-lockup`'s `align-items` from `center` to
  `flex-start` so the logo/H1/subline/buttons would left-align, the kicker
  span stayed centered because it had its own `margin: 0 auto`, which
  silently overrides a parent's `align-items`. Lesson generalized into
  `skills/prospector-mockup/prospector-mockup.md`'s shared rules and baked
  into `skills/prospector-mockup/assets/template.html`'s hero-lockup as the
  default: alignment must be controlled only by the parent container, never
  by a child's own margin/auto-centering rule.
- **2026-08-14** — Fixed the Google Cloud org-mismatch issue: the
  PROSPECTOR project lives under "No organization", not
  `calinbotean-work-org` — use the direct project URL going forward (see
  "Google Cloud console — org gotcha" above). Learned GitHub Pages needs
  either a `.nojekyll` file or a plain static-deploy Actions workflow, not
  "Deploy from a branch" with Jekyll — Jekyll processing breaks on
  `{{TOKEN}}` placeholders in skill `.md` files. WhatsApp outreach still on
  the UK number as a stopgap; Romanian number migration still pending (see
  "Later" above). `data/pipeline.csv` briefly existed in the public GitHub
  repo's commit history before `.gitignore` was added — decision was to
  leave it as-is, not scrub history.
- **2026-08-17** — Revised only the Depozit Cherestea Vâlcele hero: removed
  the opaque text card, added a left-side legibility scrim plus local
  text/button shadows, and increased the mobile hero height while shifting
  the crop right to retain the lumber stacks. The browser QA surface blocks
  direct local-file URLs, so its required desktop/mobile page screenshots
  remain pending a permitted local-page rendering route.
- **2026-08-17** — Increased the Depozit Cherestea Vâlcele hero logo from
  92/112px to 112/132px (mobile/desktop) and set the main heading into an
  explicit two-line lockup, with VÂLCELE centered beneath DEPOZIT CHERESTEA.
- **2026-08-17** — Centered the Depozit Cherestea Vâlcele hero lockup,
  including the buttons and stamp badges, and retuned the hero scrim from
  left-biased to centered radial coverage so the white/amber type remains
  legible at desktop and 360px mobile widths. Shortened the third pillar to
  the supplied wording, removing the unsupported “gata de ridicare” claim.
- **2026-08-17** — Shifted the Depozit Cherestea Vâlcele hero lockup a
  restrained 7% left only from the desktop breakpoint while preserving its
  internally centered mobile composition; moved the desktop radial scrim to
  follow. Replaced the supplied trust/contact copy only; pillar 3 remains
  unchanged.
- **2026-08-17** — Updated only the requested services-card and “Cum
  lucrăm” copy for Depozit Cherestea Vâlcele. The shorter about copy needs
  no layout padding adjustment: its existing desktop grid uses
  `items-center`, keeping the text column balanced with the adjacent photo.

- **2026-08-17** — Rebuilt only the Agrofarm Marius mockup on the standing
  Depozit Cherestea Vâlcele architecture: full-bleed supplied hero image and
  scrim, centered/desktop-left-biased lockup, trust-card grid, snap carousel
  with dot controls, alternating real-photo/about section, reviews, map
  fallback and mobile WhatsApp/call bar. Preserved the magazin-furaje palette,
  type pairing, watermarked logo, noindex and verified reviews. Desktop and
  360px mobile QA passed; mobile menu and carousel dots were exercised.

- **2026-08-17** — Adjusted only the Agrofarm Marius hero scrim and the
  “Cum lucrăm” copy: replaced its green overlay with a neutral warm near-black
  and narrowed the fade so the shelving remains naturally warm on the right;
  replaced the abstract about copy with the supplied direct Marius sentence.
  Desktop and 360px mobile QA passed with no horizontal overflow.

- **2026-08-17** — Pushed the Depozit Cherestea Vâlcele hero/copy revision to
  GitHub (commit `222d220`, includes the hero-panel removal, centered/left-
  biased lockup, rewritten pillars/CTA/"Cum lucrăm" copy, the new
  `romanian-copywriting-style.md`, and the pipeline ledger correction) —
  independently verified live via curl afterward, all three rewritten
  strings present. Depozit is now the standing structural/behavioral
  template for every future mockup rebuild (full-bleed hero, neutral
  scrim, centered-then-left-biased lockup, scroll-snap services carousel,
  reveal-on-scroll, mobile sticky WhatsApp/call bar) — Calin was explicit
  that future rebuilds should apply this template in one comprehensive
  pass, not iterative small patches like the Depozit session took.
- **2026-08-17** — Generated Agrofarm Marius's new hero photo via an
  external ChatGPT image prompt (Step 1 of the mockup build process is
  human-in-the-loop by design — the builder never generates hero/logo
  images itself). Learned the correct Cowork device-bridge direction for
  getting a generated image *into* the repo: `device_stage_files` only
  moves device → container, so pulling the ChatGPT output back out required
  `SendUserFile` (to mint a `file_uuid`) followed by
  `mcp__remote-devices__device_commit_files` targeting the device path —
  confirmed written at `mockups/agrofarm-marius/hero.png` (1727×911,
  ~2.3MB).
- **2026-08-17** — Rebuilt Agrofarm Marius onto the Depozit template (see
  above) and fixed two post-build issues found on review: the hero scrim
  was tinted with the category's brand green (`--c-primary-dark`) instead
  of a neutral tone, and the "Cum lucrăm" section had an abstract,
  nominalized sentence that didn't read like something the real owner
  would say — both fixed via a follow-up Codex prompt (neutral warm
  near-black scrim, plain-sentence rewrite naming Marius directly). Calin
  approved the result. **Not yet pushed to GitHub** — still a local,
  uncommitted change pending a push step.
- **2026-08-17** — Next up: Sabo ITP & SERVICE rebuild onto the same
  Depozit template. Calin was explicit this one should land in one
  comprehensive pass ("from one go"), with the services scroll-snap
  carousel behavior (dot pagination, IntersectionObserver-driven active
  state, touch/drag smoothness) fully and explicitly specified in the
  build prompt up front — flagged as a standing requirement for future
  mockups too, not just this one. Sabo already has both `logo.png` and
  `hero.jpg` on disk, so no new image generation is needed before this
  build.

- **2026-08-17** — Rebuilt only Sabo ITP & SERVICE onto the standing
  Depozit structure: full-bleed `hero.jpg` with neutral legibility scrim,
  centered/mobile then 7%-left desktop hero lockup, watermarked `logo.png`,
  review-grounded trust pillars, five-service scroll-snap carousel with
  IntersectionObserver-synced dot pagination, alternating decorative-photo
  about block, three-card review grid plus the retained fourth real review,
  contact/map/footer/sticky WhatsApp-call bar and shared menu/reveal JS.
  Static integrity checks passed (palette/font tokens, all four exact review
  strings, assets, noindex/disclaimer, no placeholders and clean diff). The
  in-app browser refuses local `file:` navigation under its URL policy, so
  fresh desktop and 360px visual screenshots still need a permitted local
  rendering route before this revision can be called visually QA-complete.

- **2026-08-17** — Superseded the first Sabo rebuild after Calin supplied
  the exact canonical-port brief: restored Sabo's original Tailwind config
  byte-for-byte; replaced the CSS-background hero with Depozit's absolute
  `img.hero-photo` + literal neutral `rgba(20,14,9,…)` scrim architecture;
  added the compact light logo plate and two-line amber H1; ported the
  original scroll/requestAnimationFrame carousel, map 3.5s fallback and
  reveal IIFEs; restored the three-button mobile bar; and reduced reviews to
  Radu, Ioni and Daniela only. Source QA confirms the requested structure,
  six service cards, three review cards, facts/assets/noindex/disclaimer and
  no legacy proof block or template tokens. Visual screenshots remain
  blocked by the browser's local-file URL policy.

- **2026-08-17** — Fixed the Sabo header transparency regression: Sabo's
  Tailwind config uses plain CSS-variable colours, so
  `bg-[var(--c-primary)]/95` silently emitted an unusable background.
  Replaced it with `.site-header{background:rgba(22,24,29,.97)}` and gave
  the mobile dropdown its own solid `rgba(12,13,16,.98)` rule; removed the
  corresponding Tailwind background classes. Source checks confirm neither
  header surface uses a var-based opacity background and that the brand and
  all four navigation labels remain present. Fresh visual captures remain
  blocked by the in-app browser's local-file URL policy.

- **2026-08-17** — Pushed the Agrofarm Marius and Sabo ITP & SERVICE
  Depozit-template rebuilds to GitHub (commit `04fbf9e`) and independently
  verified both live via curl: last-modified today, and each page's
  distinctive new markup/copy present (`hero-scrim`/`hero.png` and
  "Sfaturi corecte" on Agrofarm; `hero-scrim`/`site-header`/"ITP rapid" on
  Sabo). All three mockups (Depozit, Agrofarm, Sabo) are now BUILT, live,
  and on the shared Depozit architecture — none has been contacted yet.
  Calin's plan for next session: switch WhatsApp outreach to the Romanian
  number (see "Later" above) and send the first outreach messages for
  these three leads.

- **2026-08-17** — Closed a real gap Calin flagged: `skills/prospector-mockup/assets/template.html` was still the pre-Depozit generic template (no Tailwind, box-overlay hero, no carousel) even though every live mockup had already moved past it — meaning the next brand-new lead would have started from the old architecture and needed the exact same afternoon of ad-hoc fixing all over again. Rewrote `template.html` from Depozit's proven, live-verified architecture (full-bleed hero + literal-neutral scrim, centered-then-left-biased lockup, svcTrack/svcDots scroll-snap carousel with reusable dot-pagination JS, reveal/reveal-left/reveal-right, 3.5s map-fallback timeout, sticky mobile bar), tokenized for any lead, using the existing generic --c-primary/--c-accent palette naming (not Depozit's one-off --c-bark/--c-pine names) so it drops into the existing six-shell system unchanged. Updated `prospector-mockup.md`'s Step 3, Shared/general rules, Sector palette table, and QA checklist to document the four lessons this session actually cost real revisions to learn: the hero-scrim color must be a literal neutral rgba, never a brand var (shipped a green cast once); a generated logo needs a contrast check against the hero photo and the template's new `logo-plate` class if it's dark (shipped illegible once); a Tailwind color used with a `/NN` opacity modifier needs an RGB-triplet definition or the class silently renders nothing (shipped a fully transparent header once); and the services carousel is a mandatory, verbatim-reused component, not a grid to rebuild per lead. Added RGB-triplet and Google Fonts values for all six sector shells to the palette table so builders never have to hand-convert them (the actual root cause of the header bug was a missing value there, not a bad pattern).
