---
product: Cowork
type: pricing
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: SYNTHETIC
---

# Cowork — Commercial model

> ## ⚠ SYNTHETIC — structure only, no real figures
>
> **This file contains no pricing.** Every number is a bracketed placeholder.
> It exists so the CFO conversation has a shape, and so the system can be shown
> reaching a pricing layer that currently holds nothing real.
>
> Per the rules in `.claude/skills/gtm-from-positioning/SKILL.md`, `SYNTHETIC`
> content **must never reach customer-facing output.** An asset that needs a
> number will say the number is unavailable — which is correct, and stays
> correct until someone with commercial authority replaces the placeholders.
>
> Do not fill these in from a guess, a competitor's published pricing, or a
> figure recalled from somewhere. The gap is the honest state.

## What the CFO actually needs

Not a list price. **A per-seat number set against current AI run-rate**, which is
a comparison, not a quote. See `personas/cfo/README.md` — the whole argument
leads with `vp-coverage`, and consolidation is only credible with arithmetic
behind it.

## The comparison model

The structure is the reusable part. Fill the left column from the customer's own
spend; the right is what Cowork replaces.

| Line | Today | Under Cowork |
|---|---|---|
| Chat assistant, per seat / year | `[CURRENT]` | consolidated |
| Copilot or equivalent, per seat / year | `[CURRENT]` | consolidated |
| Function-bought tools (marketing, sales, legal) | `[CURRENT]` | consolidated |
| Cowork, per seat / year | — | `[LIST PRICE]` |
| **Net change to AI run-rate** | | `[DELTA]` |

Two things make this land rather than read as vendor arithmetic:

- **Count only what actually gets displaced.** Inflating the left column to make
  the delta look better is the fastest way to lose a CFO, and they will check.
- **Show unused licences separately.** Roughly half of enterprise SaaS seats go
  unused; consolidating a licence nobody used is a real saving but a different
  argument from replacing one in daily use. Conflating them looks like padding.

## Consumption

Agentic work consumes more than chat, and a CFO measured on forecast accuracy
will ask what happens when usage grows — see the consumption objection in
`personas/cfo/README.md`, which is currently the sharpest one this repo cannot
answer.

> `TODO(source)`: whether the commercial model is per-seat, consumption-based, or
> a hybrid materially changes that answer. **This is the highest-value thing to
> establish**, ahead of list price — a predictable number that is higher beats an
> unpredictable one that might be lower, for this buyer specifically.

## Thresholds

Where approval sits changes who the asset is for — see `roles_by_motion` in each
persona.

| | |
|---|---|
| Below `[THRESHOLD]` | Function head signs. Departmental motion. |
| Above `[THRESHOLD]` | CFO approves. |
| Enterprise-wide | CFO is the economic buyer. |

> `TODO(source)`: thresholds vary by customer and are discoverable on a first
> call. Ask rather than assume — it decides which persona file applies.

## What must never be inferred

Discounting, term length, ramp schedules, and anything about another customer's
deal. A seller improvising on these does damage a correction cannot undo, and
none of it belongs in generated material regardless of what this file eventually
contains.
