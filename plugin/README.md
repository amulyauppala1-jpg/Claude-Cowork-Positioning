# Cowork Positioning — Cowork plugin

Lets marketing and sales build GTM assets from the positioning repo without
cloning anything, editing markdown, or asking the person who maintains it.

## What it does

9 skills, all grounded in the same source:

| Skill | Produces |
|---|---|
| `blog-post` | Long-form article — must be useful to someone who never buys |
| `campaign-email` | Marketing/nurture email, plus short paid copy |
| `competitive-battlecard` | Category battlecard (see the gap note in the skill) |
| `internal-champion-pitch` | A forwardable business case in *their* voice, not ours |
| `landing-page` | Landing page or page section, as HTML |
| `persona-one-pager` | Single-page overview — the canonical leave-behind |
| `pitch-and-narrative-deck` | 3–8 slide narrative, as HTML slides |
| `roleplay-tester` | Attacks a draft in character. Run before anything ships |
| `sales-outreach-sequence` | Multi-touch 1:1 outreach cadence |

Ask in plain language — *"landing page for a CFO"*, *"outreach sequence for a
CRO"* — and the skill resolves the persona, checks the motion, ranks the value
props for that buyer, and cites what it used.

Two of these aren't generators, and they're the reason this is a system rather
than a content mill:

- **`internal-champion-pitch`** is the only asset whose reader isn't its
  audience. The champion receives it; their CFO reads it. So it composes *two*
  persona files — the champion's for vocabulary, the approver's for decision
  criteria — and is written in their voice with no brand styling, because
  anything that looks like vendor material can't be forwarded.
- **`roleplay-tester`** attacks a draft in character using the persona's
  documented objections, after six mechanical PASS/FAIL checks. It's how anyone
  can verify an asset without the person who built the repo.

## Install

1. Install this plugin in Cowork.
2. **Connect GitHub** and grant access to
   `amulyauppala1-jpg/Claude-Cowork-Positioning`.

Step 2 is required, not optional. The skills read the repo at generation time.

## Why it reads live instead of bundling the content

A plugin that ships a copy of the positioning is stale the moment someone edits
a persona file — which is the exact failure this repo exists to prevent,
reintroduced at the distribution layer. So the content stays in one place and
the plugin fetches it. The cost is the GitHub connector requirement. It's worth it.

## What it will refuse to do

- Invent a customer example, statistic, or proof point.
- Use a proof point past its 90-day freshness ceiling without flagging it.
- Present `draft` positioning as approved.
- Fill a `TODO(source)` or `SYNTHETIC` gap with a plausible guess.

If it says something is unavailable, that is the system working. The gap is in
the repo, and the fix is to add the content there — not to talk the assistant
into producing it.

## What it deliberately doesn't do

It doesn't recreate `/draft-content`, `/campaign-plan` or `/email-sequence` from
Anthropic's marketing plugin, or `/call-summary` and `/pipeline-review` from
sales. Those already exist and are better than a reimplementation. What they
don't have is *your* positioning — which is the whole contribution here. Use
both: this for grounded messaging, those for the broader workflow.
