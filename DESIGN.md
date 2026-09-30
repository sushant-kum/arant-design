# ARANT DESIGN · Design system and design contract

The binding brief for anyone (human or AI) designing, writing or building for ARANT DESIGN. It stands alone: read it
and you can make a correct first decision about anything. Detail, reasoning and examples live in
[`brand/design-language/`](brand/design-language/README.md). Values live in the canonical sources, which this file
names but doesn't copy. When this file and a canonical source disagree, the source wins; fix this file.

Every rule is labelled:

- **Established**: backed by a file in this repo (named in each section). Changing it is a brand decision.
- **Recommended**: a logical extension of the identity that no repo file defines yet. Apply it by default, but don't
  cite it as a brand rule. Proposed values (type sizes, packaging text sizes and similar) are Recommended until
  they are tokens.
- **Experimental**: exploratory only; never in production work.

---

## Brand

**Established** (`README.md`, `brand/identity/README.md`, `build_guide.py`):

- Name: **ARANT DESIGN**. Primary display name **ARANT**; descriptor **DESIGN**. Web `arantdesign.com`, Instagram
  `@arantdesign`. Written in capitals in running text.
- Tagline: **Objects for Considered Spaces.** Always in title case with the full stop (decided by the studio). Where
  a design sets it in capitals, such as an uppercase label or the seal's ring text, the capitals replace the case.
- The mark is **Balance**: two equal stone slabs lean together and hold a pebble. Architectural, tactile and quiet.
- Identity version **v1.1**.
- Positioning statement (from the studio's brief for this design system; for "about" copy and briefings, not a
  tagline): _A contemporary Indian objects and home-design brand creating refined objects for considered spaces._

**Recommended:**

- **Material-neutral.** Current products may use CALSO ONE and other mineral casting materials, but the brand is not
  a "Jesmonite brand" or a casting brand. Everything must work as well for ceramics, wood, metal, glass, lighting,
  textiles, furniture, architectural objects and lifestyle products.
- **Indian in sensibility, contemporary in expression.** Indianness comes from architecture, materials, light and
  making, never from applied motifs (mandalas, lotus, paisley, temple silhouettes and the like).
- Personality: considered, warm, tactile, architectural, calm, understated, human. Never flashy, ornate, rustic,
  cute, sterile, corporate or "craft market".

