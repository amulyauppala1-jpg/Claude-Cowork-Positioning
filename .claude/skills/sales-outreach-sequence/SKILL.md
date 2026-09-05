---
name: sales-outreach-sequence
description: >-
  Writes a multi-touch 1:1 sales outreach sequence (cold or re-engagement) for a
  named buyer persona, grounded in the Cowork positioning repo. Use when asked
  for an outreach sequence, cadence, prospecting emails, or follow-ups "for a
  [persona]."
---

# Sales outreach sequence

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

## Step 4 — Understand what makes this different

Not a campaign email split into parts. **Each touch does a different job**, and
a sequence where every touch restates the value proposition is one email sent
five times.

Default 4-5 touch structure:

1. **Touch 1 — the problem.** Their opening position, in their vocabulary. No
   product. The only goal is recognition.
2. **Touch 2 — the specific claim.** One thing Cowork does, tied to touch 1.
   The leading value prop, named concretely.
3. **Touch 3 — proof.** A dated, sourced proof point. If none current exists,
   **say so and use a different angle** rather than inventing one.
4. **Touch 4 — the objection.** Name their most likely documented objection
   before they raise it. This is the touch that separates a real sequence from a
   template, and it is the one most often skipped.
5. **Touch 5 — the close or the break-up.** Short. No guilt, no false deadline.

Spacing: 3-4 business days. Say the cadence explicitly.

## Step 5 — Rules that matter here

- **Under 90 words per touch.** A 1:1 email that looks mass-produced is deleted.
- **No "just circling back," no "bumping this," no fake urgency.**
- **No "I noticed you..."** unless there is a real observation to make.
- Each touch must stand alone — many are read out of order or not at all.
- Check the motion: a `champion` reader needs something forwardable, so write
  touch 4 knowing it may be pasted into Slack.

## Step 6 — Render

Plain text. Number the touches, state the day offset for each.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
