#!/usr/bin/env python3
"""Flag numeric claims that have no citation nearby.

A number without a traceable source is the failure mode this repo exists to
prevent: it reads as established, gets lifted into an asset, and nobody can
find where it came from. This finds them. Run alongside check-refs.py.

LIMIT, and it matters: this proves a citation is PRESENT near a figure. It does
not and cannot prove the figure appears in the cited page. A number lifted from
a search-result summary and attributed to a page that never contained it passes
this check cleanly. Verifying that is the writer's job -- see the sourcing rules
in .claude/skills/gtm-from-positioning/SKILL.md.

Heuristic: split each file into blocks on blank lines. A block containing a
figure must have a source marker in itself or the block immediately after.
"""
import re, sys, glob, os

FIGURE = re.compile(r"(?<![\w.])\d{1,3}(?:\.\d+)?\s?%|\b\d+\.\d+x\b")
# "90-day ceiling" is this repo's own freshness rule, not a sourced claim
NOISE = re.compile(r"90[- ]day (ceiling|shelf)")
MONTHS = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
SOURCE = re.compile(
    r"Source:|confidence:|\]\(https?://|tier \d"
    r"|\d{4}-\d{2}-\d{2}"
    rf"|(?:{MONTHS})[a-z]* \d{{1,2}}, \d{{4}}"
    r"|Survey|Gartner|Forrester|Salesforce|Anthropic blog", re.I)
# prose that names its own limits rather than asserting a figure
HEDGED = re.compile(r"trace only to|directionally|without numbers deliberately|don't quote|do not quote", re.I)

flagged = []
for f in sorted(glob.glob("personas/*/README.md") + glob.glob("personas/_*.md")) + sorted(glob.glob("products/*.md")):
    blocks = open(f).read().split("\n\n")
    for i, b in enumerate(blocks):
        if not FIGURE.search(NOISE.sub("", b)):
            continue
        window = " ".join(blocks[i:i+2])
        if SOURCE.search(window) or HEDGED.search(window):
            continue
        first = next((l for l in b.strip().splitlines() if l.strip()), "")
        flagged.append((f, FIGURE.findall(b)[:4], first[:88]))

for f, figs, line in flagged:
    print(f"  {f}")
    print(f"    figures: {figs}")
    print(f"    {line}")
    print()

if flagged:
    print(f"FAIL — {len(flagged)} block(s) with uncited figures")
    sys.exit(1)
print("OK — every numeric claim has a citation or is explicitly hedged")
