---
name: landing-page
description: >-
  Builds a landing page (or a single page section) for a named buyer persona,
  grounded in the Cowork positioning repo and rendered as HTML in brand colors.
  Use when asked for a landing page, web page, hero, or page copy "for a
  [persona]" or "using our positioning."
---

# Landing page

## Step 1 — Load the source, freshest first

Try these in order and **stop at the first that works**. Never work from memory
or from earlier in the conversation.

1. **GitHub connector** — if connected, read from
   `amulyauppala1-jpg/Claude-Cowork-Positioning`. Live.
2. **Direct fetch** — if the repo is public, fetch the raw files at
   `https://raw.githubusercontent.com/amulyauppala1-jpg/Claude-Cowork-Positioning/main/<path>`.
   Live, and needs no connector or account.
3. **Local folder** — if the repo is open as a workspace, read it from disk.
   Live as of the last `git pull`.
4. **Embedded snapshot** — `reference/` inside this skill bundle, if present.
   Read `reference/VERSION.json` for its build date.

Load: `README.md`, `products/cowork-enterprise.md`,
`personas/<role>/README.md`, `brand/README.md`, and — where not already in your
instructions — the repo's `.claude/skills/gtm-from-positioning/SKILL.md` for the
full grounding rules. **Follow them.** They are not restated here, so they can't
drift from the repo.

**Say which source you used, in one line.** "Read live from GitHub" and "using an
embedded snapshot built 2026-09-05" mean different things to whoever relies on
the output, and only one of them needs checking. If you fell back to the
snapshot and it is more than about six weeks old, say so plainly — proof points
that were current at build time may have passed their 90-day ceiling since.

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

## Step 4 — Ask what scope

A **full page** and a **single section** are different asks. If unclear, assume a
section — it slots into an existing page and is more often what is wanted.

## Step 5 — Build it

**Section:** headline (leading prop, their vocabulary) → sub-headline (one
sentence, the buyer problem) → two or three supporting points in the persona's
order → one proof element → one CTA. No nav, no footer, no repeated logo.

**Full page:** the above as the hero, then one block per remaining value prop,
a proof block, an objection-handling block drawn from the persona's documented
objections, and a closing CTA. **Handle objections in the page** for an
`economic_buyer` — for that reader they are decision criteria, not an FAQ.

Never write a headline that would work for any product. If it would, it is
describing a category, not a position.

## Step 6 — Render

Standalone HTML. Ivory `#FAF9F5` ground, Slate `#141413` text, Clay `#D97757`
used once per view. Responsive, generous line height, real margins. Define the
three as CSS custom properties. No gradients, shadows, or icon sets — restraint
carries this brand.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
