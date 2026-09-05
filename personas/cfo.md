---
persona: CFO
function: Finance
seniority: C-level
roles_by_motion:
  departmental: approver        # appears above a spend threshold on someone else's buy
  enterprise: economic_buyer    # owns the budget and the decision
applies_to: [cowork-enterprise]
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: public-research   # public-research | connector-sourced | synthetic-mixed
---

# CFO

> **Read the motion first.** This persona's role changes with the deal shape, and
> so does the asset.
>
> - **Enterprise rollout** — the CFO is the economic buyer. Everything below
>   applies as written. Make a case, drive to a decision.
> - **Departmental buy** (a CMO or CRO landing Cowork for their function) — the
>   CFO is an approver above a spend threshold. The consolidation argument is
>   weaker, because only one function's tools are being collapsed. Lead instead
>   with the function head's business case and use this file only to pre-answer
>   what finance will ask.
>
> But do not mistake "economic buyer" for "receptive audience." The evidence bar
> here is higher than for any other buyer, and the objections below are not
> obstacles to route around — **they are the decision criteria.** An asset that
> handles them is the pitch. An asset that leads with capability and saves them
> for a FAQ will lose to one that doesn't.

## What they own
Budget authority over the line item, and the renewal. In 2026 the role has
expanded past cost control into capital allocation and — increasingly —
governing AI spend as a portfolio rather than approving it case by case.

## What loses the deal

1. **It looks like a duplicate line item.** This is the sharpest risk. At median
   enterprise scale companies run 305 SaaS apps against $55.7M of spend, with
   51% of licenses unused and ~15% of spend sitting on outright duplicates — and
   duplicate subscriptions now cost roughly 3x what they did in 2024 because each
   one stacks an AI surcharge on the base fee. A CFO who files Cowork next to
   Copilot and ChatGPT Enterprise has already decided.
2. **No attributable financial outcome.** Fewer than a third of decision-makers
   can point to a specific financial result from their AI investments. The ask
   isn't "will this help" — it's "what number moves, and when."
3. **Adoption risk.** They've watched Copilot land at low single-digit sustained
   adoption and struggled to justify the incremental $360/user/year. Shelfware
   with an AI label is the specific failure they're guarding against.

## Where the money comes from

Ask early, because it changes the entire shape of the pitch. AI funding is drawn
from one of three places, and they behave completely differently:

- **Innovation budget** — a pilot with a death date. Renewal is a fresh fight
  and the default outcome is quiet non-renewal.
- **Functional budget** (the CRO's, the CMO's) — permanent, and the function
  head becomes your champion. This is the one to aim for.
- **Headcount allocation** — the money is real and durable, but you have
  implicitly promised an FTE outcome. Only take this if the math survives review.

