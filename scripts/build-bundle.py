#!/usr/bin/env python3
"""Package the whole system into one uploadable .zip skill.

Why this exists: the runtime paths (clone the repo, or connect GitHub) both
require the user to reach the source. A salesperson shouldn't have to. This
embeds the positioning, personas, brand kit and every skill's instructions into
a single file they upload once in Settings > Skills.

The tradeoff is honest and unavoidable: an embedded copy is a snapshot. It is
stamped with the commit SHA and build date so its age is visible, and the fix
for staleness is republishing on merge, not pretending it's live.
"""
import os, sys, json, zipfile, subprocess, datetime, glob, shutil

OUT = "dist/cowork-positioning.zip"
sha = subprocess.run(["git","rev-parse","--short","HEAD"], capture_output=True, text=True).stdout.strip()
dirty = bool(subprocess.run(["git","status","--porcelain"], capture_output=True, text=True).stdout.strip())
built = datetime.date.today().isoformat()

os.makedirs("dist", exist_ok=True)
stage = "dist/_stage"
shutil.rmtree(stage, ignore_errors=True)
os.makedirs(stage)

# --- the router becomes the bundle's SKILL.md, rewritten to read embedded files
router = open("plugin/skills/start-here/SKILL.md").read()
body = router.split("---", 2)[2]
body = body.replace("""Read `README.md` from the repo (local folder or the GitHub connector), then list
what actually exists: which personas are in `personas/`, and which skills are
available. **Don't assume this document is current** — personas get added.""",
"""Read `reference/README.md` from this skill's own bundled files, then list what
actually exists: the personas in `reference/personas/`, and the asset
instructions in `reference/skills/`. Everything is embedded — there is nothing
to clone and no connector to configure.""")
body = body.replace("""Invoke the matching skill. It handles grounding, ranking, brand and citation.
**Don't rebuild its work here** — this skill routes, it doesn't generate.""",
"""Read `reference/skills/<name>.md` and follow it exactly. Those files carry the
grounding rules, format conventions and reporting requirements. Ground every
claim in `reference/products/cowork-enterprise.md`, rank using the persona file,
and apply `reference/brand/README.md`.""")

open(f"{stage}/SKILL.md","w").write(f"""---
name: cowork-positioning
description: >-
  The Cowork positioning system. Build any GTM asset — one-pager, landing page,
  deck, email, outreach sequence, blog post, battlecard, champion pitch,
  campaign set — for a named buyer (CFO, CMO, CRO, CHRO, General Counsel),
  grounded in embedded positioning, persona and brand files. Also prepares a
  seller for a specific meeting, and pressure-tests a draft in character. Use
  whenever someone mentions Cowork positioning, names one of those buyers or
  their function, asks for GTM or marketing or sales material, or says anything
  like "I need to use the Cowork positioning" or "prep me for this meeting."
---

# Cowork Positioning
{body}
---

## About this bundle

Everything is embedded under `reference/` — no repository access needed.

- **Built:** {built}
- **Source commit:** `{sha}`{" (uncommitted changes present at build time)" if dirty else ""}
- **Source:** github.com/amulyauppala1-jpg/Claude-Cowork-Positioning

**This is a snapshot, not a live read.** If the build date is more than a few
weeks old, say so when it matters — a proof point that was current at build time
may have passed its 90-day ceiling since. Re-export from the repo to refresh.
""")

# --- embed the content
def add(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

add("README.md", f"{stage}/reference/README.md")
add("products/cowork-enterprise.md", f"{stage}/reference/products/cowork-enterprise.md")
add("brand/README.md", f"{stage}/reference/brand/README.md")
for p in glob.glob("brand/logos/*.svg"):
    add(p, f"{stage}/reference/brand/logos/{os.path.basename(p)}")
for p in glob.glob("personas/*/README.md"):
    add(p, f"{stage}/reference/personas/{p.split('/')[1]}.md")
for p in glob.glob("plugin/skills/*/SKILL.md"):
    n = os.path.basename(os.path.dirname(p))
    if n != "start-here":
        add(p, f"{stage}/reference/skills/{n}.md")

json.dump({"built": built, "commit": sha, "dirty": dirty},
          open(f"{stage}/reference/VERSION.json","w"), indent=2)

# --- zip it
if os.path.exists(OUT): os.remove(OUT)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(stage):
        for f in files:
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, stage))
shutil.rmtree(stage)

n = len(zipfile.ZipFile(OUT).namelist())
print(f"built {OUT}  —  {n} files, {os.path.getsize(OUT)/1024:.0f} KB, commit {sha}")
if dirty:
    print("  warning: uncommitted changes were included")
