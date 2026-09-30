"""Geometry primitives for the ARANT logo build: closed subpaths, polygons and rounded polygons (y down).

Used by build_logo.py. A subpath is a list of absolute-coordinate commands; tf() scales and moves it.
"""

import math


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class Sub:
    """One closed subpath: commands ('M',x,y) ('L',x,y) ('A',rx,ry,rot,large,sweep,x,y) ('Q',cx,cy,x,y) ('C',...)"""

    def __init__(self, cmds):
        self.cmds = cmds

    def tf(self, s, dx, dy):
        out = []
        for c in self.cmds:
            k = c[0]
            if k in "ML":
                out.append((k, c[1] * s + dx, c[2] * s + dy))
            elif k == "A":
                out.append(("A", c[1] * s, c[2] * s, c[3], c[4], c[5], c[6] * s + dx, c[7] * s + dy))
            elif k == "Q":
                out.append(("Q", c[1] * s + dx, c[2] * s + dy, c[3] * s + dx, c[4] * s + dy))
            elif k == "C":
                out.append(("C",) + tuple(v * s + (dx if i % 2 == 0 else dy) for i, v in enumerate(c[1:])))
        return Sub(out)

    def d(self):
        parts = []
        for c in self.cmds:
            k = c[0]
            if k in "ML":
                parts.append(f"{k}{fmt(c[1])} {fmt(c[2])}")
            elif k == "A":
                parts.append(f"A{fmt(c[1])} {fmt(c[2])} {c[3]} {c[4]} {c[5]} {fmt(c[6])} {fmt(c[7])}")
            else:
                parts.append(k + " ".join(fmt(v) for v in c[1:]))
        return "".join(parts) + "Z"


def poly(pts):
    """Polygon, forced clockwise (in y-down screen space) so all positives share a winding."""
    a = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))
    if a < 0:
        pts = pts[::-1]
    return Sub([("M",) + tuple(pts[0])] + [("L",) + tuple(p) for p in pts[1:]])


def rect(x, y, w, h):
    return poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])


def rounded_poly(pts, radii, ccw=False):
    """Polygon with circular-arc rounded corners (radius per vertex). Clockwise unless ccw (for holes)."""
    n = len(pts)
    a = sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))
    if (a < 0) != ccw:
        pts, radii = pts[::-1], radii[::-1]
    cmds = []
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        v1 = (p0[0] - p1[0], p0[1] - p1[1])
        v2 = (p2[0] - p1[0], p2[1] - p1[1])
        l1, l2 = math.hypot(*v1), math.hypot(*v2)
        u1, u2 = (v1[0] / l1, v1[1] / l1), (v2[0] / l2, v2[1] / l2)
        ang = math.acos(max(-1, min(1, u1[0] * u2[0] + u1[1] * u2[1])))
        r = radii[i]
        t = r / math.tan(ang / 2) if r else 0
        a_pt = (p1[0] + u1[0] * t, p1[1] + u1[1] * t)
        b_pt = (p1[0] + u2[0] * t, p1[1] + u2[1] * t)
        cross = v1[0] * v2[1] - v1[1] * v2[0]
        sweep = 1 if cross < 0 else 0
        cmds.append(("M" if i == 0 else "L",) + a_pt)
        if r:
            cmds.append(("A", r, r, 0, 0, sweep, b_pt[0], b_pt[1]))
    return Sub(cmds)
