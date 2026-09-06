---
persona: General Counsel
function: Legal
seniority: C-level
roles_by_motion:
  departmental: economic_buyer   # legal buys for legal — and is the heaviest user function
  enterprise: blocker            # gates every other function's purchase on data handling
applies_to: [cowork-enterprise]
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: public-research
---

# General Counsel

> **Two modes, and they need opposite things. Establish which one before you
> write a word.**
>
> **Mode A — buying for legal.** They're the economic buyer, and legal is the
> heaviest-adopting function in the product. Make a case. Everything through
> "When they're the blocker" applies.
>
> **Mode B — reviewing someone else's purchase.** Nobody is selling to them.
> There is no lead value prop here because there is no pitch: the job is
> clearing a gate. Skip to "Mode B" below.
>
> Mode B is the more common encounter, since a GC touches every other function's
> deal and only occasionally buys their own.

## Positioning — value proposition

> **For** an in-house legal team reviewing more contracts than it can staff
> **that need** review against their own risk posture rather than a generic standard
> **Cowork** **is an** agentic workspace configured with the team's contract playbook
> **that** triages and reviews clause by clause against that playbook, with
> attorney review preserved.

> ⚠ **This differentiation is weaker than it looks, and the framework caught it.**
> The `Unlike` below answers a *general* assistant pointed at contract review. It
> does not answer a purpose-built legal AI tool, which is neither generic nor
> inferring a standard: those products also run against the customer's playbook.
> A GC asking "how does this compare" is almost always thinking of the
> purpose-built category, not of someone pasting a contract into a chat window.
>
> `TODO(source)`: this is a real positioning gap, not a wording problem. Closing
> it needs a `competitors/` layer and an honest answer on where Cowork wins
> against a category-specific tool. Until then, say the comparison is one we
> haven't published rather than reaching for the generic contrast.

## Positioning — differentiation

> **Unlike** generic AI review applying a standard it inferred rather than the
> one you set
> **Cowork provides** analysis against your playbook, with the human-review
> boundary stated rather than glossed.

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
| **1. Feature** | Clause-by-clause review against your own playbook |
| **2. Functional benefit** | NDA and contract queues triaged before a lawyer opens them |
| **3. Business outcome** | Legal handles more volume without adding headcount |
| **4. What it means for them** | You keep the judgment call and lose the reading |

**Lead from rung 2 or 3. Never rung 1.** A feature-led opening is the most
common failure in B2B copy, and it is structurally fine — it just argues at the
wrong altitude. Rung 3 is where a business case lives; rung 2 is where a first
conversation lives.

**Rung 4 shapes emphasis; it is rarely said out loud.** Naming a buyer's
personal exposure back to them reads as manipulative and costs you the room.
Use it to decide what to lead with, not as a line in the asset.

## The GC is not only a gatekeeper

The intuitive model is that the GC gates purchases and never makes them. The
buying half of that is wrong.

Following the February legal plugin launch, Anthropic's Associate General
Counsel reports that **legal became the number-one power-user job function in
Claude Cowork, with over three times the usage of any other function.** Over
20,000 people registered for a single April webinar. His framing is that lawyers
are no longer asking whether to use AI, but how.

