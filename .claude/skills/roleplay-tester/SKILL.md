---
name: roleplay-tester
description: >-
  Tests a draft GTM asset by role-playing the target buyer and pushing back with
  their documented objections and vocabulary. Use when asked to
  test, review, pressure-test, critique, or "check if this is on-positioning," or
  before an asset goes out.
---

# Roleplay tester

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

## Step 4 — What this skill is for

Everything else here generates. **This one reads it back as the buyer would.**
It is the check that makes the system trustworthy rather than merely productive:
it can be run on any asset, by anyone, without the person who built the repo.

Run it on a draft before that draft goes anywhere.

## Step 5 — Mechanical checks first

Before role-playing anything, verify against the repo. These are pass/fail and
do not require judgment:

1. **Value prop order** — does the asset lead with the prop this persona's
   file ranks first, *for the stated motion*? Leading with the product file's
   default order is the most common failure and is invisible unless checked.
2. **Vocabulary** — does it use anything from the persona's **Avoid** list?
   Quote the offending phrase.
3. **Proof points** — is every customer, statistic or example traceable to a
   dated, sourced entry in `products/`? Anything past 90 days flagged?
4. **Invented claims** — any capability asserted that `products/` does not support?
5. **Status** — if the positioning file is `draft`, does the asset say so?
6. **Motion fit** — an `economic_buyer` asset should handle objections in the
   body; a `champion` asset must be forwardable and not read as vendor material.
7. **Altitude** — does it open on a feature (rung 1)? The lead should sit at
   rung 2 or 3 of the persona's ladder. Quote the opening line and name its rung.
8. **Positioning anti-patterns** — is any claim a tagline, a feature list, a
   generic line that would fit any product, or aspirational fluff with no
   specifics? Quote it. "For businesses that need efficiency" fails; so does
   "revolutionises productivity."

Report each of the eight as PASS or FAIL with the specific line at fault. **Do not soften a
FAIL** — a passed asset that should have failed is worse than no check.

## Step 6 — Then role-play the buyer

Adopt the persona. Read the asset as them, with their documented pressures and
scepticism, and respond in character:

- **Raise their objections in the file's order.** Does the asset answer them,
  or does it leave the strongest one untouched?
- **React to the opening.** A CMO who has already bought AI, a CRO whose reps
  ignore the last tool, a CFO who cannot measure the last pilot — does the first
  line survive that? Say where you would stop reading.
- **Push on the weakest claim.** Which sentence would you challenge in a meeting?
- **Say what is missing** that would change your answer.

Stay in character. A polite review is useless — this buyer is not polite about
their budget.

## Step 7 — Verdict

1. **Mechanical results** — the six checks, PASS/FAIL with line references.
2. **In-character reaction** — where they disengaged and why.
3. **The single highest-impact fix**, named specifically.
4. **Ship / do not ship**, and say which. A recommendation that hedges is not one.

Note the limits: this tests against **documented** objections. Real buyers raise
things the repo has not captured. A pass means consistent with the repo, not
guaranteed to land — and where a persona file carries `TODO(source)` gaps, say
which parts of the test could not be run.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
