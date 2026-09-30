"""ARANT brand guide → ../guide/arant-brand-kit.html and ../guide/palette.svg.

Coloured from packages/tokens/tokens.json.
"""

import os
import random
import re

import brand_tokens as tokens

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")  # brand/identity/
SVG = os.path.join(ROOT, "logo", "svg")


def read_master(name):
    with open(os.path.join(SVG, name)) as f:
        return f.read()


def mark(name, cls="", label=None):
    """Inline an SVG master, painted with currentColor so each surface sets its own ink."""
    s = read_master(name)
    s = re.sub(r"<title[^>]*>.*?</title>", "", s)
    s = re.sub(r' width="[\d.]+" height="[\d.]+"', "", s)
    s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="currentColor"', s)
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    s = s.replace('role="img" aria-labelledby="title"', f'{aria} class="{cls}"')
    return s.strip()


def mask_uri(name):
    s = read_master(name)
    s = re.sub(r"<title[^>]*>.*?</title>", "", s)
    s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="#000"', s)
    return "data:image/svg+xml," + (s.replace("#", "%23").replace('"', "'").replace("\n", ""))


def terrazzo(seed, base, chips, n=90, w=240, h=240):
    """Tileable terrazzo chips as an SVG data URI (deterministic)."""
    rnd = random.Random(seed)
    shapes = []
    for _ in range(n):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        r = rnd.choice([1.2, 1.6, 2.2, 3, 4.2, 5.5]) * rnd.uniform(0.7, 1.2)
        k = rnd.randint(3, 6)
        rot = rnd.uniform(0, 6.28)
        import math

        pts = " ".join(
            f"{x + r * rnd.uniform(0.6, 1.1) * math.cos(rot + i * 6.28 / k):.1f},"
            f"{y + r * rnd.uniform(0.6, 1.1) * math.sin(rot + i * 6.28 / k):.1f}"
            for i in range(k)
        )
        shapes.append(f"<polygon points='{pts}' fill='{rnd.choice(chips)}'/>")
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"
        f"<rect width='{w}' height='{h}' fill='{base}'/>{''.join(shapes)}</svg>"
    )
    return "data:image/svg+xml," + svg.replace("#", "%23")


# ---------------------------------------------------------------- colour: everything comes from the tokens
C = {k: tokens.color(k) for k in tokens.palette()}  # brand palette (packages/tokens/tokens.json)
mix = tokens.mix
UI = {  # the guide page's own interface shades: tints of the palette, so they follow any palette change
    "paper": C["ivory"],
    "sheet": mix("ivory", "#FFFFFF", 0.40),
    "plate": mix("ivory", "#FFFFFF", 0.62),
    "ink": mix("earth", "#000000", 0.34),
    "muted": mix("earth", "ivory", 0.22),
    "line": mix("sand", "#FFFFFF", 0.19),
    "accent": C["terracotta"],
    "d_paper": mix("charcoal", "#000000", 0.25),
    "d_sheet": C["charcoal"],
    "d_plate": mix("charcoal", "earth", 0.22),
    "d_ink": C["ivory"],
    "d_muted": mix("sand", "charcoal", 0.18),
    "d_line": mix("charcoal", "sand", 0.10),
    "d_accent": mix("terracotta", "#FFFFFF", 0.18),
}
M = {  # material props in the mockups (stone, kraft, table, walls), also mixed from the palette
    "table_hi": mix("ivory", "sand", 0.25),
    "table_lo": mix("sand", "earth", 0.08),
    "stone_hi": mix("olive", "ivory", 0.30),
    "ring": mix("ivory", "olive", 0.15),
    "kraft_hi": mix("kraft", "ivory", 0.10),
    "kraft_lo": mix("kraft", "earth", 0.10),
    "box_hi": mix("kraft", "ivory", 0.15),
    "box_lo": mix("kraft", "earth", 0.10),
    "kraft_ink": mix("earth", "#000000", 0.20),
    "hole": mix("sand", "earth", 0.22),
    "caption": mix("sand", "earth", 0.50),
    "scene": mix("ivory", "sand", 0.30),
    "rule": mix("ivory", "sand", 0.35),
    "wall_hi": mix("charcoal", "sand", 0.08),
    "door": mix("charcoal", "#000000", 0.35),
    "terrazzo_sand": mix("sand", "ivory", 0.30),
    "terrazzo_ivory": mix("ivory", "sand", 0.15),
    "chip_sand": mix("sand", "earth", 0.08),
    "chip_grey": mix("sand", "earth", 0.40),
}
OFF_PALETTE_BLUE = "#2E6FD8"  # deliberately not a brand colour: the "don't recolour" example

TERRAZZO_SAND = terrazzo(
    7, M["terrazzo_sand"], [C["terracotta"], M["caption"], C["ivory"], C["earth"], M["chip_sand"]], n=110
)
TERRAZZO_IVORY = terrazzo(11, M["terrazzo_ivory"], [C["sand"], C["terracotta"], M["chip_grey"], "#FFFFFF"], n=80)

PALETTE = [
    (tokens.name(k), C[k], " ".join(map(str, tokens.rgb(C[k]))), " ".join(map(str, tokens.cmyk(C[k]))), tokens.role(k))
    for k in tokens.palette()
    if k != "kraft"
]  # kraft is a mockup reference, not palette

