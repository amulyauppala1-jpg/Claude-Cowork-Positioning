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

Pull whatever's relevant to the request. This repo currently has `products/`,
`personas/`, `brand/` and `pricing/` (no `pillars/`, `competitors/` or `segments/` yet).
**`pricing/` is `SYNTHETIC`** -- structure and bracketed placeholders, no figures.
Use it to shape a commercial conversation; never render a placeholder as a number -- don't assume others exist; check what's actually here before reading.

## Step 2: Check status before using anything

Every file's frontmatter has `status`. If it's anything other than `approved` (e.g. `draft`), say so before using it -- don't silently treat draft positioning as final.

## Step 2b: Compose product + persona

If the request names a role -- "for a CFO", "email to a CHRO", "a legal buyer" --
look for a matching file in `personas/`. If none exists, say so and build the
function-agnostic version. Don't improvise the persona.

Persona files reference product value props by slug (`vp-executes`,
`vp-configured`, `vp-coverage`) rather than restating them. Resolve each slug
against `products/` and use that file's wording as the source of truth for what
the claim actually is.

**Precedence when the two conflict:**

- `products/` wins on **what is true** -- claims, capabilities, proof points.
  A persona file can never assert a capability the product file doesn't support.
- `personas/` wins on **emphasis and framing** -- which props lead and in what
  order, vocabulary, which objections to pre-empt, what the asset is *for*.

Personas declare `roles_by_motion`, because a persona's role is a property of the
deal, not of the person. Establish the motion before building:

- **departmental** -- a function head buying for their own team.
- **enterprise** -- an org-wide rollout, typically signed by the CFO or CIO.

If the request doesn't say, ask. Guessing picks the wrong value-prop ranking:
`vp-coverage` is the strongest argument in an enterprise motion and among the
weakest in a departmental one, since org-wide breadth is irrelevant to someone
buying for one function.

Once the motion is known, look up the role it maps to. The role determines the
*shape* of the asset, not just its content:

- `economic_buyer` -- makes a case and drives to a decision. Objections are
  decision criteria, so handle them in the body rather than deferring to a FAQ.
  If the persona marks a BLOCKING GAP, say plainly that the asset is incomplete.
- `champion` -- the reader is not the buyer. They need ammunition to sell
  internally: a case they can forward, in their own function's language.
- `approver` / `blocker` -- pre-answered review material, not a pitch. Leading
  with a value proposition is the wrong shape even when every claim is correct.

## Step 2c: Unsourced content is a gap, not a blank to fill

Two markers mean the content is not real:

- `TODO(source)` -- not yet gathered.
- `SYNTHETIC` -- a placeholder standing in for a connector that isn't attached.

Treat both exactly like a missing proof point: never render them into an asset,
and tell the user which section was unavailable and why. `SYNTHETIC` content must
never reach customer-facing output under any circumstances.

**Prefer first-party evidence.** When writing about Cowork, Anthropic's own
published data outranks everything else -- it is both more relevant and more
defensible than third-party research about the category. Order of preference:

