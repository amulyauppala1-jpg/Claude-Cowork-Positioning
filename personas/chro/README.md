---
persona: CHRO
function: People / HR
seniority: C-level
roles_by_motion:
  departmental: economic_buyer   # owns the HR tooling budget
  enterprise: champion           # and unusually, a stakeholder in their own right — see below
applies_to: [cowork-enterprise]
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: public-research
---

# CHRO

> **Read the motion first.**
>
> - **Departmental buy** — owns the HR budget and decides.
> - **Enterprise rollout** — champion, but **not a passive one.** Unlike the CMO
>   or CRO, the CHRO has a legitimate enterprise-wide stake: they typically own
>   workforce reskilling and change management for exactly this kind of rollout.
>   `vp-coverage` therefore lands better here than with any other function head.

## Positioning — value proposition

> **For** a people leader accountable for AI outcomes their employer can be
> sued over
> **that need** AI that works from their own written policy and leaves a record
> **Cowork** **is an** agentic workspace configured to the organisation's HR policy
> **that** handles onboarding, policy and documentation work with session-level
> auditability.

## Positioning — differentiation

> **Unlike** general-purpose AI pointed at HR work with no policy grounding and
> no audit trail
> **Cowork provides** work that traces to the company's own policy and can be
> produced in a review.

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
| **1. Feature** | Operates against your written policy, with session-level auditability |
| **2. Functional benefit** | HR work gets done with a record of how it was done |
| **3. Business outcome** | Your team gets more done, and nothing new lands on your risk register |
| **4. What it means for them** | You can say yes to AI without it becoming your risk to carry |

**Lead from rung 2 or 3. Never rung 1.** A feature-led opening is the most
common failure in B2B copy, and it is structurally fine — it just argues at the
wrong altitude. Rung 3 is where a business case lives; rung 2 is where a first
conversation lives.

**Rung 4 shapes emphasis; it is rarely said out loud.** Naming a buyer's
personal exposure back to them reads as manipulative and costs you the room.
Use it to decide what to lead with, not as a line in the asset.

## The one thing to get right

Two of the four capabilities in the HR plugin — **performance review** and
**compensation analysis** — sit in the two most legally exposed domains in HR:
bias in performance systems, and pay equity. The other two, **onboarding** and
**policy guidance**, are comparatively low-risk.

**Demo onboarding and policy work, not performance reviews or comp.** The impressive-sounding features
are the ones most likely to trigger this buyer's governance objection before you
have earned the right to answer it. This is the opposite of the instinct for
every other persona in this repo, where you lead with the most powerful thing.

