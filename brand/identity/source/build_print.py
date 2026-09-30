"""Print files: vector PDFs and JPGs on warm ivory, coloured from packages/tokens/tokens.json.

Output: ../print/pdf/arant-<version>-<colour>.pdf  (earth, terracotta, black)
        ../print/jpg/arant-<version>-on-ivory.jpg
PDFs are RGB and open in Illustrator, Affinity, InDesign and Acrobat (save as AI/EPS from Illustrator if needed).
Run after build_exports.py:  python3 build_print.py   (needs Chrome/Chromium)
"""

import os
import shutil

import brand_tokens as tokens
import render

HERE = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.join(HERE, "..", "export")
PDF_DIR = os.path.join(HERE, "..", "print", "pdf")
JPG_DIR = os.path.join(HERE, "..", "print", "jpg")

VERSIONS = ("horizontal", "stacked", "one-line", "wordmark", "wordmark-short", "symbol")
PDF_COLOURS = ("earth", "terracotta", "black")


def svg(version, colour):
    return open(os.path.join(EXPORT, version, f"arant-{version}-{colour}.svg")).read()


def main():
    for d in (PDF_DIR, JPG_DIR):
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
    for v in VERSIONS:
        for c in PDF_COLOURS:
            title = f"ARANT DESIGN logo · {v.replace('-', ' ')} · {tokens.name(c) if c in tokens.palette() else c}"
            render.pdf(svg(v, c), os.path.join(PDF_DIR, f"arant-{v}-{c}.pdf"), title=title)
    ivory = tokens.color("ivory")
    render.rasterize(
        [
            {
                "svg": svg(v, "earth"),
                "out": os.path.join(JPG_DIR, f"arant-{v}-on-ivory.jpg"),
                "width": 1600 if v == "symbol" else 2400,
                "height": 1600 if v == "symbol" else None,
                "pad": 190 if v == "symbol" else 288,
                "bg": ivory,
                "fmt": "jpeg",
            }
            for v in VERSIONS
        ]
    )
    print(f"ok · {len(os.listdir(PDF_DIR))} PDFs, {len(os.listdir(JPG_DIR))} JPGs")


if __name__ == "__main__":
    main()
