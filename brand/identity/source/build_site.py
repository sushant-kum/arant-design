"""GitHub Pages site → ../../../site/ (gitignored), published at https://sushant-kum.github.io/arant-design/.

  index.html                  a landing page: the stacked lockup, links to the pages and to the files in the repo
  brand-kit/index.html        guide/arant-brand-kit.html, wrapped in a full HTML document (content unchanged)
  design-language/index.html  brand/design-language/arant-design-language.html, wrapped the same way
  icons/index.html            the interface icons, drawn from icons/sprite.svg, and the preview sheet
  social/index.html           the Instagram templates in brand/social/templates/
  assets/                     only the files these pages reference

Python stdlib only and no Chrome: it reads the committed, generated files and never rebuilds them, so CI can run it.
Run `pnpm identity:build` first when the identity has changed. Every link inside the site is relative, so it works
under the /arant-design/ path. Colours, type and spacing come from packages/tokens/tokens.json.
Run: python3 build_site.py
"""

# cspell:ignore IHDR figcaption labelledby minmax nojekyll stdlib wght
import html
import os
import re
import shutil
import struct

import brand_tokens as tokens

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
IDENTITY = os.path.join(REPO, "brand", "identity")
SITE = os.path.join(REPO, "site")

REPO_URL = "https://github.com/sushant-kum/arant-design"
TREE, BLOB = f"{REPO_URL}/tree/main/", f"{REPO_URL}/blob/main/"
FONTS_CSS = (
    "https://fonts.googleapis.com/css2?family=Jost:wght@400;500"
    "&family=Newsreader:opsz,wght@6..72,300;6..72,400&display=swap"
)  # the guide's own font request


def read(*parts):
    with open(os.path.join(REPO, *parts), encoding="utf-8") as f:
        return f.read()


def write(rel, text):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


ASSETS = []  # (source path relative to the repo, published name under assets/), filled as pages reference them


def png_size(src):
    """Width and height from a PNG's IHDR chunk, so the page reserves the image's space before it loads."""
    with open(os.path.join(REPO, src), "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def asset(src, depth):
    """Reference a repo file from a page `depth` folders below the site root, and queue it for copying."""
    name = os.path.basename(src)
    if (src, name) not in ASSETS:
        ASSETS.append((src, name))
    return "../" * depth + "assets/" + name


# ---------------------------------------------------------------- tokens
def stack(key):
    generic = {"serif", "sans-serif"}
    return ", ".join(f if f in generic else f'"{f}"' for f in tokens.fonts(key))


V = tokens.value
LIGHT = {
    "ground": tokens.color("color.role.surface.ground"),
    "alt": tokens.color("color.role.surface.alt"),
    "text": tokens.color("color.role.text.primary"),
    "head": tokens.color("color.role.text.secondary"),
    "muted": tokens.color("color.role.text.muted"),
    "line": tokens.color("color.role.line.subtle"),
    "strong": tokens.color("color.role.line.strong"),
    "accent": tokens.color("color.role.accent"),
    "logo": tokens.color("logo.default"),
}
DARK = {
    "ground": tokens.color("color.roleDark.surface.ground"),
    "alt": tokens.color("color.roleDark.surface.alt"),
    "text": tokens.color("color.roleDark.text.primary"),
    "head": tokens.color("color.roleDark.text.primary"),  # the dark theme has no separate secondary text colour
    "muted": tokens.color("color.roleDark.text.muted"),
    "line": tokens.color("color.roleDark.line.subtle"),
    "strong": tokens.color("color.roleDark.line.strong"),
    "accent": tokens.color("color.roleDark.accent"),
    "logo": tokens.color("logo.reversed"),
}


def palette_css(selector, values):
    return f"{selector} {{ " + " ".join(f"--{k}: {v};" for k, v in values.items()) + " }"


THEME = "\n".join(
    [
        palette_css(":root", LIGHT),
        "@media (prefers-color-scheme: dark) { "
        + palette_css(':root:not([data-theme="light"])', DARK)[:-1]
        + "color-scheme: dark; } }",
        palette_css(':root[data-theme="dark"]', DARK)[:-1] + "color-scheme: dark; }",
    ]
)
GUTTER = f"clamp({V('gutter.min')}, {V('gutter.preferred')}, {V('gutter.max')})"
TRACK = V("letterSpacing.label")
HAIR = f"{V('border.subtle')['width']} {V('border.subtle')['style']} var(--line)"
QUICK = V("duration.quick")


# ---------------------------------------------------------------- the logo masters, unchanged, in currentColor
def master(name, label=None):
    s = read("brand", "identity", "logo", "svg", name)
    s = re.sub(r"<title[^>]*>.*?</title>", "", s)
    s = re.sub(r' width="[\d.]+" height="[\d.]+"', "", s)
    s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="currentColor"', s)
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return s.replace('role="img" aria-labelledby="title"', aria).strip()


# ---------------------------------------------------------------- documents
FONT_LINKS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    f'<link rel="stylesheet" href="{FONTS_CSS}">\n'
)


