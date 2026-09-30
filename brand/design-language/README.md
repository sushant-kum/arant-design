# ARANT DESIGN · Design language

How the brand looks, behaves and speaks beyond the logo. Part of the
[ARANT DESIGN monorepo](../../README.md).

The short, stand-alone contract is [`DESIGN.md`](../../DESIGN.md) at the repo root: read it first. The files here
hold the reasoning, detail and examples behind each of its sections. They don't repeat values that live elsewhere:

- Colour and type values: [`packages/tokens/tokens.json`](../../packages/tokens/tokens.json).
- Logo artwork, clear space, minimum sizes and misuse: [`brand/identity/`](../identity/) and its
  [README](../identity/README.md).

## Status labels

Every rule in this folder carries one of three labels.

| Label            | Means                                                                                                   | How to use it                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Established**  | Backed by a file in this repo: the identity artwork, the tokens, the identity README or the brand guide | Follow it. Changing it is a brand decision                                   |
| **Recommended**  | A logical extension of the identity that no repo file defines yet                                       | Apply it by default. Don't cite it as a brand rule; promote it once approved |
| **Experimental** | An exploratory direction                                                                                | Use only in explorations, never in production work                           |

Proposed values (type sizes, packaging text sizes and similar) are **Recommended** until they are added to
`tokens.json`. Spacing, layout, radius, borders, motion and colour roles are tokens now, and **Established**. Don't copy
them into app code as if they were tokens; add the token first.

## Contents

| File                                       | Covers                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------- |
| [`principles.md`](principles.md)           | Six principles, each translated into visual, UI, packaging and photography rules      |
| [`visual-language.md`](visual-language.md) | The visual signature, the symbol pattern, graphic elements, icons, Indian sensibility |
| [`colour.md`](colour.md)                   | Colour roles, balance, pairings, contrast, dark contexts                              |
| [`typography.md`](typography.md)           | Jost and Newsreader: roles, hierarchy, casing, spacing, responsive type               |
| [`layout.md`](layout.md)                   | Containers, spacing, grids, section rhythm, breakpoints                               |
| [`shape-language.md`](shape-language.md)   | The shape vocabulary and how it applies to UI, packaging and product styling          |
| [`photography.md`](photography.md)         | Light, surfaces, composition, styling, crops                                          |
| [`materiality.md`](materiality.md)         | How materials inform the look, and how to use texture on screen                       |
| [`packaging.md`](packaging.md)             | Cartons, boxes, tissue, bands, labels, stickers and cards                             |
| [`digital.md`](digital.md)                 | Components and behaviour for arantdesign.com                                          |
| [`social.md`](social.md)                   | Instagram: profile, posts, carousels, reels, launches                                 |
| [`voice-and-copy.md`](voice-and-copy.md)   | Tone of voice, naming and copy examples                                               |
| [`do-and-dont.md`](do-and-dont.md)         | A review checklist with specific examples                                             |

## Open decisions

These are not settled. Don't resolve them in work; flag them to the studio.

1. **Casting-specific sample copy in the brand guide.** `brand/identity/source/build_guide.py` uses "Cast by hand,
   finished slowly." (type sample), "HANDCAST IN INDIA" (maker's stamp ring), "poured in small batches from a mineral
   composite" (hierarchy sample) and "cast terrazzo tray" (a caption). These tie brand-level examples to one process.
   They are samples, not brand lines; don't reuse them at brand level.

### Resolved

- **Tagline** (resolved by the studio). The final tagline is **Objects for Considered Spaces.**, in title case with
  the full stop. It replaces both earlier forms, "Objects for considered spaces." (identity README, brand guide,
  Instagram bio) and "Contemporary objects for considered spaces." (the brand agent brief). Where a design sets it in
  capitals (an uppercase label, the seal's ring text), the capitals replace the case.
- **Label tracking** (resolved by the studio). Every uppercase Jost label uses `letterSpacing.label` (0.2em), read
  from the token and never written as a literal. The brand guide and the Instagram templates now do so. The only
  exceptions are ring text fitted to a circle (the seal and the maker's stamp), and lowercase or mono text. See
  [`typography.md`](typography.md#letter-spacing).
- **Small Terracotta text** (resolved by the studio). Terracotta is for non-text accents (a rule, a dot, a band, a seal)
  and for text 24 px and larger only. Below 24 px it fails WCAG AA on every brand ground (3.69 : 1 on Ivory, 2.60 on
  Sand, 4.45 on white), so small text goes in Earth or `text.muted`, with a small Terracotta rule or dot beside it where
  the accent matters. The brand guide now follows this. See [`colour.md`](colour.md#approved-pairings-and-contrast).

## Maintaining this folder

- Keep `DESIGN.md` concise; put detail here and link to it.
- When a Recommended rule is approved, change its label to Established, name its source, and update `DESIGN.md`.
- When a proposed value becomes a token, delete the number from these docs and cite the token instead.
- British English. Formatting follows the repo Prettier config.
