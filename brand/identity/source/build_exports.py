"""One-colour exports, PNG sizes and the web/app icon set, all coloured from packages/tokens/tokens.json.

Output: ../export/<version>/arant-<version>-<colour>.svg|png  (colour = token name, so file names never change
when a colour value does), plus ../export/symbol/ web icons: favicon.ico/.svg, PNG icons, site.webmanifest,
head-snippet.html.
Run: python3 build_exports.py   (needs Chrome/Chromium; set CHROME=/path if it isn't on PATH)
"""

import json
import os
import re
import shutil

import brand_tokens as tokens
import render

HERE = os.path.dirname(os.path.abspath(__file__))
MASTERS = os.path.join(HERE, "..", "logo", "svg")
OUT = os.path.join(HERE, "..", "export")

VERSIONS = {  # master file → PNG widths
    "symbol": (64, 256, 512, 1024),
    "horizontal": (600, 1200, 2400),
    "stacked": (600, 1200, 2400),
    "one-line": (600, 1200, 2400),
    "wordmark": (600, 1200, 2400),
    "wordmark-short": (600, 1200, 2400),
}
# brand colours from the tokens, plus plain black and white for production (stamps, dies, engraving files)
COLOURS = {k: tokens.color(k) for k in ("earth", "charcoal", "terracotta", "ivory")}
COLOURS.update({"black": "#000000", "white": "#FFFFFF"})

SITE_NAME, SHORT_NAME = "ARANT DESIGN", "ARANT"


def master(version):
    return open(os.path.join(MASTERS, f"arant-{version}.svg")).read()


def recolour(svg, hex_value):
    return re.sub(r'fill="#[0-9A-Fa-f]{6}"', f'fill="{hex_value}"', svg)


def inner(svg):
    """The master's drawing without the outer <svg> and <title>, for placing inside another SVG."""
    body = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    return re.sub(r"<title[^>]*>.*?</title>", "", body)


def symbol_on(size, scale, fill, tile=None, radius=0.0, dark_fill=None, title="ARANT symbol"):
    """Symbol centred on a size×size canvas, scaled to `scale` of it, optionally on a (rounded) tile."""
    s = size / 256 * scale
    off = (size - 256 * s) / 2
    style = ""
    if dark_fill:  # favicon.svg follows the browser's light/dark tab bar
        style = f"<style>@media (prefers-color-scheme: dark) {{ .m {{ fill: {dark_fill} }} }}</style>"
    bg = f'<rect width="{size}" height="{size}" rx="{radius * size:.2f}" fill="{tile}"/>' if tile else ""
    art = re.sub(r'<g fill="#[0-9A-Fa-f]{6}">', f'<g class="m" fill="{fill}">', inner(master("symbol")))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}" '
        f'role="img" aria-labelledby="title"><title id="title">{title}</title>{style}{bg}'
        f'<g transform="translate({off:.2f} {off:.2f}) scale({s:.4f})">{art}</g></svg>\n'
    )


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    jobs = []

    # 1 · one-colour SVGs + transparent PNGs for every version
    for version, widths in VERSIONS.items():
        for cname, hex_value in COLOURS.items():
            svg = recolour(master(version), hex_value)
            base = os.path.join(OUT, version, f"arant-{version}-{cname}")
            write(base + ".svg", svg)
            jobs += [
                {"svg": svg, "out": f"{base}-{w}.png", "width": w, "height": w if version == "symbol" else None}
                for w in widths
            ]

    # 2 · symbol formats for avatars, app icons and browsers
    logo, reversed_ = tokens.color("logo.default"), tokens.color("logo.reversed")
    sym = os.path.join(OUT, "symbol")
    square = symbol_on(256, 0.80, logo)  # avatar master, transparent
    app_icon = symbol_on(256, 0.62, reversed_, tile=logo, radius=0.225)  # rounded tile, iOS/Android style
    full_tile = symbol_on(256, 0.62, reversed_, tile=logo)  # square tile (apple-touch: iOS rounds it)
    maskable = symbol_on(256, 0.50, reversed_, tile=logo)  # mark inside the 80 % safe zone
    favicon = symbol_on(256, 0.96, logo, dark_fill=reversed_)  # tight, follows light/dark tab bars
    write(os.path.join(sym, "arant-symbol-square.svg"), square)
    write(os.path.join(sym, "arant-symbol-app-icon.svg"), app_icon)
    write(os.path.join(sym, "favicon.svg"), favicon)
    for w in (256, 512, 1024):
        jobs.append({"svg": square, "out": os.path.join(sym, f"arant-symbol-square-{w}.png"), "width": w, "height": w})
        jobs.append(
            {"svg": app_icon, "out": os.path.join(sym, f"arant-symbol-app-icon-{w}.png"), "width": w, "height": w}
        )
    favicon_light = symbol_on(256, 0.96, logo)
    for w in (16, 32, 48):
        jobs.append({"svg": favicon_light, "out": os.path.join(sym, f"favicon-{w}.png"), "width": w, "height": w})
    jobs.append({"svg": full_tile, "out": os.path.join(sym, "apple-touch-icon.png"), "width": 180, "height": 180})
    jobs.append({"svg": app_icon, "out": os.path.join(sym, "icon-192.png"), "width": 192, "height": 192})
    jobs.append({"svg": app_icon, "out": os.path.join(sym, "icon-512.png"), "width": 512, "height": 512})
    jobs.append({"svg": maskable, "out": os.path.join(sym, "maskable-512.png"), "width": 512, "height": 512})

    render.rasterize(jobs)
    render.write_ico([os.path.join(sym, f"favicon-{w}.png") for w in (16, 32, 48)], os.path.join(sym, "favicon.ico"))

    manifest = {
        "name": SITE_NAME,
        "short_name": SHORT_NAME,
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "theme_color": logo,
        "background_color": tokens.color("ivory"),
        "display": "standalone",
    }
    write(os.path.join(sym, "site.webmanifest"), json.dumps(manifest, indent=2) + "\n")
    write(
        os.path.join(sym, "head-snippet.html"),
        '<link rel="icon" href="/favicon.ico" sizes="48x48">\n'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<link rel="manifest" href="/site.webmanifest">\n'
        f'<meta name="theme-color" content="{logo}">\n',
    )
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print(f"ok · {n} files in export/")


if __name__ == "__main__":
    main()
