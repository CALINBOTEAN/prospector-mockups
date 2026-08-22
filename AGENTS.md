> Keep this file identical to its counterpart — apply every edit to both files in the same turn.

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

## Vacation rentals (formerly "Offer C") — now the primary Offer A category (since 2026-08-20)

Status change: this was a ring-fenced, scan-only idea; Calin has now made
it the primary focus category for Offer A, ahead of the mixed-category
scanning that produced Depozit/Sabo/Agrofarm/AVA/Confecții Metalice/BUSU.
It is not a separate offer track — it uses the exact same free-mockup +
WhatsApp-outreach mechanics as the rest of Offer A, just concentrated on
one category (`offer=A`, `category=cabana / pensiune (vacation rental)` in
`data/pipeline.csv`), the way Depozit's tamplarie or Sabo's service auto
categories were.

Rationale (unchanged from the original idea): businesses on Booking.com/
Airbnb with high occupancy but no direct-booking website of their own are a
strong lead category — they're already proven to convert bookings, but lose
money to OTA commissions (Booking.com ~15–18%, Airbnb ~3% host-side + guest
fee up to ~14.2%), last-minute cancellations, and have no direct guest
relationship.

**Current state (2026-08-20):** `data/scan_c_2026-08-18.csv` (80 raw leads,
mountain localities around Beliș/Mărișel/Băișoara/Mărgău) was qualified this
session — `skills/prospector-qualify/prospector-qualify.md` was updated
first to add vacation rentals as a Tier-1 category and add a low-engagement
gate (discard <5 reviews AND zero social footprint to `DORMANT`, added
specifically because early outreach on other categories was hitting
low-digital-adoption owners who were never going to convert). 65 of 80
leads passed; 3 selected as this week's shortlist (`QUALIFIED`, non-competing
localities, highest score/review-count first — Casa Eden, Pensiunea Larix,
Cabana Trofeul Munților), the rest held `NEW` in the backlog for future
weeks. 2 discarded to `DORMANT` under the new gate.

**Blocking item before any build:** `skills/prospector-mockup/reference-library.md`
has zero filled-in references — no design/motion direction exists yet for
this category. Calin said he wants "a template or 1-2" for vacation
rentals specifically before building starts. This must be resolved (a
short design-direction conversation, per the standing Step 2 rule) before
Automated batch pipeline Step 5/6 can run for any vacation-rental lead.

**Plan going forward (Calin's explicit direction, 2026-08-20):** work this
category's backlog top-down by review count, starting with the automated
batch pipeline's mandatory first-run-of-1 test (exactly one lead through
all six steps, to prove the autonomous build works), then move to the
10-lead batch cap once that succeeds. After several vacation-rental builds
are through the pipeline, move on to the next category from the deep-dive
ranking (wedding venues was the top-ranked new candidate; see
`claude/industry-deep-dive-framework.md` in the Claude project). Existing
`categories_ro.txt` categories (tamplarie, service auto, agri supply,
metal fabrication, construction) are not abandoned — Confecții Metalice
Cluj and BUSU Building Cluj remain `QUALIFIED` and can still be picked up —
but vacation rentals now has first claim on the weekly WIP cap.

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

## Mistake → Rule pipeline

Whenever a mistake is found and fixed during a session, before the session
ends, evaluate whether it could recur. If yes, the fix must be written as a
standing rule into the relevant skill file — not only logged in this file's
Session log. The Session log records what happened; the skill file is what
prevents the repeat.

## Pacing caps

- The existing weekly send cap remains a hard limit for all first-contact
  outreach.
- No more than 3 leads may be built but unsent at one time. Batch work may
  prepare candidates ahead, but it must not place more than that number into
  the active build queue.

## Automated batch pipeline

Trigger this standing workflow when Calin clearly says something like
"let's go", "start the batch", or "run the pipeline" in a Prospector
session. The trigger is authorization for the automated steps below; merely
mentioning those phrases while discussing or documenting the workflow is not
a trigger.

