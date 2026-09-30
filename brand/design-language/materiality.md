# Materiality

How physical materials inform the visual language, and how to carry texture onto screens. Back to the
[design-language index](README.md).

---

## What ARANT should feel connected to

**Established** (guide section 06 mockups): the mark shown on terrazzo, stone, kraft and paper, applied as a blind
deboss, an engraving and a moulded maker's stamp. The mark was designed for this: nothing is narrower than the split,
so it survives a rubber stamp, a deboss and a silicone mould (identity README).

**Recommended:** stone and mineral surfaces, terrazzo, lime plaster, warm wood, uncoated paper, kraft, tactile
finishes (honed, sanded, sealed, waxed), and the subtle variation of things finished by hand.

## Refined craftsmanship, not rustic craft

| Refined craftsmanship (yes)                        | Rustic craft (no)                                      |
| -------------------------------------------------- | ------------------------------------------------------ |
| Precise forms with a soft, finished edge           | Deliberately rough, lumpy or "distressed" forms        |
| Variation that comes from the process              | Variation added as decoration                          |
| Clean typography and generous space around texture | Hand-lettering, stamps as decoration, twine and burlap |
| Honed stone, sealed plaster, uncoated paper        | Weathered boards, jute, chalkboard, mason jars         |
| Process shown clearly and calmly                   | "Artisan" theatre, sepia, heavy grain                  |

## Material-neutral by design

**Recommended.** The brand must not become a "Jesmonite brand" or a casting brand. Current products use mineral
casting materials (such as CALSO ONE), but:

- Brand-level lines, packaging and the website frame never name a material or process. "Cast", "poured" and
  "hand-cast" belong in a product's own description.
- Materials are shown, not branded: the texture of each object speaks for itself.
- Any future material (ceramic, wood, metal, glass, textile) sits in the same system without change.

The brand guide's casting-specific sample copy is flagged in the [index](README.md#open-decisions).

## Physical applications of the mark

**Established** (identity README, "Which file do I need?" and minimum sizes):

- Stamps, deboss dies and moulds use the black PDF or SVG (`print/pdf/*-black.pdf`).
- Respect the stamp, deboss, mould and engrave column of the minimum-size table in the identity README.
- Before a first run, make one proof stamp and one test pour at the smallest planned size.

**Recommended:**

- Prefer the symbol or ARANT only on objects; lockups with DESIGN are for print and packaging.
- A blind deboss or a mould mark on the underside or back, never on the object's display face unless the design
  calls for it.
- Engrave or laser-mark wood, metal and glass using the same files and the same minimum sizes.

## Texture on screen

**Recommended.** Texture comes from photography of real materials, not from simulated surfaces.

- **Use:** full-bleed photographs of material (a stone surface, a plaster wall, kraft board) as section grounds;
  detail crops in product galleries; the symbol pattern in small areas (a footer, an empty state).
- **Keep it calm:** at most one textured area per viewport. Reading text sits on flat Ivory or Sand, never on
  texture. If type must sit on an image, it sits on a calm area with enough contrast, checked.
- **Performance:** texture images are compressed, lazy-loaded below the fold, and never used as tiled CSS
  backgrounds for whole pages.
- **Avoid:** paper-grain overlays, noise filters, faux-stone CSS, skeuomorphic paper edges, torn-paper dividers,
  photographic textures behind body text.
