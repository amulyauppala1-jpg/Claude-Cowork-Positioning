# Examples — not an asset library

**These are specimens, not marketing assets.** They exist to show the system
produces what it claims, so the ranking argument in `../README.md` can be read
next to the ranking applied. They are not for download, reuse or distribution.

## Why generated output doesn't normally live in this repo

The repo is the source of truth for *positioning*. These are output, and output
in a source repo has a specific failure mode: **it goes stale silently.**

Edit `../README.md` to reorder the CFO's value props and these files are
immediately wrong — and nothing catches it. `check-refs.py` catches a broken
slug reference because a slug is a pointer; a rendered landing page is a copy,
and a copy has no pointer to break. It's the same duplication-drift problem the
whole system is built to avoid, one layer out.

## What should happen instead

A marketer or seller **generates a fresh asset when they need one**, from
whatever the source resolves to at that moment. That is what the twelve skills
in `plugin/` are for. Nobody downloads a file from a repository.

Finished assets then live where the team actually works — a DAM, the CMS, Figma,
the campaign tool. Those systems handle versioning, approval and distribution;
a git repo handles none of that well for binary or rendered output.

## What's here

| File | |
|---|---|
| `SPINE.md` | The fixed decisions all three assets hold to. **Read this first** — it's the part worth reviewing. |
| `landing-section.html` | Landing page section |
| `pitch-narrative.html` | Five-slide pitch narrative |
| `ad-banner.html` | Ad units, 728×90 and 300×250 |
| `ad-and-email.md` | Ad copy rationale and the campaign email |

All generated on 2026-09-05 from `products/cowork-enterprise.md` and
`personas/cfo/README.md`, both `status: draft`. If either has changed since,
**these are out of date** — regenerate rather than editing them here.
