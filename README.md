# Cowork Positioning System

**Agents: read this file first.** It routes you to the right content and states
the rules you must follow. Everything else assumes you have read it.

A single source of truth for Cowork positioning, structured so Claude can build
GTM assets from it without drifting from what is actually written down.

---

## Start here

1. **`products/cowork-enterprise.md`** — the foundation. What is true: claims,
   capabilities, plugin roster, proof points. Every other file defers to it.
2. **`personas/<role>/README.md`** — who you're writing for. Which claims lead,
   in what vocabulary, against which objections.
3. **`brand/README.md`** — how it should sound and look.

Read all three before producing anything. An asset missing any one of them is
generic, wrongly ordered, or off-brand.

## Layout

```
products/cowork-enterprise.md    The foundation — what is true
personas/
  cfo/          cmo/          cro/          chro/       general-counsel/
    README.md     README.md     README.md     README.md    README.md
    assets/       assets/       assets/       assets/      assets/
  _TEMPLATE.md                   Start here for a new persona
brand/README.md                  Voice, tone, colors, logos
plugin/                          Installable Cowork plugin — 9 asset skills + the tester
.claude/skills/                  Project skill — auto-loads in Claude Code
scripts/                         Integrity checks — run before committing
refresh-tasks.md                 Scheduled tasks to keep the foundation current
```

## Precedence — settle disagreements in this order

1. **`products/` wins on what is true.** A persona can never assert a capability
   the product file doesn't support.
2. **`personas/` wins on emphasis.** Which props lead, in what order, what
   vocabulary, which objections to pre-empt.
3. **`brand/` wins on register** — except where a persona's vocabulary section
   overrides it. "Efficiency" is neutral generally and dangerous with a CHRO.

## Two things that are easy to get wrong

**Value prop order is not fixed.** Personas reference product claims by slug
(`vp-executes`, `vp-configured`, `vp-coverage`) and rank them differently.
`vp-coverage` leads for a CFO enterprise-wide and comes *last* for a CMO buying
for their own team. Using the product file's default order is a silent error.

**A persona's role depends on the motion, not the person.** Each persona declares
`roles_by_motion`. The same CMO is the economic buyer for a departmental purchase
and a champion in an enterprise rollout, and those need differently shaped
assets. If the request doesn't say which motion, ask.

## Non-negotiables

- **Check `status`.** Files carry frontmatter. Anything not `approved` must be
  flagged in the output — the product file is currently `draft`.
- **Never invent a proof point.** Use only dated, sourced entries. Flag anything
  past its 90-day ceiling.
- **`TODO(source)` and `SYNTHETIC` mean the content is missing**, not that you
  should fill the gap. Say what was unavailable.
- **Never write down an unverified number**, even to warn against it. Record the
  question, not the value.
- **Don't repeat a competitor's factual claims or benchmark figures.**
- **Adoption data is an existence proof, not a profile.** Never imply a buyer is
  behind their peers.
- **Cite your source** at the end of every asset, with the `last_updated` date.

Full rules: `.claude/skills/gtm-from-positioning/SKILL.md`.

## Using it

**Cowork** (marketers and sales — no clone needed): install the plugin in
`plugin/`, connect GitHub, point it at this repo. See `plugin/README.md`.

**Claude Code** (maintainers): clone and run `claude` in the repo. The skill in
`.claude/skills/` auto-loads.

```bash
git clone https://github.com/amulyauppala1-jpg/Claude-Cowork-Positioning.git
cd Claude-Cowork-Positioning && claude
```

## Before committing

```bash
python3 scripts/check-refs.py && python3 scripts/check-sources.py
```

`check-refs` fails if a persona references a value prop slug that doesn't exist,
so the link to the foundation can't silently rot. `check-sources` fails on any
figure without a citation nearby — a number with no traceable source reads as
established, gets lifted into an asset, and can't be defended.

## How sources are weighted

1. Anthropic / Claude published data
2. Independent named research
3. Aggregated secondary write-ups
4. Individual practitioner accounts

Reach down the list only for what the tier above doesn't cover, and say which
tier a figure came from. Where only a weak tier exists, claims are stated
directionally without a number — the direction is reliable, the decimal places
aren't. A community-contributed skill is not first-party evidence.
