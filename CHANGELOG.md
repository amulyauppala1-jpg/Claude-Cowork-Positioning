# Changelog

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
