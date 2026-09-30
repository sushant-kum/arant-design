# Colour

How the palette is used. Back to the [design-language index](README.md).

The values live only in [`packages/tokens/tokens.json`](../../packages/tokens/tokens.json). This file never states a
hex; it states roles and relationships. Contrast ratios below are computed from the tokens with
`tokens.contrast()` in `brand/identity/source/brand_tokens.py`, and change if a token changes.

---

## The palette

**Established** (`tokens.json` `color.*`, names from `$extensions`, roles from `$description`):

| Token              | Name          | Role (token description)                                                                     | Visual role in the system                                               |
| ------------------ | ------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `color.ivory`      | Warm Ivory    | Ground for print and screen                                                                  | The default ground; paper; reversed logo and text on dark               |
| `color.sand`       | Sand          | Secondary ground, tags, tissue                                                               | Second ground, image backdrops, pattern, tissue                         |
| `color.earth`      | Earth Brown   | Primary logo colour                                                                          | The logo; headings and emphasis; dark grounds                           |
| `color.charcoal`   | Deep Charcoal | Text, signage, maximum contrast                                                              | Running text; the darkest ground; signage                               |
| `color.terracotta` | Terracotta    | Accent: one element per piece, like a seal, a band or a rule; as text, 24 px and larger only | The single warm accent                                                  |
| `color.olive`      | Muted Olive   | Supporting colour, sparingly                                                                 | A rare secondary note: a collection, a detail, a ground in a photograph |
| `color.kraft`      | Kraft         | Reference only: typical kraft board, for mockups and contrast checks                         | Not a palette colour. Stands for the real board                         |

Logo aliases (**Established**): `logo.default` → earth (light grounds), `logo.reversed` → ivory (dark grounds),
`logo.accent` → terracotta (one-colour logo in the accent, e.g. seals).

**Kraft is reference only.** Never specify it as an ink or a screen colour. On packaging, the kraft colour is the
board itself; on screen, show real kraft in a photograph or a mockup.

## The balance

**Established:** "Earth on ivory, with one warm accent" (brand guide, section 04). The logo lives in Earth Brown or
Deep Charcoal on warm grounds. Terracotta is used for one element per piece.

**Recommended** proportions for any composition (page, post, box):

| Share   | Colours                    | Used for                                 |
| ------- | -------------------------- | ---------------------------------------- |
| ~70–85% | Warm Ivory, Sand           | Grounds, large surfaces, image backdrops |
| ~15–25% | Earth Brown, Deep Charcoal | Text, logo, rules, dark bands, footers   |
| ≤ ~5%   | Terracotta, or Muted Olive | One accent element                       |

- Terracotta and olive never appear together as accents on the same surface. Pick one.
- Neither Terracotta nor Olive is used as a large ground on screen. A seal sticker or a single band is the largest
  Terracotta area in the system.
- Photography brings its own colour; the interface around it stays neutral.

## Roles for implementation

**Established** as `color.role.*` in [`tokens.json`](../../packages/tokens/tokens.json). Each role is an `{alias}` of
a palette colour, or a mix of two recorded under `$extensions["com.arantdesign"].mix`; `pnpm identity:check` fails if
a recorded mix no longer matches the palette. Use the role, not the palette colour, in interface code.

| Token                        | Resolves to                | Notes                                                                |
| ---------------------------- | -------------------------- | -------------------------------------------------------------------- |
| `color.role.surface.ground`  | `color.ivory`              | Page background                                                      |
| `color.role.surface.alt`     | `color.sand`               | Alternating sections, image backdrops, footers                       |
| `color.role.surface.inverse` | `color.charcoal`           | Dark bands, footers, signage (Earth is also approved as a dark band) |
| `color.role.text.primary`    | `color.charcoal`           | Body and UI text                                                     |
| `color.role.text.secondary`  | `color.earth`              | Headings, emphasis, links                                            |
| `color.role.text.muted`      | `mix(earth, ivory, 0.22)`  | Metadata and captions on ivory only (5.2 : 1); not on sand (3.7 : 1) |
| `color.role.text.inverse`    | `color.ivory`              | Text on charcoal or earth                                            |
| `color.role.line.subtle`     | `mix(sand, #FFFFFF, 0.19)` | Decorative dividers only (1.3 : 1 on ivory)                          |
| `color.role.line.strong`     | `color.earth`              | Input borders, focus rings, anything interactive                     |
| `color.role.accent`          | `color.terracotta`         | One accent element                                                   |