1. **Pre-flight, then select the batch.** When a trigger is heard, before
   ranking or selecting any lead, read `STATUS.md`'s `Automated batch
   workflow full successful run` marker to determine the target: 1 on the
   first run, or 10 after the first successful run. Then check and report all
   of the following:
   - Count leads with `status=QUALIFIED`. If fewer than the target are
     available, state the actual count and do not build a partial or
     undersized batch automatically. Ask Calin whether to (a) run
     `prospector-qualify` over some `NEW` leads first, or (b) proceed anyway
     with the available leads.
   - Check whether `skills/prospector-mockup/reference-library.md` has at
     least one entry with a filled-in short name, best-suited category, and
     motion/animation direction. If it is fully empty, say so plainly: Steps
     5 and 6 cannot proceed without at least one usable reference, unless
     Calin supplies complete design and motion direction manually in the
     trigger message itself.
   - Confirm that the existing session-start gate has already reported the
     current weekly send-cap and built-but-unsent-cap status; do not duplicate
     that cap calculation here.

   Only after reporting all three may the workflow proceed. If any gap needs
   Calin's decision, stop and wait for that decision. If the pre-flight is
   clear, read `data/pipeline.csv` and sort `QUALIFIED` leads by effective
   qualification date ascending: use `date_qualified` when it is present,
   otherwise use `date_found`. Leave a blank `date_qualified` on historic
   rows blank — do not guess or backfill it.
   - If the marker is absent or `no`, this is the first run: identify exactly
     1 lead and carry only that lead through all six steps to completion. Do
     not identify a batch of 10 or queue up to 3 leads on this run. This
     first-run-of-1 rule exists specifically to test the autonomous Step 6
     build before trusting it at full batch width.
   - If the marker is `yes`, identify the next 10 as the ranked batch
     candidate set, but only put as many into the active build queue as can
     realistically move through the existing caps — especially the maximum of
     3 built-but-unsent leads. Report both the 10 candidates and the
     cap-limited active queue; do not change pipeline rows merely to queue
     them.
   In the same trigger message, Calin may optionally choose a reference number
   for each lead or one reference for the whole batch — for example,
   "let's go — Agrofarm: reference 3, Sabo: reference 5."
2. **Write image prompts.** For every lead in the active candidate set — one
   on the first run, or all 10 on later runs — write a logo prompt and a
   hero-image prompt as separate copy-paste-ready fenced text blocks for
   Calin to paste into ChatGPT manually. This is prompt-writing only: no
   image generation happens inside this pipeline.
3. **Image approval — manual checkpoint.** Calin reviews each generated
   image set and approves or rejects it. No automation action happens at
   this checkpoint.
4. **File approved assets.** When Calin uploads approved images in a Cowork
   session and names the lead each image belongs to, Claude directly renames
   and files them into that lead's existing `mockups/<slug>/` folder as
   `logo.jpg` and `hero.jpg`. Never overwrite an existing asset: file a
   conflict as `logo_new.jpg` or `hero_new.jpg` instead and warn Calin.
   Report every asset filed. This replaces manual renaming entirely; Calin
   never needs to run a terminal command for this step.
5. **Prepare a lead for its build — automatic, not a checkpoint.** Once a
   lead has filed assets, use the reference chosen in the trigger, or the
   complete design and motion direction Calin supplied manually in that
   trigger. If neither was specified for that lead, ask Calin only for that
   lead's reference number at the moment it is otherwise ready for Step 6;
   do not stop or ask for references for the rest of the batch.
6. **Build and final review.** Once a lead is build-ready, its mockup build
   runs autonomously end-to-end through the finished site, using the chosen
   reference's documented motion/animation direction or Calin's complete
   manually supplied direction. The build then stops for Calin's final mockup
   review before anything goes live or is sent. When the first-run lead has
   successfully reached final review, with its assets filed and Calin having
   reviewed the result, update `STATUS.md`'s `Automated batch workflow full
   successful run` marker to `yes`.

There are exactly two manual checkpoints: image approval in Step 3 and final
mockup review in Step 6. Reference selection is not a separate checkpoint:
it is optional in the trigger and otherwise a single-lead fallback question
only when that lead is ready to build. Once the workflow is triggered, Steps
1, 2 (prompt-writing only), 4, 5, and the build portion of Step 6 run without
further confirmation. This workflow still obeys the weekly send cap and the
built-but-unsent cap from **Pacing caps**: it may queue and build ahead, but
outreach must never exceed those limits.

## Post-build fixes — division of labor (standing rule, effective 2026-08-18)

This is the fix for "Codex burns a lot of tokens on every little fix" —
observed directly on the AVA Möbelhaus build, where round after round of
small CSS/copy/JS fixes each cost a full Codex re-read of the file (and
sometimes the skill/template) before making a one-line change.

- **Once a mockup is `BUILT` (or later), the default for a cosmetic,
  copy, CSS, or small-JS fix is: Claude edits the file directly** through
  the Cowork desktop bridge — `device_stage_files` → `Read`/`Edit` →
  `SendUserFile` → `device_commit_files` — not a Codex prompt. A direct
  edit costs one read and one targeted edit; a Codex prompt re-reads the
  whole file (and often the skill) every single time, even for a one-line
  change. Calin still runs the 3-line PowerShell deploy below afterward —
  that part doesn't change.
- **Codex (or Claude Code in the terminal) stays the right tool for:**
  (a) a brand-new mockup build via prospector-mockup's Step 1–3 process —
  reading the template/skill once per build is legitimate overhead, not
  waste; (b) a change to the shared architecture itself
  (`assets/template.html`, a category-shell definition) — this has
  cross-mockup impact and deserves the fuller read; (c) anything that
  genuinely needs a local shell, dev server, or file operation Cowork
  can't do (device bridge has no git, no shell, no network).
- **If a fix does have to go through Codex anyway** (Cowork unavailable,
  or it's a (c)-case above), keep the prompt surgical: name the exact
  file and the exact selector/line, state before → after, and say
  explicitly not to re-read the template or other mockups. Do not paste
  a general complaint ("the scrolling is laggy") and let it re-derive
  context from scratch each time — diagnose the root cause first (in
  Cowork or Claude Code, both of which can just read and reason about
  the file directly), then hand over a one-line surgical instruction, or
  make the edit directly and skip Codex entirely.
- **Self-check before ever showing Calin a build.** For JS/animation/
  interaction fixes, verify in a headless Chromium session
  (`/opt/pw-browsers/chromium` via Playwright/`node -e`) before asking
  Calin to test on his phone. Headless tabs report
  `document.visibilityState === "visible"` and don't suffer the
  background-tab `requestAnimationFrame`/timer throttling that makes the
  interactive Claude-in-Chrome extension unreliable for this kind of
  check (confirmed directly on the AVA product-rail debugging). Use this
  to catch an obviously frozen/broken state pre-emptively — it cuts a
  full "still laggy, try again" round-trip, which is exactly the kind of
  loop that burns tokens and Calin's patience together.

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

- **2026-08-19** — Daily reply check (Cowork): still no reply on Depozit
  Cherestea Vâlcele, Sabo ITP & SERVICE, or Agrofarm Marius (Template 2
  windows open 2026-08-20). Confirmed with Calin that AVA Möbelhaus's
  proposal PDF (sent 2026-08-18) was owner-initiated — AVA asked for the
  offer in reply to Template 1 — still no reply to the offer itself.
  **Self-caught process error:** transitioned AVA's pipeline status
  straight from `CONTACTED` to `MEETING` on the strength of "they asked
  for and received an offer," then caught that this violates
  prospector-pipeline's no-skipped-statuses rule (CONTACTED must pass
  through FOLLOWUP_1/FOLLOWUP_2 before MEETING, absent an actual scheduled
  meeting or live back-and-forth negotiation) and reverted it to
  `CONTACTED` in the same session, before the ledger was left in a bad
  state for anyone reading it later. **Lesson: an engaged reply (a
  question, a request) is not automatically a `MEETING` — reserve that
  status for an actual scheduled meeting or an active, ongoing
  negotiation thread, not a single request-and-response.** No other
  ledger, build, or outreach changes made.
- **2026-08-18** — Ran the Offer C (vacation rentals) micro-test scan from a
  Cowork cloud session — scan only, ring-fenced per plan: scratch inputs
  `data/categories_c_test.txt` (cabana / pensiune agroturistica / casa de
  vacanta) × `data/localities_c_test.txt` (8 mountain/lake localities:
  Belis, Marisel, Rasca, Valea Ierii, Baisoara, Muntele Baisorii, Sacuieu,
  Margau). 24 billable calls, zero failures. Output
  `data/scan_c_2026-08-18.csv`: **80 new leads (64 none / 16 social_only;
  67 with phone; 0 pipeline duplicates)**; 67 further results had real
  sites. Lead rate ~54% of unique results — far above the trade-sector
  scans — with density concentrated in Belis (24), Marisel (15), Baisoara
  (12), Margau (10); 59 of 80 leads show rating ≥4.5 with ≥5 reviews.
  `categories_ro.txt` and `pipeline.csv` untouched; no qualification run.
  Scratch input files deliberately left in `data/` for a pilot-review
  re-run (the device bridge cannot delete files; note they are NOT
  gitignored — harmless if committed). Lessons: `scanner.py` hard-codes
  `scan_<date>.csv`, so the Offer C run wrote to a scratch dir and was
  renamed to `scan_c_…` before commit — consider an `--out-name` flag if
  Offer C scans become regular. The cloud sandbox cannot read the desktop
  `GOOGLE_PLACES_API_KEY` env var, so the key was pasted into the session
  for this run (not written to any file); optional key rotation flagged
  to Calin.
- **2026-08-18** — Finalized and sent AVA Möbelhaus (first outreach of the
  pilot's second batch). Redesign work: hero reverted to full-bleed
  `object-fit:cover` after a contain/blur-backdrop experiment was
  rejected on taste grounds ("I don't like it like this"); real
  Google-listing copy dropped into "Despre showroom" and the hero
  tagline, verbatim, replacing placeholder-style text; sticky mobile
  WhatsApp bar now shows/hides via `IntersectionObserver` on the hero
  and carries a WhatsApp bubble icon instead of the `↗` glyph.
  **Product-rail smoothness root-caused through three layers, worth
  remembering for any future horizontal-scroll build:** (1)
  `touch-action:pan-y` was blocking native touch scrolling entirely,
  forcing everything through custom JS that could never feel as smooth
  as the browser's own compositor — switched to `pan-x` and deleted the
  custom touch-drag JS; (2) `getBoundingClientRect()` was being called
  every animation frame, forcing layout recalculation continuously —
  cached it, refresh only on debounced resize; (3) even after those
  fixes, a JS-driven `scrollLeft` ambient auto-scroll was still
  reported "not smooth" — replaced entirely with a pure CSS
  `@keyframes`/`transform:translate3d` animation
  (`animation-play-state` toggled on real interaction only), which
  removed the main-thread cost altogether and was the fix that actually
  landed. Sent Template 1 via WhatsApp by hand; logged
  `status=CONTACTED`, `date_contacted`=2026-08-18,
  `next_action_date`=2026-08-21. Decided not to add email or Facebook
  in parallel for this lead — AVA has a working WhatsApp number, so it
  doesn't qualify for prospector-outreach's Facebook-Messenger-first
  policy (that's for `social_only` leads only), and email is explicitly
  discouraged as a fallback for this segment; staying on the WhatsApp
  Template 1→2→3 cadence per the skill. **New standing rule:** every
  mockup now gets an `outreach/` folder (see prospector-mockup and
  prospector-outreach skill updates below) holding the actual
  phone-view screenshots sent alongside the WhatsApp link, since most
  leads will only ever see the site on a phone. Confecții Metalice Cluj
  and BUSU Building Cluj (the other two leads from this week's batch)
  are **deferred, not built this week** — token budget; no pipeline
  status change, still `QUALIFIED`. Also wrote up the token-efficiency
  fix as a standing process rule (see "Post-build fixes — division of
  labor" above) and confirmed headless Playwright doesn't suffer the
  interactive browser extension's background-tab throttling, making it
  usable for pre-flight JS/animation checks going forward.
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

- **2026-08-17** — Ran Agent 1's week-2 batch (mobilă la comandă, confecții metalice, instalații sanitare, firme construcții, amenajări interioare) across the 20 Cluj localities. The successful run used 100 calls and produced `data/scan_2026-08-17.csv`: 153 leads (126 no website, 27 social-only), with 3 pipeline duplicates skipped. The first run lost its connection after 84 completed requests and did not write output; one identical retry completed, so 184 API requests definitely completed across the session (the aborted 85th request may also appear in Google billing). Scratch `data/categories_batch2.txt` was removed; no commit or push was made.
- **2026-08-17** — Ran Agent 2 qualify on `data/scan_2026-08-17.csv` (Cowork session). Hard-gated on phone-present + not-already-known (134 of 153 passed; 19 no-phone discarded per gate), scored the rubric: 88 A / 27 B / 19 C. **Verification pass caught two false positives before they wasted build hours**: SANTECHSTEEL SRL (instalatii sanitare, Baciu Cluj) and Instalis Engineering Solutions SRL (instalatii sanitare, Capusu Mare) both scored A on paper, but a plain web search found live sites (`santechsteel.ro`, `instalis.ro`) with matching business names/phone that Google Places' `websiteUri` field simply hadn't captured — discarded from Offer A entirely (hard gate 1). **Lesson: `website_status=none`/`social_only` from the scanner is not sufficient proof of no website — Places can miss a real site that exists but isn't linked on the Business Profile; always web-search the exact name + locality during the verification pass, especially for generic/common business names.** Both are plausible Offer B (GBP) candidates instead (real site, not connected to their Maps listing) but were not run through prospector-gbp's own rubric — flagged for Calin, not added to the pipeline as B leads. Selected the weekly three (sector-diverse, all verified clean, all 07xx mobile phones): AVA Möbelhaus (mobila la comanda, Gilau, score 12 — large multi-region furniture outlet, heavy FB/IG/TikTok presence, no dedicated site), Confecții Metalice Cluj (confectii metalice, Floresti Cluj, score 12 — the only similarly-named domains found belong to different companies with different phone/CUI), BUSU Building Cluj (firma constructii, Floresti Cluj, score 12 — confirmed active via risco.ro, registered 2019, 2025 financials on file). Logged as QUALIFIED with full per-lead verification notes; other 83 leftover-A and 27 B leads appended as NEW (held for future weeks per WIP cap); 19 C leads appended as DORMANT. `data/pipeline.csv` grew 220→352 rows. Wrote a same-day dated backup, `data/pipeline_backup_2026-08-17.csv`, before the append (the weekly-backup step this session had otherwise skipped in the moment). Next: run prospector-mockup for lead #1, AVA Möbelhaus.

- **2026-08-18** — Began Agent 3 for AVA Möbelhaus. The Places photo fetch returned five real listing images; selected the landscape showroom image as `mockups/ava-mobelhaus/hero.png` and retained the fetched originals/provenance in its `assets/` folder. Sourced AVA's genuine public Facebook profile graphic as `logo.png` (not generated, so no DEMO watermark). Read the live Maps listing: it is active/not marked permanently closed; published hours are Mon–Fri 10:00–18:00, Sat 10:00–16:00, Sun closed; in-store shopping, pickup, delivery, address and phone match the lead row. Stopped before finalizing the reviews section as the explicit AVA brief requires — waiting for Calin to paste 2–3 verbatim Google quotes with reviewer first name + initial. No HTML, deployment, or ledger-status change yet.

- **2026-08-18** — Resumed the AVA Möbelhaus build with the supplied three verbatim Google reviews and a seven-category product grid sourced from AVA's public Facebook photos (Canapele, Colțare, Paturi tapițate, Paturi rabatabile, Dulapuri cu uși glisante, Mese de cafea, Comode TV). Built the Tailwind mockup on the shared Depozit architecture and checked it locally at 1280px and 360px: no broken page images or console errors, no mobile horizontal overflow, working menu, synced carousel dots, map/fallback, correct WhatsApp/tel links, noindex and disclaimer. **Not deployed or committed:** the requested generated wordmark was not yet available. The only on-disk image was a different public Facebook flyer, so it was not substituted or watermarked; AVA remained QUALIFIED and `data/pipeline.csv` was untouched.

- **2026-08-18** — Rebuilt AVA Möbelhaus as a deliberately distinct light, warm-white premium mockup: a floating responsive header, three-image carousel, compact facts band, real-product marquee, beige services panel, review cards, contact/map and dark footer. The supplied wordmark was watermarked with a restrained visible `DEMO` tag; the obsolete Facebook flyer asset was removed, with no repository references left. Kept the four strongest high-resolution genuine AVA Facebook product photos for display and retained the source material/provenance. Browser QA passed at 1280px and 360px (including menu, sticky header, active nav, carousel dots/arrows/autoplay and real review links); the source also contains the required touch-swipe handler. Committed the mockup as `664cdfa` and pushed to `main`; curl confirmed the live mockup returns HTTP 200 with the new hero/disclaimer. AVA remains QUALIFIED and `data/pipeline.csv` was untouched.

- **2026-08-18** — Applied AVA's post-review fixes and pushed `21ab625`: removed every logo instance outside the header; replaced its display asset with a high-resolution cropped/watermarked version plus an optimised WebP delivery file; changed the H1 to `AVA Möbelhaus` and added a restrained title entrance; rewrote the page in plain formal Romanian; replaced the CSS marquee with a native horizontal rail that supports pointer drag, wheel/touch pause and rAF auto-scroll with a seamless duplicated-set reset; and moved contact/footer to the same light beige palette. The rail was run for nearly three minutes and crossed its reset point without blank space. Added `AGENTS.md`, `CLAUDE.md` and `STATUS.md` to `.gitignore`, untracked all three while preserving local copies, and verified their public Pages URLs now return 404. AVA remains QUALIFIED and the pipeline ledger was untouched.

- **2026-08-18** — Applied the three final AVA corrections and pushed `ba5a99e`: regenerated both delivered logo files from the clean `assets/logo-source.png` chair-outline source at proper header resolution, with a restrained DEMO stamp, replacing the old glowing/cropped version everywhere in the AVA delivery assets; added true card-row `mousedown` / `mousemove` / `mouseup` panning, a resettable 2.4-second interaction pause, and retained the seamless rAF loop; kept contact light beige while restoring only the footer to near-black, with logo, tagline, contact list and disclaimer. Full browser QA passed at 1280px and 360px (18 images, no errors/overflow, links, map fallback, noindex/disclaimer, responsive menu/sticky bar). Direct card dragging was exercised and the final rail ran for 200 seconds across multiple gap-free wraps. GitHub Pages workflow completed successfully and the live HTML was verified. AVA remains QUALIFIED; `data/pipeline.csv` was untouched.

- **2026-08-18** — Applied AVA's final visual refinements and pushed `dbf10aa`: deterministically keyed the uniform white matte out of the supplied chair-outline mark at `assets/logo-source.png`, then regenerated the transparent PNG/WebP delivery exports with a restrained DEMO stamp; removed all header-logo box treatment and used a compatible light treatment only in the dark footer. Changed the hero and its inner content from fixed heights to `100vh`/`100svh` while retaining the feature-band overlap; changed contact to `--c-bg`; and set the desktop/mobile header, hero, contact and sticky WhatsApp buttons to #25D366/#1EBE5D with white icon/text. Full browser QA passed at 1280px and 360px: no errors/overflow, menu/sticky bar/hero carousel verified, all images loaded, and the product rail dragged directly by mouse, paused, resumed and completed a 2m45s seamless-loop run. Pages deployment succeeded and the public HTML contains all new markers. AVA remains QUALIFIED; `data/pipeline.csv` was untouched.

- **2026-08-18** — Follow-up AVA fold correction, pushed as `7f34291`: removed the negative feature-band margins and added a clean 32px desktop / 20px mobile gap immediately after the full-height hero. The three-point card is now entirely below the initial viewport at 1280px and 360px (rather than sliced at the hero boundary); one normal first scroll exposes the full card clear of the fixed header and mobile sticky bar. Browser QA passed at both breakpoints with no clipping, horizontal overflow or console errors. Pages deployment succeeded and its public HTML was checked for the new positive offsets and absence of the legacy negative margins. AVA remains QUALIFIED; `data/pipeline.csv` was untouched.

- **2026-08-18** — Superseded the external feature-band placement after Calin clarified the intended composition; pushed `077da6b`. Moved the three AVA features directly under the hero CTA row as compact translucent, rounded pills with a restrained 0.2-second lift/background/border hover state, then removed the separate post-hero band and its CSS. At 1280px the complete hero lockup ends at 583px within a 720px hero; at 360×800 it ends at 652px, clear of the sticky bar at 726px. Both breakpoints passed image, overflow and console checks; the browser also exercised the pill hover. Pages deployment succeeded and public HTML confirms in-hero pills, hover CSS, no external band and the retained full-viewport hero. AVA remains QUALIFIED; `data/pipeline.csv` was untouched.

- **2026-08-18** — Refined AVA's in-hero pills again and pushed `4c43501`: restored the warm-white card background with dark-brown labels and mustard icons, while preserving their existing outer dimensions; added a deeper mustard-border/white-surface/shadow hover state on the normal 0.2-second timing; and translated the band lower toward the carousel nav (40px desktop, 20px mobile) without moving it out of the hero. Browser QA passed at 1280px and 360×800: every hero component fits, the desktop cards are 193×86px at y537–623, the mobile cards are ~100×87px at y585–672 and clear the y726 sticky bar by 54px, no images failed, no overflow and no console errors. Pages deployment succeeded and the public HTML markers were checked. AVA remains QUALIFIED; `data/pipeline.csv` was untouched.

- **2026-08-18** — Built and sent a restyled written proposal PDF for AVA Möbelhaus, `mockups/ava-mobelhaus/AVA-Mobelhaus-Propunere-v2.pdf` (Windows/PowerShell session, not Cowork). Starting point was a supplied `AVA-Mobelhaus-Propunere.pdf` in Downloads with no source file anywhere — searched this repo, Desktop, and Downloads and found nothing, so the HTML source was rebuilt from scratch (kept the original's exact copy/structure/prices per Calin's instructions) rather than edited in place; source lives only in a scratch temp dir, not committed. Palette/fonts pulled directly from `mockups/ava-mobelhaus/index.html`'s CSS variables and Google Fonts link so the proposal visually matches the live mockup; rendered to PDF via headless Chrome (`chrome --headless --print-to-pdf`) since neither Node nor Playwright was available locally — Chrome/Edge's built-in print-to-PDF is a solid fallback for this when Playwright isn't installed. Iterated through several real bugs worth remembering: (1) the cover H1 inherited the same dark-brown `--c-primary` as its own background, rendering it essentially invisible — always explicitly set text color when reusing a shared heading rule on a dark surface; (2) `text-shadow` used for legibility over the cover photo (copying the live mockup's own technique) silently duplicated the underlying PDF text layer — visually fine but every character came out doubled on copy-paste extraction; switched to a plain darkening-gradient wash over the photo instead, which has no such side effect and is the safer default for anything meant to become a print PDF. Content changes made at Calin's direction during review: removed the Magazin Online tier from pricing entirely (he has no e-commerce build experience yet) and replaced it with a short note inviting the lead to ask for a separate custom quote if they need a full paid online store; changed Esențial/Catalog from price *ranges* to single fixed prices (600 € / 1.000 €, reasoning: a range just anchors the client to the low end) with mentenanță raised to 60–80 €/lună and 100–120 €/lună; redesigned the cover so the real showroom photo runs full-bleed the entire page (it was previously hidden under a solid-color panel for the bottom half) with the logo enlarged and moved to the top; added the same real logo to the empty space at the bottom of the closing page. **Recurring gotcha this session, worth remembering for any future file handoff:** reusing the same filename across repeated `SendUserFile` sends caused Calin's viewer to keep showing a stale cached copy even after the on-disk bytes had changed (verified via md5) — the fix each time was sending under a new filename; a leftover Office-style `~$...` lock file next to the real filename confirmed a viewer had it open. Outreach: sent this PDF via WhatsApp same-day alongside the already-sent Template 1 (see below); `data/pipeline.csv` updated accordingly (backup written first per the mandatory rule), status stayed `CONTACTED` since there's still no reply, `next_action_date` unchanged at 2026-08-21.
