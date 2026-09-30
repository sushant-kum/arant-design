# ARANT DESIGN · Design tokens

The single source of truth for colour and type values, in the
[W3C Design Tokens](https://www.designtokens.org/tr/drafts/format/) format: [`tokens.json`](tokens.json).

| Group           | Tokens                                                                                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `color`         | `ivory` `#F1E9DC` · `sand` `#D8C3A7` · `earth` `#4A3527` · `charcoal` `#292622` · `terracotta` `#B85F32` · `olive` `#64654A` · `kraft` `#C4A57F` (reference only) |
| `logo`          | `default` → earth · `reversed` → ivory · `accent` → terracotta                                                                                                    |
| `font.family`   | `sans` (Jost) · `serif` (Newsreader), with fallback stacks                                                                                                        |
| `font.weight`   | `light` 300 · `regular` 400 · `medium` 500                                                                                                                        |
| `letterSpacing` | `label` 0.2em (uppercase Jost labels)                                                                                                                             |

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
repo root: the logo files, one-colour exports, web icons and manifest, print PDFs and JPGs, palette image and brand
guide are all regenerated from it. `pnpm identity:check` (part of the build) fails if a colour is ever hard-coded in
the identity scripts.

The guide's interface tints and the mockups' material colours (kraft, stone) are mixed from these tokens, so they
follow a palette change too. Colour _names_ and roles live here as well, under `$description` and
`$extensions["com.arantdesign"].name`.
