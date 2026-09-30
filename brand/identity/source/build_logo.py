"""ARANT DESIGN — final logo system v1.1 (Balance direction). v1.0 geometry lives in the git history.

Geometry is defined once in design units and exported as clean, font-free SVG masters:
  symbol (regular / reversed-thinned / small-size cut), ARANT wordmark, DESIGN descriptor, and lockups.
Run: python3 build_logo.py  → ../logo/svg/*.svg
"""

import math
import os

import brand_tokens as tokens
from glyphs import Sub, fmt, poly, rect, rounded_poly

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logo", "svg")
os.makedirs(OUT, exist_ok=True)

# colours come from packages/tokens/tokens.json — never hard-code them here
LOGO = tokens.color("logo.default")
LOGO_REVERSED = tokens.color("logo.reversed")


def circle(cx, cy, r):
    return Sub([("M", cx - r, cy), ("A", r, r, 0, 1, 0, cx + r, cy), ("A", r, r, 0, 1, 0, cx - r, cy)])


def place(subs, s, dx, dy):
    return [x.tf(s, dx, dy) for x in subs]


# ------------------------------------------------------------------ symbol (100-unit design grid)
def balance(
    foot=14.0,
    seam=2.5,
    tip=6.0,
    pebble_r=6.2,
    pebble_gap=5.0,
    r_foot=3,
    r_cap=(3, 3.5),
    top=13.0,
    base=87.0,
    foot_out=17.0,
):
    """Two equal slabs lean together; split = 2*seam; the pebble is lifted until its clearance to each slab
    (perpendicular to the slab edge) equals pebble_gap. All values in the 100-unit grid."""
    subs = []
    for side in (-1, 1):
        fo = 50 + side * (50 - foot_out)
        fi = fo - side * foot
        xs = 50 + side * seam
        xt = xs + side * tip
        slope = (xt - fo) / (top - base)
        y_in = base + (xs - fi) / slope
        subs.append(
            rounded_poly(
                [(fo, base), (fi, base), (xs, y_in), (xs, top), (xt, top)], [r_foot, r_foot, 0, r_cap[0], r_cap[1]]
            )
        )
    # pebble height from the left slab's inner edge
    fo, fi, xs = foot_out, foot_out + foot, 50 - seam
    slope = ((xs - tip) - fo) / (top - base)
    h = (pebble_r + pebble_gap) * math.sqrt(1 + slope**2)
    py = base + (50 - h - fi) / slope
    subs.append(circle(50, py, pebble_r))
    return subs


SYMBOL = dict()  # regular: Split 5, rounded tops, pebble gap 5 (as approved)
# v1.1: every A is the approved A. No thinned reversed cut and no small-size cut.


# ------------------------------------------------------------------ ARANT wordmark (cap height 100)
H = 100
K_A = H / 74  # symbol ink is 74 units tall (y 13..87) → scale to the cap height
# stroke of the symbol's slabs, measured square to the slab: foot 14 wide, slab leans 24.5 over 74
W_STEM = 14 * K_A * math.cos(math.atan2(24.5, 74))  # ≈ 17.95
R_CORNER = 3 * K_A  # the symbol's foot radius at text size ≈ 4.05


def rrect(x, y, w, h, r=R_CORNER):
    return rounded_poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], [r] * 4)


def glyph_A():
    """Exactly the symbol, scaled so its ink spans the cap height."""
    return place(balance(**SYMBOL), K_A, -17 * K_A, -13 * K_A), 66 * K_A


def glyph_R(width=72, bowl_h=58):
    w = W_STEM
    ro = bowl_h / 2
    cx = width - ro - 3
    x0 = w / 2  # bowl starts inside the stem so the stem's rounded top-left corner stays visible
    bowl = Sub(
        [
            ("M", x0, 0),
            ("L", cx, 0),
            ("A", ro, ro, 0, 0, 1, cx, bowl_h),
            ("L", x0, bowl_h),
            ("L", x0, bowl_h - w),
            ("L", cx, bowl_h - w),
            ("A", ro - w, ro - w, 0, 0, 0, cx, w),
            ("L", x0, w),
        ]
    )
    stem = rrect(0, 0, w, H)
    lx = cx - w * 0.15
    a = math.atan2(H - bowl_h, width - lx)
    d = w / math.sin(a)
    leg = rounded_poly(
        [(lx - d * 0.5, bowl_h - w * 0.5), (lx + d * 0.5, bowl_h - w * 0.5), (width, H), (width - d, H)],
        [0, 0, R_CORNER, R_CORNER],
    )
    return [stem, bowl, leg], width


