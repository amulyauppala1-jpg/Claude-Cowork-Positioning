# Cowork Positioning — Cowork plugin

Lets marketing and sales build GTM assets from the positioning repo without
cloning anything, editing markdown, or asking the person who maintains it.

## What it does

Three skills, each producing one asset type, all grounded in the same source:

| Skill | Produces |
|---|---|
| `landing-section` | A landing-page section as standalone HTML |
| `pitch-narrative` | A 3–5 slide pitch narrative as HTML slides |
| `ad-and-email` | An ad unit (headline / sub-headline / CTA) or a cold email |

Ask in plain language — *"landing page section for a CFO"* — and the skill
resolves the persona, checks the motion, ranks the value props correctly, and
cites what it used.

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