> Source: [Mark Pike, Anthropic Associate General Counsel — Artificial Lawyer interview, 12 May 2026](https://www.artificiallawyer.com/2026/05/12/al-interview-mark-pike-anthropic-associate-general-counsel/) · **tier 1 — first-party**
>
> 116 days old as of 2026-09-05, past the 90-day ceiling. Flag on use.

**Read this as an existence proof, not a profile.** It shows that legal *can* be
a leading adopter — which is genuinely useful, because the assumption in the room
usually runs the other way. It does **not** mean the GC in front of you is
enthusiastic, and it is not a benchmark to measure them against.

Note also what population it describes: usage within Claude Cowork as reported by
Anthropic. That is a self-selected group of organizations already using the
product. It says legal adoption happens and can lead; it does not describe legal
functions generally.

**Two failure modes, and the second is the one to watch.** Treating a GC as an
obstacle wastes a real signal. But arriving with "legal is usually our biggest
adopter" and finding a cautious GC is worse — it reads as pressure, and caution
is the correct professional posture for the role. Use this to open a door, never
to imply someone is behind.

Why the adoption makes sense where it happens: legal work is document
comprehension at volume — tracking defined terms across exhibits and schedules —
which is the shape of work that rewards this product.

## What already ships for this function

The **legal plugin** is first-party. Detail in `products/cowork-enterprise.md`.

- **`/review-contract`** — clause-by-clause analysis **against your
  organization's playbook**, flagging GREEN/YELLOW/RED with redline suggestions.
- **`/triage-nda`** — screens incoming NDAs into standard approval, counsel
  review, or full review.
- **`/vendor-check`** — vendor agreement status and obligations.
- **`/brief`** — daily summaries, topic research, incident response.
- **`/respond`** — templated responses for data subject requests and discovery holds.

Connects via MCP to document management, chat and project tracking. Aimed at
in-house commercial, product, privacy/compliance and litigation support teams.

**Note the product's own framing: all outputs should be reviewed by licensed
attorneys.** Use that line rather than softening it. A GC trusts a vendor who
states the limit more than one who claims it isn't needed.

> Source: [legal plugin](https://claude.com/plugins/legal) · tier 1.

Reported benchmark: **90.9% on BigLaw Bench**, with particular strength in
grounding and citation faithfulness — which is the metric that maps to the
profession's actual anxiety about fabricated citations.

> Source: Pike interview, as above · tier 1 (vendor-reported benchmark — say so).

## Value props, ranked — legal buying for legal

> Completing the split across this repo: CFO leads `vp-coverage` · CMO
> `vp-executes` · CRO `vp-configured` · CHRO `vp-configured` · **GC `vp-configured`.**

1. **`vp-configured`** — leads, and more literally than for any other persona.
   `/review-contract` runs *against your playbook*. Without the playbook, it is
   generic; with it, it encodes the firm's actual risk posture. Configuration
   isn't a differentiator here, it's the product.
2. **`vp-executes`** — second. NDA triage and contract queues are genuine volume
   work with a clean human-review boundary already built in.
3. **`vp-coverage`** — last in a departmental motion.

## Vocabulary

**Use:** playbook · escalation path · risk threshold · human review · grounding ·
citation faithfulness · defensibility · retention · work product · matter.

**Avoid:**
- **"Replace lawyers"** or **"automated legal advice."** The second edges toward
  unauthorized practice of law — a category error, not just bad taste.
- **"Claude decides."** Nothing decides. Claude drafts, flags, and triages.
- **Softening the human-review requirement.** Stating it plainly builds more
  credibility than claiming it away.

## Objections

**"How much work is it to get our playbook in?"**
> `TODO(source)` — **the load-bearing question for this buyer, and the repo has
> no answer.** Configuration is the product for legal, which makes setup effort
> the thing they press hardest on. A competitor has publicly criticised exactly
> this as a cold-start cost. Until there is real onboarding content, say the
> honest thing: the playbook has to go in, that is the work, and here is roughly
> what it involves. Do not wave it away.

**"How does this compare to purpose-built legal AI?"**
> See the warning at the top of this file. The `Unlike` line does not answer
> this, and repeating a competitor's benchmark claims is out per the sourcing
> rules. `TODO(source)`: needs a `competitors/` layer.

**"What is the privilege posture for work done here?"**
> A standard question from this desk, and this repo has no content on it.
> **Escalate to counsel — do not improvise an answer.** Privilege turns on
> facts and jurisdiction, and a confident guess from a seller is worse than
> "I'll get you a proper answer."
> `TODO(source)`: the repo needs a reviewed position on privilege and work
> product, written or approved by counsel. Until then this is an escalation,
> not an objection to handle.

**"How does this perform against purpose-built legal AI?"**
> Purpose-built legal AI vendors publish comparisons favouring themselves. Expect
> them to come up; they are unaudited self-comparisons and this repo has no
> neutral benchmark to answer with.
> The repo has BigLaw Bench (vendor-reported, ours) and nothing independent.
> `TODO(source)`: an independent comparison. Until then, compete on the playbook
> and workflow-fit argument below rather than on benchmark numbers.

**"Doesn't this need heavy configuration to be useful?"**
> Competing vendors frame the dependency on detailed "cold-start" playbook,
> escalation and risk-threshold setup as a weakness.
> **This critique is our value proposition.** They are describing `vp-configured`
> as a cost; to a GC who has watched generic tools produce unusable output, it
> reads as the reason it works. Concede the setup cost and reframe: the playbook
> *is* the product. Don't argue the premise — it's true.

**"Where does the data go, and how long is it kept?"**
> Route to the Compliance API proof point in `products/cowork-enterprise.md`.
> This is also the question they ask on *everyone else's* purchase — see below.

## Mode B — reviewing someone else's purchase

**Nothing above this line applies.** No value prop leads, because nobody is
pitching. The GC is not evaluating whether the product is good; they are looking
for a reason to stop, delay, or condition it. An asset that opens with a benefit
statement here reads as someone who doesn't understand what the meeting is for.

**What they will ask**, in roughly this order, and what satisfies each:

| They ask | What answers it |
|---|---|
| Where is data processed and retained? | The Compliance API proof point in `products/cowork-enterprise.md` |
| Does content train a model? | `TODO(source)` — this repo has no position. Escalate, don't improvise. |
| What does the audit trail look like? | Session-level records across desktop, web and mobile, same Compliance API |
| Do outputs touch regulated decisions? | Depends on the function. HR is the exposed one — see `personas/chro/README.md` |
| Who is liable when it's wrong? | The customer. Say so plainly; a reassuring non-answer fails here. |

**The privilege question also comes up and this repo cannot answer it.** Route to
counsel rather than guessing.

**How to prepare a champion.** Give them the Compliance API proof point and the
product's own human-review framing. Tell them plainly that privilege questions
route to counsel rather than being answered in the meeting. **A champion who
improvises an answer to a legal question does more damage than one who says
"I'll get you that"** — the second is normal, the first is disqualifying.

**Cross-reference:** the CHRO file escalates AI Act classification here. The two
personas are tightly coupled — HR use cases are named high-risk categories, so a
CHRO purchase routes through this desk more tightly than any other function's.

## What they need to say yes
As a buyer: a playbook-driven contract or NDA workflow with the human-review
boundary intact. As a blocker: documented answers on data handling, retention and
privilege — the third of which this repo does not yet have.

> TODO(source): no `pricing/` content.

## Who else is in the room
- **CISO** — co-gates on data handling; often the technical half of the same review.
- **CFO** — approves above threshold. See `personas/cfo.md`.
- **CHRO** — the function whose purchases route here most tightly. See `personas/chro.md`.
- **Outside counsel** — may be consulted on the privilege question, and will be
  more conservative than in-house.

> TODO(source): committee shape inferred, not observed.

---

## Sourcing note

Confidence tiers as defined in `cfo.md`; hierarchy in the skill.

Sources here are tier 1 first-party (the Pike interview, the plugin
documentation). Competitor marketing from a rival legal-AI vendor was reviewed
and **deliberately not used**: its specific factual and benchmark assertions
were unverified and published by an interested party, and recording them even as
open questions would propagate them. Where competitor framing is referenced above
it is described generically, with no figures and no claims restated.

A community tutorial for the legal plugin was also reviewed; it self-identifies
as unofficial and unaffiliated, so it is not used as a source for what ships.

**Highest-value addition:** a counsel-reviewed position on privilege and work
product. It is the one question this desk asks that the repo cannot answer.
