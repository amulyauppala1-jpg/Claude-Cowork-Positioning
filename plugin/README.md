# Cowork Positioning — Cowork plugin

Lets marketing and sales build GTM assets from the positioning repo without
cloning anything, editing markdown, or asking the person who maintains it.

## What it does

12 skills, all grounded in the same source:

| Skill | Produces |
|---|---|
| `start-here` | **The front door.** Turns a vague ask into the right asset |
| `blog-post` | Long-form article — must be useful to someone who never buys |
| `campaign-email` | Marketing/nurture email, plus short paid copy |
| `competitive-battlecard` | Category battlecard (see the gap note in the skill) |
| `internal-champion-pitch` | A forwardable business case in *their* voice, not ours |
| `landing-page` | Landing page or page section, as HTML |
| `persona-one-pager` | Single-page overview — the canonical leave-behind |
| `pitch-and-narrative-deck` | 3–8 slide narrative, as HTML slides |
| `deal-prep` | A briefing for a specific meeting — not something to send |
| `campaign-kit` | A coordinated set that all leads with the same argument |
| `roleplay-tester` | Role-plays the buyer to test a draft. Run before anything ships |
| `sales-outreach-sequence` | Multi-touch 1:1 outreach cadence |

**If you don't know where to start, just say so.** Something like *"I need to
use the Cowork positioning"* or *"help me make something for a finance buyer"*
lands on `start-here`, which works out what you need by asking two or three
plain questions — no file names, no jargon — then routes to the right skill.

If you already know what you want, ask for it directly: *"landing page for a
CFO"*, *"outreach sequence for a CRO"*. The skill resolves the persona, checks
whether it's a departmental or company-wide purchase, ranks the value props for
that buyer, and cites what it used.

Two requests don't look like asset requests, and they get their own skills:
**`deal-prep`** turns "I have a CFO meeting Thursday" into a briefing — what to
lead with, what not to say, what you can't answer — rather than a document.
**`campaign-kit`** builds several assets as one thing, fixing the lead argument,
proof point and core phrase up front, because three skills run separately
produce three pieces that disagree with each other.

Two more aren't generators at all, and they're the reason this is a system
rather than a content mill:

- **`internal-champion-pitch`** is the only asset whose reader isn't its
  audience. The champion receives it; their CFO reads it. So it composes *two*
  persona files — the champion's for vocabulary, the approver's for decision
  criteria — and is written in their voice with no brand styling, because
  anything that looks like vendor material can't be forwarded.
- **`roleplay-tester`** role-plays the buyer to test a draft using the persona's
  documented objections, after six mechanical PASS/FAIL checks. It's how anyone
  can verify an asset without the person who built the repo.

## Install

```
/plugin marketplace add amulyauppala1-jpg/Claude-Cowork-Positioning
/plugin install cowork-positioning@cowork-positioning
```

Then **connect the GitHub connector** and grant access to
`amulyauppala1-jpg/Claude-Cowork-Positioning`. That step is required, not
optional — the skills read the repo at generation time, so without it they have
nothing to ground against.

Skills appear namespaced: `/cowork-positioning:landing-page`,
`/cowork-positioning:roleplay-tester`, and so on. Namespacing is automatic and
prevents collisions with other plugins' skills.

The repo is **private**, so anyone installing needs read access to it.

### If the marketplace add is blocked

Managed settings can restrict which marketplaces you may add, usually to
`anthropics/*` plus your own organization's repos. A personal repo will be
refused. That control is doing its job — don't route around it.

Two options: clone the repo and use the skills directly from `.claude/skills/`
(no install, works immediately), or ask whoever manages those settings to
allowlist the repo.

### To develop or test locally

```bash
claude --plugin-dir ./plugin
```

Loads it without installing. Run `/reload-plugins` after editing a skill.

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
