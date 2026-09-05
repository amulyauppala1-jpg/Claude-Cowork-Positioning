---
name: start-here
description: >-
  The front door for building anything from the Cowork positioning system. Use
  this whenever someone mentions Cowork positioning, asks for GTM or marketing
  or sales material for Cowork, names a buyer (CFO, CMO, CRO, CHRO, General
  Counsel, finance, marketing, sales, HR, legal), asks for a one-pager, deck,
  landing page, email, blog post, battlecard or ad, or says anything like "I
  need to use the Cowork positioning," "help me make something for a customer,"
  or "what can this do." Also use when the request is vague and positioning
  might be involved — route from here rather than guessing.
---

# Start here

The person using this probably does not know how the repo is organized, and
should not have to. **Your job is to turn a vague request into the right asset,
asking as little as possible.**

## Step 1 — Orient yourself first, silently

Read `README.md`, trying these in order and stopping at the first that works:
the **GitHub connector**; a **direct fetch** of
`https://raw.githubusercontent.com/amulyauppala1-jpg/Claude-Cowork-Positioning/main/README.md`
if the repo is public; the **local folder** if it's open as a workspace; or the
**embedded snapshot** at `reference/README.md` if this is a bundle.

Then list what actually exists — the personas in `personas/`, the skills
available. **Don't assume this document is current**; personas get added.

Note which source you got, and mention it once when you deliver — live versus a
dated snapshot is the difference between output that can be trusted and output
that should be checked.

Do not narrate this. The person asked for help, not a status report.

## Step 2 — Work out what they need

You need three things. **Infer whatever you can from what they already said and
only ask for the rest.** If they said "landing page for a CFO," you have two of
three — ask one question, not three.

### Who is the audience?

If they named a role or a function, map it and move on. Otherwise ask, in plain
language — no jargon, no file names:

> Who's this for?
> - **Finance** — CFO, or anyone signing off on the spend
> - **Marketing** — CMO and their team
> - **Sales** — CRO, revenue leaders
> - **People / HR** — CHRO
> - **Legal** — General Counsel
> - Not sure / general audience

"Not sure" is a legitimate answer: build the function-agnostic version from
`products/` and say that is what you did.

### What do they need to make?

Map plain words to skills. Someone saying "something to send before a meeting"
means a one-pager; "something for the website" means a landing page.

| They say | Skill |
|---|---|
| one-pager, overview, leave-behind, something to send | `persona-one-pager` |
| landing page, web page, site copy, hero | `landing-page` |
| deck, slides, pitch, presentation, narrative | `pitch-and-narrative-deck` |
| email, campaign, nurture, ad, banner | `campaign-email` |
| outreach, sequence, cadence, prospecting, follow-ups | `sales-outreach-sequence` |
| blog, article, thought leadership, post | `blog-post` |
| battlecard, competitor, "how we win against" | `competitive-battlecard` |
| something they can take to their boss / their team | `internal-champion-pitch` |
| check this, review, test, is this on-message | `roleplay-tester` |
| a meeting, call, demo, named account, "prep me" | `deal-prep` |
| a campaign, launch, "everything I need for" | `campaign-kit` |

If nothing matches, ask what they'd do with it rather than listing options.
The use tells you the format.

**Two requests aren't asset requests, and they're easy to misroute:**

- **A meeting or a named account** — "I have a CFO call Thursday" is not a
  request for a one-pager. They want to walk in ready. Route to `deal-prep`,
  which produces a briefing, not something to send.
- **Several assets for one audience** — route to `campaign-kit`, not three
  separate skills. Run separately they each lead with a different argument and
  read as unrelated; `campaign-kit` fixes one spine across the set.

### One team, or the whole company?

The question that changes the answer most, and the one nobody will volunteer.
Ask it in plain English — **never say "motion":**

> Is this for one team buying it for themselves, or a company-wide rollout?

It matters because it flips which argument leads. "One vendor for everyone" is
the strongest pitch to a CFO buying company-wide and close to irrelevant to a
CMO buying for forty people. If they don't know, assume **one team** — the more
common case — and say which you assumed.

## Step 3 — Say what you can't do, before you start

Check the persona file for `TODO(source)` gaps that affect this request and
**raise them now rather than at the end.** The two that bite most often:

- **Pricing.** There is no pricing content. Anything needing a number will say
  so instead of estimating.
- **Named competitors.** There is category-level differentiation but no
  competitor files, so a battlecard against a specific competitor can't be
  built without inventing it.

One sentence, not a disclaimer paragraph. Then carry on.

## Step 4 — Hand off

Invoke the matching skill. It handles grounding, ranking, brand and citation.
**Don't rebuild its work here** — this skill routes, it doesn't generate.

## Step 5 — Offer the check

After delivering, offer once:

> Want me to pressure-test this? I can read it as that buyer would and tell you
> where it falls down.

That runs `roleplay-tester`. It is the difference between output someone hopes
is right and output that has been checked, and most people won't know to ask.

## Tone

Be brief. Someone who asks for a one-pager wants a one-pager, not an education
in the positioning system. Explain the structure only if they ask.

Two things worth saying once, in passing, when relevant:

- If the positioning file is `status: draft`, say so — it means the language
  is still being signed off.
- If you led with a different argument than they expected, say why in one line.
  That's how they learn the system is doing something, not just writing.
