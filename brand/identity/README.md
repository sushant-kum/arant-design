# ARANT DESIGN · Brand identity

![ARANT DESIGN logo](print/jpg/arant-horizontal-on-ivory.jpg)

**Objects for considered spaces.** The ARANT DESIGN logo system: master artwork, ready-to-use exports, print files,
the brand guide, and the scripts that generate all of them. Part of the [ARANT DESIGN monorepo](../../README.md).

**Version 1.1** · Brand guide: open [`guide/arant-brand-kit.html`](guide/arant-brand-kit.html) in a browser.

---

## The mark

<img src="print/jpg/arant-symbol-on-ivory.jpg" alt="ARANT symbol" width="220" align="right">

**Balance.** Two equal stone slabs lean together and hold a pebble between them. The A becomes an object in balance:
architectural, tactile and quiet.

- **One opening, repeated.** The split between the slabs and the gap around the pebble share one width (5 % of the
  symbol grid). That rule is what lets the mark survive a rubber stamp, a blind deboss and a silicone mould.
- **Rounded caps and feet.** Nothing is narrower than the split, so there is nothing to chip in a mould.
- **A drawn wordmark.** ARANT is custom-drawn, never typed. Both As are the symbol itself, scaled to the cap height.
  R, N and T share its stroke (about 18 % of the cap height) and its corner radius. The N's diagonal sits at 60°.
- **DESIGN** is set at 27 % of the ARANT cap height and spaced to the exact width of ARANT.

## Logo versions

| Version                  | Preview                                                                                 | Use it for                                                          |
| ------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Horizontal** (primary) | <img src="print/jpg/arant-horizontal-on-ivory.jpg" width="260" alt="Horizontal lockup"> | Website header, packaging, documents                                |
| **Stacked**              | <img src="print/jpg/arant-stacked-on-ivory.jpg" width="150" alt="Stacked lockup">       | Labels, cards, square formats, signage                              |
| **Wordmark**             | <img src="print/jpg/arant-wordmark-on-ivory.jpg" width="220" alt="Wordmark">            | Editorial use, and where the symbol already appears                 |
| **One line**             | <img src="print/jpg/arant-one-line-on-ivory.jpg" width="260" alt="One-line lockup">     | Narrow bands: product wraps, email footers, sticky site header      |
| **ARANT only**           | <img src="print/jpg/arant-wordmark-short-on-ivory.jpg" width="200" alt="ARANT only">    | Moulded into products and on small tags, where DESIGN would fill in |
| **Symbol**               | <img src="print/jpg/arant-symbol-on-ivory.jpg" width="90" alt="Symbol">                 | Stamps, seals, product marks, social avatar, favicon                |

Use the horizontal lockup by default. Reach for the others when the space asks for it, never for variety.

## Which file do I need?