> Source: [Murray Newlands, Open Future Forum, Aug 9 2026](https://murraynewlands.substack.com/p/the-questions-san-francisco-cfos) · confidence: practitioner opinion (single source, not survey data)

**Confirmed by a sitting CFO on the record.** Pothier describes renegotiating
existing software contracts specifically, in his words, to "go fund my AI
investment" — the money is being moved, not created. This is the consolidation
thesis stated by a buyer rather than inferred from spend data, and it's the
single strongest support for leading with `vp-coverage`.
> Source: [Gordon Pothier, CFO of Board, Bloomberg Businessweek Daily, Aug 2026](https://www.youtube.com/watch?v=jQ3DKTDMFx4) · confidence: primary source (named, on record, n=1)

### Which category, not just which budget

One level below the budget-source question: how the spend gets *classified*.
Discretionary categories (R&D, innovation, "digital transformation") are the
first cut in a squeeze. Cost-of-delivery is protected, because cutting it means
not shipping.

**This argument is only available in some businesses.** Where the deliverable
*is* knowledge work — agencies, consultancies, law firms, professional services
— Cowork can credibly sit near cost of delivery. In manufacturing or retail it
is overhead, and claiming otherwise will not survive a finance review. Qualify
before reaching for it.

> Source: analysis, not sourced research · confidence: `analysis`
> Prompted by the COGS-vs-R&D framing attributed to Anthropic CFO Krishna Rao in
> secondary commentary. **That attribution could not be verified** — it does not
> appear in the [available clip](https://www.youtube.com/watch?v=AOPrW8Jc94s),
> and the [full episode](https://www.youtube.com/watch?v=wEEZPpx8qow) exposes no
> retrievable transcript. Do not cite Rao for this. What *is* verifiable from the
> clip is a CFO treating large tech procurement as strategic and time-consuming
> (30-40% of his time), which supports the economic-buyer model directionally —
> though note he is buying his own company's cost of goods, which is not the
> customer's situation.
>
> TODO(source): confirm from a primary transcript before using externally.

## Measured on
Opex predictability and run-rate. Forecast accuracy. Margin. Increasingly,
pricing power — 86% of finance chiefs plan to increase emphasis on pricing in
2026. Note the posture: cost discipline is *surgical*, not across-the-board —
trimming corporate IT, HR and marketing while protecting spend that
differentiates. Cowork must be argued into the second bucket.

## Value props, ranked for this buyer

> **Ranking below assumes an enterprise motion.** In a departmental buy,
> `vp-coverage` drops to last — "every knowledge worker gets it" is not a
> selling point to someone buying for forty people — and `vp-executes` leads,
> because the function head is buying capability for a specific job.

1. **`vp-coverage`** — leads in an enterprise motion, and it isn't close. One vendor across every
   function is a *consolidation* story, and consolidation is the CFO's own
   language for the problem they already have. This reframes Cowork from a new
   line item into a way to collapse several — the single most useful move
   available at this desk.
2. **`vp-configured`** — directly answers the adoption fear. The documented
   failure mode is AI that's bought broadly and used shallowly; "already knows
   how to work at your company on day one" is the counter. Supporting, not
   leading — it only matters once they've stopped seeing a duplicate.
3. **`vp-executes`** — weakest here, and deliberately last. It's true, but it's
   the claim every AI vendor has made to this person for three years, and the
   confidence gap is documented: 39% of CFOs prioritize accelerating AI in
   finance while only 36% feel confident of real enterprise impact. Leading with
   capability spends credibility rather than building it. *Do not promote this
   without a customer-specific number attached.*

## Vocabulary

**Use:** consolidation · run-rate · spend visibility · per-seat · renewal ·
vendor count · capacity · **operating evidence** · **business case ownership**.
Anchor to *avoided* spend where you can — it's more credible to this audience
than projected gains. The last two signal a shift from pilot justification to
permanent budget accountability; using them shows you know which conversation
you're in.

**"Should we," not "can we."** Pothier returns to this repeatedly — the internal
question has moved from whether AI *can* do something to whether it *should* be
relied on. Capability framing reads as naive to this buyer; judgment framing
reads as peer-level. (Source: [Gordon Pothier, CFO of Board, Bloomberg Businessweek Daily, Aug 2026](https://www.youtube.com/watch?v=jQ3DKTDMFx4))

**Avoid:**
- **"Productivity"** unqualified. Burned word. Every AI vendor has used it, and
  it's the exact claim the ROI data has failed to substantiate.
- **"Efficiency" without a number.** Reads as a dodge.
- **"Transformation."** Reads as expensive and slow.
- **Headcount-reduction framing.** Not for the CHRO's reasons — a CFO will simply
  hold you to it at renewal. Promise capacity, not FTE savings, unless you can
  defend the math.

## Objections

**"We already pay for Copilot and ChatGPT Enterprise. Why is this a third line item?"**
> Source: [Coommit duplicate-SaaS benchmark 2026](https://coommit.com/blog/duplicate-saas-subscriptions-2026-benchmark); [CloudEagle on managing Copilot/ChatGPT/Gemini together](https://www.cloudeagle.ai/blogs/manage-copilot-chatgpt-enterprise-and-gemini-from-one-place) · confidence: public research
> **Answer with `vp-coverage`.** Don't argue Cowork is better — argue it's fewer.

**"Show me the ROI. Our last AI initiative never produced a number."**
> Source: [Gartner via aibusinessweekly](https://aibusinessweekly.net/p/enterprise-ai-spending-cfo-scrutiny-roi-2026) (<1/3 can identify financial outcomes); Forrester (25% of planned AI spend deferred to 2027) · confidence: public research
> **Weakest position.** See gap below — there is no pricing or TCO content in
> this repo to answer with. Flag rather than improvise.

**"What if it lands at 3% adoption like Copilot did?"**
> Source: [eMarketer on Copilot cost vs. results](https://www.emarketer.com/content/microsoft-copilot-fails-impress-businesses-due-high-costs-limited-results) · confidence: public research
> **Answer with `vp-configured`**, then the usage proof point in `products/cowork-enterprise.md` —
> >90% of Cowork usage being non-engineering is evidence of breadth, not just claims of it.

**"Can I trust the data it's working from?"**
> Source: 35% cite data trust/reliability as top ROI barrier; only 10% fully trust their enterprise data ([CFO.com](https://www.cfo.com/news/so-far-few-cfos-see-substantial-roi-from-ai-spending-RPG/808249/)) · confidence: public research
> Route to the Compliance API proof point in `products/cowork-enterprise.md`. Note this is usually a
> CISO/GC question the CFO is relaying — see who else is in the room.

**"Did this reduce hiring, increase output, or just add software expense?"**
> Source: [Murray Newlands, Open Future Forum, Aug 9 2026](https://murraynewlands.substack.com/p/the-questions-san-francisco-cfos) · confidence: practitioner opinion
> The sharpest framing of the adoption fear available — a forced trichotomy where
> the third option is the accusation. Answer with `vp-coverage` (avoided spend is
> a defensible third answer: not more output, *fewer line items*). Do not claim
> reduced hiring without defensible math — see vocabulary.

**"What happens to this cost when usage grows?"**
> Source: [Gordon Pothier, CFO of Board, Bloomberg Businessweek Daily, Aug 2026](https://www.youtube.com/watch?v=jQ3DKTDMFx4) · confidence: primary source (named, on record, n=1)
> Pothier frames it as not wanting a dependency with "cost to go out of control
> later on," and describes tracking token usage at a functional level.
> **The most dangerous objection for an agentic product specifically.** Agents
> consume far more than chat, so this buyer's instinct is correct. It attacks
> forecast accuracy — a number they're measured on — not just budget size.
> No content in this repo answers it.
>
> TODO(source): needs the commercial model. Until `pricing/` exists, say so.

**"Who owns the business case after the vendor leaves?"**
> Source: [Murray Newlands, Open Future Forum, Aug 9 2026](https://murraynewlands.substack.com/p/the-questions-san-francisco-cfos) · confidence: practitioner opinion
> Post-purchase accountability, not a purchase objection — and the only one here
> that no product capability answers. It needs a named internal owner and a
> review cadence. Route to the deal team — no product content answers it.

## What they need to say yes
A per-seat number set against current AI spend across the tools Cowork
consolidates. Everything above is framing; this is the artifact that closes it.

> **BLOCKING GAP — `TODO(source)`.** No `pricing/` content exists in this repo.
> When the CFO was modeled as an approver this was a weakness. As the economic
> buyer it is a hole in the middle of the primary asset: the person who signs
> cannot sign without a number. Every other section here is preparation for a
> conversation this repo cannot currently finish.
>
> Until `pricing/` exists, assets for this persona must state that commercial
> terms are unavailable rather than estimate them — and whoever uses one should
> know they are carrying an incomplete document.

## Who else is in the room
The CFO decides; everyone else shapes the decision.

- **CIO / Head of IT** — owns implementation and technical evaluation. Their
  sign-off de-risks the purchase but does not fund it. Route deployment and
  integration questions here rather than answering them in the CFO asset.
- **CISO / General Counsel** — gate on data handling. They can block; they
  cannot approve. See the GC profile.
- **Function heads (CRO, CMO, CHRO)** — supply the demand signal, and their
  budgets are the line items being consolidated. This is the structural point:
  **the consolidation story only works if the function heads want it**, because
  it's their tools being collapsed. Without them the CFO is being asked to
  approve a new expense, not a swap.

> TODO(source): committee shape inferred from the buyer definition in
> `products/cowork-enterprise.md`, not from observed deals. Confirm against win/loss
> notes — the CFO-as-economic-buyer model came from the repo owner, not from data.

---

## Sourcing note

Every claim carries an inline `confidence:` tier:

| Tier | Meaning | Weight |
|---|---|---|
| `public research` | Analyst survey or trade reporting, multiple orgs | Highest available here |
| `primary source` | A named practitioner on the record; n=1, verbatim | Best available for voice and vocabulary |
| `practitioner opinion` | One informed person's synthesis; no sample | Directionally useful, don't quote as fact |
| `analysis` | Reasoning from repo content; no external source | Internal drafts only; never cite as evidence |
| `SYNTHETIC` | Placeholder for an unattached connector | Never customer-facing |

Nothing in this file came from call recordings, win/loss notes, or a quote
database — no such connector is attached. Anything requiring that data is marked
`TODO(source)` rather than filled in.

**Caveat on the primary source:** Pothier is the CFO of a software vendor. His
own buying posture is real and on the record, but a software CFO's instincts
around token cost may run sharper than a retail or manufacturing CFO's. Treat as
one strong data point, not a representative sample.

**Highest-value additions when connectors land:** real objection ordering from
call recordings, and whether the CFO is in fact an approver or the economic
buyer in Cowork deals — the whole template rests on the former.
