---
name: gtm-from-positioning
description: >-
  Generates GTM deliverables (one-pagers, social copy, sales talk tracks, battlecards, email sequences, deck content) for a named product or persona by pulling current positioning directly from this repo -- never from memory or a prior conversation's cached understanding. Use whenever asked to write, draft, or build a GTM asset 'for [product/persona]' or 'using our positioning,' whenever a product or persona name is mentioned as the target of an asset, or when asked to check whether an asset is 'on-positioning.' The repo is the review gate, not a person -- content isn't final until it's merged here.
---

# GTM From Positioning

Turns this repo into a live source Claude reads from every time it builds a GTM asset, so output can't drift from the current, approved version of positioning.

This skill ships inside the repo at `.claude/skills/gtm-from-positioning/`, so cloning the repo and running Claude Code from inside it is the entire install -- project-scoped skills auto-load from this path, no separate setup.

## Step 1: Get fresh content

**In Claude Code (this repo cloned locally):** Run `git pull` before reading any positioning file for a new request -- freshness here is a git operation, not a network fetch, since Claude already has filesystem access to the clone. Then read files directly.

**In claude.ai chat (repo not cloned):** Fetch the raw file instead -- e.g. `https://raw.githubusercontent.com/<org>/<repo>/main/products/cowork-enterprise.md` via `web_fetch` for a public repo, or the GitHub connector for a private one.

Pull whatever's relevant to the request. This repo currently only has a `products/` folder (no `personas/`, `pillars/`, `pricing/`, or `segments/` yet) -- don't assume those exist; check what's actually here before reading.

## Step 2: Check status before using anything

Every file's frontmatter has `status`. If it's anything other than `approved` (e.g. `draft`), say so before using it -- don't silently treat draft positioning as final.

## Step 3: Build the asset

- Every claim should trace to something actually present in the fetched file(s). Flag gaps rather than filling them with a plausible guess.
- **Proof points are non-negotiable:** only use a named customer or stat if the file's proof points section has a dated, sourced entry. If a proof point is more than ~90 days old at generation time, flag it as due for a refresh.
- Match the requested output format's own conventions (markdown for quick drafts; use docx/pptx/pdf skills if a polished file is requested).

## Step 4: Cite the source

End every generated asset with a provenance line, e.g.:

> *Grounded in `products/cowork-enterprise.md` (updated 2026-09-05).*

## Step 5: Flag drift

If a fetched file conflicts with something the user says in chat, say so and ask whether the repo needs updating -- don't quietly reconcile the two.
