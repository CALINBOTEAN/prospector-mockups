# Romanian Copywriting Style — Avoiding the "AI-Translated" Voice

Read this before writing any copy for a mockup. It exists because the copy
across the first three builds (Agrofarm Marius, Sabo ITP & SERVICE, Depozit
Cherestea Vâlcele) reads as AI-generated to a Romanian reader — grammatically
correct, but not how a real Cluj-county tradesman or shop owner writes.
Calin flagged this on 2026-08-17. This file replaces guesswork with rules
grounded in the actual flagged text.

## Why it reads as AI, with real examples

**1. The same three-part "why us" skeleton, regardless of business.**
`prospector-mockup.md`'s old copy rule mandated exactly 3 pillars built from
the same three fact types every time: a rating stat, a locality proximity
line, and an hours line. The result is nearly interchangeable across three
unrelated trades:

- Lumber yard: *"Calificativ 5,0 din 5 pe Google... / În Vâlcele, comuna
  Mociu — aproape de dumneavoastră... / Program Luni–Vineri, 08:00–17:00..."*
- Farm shop: *"Rating 5.0/5.0 din 9 recenzii Google... / Magazinul este pe
  Strada București 79... / Program pentru zilele de lucru..."*
- Auto shop: *"Rating 4,7/5 din 102 recenzii Google... / Service-ul este pe
  DJ161A 23, Apahida... / Program lung, inclusiv sâmbăta..."*

Same shape, same order, same three facts, three different businesses. A real
owner would lead with whatever actually matters to *that* trade (e.g. an ITP
shop leads with paperwork/speed, a lumber yard leads with cutting to size),
not a fixed rating/address/hours triad.

**2. Blanket formal `dumneavoastră`, everywhere, regardless of trade or
register.** The old rule mandated formal register in all body copy. Real
Romanian small-business Facebook posts and signage — especially rural trades
like a village lumber depot — are rarely this consistently formal. The
effect reads like a call-center script, not a person who runs the yard.

**3. English-marketing constructs calqued straight into Romanian.**
- *"Semne clare pentru o alegere fără grabă"* / *"Semne clare că mașina e pe
  mâini bune"* — this is the English SaaS pattern "clear signs your car is
  in good hands," translated. No Romanian tradesman writes a section header
  like this.
- *"Cuvântul clientului"* — a literal rendering of "in the customer's
  words." Romanian testimonial sections just say "Ce spun clienții" or
  "Recenzii" — they don't personify "the word of the client."
- *"Recomandări pe înțeles"* / *"Semne clare"* / *"Fragmente fidele din
  recenziile Google"* repeated near-verbatim across all three sites — this
  kind of alliterative, poetic section-header phrasing is a generator tell.
  Real trade copy is flatter and more concrete.

**4. The identical CTA sentence formula on every mockup.**
*"Aveți nevoie de cherestea?"* / *"Aveți de ales un produs...?"* / *"Aveți
nevoie de ITP sau o reparație?"* followed by *"Scrieți pe WhatsApp și..."* —
same question-then-instruction shape, three times. It is fine as one option,
not as the default for every single build.

**5. Abstract positioning lines that say nothing concrete.**
*"Un depozit local, cu răspuns rapid"* could describe almost any business.
Real copy should name the one or two things this specific business is
actually known for (per its reviews), not a generic value proposition.

## Replacement rules

- **Vary register by trade and locality.** A village lumber depot (comuna
  Mociu) or a farm-supply shop can read plainer and warmer than a
  Cluj-Napoca service business. Default to a natural mix — direct
  imperative on buttons ("Scrie pe WhatsApp", "Sună acum"), but don't force
  `dumneavoastră` into every sentence if it starts to read stiff. Read the
  paragraph out loud; if it sounds like a call-center script, cut the
  formality.
- **Do not reuse the same "De ce noi" fact triad verbatim.** Three pillars
  is still fine structurally, but each one must be the fact that actually
  matters for *this* trade and *these* reviews — not a fixed
  rating/address/hours template every time. If two mockups end up with
  near-identical pillar wording, that is a signal to rewrite, not reuse.
- **Ban calque section headers.** No "semne clare," "cuvântul clientului,"
  or other literal English-idiom translations. If a header sounds like it
  was translated from an English landing-page template, replace it with a
  plain Romanian equivalent a shop owner would actually write (e.g. "Ce
  spun clienții," "Recenzii," "Program și contact").
- **Vary the CTA sentence per business.** Do not default to "Aveți nevoie
  de X? Scrieți pe WhatsApp..." on every build. Write a CTA line specific
  to what this business's customers actually ask for.
- **Lead with something concrete and specific**, drawn from the actual
  listing/reviews, not a generic positioning statement. If nothing specific
  is verifiable, say less rather than filling the gap with an abstraction.
- **Prefer short, plain, active sentences** over subordinate clauses and
  poetic apposition. Real trade-business copy in Romania reads closer to a
  Facebook post or a sign in the shop window than to a landing page.
- **Keep the integrity rules unchanged** — correct diacritics, no fabricated
  claims, real reviews only, DEMO watermark and noindex. This file only
  changes *voice*, not the honesty rules in `prospector-mockup.md`.

## Before / after (using the actual flagged lines)

| Before (flagged) | Why it's off | After (example direction) |
|---|---|---|
| "Un depozit local, cu răspuns rapid" | Generic, could be any business | Name what Vâlcele customers actually get — e.g. cutting to size, same-week delivery |
| "Semne clare că mașina e pe mâini bune" | Calqued English idiom as a header | "De ce vin clienții la noi" or drop the header, let the facts speak |
| "Cuvântul clientului" | Literal "in the customer's words" | "Ce spun clienții" |
| "Aveți nevoie de ITP sau o reparație? Scrieți pe WhatsApp..." | Same formula on every site | A line specific to this shop's actual customer pattern (e.g. speed of ITP scheduling, since that's what the reviews praise) |

## Checklist before shipping copy

1. Read the hero, pillars, and CTA out loud — does it sound like a person
   who runs this specific business, or like a template?
2. Do the three "De ce noi" pillars read differently from the other two
   live mockups, or could you swap them between businesses unnoticed?
3. Any section header that would need to be explained if translated back
   to English literally? Rewrite it.
4. Every claim still traceable to the listing/reviews (integrity rules
   unchanged).
