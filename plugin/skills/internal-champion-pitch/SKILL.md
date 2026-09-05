---
name: internal-champion-pitch
description: >-
  Builds material a champion can take to their own internal stakeholders to make
  the case for Cowork — a forwardable business case written in their voice, not
  ours. Use when asked for something "they can bring to their team," an internal
  business case, a champion enablement doc, or help getting internal buy-in.
---

# Internal champion pitch

## Step 1 — Load the source (always, every time)

Fetch these from `amulyauppala1-jpg/Claude-Cowork-Positioning` via the GitHub
connector. Never work from memory or from earlier in the conversation.

1. `README.md` — routing and the rules.
2. `products/cowork-enterprise.md` — the foundation.
3. `personas/<role>/README.md` — the persona.
4. `brand/README.md` — voice, tone, colors.
5. `.claude/skills/gtm-from-positioning/SKILL.md` — the full grounding rules.
   **Follow them.** They are not restated here, so they can't drift from the repo.

If the persona folder doesn't exist, say so and build the function-agnostic
version. Don't improvise a persona.

## Step 2 — Establish the motion

Each persona declares `roles_by_motion`. **Departmental** (a function head buying
for their team) and **enterprise** (an org-wide rollout) produce differently
shaped assets and different value-prop rankings. If the request doesn't say,
ask before building.

## Step 3 — Rank, don't default

Use the persona's ranking, not the product file's order. `vp-coverage` leads for
a CFO enterprise-wide and comes last for a CMO buying for their own function.

## Step 4 — Understand who actually reads this

**This is the only asset here whose reader is not its audience.**

The champion receives it. Their CFO, CIO or exec team reads it. That inverts the
usual rules, and getting this wrong is the most common failure:

- **Write in their voice, not ours.** No "we," no "our platform," no seller
  register. If it reads as vendor material, the champion cannot forward it — and
  forwarding it is the entire point.
- **It must survive being read without the champion in the room.** They will
  paste it into Slack or drop it in a deck. Assume no narration.
- **Do not sell the champion.** They are already convinced. They need ammunition,
  not persuasion.

## Step 5 — Compose two personas

This skill uses **two persona files**, and this is the part that makes it work:

1. **The champion's persona** — supplies the vocabulary and what they care
   about. Check their `roles_by_motion`: this asset exists because they are a
   `champion` in this motion, not the economic buyer.
2. **The approver's persona** — usually `personas/cfo/README.md` — supplies
   the **decision criteria**. Their objections are what the document must answer.

So a CMO championing to a CFO gets a document in marketing's language that
answers finance's questions. Leading with the CMO's own value prop ranking
would be wrong: **rank for the person who signs**, and phrase for the person who
sends. If the approver's persona file does not exist, say so and use the
function-agnostic version.

## Step 6 — Build it

1. **The problem, in business terms** — their function's problem stated as a
   company problem. Cost, risk or growth, not workflow annoyance.
2. **What we would do** — scoped, specific, small enough to approve.
3. **What it costs** — `TODO(source)`: the repo has no `pricing/` content. **Say
   the number is not available rather than estimating one.** A champion caught
   with an invented figure loses credibility permanently.
4. **What we expect back** — tied to a metric the approver is measured on, from
   their persona file.
5. **The risks, named** — pre-answer the approver's top two documented
   objections. Naming them is what makes a document credible internally.
6. **The ask** — one decision, clearly stated.

Under two pages. An internal doc that needs a meeting to explain has failed.

## Step 7 — Render

Markdown or a clean HTML page. **No logos, no brand styling.** Brand colours
here signal vendor material, which is exactly what this must not look like.
This is the one asset where `brand/README.md` governs the *writing* and
explicitly not the *visual design*.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
