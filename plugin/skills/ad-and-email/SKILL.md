---
name: ad-and-email
description: >-
  Writes an ad unit (headline, sub-headline, CTA) or a cold/nurture email for a
  named buyer persona (CFO, CMO, CRO, CHRO, General Counsel), grounded in the
  Cowork positioning repo. Use when asked for ad copy, a banner, paid social,
  or an email "for a [persona]."
---

# Ad unit or email

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

## Step 4 — Build it

Short formats are where invented claims and banned vocabulary slip through,
because there's no room for qualification. **Check the persona's Avoid list
before writing, not after.**

### Ad unit

- **Headline** — under 10 words. The persona's leading value prop as a claim
  about their world, not a product description.
- **Sub-headline** — under 20 words. Earns the headline. Concrete.
- **CTA** — 2-4 words, matching the motion. Departmental buys take a lighter ask
  than enterprise.

Produce **three headline options** with a one-line rationale each, then
recommend one. Don't make the requester guess which you'd pick.

### Email

- **Subject** — under 8 words, no colon-stacking, no "Quick question."
- **Preview text** — a second line that adds, not repeats.
- **Body** — under 150 words. Open on their problem in their vocabulary, one
  specific claim from the persona's leading prop, one proof point if a current
  one exists, one ask.
- **One ask.** Two asks is zero asks.

No merge-field theatre, no fake personalization, no "I noticed you..." unless
there is a real observation to make.

## Step 5 — Render

Ad unit: HTML at a standard size (300×250 or 728×90 — say which). Ivory ground,
Slate text, Clay on the CTA only.

Email: plain text. Most cold email is read in plain text, and HTML email is a
different craft with different constraints.

## Step 6 — Report

End with:
- The provenance line with `last_updated` dates.
- A `status: draft` warning if applicable.
- **The vocabulary check** — name the persona's Avoid terms you steered around.
  In short copy this is the most likely failure, so make it visible.
- Anything omitted and why.
