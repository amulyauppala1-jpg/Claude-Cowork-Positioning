---
name: pitch-and-narrative-deck
description: >-
  Builds a pitch narrative or deck (3-8 slides) for a named buyer persona,
  grounded in the Cowork positioning repo, rendered as HTML slides. Use when
  asked for a pitch, deck, slide story, narrative, or presentation "for a
  [persona]."
---

# Pitch and narrative deck

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

## Step 4 — Build the narrative

**A narrative, not a feature list.** Each slide earns the next. If the slides
could be reordered without loss, it is not a narrative yet.

Default arc, adapted to the persona:

1. **Their problem, in their words** — from the persona's buyer problem or
   opening position. If they do not recognize themselves here, nothing else lands.
2. **Why the obvious fix has not worked** — the persona's documented failure:
   the CMO's review-cycle trap, the CRO's 19% rep usage, the CFO's
   unmeasurable pilot. The slide most decks skip, and the one that earns credibility.
3. **What Cowork is** — differentiation, framed by the leading value prop.
4. **Why it holds** — the remaining props in the persona's order.
5. **Proof** — dated and sourced. Flag if stale. Omit the slide rather than invent.
6. **The next step** — concrete and small. Not "get started."

Three to five slides for a pitch; up to eight for a full deck. **Fewer is
better — cut before padding.**

## Step 5 — Render

HTML slides: one `<section>` per slide, each a full viewport, scroll or arrow-key
to advance. Ivory ground, Slate text, Clay at most once per slide.

**One idea per slide.** Headline plus at most three lines. If it needs a
paragraph it is a document, not a slide. Speaker notes in `<!-- comments -->`.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
