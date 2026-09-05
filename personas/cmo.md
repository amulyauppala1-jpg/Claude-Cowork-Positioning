---
persona: CMO
function: Marketing
seniority: C-level
roles_by_motion:
  departmental: economic_buyer   # primary motion — owns marketing budget outright
  enterprise: champion           # CFO/CIO signs; CMO supplies demand and the internal case
applies_to: [cowork-enterprise]
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: public-research
---

# CMO

> **Read the motion first.**
>
> - **Departmental buy (primary)** — the CMO owns the budget and decides. Make a
>   case, drive to a decision.
> - **Enterprise rollout** — the CMO is a champion arming the CFO. What they need
>   is a forwardable business case in finance's language, not a marketing pitch.

## The thing that makes this buyer different from the CFO

**They have already bought AI.** 15.3% of the average marketing budget already
goes to AI initiatives, and adoption across marketing teams is close to
universal. The sale is not "try AI." The sale is *"the AI you already bought
didn't move the number, and here is why this is a different category of thing."*

> Budget figure: [Gartner 2026 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities) · tier 2.
> The adoption claim is stated directionally on purpose — the widely repeated
> percentages trace only to aggregated write-ups, so the shape is reliable and
> the decimal places are not.

Every asset for this persona has to survive that opening position. A capability
pitch reads as the fourth vendor this quarter making the same promise.

## What loses the deal

1. **It sounds like the AI they already have.** They have chat assistants. If
   Cowork is described in terms of helping people write faster, it is a
   line-item duplicate — and marketing budgets are flat (7.8% of revenue, 18%
   below four years ago), so a duplicate has to displace something.
2. **Brand risk.** AI content governance has moved from a content-team concern to
   an executive accountability question, now appearing in board-level disclosure
   language and enterprise procurement checklists. Anything that reads as
   "generate more content faster" activates this. It is the fastest way to lose
   a CMO who otherwise wanted to say yes.
