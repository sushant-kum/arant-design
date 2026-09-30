"""Instagram tiles, carousel frames and story / reel covers → ../../social/templates/ and ../../social/posts/.

Layouts follow brand/design-language/social.md:
  tile   a designed graphic: Ivory or Sand ground, an uppercase Jost label, one Newsreader Light line, at most one
         Terracotta or Olive element, the symbol small and optional (bottom right, with its clear space)
  photo  a photograph (or a marked placeholder plate while none exists), optionally with a short Newsreader title
  info   the carousel information frame: name, then size, material and price in Jost on Ivory
  close  the carousel close: one mark (the stacked lockup by default) and where to find ARANT (the site and the
         Instagram handle), no hard sell
Formats: feed 1080 × 1350 (4:5; key content inside the centre 1:1 area for grid previews) and story / reel cover
1080 × 1920 (9:16; text clear of the top and bottom 250 px, and inside the centre 1:1 for reel covers).

Each frame is a self-contained HTML page with Jost and Newsreader embedded from fonts/ (run fetch_fonts.py once if
they are missing), rendered by headless Chrome at device scale 1, so the type is the real type. Colours, spacing and
label tracking come from packages/tokens/tokens.json; web values are multiplied by K, because Instagram shows a
1080 px frame at about 360 pt wide on a phone.

templates/ is the reusable set with placeholder copy, each also with a -guides.png showing the safe areas.
posts/ is rendered from ../../social/posts.json: add an entry there to make a new post.
Run: python3 build_social.py   (needs Chrome/Chromium)
"""

import base64
import html
import json
import os
import re
import shutil
from concurrent.futures import ThreadPoolExecutor

import brand_tokens as tokens
import render

HERE = os.path.dirname(os.path.abspath(__file__))
SOCIAL = os.path.normpath(os.path.join(HERE, "..", "..", "social"))
MASTERS = os.path.join(HERE, "..", "logo", "svg")
FONTS = os.path.join(HERE, "fonts")

FORMATS = {"feed": (1080, 1350), "story": (1080, 1920)}
STORY_SAFE = 250  # social.md: keep text out of the top and bottom ~250 px of a story or reel (app interface)
K = 3  # tile px per web px: a 1080 px frame is shown about 360 pt wide


def dim(path):
    """A dimension token (e.g. space.7 = 48px) at tile scale."""
    return float(re.match(r"[\d.]+", tokens.value(path)).group()) * K


MARGIN = dim("space.7")  # 144 px, above social.md's minimum of a tenth of the width (108 px)
GAP = dim("space.3")  # 36 px, label to accent and label to headline
ROW = dim("space.5")  # 72 px, between information rows
HAIR = float(re.match(r"[\d.]+", tokens.value("border.subtle")["width"]).group()) * K  # border.subtle
TRACK = tokens.value("letterSpacing.label")

COLOUR = {
    "ivory": tokens.color("color.role.surface.ground"),
    "sand": tokens.color("color.role.surface.alt"),
    "text": tokens.color("color.role.text.primary"),
    "head": tokens.color("color.role.text.secondary"),
    "muted": tokens.color("color.role.text.muted"),  # on Ivory only
    "line": tokens.color("color.role.line.subtle"),
    "inverse": tokens.color("color.role.surface.inverse"),
    "on_inverse": tokens.color("color.role.text.inverse"),
    "terracotta": tokens.color("color.role.accent"),
    "olive": tokens.color("olive"),
    "logo": tokens.color("logo.default"),
    "logo_reversed": tokens.color("logo.reversed"),
}


def stack(key):
    """A token font stack as CSS: family names quoted, generic families bare."""
    generic = {"serif", "sans-serif"}
    return ", ".join(f if f in generic else f'"{f}"' for f in tokens.fonts(key))


SANS, SERIF = stack("sans"), stack("serif")
W_LIGHT, W_REGULAR, W_MEDIUM = (tokens.value(f"font.weight.{w}") for w in ("light", "regular", "medium"))


