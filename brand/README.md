---
type: brand
owner: TBD
last_updated: 2026-09-05
status: draft
sourcing: first-party
---

# Brand Kit — voice, tone, and visual system

Read this **with** a product file and a persona file, never instead of them.
`products/` says what is true, `personas/` says what to emphasize, and this file
says how it should sound and look. Any asset that skips this reads as generic.

---

## Voice — derived from the company values

Anthropic publishes seven values. Three of them are directly a writing standard,
and they are unusually useful because they resolve real drafting arguments.

### "Do the simple thing that works"

The single most useful voice instruction available. Empirical, results-focused,
straightforward over complex.

In practice:
- Say the thing. Don't build to it over three sentences.
- Prefer the plain word. *Use*, not *leverage*. *Build*, not *architect*.
- Cut throat-clearing. "It's worth noting that" is never worth noting.
- One idea per sentence. If it needs a semicolon to survive, split it.

### "Be helpful, honest, and harmless" — *high trust, low ego, kind and direct*

This is the sentence that makes our sourcing rules a brand requirement rather
than an internal nicety.

- **Honest** means no unverifiable claims, no borrowed numbers, no proof points
  that don't exist. The rules in `.claude/skills/gtm-from-positioning/SKILL.md`
  are this value expressed as a process.
- **Low ego** means don't oversell. Naming a limitation earns more than
  claiming it away — which is exactly why the legal plugin's own "all outputs
  should be reviewed by licensed attorneys" line is an asset, not a caveat.
- **Direct** means the reader gets the answer, not a journey toward it.

### "Be good to our users" — *generosity and kindness*

Applied to GTM: write for the reader's problem, not our launch calendar. The
persona files exist so an asset can be about their week rather than our roadmap.

---

## Tone

Confident and quiet. The product claims are strong enough that hype makes them
sound weaker. The register is a capable colleague explaining something clearly —
not a vendor, not a keynote.

**Never:** revolutionary, game-changing, unleash, supercharge, transform your
business, the future of work, 10x, effortless, seamless, magic.

**Sparingly:** *powerful*, *unprecedented*, *AI-powered*. If the sentence works
without it, it works better without it.

**Modulate by persona** — the vocabulary sections in `personas/` override
anything here. "Efficiency" is neutral in general and actively dangerous with a
CHRO. When this file and a persona file disagree, **the persona wins**, same
precedence as `products/` over `personas/` on matters of fact.

---

## Visual system

Colors taken from the official media kit SVGs, so these are exact.

| Name | Hex | Use |
|---|---|---|
| **Clay** | `#D97757` | The accent. Sparingly — one focal point per view. Never body text. |
| **Ivory** | `#FAF9F5` | Default background. Warm off-white, not pure white. |
| **Slate** | `#141413` | Text and dark surfaces. Near-black, never `#000`. |

Supporting values in the kit: `#DC6038` (warmer Clay variant), `#151514`
(Slate variant). Use the primaries unless matching an existing surface.

**The Ivory/Slate pairing is the brand's most recognizable property** — warm
off-white with near-black, Clay used once. A deck or page that reads as
Anthropic gets that pairing right before it gets anything else right. Pure white
on pure black is the most common way to lose it.

### Typography

> `TODO(source)`: the media kit contains logos only — no font files and no
> written brand guideline. The actual typefaces are not sourced here.
> Until they are, use a system stack and don't assert a brand font:
> `ui-sans-serif, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif`
> with a serif stack for long-form display. Generous line height (1.6 body),
> generous margins. The restraint carries the brand more than the typeface does.

### Logos

In `brand/logos/`, from the official kit:

| File | Use |
|---|---|
| `claude-logo-slate.svg` | Claude wordmark on Ivory or light backgrounds |
| `claude-logo-ivory.svg` | Claude wordmark on Slate or dark backgrounds |
| `claude-spark-clay.svg` | The Spark mark, Clay — use as an accent, not a bullet |
| `anthropic-logo-slate.svg` | Anthropic wordmark, light backgrounds |

Don't recolor, rotate, stretch, add effects to, or place a logo on a busy
background. If the contrast is wrong, change the background rather than the mark.

---

## Output format

**Default to HTML** for anything visual — landing page sections, slides, ad
units. It renders anywhere, needs no design tool, and can be published as an
artifact for review. Slides are HTML sections, not a deck file, unless someone
specifically asks for `.pptx`.

Reference the tokens rather than hardcoding:

```css
:root {
  --clay:  #D97757;
  --ivory: #FAF9F5;
  --slate: #141413;
}
```

---

## Checklist before any asset ships

1. Grounded — every claim traces to `products/`, cited.
2. Persona-ranked — value props ordered per that persona and motion, not the
   product file's default order.
3. Vocabulary-checked — nothing from that persona's **Avoid** list.
4. Proof-checked — no invented customers or statistics; stale proof points flagged.
5. Tone-checked — no banned words; would a capable colleague say it out loud?
6. Visually correct — Ivory ground, Slate text, Clay used once.
7. Status-flagged — the positioning file is `status: draft` and the asset says so.

---

## Sourcing note

Values are from [Anthropic's company page](https://www.anthropic.com/company)
(tier 1). Colors are extracted from the official media kit SVGs (tier 1, exact).
Typography is **unsourced** and marked as such. Voice guidance is this repo's own
interpretation of the published values applied to GTM writing — `analysis` tier,
not something Anthropic has published as a brand voice guide. Label it that way
if anyone asks.
