"""Fail if a brand colour is hard-coded anywhere in the identity source instead of read from the tokens, or if
tokens.json itself is inconsistent.

packages/tokens/tokens.json is the only place palette values may be written. This scans the build scripts for any
palette hex value (case-insensitive), checks that every {alias} in tokens.json resolves, and checks that every role
colour stored as a mix ($extensions["com.arantdesign"].mix) still equals that mix of the current palette. It exits
non-zero on any problem.
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


# tokens.json: every {alias} resolves, and every recorded mix matches the palette
def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


paths = {p for p, _ in tokens.tokens()}
for path, tok in tokens.tokens():
    missing = [a for a in aliases(tok["$value"]) if a not in paths]
    problems += [f"tokens.json: {path} refers to {{{a}}}, which doesn't exist" for a in missing]
    expected = tokens.recorded_mix(path)
    if expected and tok["$value"].upper() != expected:
        problems.append(f"tokens.json: {path} is {tok['$value']} but its recorded mix gives {expected}; update it")
if problems:
    print("Token problems found:\n  " + "\n  ".join(problems))
    sys.exit(1)
print(f"ok · no hard-coded brand colours in {HERE}; {len(paths)} tokens in tokens.json, all references resolve")
