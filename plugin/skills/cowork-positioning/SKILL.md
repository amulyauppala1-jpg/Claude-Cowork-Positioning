---
name: cowork-positioning
description: >-
  The front door to the Cowork positioning system. Use whenever someone mentions
  Cowork positioning or messaging, asks for campaign, marketing or sales material
  for Cowork, names a buyer (CFO, CMO, CRO, CHRO, General Counsel, finance,
  marketing, sales, HR, legal), asks for a landing page, deck, email, ad, blog
  post, one-pager, battlecard or outreach sequence, or says anything like "use
  the Cowork positioning," "I need assets for my campaign," or "what can this
  do." Also use when a request is vague and positioning might be involved.
---

# Cowork positioning

This is one file. Everything it needs lives in a public repo and is read at
request time, so **this file never goes stale** — when the positioning changes,
the next request picks up the change with no reinstall.

The person using this probably doesn't know how the repo is organized and
shouldn't have to. **Turn a vague request into the right asset, asking as little
as possible.**

## Step 1 — Read the source. Never work from memory.

Base URL:

```
https://raw.githubusercontent.com/amulyauppala1-jpg/Claude-Cowork-Positioning/main
```

Fetch `README.md` first. It is the routing document and lists what exists.

Try in this order, stop at the first that works:

1. **Direct fetch** of the raw URL above. The repo is public, so this needs no
   connector and no account. **This is the normal path.**
2. **GitHub connector**, if one is attached to the session.
3. **Local folder**, if the repo is open as a workspace.

**If none of them work, stop and say so.** Do not build from memory of this
file, from a Google Doc, or from anything earlier in the conversation. A
plausible-looking asset built from an unknown source is the failure this system
exists to prevent, and it is worse than no asset. Say which path you used, in
one line, when you deliver.

Then read:

- `products/cowork-enterprise.md` — the foundation. What is true about Cowork.
- `personas/<role>/README.md` — the buyer. Emphasis, objections, vocabulary.
- `brand/README.md` — voice and register.
- `.claude/skills/gtm-from-positioning/SKILL.md` — the full grounding rules.
  **Read and follow them.** They are not restated here so they cannot drift.

Don't narrate any of this. They asked for help, not a status report.

## Step 2 — Work out what they need

Three things. **Infer what you can and ask only for the rest.** "I need a deck
for a CFO" already gives you two of three.

**Who is the audience?** Map a named role or function and move on. Personas live
in `personas/`: `cfo`, `cmo`, `cro`, `chro`, `general-counsel`. If they name a
buyer with no folder, say so and build the function-agnostic version. **Never
improvise a persona.**

**What is the deal shape?** Each persona declares `roles_by_motion`.
*Departmental* (a function head buying for their team) and *enterprise* (an
org-wide rollout) rank the value props differently and produce differently
shaped assets. **This is the one question worth asking** when the request
doesn't say. Ask it in plain language: is this one team, or the whole company?

**What are they making?** Map the request to a skill in
`plugin/skills/<name>/SKILL.md`:

| They want | Skill |
|---|---|
| Several assets for one campaign | `campaign-kit` |
| Web page, hero, section | `landing-page` |
| Deck, pitch, narrative | `pitch-and-narrative-deck` |
| Email, nurture, lifecycle | `campaign-email` |
| Outreach, sequence, cold email | `sales-outreach-sequence` |
| Blog, article, thought leadership | `blog-post` |
| One-pager, leave-behind | `persona-one-pager` |
| Competitor comparison | `competitive-battlecard` |
| Help a champion sell internally | `internal-champion-pitch` |
| Prep for a specific meeting | `deal-prep` |
| Pressure-test something already written | `roleplay-tester` |

**Fetch that skill and follow it.** It owns the format conventions; this file
only gets the request to the right place. If several assets are wanted, use
`campaign-kit` — it holds one argument and one proof point across the set,
which is the thing that breaks when assets are built separately.

## Step 3 — What must survive even if a fetch fails

The full rules are in `gtm-from-positioning`. These are the ones that matter
most and are repeated here on purpose:

- **Lead with what the persona ranks first**, not what sounds strongest while
  drafting. The ranking is written down because it is a decision, not a
  preference.
- **Every buyer here is an executive buying for a department.** The capability
  lands on their team; the consequence lands on them. Write both.
- **Never invent a number.** Not pricing, not ROI, not a percentage. Pricing is
  a placeholder file on purpose. If they ask, say the system has no figure and
  route it to the deal team. Refusing beats guessing.
- **Only quote a figure you have read on the page you are citing.** A search
  summary is not the source.
- **Competitor names stay internal.** Internal enablement can name them;
  customer-facing assets don't.
- **Check the proof point's date.** Anything past 90 days gets flagged in the
  output, not quietly used.
- **Respect the persona's avoid list.** Short copy is where banned vocabulary
  slips through, so check headlines and CTAs hardest.

## Step 4 — Deliver

Lead with the asset. Then, briefly:

- Which source you read from, and whether it was live.
- Which value prop you led with, and the one-line reason from the persona file.
- Anything you had to flag: a stale proof point, a missing number, a gap.

**The positioning is `status: draft`.** Say so once. It has not been signed off
and has not met a real buyer.

## If they ask what this can do

List the personas and the asset types above, in plain language. Then ask what
they're working on. Don't explain the repo structure.