The hairline borders built from the line roles are `border.subtle` and `border.strong` (see
[`digital.md`](digital.md#borders-radius-and-elevation)).

## Approved pairings and contrast

**Established** (identity README, "Approved pairings"; guide section 04): Earth on Ivory · Ivory on Earth · Earth on
Sand · dark brown on kraft · Ivory on Charcoal · Ivory on Terracotta (seals and large sizes only).

Contrast from the tokens (text on ground):

| Text ↓ / ground → | Ivory | Sand | Earth | Charcoal | Terracotta | Olive |
| ----------------- | ----- | ---- | ----- | -------- | ---------- | ----- |
| Ivory             | —     | 1.4  | 9.5   | 12.5     | 3.7        | 5.0   |
| Earth             | 9.5   | 6.7  | —     | 1.3      | 2.6        | 1.9   |
| Charcoal          | 12.5  | 8.8  | 1.3   | —        | 3.4        | 2.5   |
| Terracotta        | 3.7   | 2.6  | 2.6   | 3.4      | —          | 1.4   |
| Olive             | 5.0   | 3.5  | 1.9   | 2.5      | 1.4        | —     |

Earth and Charcoal on kraft: 4.9 and 6.5 : 1. The guide's kraft ink, `mix(earth, #000000, 0.20)`, reaches 5.9 : 1.

**Established** (studio decision): Terracotta is for non-text accents (a rule, a dot, a band, a seal) and for text 24 px
and larger only. Below 24 px it fails WCAG AA on every brand ground (3.69 : 1 on Ivory, 2.60 on Sand, 4.45 on white), so
small text goes in Earth or `text.muted`, with a small Terracotta rule or dot beside it where the accent matters.

**Recommended** rules (WCAG 2.2 AA):

- Body and UI text: 4.5 : 1 or more. Use Charcoal or Earth on Ivory or Sand; Ivory on Charcoal or Earth (or on a small
  Olive element, 5.0 : 1).
- Large text (24 px and up; the brand weights stop at 500, so the smaller "bold" threshold never applies): 3 : 1
  or more. Only here may Terracotta be used as a text colour on Ivory (3.7 : 1), or Ivory on Terracotta.
- Small labels, prices, links and buttons are never set in Terracotta (**Established**, above).
- Interactive boundaries (inputs, focus rings) need 3 : 1 against the ground: use Earth, not Sand.
- Sand on Ivory (1.4 : 1) is for grounds and pattern only, never for text or meaningful lines.
- Check any new pair with `tokens.contrast()` before using it.

## Light and dark contexts

- **Established:** reversed logo in Warm Ivory on dark grounds (`logo.reversed`, `arant-symbol-reversed.svg`,
  `-ivory` exports). Ivory on Charcoal is the signage pairing.
- **Established:** the optional dark theme is `color.roleDark.*` in `tokens.json`, the brand guide's own dark mixes:

  | Token                           | Resolves to                      | Guide use     |
  | ------------------------------- | -------------------------------- | ------------- |
  | `color.roleDark.surface.ground` | `mix(charcoal, #000000, 0.25)`   | Page          |
  | `color.roleDark.surface.alt`    | `color.charcoal`                 | Panels        |
  | `color.roleDark.text.primary`   | `color.ivory`                    | Text          |
  | `color.roleDark.text.muted`     | `mix(sand, charcoal, 0.18)`      | Muted text    |
  | `color.roleDark.line.subtle`    | `mix(charcoal, sand, 0.10)`      | Hairlines     |
  | `color.roleDark.line.strong`    | `color.ivory`                    | Focus, inputs |
  | `color.roleDark.accent`         | `mix(terracotta, #FFFFFF, 0.18)` | Accent        |

  The lighter accent reaches 5.2 : 1 on the dark ground. `line.strong` is Ivory, the focus colour the accessibility
  rules give for dark grounds.

- **Recommended:** light stays the default theme: the brand is Warm Ivory first. A dark theme, if offered, uses these
  tokens rather than new mixes, and the reversed logo files.

## Print

**Established** (guide section 04, identity README): CMYK values in the guide are straight RGB conversions, a
starting point only. Confirm CMYK and any Pantone match on a printed proof, against a physical Pantone guide. Ask the
printer to build the dark browns as rich blacks.

**Recommended:** for one-colour print use Earth Brown (or black for stamps and dies); for two-colour, Earth plus
Terracotta for the one accent element.

## Never

- Gradients, including subtle ones on buttons or backgrounds (**Established** for the logo; **Recommended** for
  everything else).
- New colours, tints picked by eye, or hex values typed into code. Derive shades with `tokens.mix(...)`, or add a
  token.
- Colour as the only carrier of meaning (see [`digital.md`](digital.md)).
