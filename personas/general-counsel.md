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

> **This file has two readers, and they need opposite things.**
>
> - **Legal buying for legal** — an economic buyer, and an enthusiastic one.
>   Make a case.
> - **Legal reviewing someone else's purchase** — a blocker. Pre-answered review
>   material, no pitch. See the second half.
>
> Establish which one you're writing for before you start.

## Correcting the obvious assumption

The intuitive model is that the GC is a gatekeeper who never buys. **That is
wrong, and the evidence is first-party and unambiguous.**

Following the February legal plugin launch, Anthropic's Associate General
Counsel reports that **legal became the number-one power-user job function in
Claude Cowork, with over three times the usage of any other function.** Over
20,000 people registered for a single April webinar. His framing is that lawyers
are no longer asking whether to use AI, but how.

> Source: [Mark Pike, Anthropic Associate General Counsel — Artificial Lawyer interview, 12 May 2026](https://www.artificiallawyer.com/2026/05/12/al-interview-mark-pike-anthropic-associate-general-counsel/) · **tier 1 — first-party**
>
> 116 days old as of 2026-09-05, past the 90-day ceiling. Flag on use.

This is the most striking finding in this repo. **Legal is not the reluctant
function — it is the leading one.** Treating a GC as an obstacle to be managed
misreads the room and wastes the strongest adoption signal available.

Why it makes sense: legal work is document comprehension at volume — tracking
defined terms across exhibits and schedules — which is precisely the shape of
work that rewards this product.

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

**"Do exchanges with Claude carry attorney-client privilege?"**
> ⚠️ **The highest-stakes question in this file, and this repo cannot currently
> answer it.**
>
> A competitor's published comparison asserts that a 2026 federal ruling found
> Claude exchanges lack attorney–client privilege protection.
> [LegalOnTech, 15 Jun 2026](https://www.legalontech.com/post/claude-for-legal) —
> **tier 4 for this purpose: a competing legal-AI vendor writing about us.**
>
> **Do not repeat this claim, and do not dismiss it.** It is a specific factual
> assertion about a court ruling, sourced from a party with an interest in it
> being true, and unverified here.
>
> `TODO(source)` — **highest priority in this repo.** Verify against the primary
> record. If substantiated, it belongs in `products/cowork-enterprise.md` with a
> proper answer attached, because a GC will ask and an unprepared response is
> worse than a difficult one. Escalate to counsel rather than improvising.

**"How does this perform against purpose-built legal AI?"**
> The same competitor reports completing reviews ~17x faster and being favoured
> ~1.8x on accuracy in their own evaluation.
> Source: LegalOnTech, as above · **tier 4 — vendor self-comparison, unaudited,
> published by the winner.** Treat as a claim to be aware of, not a fact.
> `TODO(source)`: independent benchmark comparison. The repo has BigLaw Bench
> (vendor-reported) and nothing neutral.

**"Doesn't this need heavy configuration to be useful?"**
> The same source criticizes a dependency on detailed "cold-start" interviews
> calibrating playbooks, escalation chains and risk thresholds, arguing generic
> defaults underperform.
> **This critique is our value proposition.** They are describing `vp-configured`
> as a cost; to a GC who has watched generic tools produce unusable output, it
> reads as the reason it works. Concede the setup cost and reframe: the playbook
> *is* the product. Don't argue the premise — it's true.

**"Where does the data go, and how long is it kept?"**
> Route to the Compliance API proof point in `products/cowork-enterprise.md`.
> This is also the question they ask on *everyone else's* purchase — see below.

## When the GC is the blocker

Different document, same person. When another function is buying, the GC is not
evaluating value — they are looking for reasons to stop, delay, or condition it.

**What they will ask**, in roughly this order: where data is processed and
retained; whether content trains a model; what the audit trail looks like;
whether outputs touch regulated decisions (hiring, pay, credit); and who is
liable when it's wrong.

**How to prepare a champion.** Give them the Compliance API proof point, the
product's own human-review framing, and an honest note on the privilege question
above. **A champion ambushed by the privilege question in a review meeting loses
the deal outright** — arming them with "here's the open question and here's who
to ask" survives contact; discovering it live does not.

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

**Read the tier labels carefully in this file.** It mixes tier 1 first-party
material (the Pike interview, the plugin documentation) with **tier 4
competitor content** (LegalOnTech, a competing legal-AI vendor). The competitor
material is included because it raises the privilege question, which is too
important to omit merely because of who raised it — but every claim from it is
marked, and none should be repeated as fact without independent verification.

A community tutorial for the legal plugin was also reviewed; it self-identifies
as unofficial and unaffiliated, so it is not used as a source for what ships.

**Highest-value addition:** a verified answer on privilege. Nothing else in this
repo is close in importance for this persona.
