# Layout

Containers, spacing, grids and rhythm, for screens first and print where it applies. Back to the
[design-language index](README.md).

**Status.** Containers, gutters, spacing, grid and breakpoints are **Established** as tokens in
[`packages/tokens/tokens.json`](../../packages/tokens/tokens.json) (`container.*`, `gutter.*`, `space.*`, `grid.*`,
`breakpoint.*`); the values live there and are cited here by name. How to use them (the rules, the column
relationships, the homepage example) is **Recommended**.

---

## Philosophy

- One dominant hierarchy per section (principle 1). Space separates things before lines or boxes do.
- Generous, consistent space beats clever, variable space. Pick from the scale; never nudge by eye.
- Editorial rhythm: alternate full-width images with narrower text, and wide sections with calm ones.
- Asymmetry is deliberate: an offset text column beside a large image, not random placement.
- Content, not containers, defines the page. Few cards, few panels.

## Containers

**Established** (`container.*`, `gutter.*`):

| Token               | Use                                                                            |
| ------------------- | ------------------------------------------------------------------------------ |
| `container.text`    | Reading text, product descriptions, forms (the brand guide's `p` measure)      |
| `container.content` | Default page content (the brand guide's `.wrap`)                               |
| `container.wide`    | Wide image grids and editorial spreads                                         |
| Full bleed (100vw)  | Hero photography, material close-ups, dark bands                               |
| `gutter.*`          | Side margin on every screen: `clamp(gutter.min, gutter.preferred, gutter.max)` |

Text never runs the full width of a wide container. Images may.

## Spacing scale

**Established** (`space.1`–`space.10`), a scale on a 4 px base. The guide's own gaps sit close to it.

| Token      | Typical use                                                 |
| ---------- | ----------------------------------------------------------- |
| `space.1`  | Icon to label                                               |
| `space.2`  | Label to value; tight stacks                                |
| `space.3`  | Heading to its text; card text lines                        |
| `space.4`  | Grid gap on phones; form field spacing                      |
| `space.5`  | Grid gap on desktop; image to caption group                 |
| `space.6`  | Between groups inside a section                             |
| `space.7`  | Section header to section content                           |
| `space.8`  | Section spacing on phones                                   |
| `space.9`  | Section spacing on desktop                                  |
| `space.10` | Major breaks: before the footer, between editorial chapters |

Rules (**Recommended**):

- Space between sections is always larger than space inside them, by at least one full step.
- Related things are closer together than unrelated things (a caption belongs to its image, not the next one).
- On phones, step each section-level value down one or two steps; keep inner spacing the same.
- Pick every value from the scale; never nudge by eye.

## Grid

**Established** (`grid.columns.*`, `grid.gap.*`):

| Screen  | Columns                | Gap                | Notes                                        |
| ------- | ---------------------- | ------------------ | -------------------------------------------- |
| Phone   | `grid.columns.phone`   | `grid.gap.phone`   | Mostly single column; product grids 2 across |
| Tablet  | `grid.columns.tablet`  | `grid.gap.tablet`  | The guide lays out its panels on 6 columns   |
| Desktop | `grid.columns.desktop` | `grid.gap.desktop` | Text columns span 5–7; images span 6–12      |

Column relationships that work (**Recommended**):

- **Image 7 · text 5** (or 8 · 4): the default editorial split. Text aligns to the top or the baseline of the image,
  not centred vertically by default.
- **Full-width image, then text at 6 columns offset by 1**: for collection openers.
- **Product grids: 3 across on desktop, 2 on tablet and phone**, with generous gaps. Four across only on very wide
  screens and only for large catalogues.
- Break the grid on purpose, once per page at most: a large image that spans into the margin, a single object set
  small in a large field.

Alignment:

- One shared left edge for text in a section. Centred text only for short, single-purpose moments (a thank-you line,
  a one-line collection statement).
- Images share edges with text columns; don't float them at arbitrary offsets.

## Breakpoints

**Established** (`breakpoint.*`, minimum widths, mobile first). The guide page keeps its own 860px and 480px
breakpoints; it is a generated artefact, not a website.

| Token           | Layout from that width                                     |
| --------------- | ---------------------------------------------------------- |
| (base)          | Phone: single column, `grid.columns.phone`                 |
| `breakpoint.md` | Tablet: `grid.columns.tablet`, 2-up images                 |
| `breakpoint.lg` | Desktop: `grid.columns.desktop`, split layouts             |
| `breakpoint.xl` | Wide: `container.wide` grids; more space, not more columns |

Design mobile first. Content order stays the same at every size; don't hide content on phones.

## Adaptation

- **Desktop:** split image and text layouts; generous margins; the full navigation.
- **Tablet:** splits become stacked where the text column would drop below about 40 characters.
- **Phone:** stacked, full-width images; `gutter.min` at the sides; the header shrinks to the one-line lockup or symbol plus a
  menu; sticky "add to bag" only on product pages.

## Print and packaging layout

**Recommended:** keep the same logic in print. Use the logo's clear space (half the ARANT cap height) as the minimum
margin unit on small items, and align text to one edge or centre it on one axis. See
[`packaging.md`](packaging.md).

## Example: homepage structure

**Recommended**, as an illustration of the rhythm, not a fixed template:

1. **Header:** one-line or horizontal lockup, three to five Jost links, bag.
2. **Opening image:** full-bleed photograph of one object in a considered space. One Newsreader line and one text
   link, set in a calm area of the image or below it.
3. **Collection introduction:** uppercase label, Newsreader heading, two-sentence lede at `container.text`.
4. **Selected objects:** three product cards, 3 across.
5. **Material or process story:** image 7 · text 5 split, with a Newsreader heading and one link.
6. **Journal or studio:** one feature, large image, short text.
7. **Footer:** on Sand or Charcoal; symbol or horizontal lockup; plain links; newsletter field.

Each section is separated by `space.9`; only one of them uses an accent colour.
