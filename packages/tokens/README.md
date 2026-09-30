# ARANT DESIGN · Design tokens

The single source of truth for colour, type, spacing, layout, radius and motion values, in the
[W3C Design Tokens](https://www.designtokens.org/tr/drafts/format/) format: [`tokens.json`](tokens.json).

| Group            | Tokens                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `color`          | `ivory` `#F1E9DC` · `sand` `#D8C3A7` · `earth` `#4A3527` · `charcoal` `#292622` · `terracotta` `#B85F32` · `olive` `#64654A` · `kraft` `#C4A57F` (reference only)   |
| `color.role`     | `surface.ground` · `surface.alt` · `surface.inverse` · `text.primary` · `text.secondary` · `text.muted` · `text.inverse` · `line.subtle` · `line.strong` · `accent` |
| `color.roleDark` | Optional dark theme: `surface.ground` · `surface.alt` · `text.primary` · `text.muted` · `line.subtle` · `line.strong` · `accent`                                    |
| `logo`           | `default` → earth · `reversed` → ivory · `accent` → terracotta                                                                                                      |
| `font.family`    | `sans` (Jost) · `serif` (Newsreader), with fallback stacks                                                                                                          |
| `font.weight`    | `light` 300 · `regular` 400 · `medium` 500                                                                                                                          |
| `letterSpacing`  | `label` 0.2em (uppercase Jost labels)                                                                                                                               |
| `space`          | `1`–`10`: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 144 px                                                                                                         |
| `container`      | `text` 64ch · `content` 1120px · `wide` 1440px                                                                                                                      |
| `gutter`         | `min` 20px · `preferred` 5vw · `max` 64px, used as `clamp(min, preferred, max)`                                                                                     |
| `grid`           | `columns.phone` 4 · `.tablet` 6 · `.desktop` 12; `gap.phone` → `space.4` · `.tablet` 20px · `.desktop` → `space.5`                                                  |
| `breakpoint`     | `md` 600px · `lg` 960px · `xl` 1440px (minimum widths, mobile first)                                                                                                |
| `radius`         | `none` 0px · `soft` 2px · `round` 50%                                                                                                                               |
| `border`         | `subtle` (1px, `color.role.line.subtle`) · `strong` (1px, `color.role.line.strong`); there is no shadow token                                                       |
| `duration`       | `quick` 150ms · `standard` 250ms · `gentle` 400ms                                                                                                                   |
| `easing`         | `out` (ease-out) · `inOut` (ease-in-out), as cubic Béziers                                                                                                          |
| `motion`         | `quick` · `standard` · `gentle`: transitions combining a duration and an easing                                                                                     |

The colour roles are `{alias}` references to the palette. Two light roles and four dark ones are mixes of two
palette colours (for example `text.muted` is Earth mixed 22 % towards Ivory): their `$value` is the mixed colour, and
the recipe is recorded under `$extensions["com.arantdesign"].mix`. `pnpm identity:check` fails if a recorded mix no
longer matches the palette, so after changing a palette colour, recompute those values
(`brand_tokens.recorded_mix(path)` gives the new one). How the tokens are used is explained in
[`brand/design-language/`](../../brand/design-language/README.md).

## Using them

This folder is the workspace package `@arant/tokens`. In any app or package in the repo, add it as a dependency:

```json
"dependencies": { "@arant/tokens": "workspace:*" }
```

```js
import tokens from '@arant/tokens' with { type: 'json' };
tokens.color.earth.$value; // "#4A3527"
```

The file is plain JSON, so it can also be read directly. Once the website needs CSS variables or a JS module, generate them
from this file with a tool such as [Style Dictionary](https://styledictionary.com/), and don't edit the generated
output by hand.

## Changing a value

This file is the only place a brand colour is written. Edit the value here, then run `pnpm identity:build` from the
repo root: the logo files, one-colour exports, web icons and manifest, print PDFs and JPGs, palette image, brand
guide and icon preview are all regenerated from it. `pnpm identity:check` (part of the build) fails if a colour is ever hard-coded in
the identity scripts.

The guide's interface tints and the mockups' material colours (kraft, stone) are mixed from these tokens, so they
follow a palette change too. Colour _names_ and roles live here as well, under `$description` and
`$extensions["com.arantdesign"].name`.