1. Anthropic / Claude published data (blog, docs, plugin directory)
2. Independent named research (an analyst firm or a vendor's own primary survey)
3. Aggregated secondary write-ups (a blog restating other people's numbers)
4. Individual practitioner accounts

Reach down the list only for what the tier above doesn't cover, and say which
tier a figure came from. A community-contributed skill or template is **not**
first-party evidence -- it shows what someone built, not what the product ships.

**Competitor names are internal-only.** Persona files, deal prep and battlecards
name them, because a seller needs to know what they're up against. Anything
customer-facing -- landing pages, ads, emails, decks, blog posts -- does not.
When a sourced statistic names a competitor, generalise it for external use: "the
most expensed application is now an AI assistant" carries the same argument
without the name. See `brand/README.md`.

**Don't propagate a competitor's factual claims.** Marketing from a competing
vendor is not a source. Its benchmark figures are unaudited self-comparisons, and
its assertions about our product come from a party with an interest in them being
true. Recording such a claim even as an open question puts it in front of every
future reader -- leave it out. Reference competitor *framing* generically where
useful (the argument they make), never their figures or factual assertions.

**Never write down an unverified number, even to warn against it.** If a figure
cannot be traced to a dated, citable source, delete it. Do not park it behind a
"do not use" label -- the number stays in the file, and the next person to skim
it will lift the figure and miss the caveat. Record the open *question* instead
("adoption rate worth sourcing"), never the unsourced value.

**Adoption data is an existence proof, not a profile.** Evidence that a function
or role commonly behaves some way shows what is possible; it never describes the
person in the room. Never use an adoption statistic to imply a buyer is behind
their peers -- caution is a legitimate posture, and the pressure reads badly.

**Single sources inform a point of view; they do not establish a claim.** A
`primary source` or `practitioner opinion` entry is n=1 -- one person's
experience, however well-informed. It can corroborate, sharpen, or add
vocabulary. It must never be the sole support for a load-bearing claim such as a
value-prop ranking. If the only evidence for a lead is one person saying so, mark
it as the repo's POV rather than presenting it as established.

Sourced content additionally carries a `confidence:` tier. `analysis` means the
reasoning is the repo's own with no external source behind it -- usable to shape
an internal draft, never presentable as evidence. `public research` can
be stated plainly. `practitioner opinion` is a single person's synthesis with no
sample behind it -- use it to shape framing, but don't render it as though it
were survey data, and never attribute a statistic to it.

## Step 2d: Structure and altitude

Personas carry two structures. Use both.

**Moore's framework** (`## Positioning` sections) gives the shape:
*For [customer] that need [need], [product] is a [category] that [benefit]* --
and *Unlike [alternative], [product] provides [differentiation]*. The `Unlike`
clause earns the most scrutiny: it names the alternative **this** buyer is
weighing, which differs by role. If an asset can't state it, the differentiation
isn't defensible for that buyer.

The **category** claim matters on its own. "Agentic workspace" and "AI assistant"
get judged against different things -- outcomes versus answers. Don't let an
asset drift into the second.

**The ladder** (`## The ladder`) gives the altitude:

1. Feature -- what it is
2. Functional benefit -- what gets done
3. Business outcome -- the number that moves
4. What it means for them -- personal stake

**Address the executive, name the team.** Every persona here is an executive
buying for a department or the whole company, not for themselves. The pattern is
almost always *your team gets X, which means you get Y*. A line that says only
"capacity added" hides whose capacity and whose risk, which is the difference
between a claim a buyer recognises and one they skim past.

**Lead from rung 2 or 3, never rung 1.** Feature-led openings are the most common
B2B failure: structurally fine, pitched a rung too low. **Rung 4 shapes what you
emphasise and is rarely said aloud** -- naming someone's personal exposure back
to them reads as manipulative.

Four things a positioning claim is not, all easy to slip into:

- **A tagline.** Positioning is not "Just Do It."
- **A feature list.** "Provides AI, automation and integrations" says nothing.
- **Generic.** "For businesses that need efficiency" is positioning theatre.
- **Aspirational fluff.** "Revolutionises productivity" with no specifics is noise.

## Step 3: Build the asset

- Every claim should trace to something actually present in the fetched file(s). Flag gaps rather than filling them with a plausible guess.
- **Proof points are non-negotiable:** only use a named customer or stat if the file's proof points section has a dated, sourced entry. If a proof point is more than ~90 days old at generation time, flag it as due for a refresh.
- Match the requested output format's own conventions (markdown for quick drafts; use docx/pptx/pdf skills if a polished file is requested).

## Step 4: Cite the source

End every generated asset with a provenance line, e.g.:

> *Grounded in `products/cowork-enterprise.md` (updated 2026-09-05).*

## Step 5: Flag drift

If a fetched file conflicts with something the user says in chat, say so and ask whether the repo needs updating -- don't quietly reconcile the two.