| I'm making…                               | Use                                                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A website or app                          | `logo/svg/*.svg` (or `export/<version>/*.svg` for a single colour)                                                                                      |
| A favicon and app icons                   | `export/symbol/`: `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, PWA icons, `site.webmanifest`. Paste `head-snippet.html` into the page `<head>` |
| A social profile picture                  | `export/symbol/arant-symbol-app-icon-1024.png` (ivory on earth) or `arant-symbol-square-1024.png`                                                       |
| Something for a printer                   | `print/pdf/*.pdf` (vector, opens in Illustrator, Affinity, InDesign)                                                                                    |
| A rubber stamp, deboss die or mould       | The PDF or SVG in black: `print/pdf/*-black.pdf`. Check the minimum sizes below                                                                         |
| An email, document or marketplace listing | `print/jpg/*-on-ivory.jpg`, or the transparent PNGs in `export/<version>/`                                                                              |
| A dark background                         | The `-ivory` or `-white` versions in `export/<version>/`                                                                                                |

File names end in the colour's token name: `-earth`, `-charcoal`, `-terracotta`, `-ivory`, plus `-black` and `-white`
for production. The names stay the same if a colour value is ever adjusted. PNGs come at 600, 1200 and 2400 px wide
(symbol: 64–1024 px).

## Colour

![Colour palette](guide/palette.svg)

| Name          | HEX       | RGB         | Role                                                    |
| ------------- | --------- | ----------- | ------------------------------------------------------- |
| Warm Ivory    | `#F1E9DC` | 241 233 220 | Ground for print and screen                             |
| Sand          | `#D8C3A7` | 216 195 167 | Secondary ground, tags, tissue                          |
| Earth Brown   | `#4A3527` | 74 53 39    | **Primary logo colour**                                 |
| Deep Charcoal | `#292622` | 41 38 34    | Text, signage, maximum contrast                         |
| Terracotta    | `#B85F32` | 184 95 50   | Accent: one element per piece (a seal, a band, a price) |
| Muted Olive   | `#64654A` | 100 101 74  | Supporting colour, sparingly                            |

**Approved pairings:** Earth on Ivory (9.5 : 1) · Ivory on Earth · Earth on Sand (6.7 : 1) · dark brown on kraft ·
Ivory on Charcoal (12.5 : 1) · Ivory on Terracotta (3.7 : 1, seals and large sizes only).

These values are defined in one place only: the design tokens in [`packages/tokens`](../../packages/tokens/). Every
file in this folder is generated from them. The brand guide lists starting CMYK values. Confirm CMYK and any Pantone matches on a printed proof. Ask the printer
to build the dark browns as rich blacks.

## Typography

The logo is drawn, never typed. For everything around it, use two open-licence families (SIL Open Font License,
free for commercial, print and web use) from Google Fonts:

- **[Jost](https://fonts.google.com/specimen/Jost)**: labels, navigation, product details, prices, packaging copy.
  Regular 400 and Medium 500. Uppercase labels get +0.2 em tracking.
- **[Newsreader](https://fonts.google.com/specimen/Newsreader)**: headlines, product names, stories, cards.
  Light 300 for display, Regular 400 for text. Never in all caps.

## Clear space and minimum size

Keep clear space on every side of half the ARANT cap height (for the symbol alone, a quarter of its height).
Minimum sizes follow one production rule: **every opening stays at 0.8 mm or more.**

| Version    | Screen                               | Print             | Stamp · deboss · mould · engrave                      |
| ---------- | ------------------------------------ | ----------------- | ----------------------------------------------------- |
| Horizontal | 180 px wide                          | 25 mm wide        | 82 mm wide (below that, use the symbol or ARANT only) |
| Stacked    | 120 px wide                          | 18 mm wide        | 54 mm wide                                            |
| ARANT only | 16 px cap height                     | 2.5 mm cap height | 12 mm cap height                                      |
| Symbol     | 24 px (at 16 px the split closes up) | 6 mm tall         | 12 mm tall                                            |

These are production rules of thumb. Before a first run, make one proof stamp and one test pour at the smallest size
you plan to use.

## Don't

- Stretch, squash or rotate the logo
- Close the split, move the pebble, or rearrange or resize the parts of a lockup
- Add shadows, outlines, gradients or other effects
- Recolour outside the palette
- Retype ARANT in a font
- Place the logo on busy photography without a calm area or a solid panel

## Folder layout

```
logo/svg/             masters in Earth Brown: symbol, symbol-reversed, horizontal, stacked,
                      one-line, wordmark, wordmark-short (ARANT only)
export/<version>/     one-colour SVGs (earth, charcoal, terracotta, ivory, black, white) + transparent PNGs
export/symbol/        favicon, app and PWA icons, site.webmanifest, head-snippet.html
print/pdf/            vector PDFs (Earth Brown, black, Terracotta), RGB
print/jpg/            JPGs on warm ivory
guide/                the brand guide (arant-brand-kit.html) and palette.svg
source/               Python 3 scripts that generate everything above from the tokens (no dependencies)
```

## Rebuilding the artwork

Everything in this folder is generated. The geometry lives in `source/build_logo.py` and `source/glyphs.py`, and
every colour comes from [`packages/tokens/tokens.json`](../../packages/tokens/tokens.json). To change a colour, edit
the token, then rebuild:

```bash
pnpm identity:build     # from the repo root: check, then logo → exports → print → guide
```

| Step                    | Script (in `source/`) | Writes                                                                                           |
| ----------------------- | --------------------- | ------------------------------------------------------------------------------------------------ |
| `pnpm identity:check`   | `check_tokens.py`     | Fails if a brand colour is hard-coded in the scripts                                             |
| `pnpm identity:logo`    | `build_logo.py`       | `logo/svg/` masters                                                                              |
| `pnpm identity:exports` | `build_exports.py`    | `export/`: one-colour SVGs, PNGs, favicon and app icons, `site.webmanifest`, `head-snippet.html` |
| `pnpm identity:print`   | `build_print.py`      | `print/pdf/`, `print/jpg/`                                                                       |
| `pnpm identity:guide`   | `build_guide.py`      | `guide/arant-brand-kit.html`, `guide/palette.svg`                                                |

The scripts need Python 3 and Chrome or Chromium; set `CHROME=/path/to/chrome` if it isn't on your `PATH`. The
shared helpers are `brand_tokens.py` (reads the tokens and does the colour maths) and `render.py` (headless-Chrome
rendering). No AI or EPS files are included: open any PDF in `print/pdf/` in Illustrator and save it as AI or EPS.

## Licence

See [`LICENSE`](../../LICENSE). In short:

- **Brand assets: all rights reserved.** The ARANT and ARANT DESIGN names, the Balance symbol, the wordmark and
  everything in `brand/` belong to ARANT DESIGN. Publishing them here does not grant a licence to use them. Stockists,
  press, printers and manufacturers may use them only with written permission from the studio, via
  [arantdesign.com](https://arantdesign.com).
- **Build scripts: MIT.** The code in `source/` is free to reuse. That licence doesn't extend to the artwork it generates.
