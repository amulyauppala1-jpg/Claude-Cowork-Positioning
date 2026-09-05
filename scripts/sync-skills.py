#!/usr/bin/env python3
"""Keep .claude/skills/ in sync with plugin/skills/.

The skills need to exist in two places for two different install paths:

  plugin/skills/   — the plugin, installable via a marketplace. Blocked on this
                     machine by enterprise policy until the repo is allowlisted.
  .claude/skills/  — project skills, auto-loaded by anyone who clones the repo.
                     No install, no marketplace, no policy. This is the path
                     that works today.

plugin/skills/ is canonical. Two copies of anything drifts, so this makes the
duplication mechanical instead of manual: --check fails if they diverge, and
running it without a flag re-syncs.
"""
import sys, shutil, filecmp, glob, os

SRC, DST = "plugin/skills", ".claude/skills"
KEEP = {"gtm-from-positioning"}          # project skill, not part of the plugin

check = "--check" in sys.argv
names = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{SRC}/*/SKILL.md"))
drift = []

for n in names:
    s, d = f"{SRC}/{n}/SKILL.md", f"{DST}/{n}/SKILL.md"
    if not os.path.exists(d) or not filecmp.cmp(s, d, shallow=False):
        drift.append(n)
        if not check:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)

# a skill deleted from the plugin must not linger in .claude/
stale = [os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{DST}/*/SKILL.md")]
stale = [n for n in stale if n not in names and n not in KEEP]
for n in stale:
    drift.append(f"{n} (stale)")
    if not check:
        shutil.rmtree(f"{DST}/{n}")

if check:
    if drift:
        print("FAIL — .claude/skills is out of sync with plugin/skills:")
        for d in drift:
            print("  " + d)
        print("\nRun: python3 scripts/sync-skills.py")
        sys.exit(1)
    print(f"OK — {len(names)} plugin skills mirrored into .claude/skills")
else:
    print(f"synced {len(drift)} of {len(names)}" if drift else f"already in sync ({len(names)})")
