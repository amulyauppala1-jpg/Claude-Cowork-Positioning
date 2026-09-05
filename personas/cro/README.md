---
persona: CRO
function: Revenue / Sales
seniority: C-level
roles_by_motion:
  departmental: economic_buyer   # primary motion — owns the sales tooling budget
  enterprise: champion           # CFO/CIO signs; CRO supplies demand and the pipeline case
applies_to: [cowork-enterprise]
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: public-research
---

# CRO

> **Read the motion first.**
>
> - **Departmental buy (primary)** — the CRO owns the budget and decides.
> - **Enterprise rollout** — champion. They need a pipeline-impact case the CFO
>   will accept, not a sales-tooling pitch.

## Positioning — value proposition

> **For** a revenue leader whose reps ignore the sales AI they already own
> **that need** tooling shaped around how their team already sells
> **Cowork** **is an** agentic workspace configured to the sales motion
> **that** produces forecasts, pipeline reviews and call prep from the material
> the team already has — including with no CRM connection.

## Positioning — differentiation

> **Unlike** sales AI that requires reps to change behaviour before it returns
> anything
> **Cowork provides** value in the leader's own hands on day one, independent
> of rep adoption.

> Structured to Geoffrey Moore's framework. It narrows the function-agnostic
> statement in `products/cowork-enterprise.md` — it does not replace or
> contradict it. **The "unlike" is the part that earns scrutiny:** it names the
> alternative *this buyer* is actually weighing, which differs by role and is
> where a weak differentiation claim shows up.
>
> `TODO(source)`: synthesized from the public research cited in this file, not
> from customer interviews. The framework organizes insight; it does not create
> it, so treat these as a hypothesis to test against real buyers.

## The ladder

Laddering: climb from what the product *is* to what it *means* for this buyer.

| Rung | |
|---|---|
| **1. Feature** | Configured to your sales motion; runs without a CRM connection |
| **2. Functional benefit** | Forecasts, pipeline reviews and call prep produced from what the team already has |
| **3. Business outcome** | Selling time recovered without waiting on reps to change behaviour first |
| **4. What it means for them** | This is the AI investment that didn’t get quietly abandoned at renewal |

**Lead from rung 2 or 3. Never rung 1.** A feature-led opening is the most
common failure in B2B copy, and it is structurally fine — it just argues at the
wrong altitude. Rung 3 is where a business case lives; rung 2 is where a first
conversation lives.

**Rung 4 shapes emphasis; it is rarely said out loud.** Naming a buyer's
personal exposure back to them reads as manipulative and costs you the room.
Use it to decide what to lead with, not as a line in the asset.

## The opening position — and it's a third distinct one

The three personas in this repo start from three different places, and confusing
them produces generic assets:

| Persona | Where they start |
|---|---|
| CFO | "Prove the return." Hasn't bought, or can't measure what they did buy. |
| CMO | "I already bought AI and can't show it worked." Bought, unmeasured. |
| **CRO** | **"I already bought AI and my reps won't touch it."** Bought, unadopted. |

The number that defines this buyer: **only 19% of individual reps actually use
the AI features already built into their sales tools** — and while a large
majority of teams claim AI adoption, only about a quarter have embedded it into
revenue workflows.