SYM = mark("arant-symbol.svg")
SYM_REV = mark("arant-symbol-reversed.svg")
HORIZ = mark("arant-horizontal.svg", label="ARANT DESIGN")
STACK = mark("arant-stacked.svg")
ONELINE = mark("arant-one-line.svg")
WORD = mark("arant-wordmark.svg")
SHORT = mark("arant-wordmark-short.svg")

palette_rows = "".join(
    f'<div class="swatch"><div class="chip" style="background:{h}"></div><div class="sw-meta"><b>{n}</b>'
    f'<span class="mono">{h}</span><span class="mono">RGB {rgb}</span><span class="mono">CMYK {cmyk}*</span>'
    f'<span class="use">{use}</span></div></div>'
    for n, h, rgb, cmyk, use in PALETTE
)


def ratio(bg, fg):
    return f"{tokens.contrast(bg, fg):.1f} : 1"


PAIRS = [
    (C["ivory"], C["earth"], "Earth on ivory", "Primary"),
    (C["earth"], C["ivory"], "Ivory on earth", "Reversed"),
    (C["sand"], C["earth"], "Earth on sand", "Tags, tissue"),
    (C["kraft"], M["kraft_ink"], "Dark brown on kraft", "Shipping boxes"),
    (C["charcoal"], C["ivory"], "Ivory on charcoal", "Signage"),
    (C["terracotta"], C["ivory"], "Ivory on terracotta", "Seals only, large sizes"),
]
pairs = "".join(
    f'<figure class="pair" style="background:{bg};color:{fg}">{SYM}<figcaption><b>{t}</b>'
    f"<span>{ratio(bg, fg)} · {u}</span></figcaption></figure>"
    for bg, fg, t, u in PAIRS
)

DONTS = [
    ("Don't stretch or squash", 'style="transform:scaleX(1.45)"', ""),
    ("Don't rotate", 'style="transform:rotate(-14deg)"', ""),
    ("Don't close the split or move the pebble", "", "closed"),
    (
        "Don't add effects or gradients",
        f'style="filter:drop-shadow(3px 4px 2px rgba(0,0,0,.45));color:{C["terracotta"]}"',
        "",
    ),
    ("Don't outline the mark", "", "outline"),
    ("Don't recolour outside the palette", f'style="color:{OFF_PALETTE_BLUE}"', ""),
]


def dont_art(style, kind):
    if kind == "closed":
        return (
            '<svg viewBox="0 0 256 256" aria-hidden="true"><g fill="currentColor">'
            '<path d="M43 223L106 36H150L213 223H176L128 90L80 223Z"/><circle cx="128" cy="190" r="15.9"/></g></svg>'
        )
    if kind == "outline":
        return SYM.replace('fill="currentColor"', 'fill="none" stroke="currentColor" stroke-width="5"')
    return f'<div class="dont-inner" {style}>{SYM}</div>'


donts = "".join(
    f'<figure class="dont"><div class="dont-art">{dont_art(st, k)}</div><figcaption>{t}</figcaption></figure>'
    for t, st, k in DONTS
)