> First-party: [HR plugin](https://claude.com/plugins/human-resources) — performance
> review drafting from quarterly goals and feedback, compensation benchmarking
> against market data, structured onboarding plans (30-60-90), and policy
> summarization. Maker: Anthropic (verified). Tier 1.

## What loses the deal

1. **Anything that sounds like headcount reduction.** This is not squeamishness.
   Reporting indicates a large majority of boards are planning AI-driven
   workforce reductions, which means the CHRO is already being asked to execute
   them. Positioning Cowork as a headcount play either makes them the villain or
   makes you sound like you're recruiting them into it. Promise **capacity**.
2. **Unowned liability.** Employers remain liable for discriminatory outputs from
   third-party AI vendors. The vendor's compliance posture does not transfer the
   risk — it stays with the employer. A CHRO knows this and will not accept
   reassurance in place of an audit trail.
3. **No answer on bias.** The reference case is Amazon scrapping a CV screening
   tool for systematic gender discrimination, and it comes up unprompted. A
   product that touches hiring, performance or pay without a bias answer is not
   evaluable.

> Source: [IMD, "AI and the CHRO," 13 May 2026](https://www.imd.org/ibyimd/human-resources/ai-and-the-chro-redefining-human-capital-leadership/) (Trantopoulos, Ben-Hur, Wade) · tier 2 — named academic authors, business school publication.

## Timing — this is live right now

The EU AI Act compliance deadline fell in **August 2026**, i.e. *last month* as of
this file's date. High-risk-system obligations covering employment and worker
management are not a future planning item for any org with EU exposure — they
are current. US state rules add fragmented requirements on top.

**Check this date before using this file.** If it has drifted materially from
2026-09-05, the urgency framing needs rechecking rather than repeating.

> Source: IMD, as above · tier 2.

## Measured on
Retention and regrettable attrition, time-to-fill, engagement, internal mobility,
and increasingly **workforce readiness** — the share of the org equipped for
AI-changed work. Reported figures put roughly 90% of CHROs naming AI and
digitization their top concern, around 40% reporting insufficient AI knowledge
inside their own HR team, and a substantial share of current skills expected to be
obsolete by 2030.

> Source: IMD, as above · tier 2. Stated as approximations — the underlying
> surveys are cited secondhand within that piece.

## Value props, ranked for this buyer

> **Departmental motion.** The four-way split across this repo:
> CFO leads `vp-coverage` · CMO `vp-executes` · CRO `vp-configured` · **CHRO `vp-configured`.**
> The CHRO shares the CRO's lead for an entirely different reason — the CRO needs
> configuration for *adoption*, the CHRO needs it for *defensibility*.

1. **`vp-configured`** — leads, because configuration is the governance answer.
   An agent operating against your written policies, with an auditable trail of
   what it did and why, is the only form of this product a CHRO can defend to a
   regulator or a plaintiff. Generic capability is a liability surface; encoded
   policy is a control. Pair with the Compliance API proof point in
   `products/cowork-enterprise.md` — session-level auditability is the concrete
   half of this argument.
2. **`vp-executes`** — second. HR teams report lacking the AI skills to build
   anything themselves, so finished output matters more than tooling. But frame
   it on the *low-risk* workflows: onboarding plans, policy summaries, document
   organization — not performance or pay.
3. **`vp-coverage`** — third, but **stronger here than for any other function
   head**, because the CHRO often owns enterprise AI enablement. One deployment
   with one change-management effort, rather than five tools arriving
   independently, is genuinely their problem.

## Vocabulary

**Use:** capacity · readiness · enablement · internal mobility · fairness audit ·
bias testing · algorithmic governance · human-in-the-loop · auditability. The
governance vocabulary is not decoration — using it signals you understand what
they are accountable for.

**Avoid:**
- **"Headcount," "FTE savings," "do more with less," "reduce reliance on staff."**
  The most dangerous vocabulary in this repo. See above.
- **"Automate HR."** HR's defensibility rests on documented human judgment.
  Automation language tests the thing they most need to preserve.
- **"Replace recruiters / screen candidates automatically."** Straight into the
  Amazon precedent.
- **"Employee monitoring"** or anything adjacent. Different product category,
  different regulatory regime, and an instant trust failure.

## Objections

**"If it produces a biased outcome, who is liable?"**
> Source: IMD (employer liability for third-party AI outputs) · tier 2
> **The central objection.** Answer honestly: liability stays with the employer,
> which is precisely why configuration and auditability matter rather than
> vendor assurances. Route to `vp-configured` plus the Compliance API proof
> point. Do not claim the product removes this risk.

**"We're mid-EU-AI-Act compliance. Does this create a new high-risk system?"**
> Source: IMD · tier 2
> A real question, not a stalling tactic — employment and worker management are
> named high-risk categories.
> `TODO(source)`: this repo has no content on AI Act classification. **Escalate
> to legal rather than answering.** See `personas/general-counsel.md`.

**"My HR team doesn't have the skills to run this."**
> Source: IMD (~40% report insufficient AI knowledge in HR) · tier 2
> Genuine. `vp-configured` is the answer — the capability ships configured
> rather than being built by a team that can't build it.

**"Is this going to be used to justify cuts?"**
> May not be said aloud, and matters more than most that are. Answer through the
> use cases you choose to demonstrate rather than by protesting. Leading with
> onboarding and policy work answers it implicitly; leading with efficiency
> confirms the fear.
> `TODO(source)`: unevidenced — inferred from the workforce-reduction pressure
> described in the IMD piece. Confirm against real conversations.

## What they need to say yes
A low-risk workflow with a visible audit trail, plus a defensible answer on where
liability sits. Onboarding is the natural first deployment: real volume, real
time savings, minimal regulatory exposure.

> TODO(source): no `pricing/` content.

## Who else is in the room
- **General Counsel** — gates this more tightly than any other function's
  purchase. Involve early rather than being routed there late. See
  `personas/general-counsel.md`.
- **CFO** — approves above threshold. See `personas/cfo.md`.
- **HRBP leads and Talent Acquisition** — the actual users; TA carries the bias
  exposure most directly.
- **Works councils / employee representatives** — in EU operations these can
  gate deployment outright, and they are absent from every other persona here.

> TODO(source): committee shape inferred, not observed.

---

## Sourcing note

Confidence tiers as defined in `cfo.md`; source hierarchy in the skill. The
IMD piece is the backbone here and is tier 2 — named academic authors at a
business school, but it cites its own underlying surveys secondhand, so specific
percentages are stated as approximations.

A Substack account of CHRO Cowork workflows (file organization, board-summary
synthesis, job description drafting) sits behind a paywall; the visible portion
describes plausible low-risk workflows consistent with the recommendation above.
A Medium post claiming large monthly time savings could not be retrieved (HTTP
403) and its headline figure is not used.

**Highest-value additions when connectors land:** whether liability or bias is
the first question asked in real deals, and whether onboarding-first actually
shortens the legal review.
