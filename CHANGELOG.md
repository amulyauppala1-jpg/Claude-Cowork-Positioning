# Changelog

## 2026-09-05 (staying current + pricing)
- `ARCHITECTURE.md` and the overview page now name the assumed inbound connectors — Gong, Guru, a quote database, CRM, the Anthropic blog, Slack — each matched to the kind of staleness it can catch, and trace one update end to end: the 108-day-old sales proof point clearing through a PR that CI gates. Nothing writes to `main`.
- `pricing/cowork-enterprise.md` — the commercial layer, `SYNTHETIC`. Bracketed placeholders, never figures. Carries the per-seat-versus-run-rate comparison model, the approval-threshold question, and the consumption question that matters more than list price for a buyer measured on forecast accuracy.

## 2026-09-05 (repo is the backend)
- Removed the generated CFO assets. The repo holds the foundation, personas, brand, skills and checks; assets are generated in Claude on demand and live wherever the person needs them. Committing output puts a copy where a pointer belongs, and a copy goes stale with nothing to catch it.

## 2026-09-05 (deliverables)
- `personas/cfo/assets/` — three coordinated assets built to one spine: landing section, 5-slide pitch narrative, ad unit + email. All lead `vp-coverage`, share one proof point and one core phrase.
- `ARCHITECTURE.md` — diagram plus rationale and the five trust mechanisms.

## 2026-09-05 (source resolution)
- Every skill now resolves its source live-first: GitHub connector, then a direct raw fetch (live and zero-setup if the repo is readable), then the local folder, then the embedded snapshot. Stops at the first that works and reports which it used.
- `scripts/build-bundle.py` packages the whole system as one uploadable `.zip` for Settings > Skills. The embedded copy is the floor, not the goal.
- README documents the assumption the design rests on — a company-readable repo — and what happens when it doesn't hold.

## 2026-09-05 (request shapes)
- `deal-prep` — the sales-shaped request. "I have a CFO meeting Thursday" wants readiness, not an asset: lead line, what not to say, documented objections with answers, proof to bring, and what you cannot answer. Explicitly not customer-facing.
- `campaign-kit` — the marketing-shaped request. Fixes one spine (lead argument, proof point, core phrase, CTA) before writing, then delegates each format to its own skill, then checks the set against itself. Three asset skills run separately produce three assets that disagree.
- Both wired into `start-here` as the two request shapes most likely to be misrouted.

## 2026-09-05 (front door)
- `start-here` — a router skill with a deliberately broad trigger. Turns a vague ask into the right asset by inferring what it can and asking at most three plain-language questions. Never says "motion" — asks "one team, or the whole company?" instead. Raises known gaps (pricing, named competitors) before starting rather than after, and offers the roleplay check on delivery.
- `.claude/skills/` mirrors all ten plugin skills, kept honest by `scripts/sync-skills.py --check`.

## 2026-09-05 (plugin skills)
- Nine skills: `persona-one-pager`, `landing-page`, `pitch-and-narrative-deck`, `campaign-email`, `sales-outreach-sequence`, `blog-post`, `competitive-battlecard`, `internal-champion-pitch`, `roleplay-tester`.
- `internal-champion-pitch` composes two persona files — the champion's for voice, the approver's for decision criteria — and carries no brand styling, since vendor-looking material can't be forwarded.
- `roleplay-tester` runs six mechanical PASS/FAIL checks then attacks the draft in character. This is the trust instrumentation.
- `competitive-battlecard` documents a real gap: the repo has category-level differentiation but no `competitors/` layer, so named-competitor cards can't be built without inventing content.

## 2026-09-05 (system layer)
- `brand/README.md` — voice and tone derived from Anthropic's seven published values, plus the visual system. Colors extracted from the official media kit SVGs (Clay `#D97757`, Ivory `#FAF9F5`, Slate `#141413`); logos included. Typography left unsourced and marked, since the kit ships no font files or written guideline.
- Root `README.md` rewritten as an agent entry point: routing, precedence, non-negotiables.
- Personas restructured into per-persona folders (`personas/cfo/README.md` + `assets/`) so generated work lives beside the definition that produced it. Checkers updated to follow.
- `plugin/` — installable Cowork plugin with nine skills (`landing-section`, `pitch-narrative`, `ad-and-email`). Reads the repo live via the GitHub connector rather than bundling a copy, since a bundled copy is stale the moment a persona file changes.

## 2026-09-05 (corrections)
- Removed an unverified competitor claim about attorney-client privilege from `personas/general-counsel.md` and `products/`, along with unaudited competitor benchmark figures. Recording them even as open questions propagates them. The privilege *question* remains, as an escalation to counsel.
- Recalibrated the legal adoption finding: it is an existence proof that legal can lead adoption, not a profile of any given legal team. Using it to imply a cautious GC is behind reads as pressure, and caution is the correct posture for the role.
- Skill: two new rules covering both.

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