def head(title, description, depth, style="", fonts=False):
    favicon_ico = asset("brand/identity/export/symbol/favicon.ico", depth)
    favicon_svg = asset("brand/identity/export/symbol/favicon.svg", depth)
    touch = asset("brand/identity/export/symbol/apple-touch-icon.png", depth)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" href="{favicon_ico}" sizes="48x48">
<link rel="icon" href="{favicon_svg}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{touch}">
<meta name="theme-color" content="{LIGHT["logo"]}">
{FONT_LINKS if fonts else ""}<style>
body {{ margin: 0; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
{style}</style>
</head>
<body>
"""


FOOT = "</body>\n</html>\n"

# A slim bar above a wrapped page, so every page leads back to the index. Its colours match both pages' grounds.
BACK_CSS = f"""{THEME}
.site-back {{ background: var(--ground); border-bottom: {HAIR}; padding: 12px {GUTTER}; }}
.site-back a {{ font: 500 12px/1.3 {stack("sans")}; letter-spacing: {TRACK}; text-transform: uppercase;
  color: var(--muted); text-decoration: none; }}
.site-back a:hover {{ color: var(--head); text-decoration: underline; text-underline-offset: .25em; }}
.site-back a:focus-visible {{ outline: 2px solid var(--strong); outline-offset: 2px; }}
"""


def wrap(page_html, description):
    """A full document around an artifact-shaped page (no doctype or head of its own). Only the leading comment and
    <title> are lifted out, so the page's own content, styles and fonts stay exactly as they are."""
    body = re.sub(r"^\s*<!--.*?-->\s*", "", page_html, count=1, flags=re.S)
    title = re.match(r"\s*<title>(.*?)</title>\s*", body, re.S)
    if not title:
        raise SystemExit("a wrapped page must start with its <title>")
    back = '<nav class="site-back" aria-label="Site"><a href="../">← ARANT DESIGN · Brand pages</a></nav>\n'
    return head(html.unescape(title.group(1)), description, 1, BACK_CSS) + back + body[title.end() :] + FOOT


# ---------------------------------------------------------------- the site's own pages
BASE_CSS = f"""{THEME}
* , *::before, *::after {{ box-sizing: border-box; }}
body {{ background: var(--ground); color: var(--text); font: 400 16px/1.6 {stack("sans")};
  -webkit-font-smoothing: antialiased; }}
.wrap {{ max-width: {V("container.content")}; margin-inline: auto; padding-inline: {GUTTER}; }}
a {{ color: inherit; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: .25em;
  transition: text-decoration-thickness {QUICK} ease-out; }}
a:hover {{ text-decoration-thickness: 2px; }}
:focus-visible {{ outline: 2px solid var(--strong); outline-offset: 2px; }}
h1, h2, p, ul, figure {{ margin: 0; }}
h1 {{ font: 300 clamp(36px, 5vw, 56px)/1.08 {stack("serif")}; color: var(--head); text-wrap: balance; }}
h2 {{ font: 300 clamp(26px, 3.4vw, 34px)/1.15 {stack("serif")}; color: var(--head); }}
p {{ max-width: {V("container.text")}; text-wrap: pretty; }}
.label {{ font: 500 12px/1.3 {stack("sans")}; letter-spacing: {TRACK}; text-transform: uppercase;
  color: var(--head); }}
.muted {{ color: var(--muted); }}
.lede {{ font: 300 21px/1.5 {stack("serif")}; max-width: 58ch; }}
.top {{ padding-block: {V("space.9")} {V("space.8")}; display: grid; gap: {V("space.6")}; }}
.top .mark {{ display: block; width: 132px; height: auto; color: var(--logo); }}
.top .back {{ text-decoration: none; }}
section {{ padding-block: {V("space.7")} {V("space.8")}; display: grid; gap: {V("space.6")}; }}
section > * {{ min-width: 0; }}
.rows {{ list-style: none; padding: 0; display: grid; }}
.rows li {{ display: grid; grid-template-columns: minmax(0, 4fr) minmax(0, 7fr) auto; gap: {V("space.5")};
  align-items: baseline; padding-block: {V("space.5")}; border-bottom: {HAIR}; }}
.rows li:first-child {{ border-top: {HAIR}; }}
.rows .name {{ font: 400 22px/1.25 {stack("serif")}; color: var(--head); }}
.rows .go {{ font-weight: 500; white-space: nowrap; }}
.accent {{ display: flex; align-items: center; gap: .9em; }}
.accent::before {{ content: ""; flex: none; width: 2em; height: 2px; background: var(--accent); }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 240px), 1fr));
  gap: {V("space.6")} {V("space.5")}; }}
.grid figure {{ display: grid; gap: {V("space.3")}; align-content: start; min-width: 0; }}
.grid img {{ display: block; width: 100%; height: auto; border: {HAIR}; }}
figcaption {{ font-size: 14px; line-height: 1.5; color: var(--muted); }}
.icons {{ list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(96px, 1fr));
  gap: {V("space.5")} {V("space.3")}; }}
.icons li {{ display: grid; justify-items: center; gap: {V("space.2")}; font-size: 13px; color: var(--muted); }}
.icons svg {{ width: 24px; height: 24px; color: var(--head); }}
.sheet {{ background: {LIGHT["ground"]}; border: {HAIR}; padding: {V("space.4")}; overflow-x: auto; }}
.sheet img {{ display: block; max-width: none; width: 100%; min-width: 640px; height: auto; }}
footer .wrap {{ padding-block: {V("space.7")} {V("space.8")}; border-top: {HAIR}; display: flex; flex-wrap: wrap;
  justify-content: space-between; gap: {V("space.4")}; font-size: 14px; color: var(--muted); }}
@media (max-width: {V("breakpoint.md")}) {{
  .top {{ padding-block: {V("space.8")} {V("space.7")}; }}
  .rows li {{ grid-template-columns: minmax(0, 1fr); gap: {V("space.2")}; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
"""

LICENCE = f'<a href="{BLOB}LICENSE">Licence</a>'
FOOTER = (
    f'<footer><div class="wrap"><p>© ARANT DESIGN · all rights reserved · {LICENCE}</p>'
    f'<p><a href="{REPO_URL}">Source on GitHub</a></p></div></footer>\n'
)

PAGES = [
    (
        "brand-kit/",
        "Brand kit",
        "The identity: lockups, construction, clear space and minimum sizes, colour, type and the mark in use.",
    ),
    (
        "design-language/",
        "Design language",
        "How the brand looks, behaves and speaks beyond the logo: principles, "
        "layout, photography, packaging, digital, social and voice.",
    ),
    ("icons/", "Icons", "Seventeen interface line icons drawn from the mark, at 16, 20 and 24 px."),
    (
        "social/",
        "Instagram templates",
        "Designed tiles, carousel frames and covers, rendered from the design language.",
    ),
]
FILES = [
    ("brand/identity/export/", "Logo files", "One-colour SVG and transparent PNG for every lockup, plus favicons"),
    ("brand/identity/print/pdf/", "Print PDFs", "Vector PDFs in Earth Brown, Terracotta and black"),
    ("brand/identity/logo/svg/", "Logo masters", "The seven master SVGs every other file is drawn from"),
    ("brand/identity/icons/", "Icons", "Line icons as SVG files and a sprite"),
    ("packages/tokens/tokens.json", "Design tokens", "Colour, type, spacing, layout, radius and motion"),
    ("brand/social/templates/", "Instagram templates", "Templates and their safe-area guides"),
]


def rows(items, href, cta):
    return "".join(
        f'<li><span class="name">{html.escape(name)}</span><span class="muted">{html.escape(text)}</span>'
        f'<a class="go" href="{href(path)}">{cta}</a></li>'
        for path, name, text in items
    )


LOCKUP = master("arant-stacked.svg", "ARANT DESIGN").replace("<svg ", '<svg class="mark" ', 1)


def index_page():
    description = "The ARANT DESIGN identity, design language, icons and Instagram templates."
    body = (
        '<main><div class="wrap top">'
        f"{LOCKUP}"
        '<p class="label accent">Brand pages</p>'
        "<h1>Objects for Considered Spaces.</h1>"
        '<p class="lede">The identity and design language of ARANT DESIGN, a contemporary Indian objects and '
        "home-design brand, with the files to use them.</p></div>"
        '<div class="wrap"><section aria-labelledby="pages"><h2 id="pages">Pages</h2>'
        f'<ul class="rows">{rows(PAGES, lambda p: p, "Open →")}</ul></section>'
        '<section aria-labelledby="files"><h2 id="files">Files</h2>'
        '<p class="muted">Download the finished files from the repository. Everything is generated from the build '
        "scripts and the tokens; never edit them by hand.</p>"
        f'<ul class="rows">{rows(FILES, lambda p: (BLOB if "." in os.path.basename(p) else TREE) + p, "On GitHub →")}'
        "</ul></section></div></main>"
    )
    return head("ARANT DESIGN · Brand pages", description, 0, BASE_CSS, fonts=True) + body + FOOTER + FOOT


def subpage(title, intro, content, description):
    top = (
        '<main><div class="wrap top"><a class="label back" href="../">← ARANT DESIGN · Brand pages</a>'
        f'<h1>{html.escape(title)}</h1><p class="lede">{intro}</p></div>'
        f'<div class="wrap"><section aria-label="{html.escape(title)}">{content}</section></div></main>'
    )
    return head(f"ARANT {title}", description, 1, BASE_CSS, fonts=True) + top + FOOTER + FOOT


def icons_page():
    sprite = read("brand", "identity", "icons", "sprite.svg").strip()
    names = re.findall(r'<symbol id="icon-([a-z-]+)"', sprite)
    items = "".join(
        f'<li><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#icon-{n}"/></svg><span>{n}</span></li>'
        for n in names
    )
    preview = asset("brand/identity/icons/icons-preview.png", 1)
    w, h = png_size("brand/identity/icons/icons-preview.png")
    content = (
        f'{sprite}<ul class="icons" aria-label="The icon set">{items}</ul>'
        f'<figure><div class="sheet"><img src="{preview}" alt="Every icon at 16, 20 and 24 px, in Earth Brown on '
        f'Warm Ivory" width="{w}" height="{h}"></div>'
        "<figcaption>The preview sheet: at 16 px the stroke is 2 and at 20 px 1.75, so the line stays close to "
        "Jost Regular beside it.</figcaption></figure>"
        f'<p class="muted">SVG files and the sprite: <a href="{TREE}brand/identity/icons/">brand/identity/icons/</a>. '
        "Each icon is painted in <code>currentColor</code>; give it a visible label or an accessible name.</p>"
    )
    return subpage(
        "Icons",
        "Line icons drawn from the mark: straight strokes for the slabs, the circle for the pebble, the arch.",
        content,
        "The ARANT DESIGN interface icons.",
    )


def social_page():
    folder = os.path.join(REPO, "brand", "social", "templates")
    names = sorted(n for n in os.listdir(folder) if n.endswith(".png") and not n.endswith("-guides.png"))
    figures = "".join(
        f'<figure><img src="{asset(f"brand/social/templates/{n}", 1)}" alt="Instagram template: '
        f'{n[:-4].replace("-", " ")}" loading="lazy"><figcaption>{n[:-4]}</figcaption></figure>'
        for n in names
    )
    content = (
        f'<div class="grid">{figures}</div>'
        f'<p class="muted">Each template also has a <code>-guides.png</code> with its safe areas, in '
        f'<a href="{TREE}brand/social/templates/">brand/social/templates/</a>. New posts are entries in '
        f'<a href="{BLOB}brand/social/posts.json">posts.json</a>.</p>'
    )
    return subpage(
        "Instagram templates",
        "Feed posts at 1080 × 1350 and stories and reel covers at 1080 × 1920, with placeholder copy.",
        content,
        "The ARANT DESIGN Instagram templates.",
    )


def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    write("index.html", index_page())
    write(
        "brand-kit/index.html",
        wrap(read("brand", "identity", "guide", "arant-brand-kit.html"), "The ARANT DESIGN identity kit."),
    )
    write(
        "design-language/index.html",
        wrap(read("brand", "design-language", "arant-design-language.html"), "The ARANT DESIGN design language."),
    )
    write("icons/index.html", icons_page())
    write("social/index.html", social_page())
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    for src, name in ASSETS:
        shutil.copyfile(os.path.join(REPO, src), os.path.join(SITE, "assets", name))
    write(".nojekyll", "")  # serve the files as they are
    print(f"ok · 5 pages and {len(ASSETS)} assets in site/")


if __name__ == "__main__":
    main()