html = f"""<title>ARANT Brand Kit</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&family=Newsreader:opsz,wght@6..72,300;6..72,400&family=IBM+Plex+Mono&display=swap">
<style>
/* Layout: an identity manual. Wide single column, sections as chapters; objects shown on their own surfaces. */
:root {{
  --paper: {UI["paper"]}; --sheet: {UI["sheet"]}; --ink: {UI["ink"]}; --muted: {UI["muted"]}; --line: {UI["line"]}; --accent: {UI["accent"]};
  --plate: {UI["plate"]};
  --f-brand: "Jost", "Futura", "Century Gothic", "Helvetica Neue", Arial, sans-serif;
  --f-edit: "Newsreader", "Iowan Old Style", Georgia, serif;
  --f-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --paper: {UI["d_paper"]}; --sheet: {UI["d_sheet"]}; --ink: {UI["d_ink"]}; --muted: {UI["d_muted"]}; --line: {UI["d_line"]}; --accent: {UI["d_accent"]};
  --plate: {UI["d_plate"]}; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --paper: {UI["d_paper"]}; --sheet: {UI["d_sheet"]}; --ink: {UI["d_ink"]}; --muted: {UI["d_muted"]}; --line: {UI["d_line"]}; --accent: {UI["d_accent"]};
  --plate: {UI["d_plate"]}; color-scheme: dark }}
* {{ box-sizing: border-box }}
body {{ background: var(--paper); color: var(--ink); font: 16px/1.6 var(--f-brand); padding: 0 20px; }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding-block: 48px 96px; display: grid; gap: 88px; }}
svg {{ display: block; max-width: 100%; height: auto; }}
.mono {{ font-family: var(--f-mono); font-size: 12px; letter-spacing: .02em; }}
.eyebrow {{ font: 500 12px/1 var(--f-brand); letter-spacing: .22em; text-transform: uppercase; color: var(--muted); }}
h2 {{ font: 300 clamp(30px, 4.4vw, 44px)/1.1 var(--f-edit); margin: 0; text-wrap: balance; }}
h3 {{ font: 500 13px/1.3 var(--f-brand); letter-spacing: .16em; text-transform: uppercase; margin: 0; }}
p {{ margin: 0; max-width: 64ch; }}
.lede {{ font: 300 21px/1.5 var(--f-edit); max-width: 58ch; }}
section {{ display: grid; gap: 28px; }}
section > header {{ display: grid; gap: 12px; }}

/* hero */
.hero {{ display: grid; gap: 36px; }}
.hero-plate {{ background: var(--plate); padding: clamp(40px, 9vw, 120px) clamp(24px, 8vw, 110px); color: {C["earth"]}; }}
:root[data-theme="dark"] .hero-plate {{ color: {C["ivory"]} }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) .hero-plate {{ color: {C["ivory"]} }} }}
.hero-plate svg {{ width: min(100%, 720px); margin: 0 auto; }}
.hero-text {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 32px; align-items: start; }}
.hero-text .tagline {{ font: 500 14px/1.4 var(--f-brand); letter-spacing: .3em; text-transform: uppercase; color: var(--accent); }}

/* versions */
.versions {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; }}
.ver {{ background: var(--plate); color: var(--ink); padding: 28px; display: grid; gap: 18px; align-content: space-between; min-width: 0; }}
.ver .art {{ min-height: 150px; display: grid; place-items: center; }}
.ver .art svg {{ max-height: 170px; width: auto; max-width: 100%; }}
.ver.w2 {{ grid-column: span 2 }} .ver.w3 {{ grid-column: span 3 }} .ver.w4 {{ grid-column: span 4 }}
.ver.dark {{ background: {C["earth"]}; color: {C["ivory"]} }}
.ver p {{ font-size: 14px; color: var(--muted); }}
.ver.dark p {{ color: {C["sand"]} }}

/* construction */
.construct {{ display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 6fr); gap: 36px; align-items: center; }}
.construct figure {{ margin: 0; background: var(--plate); padding: 20px; }}
.construct dl {{ display: grid; grid-template-columns: 9em minmax(0, 1fr); gap: 10px 18px; margin: 0; }}
.construct dt {{ font-weight: 500; }}
.construct dd {{ margin: 0; color: var(--muted); }}
.diagram .ink {{ fill: var(--ink); opacity: .92 }}
.diagram .dim {{ stroke: var(--accent); stroke-width: 1.4; fill: none }}
.diagram .lbl {{ fill: var(--accent); font: 500 11px var(--f-mono); }}
.diagram .guide {{ stroke: var(--muted); stroke-width: 1; stroke-dasharray: 3 4; fill: none; opacity: .6 }}

/* tables */
.table-wrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; min-width: 620px; font-size: 15px; }}
th, td {{ text-align: left; padding: 12px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 500 12px var(--f-brand); letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }}
td {{ font-variant-numeric: tabular-nums; }}

/* colour */
.palette {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }}
.swatch {{ background: var(--sheet); border: 1px solid var(--line); min-width: 0; }}
.chip {{ height: 120px; }}
.sw-meta {{ display: grid; gap: 2px; padding: 14px 16px 16px; }}
.sw-meta b {{ font-weight: 500; }}
.sw-meta .use {{ font-size: 14px; color: var(--muted); margin-top: 6px; }}
.note {{ font-size: 14px; color: var(--muted); }}
.pairs {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; }}
.pair {{ margin: 0; padding: 22px 16px 14px; display: grid; gap: 14px; min-width: 0; }}
.pair svg {{ width: 62%; margin: 0 auto; }}
.pair figcaption {{ display: grid; gap: 2px; font-size: 13px; line-height: 1.35; }}
.pair figcaption span {{ opacity: .8 }}

/* type */
.type {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 16px; }}
.face {{ background: var(--sheet); border: 1px solid var(--line); padding: 28px; display: grid; gap: 14px; min-width: 0; }}
.face .spec {{ font-size: 14px; color: var(--muted); }}
.sample-sans {{ font: 400 40px/1.1 var(--f-brand); letter-spacing: .02em; }}
.sample-serif {{ font: 300 40px/1.15 var(--f-edit); }}
.hier {{ background: var(--plate); padding: 32px; display: grid; gap: 10px; }}
.hier .h-tag {{ font: 500 12px/1 var(--f-brand); letter-spacing: .3em; text-transform: uppercase; color: var(--accent); }}
.hier .h-title {{ font: 300 38px/1.1 var(--f-edit); }}
.hier .h-body {{ font: 400 16px/1.6 var(--f-brand); max-width: 56ch; }}
.hier .h-meta {{ font: 500 12px/1.4 var(--f-brand); letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }}

/* mockups */
.mocks {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; }}
.mock {{ margin: 0; display: grid; gap: 10px; min-width: 0; }}
.mock figcaption {{ font-size: 13px; color: var(--muted); }}
.mock .scene {{ aspect-ratio: 4 / 3; max-width: 100%; position: relative; overflow: hidden; display: grid; place-items: center; }}
.m2 {{ grid-column: span 2 }} .m3 {{ grid-column: span 3 }} .m4 {{ grid-column: span 4 }} .m6 {{ grid-column: span 6 }}
.m6 .scene {{ aspect-ratio: 21 / 8 }}
.deboss {{ position: absolute; background: rgba(62, 44, 30, .30);
  -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat;
  filter: drop-shadow(1.2px 1.4px 0 rgba(255,255,255,.55)) drop-shadow(-1px -1.2px 0 rgba(40,25,15,.4)); }}
.emboss {{ position: absolute; background: rgba(255,255,255,.12);
  -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat;
  filter: drop-shadow(-1px -1px 0 rgba(255,255,255,.5)) drop-shadow(1.5px 2px 0 rgba(60,40,25,.35)); }}
.s-table {{ background: radial-gradient(120% 90% at 30% 20%, {M["table_hi"]}, {M["table_lo"]}); }}
.tray {{ width: 78%; aspect-ratio: 1.7; border-radius: 22px; background: url("{TERRAZZO_SAND}") 0 0 / 240px;
  box-shadow: inset 0 0 0 10px rgba(255,255,255,.22), inset 0 12px 18px rgba(60,40,25,.28), 0 18px 30px rgba(60,40,25,.25); position: relative; }}
.coaster {{ width: 58%; aspect-ratio: 1; border-radius: 50%; background: url("{TERRAZZO_IVORY}") 0 0 / 200px;
  box-shadow: 0 14px 24px rgba(60,40,25,.25), inset 0 -4px 8px rgba(60,40,25,.18); position: relative; }}
.underside {{ width: 60%; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle at 40% 35%, {M["stone_hi"]}, {C["olive"]});
  box-shadow: 0 14px 24px rgba(40,30,20,.3); position: relative; display: grid; place-items: center; }}
.underside .ring {{ position: absolute; inset: 9%; }}
.kraft {{ background: linear-gradient(135deg, {M["kraft_hi"]}, {M["kraft_lo"]}); }}
.kraft::before {{ content: ""; position: absolute; inset: 0; opacity: .25;
  background: repeating-linear-gradient(80deg, rgba(90,60,30,.25) 0 1px, transparent 1px 7px),
              repeating-linear-gradient(-10deg, rgba(255,255,255,.18) 0 1px, transparent 1px 11px); }}
.box {{ width: 70%; aspect-ratio: 1.45; background: linear-gradient(160deg, {M["box_hi"]}, {M["box_lo"]}); position: relative;
  box-shadow: 0 20px 30px rgba(60,40,25,.28); display: grid; place-items: center; color: {M["kraft_ink"]}; }}
.box .band {{ position: absolute; left: 0; right: 0; top: 64%; height: 13%; background: {C["terracotta"]}; }}
.box svg {{ width: 34%; position: relative; top: -8%; }}
.tag {{ width: 36%; aspect-ratio: .55; background: {C["ivory"]}; position: relative; color: {C["earth"]}; transform: rotate(-6deg);
  box-shadow: 0 14px 22px rgba(60,40,25,.25); clip-path: polygon(18% 0, 82% 0, 100% 11%, 100% 100%, 0 100%, 0 11%);
  display: grid; align-content: space-between; justify-items: center; padding: 24% 12% 12%; }}
.tag::before {{ content: ""; position: absolute; top: 5.5%; left: 50%; width: 10%; aspect-ratio: 1; border-radius: 50%;
  transform: translateX(-50%); background: {M["hole"]}; }}
.tag svg {{ width: 56%; }}
.tag .t {{ text-align: center; font: 400 clamp(9px, 1vw, 12px)/1.45 var(--f-brand); }}
.tag .t b {{ display: block; font: 300 clamp(12px, 1.4vw, 16px)/1.2 var(--f-edit); margin-bottom: 4px; }}
.seal {{ width: 44%; aspect-ratio: 1; border-radius: 50%; background: {C["terracotta"]}; color: {C["ivory"]}; display: grid; place-items: center;
  box-shadow: 0 8px 14px rgba(60,40,25,.25); position: relative; }}
.seal > svg:first-child {{ width: 46% }}
.seal .ring {{ position: absolute; inset: 0; }}
.card-e {{ width: 60%; aspect-ratio: 1.75; background: {C["earth"]}; color: {C["ivory"]}; display: grid; place-items: center;
  box-shadow: 0 16px 24px rgba(30,20,10,.35); transform: rotate(-4deg) translate(-12%, -8%); position: absolute; }}
.card-e svg {{ width: 18% }}
.card-i {{ width: 60%; aspect-ratio: 1.75; background: {UI["sheet"]}; color: {C["earth"]}; box-shadow: 0 16px 24px rgba(30,20,10,.25);
  transform: rotate(3deg) translate(14%, 14%); position: absolute; padding: 6% 7%; display: grid; align-content: space-between; }}
.card-i svg {{ width: 52% }}
.card-i .who {{ font: 400 clamp(8px, .95vw, 11px)/1.45 var(--f-brand); }}
.card-i .who b {{ font-weight: 500; display: block; letter-spacing: .06em; }}
.thanks {{ width: 64%; aspect-ratio: 1.4; background: {C["ivory"]}; color: {C["earth"]}; box-shadow: 0 16px 24px rgba(30,20,10,.22);
  display: grid; place-items: center; align-content: center; gap: 12px; text-align: center; padding: 8%; }}
.thanks svg {{ width: 16% }}
.thanks p {{ font: 300 clamp(12px, 1.5vw, 18px)/1.35 var(--f-edit); }}
.thanks small {{ font: 500 clamp(8px, .8vw, 10px)/1 var(--f-brand); letter-spacing: .28em; text-transform: uppercase; color: {M["caption"]}; }}
.phone {{ width: 46%; aspect-ratio: .5; background: {UI["plate"]}; border-radius: 26px; box-shadow: 0 0 0 6px {C["charcoal"]}, 0 20px 30px rgba(20,15,10,.35);
  padding: 9% 7%; display: grid; align-content: start; gap: 8px; color: {C["charcoal"]}; }}
.ig-top {{ display: grid; grid-template-columns: 30% minmax(0, 1fr); gap: 8%; align-items: center; }}
.avatar {{ aspect-ratio: 1; border-radius: 50%; background: {C["earth"]}; color: {C["ivory"]}; display: grid; place-items: center; }}
.avatar svg {{ width: 58% }}
.ig-name {{ font: 500 clamp(9px, 1vw, 12px)/1.3 var(--f-brand); }}
.ig-bio {{ font: 400 clamp(7px, .8vw, 10px)/1.4 var(--f-brand); color: {UI["muted"]}; }}
.ig-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; margin-top: 6px; }}
.ig-grid i {{ aspect-ratio: 1; display: block; }}
.web {{ width: 88%; aspect-ratio: 1.6; background: {UI["sheet"]}; box-shadow: 0 18px 30px rgba(30,20,10,.22); display: grid; grid-template-rows: auto 1fr; }}
.web .bar {{ display: flex; align-items: center; justify-content: space-between; padding: 3.2% 4.5%; border-bottom: 1px solid {M["rule"]}; color: {C["earth"]}; gap: 12px; }}
.web .bar svg {{ width: 34% }}
.web nav {{ display: flex; gap: 6%; font: 500 clamp(7px, .8vw, 10px)/1 var(--f-brand); letter-spacing: .18em; text-transform: uppercase; color: {C["earth"]}; flex: 1; justify-content: flex-end; }}
.web .hero-w {{ display: grid; grid-template-columns: 1fr 1fr; }}
.web .hero-w div:first-child {{ padding: 8% 6%; display: grid; align-content: center; gap: 8px; color: {UI["ink"]}; }}
.web .hero-w b {{ font: 300 clamp(13px, 2vw, 24px)/1.15 var(--f-edit); }}
.web .hero-w span {{ font: 500 clamp(6px, .7vw, 9px)/1 var(--f-brand); letter-spacing: .2em; text-transform: uppercase; color: {C["terracotta"]}; }}
.web .hero-w div:last-child {{ background: url("{TERRAZZO_SAND}") 0 0 / 180px; }}
.sign {{ background: linear-gradient({M["wall_hi"]}, {C["charcoal"]}); }}
.sign .wall {{ position: absolute; inset: 0; background: repeating-linear-gradient(90deg, rgba(255,255,255,.035) 0 2px, transparent 2px 64px); }}
.sign .fascia {{ position: absolute; top: 18%; left: 10%; right: 10%; color: {C["ivory"]}; }}
.sign .door {{ position: absolute; bottom: 0; left: 40%; width: 20%; height: 44%; border-radius: 999px 999px 0 0; background: {M["door"]};
  box-shadow: inset 0 0 0 5px {C["earth"]}; }}
.wrap-band {{ background: {C["ivory"]}; }}
.tissue {{ position: absolute; inset: 0; color: {C["sand"]}; display: grid; grid-template-columns: repeat(16, 1fr); align-content: center; gap: 2.2% 1.4%; padding: 0 3%; transform: rotate(-4deg) scale(1.15); }}
.tissue span {{ display: block; }}
.tissue span:nth-child(odd) svg {{ transform: rotate(180deg); opacity: .8 }}
.band-strip {{ position: absolute; left: 0; right: 0; top: 38%; height: 24%; background: {C["earth"]}; color: {C["ivory"]}; display: grid; place-items: center; }}
.band-strip svg {{ height: 46%; width: auto; }}

/* usage */
.usage {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 16px; }}
.clear {{ background: var(--plate); padding: 28px; display: grid; gap: 16px; }}
.dont-grid {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; }}
.dont {{ margin: 0; display: grid; gap: 10px; min-width: 0; }}
.dont-art {{ aspect-ratio: 1; background: var(--plate); display: grid; place-items: center; color: {C["earth"]}; position: relative; overflow: hidden; }}
:root[data-theme="dark"] .dont-art {{ color: {C["ivory"]} }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) .dont-art {{ color: {C["ivory"]} }} }}
.dont-art > svg, .dont-inner {{ width: 58%; }}
.dont-art::after {{ content: ""; position: absolute; inset: 10%; background:
  linear-gradient(45deg, transparent calc(50% - 1px), var(--accent) calc(50% - 1px) calc(50% + 1px), transparent calc(50% + 1px)); opacity: .9; }}
.dont figcaption {{ font-size: 13px; color: var(--muted); }}
.files {{ columns: 2 320px; column-gap: 32px; font-size: 14px; }}
.files div {{ break-inside: avoid; padding: 10px 0; border-bottom: 1px solid var(--line); display: grid; gap: 2px; }}
.files code {{ font-family: var(--f-mono); font-size: 12.5px; color: var(--accent); }}

@media (max-width: 860px) {{
  .versions, .mocks {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  .ver.w2, .ver.w3, .ver.w4, .m2, .m3, .m4, .m6 {{ grid-column: span 2 }}
  .m6 .scene {{ aspect-ratio: 16 / 9 }}
  .palette {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  .pairs, .dont-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
  .hero-text, .construct, .type, .usage {{ grid-template-columns: minmax(0, 1fr); }}
}}
@media (max-width: 480px) {{
  .palette {{ grid-template-columns: minmax(0, 1fr); }}
  .pairs, .dont-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
}}
</style>

<div class="wrap">
  <section class="hero" aria-label="ARANT DESIGN identity">
    <div class="eyebrow">ARANT DESIGN · Identity kit · v1.1</div>
    <div class="hero-plate">{HORIZ}</div>
    <div class="hero-text">
      <p class="lede">Two equal stone slabs lean together and hold a pebble between them. The A becomes an object in balance: architectural, tactile and quiet.</p>
      <div style="display:grid;gap:14px">
        <div class="tagline">Objects for considered spaces</div>
        <p class="note">Every opening in the symbol, the split between the slabs and the gap around the pebble, has the same width. That one rule is what lets the mark survive a rubber stamp, a blind deboss and a silicone mould.</p>
      </div>
    </div>
  </section>

  <section>
    <header><div class="eyebrow">01 · Logo system</div><h2>Five lockups, one symbol</h2>
      <p>Use the horizontal lockup by default. Reach for the others when the space asks for it, never for variety.</p></header>
    <div class="versions">
      <div class="ver w4"><div class="art">{HORIZ}</div><div><h3>Horizontal · primary</h3><p>Website header, packaging, documents.</p></div></div>
      <div class="ver w2"><div class="art">{STACK}</div><div><h3>Stacked</h3><p>Labels, cards, square formats, signage.</p></div></div>
      <div class="ver w3"><div class="art">{WORD}</div><div><h3>Wordmark</h3><p>Editorial use and where the symbol already appears.</p></div></div>
      <div class="ver w3"><div class="art">{ONELINE}</div><div><h3>One line</h3><p>Narrow bands: product wraps, email footers, the site's sticky bar.</p></div></div>
      <div class="ver w3"><div class="art">{SYM}</div><div><h3>Symbol</h3><p>Stamps, seals, product marks, social avatar, favicon.</p></div></div>
      <div class="ver w3 dark"><div class="art">{SYM_REV}</div><div><h3>Symbol · reversed</h3><p>The same drawing in Warm Ivory for dark grounds.</p></div></div>
      <div class="ver w6" style="grid-column:1/-1"><div class="art" style="min-height:90px">{SHORT}</div><div><h3>ARANT only</h3><p>Moulded into products and on small tags, where DESIGN would fill in. Needs a cap height of at least 12 mm when stamped or cast, so the pebbles stay separate.</p></div></div>
    </div>
  </section>

  <section>
    <header><div class="eyebrow">02 · Construction</div><h2>One opening, repeated</h2></header>
    <div class="construct">
      <figure>
        <svg class="diagram" viewBox="0 0 256 256" role="img" aria-label="Construction of the symbol: split and pebble gap share one width">
          <line class="guide" x1="0" y1="33.3" x2="256" y2="33.3"/><line class="guide" x1="0" y1="222.7" x2="256" y2="222.7"/>
          <line class="guide" x1="128" y1="10" x2="128" y2="246"/>
          <g class="ink">{re.search(r"<g[^>]*>(.*)</g>", SYM, re.S).group(1)}</g>
          <path class="dim" d="M121.6 58h12.8M121.6 52v12M134.4 52v12"/><text class="lbl" x="140" y="62">x</text>
          <path class="dim" d="M112.9 162L100.8 158"/><text class="lbl" x="88" y="152">x</text>
          <path class="dim" d="M143.1 162L155.2 158"/><text class="lbl" x="160" y="152">x</text>
          <text class="lbl" x="6" y="28">cap line</text><text class="lbl" x="6" y="240">baseline</text>
        </svg>
      </figure>
      <dl>
        <dt>Split</dt><dd>x = 5 % of the symbol's grid. The two slabs are mirror images.</dd>
        <dt>Pebble gap</dt><dd>Also x, measured square to each slab's inner edge, not horizontally.</dd>
        <dt>Tops and feet</dt><dd>Fully rounded caps and softened feet: no point narrower than the split, nothing to chip in a mould.</dd>
        <dt>Wordmark</dt><dd>ARANT is drawn, not typed. Both As are the symbol itself, scaled to the cap height. R, N and T share its stroke (about 18 % of the cap height) and its corner radius. The N's diagonal sits at 60°.</dd>
        <dt>Descriptor</dt><dd>DESIGN is set at 27 % of the ARANT cap height and spaced to the exact width of ARANT.</dd>
      </dl>
    </div>
  </section>

  <section>
    <header><div class="eyebrow">03 · Clear space and minimum size</div><h2>Room to breathe, openings that stay open</h2>
      <p>Clear space on every side is half the ARANT cap height (for the symbol alone, a quarter of its height). Minimum sizes follow one production rule: keep every opening at 0.8 mm or more.</p></header>
    <div class="table-wrap"><table>
      <thead><tr><th>Version</th><th>Screen</th><th>Print</th><th>Stamp, deboss, mould, engrave</th></tr></thead>
      <tbody>
        <tr><td>Horizontal lockup</td><td>180 px wide</td><td>25 mm wide</td><td>82 mm wide. Below that, use the symbol or ARANT only.</td></tr>
        <tr><td>Stacked lockup</td><td>120 px wide</td><td>18 mm wide</td><td>54 mm wide</td></tr>
        <tr><td>ARANT only</td><td>16 px cap height</td><td>2.5 mm cap height</td><td>12 mm cap height</td></tr>
        <tr><td>Symbol</td><td>24 px (the split closes up at 16 px, where it reads as a solid A with a pebble)</td><td>6 mm tall</td><td>12 mm tall</td></tr>
      </tbody></table></div>
    <p class="note">These are production rules of thumb. Before the first run, make one proof rubber stamp and one test pour at the smallest size you plan to use.</p>
  </section>

  <section>
    <header><div class="eyebrow">04 · Colour</div><h2>Earth on ivory, with one warm accent</h2>
      <p>The logo lives in Earth Brown or Deep Charcoal on warm grounds. Terracotta is the accent: use it for one element per piece, like a seal, a band or a price.</p></header>
    <div class="palette">{palette_rows}</div>
    <p class="note">* CMYK values are straight conversions from RGB, a starting point only. Ask your printer to build the dark browns as rich blacks and confirm on a proof. Match Pantone references from a physical Formula Guide against the printed proof; screen previews of Pantone colours are unreliable.</p>
    <h3 style="margin-top:12px">Approved pairings</h3>
    <div class="pairs">{pairs}</div>
  </section>

  <section>
    <header><div class="eyebrow">05 · Typography</div><h2>A geometric sans and an editorial serif</h2>
      <p>The logo is custom-drawn and never typed. For everything around it, use two open-licence families from Google Fonts. Both are under the SIL Open Font License, free for commercial use, print and web.</p></header>
    <div class="type">
      <div class="face"><h3>Primary · Jost</h3><div class="sample-sans">Objects for considered spaces</div>
        <p class="spec">Geometric, like the wordmark. Use it for labels, navigation, product details, prices and packaging copy. Regular 400 and Medium 500; set uppercase labels with +0.2 em tracking.</p></div>
      <div class="face"><h3>Secondary · Newsreader</h3><div class="sample-serif">Cast by hand, finished slowly.</div>
        <p class="spec">Editorial serif for headlines, product names, stories and cards. Light 300 for display, Regular 400 for text. Never in all caps.</p></div>
    </div>
    <div class="hier" aria-label="Type hierarchy example">
      <div class="h-tag">New · The Plinth collection</div>
      <div class="h-title">A tray with the weight of stone</div>
      <div class="h-body">Each piece is poured in small batches from a mineral composite, then sanded and sealed by hand, so no two surfaces are quite alike.</div>
      <div class="h-meta">Sand · 32 × 18 cm · ₹1,800</div>
    </div>
  </section>

  <section>
    <header><div class="eyebrow">06 · In use</div><h2>On the objects first</h2>
      <p>Mockups drawn in the browser, not photographs. Product names and prices are examples only.</p></header>
    <div class="mocks">
      <figure class="mock m4"><div class="scene s-table"><div class="tray"><div class="deboss" style="--m:url(&quot;{mask_uri("arant-symbol.svg")}&quot;);inset:26% 38%"></div></div></div><figcaption>Blind deboss in a cast terrazzo tray</figcaption></figure>
      <figure class="mock m2"><div class="scene s-table"><div class="coaster"><div class="deboss" style="--m:url(&quot;{mask_uri("arant-wordmark-short.svg")}&quot;);inset:40% 18%"></div></div></div><figcaption>ARANT engraved in a coaster</figcaption></figure>
      <figure class="mock m2"><div class="scene s-table"><div class="underside"><svg class="ring" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="rp" d="M100 22a78 78 0 1 1 -0.1 0"/></defs><text fill="{M["ring"]}" style="font: 500 11px var(--f-brand); letter-spacing: 4.2px"><textPath href="#rp">HANDCAST IN INDIA · ARANTDESIGN.COM ·</textPath></text></svg><div class="emboss" style="--m:url(&quot;{mask_uri("arant-symbol.svg")}&quot;);inset:31%"></div></div></div><figcaption>Maker's stamp moulded into a base</figcaption></figure>
      <figure class="mock m2"><div class="scene kraft"><div class="box">{STACK}<div class="band"></div></div></div><figcaption>Kraft box, one-colour print with a terracotta band</figcaption></figure>
      <figure class="mock m2"><div class="scene s-table"><div class="tag">{SYM}<div class="t"><b>Plinth Tray</b>Sand · Hand-finished<br>₹1,800</div></div></div><figcaption>Hang tag</figcaption></figure>
      <figure class="mock m3"><div class="scene kraft"><div class="seal">{SYM_REV}<svg class="ring" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="sp" d="M100 18a82 82 0 1 1 -0.1 0"/></defs><text fill="{C["ivory"]}" style="font: 500 11.5px var(--f-brand); letter-spacing: 5.3px"><textPath href="#sp">ARANT DESIGN · OBJECTS FOR CONSIDERED SPACES ·</textPath></text></svg></div></div><figcaption>Seal sticker for tissue and mailers</figcaption></figure>
      <figure class="mock m3"><div class="scene s-table"><div class="thanks">{SYM}<p>Thank you for giving this object a place in your home.</p><small>ARANT DESIGN</small></div></div><figcaption>Thank-you card</figcaption></figure>
      <figure class="mock m3"><div class="scene s-table"><div class="card-e">{SYM_REV}</div><div class="card-i">{HORIZ}<div class="who"><b>STUDIO</b>hello@arantdesign.com<br>arantdesign.com · @arantdesign</div></div></div><figcaption>Business card, front and back</figcaption></figure>
      <figure class="mock m3"><div class="scene" style="background:{M["scene"]}"><div class="phone"><div class="ig-top"><div class="avatar">{SYM}</div><div><div class="ig-name">arantdesign</div><div class="ig-bio">ARANT DESIGN<br>Objects for considered spaces.<br>Small-batch, hand-finished in India.</div></div></div>
        <div class="ig-grid"><i style="background:url('{TERRAZZO_SAND}') 0 0/90px"></i><i style="background:{C["earth"]}"></i><i style="background:{C["sand"]}"></i><i style="background:{C["terracotta"]}"></i><i style="background:url('{TERRAZZO_IVORY}') 0 0/80px"></i><i style="background:{C["olive"]}"></i><i style="background:{C["ivory"]}"></i><i style="background:url('{TERRAZZO_SAND}') 40px 20px/120px"></i><i style="background:{C["charcoal"]}"></i></div></div></div><figcaption>Instagram profile: the symbol as the avatar</figcaption></figure>
      <figure class="mock m3"><div class="scene s-table"><div class="web"><div class="bar">{ONELINE}<nav><span>Objects</span><span>Studio</span><span>Journal</span></nav></div><div class="hero-w"><div><span>The Plinth collection</span><b>Objects for considered spaces</b></div><div></div></div></div></div><figcaption>Website header</figcaption></figure>
      <figure class="mock m3"><div class="scene sign"><div class="wall"></div><div class="fascia">{ONELINE}</div><div class="door"></div></div><figcaption>Studio signage: ivory on charcoal</figcaption></figure>
      <figure class="mock m6"><div class="scene wrap-band"><div class="tissue" aria-hidden="true">{"".join(f"<span>{SYM}</span>" for _ in range(64))}</div><div class="band-strip">{ONELINE}</div></div><figcaption>Tissue paper pattern in sand, with the earth-brown wrapping band</figcaption></figure>
    </div>
  </section>

  <section>
    <header><div class="eyebrow">07 · Pattern</div><h2>The symbol as texture</h2>
      <p>For tissue paper, box liners and the website background, repeat the symbol on a loose grid and turn every second one upside down, in Sand on Ivory or Ivory on Sand. Keep it at least three times smaller than any logo on the same surface, so it reads as texture, not as a second logo.</p></header>
  </section>

  <section>
    <header><div class="eyebrow">08 · Don'ts</div><h2>Keep the balance</h2></header>
    <div class="dont-grid">{donts}</div>
    <p class="note">Also: don't retype ARANT in a font, don't rearrange or resize the parts of a lockup, and don't place the logo on busy photography without a calm area or a solid panel.</p>
  </section>

  <section>
    <header><div class="eyebrow">09 · Files</div><h2>What's in the kit folder</h2>
      <p>Everything lives in <code class="mono">brand/identity/</code> in the ARANT DESIGN repository.</p></header>
    <div class="files">
      <div><code>logo/svg/</code>Masters: symbol, symbol reversed, horizontal, stacked, one-line, wordmark, ARANT only</div>
      <div><code>export/&lt;version&gt;/*.svg</code>One-colour versions: earth, charcoal, terracotta, ivory, black, white</div>
      <div><code>export/&lt;version&gt;/*.png</code>Transparent PNGs at 600 / 1200 / 2400 px (symbol: 64–1024 px)</div>
      <div><code>export/symbol/</code>favicon.ico, favicon.svg, apple-touch and PWA icons, site.webmanifest, head-snippet.html</div>
      <div><code>print/pdf/</code>Vector PDFs in earth, black and terracotta. They open in Illustrator, Affinity and InDesign.</div>
      <div><code>print/jpg/</code>JPGs on warm ivory for email, documents and marketplaces</div>
      <div><code>source/</code>The Python scripts that generate every file, so the geometry can be rebuilt exactly</div>
    </div>
  </section>
</div>
"""

