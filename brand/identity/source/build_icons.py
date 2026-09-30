"""ARANT interface icons → ../icons/svg/*.svg, ../icons/sprite.svg and ../icons/icons-preview.png.

Line icons drawn from the shape language (brand/design-language/visual-language.md, "Icons"):
  - a 24-unit grid with a 2-unit margin; one stroke weight, 1.5 units, with round caps and joins to echo the
    mark's softened caps; no fills;
  - the vocabulary of the mark: straight strokes (the slabs), one circle (the pebble), the arch (an opening),
    softened rectangles, and diagonals at 45°, the square grid's own angle;
  - painted with currentColor, so an icon always takes the colour of the text beside it;
  - drawn at 24 px with a 1.5 stroke. Smaller sizes set a heavier stroke-width so the drawn line stays about 1.3-1.5 px,
    the weight of Jost Regular beside it: 2 at 16 px, 1.75 at 20 px (STROKE_AT). The sprite reads --icon-stroke.
The icons contain no brand colour; only the preview sheet is coloured, from the tokens.
Run: python3 build_icons.py   (needs Chrome/Chromium for the preview)
"""

import math
import os
import shutil

import brand_tokens as tokens
import render
from glyphs import fmt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "icons")

GRID = 24
STROKE = 1.5
STROKE_AT = {16: 2, 20: 1.75, 24: 1.5}  # stroke-width (in grid units) for each display size, in px


# ---------------------------------------------------------------- path primitives (24-unit grid, y down)
def line(*pts):
    """An open polyline through the points."""
    (x0, y0), rest = pts[0], pts[1:]
    return f"M{fmt(x0)} {fmt(y0)}" + "".join(f"L{fmt(x)} {fmt(y)}" for x, y in rest)


def circle(cx, cy, r):
    """A full circle as two arcs (a path, so every icon is a single <path>)."""
    return (
        f"M{fmt(cx - r)} {fmt(cy)}A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx + r)} {fmt(cy)}"
        f"A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx - r)} {fmt(cy)}Z"
    )


def dot(x, y):
    """A round dot one stroke wide: a zero-length segment drawn with a round cap."""
    return f"M{fmt(x)} {fmt(y)}h0.01"


def rounded_rect(x, y, w, h, r):
    """A softened rectangle, the slab: square geometry with eased corners."""
    return (
        f"M{fmt(x + r)} {fmt(y)}H{fmt(x + w - r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + w)} {fmt(y + r)}"
        f"V{fmt(y + h - r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + w - r)} {fmt(y + h)}"
        f"H{fmt(x + r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x)} {fmt(y + h - r)}"
        f"V{fmt(y + r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + r)} {fmt(y)}Z"
    )


def heart(cx=12.0, top=9.25, r=3.9, tip=19.75):
    """Two circles side by side (two pebbles), joined at the centre and closed by straight tangents to one point."""
    ccx, ccy = cx - r, top  # left circle; the right one is its mirror image
    phi = math.atan2(tip - ccy, cx - ccx)  # direction from the circle's centre to the tip
    a = phi + math.acos(r / math.hypot(cx - ccx, tip - ccy))  # the outer tangent point
    tx, ty = ccx + r * math.cos(a), ccy + r * math.sin(a)
    return (
        f"M{fmt(cx)} {fmt(tip)}L{fmt(tx)} {fmt(ty)}A{fmt(r)} {fmt(r)} 0 1 1 {fmt(cx)} {fmt(top)}"
        f"A{fmt(r)} {fmt(r)} 0 1 1 {fmt(2 * cx - tx)} {fmt(ty)}Z"
    )


