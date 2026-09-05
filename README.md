# Cowork Positioning Project

A single source of truth for Cowork positioning, set up so Claude Code reads from it directly every time it builds a GTM asset — so what gets generated can't drift from what's actually written down here.

## What's here

```
.claude/skills/gtm-from-positioning/SKILL.md    The skill — auto-loads via Claude Code
products/cowork-enterprise.md                    Enterprise positioning, with sourced proof points
refresh-tasks.md                                 Scheduled-task prompts for keeping the above current
```

Deliberately minimal right now: one positioning file, one skill. There are no `personas/`, `pillars/`, `pricing/`, or `segments/` folders yet — the skill checks what actually exists rather than assuming a fixed structure, so those can be added later without touching it.

## Using it

```bash
git clone https://github.com/amulyauppala1-jpg/Claude-Cowork-Positioning.git
cd Claude-Cowork-Positioning
claude
```

Cloning is the whole install — the skill lives at `.claude/skills/`, which Claude Code loads automatically for the project.

Then ask for what you need:

- "Build a one-pager for Cowork enterprise"
- "Write a LinkedIn post for Cowork using our positioning"
- "Is this on-positioning?" (paste a draft)

## What to expect from the output

Three things separate a grounded asset from plausible-sounding filler:

1. **It cites its source** — the file it pulled from, with the `last_updated` date, at the bottom of whatever it generates.
2. **It flags non-approved status.** `cowork-enterprise.md` is currently `status: draft`, and the skill surfaces that rather than treating whatever it finds as final.
3. **It won't invent proof points.** The file has three real, dated, sourced ones. Ask for something that would benefit from a customer example and it should reach for those specifically, with attribution, instead of a generic "customers tell us…"

## Confirming it's reading live

Worth doing once after any structural change, to be sure output reflects the file rather than something cached earlier in the conversation:

- Edit `products/cowork-enterprise.md` (change the key message, add a bullet), commit, then ask for a new asset in the same session. It should reflect the edit.
- Flip `status: draft` to `status: approved` and ask again — the draft warning should disappear.
- Remove a proof point and ask for an asset that would have used it — it should say it's missing rather than filling the gap.

## Keeping it current

`refresh-tasks.md` has three scheduled-task prompts — proof points, competitive positioning, and internal drift — at three different cadences, so the file doesn't depend on someone remembering to check it. Set them up once the relevant connectors are attached.

## Extending it

The same pattern scales. Add `personas/`, `pillars/`, `pricing/`, or `segments/` folders using the same frontmatter convention (`status`, `last_updated`, `owner`) and the skill picks them up without modification.