> Rep-usage figure: [Salesforce State of Sales 2026](https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/) · tier 2. The adoption-versus-embedding gap is
> reported by [Momentum.io's Voice of the Market](https://www.businesswire.com/news/home/20260127999573/en/Momentum.io-Newest-2026-Voice-of-the-Market-Report-Finds-Most-AI-Adoption-Stops-Short-of-Revenue-Execution) · tier 2, stated directionally here.

So the sale is not capability and not measurement. It is **adoption**. A CRO has
already watched a tool they bought go unused, and every claim you make is heard
through that.

## What loses the deal

1. **It looks like another tool to log into.** 70% of sellers report feeling
   overwhelmed by the technology needed to do their job. Anything framed as an
   addition rather than a removal is dead on arrival with the people who have to
   use it — and the CRO knows it.
2. **It pattern-matches to a cancelled project.** Gartner expects task-specific
   AI agent adoption to jump from under 5% to 40% during 2026, while **over 40%
   of those projects get cancelled** over escalating cost and unclear value. This
   buyer may already have one in the graveyard.
3. **It depends on CRM data they don't trust.** CRM data quality is a known,
   widely felt problem — no CRO needs convincing. A pitch resting on "it reads
   your CRM" invites the objection rather than answering it.

## Measured on
Quota attainment, win rate, sales cycle length, deals per rep, average deal size,
and ramp time. Boards are reported to want payback periods under 18 months.

The structural backdrop is genuinely bad and worth understanding directionally:
enterprise sales cycles have lengthened materially since 2022, buying committees
have expanded well into double digits, enterprise win rates have compressed, and
security and procurement review adds weeks of structural delay per deal.

**Stated without numbers deliberately.** Specific figures for each of these
circulate widely but trace only to aggregated write-ups restating other people's
data. The direction is well supported; the precision is not, and a number quoted
to a CRO who knows the real one is worse than no number.

> `TODO(source)`: replace with primary research — an analyst firm's own survey,
> or Anthropic data if it covers this — and only then restore specific figures.

> Source: [Cyberbase, revenue team challenges 2026](https://www.cyberbase.ai/blog/revenue-team-challenges-2026) · confidence: **tier 3 — aggregated secondary**
> Lowest-ranked source in this file. Figures are restated from elsewhere without
> primary citation. Use for shape and context only; never quote a number from
> here externally without tracing it to its origin. Prefer the Salesforce and
> Anthropic figures below wherever they cover the same ground.

**CRO tenure is widely reported as shorter than the CMO's 4.1 years** — often
cited under two years, though again the specific range traces only to aggregated
sources. Treat the direction as reliable and the number as not.

> Same epistemic limit as the CMO file: this describes a population, not the
> person in front of you, and it shapes the repo's POV rather than profiling an
> individual. Do not use it as leverage.

## What already ships for this function

The **sales plugin** is public and open-source. Detail in
`products/cowork-enterprise.md`.

- **`/call-summary`** — call notes or transcripts into structured summaries with
  action items and draft follow-ups.
- **`/forecast`** — weighted forecasts with best/likely/worst from a CSV or a
  pipeline description.
- **`/pipeline-review`** — pipeline health, stale-deal risk flags, weekly action plan.
- **Contextual skills** — account research, call prep with discovery questions,
  daily pipeline briefings, research-based outreach, and competitive
  intelligence producing differentiation matrices and talk tracks.

Two details matter more than the command list:

**It works without connectors.** The plugin runs standalone on notes, CSV
uploads and pasted text when CRM and enrichment tools aren't wired up. That is
the direct answer to the CRM-data objection — **value doesn't wait on a data
cleanup project**, which is otherwise the thing that kills the timeline.

**`/forecast` and `/pipeline-review` are the CRO's own work, not the reps'.**
This is the wedge. Nearly everything else here depends on rep adoption, which is
the thing they've been burned on. These two produce value in the CRO's hands on
day one, independent of whether a single rep changes behaviour. Lead with them
in a first conversation and earn the adoption argument later.

## First-party evidence — use this before anything else

Anthropic's own GTM org is the most defensible material available for this
persona, and it lands directly on the adoption objection.

**Travis Bryant, Head of US Mid-Market GTM**, runs a **4,000-account book** with
Cowork. Propensity scoring across all 4,000 accounts ran **overnight** against
five-dimension rubrics combining web research, Salesforce and BigQuery, output as
an interactive dashboard with rationales — work that previously took *hundreds of
hours across RevOps, FP&A and marketing*. Plus ~90 minutes/day recovered and ~3
hours/week on forecast prep.

> **Flagged stale: 108 days old (2026-05-20), past the 90-day ceiling.** Say so
> when using it. It is kept because it is the only first-party sales evidence in
> the repo — see `products/cowork-enterprise.md`. Replacing it with something
> current is the highest-value refresh available for this persona.

Why it matters more than the category research: the overnight-versus-hundreds-of-hours
contrast is a **capacity** claim, not an efficiency one, and capacity is what a
CRO buys. It also demonstrates the wedge — this is a leader's own workflow, not
a rep behaviour change.

> `TODO(source)`: Anthropic's own internal adoption rate for the Sales plugin
> would be the strongest available answer to the rep-adoption objection below.
> No dated, citable figure located — worth sourcing.

## How practitioners actually run it

Two accounts worth knowing, both `tier 4 — practitioner`. They shape POV and
supply vocabulary; neither establishes a claim.

**Jen Allen-Knuth** runs six scheduled Cowork workflows — a Monday skill
suggester that turns repeated tasks into reusable skills, daily call prep from
calendar/email/CRM/recordings, stale-deal alerts at 7am, a prospect finder
working from news signals, a deal-risk audit cross-referencing open deals against
call recordings for thin discovery, and a Friday pattern analysis drafting
problem statements from prospects' actual language.

Her operating principle is the useful part, and it is a **strong differentiator
against the "AI SDR" category**: automation supplies *ingredients for critical
thinking*, not autonomous action — and she deliberately automates **nothing that
touches a prospect directly**. For a CRO who distrusts AI outreach, this is a
more credible posture than any capability claim.
> Source: [Jen Allen-Knuth, LinkedIn](https://www.linkedin.com/posts/demandjen1_here-are-6-ways-im-using-claude-cowork-activity-7465395638982193152-RMn8/) · confidence: practitioner (n=1)

**Sachin Bhatia, CRO at Exotel**, audited his own calendar to separate work
genuinely needing human judgment from work that was human-staffed by default. Two
things to carry forward:

- **"The bottleneck moves rather than disappears."** Automating a step surfaces
  the data-quality problem underneath it. This is honest and worth saying out
  loud to a CRO — it pre-empts the disappointment that kills renewals, and it
  pairs with the CRM objection below rather than dodging it.
- **His validation method:** two private test runs, identify false positives,
  refine the rules, then deploy live. A ready-made pilot structure to offer a
  cautious buyer.
> Source: [Sachin Bhatia, LinkedIn](https://www.linkedin.com/posts/bhatiasachin_the-cro-job-rebuilt-what-an-ai-assistant-activity-7462414896211582976-UoCd/) · confidence: practitioner (n=1, and a sitting CRO — the closest thing here to the actual buyer speaking)

> **Community skills are not product capability.** A "CS CRO Advisor" subagent
> (revenue waterfall analysis, pipeline coverage modeling, sales efficiency
> scoring) circulates via the community `borghei/Claude-Skills` repo. It is
> **not** an official Anthropic plugin. Useful as evidence that people build
> this shape of thing; never present it as something Cowork ships.

## Value props, ranked for this buyer

> **Departmental motion.** All three personas rank these differently, which is
> the clearest evidence the layer is doing real work:
> CFO leads `vp-coverage` · CMO leads `vp-executes` · **CRO leads `vp-configured`.**

1. **`vp-configured`** — leads, because it *is* the adoption answer. The research
   is explicit that the gap is workflow fit: teams automate what the vendor demo
   showed rather than what would improve their actual motion, and the fix is
   showing reps how AI fits their existing day. An agent pre-configured to their
   sales process is that, stated as a product property rather than a services
   engagement. Reps who genuinely internalize AI into their motion are reported
   to see a substantial quota-attainment advantage — the prize is large *if*
   adoption happens, which is why this prop leads.
   > Seller-overwhelm figure: [Salesforce State of Sales 2026](https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/) · tier 2. The quota-advantage
   > multiple circulating in trade coverage traces only to aggregated sources, so
   > it is stated without a number. `TODO(source)`: pin to primary research.
2. **`vp-executes`** — strong second, and it must be framed as *removal*. 70% are
   already overwhelmed. A call summary that arrives finished removes a task; a
   tool that helps write one adds an app. Say the deliverable, never the feature.
3. **`vp-coverage`** — last in a departmental motion, and raising it early
   converts a sales decision into an IT project that leaves their desk.

## Vocabulary

**Use:** quota attainment · ramp time · win rate · cycle length · pipeline
hygiene · rep capacity · selling time. Frame everything as **removing** steps or
tools, never adding.

**Avoid:**
- **"Another tool / platform / dashboard."** Naming the category triggers the
  overwhelm objection directly.
- **"AI SDR."** Crowded, burned category with a poor reputation among buyers who
  have tried one. Cowork is not this and shouldn't borrow its language.
- **"Replace reps"** or headcount framing. Politically impossible for a leader
  who needs those reps to hit a number this quarter.
- **"Efficiency."** Reps don't buy efficiency, and CROs buy attainment.

## Objections

**"My reps won't use it. Only a fraction use what we already pay for."**
> Source: [Salesforce State of Sales 2026](https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/); 19% rep feature usage / 24% workflow embedding · confidence: public research
> **The central objection — everything else is secondary.** Answer with
> `vp-configured`, and open with `/forecast` and `/pipeline-review`, which pay
> off in the CRO's hands regardless of rep behaviour. Do not promise adoption;
> show value that doesn't depend on it.

**"Our CRM data is a mess. What is it even working from?"**
> Source: CRM data quality is a widely reported problem; the specific inaccuracy
> rates in circulation trace only to aggregated write-ups
> ([Cyberbase](https://www.cyberbase.ai/blog/revenue-team-challenges-2026)) · confidence: **tier 3**
> Don't quote a percentage here. The objection is real and the buyer already
> believes it — you gain nothing by putting a contestable number on it.
> Answer with the standalone mode: the plugin works from notes, transcripts and
> CSVs without connectors. Value before cleanup. Then the Compliance API proof
> point in `products/cowork-enterprise.md` for the governance half.
> **Then concede the honest part** — Bhatia's "the bottleneck moves rather than
> disappears." Automation surfaces the data problem rather than removing it.
> Saying this first is more credible than being caught by it in month three, and
> it reframes cleanup as a known step rather than a broken promise.

**"We cancelled our last AI project."**
> Source: Gartner — >40% of task-specific AI agent projects expected to be
> cancelled over cost and unclear value · confidence: public research
> Ask what was cancelled and why before answering. Cost overrun and unclear
> value are different failures: the first is the CFO's token-cost objection in
> `personas/cfo.md`, the second is `vp-configured`. Guessing wrong here is worse
> than asking.

## What they need to say yes
A named workflow that produces something in their own hands within a week —
realistically a forecast or a pipeline review — plus a credible adoption path
for the rep-facing half. The first earns the meeting; the second closes it.

> TODO(source): no `pricing/` content. Departmental threshold, so less blocking
> than the CFO, but unanswerable.
>
> TODO(source): **no first-party sales proof point exists in this repo.**
> `products/cowork-enterprise.md` carries an Anthropic marketing-ops example but
> nothing equivalent for sales. This is the most valuable single addition for
> this persona — a sales-team workflow with a number attached.

## Who else is in the room
- **CFO** — approves above threshold. See `personas/cfo.md`; note their token-cost
  objection lands hard here, since agentic prospecting is consumption-heavy.
- **Sales ops / RevOps** — the real evaluator. Owns CRM integration and will be
  asked whether the data supports it. Win them first.
- **Front-line sales managers** — where adoption is actually won or lost. A CRO
  can buy it; managers decide whether it gets used.
- **CMO** — cross-functional ally. The competitive-brief material in
  `personas/cmo.md` is built by marketing and carried by sales; the combinatorial
  enablement problem described there is felt most acutely here, and worsens as
  buying committees expand toward 13 people.

> TODO(source): committee shape inferred, not observed.

---

## Sourcing note

Confidence tiers as defined in `cfo.md`. Note that the structural figures
(cycle length, win rates, CRM accuracy, tenure) come from an aggregated vendor
blog rather than a primary survey — directionally consistent with the wider
picture, but verify before any external use. The adoption figures come from
Salesforce's State of Sales and are firmer.

**Highest-value additions when connectors land:** which of the three failure
modes — never adopted, cancelled on cost, or blocked by data quality — actually
kills the most deals. All three are documented; their relative weight isn't.
