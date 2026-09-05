---
persona: <Role>
function: <Finance | Legal | ...>
seniority: C-level
roles_by_motion:
  departmental: <role>          # economic_buyer | champion | approver | blocker
  enterprise: <role>
applies_to: [cowork-enterprise]
owner: TBD
last_updated: <YYYY-MM-DD>
status: draft
---

# <Role> — Gatekeeper Profile

> **This is not a sales persona.** This role rarely initiates the purchase; they
> gate it. Assets built from this file should read as pre-answered review
> material, not as a pitch. If it sounds like a one-pager, it's wrong.

## What they own
Scope, reporting line, what lands on their desk and what doesn't.

## What kills a deal at this desk
The 2-3 things that make this person say no, or say "not this quarter."

## Measured on
The numbers their comp and credibility depend on.

## Value props, ranked for this buyer
Reference product slugs — never restate the claim.

1. `vp-<slug>` — why it leads here.
2. `vp-<slug>` — supporting.
3. `vp-<slug>` — weakest. Say why, so nobody re-adds it.

## Vocabulary
**Use:** words that carry weight with this function.
**Avoid:** words that reliably backfire, and why.

## Objections
Each one carries a source line and a confidence tier. No source, no objection.

| Tier | Meaning | Weight |
|---|---|---|
| `public research` | Analyst survey or trade reporting, multiple orgs | Highest |
| `practitioner opinion` | One informed person's synthesis; no sample | Directional |
| `SYNTHETIC` | Placeholder for an unattached connector | Never customer-facing |

## What satisfies them
The specific evidence that closes each objection — ideally a proof point
that already exists in `products/`.

## Who else is in the room
Who initiates, who they defer to, who they can overrule.
