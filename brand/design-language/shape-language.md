# Shape language

The ARANT shape vocabulary, and where it applies. Back to the [design-language index](README.md).

---

## Where it comes from

**Established** (the mark; `brand/identity/README.md`, `build_logo.py`):

- **Slabs.** Two equal, leaning slabs: solid, architectural planes with weight.
- **The pebble.** One small rounded object, held rather than placed.
- **One opening, repeated.** The split and the pebble gap share one width (5 % of the symbol grid). Negative space is
  measured and even.
- **Softened, not rounded.** Caps and feet are rounded with a small radius (about 4 % of the cap height, roughly a
  quarter of the stroke width in the wordmark). Corners are eased; the forms stay geometric.
- **Fixed angles.** The N's diagonal is exactly 60°. Angles are chosen, not arbitrary.

**Established** (brand guide page and mockups): interface panels, swatches and tables are square-cornered with 1 px
hairline borders or flat tinted plates; roundness appears only in the objects themselves (a round coaster, a tray
with soft corners, a circular seal, an arched doorway in the signage mockup).

## The vocabulary

**Recommended:**

| Form                        | Meaning                    | Use                                                                   |
| --------------------------- | -------------------------- | --------------------------------------------------------------------- |
| Slab (a plain rectangle)    | Structure, weight, support | Image frames, sections, bands, boxes, labels                          |
| Softened corner             | Touch, the finished edge   | Small interactive elements (buttons, fields), physical products       |
| Circle / pebble             | The held object; a seal    | Seals, stamps, avatars, the hang-tag hole, swatch dots                |
| Opening / niche / threshold | Space that holds something | Framing an object in photography; generous margins around one element |
| Arch                        | Architecture, an opening   | Photography and physical space; not a UI container (see Experimental) |
| Hairline                    | A quiet edge, like a joint | Dividers, table rules, input borders                                  |

**Shape needs a reason.** Round a corner because the thing is touched or physical, not to look friendly. If there is
no reason, keep it square.

## In the interface

**Established** (`radius.*` in [`tokens.json`](../../packages/tokens/tokens.json)):

| Token          | Applies to                                                                   |
| -------------- | ---------------------------------------------------------------------------- |
| `radius.none`  | Images, sections, panels, cards, modals, menus, banners: the default         |
| `radius.soft`  | Buttons, inputs, selects, small tags: an eased edge, echoing the logo's caps |
| `radius.round` | Truly circular items only: avatar, seal, colour-swatch dot, radio button     |

**Recommended:**

- **Cards:** no container at all by default. A product card is an image, then text on the page ground. If a panel
  is needed (a note, an order summary), it is a flat Sand or tinted plate, or a hairline box, with square corners.
- **Buttons:** rectangular, `radius.soft`, generous horizontal padding. No pills.
- **Containers:** separate with space and hairlines, not shadows or rounded boxes.
- **Icons:** see [`visual-language.md`](visual-language.md#icons).
- **Never:** pill buttons, fully rounded cards, radii other than the three tokens (in particular 8 px and up on
  large surfaces), blobs, wavy dividers.

## In print, packaging and product

**Recommended:**

- **Packaging:** plain rectangular boxes and bands; circular seal stickers (the guide's seal is a circle); a hang tag
  with clipped top corners and a round hole (guide mockup). Die-cut shapes only when they have a purpose.
- **Product styling:** set objects on planes (a plinth, a slab of stone, a shelf, a niche). Let a single rounded
  object sit against straight architecture, as the pebble sits between the slabs.
- **Graphic elements:** a single hairline, a band of colour, a circle for a seal. No decorative frames.

## Experimental

- **Arch-topped image crops** (a rectangle with a full semicircular top), for a single editorial moment such as a
  journal opener. Drawn from the arched doorway in the signage mockup and from Indian architecture. Not for product
  grids or UI containers, and not in production until reviewed.
