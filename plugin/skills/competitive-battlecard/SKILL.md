---
name: competitive-battlecard
description: >-
  Builds a competitive battlecard for a named competitor and buyer persona,
  grounded in the Cowork positioning repo. Use when asked for a battlecard,
  competitive brief, "how we win against X," or objection handling versus a
  named competitor.
---

# Competitive battlecard

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

## Step 4 — Check what the repo actually has, and say so

**Read this before building. The repo has a known gap here.**

`products/cowork-enterprise.md` carries a *category-level* differentiation claim
— against chat assistants and point copilots that answer questions and leave the
work to the employee. It does **not** contain competitor-specific intelligence:
no per-competitor pricing, feature comparison, win/loss data, or trap-setting
questions. There is no `competitors/` folder.

So:

- You **can** build a strong battlecard against the *category* — how Cowork
  differs from chat assistants generally, ranked for this persona.
- You **cannot** build one against a named competitor without inventing content.
  Say this plainly. Do not fill the gap from general knowledge, and never repeat
  a competitor's own published claims or benchmark figures — that rule is in
  the repo's grounding skill and applies with full force here.

If asked for a named competitor, produce the category battlecard, state exactly
what is missing, and note that the fix is adding a `competitors/` layer to the
repo rather than a better prompt.

## Step 5 — Build what you can

1. **Where we win, for this buyer** — the persona's leading value props as
   contrasts, not features.
2. **Where they are vulnerable** — only category-level claims traceable to
   `products/`.
3. **What they will say** — the persona's documented objections that a
   competitor would amplify.
4. **Proof** — dated and sourced, or omitted.
5. **Traps** — questions that expose the category gap. Derive from the
   differentiation claim, do not invent capability comparisons.

**Never disparage.** A battlecard that reads as an attack loses the room and is
usually wrong; contrast is stronger than criticism.

## Step 6 — Note the scale problem

Enablement coverage is competitors x use cases x industries — a product, not a
sum. See `personas/cmo/README.md`. Say which single combination this card covers
so nobody assumes broader coverage than exists.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
