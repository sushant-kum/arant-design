"""Fetch the brand typefaces, Jost and Newsreader, into fonts/ for the builds that render real type.

Both are SIL Open Font License 1.1 (OFL.txt beside each font), which allows the fonts to be bundled, embedded
and redistributed with this repository. They come from the google/fonts repository at a pinned commit, and every
file is checked against its SHA-256, so the rendered type is identical on every machine.

The files are kept in the repo, so builds work offline; run this only to restore or re-check them. It needs network
access to raw.githubusercontent.com, and uses the standard library only.
Run: python3 fetch_fonts.py   (or `pnpm identity:fonts`)
"""

import hashlib
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
COMMIT = "9710da1eacb3be272583c3224dcb70f9da6eadbb"  # google/fonts, main on 2026-09-30
BASE = f"https://raw.githubusercontent.com/google/fonts/{COMMIT}/ofl"

FILES = {  # local path in fonts/ → (path in google/fonts/ofl, SHA-256)
    "jost/Jost-Variable.ttf": (
        "jost/Jost%5Bwght%5D.ttf",
        "6343b70971000b04c5d401c96ae08ce371086135e999d5e1e1413039c0213076",
    ),
    "jost/OFL.txt": ("jost/OFL.txt", "1af3438a4d5f0ed2bdbc5751a5a67ebf6d537334161184b7fbb68503ef0ea0c5"),
    "newsreader/Newsreader-Variable.ttf": (
        "newsreader/Newsreader%5Bopsz,wght%5D.ttf",
        "8a08d13f8a6c0d51be379a60af84f945f65369a67e509ee3c3bdcc421254d7c1",
    ),
    "newsreader/OFL.txt": ("newsreader/OFL.txt", "fdfad38143ec470553cae82a1e45320bdd1b9ec70415d37bd0171051d8a4ded8"),
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check():
    """Paths that are missing or don't match their pinned hash."""
    bad = []
    for local, (_, digest) in FILES.items():
        path = os.path.join(FONTS, local)
        if not os.path.exists(path):
            bad.append(local)
            continue
        with open(path, "rb") as f:
            if sha256(f.read()) != digest:
                bad.append(local)
    return bad


def main():
    for local in check():
        remote, digest = FILES[local]
        with urllib.request.urlopen(f"{BASE}/{remote}", timeout=60) as r:
            data = r.read()
        if sha256(data) != digest:
            sys.exit(f"{remote}: downloaded file doesn't match its pinned SHA-256; not saved")
        os.makedirs(os.path.dirname(os.path.join(FONTS, local)), exist_ok=True)
        with open(os.path.join(FONTS, local), "wb") as f:
            f.write(data)
        print(f"fetched {local}")
    print(f"ok · {len(FILES)} font files in fonts/, all match their pinned SHA-256")


if __name__ == "__main__":
    main()