# ---------------------------------------------------------------- embedded assets
def font_faces():
    faces = []
    for family, path, weights in (
        ("Jost", "jost/Jost-Variable.ttf", "100 900"),
        ("Newsreader", "newsreader/Newsreader-Variable.ttf", "200 800"),
    ):
        full = os.path.join(FONTS, path)
        if not os.path.exists(full):
            raise SystemExit(f"{full} is missing: run `pnpm identity:fonts` (needs network access once)")
        with open(full, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        faces.append(
            f'@font-face{{font-family:"{family}";src:url(data:font/ttf;base64,{data}) format("truetype");'
            f"font-weight:{weights};font-style:normal;font-display:block}}"
        )
    return "".join(faces)


FONT_CSS = font_faces()


def symbol_svg(cls="symbol"):
    """The symbol master, unchanged, painted with currentColor."""
    with open(os.path.join(MASTERS, "arant-symbol.svg")) as f:
        s = f.read()
    s = re.sub(r"<title[^>]*>.*?</title>", "", s)
    s = re.sub(r' width="[\d.]+" height="[\d.]+"', "", s)
    s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="currentColor"', s)
    return s.replace('role="img" aria-labelledby="title"', f'aria-hidden="true" class="{cls}"').strip()


SYMBOL = symbol_svg()

# ---------------------------------------------------------------- the close frame's mark
TAGLINE = "Objects for Considered Spaces."  # the fixed brand line: this casing and the full stop, always
HANDLE = "@arantdesign"
CAP_UNITS = 100  # ARANT's cap height in the lockup masters' own units (build_logo.py draws ARANT 100 units tall)
LOGOS = {  # logo field → master, artwork width in the frame, and its screen minimum (brand/identity/README.md)
    "stacked": {"file": "arant-stacked.svg", "width": 140 * K, "min_screen": 120},
    "horizontal": {"file": "arant-horizontal.svg", "width": 200 * K, "min_screen": 180},
    "one-line": {"file": "arant-one-line.svg", "width": 200 * K, "min_screen": 190},
    "symbol": {"file": "arant-symbol.svg", "width": 36 * K, "min_screen": 24},
}


def artwork_box(svg):
    """(viewBox, artwork bounds) of a master, from its path end points, all in the master's own units. The masters
    are drawn with absolute M, L and A commands only; the README measures minimum sizes on the artwork, not the file."""
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    xs, ys = [], []
    for d in re.findall(r' d="([^"]+)"', svg):
        toks, i, cmd = re.findall(r"[A-Za-z]|-?\d*\.?\d+", d), 0, None
        while i < len(toks):
            if toks[i].isalpha():
                cmd, i = toks[i], i + 1
                continue
            n = {"M": 2, "L": 2, "A": 7}[cmd]
            xs.append(float(toks[i + n - 2]))
            ys.append(float(toks[i + n - 1]))
            i += n
    return vb, (min(xs), min(ys), max(xs), max(ys))


def logo_mark(kind):
    """An unchanged logo master in the logo colour, sized by its artwork, with the gap its clear space needs below
    the artwork (in frame px). Clear space: half the ARANT cap height for a lockup, a quarter of the height for the
    symbol alone (brand/identity/README.md)."""
    if kind not in LOGOS:
        raise SystemExit(f"close: logo is one of {', '.join(LOGOS)}, not {kind!r}")
    spec = LOGOS[kind]
    if spec["width"] / K < spec["min_screen"]:
        raise SystemExit(f"close: the {kind} logo would show below its {spec['min_screen']} px screen minimum")
    with open(os.path.join(MASTERS, spec["file"])) as f:
        s = f.read()
    (_, _, vw, vh), (x0, y0, x1, y1) = artwork_box(s)
    scale = spec["width"] / (x1 - x0)  # frame px per master unit
    clear = (y1 - y0) / 4 if kind == "symbol" else CAP_UNITS / 2
    s = re.sub(r"<title[^>]*>.*?</title>", "", s)
    s = re.sub(r' width="[\d.]+" height="[\d.]+"', f' width="{vw * scale:.2f}" height="{vh * scale:.2f}"', s)
    s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="currentColor"', s)
    s = s.replace('role="img" aria-labelledby="title"', 'aria-hidden="true"').strip()
    # the file's own margin below the artwork already counts towards the clear space
    return s, clear * scale, (vh - y1) * scale


def photo_uri(rel):
    """A photograph from brand/social/ as a data URI, or None while it doesn't exist."""
    path = os.path.join(SOCIAL, rel) if rel else ""
    if not rel or not os.path.exists(path):
        return None
    mime = {".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".webp": "webp"}[os.path.splitext(path)[1].lower()]
    with open(path, "rb") as f:
        return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()


# ---------------------------------------------------------------- page
def page(w, h, ground, body, sample=False, guides=None):
    marker = '<div class="sample">Sample · example content · not for posting</div>' if sample else ""
    return f"""<!doctype html><meta charset="utf-8"><style>{FONT_CSS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{w}px;height:{h}px;overflow:hidden}}
body{{background:{COLOUR[ground]};color:{COLOUR["head"]};font-family:{SANS};position:relative;
  -webkit-font-smoothing:antialiased}}
.label{{font:{W_MEDIUM} {12 * K}px/1.3 {SANS};letter-spacing:{TRACK};text-transform:uppercase}}
.headline{{font-family:{SERIF};font-weight:{W_LIGHT};font-size:{32 * K}px;line-height:1.08;text-wrap:balance}}
.body{{font:{W_REGULAR} {16 * K}px/1.5 {SANS};color:{COLOUR["text"]}}}
.symbol{{display:block;width:{32 * K}px;height:{32 * K}px;color:{COLOUR["logo"]}}}
.accent{{display:block;width:{32 * K}px;height:{2 * K}px}}
.sample{{position:absolute;left:0;right:0;top:0;height:{19 * K}px;z-index:9;
  background:{COLOUR["inverse"]};color:{COLOUR["on_inverse"]};display:flex;align-items:center;justify-content:center;
  font:{W_MEDIUM} {8 * K}px/1 {SANS};letter-spacing:{TRACK};text-transform:uppercase}}
.guide{{position:absolute;border:{K}px dashed {COLOUR["terracotta"]};z-index:8}}
.guide-band{{position:absolute;left:0;right:0;background:{COLOUR["terracotta"]}2E;z-index:8}}
.guide span,.guide-band span{{position:absolute;left:{4 * K}px;bottom:{3 * K}px;color:{COLOUR["head"]};
  font:{W_MEDIUM} {7 * K}px/1 {SANS};letter-spacing:{TRACK};text-transform:uppercase}}
.guide span.r{{left:auto;right:{4 * K}px;bottom:auto;top:{3 * K}px}}
.guide span.rb{{left:auto;right:{4 * K}px}}
</style><body>{body}{marker}{guides or ""}</body>"""


def content_box(fmt):
    """Top and bottom limits for text: the margin, plus the app interface bands in a story."""
    w, h = FORMATS[fmt]
    top = MARGIN + (STORY_SAFE if fmt == "story" else 0)
    return top, h - top


def square(fmt):
    """The centre 1:1 area: the grid preview crop of a feed post, the safest crop of a reel cover."""
    w, h = FORMATS[fmt]
    return (h - w) / 2, (h + w) / 2


def guides(fmt):
    w, h = FORMATS[fmt]
    top, bottom = content_box(fmt)
    s0, s1 = square(fmt)
    g = [
        f'<div class="guide" style="left:{MARGIN}px;right:{MARGIN}px;top:{top}px;bottom:{h - bottom}px">'
        "<span>Text area</span></div>",
        f'<div class="guide" style="left:0;right:0;top:{s0}px;bottom:{h - s1}px;border-style:dotted">'
        '<span class="r">Centre 1:1</span></div>',
    ]
    if fmt == "story":
        f0, f1 = (h - w * 5 / 4) / 2, (h + w * 5 / 4) / 2
        g.append(
            f'<div class="guide" style="left:0;right:0;top:{f0}px;bottom:{h - f1}px;border-style:dotted">'
            '<span class="rb">Centre 4:5</span></div>'
        )
        g += [
            f'<div class="guide-band" style="top:0;height:{STORY_SAFE}px"><span>App interface: no text</span></div>',
            f'<div class="guide-band" style="bottom:0;height:{STORY_SAFE}px"><span>App interface: no text</span></div>',
        ]
    return "".join(g)


# ---------------------------------------------------------------- layouts
def tile(fmt, spec):
    """A designed graphic. ground: ivory | sand. accent: terracotta | olive | none (one element, never text)."""
    ground = spec.get("ground", "ivory")
    if ground not in ("ivory", "sand"):
        raise SystemExit(f"{spec.get('slug')}: a tile's ground is ivory or sand")
    top, bottom = content_box(fmt)
    w, h = FORMATS[fmt]
    accent = spec.get("accent")
    rule = f'<i class="accent" style="background:{COLOUR[accent]};margin-bottom:{GAP}px"></i>' if accent else ""
    symbol = (
        f'<div style="position:absolute;right:{MARGIN}px;top:{bottom - 32 * K}px">{SYMBOL}</div>'
        if spec.get("symbol")
        else ""
    )
    body = (
        f'<div style="position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{top}px;bottom:{h - bottom}px;'
        f'display:flex;flex-direction:column">{rule}<p class="label">{html.escape(spec.get("label", ""))}</p>'
        f'<div style="flex:1;display:flex;align-items:center;padding-bottom:{32 * K}px">'
        f'<h1 class="headline">{html.escape(spec["headline"])}</h1></div></div>{symbol}'
    )
    return ground, body


def photo(fmt, spec):
    """A photograph filling the frame, or a marked placeholder plate; an optional title sits inside the centre
    1:1 area, in Earth (ink: dark) or Ivory (ink: light) on a calm part of the photograph."""
    w, h = FORMATS[fmt]
    uri = photo_uri(spec.get("photo"))
    if uri:
        art = f'<img src="{uri}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
    else:
        top, _ = content_box(fmt)
        inset = MARGIN / 2
        art = (
            f'<div style="position:absolute;inset:{inset}px;border:{K}px dashed {COLOUR["head"]}"></div>'
            f'<div style="position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{top}px;display:grid;gap:{GAP / 2}px">'
            f'<p class="label">Photograph · placeholder</p>'
            f'<p class="body" style="color:{COLOUR["head"]}">{html.escape(spec.get("shot", "Photograph"))}, '
            f"{'4:5' if fmt == 'feed' else '9:16'}</p>"
            f'<p class="label" style="font-weight:{W_REGULAR};text-transform:none;letter-spacing:0">'
            f"{html.escape(spec.get('photo') or 'photos/…')}</p></div>"
        )
    title = ""
    if spec.get("title"):
        ink = COLOUR["logo_reversed"] if spec.get("ink") == "light" else COLOUR["head"]
        _, s1 = square(fmt)
        title = (
            f'<h1 class="headline" style="position:absolute;left:{MARGIN}px;right:{MARGIN}px;'
            f'bottom:{h - s1 + dim("space.6")}px;color:{ink}">{html.escape(spec["title"])}</h1>'
        )
    return ("sand" if not uri else "ivory"), art + title


def info(fmt, spec):
    """The information frame: the product name in Newsreader, then label and value rows in Jost, on Ivory."""
    top, bottom = content_box(fmt)
    w, h = FORMATS[fmt]
    rows = "".join(
        f'<div style="border-top:{HAIR}px solid {COLOUR["line"]};padding-top:{GAP / 2}px;display:grid;gap:{K * 2}px">'
        f'<p class="label" style="color:{COLOUR["muted"]}">{html.escape(k)}</p>'
        f'<p class="body">{html.escape(v)}</p></div>'
        for k, v in spec["details"]
    )
    body = (
        f'<div style="position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{top}px;bottom:{h - bottom}px;'
        f'display:flex;flex-direction:column;justify-content:center;gap:{ROW}px">'
        f'<h1 class="headline" style="font-size:{32 * K}px">{html.escape(spec["name"])}</h1>'
        f'<div style="display:grid;gap:{GAP}px">{rows}</div></div>'
    )
    return "ivory", body


def close(fmt, spec):
    """The carousel close, centred inside the text area: one mark (logo: stacked | horizontal | one-line | symbol;
    the stacked lockup by default, never with a second mark), then the site line with the Instagram handle below it
    (handle: true) in Jost. tagline: true (off by default) adds the tagline in Newsreader Light between them. All in
    the role text colours; no accent."""
    top, bottom = content_box(fmt)
    w, h = FORMATS[fmt]
    svg, clear, margin = logo_mark(spec.get("logo", "stacked"))
    tagline = spec.get("tagline", False)
    # logo to the next line: at least the clear space below the artwork; a row before a tagline, and a wider
    # space.6 step before the contact lines when they follow the logo directly
    after_logo = max(ROW if tagline else dim("space.6"), clear) - margin
    parts = [f'<div style="color:{COLOUR["logo"]};margin-bottom:{after_logo:.2f}px;line-height:0">{svg}</div>']
    if tagline:
        parts.append(f'<p class="tagline" style="margin-bottom:{ROW}px">{html.escape(TAGLINE)}</p>')
    contact = [spec.get("line", "arantdesign.com")] + ([HANDLE] if spec.get("handle", True) else [])
    parts.append("".join(f'<p class="body" style="color:{COLOUR["head"]}">{html.escape(c)}</p>' for c in contact))
    body = (
        f'<div style="position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{top}px;bottom:{h - bottom}px;'
        f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">'
        f"{''.join(parts)}</div>"
        f"<style>.tagline{{font:{W_LIGHT} {21 * K}px/1.3 {SERIF};color:{COLOUR['head']};text-wrap:balance}}</style>"
    )
    return "ivory", body


LAYOUTS = {"tile": tile, "photo": photo, "info": info, "close": close}


def frame_page(fmt, spec, sample=False, with_guides=False):
    w, h = FORMATS[fmt]
    ground, body = LAYOUTS[spec["layout"]](fmt, spec)
    return page(w, h, ground, body, sample=sample, guides=guides(fmt) if with_guides else None), w, h


# ---------------------------------------------------------------- the reusable set (placeholder copy)
TEMPLATES = {
    "feed-tile-ivory": (
        "feed",
        {
            "layout": "tile",
            "ground": "ivory",
            "label": "Label · two to four words",
            "headline": "One Newsreader line, two at most",
            "accent": "terracotta",
            "symbol": True,
        },
    ),
    "feed-tile-sand": (
        "feed",
        {"layout": "tile", "ground": "sand", "label": "Label", "headline": "One Newsreader line", "symbol": True},
    ),
    "feed-photo-title": (
        "feed",
        {"layout": "photo", "shot": "Hero", "photo": "photos/<object>/hero.jpg", "title": "A short title"},
    ),
    "feed-photo": ("feed", {"layout": "photo", "shot": "Photograph, no type", "photo": "photos/<object>/<shot>.jpg"}),
    "carousel-information": (
        "feed",
        {
            "layout": "info",
            "name": "Object Name",
            "details": [["Colour", "Colour"], ["Size", "00 × 00 cm"], ["Material", "Material"], ["Price", "₹0,000"]],
        },
    ),
    "carousel-close": (
        "feed",
        {"layout": "close", "logo": "stacked", "handle": True, "line": "arantdesign.com"},
    ),
    "story-tile": (
        "story",
        {"layout": "tile", "ground": "ivory", "label": "Label", "headline": "One Newsreader line", "symbol": True},
    ),
    "reel-cover": ("story", {"layout": "photo", "shot": "A calm frame from the reel", "title": "A short title"}),
}


def jobs():
    out = []
    tdir, pdir = os.path.join(SOCIAL, "templates"), os.path.join(SOCIAL, "posts")
    for name, (fmt, spec) in TEMPLATES.items():
        for suffix, g in (("", False), ("-guides", True)):
            doc, w, h = frame_page(fmt, spec, with_guides=g)
            out.append((doc, os.path.join(tdir, f"{name}{suffix}.png"), w, h))
    with open(os.path.join(SOCIAL, "posts.json")) as f:
        posts = json.load(f)["posts"]
    for post in posts:
        fmt, sample = post["format"], post.get("sample", False)
        if post["layout"] == "carousel":
            for i, frame in enumerate(post["frames"], 1):
                doc, w, h = frame_page(fmt, frame, sample=sample)
                name = f"{i:02d}-{frame.get('role', frame['layout'])}.png"
                out.append((doc, os.path.join(pdir, post["slug"], name), w, h))
        else:
            doc, w, h = frame_page(fmt, post, sample=sample)
            out.append((doc, os.path.join(pdir, f"{post['slug']}.png"), w, h))
    return out


def main():
    for d in ("templates", "posts"):
        path = os.path.join(SOCIAL, d)
        if os.path.isdir(path):
            shutil.rmtree(path)
    work = jobs()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda j: render.screenshot(*j), work))
    print(f"ok · {len(work)} PNGs in brand/social/templates/ and brand/social/posts/")


if __name__ == "__main__":
    main()
