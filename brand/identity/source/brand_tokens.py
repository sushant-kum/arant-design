"""Read ARANT design tokens from packages/tokens/tokens.json — the only place brand colours are defined.

Every identity build step imports colours from here, so changing a value in tokens.json and running
`pnpm identity:build` updates the logo files, exports, print files, palette image and brand guide together.
"""

import json
import os
import re

TOKENS_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "packages", "tokens", "tokens.json")
)

with open(TOKENS_PATH) as f:
    _TOKENS = json.load(f)


def _node(path):
    node = _TOKENS
    for part in path.split("."):
        node = node[part]
    return node


def value(path):
    """Resolved $value of a token, following {alias} references (e.g. logo.default → color.earth)."""
    v = _node(path)["$value"]
    while isinstance(v, str) and re.fullmatch(r"\{[^}]+\}", v):
        v = _node(v[1:-1])["$value"]
    return v


def color(path):
    """A colour token as upper-case #RRGGBB. Accepts 'earth' or a full path like 'logo.default'."""
    return value(path if "." in path else f"color.{path}").upper()


def name(key):
    """Display name of a palette colour, e.g. 'earth' → 'Earth Brown'."""
    return _node(f"color.{key}").get("$extensions", {}).get("com.arantdesign", {}).get("name", key.title())


def role(key):
    return _node(f"color.{key}").get("$description", "")


def palette():
    """Palette colour keys in file order."""
    return [k for k in _TOKENS["color"] if not k.startswith("$")]


def fonts(key):
    return value(f"font.family.{key}")


# ---------------------------------------------------------------- colour maths (derived values, never stored)
def rgb(hex_):
    return tuple(int(hex_[i : i + 2], 16) for i in (1, 3, 5))


def hex_(r, g, b):
    return f"#{round(r):02X}{round(g):02X}{round(b):02X}"


def mix(a, b, t):
    """Mix colour a toward b by t (0..1). a and b are token keys or #hex."""
    a = a if a.startswith("#") else color(a)
    b = b if b.startswith("#") else color(b)
    return hex_(*(x + (y - x) * t for x, y in zip(rgb(a), rgb(b), strict=True)))


def cmyk(hex_value):
    """Straight RGB→CMYK conversion (a starting point for the printer, not a press profile)."""
    r, g, b = (c / 255 for c in rgb(hex_value))
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


def contrast(a, b):
    """WCAG contrast ratio between two colours."""

    def lum(h):
        c = [v / 255 for v in rgb(h)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def slug(hex_value):
    return hex_value.lstrip("#").lower()
