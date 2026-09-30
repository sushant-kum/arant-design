"""Fail if a brand colour is hard-coded anywhere in the identity source instead of read from the tokens.

packages/tokens/tokens.json is the only place palette values may be written. This scans the build scripts for any
palette hex value (case-insensitive) and exits non-zero if it finds one.
Run: python3 check_tokens.py   (or `pnpm identity:check`)
"""

import os
import re
import sys

import brand_tokens as tokens

HERE = os.path.dirname(os.path.abspath(__file__))
palette = {tokens.color(k).lstrip("#").lower(): k for k in tokens.palette()}
problems = []
for fname in sorted(os.listdir(HERE)):
    if not fname.endswith(".py") or fname == os.path.basename(__file__):
        continue
    with open(os.path.join(HERE, fname)) as fh:
        lines = fh.readlines()
    for n, line in enumerate(lines, 1):
        for m in re.finditer(r"#?([0-9A-Fa-f]{6})\b", line):
            key = palette.get(m.group(1).lower())
            if key:
                problems.append(f"{fname}:{n}: {m.group(0)} is color.{key}, use brand_tokens.color('{key}')")
if problems:
    print("Hard-coded brand colours found:\n  " + "\n  ".join(problems))
    sys.exit(1)
print(f"ok · no hard-coded brand colours in {HERE}")