3. **The review-cycle trap.** The most precise statement of the failure mode:
   teams end up producing more mediocre work faster, and burning the saved time
   on review. Generation accelerated; approval didn't. **This is the mechanism
   behind why `vp-executes` leads** — a tool that produces more drafts moves work
   from creation into review rather than removing it. If Cowork is positioned as
   a faster drafter, it walks straight into a failure they have already lived.
   > Source: [Timothy Young, LinkedIn, 2026](https://www.linkedin.com/posts/timhyoung_i-talk-with-enterprise-cmos-and-marketing-activity-7491248391998484480-NRRv/) · confidence: practitioner opinion (synthesized from many CMO conversations; still n=1)

4. **Unmeasurable outcome.** Marketing leaders overwhelmingly prioritize
   demonstrating ROI, while only around a third report being able to measure it
   accurately — and AI-specific KPI tracking is rarer still. A tool that cannot
   be attributed becomes the first thing cut.
   > Source: [ABM Alliance, CMO AI challenges 2026](https://abmalliance.com/news/cmo-and-ai-marketing-challenges-2026) · tier 3 — aggregated. Ratio is reliable; exact percentages trace to secondary write-ups, so state it directionally.

## Personal exposure — read this before writing anything

This buyer is materially more exposed than the CFO, and it changes the tone.

- CMO tenure at S&P 500 firms has fallen to **4.1 years**.
- Board pressure on CMOs rose **21%** from 2023 to 2025; pressure specifically
  from the **CFO rose 52%**.
- **62%** say missing 2026 growth expectations results in budget cuts.
- **70%** say becoming an AI leader is a critical 2026 goal, while only **30%**
  report mature AI readiness.

> Sources: tenure and pressure figures — [CMSWire, CMO survival guide 2026](https://www.cmswire.com/digital-marketing/why-the-cmo-job-is-being-rewritten-in-real-time-and-how-to-land-on-the-right-side/) · tier 2.
> AI-leadership and readiness figures — [Gartner 2026 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities) · tier 2.

They are being asked to lead on AI, judged on it, and are not resourced for it.
That gap is the emotional center of this persona. An asset that helps them look
credible to their board is doing more work than one that explains a feature.

> **Two limits on this section.**
>
> *Epistemic:* these are aggregate survey figures, not one person's account —
> but they describe a population, not the buyer in front of you. Plenty of CMOs
> are secure, well-resourced, and three years into a mandate. Treat this as
> shaping the repo's point of view on the role, not as a profile of any
> individual. Read the room before assuming any of it applies.
>
> *Tactical:* don't use it as leverage. Fear framing reads as manipulative to a
> sophisticated buyer and will backfire. The use is knowing what they may be
> carrying, not naming it back at them.

## What already ships for this function

Check this before writing anything — assets that describe Cowork generically to
a CMO are leaving the strongest material on the table.

The **marketing plugin** is public and open-source: `/draft-content`,
`/campaign-plan`, `/brand-review`, `/competitive-brief`, `/performance-report`,
`/seo-audit`, `/email-sequence`, connecting Slack, Canva, Figma, HubSpot,
Amplitude, Ahrefs and Klaviyo. Full detail in `products/cowork-enterprise.md`.

Two of those commands answer objections in this file directly:

- **`/brand-review`** — reviews content against brand voice and style guide.
  The brand-risk objection has a shipped answer, not a reassurance. Lead with it
  when brand risk comes up rather than arguing about governance in the abstract.
- **`/competitive-brief`** — this is the Snowflake competitive-intelligence agent,
  shipped. It substantially changes the answer to "do I have to build that?"

**Anthropic's own marketing ops team** is the closest available proof: a weekly
metrics review cut from one-to-two days to roughly two hours, and multi-day
campaign builds automated across Salesforce, HubSpot, Swoogo and Asana. The
governance design matters as much as the number — a separate audit agent
verifies output, a proofreading skill checks figures against sources, and a
human approves before anything ships. That structure is the honest answer to
"how do I stop this producing off-brand work at scale": **review is built into
the workflow, not bolted on after.**

> Cited in `products/cowork-enterprise.md` (Anthropic blog, 2026-07-08 — 59 days
> old, inside the 90-day ceiling). Use the product file's wording as the source
> of truth.

## Value props, ranked for this buyer

> **Departmental motion.** In an enterprise motion `vp-coverage` moves up, since
> they are then helping the CFO justify org-wide spend rather than buying for
> their own team. **This ranking is close to the inverse of the CFO's** — the
> clearest evidence that ranking by motion is doing real work.

1. **`vp-executes`** — leads. This is the only prop that answers the opening
   position. They own tools that produce drafts; the claim that matters is
   finished output. The distinction between *assistance* and *completed work* is
   the entire sale here, and it should be concrete: name the deliverable, not
   the capability.
2. **`vp-configured`** — strong second, and it answers the readiness gap
   directly. Young's framing is the cleanest articulation of why this prop
   matters at all: access to AI is no longer an advantage because everyone has
   it; the advantage is the operating model. That is `vp-configured` restated in
   the buyer's own terms. 57% say they lack the talent to execute their 2026 strategy and 56%
   say they lack the budget. ([Gartner 2026 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities) · tier 2)
   They cannot hire maturity. Configuration is the
   substitute — plugins carry the process knowledge their team doesn't yet have.
3. **`vp-coverage`** — last in a departmental motion. That every knowledge worker
   gets Cowork is irrelevant to someone buying for their own function, and
   raising it invites the "so this is really an IT project" objection, which
   moves the decision away from their desk.

## Vocabulary

**Use:** pipeline · attribution · brand safety · governance · capacity ·
finished work · review cycle. Anchor claims to something measurable — this
buyer's core wound is spending they can't attribute.

**Two metrics specifically.** Boards are reported to want *agency-spend
reduction* and *pipeline influence*; **time-saved does not persuade them.** This
is the sharpest vocabulary guidance in this file — it names the two numbers a
CMO can actually carry upward, and rules out the metric most AI tools lead with.
(Source: [Timothy Young, LinkedIn, 2026](https://www.linkedin.com/posts/timhyoung_i-talk-with-enterprise-cmos-and-marketing-activity-7491248391998484480-NRRv/) · practitioner opinion)

**Avoid:**
- **"Content at scale" / "10x your content."** The single worst framing
  available. It activates the brand-risk objection and describes a problem they
  already have rather than one they want.
- **"Productivity."** Burned for the CFO because it was never substantiated;
  burned for the CMO because it implies commodity output.
- **"Creative"** as a thing the tool does. Threatens the team and picks a fight
  you don't need — position against the work *around* the creative.
- **"Replace your agency."** Procurement implication they didn't ask for.

## Objections

**"We already spend 15% of our budget on AI. What did that buy me?"**
> Source: [Gartner 2026 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities) · confidence: public research
> **The opening position, not an objection to overcome later.** Answer with
> `vp-executes` and a named deliverable. Do not answer with capability.

**"How do I stop this producing off-brand content at scale?"**
> Source: [eMarketer on AI brand safety 2026](https://www.emarketer.com/content/faq-on-brand-safety--how-ai-content-creator-marketing-reshaping-risk-2026); [CEOWORLD on AI content as brand risk](https://ceoworld.biz/2026/05/21/ai-content-is-a-real-brand-risk-smart-executives-are-already-one-step-ahead/) · confidence: public research
> Route to `vp-configured`, and be specific: `/brand-review` checks content
> against brand voice and style guide, and Anthropic's own marketing workflows
> put a separate audit agent plus human approval in front of anything shipping.
> Then the Compliance API proof point in `products/cowork-enterprise.md` for the
> auditability half. **Answer with the mechanism, not with reassurance** — this
> objection is on procurement checklists and a vague answer fails the checklist.
> **This objection is now on procurement checklists**, so it will be asked
> formally even if the CMO personally doesn't care.

**"My team isn't ready for this."**
> Source: [Gartner 2026 CMO Spend Survey](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities) (30% mature readiness; 57% lack talent) · confidence: public research
> Genuine, not a brush-off. `vp-configured` is the answer: the readiness is
> shipped in the configuration rather than hired.

**"If we miss targets this gets cut anyway."**
> Source: 62% expect cuts on missed 2026 growth ([Gartner via CMSWire](https://www.cmswire.com/digital-marketing/why-the-cmo-job-is-being-rewritten-in-real-time-and-how-to-land-on-the-right-side/)) · confidence: public research
> Not really an objection — a request to be tied to a growth number rather than
> an efficiency one. Efficiency framing puts Cowork in the cut pile.

## What they need to say yes
A named deliverable their team currently pays for or can't get to, produced
end-to-end, with an attribution story their CFO will accept. Note the second
half: this buyer is increasingly selling *upward* even in a departmental motion,
because CFO pressure on marketing rose 52% ([CMSWire, CMO survival guide 2026](https://www.cmswire.com/digital-marketing/why-the-cmo-job-is-being-rewritten-in-real-time-and-how-to-land-on-the-right-side/) · tier 2).

> TODO(source): no `pricing/` content. Less blocking than for the CFO — a
> departmental buy clears at a lower threshold — but still unanswerable.

## Who else is in the room
- **CFO** — approves above threshold, and pressure from this direction is rising
  fast. See `personas/cfo.md`; the consolidation argument that wins there is the
  wrong lead here.
- **Brand / Comms lead** — owns the brand-risk objection in practice and can
  block on it.
- **Marketing ops** — evaluates integration and attribution. Often the real
  evaluator of whether the tool can be measured at all.
- **Agency partners** — threatened by the purchase. Handle deliberately.

> TODO(source): committee shape inferred, not observed. Confirm against win/loss.

## What `vp-configured` actually looks like — the Snowflake reference

`vp-configured` is the hardest prop to make concrete. "An agent that knows how
your company works" is abstract until someone sees one. Snowflake's GTM
programme is the clearest public picture of the finished thing, and it maps to
this buyer's two problems almost exactly.

**Campaign agent — answers the attribution wound.** Real-time ROI by campaign,
automatically reallocating digital ad spend across channels. This is the direct
answer to the objection at the top of this file: the CMO who cannot say what
their AI spend returned is describing the absence of exactly this.

**Competitive intelligence agent — answers the combinatorial problem.** Instant
talking points customized to a specific competitor, use case, and industry.
The reason this matters is arithmetic: enablement coverage is competitors ×
use cases × industries, which is a *product*, not a sum. Twelve competitors
across eight use cases and six industries is 576 combinations. No enablement
team staffs against that, so in practice reps improvise and the positioning in
`products/cowork-enterprise.md` never survives contact with the deal. An agent
trained on the real material closes that gap at scale.

Note what both examples have in common: they are trained on **live operating
data** — campaign performance, competitive material, customer context — not on
general knowledge. That is the substance behind `vp-configured`, and it is why
the prop is second rather than third for this buyer despite sounding like an
IT concern.

**Use this to show a CMO the destination**, especially one who has only ever
seen chat assistants. It reframes the category from "writes things faster" to
"operates on our data" — which is the same reframe `vp-executes` needs.

**The buyer's next question is "do I have to build that?"** Snowflake did, with
an executive mandate and an internal AI council on 20% time. But the answer is
now largely **no**: `/competitive-brief` ships in the marketing plugin. The
honest version is that the shipped command is a starting point and Snowflake's
was tuned to their own data over time — so the gap is customization depth, not
existence. That is a far better position than "you could build this too," and
it is the single strongest use of this reference. Expect technically confident
enterprises to consider building regardless.

> Source: [Jason Lemkin, LinkedIn, 29 Oct 2025](https://www.linkedin.com/pulse/snowflakes-ai-revolution-how-transformed-marketing-sales-lemkin-n8ltf/) · confidence: practitioner opinion
>
> **Not a proof point.** A third party's account of another company's internal
> build — not a Cowork customer outcome, and never to be presented as one. At
> ~10 months it is also well past the 90-day ceiling governing proof points in
> `products/cowork-enterprise.md`. Use it to illustrate the category and shape a
> point of view; cite the product file's own proof points as evidence.
>
> Cross-reference: the competitive-intelligence example belongs in the CRO
> persona too — marketing builds it, sales carries it.

---

## Sourcing note

Confidence tiers as defined in `cfo.md`. All content here is `public research`
from 2026 analyst and trade sources, cited inline. No connector data — nothing
from call recordings, win/loss notes, or a quote database.

**Highest-value additions when connectors land:** whether brand risk or
measurement is the actual blocker in lost deals — the public data says both
matter, but not which one kills more deals.
