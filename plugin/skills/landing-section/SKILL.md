---
name: landing-section
description: >-
  Builds a landing-page section for a named buyer persona (CFO, CMO, CRO, CHRO,
  General Counsel), grounded in the Cowork positioning repo and rendered as
  standalone HTML in brand colors. Use when asked for a landing page section,
  web section, hero, or page copy "for a [persona]" or "using our positioning."
---

# Landing page section

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

## Step 4 — Build the section

**One section, not a page.** It slots into an existing page, so no nav, no
footer, no repeated logo.

Structure:

1. **Headline** — the persona's leading value prop, in their vocabulary. Not the
   product file's key message verbatim; that's function-agnostic by design.
2. **Sub-headline** — one sentence. The buyer problem from the persona file, in
   their words, or the differentiation claim.
3. **Two or three supporting points** — the remaining props in the persona's
   order. Name the deliverable, not the capability.
4. **One proof element** — a dated, sourced proof point from `products/`.
   If the freshest relevant one is past 90 days, use it and say it's stale.
   If none fits, omit this block rather than writing a vague trust line.
5. **One CTA** — the Primary CTA from `products/`, unless the persona's motion
   calls for something softer.

## Step 5 — Render

Standalone HTML. Ivory `#FAF9F5` ground, Slate `#141413` text, Clay
`#D97757` used exactly once. Responsive, generous line height, real margins.
Define the three colors as CSS custom properties at the top.

Restraint carries this brand. No gradients, no shadows, no icon set.

## Step 6 — Report

End with:
- The provenance line (source files and `last_updated` dates).
- A `status: draft` warning if the positioning file is not approved.
- Which value prop you led with **and why**, in one sentence — this is how the
  requester checks the system worked rather than trusting the output.
- Anything you could not include and the reason.
