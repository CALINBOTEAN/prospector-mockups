---
name: prospector-outreach
description: Agent 4 of the Prospector pipeline — prepares WhatsApp-first, text-only outreach and follow-ups for a prospect whose mockup is built. No phone calls anywhere in this pipeline. Use this skill whenever the user wants to contact a lead, draft the WhatsApp message, write follow-up messages, handle an objection from a prospect, or says anything like "prepare the outreach", "write the message for", "how do I follow up", or "ce îi scriu". Also use it to log outreach outcomes into the pipeline.
---

# Prospector — Agent 4: Outreach (WhatsApp-first, text-only)

## Mission
Convert a built mockup into a reply, then a meeting — entirely by text.
No phone calls at any stage. This agent drafts every message; **the human
sends everything personally**, from their own WhatsApp number.

## Backup (mandatory, first action)

Before any append or status change to `data/pipeline.csv`, write a dated
backup `data/pipeline_backup_YYYY-MM-DD.csv` if one does not already exist
for today. This is unconditional, not a weekly-rhythm item.

## Channel strategy (ranked)

1. **WhatsApp direct** — default and primary channel. Personal, high open
   rate, matches how this segment already communicates with customers.
2. **Facebook Page message (Messenger)** — for `social_only` leads who are
   more active on their Facebook page than WhatsApp.
3. **Email** — fallback only, for the rare lead with no phone/WhatsApp and no
   reachable Facebook page. Expect materially lower reply rates for this
   segment than the general B2B benchmark, since businesses without a
   website typically also lack an active email habit — do not lead with it,
   and note that Google Places has no email field at all, so an email
   address for this fallback has to be sourced manually (Facebook "About"
   tab, ANAF/listafirme filings) rather than pulled from the scan.

Phone calls are excluded from this pipeline by design. Do not suggest or
draft call scripts, and do not steer a text conversation toward "let's hop on
a call" — that reintroduces the channel the founder chose to avoid.

## Legal and platform guardrails (non-negotiable)

- Unsolicited commercial electronic messages are restricted in Romania
  (Law 506/2004, implementing the e-Privacy Directive, alongside GDPR).
  Because there is no prior call to obtain verbal consent in this pipeline,
  every first-contact message must read as a personal, individually-written
  note — not a broadcast — and must include a clear, low-friction opt-out in
  the same message.
- **Never** use bulk-sending tools, WhatsApp Business API blasts, or
  scheduling/automation software for first contact — this both violates
  WhatsApp's terms (number ban risk) and destroys the one-to-one positioning
  that makes the reply rate viable at all. Every message is typed and sent by
  hand, from a real personal or verified WhatsApp Business number.
- Maximum ~5 first contacts per day, Monday–Thursday, 09:00–18:00. Space
  sends by a few minutes each — a burst of identical-looking messages in one
  minute reads as automated even when it isn't.
- The demo link must open a page carrying the demo disclaimer and noindex
  (Agent 3 guarantees this).

## Message templates (Romanian — personalise every send: name, locality, one
concrete detail from the Maps listing or reviews)

**Template 1 — first contact:**
> Bună ziua! Mă numesc {name} și lucrez cu firme din zona {zonă} la partea de
> prezență online. Am observat că {Firma} are recenzii foarte bune pe Google
> — {rating} din {review_count} — dar nu are un site propriu. Ca să nu vă
> răpesc timpul cu teorie, v-am pregătit deja o propunere concretă, gratuit:
> {link} — se deschide direct pe telefon. Dacă vă place, o discutăm; dacă nu
> vă interesează, un simplu «nu, mulțumesc» este suficient și nu vă mai
> deranjez. O zi bună!

**Template 2 — follow-up, day +3:**
> Bună ziua! Revin cu un mesaj scurt — ați reușit să aruncați o privire peste
> propunerea de site pentru {Firma}? {link}
> Mă interesează sincer părerea dumneavoastră, chiar și una critică. Mulțumesc!

**Template 3 — follow-up, day +7 (close):**
> Bună ziua! Ultimul mesaj din partea mea, promit. Păstrez demo-ul pentru
> {Firma} activ până pe {data}; după aceea îl retrag. Dacă doriți, putem
> continua aici pe WhatsApp să stabilim exact ce rămâne din propunere și
> costul — durează 5 minute în scris. Dacă nu este momentul potrivit, nicio
> problemă — vă doresc mult succes în continuare!

**Facebook Messenger variant (social_only leads):** same text as Template 1,
opened with "Bună ziua! V-am scris aici pentru că am văzut pagina de
Facebook a {Firma}."

## Screenshots (standing rule, effective 2026-08-18)

Most leads will only ever open the demo link on a phone. Before the first
WhatsApp send, put 2-3 real device-view screenshots of the finished, live
page into `mockups/{slug}/outreach/` (create the folder if it doesn't
already exist) — hero, one product/services view, and one more section
that sells the page well (about/trust/reviews). Name them descriptively,
e.g. `whatsapp-1-hero.png`, `whatsapp-2-produse.png`,
`whatsapp-3-despre.png`. Send these alongside the WhatsApp text and link,
in the same message flow — they let the prospect see what the phone
experience actually looks like without needing to tap through first, which
matters more for this channel than for a desktop-first cold email. This
folder holds everything sent with that particular WhatsApp send, so if a
later follow-up (Template 2/3) needs different or updated screenshots,
add them here too rather than creating a second folder.

## Objection handling (all in text — no call fallback)

- **"Am pagină de Facebook."** — "Excelent, pagina rămâne și este importantă.
  Site-ul face altceva: apare pe Google când cineva caută «{serviciu}
  {localitate}» și inspiră încredere clienților noi care nu vă cunosc încă.
  Cele două lucrează împreună."
- **"Cât costă?"** — never quote in the first message. When asked directly:
  "Depinde de ce păstrăm din propunere — de regulă între {low} și {high} lei,
  o singură dată, plus găzduirea. Vă pot trimite aici, în scris, o defalcare
  exactă dacă doriți." Always answer numerically over text.
- **"Nu am nevoie, clienții mă știu."** — "Perfect pentru clienții actuali.
  Site-ul este pentru cei care nu vă știu încă și caută pe Google. Demo-ul
  rămâne oricum gratuit — dacă vă răzgândiți, mă găsiți."
- **Silence after Template 1** — do not escalate to a phone call. Follow the
  Template 2 / Template 3 cadence and then let it go to `LOST`.

## Expectation setting

Text-only outreach to a low-digital-adoption segment should be expected to
underperform typical B2B cold-email benchmarks (roughly 3–6% reply rate for
well-targeted general audiences, per current industry data) until proven
otherwise by your own numbers. WhatsApp's higher open rate compared to email
helps, but nothing here replaces the trust a live conversation would build —
that trade-off was made deliberately in exchange for not making calls, and it
should be tracked, not assumed away. Track reply rate explicitly from message
1 (see prospector-pipeline monthly review) and treat a rate persistently
under ~10% as a signal to revisit targeting or messaging, not to push more
volume through the same approach.

## Logging (mandatory after every action)

Update the lead's row in `data/pipeline.csv`:
`status` (CONTACTED → FOLLOWUP_1 → FOLLOWUP_2 → MEETING → WON / LOST),
`date_contacted`, `next_action_date` (+3 or +7 days), and a short note
(channel used, outcome, any objection verbatim, and whether screenshots
from `mockups/{slug}/outreach/` were sent). After Template 3 with no
reply → `LOST`, schedule demo takedown per Agent 3, and a single re-approach
is permitted after 6 months.