**Open decision** (don't resolve it in work; see
[`brand/design-language/README.md`](brand/design-language/README.md#open-decisions)): the casting-specific sample
copy in the brand guide. The tagline wording, label tracking and small Terracotta text are resolved (above, and in
Typography and Colour).

## Brand principles

**Recommended** wording of **Established** qualities. Detail and per-medium rules:
[`principles.md`](brand/design-language/principles.md).

1. **One idea, held in balance.** One dominant element per composition; the rest supports it. Asymmetry only when
   the weights still balance.
2. **Space is part of the material.** Whitespace is active. Never fill space because it is there.
3. **The object leads.** Products and materials carry the expression; the identity stays small and quiet.
4. **Structure before ornament.** Alignment, planes, proportion and hairlines instead of decoration.
5. **Warm through material, not effects.** Warm grounds, real textures and daylight; no gradients, glows or shadows.
6. **Made to last.** A small, stable vocabulary; nothing trend-led; nothing tied to one material or category.

When a request is ambiguous, choose the option that is more consistent, clearer, more timeless, more tactile, less
decorated and more scalable to future categories.

## Visual signature

**Established** (guide sections 04–07): warm grounds, Earth Brown logo and type, one Terracotta accent, a geometric
sans with an editorial serif, and objects shown on their own surfaces (stone, terrazzo, kraft, paper).

Graphic elements are few (**Established**, guide): the symbol pattern (below), a colour band, a circular seal,
hairline rules, and flat tinted plates. **Recommended:** no other patterns, illustrations or decorative icons.

- **Icons** (**Established**, `brand/identity/icons/`): 17 line icons on a 24 px grid, one 1.5 stroke, rounded caps and
  joins, `currentColor`, drawn from the mark's slab, pebble and arch. At 16 px use stroke-width 2, at 20 px 1.75.
  Words first; the symbol is never an icon.

- **Symbol as texture** (**Established**, guide section 07): repeat the symbol on a loose grid, every second one
  upside down, in Sand on Ivory or Ivory on Sand, at least three times smaller than any logo on the same surface. For
  tissue, box liners and web backgrounds. **Recommended:** on the web, small areas only (a footer band, an empty
  state), never behind reading text.

Detail: [`visual-language.md`](brand/design-language/visual-language.md).

## Logo

The logo is separate from the wider visual system: it is fixed artwork, placed, never rebuilt.

**Established** (`brand/identity/README.md`, `build_guide.py`):

| Version                  | Master (`brand/identity/logo/svg/`) | Use it for                                                |
| ------------------------ | ----------------------------------- | --------------------------------------------------------- |
| **Horizontal** (primary) | `arant-horizontal.svg`              | Website header, packaging, documents                      |
| **Stacked**              | `arant-stacked.svg`                 | Labels, cards, square formats, signage                    |
| **Wordmark**             | `arant-wordmark.svg`                | Editorial use, and where the symbol already appears       |
| **One line**             | `arant-one-line.svg`                | Narrow bands: product wraps, email footers, sticky header |
| **ARANT only**           | `arant-wordmark-short.svg`          | Moulded into products, small tags                         |
| **Symbol**               | `arant-symbol.svg`                  | Stamps, seals, product marks, social avatar, favicon      |
| **Symbol · reversed**    | `arant-symbol-reversed.svg`         | The same drawing in Warm Ivory, for dark grounds          |

- Use the horizontal lockup by default; the others when the space asks for it, never for variety.
- **Files for each job** (web, favicon, social, print, stamp, dark ground): the "Which file do I need?" table in
  `brand/identity/README.md`. One-colour exports are `brand/identity/export/<version>/arant-<version>-<token>.svg|png`,
  named by token (`earth`, `charcoal`, `terracotta`, `ivory`, plus `black` and `white` for production). Vector print
  files: `brand/identity/print/pdf/`. Web icons: `brand/identity/export/symbol/`.
- **Monochrome and reversed:** the logo works in one colour. On light grounds use Earth Brown or Deep Charcoal; on
  dark grounds the `-ivory` or `-white` files. There is no separate small-size or thinned reversed drawing.
- **Physical:** stamps, deboss dies, moulds and engraving use the black PDF or SVG (`print/pdf/*-black.pdf`).
  Proof one stamp and one test pour at the smallest planned size before a first run.
- **Clear space:** half the ARANT cap height on every side (a quarter of its height for the symbol alone).
- **Minimum size:** every opening stays at 0.8 mm or more. The size table (screen, print, stamp · deboss · mould ·
  engrave) is in `brand/identity/README.md` and `build_guide.py`, with a row for every lockup; read it there, don't
  copy it.

**Don't** (**Established**, `brand/identity/README.md`, guide section 08): stretch, squash or rotate the logo; close
the split, move the pebble, or rearrange or resize the parts of a lockup; add shadows, outlines, gradients or other
effects; recolour outside the palette; retype ARANT in a font; place the logo on busy photography without a calm area
or a solid panel.

## Colour

**Established** (`packages/tokens/tokens.json`; roles are the tokens' `$description`):

| Token              | Name          | Role                                                                                         |
| ------------------ | ------------- | -------------------------------------------------------------------------------------------- |
| `color.ivory`      | Warm Ivory    | Ground for print and screen                                                                  |
| `color.sand`       | Sand          | Secondary ground, tags, tissue                                                               |
| `color.earth`      | Earth Brown   | Primary logo colour                                                                          |
| `color.charcoal`   | Deep Charcoal | Text, signage, maximum contrast                                                              |
| `color.terracotta` | Terracotta    | Accent: one element per piece, like a seal, a band or a rule; as text, 24 px and larger only |
| `color.olive`      | Muted Olive   | Supporting colour, sparingly                                                                 |
| `color.kraft`      | Kraft         | Reference only: mockups and contrast checks, not palette                                     |

- Logo aliases: `logo.default` → earth, `logo.reversed` → ivory, `logo.accent` → terracotta.
- Values live only in `tokens.json`. Never write a hex elsewhere; import the tokens. Derived shades are
  `tokens.mix(...)` of palette colours (`brand_tokens.py`), never new literals.
- Approved pairings: Earth on Ivory (9.5 : 1) · Ivory on Earth · Earth on Sand (6.7 : 1) · dark brown on kraft ·
  Ivory on Charcoal (12.5 : 1) · Ivory on Terracotta (3.7 : 1, seals and large sizes only).
- Terracotta is for non-text accents (a rule, a dot, a band, a seal) and for text 24 px and larger only. Below 24 px it
  fails WCAG AA on every brand ground (3.69 : 1 on Ivory, 2.60 on Sand, 4.45 on white), so small text goes in Earth or
  `text.muted`, with a small Terracotta rule or dot beside it where the accent matters (studio decision).
- Kraft is the board itself; never specify it as an ink or a screen colour.
- CMYK in the guide is a starting point only; confirm CMYK and Pantone on a printed proof.
- No gradients.

**Established** (`tokens.json` `color.role.*`, `color.roleDark.*`; detail:
[`colour.md`](brand/design-language/colour.md#roles-for-implementation)):

- **Roles:** interface code uses the role tokens, not palette colours: `surface.ground` (Ivory), `surface.alt`
  (Sand), `surface.inverse` (Charcoal), `text.primary` (Charcoal), `text.secondary` (Earth), `text.muted` (an
  Earth–Ivory mix, on Ivory only), `text.inverse` (Ivory), `line.subtle` (decorative only), `line.strong` (Earth:
  inputs and focus), `accent` (Terracotta). Mixes are recorded in the token and checked by `pnpm identity:check`.
- **Dark theme** (optional): `color.roleDark.*`, the guide's dark mixes, with the reversed logo files.

**Recommended:**

- **Balance:** Warm Ivory and Sand for large surfaces (about 70–85 %); Deep Charcoal and Earth Brown for text, logo,
  rules and dark bands (about 15–25 %); **one** Terracotta or Muted Olive accent element (about 5 % or less), never
  both on one surface, never a large screen ground.
- Light is the default theme.

## Typography

**Established** (`tokens.json` `font.*`, `letterSpacing.label`; `brand/identity/README.md`; guide section 05):

| Token               | Family     | Use                                                         | Weights                                                         |
| ------------------- | ---------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| `font.family.sans`  | Jost       | Labels, navigation, product details, prices, packaging copy | `font.weight.regular` 400, `font.weight.medium` 500             |
| `font.family.serif` | Newsreader | Headlines, product names, stories, cards, editorial         | `font.weight.light` 300 display, `font.weight.regular` 400 text |

- Jost is primary, Newsreader secondary. Use the token fallback stacks. Both SIL OFL 1.1, from Google Fonts; load
  Newsreader with its `opsz` axis, as the guide does.
- Every uppercase Jost label takes `letterSpacing.label` (0.2em), read from the token, never typed as a literal
  (studio decision). Only ring text fitted to a circle (seal, maker's stamp) and lowercase or mono text are exempt.
  **Newsreader is never set in all caps.**
- No other typefaces for brand communication. (The guide loads IBM Plex Mono for code samples only.)

**Recommended** (detail and type roles: [`typography.md`](brand/design-language/typography.md)):

- **Jost** for everything functional: navigation, buttons, labels, forms, prices, specifications, UI body copy.
  **Newsreader** for headlines, product and collection names, introductions and long-form stories. Never Newsreader
  for buttons, navigation, forms, prices or uppercase labels.
- Hierarchy from size, weight and space, not colour or boxes. One display headline per view.
- Body text 16 px or more (the guide sets Jost 16/1.6), reading measure about 64ch; nothing below 12 px, and 12–13 px
  only for uppercase labels. No bold 700.
- On screen, Newsreader Light for about 21 px and up (headings: `clamp(30px, 4.4vw, 44px)` / 1.1 in the guide);
  Regular below that.
- Sentence case for headlines; title case for product and collection names; uppercase only in short Jost labels.

## Layout

**Established** (`tokens.json` `container.*`, `gutter.*`, `space.*`, `grid.*`, `breakpoint.*`; detail and the
homepage example: [`layout.md`](brand/design-language/layout.md)):

- **Containers:** `container.text` for reading text, `container.content` for pages, `container.wide` for image
  grids; full-bleed images. Page gutter `clamp(gutter.min, gutter.preferred, gutter.max)`.
- **Spacing:** `space.1`–`space.10`, a 4 px-based scale. Section spacing `space.9` on desktop and `space.8` on phones.
- **Grid:** `grid.columns.*` and `grid.gap.*` for phone, tablet and desktop.
- **Breakpoints:** `breakpoint.md`, `.lg`, `.xl`; mobile first. The guide keeps its own breakpoints for its page.

**Recommended:**

- One dominant hierarchy per section; generous section spacing; restrained borders; few decorative elements.
- Section spacing is always larger than any spacing inside a section. Never pick a value by eye.
- Default editorial split 7 · 5 (image · text). Product grids 3 across on desktop, 2 on tablet and phone.
- One shared left edge for text; centre only short, single-purpose lines. Break the grid deliberately, once per page
  at most.

## Shape language

**Established** (the mark and the guide): slabs, one pebble, one repeated opening, softened (not rounded) caps and
feet, fixed angles (the 60° N). The guide's interface panels are square with 1 px hairlines; roundness appears only in
objects (a round coaster, a circular seal, an arched doorway).

**Established** (`tokens.json` `radius.*`): `radius.none` for images, sections, panels, cards and modals;
`radius.soft` for buttons, inputs and small tags; `radius.round` only for circles (avatar, seal, swatch dot, radio).

**Recommended** (detail: [`shape-language.md`](brand/design-language/shape-language.md)):

- Shape needs a reason: round a corner because the thing is touched or physical.
- **No rounded cards, no pill buttons,** no blobs or wavy dividers. Cards have no container: an image, then text.
- **Experimental:** arch-topped image crops for a single editorial moment.

## Photography

No photography is in the repo yet. **Recommended** (detail and shot list:
[`photography.md`](brand/design-language/photography.md)):

- **The product is the hero.** One clear subject, negative space, editorial framing, one material close-up per
  product.
- **Light:** natural daylight or one soft directional source; soft-edged shadows; warm-neutral white balance.
- **Surfaces:** honed stone, lime or clay plaster, terrazzo, warm wood, paper, kraft, architectural details (a niche,
  a step, a threshold).
- **Styling:** objects placed as they would be used in a considered interior; one or two quiet props at most.
- **Avoid:** studio strobes, pure-white sweeps (except marketplace listings), heavy HDR, filters, stock imagery,
  prop clutter, glossy e-commerce clichés. Correct colour; don't grade it.

## Materiality

**Established** (guide section 06; identity README): the mark on terrazzo, stone, kraft and paper, as a blind
deboss, an engraving and a moulded maker's stamp; built so nothing is narrower than the split.

**Recommended** (detail: [`materiality.md`](brand/design-language/materiality.md)):

- Refined craftsmanship, never rustic craft: precise forms with finished edges; variation from the process, not
  added as decoration; no burlap, twine, chalkboard or "artisan" theatre.
- Name materials and processes ("cast", "turned") only in a product's own description.
- **Texture on screen** comes from photographs of real materials: at most one textured area per viewport, never
  behind reading text; no grain overlays, faux stone or paper effects.

## Packaging

**Established** (guide section 06; identity README): kraft box with one-colour print and a Terracotta band; hang
tag; Terracotta seal sticker with the reversed symbol; tissue in the Sand pattern with an Earth Brown band carrying
the one-line lockup; thank-you card; business card; signage in Ivory on Charcoal. Stamps and dies from the black
files, above the stamp minimum sizes. Mockups place the logo from `brand/identity/`; example names and prices are
marked as examples (`brand/mockups/README.md`).

**Recommended** (detail, pieces and label example: [`packaging.md`](brand/design-language/packaging.md)):

- One mark, one message, one accent per surface. Kraft, ivory stock and corrugated board; one- or two-colour print
  (Earth, plus Terracotta for one element), rubber stamp, or blind deboss. No foil, lamination or spot UV.
- On kraft, print dark brown (Earth, or the guide's `mix(earth, #000000, 0.20)`).
- Logo small, once per face, with clear space. Information in Jost; only the product name in Newsreader.
- Operationally realistic: stock box sizes, short runs, hand-applied labels and seals. Include the statutory
  declarations required for retail packs in India, confirmed with an advisor.

## Digital / UI

**Established** (`apps/website/README.md`; guide website mockup):

- Colour and type come from `@arant/tokens` (`workspace:*`); generate CSS variables or JS from `tokens.json`; never
  hard-code hex values or font names; no parallel token system.
- Header logo: `arant-one-line.svg` or `arant-horizontal.svg`. Icons, manifest and `head-snippet.html` from
  `brand/identity/export/symbol/`.
- Guide mockup: one-line lockup left, uppercase Jost navigation right, a hairline below the bar.
- Tokens for colour roles, spacing, layout, `radius.*`, `border.subtle` and `border.strong` (hairlines), and
  `motion.quick`, `.standard` and `.gentle` (hover; drawers and menus; image cross-fades). There is no shadow token.
- Icons from `brand/identity/icons/` (SVG files or `sprite.svg`).

**Recommended** (detail for every component: [`digital.md`](brand/design-language/digital.md)):

- A design studio's site, not a template: typography, large photography, whitespace, few quiet components.
- **Buttons:** Charcoal or Earth fill with Ivory Jost 500 uppercase label, `radius.soft`, at least 48 px high; one
  primary per view. Secondary: 1 px Earth border. Tertiary: a text link.
- **Links:** text colour with a 1 px underline. Hover is a colour or underline change; never a lift, scale or shadow.
- **Product card:** a 4:5 image with square corners and no border, then name (Newsreader 400), material and size
  (Jost, muted), price (Jost). No container, badges or overlays.
- **Product page:** large gallery; the name as the only display line; one "Add to bag"; details in Jost; a plain note
  that hand-finished pieces vary.
- **Forms:** visible labels above fields; 1 px Earth borders; errors in text, not colour alone.
- **Modals:** only for the bag drawer, mobile menu, image zoom and confirmations; no arrival pop-ups.
- **Elevation:** none. Separate layers with colour and hairlines. The guide's shadows render physical objects in
  mockups; they are not a UI pattern.
- **Motion:** use the `motion.*` tokens; fades and short slides only; no parallax, bounce or scroll-jacking.
- **Never:** gradients, glassmorphism, blur, drop shadows, pills, oversized rounded containers, auto-carousels,
  marquees, countdowns, fake scarcity.

## Social

**Established** (identity README; guide Instagram mockup): the profile picture is
`export/symbol/arant-symbol-app-icon-1024.png` (ivory on earth) or `arant-symbol-square-1024.png`; the bio reads
"ARANT DESIGN · Objects for Considered Spaces. · Small-batch, hand-finished in India."

**Recommended** (detail, formats and carousel structure: [`social.md`](brand/design-language/social.md)):

- The feed is the brand world, not a catalogue: about four in five posts are photographs with no type.
- Designed tiles: Ivory or Sand ground, an uppercase Jost label, one Newsreader Light line, at most one accent, the
  symbol small and optional.
- The logo only on launch covers, designed graphics and the carousel close, never on every post.
- Carousels: cover → context → material → use → making → information → close.
- **Established** (studio decision): the close frame shows the stacked lockup, arantdesign.com and @arantdesign
  (in Jost, the handle below the site), with no tagline
  ([`social.md`](brand/design-language/social.md#close-frame)).

**Established** (`brand/social/`, rendered by `pnpm identity:social`): the working sizes (feed 1080 × 1350, story and
reel cover 1080 × 1920 with the top and bottom 250 px kept clear) and the templates for designed tiles, photo frames,
the information and close frames, stories and reel covers. New posts are entries in `brand/social/posts.json`; sample
posts carry a SAMPLE band and are never posted.

## Voice & copy

**Established** (identity README; guide mockups): "Objects for Considered Spaces." · "Thank you for giving this
object a place in your home." · "Small-batch, hand-finished in India." · prices written `₹1,800` · British English
(`cspell.json`).

**Recommended** (detail, naming and examples: [`voice-and-copy.md`](brand/design-language/voice-and-copy.md)):

- Thoughtful, clear, concise, confident, warm, contemporary, understated. Write about form, material, object, space,
  use, process, detail and intention.
- No hype, luxury superlatives ("stunning", "must-have", "elevate"), fake scarcity, clichés, jargon, exclamation
  marks or piles of adjectives.
- Materials and processes ("cast", "hand-cast") at product level only, never in brand-level lines.
- Only claim "handmade" or "small-batch" where true. Specific facts over adjectives: `32 × 18 cm`, `1.2 kg`.
- Example: "A low tray with the weight of stone, for the things you set down at the door." CTA: "View the
  collection", not "Shop now!".

## Do / Don't

The full review table is [`do-and-dont.md`](brand/design-language/do-and-dont.md). The essentials:

| Do                                                            | Don't                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| Place generated logo files; horizontal lockup by default      | Retype, redraw, stretch, recolour or add effects to the logo          |
| Ivory or Sand grounds; Charcoal or Earth text; one accent     | Terracotta and Olive together; Terracotta text under 24 px; gradients |
| Jost for function, Newsreader for headlines and stories       | Newsreader in capitals; a third typeface; bold 700                    |
| One dominant element per section; generous, scale-based space | Dense grids, card walls, filling space for its own sake               |
| Square images and panels; `radius.soft` on controls           | Pills, rounded cards, shadows, glassmorphism                          |
| Daylight, real surfaces, one subject, true colour             | Studio strobes, filters, stock images, prop clutter                   |
| Kraft and ivory stock, one-colour print, a seal or band       | Foil, lamination, full-bleed print, a logo on every face              |
| Photography-led social feed                                   | A logo on every post; "SALE" bursts; trend effects                    |
| Specific, calm copy about the object                          | Hype, "luxury", fake scarcity, process words in brand lines           |
| Indianness through architecture, material, light and making   | Mandalas, lotus, paisley, temple silhouettes as signifiers            |

## Accessibility

**Recommended** (WCAG 2.2 AA as the floor). Aesthetics never override these:

- **Contrast:** 4.5 : 1 for body and UI text, 3 : 1 for text 24 px and larger (the brand weights stop at 500, so the
  bold exception never applies) and for interactive boundaries and focus indicators. Check every new pair with
  `tokens.contrast()`. Terracotta text is 24 px and larger only (**Established**, see Colour); Sand on Ivory (1.4 : 1)
  is never text or a meaningful line; the muted text mix is for Ivory grounds only. Contrast table:
  [`colour.md`](brand/design-language/colour.md#approved-pairings-and-contrast).
- **Readable type:** body at 16 px or more, line height about 1.5–1.6, measure about 64ch, nothing below 12 px; text
  resizes to 200 % without loss.
- **Focus:** a visible focus ring on every interactive element, for example a 2 px Earth outline with a 2 px offset
  (Ivory on dark grounds). Never remove outlines without a replacement.
- **Targets:** at least 24 × 24 px (the AA minimum); aim for 44 × 44 px, and 48 px high for buttons and inputs.
- **Alt text:** describe the object, its material and setting ("Sand-coloured tray on a stone console, holding a
  set of keys"). Decorative images, including the symbol pattern, get empty alt. The logo's alt is "ARANT DESIGN".
- **Not colour alone:** errors, states, selected options and colour swatches also carry text, an icon or a shape.
- **Motion:** respect `prefers-reduced-motion`; nothing flashes; nothing auto-plays with sound; carousels never
  auto-advance.
- **Structure:** semantic HTML, one `h1` per page, labelled landmarks and form fields, keyboard access for every
  control, focus management in dialogs.

## Canonical sources

When sources disagree, the higher one wins. Don't silently override a canonical source.

| Rank | Source                                                       | Holds                                                  | Edit it?                              |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------- |
| 1    | `brand/identity/logo/`, `export/`, `print/`, `guide/`        | Approved identity artwork and the brand guide          | **No: generated.** Rebuild instead    |
| 2    | [`packages/tokens/tokens.json`](packages/tokens/tokens.json) | Every colour, font family, weight and label tracking   | Yes, then `pnpm identity:build`       |
| 3    | [`brand/identity/README.md`](brand/identity/README.md)       | Logo usage, files, clear space, minimum sizes, don'ts  | Yes, by hand                          |
| 4    | `DESIGN.md` (this file)                                      | The AI-facing, repository-wide design contract         | Yes                                   |
| 5    | [`brand/design-language/`](brand/design-language/README.md)  | Detailed design-language rules, reasoning and examples | Yes                                   |
| 6    | `brand/mockups/` (planned) and the guide's "In use" mockups  | Examples                                               | Mockups yes; the guide via its source |
| 7    | Assumptions                                                  | State them and mark them Recommended                   | —                                     |

Editable identity source: `brand/identity/source/` (`build_logo.py` and `glyphs.py` hold the geometry;
`build_guide.py` the guide; `brand_tokens.py` reads the tokens). Build mechanics, logo invariants and linting are in
[`CLAUDE.md`](CLAUDE.md).

**Generated, never edited by hand:** everything in `brand/identity/logo/`, `brand/identity/export/`,
`brand/identity/print/`, `brand/identity/guide/`, `brand/identity/icons/`, `brand/social/templates/` and
`brand/social/posts/`. Change `brand/identity/source/*.py` or `tokens.json`, then run
`pnpm identity:build`.

## Implementation rules

**Established** (`CLAUDE.md`, `apps/website/README.md`):

- Read colours, type, spacing, layout, radius and motion from the tokens (`@arant/tokens`, or `brand_tokens.py` in the
  build scripts). Never type a palette hex; `pnpm identity:check` fails on one in the scripts. Derive shades with
  `tokens.mix(...)`.
- Reference logo files from `brand/identity/` (or copy them in a build step); never commit edited copies elsewhere.
- Logo geometry and its invariants (the split, pebble clearance, A = symbol, the 60° N) are brand decisions; don't
  change them unless asked. If tokens or geometry change, update the hand-written hex values and minimum sizes in the
  READMEs and `build_guide.py`.
- Brand assets are all rights reserved (`LICENSE`).

**Recommended:**

- **Add a token before using a new value.** The tokens cover colour and colour roles, type, spacing, containers,
  gutters, grid, breakpoints, radius, borders and motion (listed in
  [`packages/tokens/README.md`](packages/tokens/README.md)). Type sizes and roles
  ([`typography.md`](brand/design-language/typography.md)) are not tokens yet.

- Compose from a few components (header, footer, button, link, product card, grid, gallery, form field, drawer); no
  one-off styling that contradicts them.
- Mobile first; the same content and order at every size.
- Mark example product names and prices as examples.

## AI agent checklist

Before shipping any design, copy or code, confirm:

**Identity**

- [ ] The logo is a generated file from `brand/identity/`, the right version for the space, not retyped or redrawn.
- [ ] Clear space and minimum size are respected; reversed files on dark grounds; no effects.

**Colour**

- [ ] Every colour comes from `tokens.json` or a `tokens.mix(...)` of it; no new hex values.
- [ ] Ivory or Sand grounds, Charcoal or Earth text; one Terracotta or Olive accent at most; no gradients.
- [ ] Text pairs pass 4.5 : 1 (3 : 1 for 24 px and larger); `color.kraft` is not used as an ink or screen colour.

**Typography**

- [ ] Jost for function, Newsreader for headlines and stories; no other faces; weights 300, 400, 500 only.
- [ ] No all-caps Newsreader; uppercase Jost labels use `letterSpacing.label`; body 16 px or more.

**Layout and shape**

- [ ] One dominant element per section; spacing from the scale; generous section spacing; readable measure.
- [ ] Square images and panels; no pills, rounded cards or shadows; responsive and mobile first.

**Visual language**

- [ ] Warm, tactile, architectural, restrained: the product or material is the hero; the identity stays quiet.
- [ ] No generic luxury or SaaS patterns; no stereotypical Indian motifs.
- [ ] Works in monochrome where the application needs it (stamp, deboss, one-colour print).
- [ ] Nothing ties the brand to one material, process or category.

**Copy**

- [ ] Calm, specific, British English; no hype or fake scarcity; process words only at product level.

**Implementation**

- [ ] Accessible: contrast, focus, targets, alt text, not colour alone, reduced motion, semantic HTML.
- [ ] Token-driven with no duplicated design-system values; proposed values added as tokens first.
- [ ] No generated file under `brand/identity/{logo,export,print,guide,icons}/` or `brand/social/{templates,posts}/`
      edited by hand.
- [ ] New guidance labelled Recommended or Experimental, never presented as Established.
