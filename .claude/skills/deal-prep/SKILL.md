---
name: deal-prep
description: >-
  Prepares a seller for a specific meeting or deal with a named buyer — what to
  lead with, what they'll push back on, what not to say, and what you can't
  answer. Use when someone mentions a call, meeting, demo, discovery, QBR,
  renewal or a named account, or says anything like "I have a CFO meeting
  Thursday," "prep me for this," "how do I handle their legal team," or "what
  should I lead with."
---

# Deal prep

**The seller does not want an asset. They want to walk in ready.** Output a
briefing, not a document to send. Nothing here is customer-facing.

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

## Step 4 — Build the briefing

Keep it scannable — this gets read in the ten minutes before a call.

1. **Who you're talking to** — two lines. What they own, what they're measured
   on. Enough to sound like you did the work.
2. **Lead with this** — the persona's top value prop, plus the one-line reason.
   State it as the sentence to actually say, not the concept.
3. **Do not say** — the persona's Avoid list, with the reason for each. The
   highest-value section: it prevents a specific unforced error, and it is the
   part a seller cannot get anywhere else.
4. **They will push back on** — their top two or three documented objections, in
   the file's order, each with how to answer and which proof to reach for.
5. **Bring this proof** — dated, sourced entries only. Flag anything stale.
6. **You cannot answer** — the `TODO(source)` gaps that will come up. Pricing
   most often. **Say "I'll get you that" rather than improvising** — a number
   invented in a meeting cannot be walked back.
7. **Who else is in the room** — the buying committee from the persona file, and
   who to route which question to.

## Step 5 — Adapt to the meeting

- **First call** — heavier on 1, 2 and 3. Objections come later.
- **Later-stage or security review** — heavier on 4, 6 and 7.
- **The buyer is a champion, not the decider** — say so, and offer
  `internal-champion-pitch`. What they need is something to forward, and
  arming a champion badly loses the deal at a meeting you aren't in.

## Step 6 — Be honest about the limits

Close with one line: this covers what the repo documents. Real buyers raise
things it hasn't captured, and where the persona carries `TODO(source)` gaps,
say which parts you couldn't prepare.
