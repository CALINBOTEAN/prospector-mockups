---
name: prospector-gbp
description: Offer B of the Prospector system — a Google Business Profile (GBP) audit and local-rank optimisation retainer for Cluj businesses that already have web presence but underperform in the Local Pack (rank 4th or lower for their core keyword). Runs parallel to Offer A (no-website builds) with its own lead identification logic, audit checklist, and WhatsApp outreach script. Use this skill whenever the user wants to identify GBP leads, run a GBP audit, draft the Offer B pitch, or says anything like "find GBP leads", "audit this listing", "pitch the GBP retainer". Read prospector-pipeline first — Offer B shares the same ledger and WIP discipline as Offer A.
---

# Prospector — Offer B: GBP Local-Rank Retainer

## Positioning

Offer A sells a website to a business with none. Offer B sells ongoing local
visibility work to a business that already has *some* presence but is losing
Local Pack traffic to competitors — often while paying for Google Ads to
compensate. Same pipeline discipline (ledger, WIP limits, WhatsApp-first,
text-only outreach), separate lead pool, separate service.

**Sequencing note:** run this at a token scale (≈1 lead/week) alongside Offer
A until Offer A's own pilot has produced real reply/close data. Two unproven
funnels run at full volume simultaneously make it impossible to tell which
one, if either, is working.

## 1. Offer definition

**Service:** GBP audit + ongoing optimisation —
category and services-list accuracy, Q&A seeding, photo cadence, a
*legitimate* review generation and response system, local citation
consistency, weekly GBP posts.

**Price:** €150–300/month, calibrated to Cluj market rates. This is
deliberately below the ~€400+/month floor for full-scope Romanian SEO
retainers, because GBP management is a narrower, adjacent service, not "SEO"
in the full technical sense — do not market it as full SEO.

**What this is NOT, and never claim it is:**
- Not a ranking guarantee. Local Pack position is an algorithmic outcome
  shaped by competitors and Google's own changes — sell the process and the
  monthly effort, never a promised position or timeline.
- Not 95% automatable. Review-response drafting and citation bulk-checks
  can be templated; actually writing personalised responses, judging tone,
  and resolving citation conflicts (same business listed under two slightly
  different names/addresses) requires a human pass every time. Say this to
  the client up front — it's also the honest reason the price isn't €50/month.
- Not a substitute for review generation ethics: only prompt real customers
  for honest reviews, at a natural moment (after service, on the invoice, via
  a follow-up text). Never incentivise, never gate by star rating, never
  write or edit a review on the client's behalf. This is a Google policy
  violation with listing-suspension risk, and it undermines the exact metric
  you're selling.

## 2. Lead identification logic

**What Places-style APIs can give you directly:** category, address, phone,
rating, review count, whether a website/social link exists.

**What no API gives you directly:** Local Pack rank for a specific keyword
in a specific location. This is query- and location-dependent and Google
does not expose it as queryable data. Two honest paths:

- **Manual (no new cost, slower):** search `"{core service}" Cluj-Napoca`
  (and 2–3 nearby localities) from a location matching the target area,
  screenshot or note the top 3 vs. positions 4+. Cap this at ~10 keyword
  searches per session — it does not scale the way Offer A's scan does, and
  should not be pretended to.
- **Paid rank-tracking API (DataForSEO, SerpApi, or similar):** removes the
  manual bottleneck at a real, recurring cost — evaluate this only after
  Offer B shows it converts; do not add a second paid tool before the offer
  is validated.

**Filter criteria, once a candidate is found ranking 4th or lower:**
1. Has a website or an active GBP listing (this is what separates Offer B
   from Offer A — a lead qualifying for one should never also sit on the
   other list).
2. Cross-check the Google Ads Transparency Center
   (adstransparency.google.com — public, no login) for the business name or
   domain. An active ad campaign strengthens the pitch considerably: "you're
   paying per click while ranking below competitors organically." Absence of
   ads is not a disqualifier, just a weaker opening line.
3. GBP listing is claimed and has at least one review (an unclaimed or
   empty listing is a different, colder conversation — log separately).

**Deduplication (mandatory):** before adding a lead to the Offer B list,
check it is not already in `pipeline.csv` under Offer A. A business with no
website belongs to Offer A only; a business with a website ranking poorly
belongs to Offer B only. Add an `offer` column (`A` or `B`) to the shared
ledger to make this check trivial rather than memory-based.

## 3. Delivery workflow — GBP audit checklist

Run this on every qualified lead before the outreach pitch, and again as the
first deliverable after a client signs.

**Completeness**
- [ ] Primary category correct and specific (not a generic parent category)
- [ ] Secondary categories cover real services offered, none padded/irrelevant
- [ ] Services list populated with descriptions, not just names
- [ ] Business description present, keyword-relevant, no keyword stuffing
- [ ] Hours accurate, including holiday hours if seasonal
- [ ] Phone number matches the number used everywhere else (website, citations)
- [ ] At least 10 photos, dated within the last 6 months

