---
name: blog-post
description: >-
  Drafts a blog post or thought-leadership article informed by a named buyer
  persona and the Cowork positioning repo. Use when asked for a blog post,
  article, thought leadership, or long-form content "for a [persona]" or
  "using our positioning."
---

# Blog post

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

## Step 4 — Understand the constraint

**A blog post is not a pitch, and this is the skill most likely to be misused.**
A reader arrives from search or a share, owing you nothing. If it reads as
marketing they leave, and the positioning does more harm than good.

The test: **the post should be useful to someone who never buys Cowork.** If
removing the product mentions leaves nothing of value, it is an ad.

## Step 5 — Build it

- **Lead with the problem, not the product.** Use the persona's documented
  pain — these are researched and specific, which is exactly what makes a post
  worth reading.
- **Earn the product mention.** One, placed where it genuinely answers the
  problem, usually two-thirds in. Never in the opening.
- **Cite the persona research** where it is public and citable — the sourcing
  discipline in the repo is itself credibility. Follow the source hierarchy and
  do not repeat a competitor's claims.
- **Take a position.** A post that could have been written by any vendor in the
  category has no reason to exist.
- 800-1,400 words. Descriptive subheads, not clever ones.

Value props inform what you argue; **do not list them.** A blog post that walks
through three value props in order is a one-pager with paragraphs.

## Step 6 — Render

Markdown. Suggest a title and two alternates. Flag any claim that would need
legal or comms review before publishing — this is the only asset here that goes
out publicly, so the bar is different.

## Final step — Report what you did

End every output with:
- **Provenance** — source files with their `last_updated` dates.
- **Status warning** if the positioning file is not `approved`.
- **Which value prop you led with and why**, in one sentence. This is how the
  requester verifies the system worked instead of trusting the output.
- **Vocabulary check** — name the persona's Avoid terms you steered around.
- **Gaps** — anything you could not include, and why. A stated gap is the system
  working; a filled gap is the system failing.
