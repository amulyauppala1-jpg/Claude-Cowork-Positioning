---
name: pitch-narrative
description: >-
  Builds a 3-5 slide pitch narrative for a named buyer persona (CFO, CMO, CRO,
  CHRO, General Counsel) grounded in the Cowork positioning repo, rendered as
  HTML slides. Use when asked for a pitch, deck narrative, slide story, or
  presentation "for a [persona]."
---

# Pitch narrative (3-5 slides)

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
ask before building — guessing picks the wrong lead.

## Step 3 — Rank, don't default

Use the persona's ranking, not the product file's order. This is the point of
the system: `vp-coverage` leads for a CFO enterprise-wide and comes last for a
CMO buying for their own function.

## Step 4 — Build the narrative

**A narrative, not a feature list.** Each slide earns the next. If the slides
could be reordered without loss, it isn't a narrative yet.

The default arc, adapted to the persona:

1. **Their problem, in their words.** Straight from the persona's buyer problem
   or opening position. If they don't recognize themselves here, nothing else lands.
2. **Why the obvious fix hasn't worked.** The persona's documented failure — the
   CMO's review-cycle trap, the CRO's 19% rep usage, the CFO's unmeasurable pilot.
   This is the slide most decks skip and the one that earns credibility.
3. **What Cowork is** — differentiation from `products/`, framed by the
   persona's leading value prop.
4. **Proof** — a dated, sourced proof point. Flag if stale. Omit the slide
   rather than invent one.
5. **The next step** — concrete and small. Not "get started."

Four slides is usually better than five. Cut before padding.

## Step 5 — Render

HTML slides — one `<section>` per slide, each a full viewport, scroll or
arrow-key to advance. Ivory ground, Slate text, Clay once per slide at most.

**One idea per slide.** Headline plus at most three lines. If it needs a
paragraph, it's a document. Speaker notes go in `<!-- comments -->`, never
on the slide.

## Step 6 — Report

End with:
- The provenance line with `last_updated` dates.
- A `status: draft` warning if applicable.
- **The narrative logic in two sentences** — why this arc for this buyer. If you
  can't justify the order, the deck is a feature list.
- Anything omitted and why.
