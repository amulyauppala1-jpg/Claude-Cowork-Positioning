# Cowork Positioning System

**Agents: read this file first.** It routes you to the right content and states
the rules you must follow. Everything else assumes you have read it.

A single source of truth for Cowork positioning, structured so Claude can build
GTM assets from it without drifting from what is actually written down.

---

**Architecture:** see [`ARCHITECTURE.md`](ARCHITECTURE.md) — diagram, design
rationale, and what keeps output trustworthy.

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
  _TEMPLATE.md                   Start here for a new persona
brand/README.md                  Voice, tone, colors, logos
plugin/                          Installable Cowork plugin — 12 skills, entry point is start-here
.claude/skills/                  Same skills, auto-loaded on clone — kept in sync by script
scripts/                         Integrity checks and the bundle builder
dist/                            Built .zip skill — one upload, nothing to connect
refresh-tasks.md                 Scheduled tasks to keep the foundation current
```

**No generated assets live here, deliberately.** This repo is the backend: the
foundation, the persona layer, the brand kit, the skills and the checks. Assets
are generated in Claude when someone needs one and live wherever that person
works — a doc, a deck, the CMS, an email. Nothing is written back.

That isn't tidiness. A rendered page is a *copy*, not a pointer, so it goes stale
the moment a persona changes and nothing catches it — `check-refs.py` catches a
broken slug precisely because a slug points at something. Committing output
would reintroduce the drift the whole system exists to prevent, one layer out.

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

**Clone and open it** — works today, no install step:

```bash
git clone https://github.com/amulyauppala1-jpg/Claude-Cowork-Positioning.git
cd Claude-Cowork-Positioning && claude
```

The skills in `.claude/skills/` load automatically for anyone in the repo. This
is the path to use.

**Then just ask.** Someone who has never seen this repo can say *"I need to use
the Cowork positioning"* and the `start-here` skill works out the rest — who the
audience is, what they need, and whether it's a one-team or company-wide
purchase — in plain language. No file names, no jargon, nobody to ask.

**Install as a plugin** — for people who shouldn't have to clone anything:

```
/plugin marketplace add amulyauppala1-jpg/Claude-Cowork-Positioning
/plugin install cowork-positioning@cowork-positioning
```

Then connect the GitHub connector and grant access to this repo, since the
skills read it at generation time.

> **Note:** on a machine with managed plugin settings, adding a personal
> marketplace can be blocked by policy — the allowlist typically covers
> `anthropics/*` and your own org's repos. That is a supply-chain control
> working as intended, not a bug. Either use the clone path above, or ask
> whoever manages those settings to allowlist this repo.

**Claude Code** (maintainers): clone and run `claude` in the repo. The skill in
`.claude/skills/` auto-loads.

```bash
git clone https://github.com/amulyauppala1-jpg/Claude-Cowork-Positioning.git
cd Claude-Cowork-Positioning && claude
```

## Before committing

```bash
python3 scripts/check-refs.py && python3 scripts/check-sources.py && python3 scripts/sync-skills.py --check
```

`sync-skills --check` fails if `.claude/skills/` has drifted from `plugin/skills/`
— the skills exist in both places for two install paths, so the duplication is
enforced mechanically rather than remembered. Run it without `--check` to re-sync.

`check-refs` fails if a persona references a value prop slug that doesn't exist,
so the link to the foundation can't silently rot. `check-sources` fails on any
figure without a citation nearby — a number with no traceable source reads as
established, gets lifted into an asset, and can't be defended.

## Assumptions

**The repo is readable by everyone at the company.** Public, or org-visible with
read access granted broadly. That assumption is what makes the second source in
every skill's Step 1 work: a direct fetch of
`raw.githubusercontent.com/.../main/<path>` needs no connector, no account and
no clone, while still reading the current file. It is the only configuration
that delivers *live* and *zero-setup* at the same time.

**This repo is private today**, so that path doesn't resolve yet — which is
useful, because it exercises the fallback. Skills drop to the local folder if
one is open, then to the snapshot embedded in the bundle, and say which they
used. Nothing breaks; the output just tells you it may be dated.

The order is deliberate — most current first, always available last:

| Source | Live | Setup | When it applies |
|---|---|---|---|
| GitHub connector | Yes | Connect once, org-wide | Enterprise default |
| **Direct raw fetch** | **Yes** | **None** | **Repo readable — the assumption above** |
| Local folder | As of last pull | Clone | Maintainers |
| Embedded snapshot | No — dated | None | Floor. Always works |

**Two things follow from this, and both are design decisions rather than
accidents.** The skill *instructions* are stable and the *positioning* is what
goes stale, so instructions can safely ship embedded while content resolves
live. And a skill that silently used a six-month-old snapshot would be worse
than one that failed, so every skill reports its source and flags a stale
fallback.

## How sources are weighted

1. Anthropic / Claude published data
2. Independent named research
3. Aggregated secondary write-ups
4. Individual practitioner accounts

Reach down the list only for what the tier above doesn't cover, and say which
tier a figure came from. Where only a weak tier exists, claims are stated
directionally without a number — the direction is reliable, the decimal places
aren't. A community-contributed skill is not first-party evidence.
