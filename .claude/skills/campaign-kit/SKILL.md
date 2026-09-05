---
name: campaign-kit
description: >-
  Builds a coordinated set of assets for one buyer persona — landing page, email
  and ad, or a chosen combination — that all lead with the same argument and use
  the same proof. Use when someone mentions a campaign, launch, program, or
  "everything I need for," or asks for several assets at once for the same
  audience.
---

# Campaign kit

**The value here is consistency, not volume.** Running three asset skills
separately produces three assets that each make sense alone and disagree with
each other — different lead argument, different proof, different phrasing. This
builds them as one thing.

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

## Step 4 — Fix the spine before writing anything

Decide these once, write them down, and hold them across every asset:

- **The lead argument** — one value prop, from the persona's ranking.
- **The proof** — one dated, sourced point, used consistently. Not a different
  one per asset.
- **The core phrase** — the sentence the campaign turns on, appearing near-verbatim
  in each piece. Repetition across touches is how a message lands; variation
  reads as three unrelated things.
- **The CTA** — one, matched to the motion.

**State the spine in your output before the assets.** It is what the requester
reviews, and it is cheaper to correct there than across four finished pieces.

## Step 5 — Build the set

Default set, unless they asked for something specific:

1. **Landing page section** — where the CTA points.
2. **Campaign email** — drives to the landing page.
3. **Ad unit** — headline, sub-headline, CTA. Three headline options.

Add a **pitch deck** or **one-pager** if sales will follow up, and say why you
added it. Delegate each to its own skill so the format conventions are applied —
this skill owns the spine and the consistency, not the craft of each format.

## Step 6 — Check the set against itself

Before delivering, verify across the assets:

- Same lead argument in all of them.
- Same proof point, phrased consistently.
- The core phrase appears in each.
- One CTA, not three variants.
- No banned vocabulary anywhere — check the short copy hardest, since that is
  where it slips through.

**Report this check.** If an asset had to diverge, say which and why.

## Step 7 — Offer the test

Offer `roleplay-tester` on the strongest asset. A campaign that fails in
character fails in all three pieces at once, which is exactly why testing one is
worth it before the set ships.