def glyph_N(width=None):
    sw = W_STEM
    d = W_STEM / math.sin(math.radians(60))
    width = width or (d + H / math.tan(math.radians(60)))  # diagonal at exactly 60°
    # the diagonal's own corners are rounded too, so it never re-sharpens the stems' rounded corners
    diag = rounded_poly([(0, 0), (d, 0), (width, H), (width - d, H)], [R_CORNER] * 4)
    return [rrect(0, 0, sw, H), rrect(width - sw, 0, sw, H), diag], width


def glyph_T(width=76):
    return [rrect(0, 0, width, W_STEM), rrect((width - W_STEM) / 2, 0, W_STEM, H)], width


def wordmark(**_):
    A = glyph_A()
    R = glyph_R()
    N = glyph_N()
    T = glyph_T()
    seq = [A, R, A, N, T]
    gaps = [12, 11, 14, 15]  # optical: the A's open feet need less space than R/N stems
    x, subs = 0, []
    for i, (g, adv) in enumerate(seq):
        subs += place(g, 1, x, 0)
        x += adv + (gaps[i] if i < len(gaps) else 0)
    return subs, x


# ------------------------------------------------------------------ DESIGN descriptor (cap height 100)
T_D = 16.0  # a touch heavier to sit with the fatter ARANT


def band(cx, cy, rx, ry, t, a0, a1, ccw):
    """Elliptical band (centre-line radii rx, ry; thickness t) from angle a0 to a1 (degrees, maths convention)."""

    def p(rxx, ryy, a):
        return (cx + rxx * math.cos(math.radians(a)), cy - ryy * math.sin(math.radians(a)))

    span = abs(a1 - a0)
    large = 1 if span > 180 else 0
    so, si = (0, 1) if ccw else (1, 0)
    o0, o1 = p(rx + t / 2, ry + t / 2, a0), p(rx + t / 2, ry + t / 2, a1)
    i1, i0 = p(rx - t / 2, ry - t / 2, a1), p(rx - t / 2, ry - t / 2, a0)
    return Sub(
        [
            ("M",) + o0,
            ("A", rx + t / 2, ry + t / 2, 0, large, so) + o1,
            ("L",) + i1,
            ("A", rx - t / 2, ry - t / 2, 0, large, si) + i0,
        ]
    )


def d_D():
    t, w = T_D, 78
    cxb = w - 50
    bowl = Sub(
        [
            ("M", 0, 0),
            ("L", cxb, 0),
            ("A", 50, 50, 0, 0, 1, cxb, 100),
            ("L", 0, 100),
            ("L", 0, 100 - t),
            ("L", cxb, 100 - t),
            ("A", 50 - t, 50 - t, 0, 0, 0, cxb, t),
            ("L", 0, t),
        ]
    )
    return [rect(0, 0, t, 100), bowl], w


def d_E():
    t = T_D
    return [
        rect(0, 0, t, 100),
        rect(0, 0, 60, t * 0.92),
        rect(0, 50 - t * 0.46, 54, t * 0.92),
        rect(0, 100 - t * 0.92, 60, t * 0.92),
    ], 60


def d_S():
    t = T_D
    ry = (100 - t) / 4
    rx = 25
    cx = rx + t / 2
    c1, c2 = ry + t / 2, 3 * ry + t / 2
    return [band(cx, c1, rx, ry, t, 32, 270, ccw=True), band(cx, c2, rx, ry, t, 90, -148, ccw=False)], 2 * rx + t


def d_I():
    return [rect(0, 0, T_D, 100)], T_D


def d_G():
    t = T_D
    r = 50 - t / 2
    cx = 50
    return [band(cx, 50, r, r, t, 42, 360, ccw=True), rect(54, 50 - t * 0.02, 100 - 54, t * 0.92)], 100


def d_N():
    t = T_D
    w = 76
    alpha = math.atan2(100, w - t)
    d = t / math.sin(alpha)
    return [rect(0, 0, t, 100), rect(w - t, 0, t, 100), poly([(0, 0), (d, 0), (w, 100), (w - d, 100)])], w


def descriptor(total_width):
    """DESIGN spread to exactly total_width (in its own units) with even letter gaps."""
    gl = [d_D(), d_E(), d_S(), d_I(), d_G(), d_N()]
    ink = sum(a for _, a in gl)
    gap = (total_width - ink) / (len(gl) - 1)
    x, subs = 0, []
    for g, a in gl:
        subs += place(g, 1, x, 0)
        x += a + gap
    return subs