# ---------------------------------------------------------------- the set
ICONS = {
    # navigation and utility
    "search": circle(10.5, 10.5, 6.25) + line((14.92, 14.92), (19.75, 19.75)),
    "bag": rounded_rect(4.75, 8.25, 14.5, 11.5, 1) + "M9 8.25V7A3 3 0 0 1 15 7V8.25",
    "account": circle(12, 7.25, 3.25) + "M5 20A7 7 0 0 1 19 20",
    "menu": line((4.25, 9), (19.75, 9)) + line((4.25, 15), (19.75, 15)),
    "close": line((6, 6), (18, 18)) + line((18, 6), (6, 18)),
    # direction
    "arrow-right": line((4.25, 12), (19.75, 12)) + line((14, 6.25), (19.75, 12), (14, 17.75)),
    "arrow-left": line((19.75, 12), (4.25, 12)) + line((10, 6.25), (4.25, 12), (10, 17.75)),
    "chevron-right": line((9.25, 5.75), (15.5, 12), (9.25, 18.25)),
    "chevron-left": line((14.75, 5.75), (8.5, 12), (14.75, 18.25)),
    "chevron-down": line((5.75, 9.25), (12, 15.5), (18.25, 9.25)),
    "chevron-up": line((5.75, 14.75), (12, 8.5), (18.25, 14.75)),
    # quantity, accordions and states
    "plus": line((12, 5), (12, 19)) + line((5, 12), (19, 12)),
    "minus": line((5, 12), (19, 12)),
    "check": line((5, 12.5), (9.5, 17), (19, 7.5)),
    "alert": circle(12, 12, 8.25) + line((12, 7.75), (12, 12.75)) + dot(12, 16.25),
    # gallery and wishlist
    "expand": (
        line((4.75, 9.25), (4.75, 4.75), (9.25, 4.75))
        + line((14.75, 4.75), (19.25, 4.75), (19.25, 9.25))
        + line((19.25, 14.75), (19.25, 19.25), (14.75, 19.25))
        + line((9.25, 19.25), (4.75, 19.25), (4.75, 14.75))
    ),
    "wishlist": heart(),
}

ATTRS = (
    f'viewBox="0 0 {GRID} {GRID}" fill="none" stroke="currentColor" stroke-width="{STROKE}" '
    'stroke-linecap="round" stroke-linejoin="round"'
)


def icon_svg(name, d):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{GRID}" height="{GRID}" {ATTRS} aria-hidden="true" '
        f'data-icon="{name}"><path d="{d}"/></svg>\n'
    )


def sprite():
    # stroke-width comes from --icon-stroke (inherited through <use>), so a page can set it per size
    attrs = ATTRS.replace(f'stroke-width="{STROKE}" ', f'style="stroke-width:var(--icon-stroke, {STROKE})" ')
    symbols = "".join(f'<symbol id="icon-{n}" {attrs}><path d="{d}"/></symbol>' for n, d in ICONS.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="display:none">{symbols}</svg>\n'


def preview_svg():
    """Every icon at 16, 20 and 24 px with its size's stroke, in the logo colour on Warm Ivory, one column each."""
    ink, ground, muted = (
        tokens.color("logo.default"),
        tokens.color("color.role.surface.ground"),
        tokens.color("color.role.text.muted"),
    )
    col, pad, rows = 56, 24, tuple(STROKE_AT)
    w = pad * 3 + col * len(ICONS)
    h = pad * 2 + 22 + sum(s + 20 for s in rows) - 20
    cells = []
    for i, (name, d) in enumerate(ICONS.items()):
        x0 = pad * 2 + i * col
        y = pad + 22
        for s in rows:
            k = s / GRID
            x = x0 + (col - s) / 2
            cells.append(
                f'<g transform="translate({fmt(x)} {fmt(y)}) scale({fmt(k)})" fill="none" stroke="{ink}" '
                f'stroke-width="{STROKE_AT[s]}" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></g>'
            )
            y += s + 20
        label = name.replace("chevron-", "chev-")
        cells.append(f'<text x="{fmt(x0 + col / 2)}" y="{pad + 8}" text-anchor="middle">{label}</text>')
    for j, s in enumerate(rows):
        y = pad + 22 + sum(r + 20 for r in rows[:j]) + s / 2 + 3
        cells.append(f'<text x="{pad + 12}" y="{fmt(y)}" text-anchor="end">{s}</text>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f'<rect width="{w}" height="{h}" fill="{ground}"/>'
        f'<g font-family="Helvetica Neue, Arial, sans-serif" font-size="9" fill="{muted}">{"".join(cells)}</g></svg>'
    )


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "svg"))
    for name, d in ICONS.items():
        with open(os.path.join(OUT, "svg", f"{name}.svg"), "w") as f:
            f.write(icon_svg(name, d))
    with open(os.path.join(OUT, "sprite.svg"), "w") as f:
        f.write(sprite())
    sheet = preview_svg()
    w, _ = render.svg_size(sheet)
    render.rasterize([{"svg": sheet, "out": os.path.join(OUT, "icons-preview.png"), "width": round(w * 2)}])
    print(f"ok · {len(ICONS)} icons in icons/svg/, sprite.svg, icons-preview.png")


if __name__ == "__main__":
    main()
