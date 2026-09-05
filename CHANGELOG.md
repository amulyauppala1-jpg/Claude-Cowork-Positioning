# Changelog

## 2026-09-05 (CHRO + General Counsel — persona set complete)
- `personas/chro.md` — the HR plugin's two headline capabilities (performance review, compensation analysis) sit in HR's two most legally exposed domains. Lead with onboarding and policy guidance instead; this inverts the instinct used for every other persona.
- `personas/general-counsel.md` — **corrects the gatekeeper assumption.** First-party evidence: legal became the number-one power-user function in Cowork at 3x any other. The GC is the leading function, not the reluctant one. File serves two readers — legal as buyer, legal as blocker.
- Open, highest-priority question: an unverified competitor claim that a 2026 federal ruling found Claude exchanges lack attorney-client privilege. Recorded as a question to verify, not repeated as fact.
- `products/` gains legal and HR plugin detail plus the legal adoption data.

## 2026-09-05 (sourcing audit)
- `scripts/check-sources.py` — fails on any numeric claim without a citation nearby. Found 9 uncited blocks across the three personas on first run.
- Source hierarchy encoded: Anthropic first-party > independent named research > aggregated secondary > practitioner. Community-contributed skills are explicitly not first-party evidence.
- Unverifiable figures are now deleted rather than parked behind a warning label — the number survives the label. Removed one such figure; hedged several tier-3 statistics to directional claims.

## 2026-09-05 (CRO)
- `personas/cro.md` — CRO. Opening position is adoption, not capability or measurement: only 19% of reps use AI features they already have. Leads `vp-configured`, completing a three-way split (CFO leads `vp-coverage`, CMO `vp-executes`, CRO `vp-configured`).
- `products/cowork-enterprise.md` — added sales plugin detail, including that it runs standalone without connectors.

## 2026-09-05 (first-party function messaging)
- `products/cowork-enterprise.md` — added the shipped plugin roster (11 plugins, marketing and finance command lists) and a first-party proof point: Anthropic's own marketing ops team, weekly metrics review cut from 1-2 days to ~2 hours (blog 2026-07-08, 59 days old).
- `personas/cmo.md` — brand-risk objection now answered with `/brand-review` and the audit-agent + human-approval structure rather than reassurance. `/competitive-brief` largely answers "do I have to build that?".
- `personas/cfo.md` — the finance plugin makes the CFO a potential *user*, not only a buyer, which is the strongest available answer to the ROI objection. Added a third motion: a finance-first land where the CFO is the economic buyer for their own function.

## 2026-09-05 (CMO + sourcing rules)
- `personas/cmo.md` — CMO. Value-prop ranking is close to the inverse of the CFO's, which is the motion model doing real work.
- Skill rule: single sources inform a point of view, they do not establish a claim. An n=1 entry can corroborate or supply vocabulary, never solely support a value-prop ranking. Applied retroactively to the CFO file.
- Snowflake GTM programme added to the CMO as an illustration of what `vp-configured` produces, explicitly marked not a proof point.

## 2026-09-05 (personas)
- `personas/cmo.md` — CMO, sourced from 2026 Gartner CMO Spend Survey and trade research. Value-prop ranking is close to the inverse of the CFO's.
- `roles_by_motion` replaces fixed `role_in_deal`: a persona's role is a property of the deal shape, not the person. Departmental vs. enterprise motion changes the value-prop ranking.
- `scripts/check-refs.py` — verifies every persona->product slug reference resolves, so the source-of-truth link is enforced rather than assumed.

## 2026-09-05 (later)
- Added stable slugs to product value props (`vp-executes`, `vp-configured`, `vp-coverage`) so personas can reference claims by name rather than position.
- Added `personas/` with a gatekeeper template and `cfo.md`, sourced from public 2026 analyst/trade research (cited inline). No connector data.
- Skill: added persona composition + precedence rules, and a guard treating `TODO(source)` / `SYNTHETIC` as missing content.

## 2026-09-05
- Initial commit: `products/cowork-enterprise.md` with sourced proof points (Anthropic blog, July 7 and Aug 11, 2026), the `gtm-from-positioning` skill, and `refresh-tasks.md`.
