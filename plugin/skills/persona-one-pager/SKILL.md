---
name: persona-one-pager
description: >-
  Builds a single-page positioning one-pager for a named buyer persona (CFO, CMO,
  CRO, CHRO, General Counsel), grounded in the Cowork positioning repo. Use when
  asked for a one-pager, leave-behind, or overview "for a [persona]."
---

# Persona one-pager

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

## Step 4 — Build it

The canonical asset. A rep sends it before a meeting or leaves it behind after.
It must survive being read alone, with nobody there to explain it.

Structure — **one page, and mean it**:

1. **Headline** — the persona's leading value prop as a claim about their world.
2. **The problem** — their buyer problem or opening position, in their words.
3. **What Cowork is** — the positioning statement, trimmed to this buyer.
4. **Three reasons** — the props in the persona's order, each with its RTB
   from `products/`. Name the deliverable, not the capability.
5. **Proof** — dated and sourced. Flag if stale. Omit rather than invent.
6. **One CTA.**

If it runs past a page, cut a reason before cutting the proof.

## Step 5 — Render

Markdown by default. HTML if they want something designed — Ivory ground, Slate
text, Clay once. Use the `docx`/`pdf` skills only if a file is explicitly asked for.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