**Review profile**
- [ ] Review velocity — new reviews at least monthly, not a stale spike
- [ ] Owner responses present on both positive and negative reviews
- [ ] No sign of incentivised or gated reviews (a compliance flag, not a
      growth opportunity — if found, this is a risk to disclose, not exploit)

**Citations (NAP — Name, Address, Phone consistency)**
- [ ] Google, Facebook, and at least 3 major Romanian directories checked
      (e.g. firme.info, paginiaurii.ro, listafirme.ro) for exact-match
      name/address/phone
- [ ] Any mismatches logged with the specific conflicting listing

**Ongoing cadence (semi-automatable — template, human reviews before posting)**
- [ ] Weekly GBP post scheduled (offer, update, or photo)
- [ ] Monthly Q&A seeding — 2–3 real, useful questions answered proactively
- [ ] Bulk citation re-check monthly (templated check, human resolves conflicts)

**What's templated vs. manual, explicitly:**

| Step | Automatable/templated | Requires manual judgment |
|---|---|---|
| Citation consistency scan | Yes — bulk check against a directory list | Resolving found conflicts |
| Review-response drafting | Yes — draft from a template bank | Final tone/personalisation before sending |
| GBP post copy | Yes — draft from a monthly content calendar | Photo selection, final approval |
| Review solicitation | No | Always a human, at the right real moment |
| Category/services audit | No — one-time judgment call per listing | — |

## 4. Outreach script (WhatsApp/Messenger, text-only — same rules as Offer A)

Same guardrails as prospector-outreach apply in full: no calls, ≤5 first
contacts/day, opt-out line in every first message, no bulk sending.

**Template 1 — first contact, ads-aware variant (if an active ad campaign
was found in the Ads Transparency Center):**
> Bună ziua! Mă numesc {name} și lucrez cu firme din zona {zonă} la vizibilitate locală pe Google. Am observat că {Firma} rulează reclame Google în acest moment, dar apare mai jos de {N} concurenți în rezultatele locale organice pentru „{cuvânt cheie}" — practic plătiți per click pentru un loc pe care alții îl au gratuit. Vă pot trimite un audit scurt, gratuit, al profilului Google Business — 10 minute de citit, fără nicio obligație. Dacă nu vă interesează, un „nu, mulțumesc" este suficient. O zi bună!

**Template 1b — no ad activity found:**
> Bună ziua! Mă numesc {name} și lucrez cu firme din zona {zonă} la vizibilitate locală pe Google. Am observat că {Firma} are un profil Google Business activ, dar apare mai jos de {N} concurenți în rezultatele locale pentru „{cuvânt cheie}" — ceea ce înseamnă clienți pierduți către ei. V-am pregătit un audit scurt, gratuit, al profilului — 10 minute de citit. Dacă nu vă interesează, un „nu, mulțumesc" este suficient și nu vă mai deranjez. O zi bună!

**Template 2 — delivering the audit (after a yes):**
> Mulțumesc! Iată auditul: {audit summary — 3-4 concrete findings, e.g. "lipsesc fotografii recente", "categoria principală nu reflectă exact serviciul", "3 din 5 citări au adresa scrisă diferit"}. Fiecare dintre acestea contează pentru cum vă clasează Google local. Dacă doriți, pot prelua această parte lunar — {price range} pe lună, fără contract pe termen lung. Vă spun clar: nu pot garanta o poziție anume, pentru că depinde și de concurență — dar aceasta este exact munca ce influențează rezultatul.

**Template 3 — follow-up, day +3:** identical structure to prospector-outreach
Template 2, referencing the audit instead of a mockup link.

**Objection handling specific to Offer B:**

- **"Cum garantați rezultatele?"** — "Nu pot garanta o poziție anume — nimeni onest nu poate, pentru că depinde și de ce fac concurenții și de actualizările Google. Ce pot garanta este munca lunară: postări, verificare citări, gestionarea recenziilor. Rezultatele tipice apar în 3-6 luni, nu imediat."
- **"Am deja pe cineva care se ocupă de reclame."** — "Perfect, reclamele și profilul Google Business lucrează pe planuri diferite — una e plătită per click, cealaltă e vizibilitate organică, gratuită pe termen lung. Deseori clienții noștri le țin pe amândouă la început, apoi reduc bugetul de reclame pe măsură ce partea organică crește."
- **"Pot face asta singur."** — "Absolut, multe din pașii de bază pot fi făcuți intern. Ce aducem noi este timpul constant — verificarea lunară, postările regulate — lucruri care se lasă de obicei la urmă când sunteți ocupat cu activitatea de bază."

## Integration with the existing pipeline

- Add an `offer` column to `data/pipeline.csv` (`A` or `B`) — everything
  else in the ledger schema and the orchestrator's status flow
  (`NEW → QUALIFIED → CONTACTED → FOLLOWUP_1 → FOLLOWUP_2 → WON/LOST`)
  applies unchanged.
- WIP limits from prospector-pipeline are shared across both offers, not
  additive, until Offer A's pilot data justifies raising total capacity —
  e.g. 3 total builds/audits per week across A+B, not 3 each.
- Report Offer A and Offer B conversion separately in the monthly review —
  merging them would hide which offer is actually working.
