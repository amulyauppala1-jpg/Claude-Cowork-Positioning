---
name: campaign-email
description: >-
  Writes marketing campaign or nurture email for a named buyer persona, and short
  paid copy (ad headline, sub-headline, CTA), grounded in the Cowork positioning
  repo. Use when asked for a campaign email, nurture email, newsletter copy, ad
  copy, or a banner "for a [persona]."
---

# Campaign email and short-form paid copy

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

## Step 4 — Note the format risk

Short copy is where invented claims and banned vocabulary slip through, because
there is no room to qualify anything. **Read the persona's Avoid list before
writing, not after.**

## Step 5 — Build it

### Campaign / nurture email

One-to-many, so no fake personalization and no merge-field theatre.

- **Subject** — under 8 words. No colon-stacking, no "Quick question."
- **Preview text** — adds, never repeats the subject.
- **Body** — under 150 words. Open on their problem in their vocabulary, one
  specific claim from the leading prop, one current proof point if one exists,
  one ask.
- **One ask.** Two asks is zero asks.

### Ad unit

- **Headline** under 10 words — the leading prop as a claim about their world,
  not a product description.
- **Sub-headline** under 20 words, concrete, earning the headline.
- **CTA** 2-4 words, matched to the motion. Departmental buys take a lighter ask.

Give **three headline options with a one-line rationale each**, then recommend
one. Do not make the requester guess which you would pick.

## Step 6 — Render

Email as plain text — most is read that way, and HTML email is a different craft.
Ad unit as HTML at a stated standard size (300x250 or 728x90): Ivory ground,
Slate text, Clay on the CTA only.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