with open(os.path.join(ROOT, "guide", "arant-brand-kit.html"), "w") as f:
    f.write(html)


def palette_svg():
    """guide/palette.svg: the swatch strip used in the READMEs, drawn from the tokens."""
    keys = [k for k in tokens.palette() if k != "kraft"]
    notes = {"earth": " · logo", "terracotta": " · accent"}
    cells = []
    for i, k in enumerate(keys):
        x = 20 + i * 156
        edge = f' stroke="{UI["line"]}"' if tokens.contrast(C[k], UI["sheet"]) < 1.3 else ""
        cells.append(
            f'<rect x="{x}" y="20" width="140" height="110" fill="{C[k]}"{edge}/>'
            f'<text x="{x}" y="152" font-weight="600">{tokens.name(k)}</text>'
            f'<text x="{x}" y="172" fill="{UI["muted"]}">{C[k]}{notes.get(k, "")}</text>'
        )
    w = 20 + len(keys) * 156 + 4
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 200" width="{w}" height="200" role="img" '
        f'aria-labelledby="title"><title id="title">ARANT DESIGN colour palette</title>'
        f'<rect width="{w}" height="200" fill="{UI["sheet"]}"/>'
        f'<g font-family="Helvetica Neue, Arial, sans-serif" font-size="13" fill="{UI["ink"]}">{"".join(cells)}</g></svg>\n'
    )


with open(os.path.join(ROOT, "guide", "palette.svg"), "w") as f:
    f.write(palette_svg())
print("ok", len(html) // 1024, "KB")
