#!/usr/bin/env python3
"""Verify every persona -> product reference resolves.

The repo's whole premise is that personas point at product claims rather than
restating them. That only holds if the pointers are real, so this makes the
linkage enforceable instead of aspirational. Run before committing.
"""
import re, sys, glob, os

defined = set()
for f in glob.glob("products/*.md"):
    defined |= set(re.findall(r"\{#(vp-[a-z-]+)\}", open(f).read()))

if not defined:
    sys.exit("FAIL: no {#vp-*} slugs defined in products/ — did a heading lose its slug?")

errors = []
for f in sorted(glob.glob("personas/*/README.md") + glob.glob("personas/_*.md")):
    body = open(f).read()
    used = {s for s in re.findall(r"\b(vp-[a-z-]+)\b", body) if not s.endswith("-")}
    for missing in sorted(used - defined):
        errors.append(f"{f}: references undefined slug '{missing}'")
    # a persona that cites the product folder should name the file
    if re.search(r"`products/`", body) and not os.path.basename(f).startswith("_"):
        errors.append(f"{f}: cites `products/` without naming the file")
    label = "/".join(f.split("/")[-2:])
    print(f"  {label:28} {len(used)} slug refs")

print()
if errors:
    print("FAIL")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print("OK — all persona references resolve against products/")