# ------------------------------------------------------------------ files
def write_svg(name, w, h, subs, title, fill=LOGO, bg=None, rule=None):
    body = f'<rect width="{fmt(w)}" height="{fmt(h)}" fill="{bg}"/>' if bg else ""
    # one path per shape inside a filled group: overlaps always union, whatever each shape's winding
    body += f'<g fill="{fill}">' + "".join(f'<path d="{s.d()}"/>' for s in subs) + "</g>"
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" width="{fmt(w)}" height="{fmt(h)}" '
        f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n'
    )
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


def symbol_subs(params, canvas=256, pad=0.0):
    return place(balance(**params), canvas / 100, 0, 0)


def lockups():
    wm, wm_w = wordmark()
    DESC_RATIO = 0.27  # DESIGN cap height relative to ARANT (v1.0: 0.21)
    DESC_GAP = 0.34  # gap ARANT→DESIGN, in ARANT cap heights
    block_h = H * (1 + DESC_GAP + DESC_RATIO)
    desc = descriptor(wm_w / DESC_RATIO)

    def word_block(x, y, s):
        """ARANT over DESIGN, scale s, top-left at (x,y). Returns subs and size."""
        subs = place(wm, s, x, y) + place(desc, s * DESC_RATIO, x, y + s * H * (1 + DESC_GAP))
        return subs, wm_w * s, block_h * s

    sym = balance()
    # symbol ink box in the 100 grid: x 17..83, y 13..87 (74 tall)
    SYM_TOP, SYM_H, SYM_L, SYM_W = 13, 74, 17, 66

    # 1 · Wordmark (primary typographic logo): ARANT / DESIGN
    s = 1.6
    pad = 24
    subs, bw, bh = word_block(pad, pad, s)
    write_svg("arant-wordmark.svg", bw + 2 * pad, bh + 2 * pad, subs, "ARANT DESIGN wordmark")

    # 2 · Horizontal lockup: symbol + ARANT/DESIGN; symbol height = ARANT cap height × 1.62 (spans the block)
    s = 1.0
    cap = H * s
    sym_h = block_h * s
    k = sym_h / SYM_H
    gap = cap * 0.95  # wide enough that the symbol never reads as a first letter
    pad = 24
    subs = place(sym, k, pad - SYM_L * k, pad - SYM_TOP * k)
    x0 = pad + SYM_W * k + gap
    ws, bw, bh = word_block(x0, pad, s)
    write_svg("arant-horizontal.svg", x0 + bw + pad, bh + 2 * pad, subs + ws, "ARANT DESIGN logo, horizontal")

    # 3 · Stacked lockup: symbol centred above ARANT/DESIGN
    s = 1.0
    ws_w = wm_w * s
    sym_h = H * s * 1.55
    k = sym_h / SYM_H
    pad = 24
    W = ws_w + 2 * pad
    subs = place(sym, k, W / 2 - 50 * k, pad - SYM_TOP * k)
    ws, bw, bh = word_block(pad, pad + sym_h + H * s * 0.62, s)
    write_svg("arant-stacked.svg", W, pad + sym_h + H * s * 0.62 + bh + pad, subs + ws, "ARANT DESIGN logo, stacked")

    # 4 · One-line: symbol · ARANT · DESIGN (website header, packaging bands)
    s = 1.0
    k = (H * s * 1.28) / SYM_H
    pad = 20
    sy = pad
    subs = place(sym, k, pad - SYM_L * k, sy - SYM_TOP * k)
    x = pad + SYM_W * k + H * 0.85
    cap_top = sy + (SYM_H * k - H * s) / 2 + 4
    subs += place(wm, s, x, cap_top)
    x += wm_w * s + H * 0.42
    dr = 0.36
    desc_line = descriptor(wm_w * 0.62 / dr)
    subs += place(desc_line, s * dr, x, cap_top + H * s * (1 - dr) / 2)
    Wd = x + wm_w * 0.62 * s + pad
    write_svg("arant-one-line.svg", Wd, SYM_H * k + 2 * pad, subs, "ARANT DESIGN logo, one line")

    # 5 · ARANT only (for product moulds and small tags, where DESIGN would fill in)
    pad = 20
    write_svg("arant-wordmark-short.svg", wm_w + 2 * pad, H + 2 * pad, place(wm, 1, pad, pad), "ARANT wordmark")


def symbols():
    write_svg("arant-symbol.svg", 256, 256, place(balance(**SYMBOL), 2.56, 0, 0), "ARANT symbol")
    write_svg(
        "arant-symbol-reversed.svg",
        256,
        256,
        place(balance(**SYMBOL), 2.56, 0, 0),
        "ARANT symbol, ivory for dark grounds",
        fill=LOGO_REVERSED,
    )


if __name__ == "__main__":
    symbols()
    lockups()
    print("ok")
