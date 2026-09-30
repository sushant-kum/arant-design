# Social

How the design language carries onto Instagram (`@arantdesign`). Back to the [design-language index](README.md).

The feed is an extension of the brand world, not a catalogue: rooms, materials, making and objects in use, with the
occasional clear product announcement.

---

## Profile

**Established** (identity README "Which file do I need?"; guide Instagram mockup):

- Profile picture: `brand/identity/export/symbol/arant-symbol-app-icon-1024.png` (ivory symbol on earth) or
  `arant-symbol-square-1024.png`.
- Bio, as shown in the guide mockup: "ARANT DESIGN · Objects for Considered Spaces. · Small-batch, hand-finished in
  India."
- The guide's feed mockup mixes terrazzo, flat palette colours and ivory in a 3 × 3 grid. It is a colour study, not
  a template.

## Feed principles

**Recommended:**

- **Mostly photography.** About four in five posts are photographs with no type on them. Graphics are the exception.
- **Rhythm over uniformity.** Alternate wide in-context images, close material details and quieter frames. Avoid
  running the same crop or background three times in a row.
- **No logo on every post.** The profile carries the brand. Put the symbol on launch covers and designed graphics
  only, small, in a corner or bottom centre, with its clear space. The carousel close frame is the one place a
  lockup appears in the feed (see [Close frame](#close-frame)).
- **Palette discipline.** Designed tiles use Ivory or Sand grounds, Earth or Charcoal type, and at most one
  Terracotta or Olive element.

## Formats

**Established** (the working sizes `pnpm identity:social` renders; templates and posts in
[`brand/social/`](../social/README.md)):

| Format       | Size                         | Notes                                                                  |
| ------------ | ---------------------------- | ---------------------------------------------------------------------- |
| Feed post    | 1080 × 1350 (4:5)            | Default; keep key content inside the centre 1:1 area for grid previews |
| Carousel     | 1080 × 1350 per frame        | Up to about 8 frames                                                   |
| Reel / story | 1080 × 1920 (9:16)           | Keep text out of the top and bottom ~250 px (app UI)                   |
| Reel cover   | 1080 × 1920, safe centre 4:5 | Must read in the 4:5 and 1:1 crops; the title sits in the centre 1:1   |

The profile picture is the existing symbol file (above); no separate 1:1 tile is needed. Check current platform
specifications before producing a series; they change.

## Templates

**Established** as rendered templates in [`brand/social/templates/`](../social/README.md) (each with a `-guides.png`
showing its safe areas); new posts are entries in `brand/social/posts.json`.

**Designed post** (announcement, quote, information):

```
┌───────────────────────────────┐
│ NEW · THE PLINTH COLLECTION   │  Jost 500 uppercase label, letterSpacing.label, Earth
│                               │
│ A tray with the weight        │  Newsreader Light, large, Earth or Charcoal
│ of stone                      │
│                               │
│                      [symbol] │  small symbol, optional
└───────────────────────────────┘  Ivory or Sand ground, margins ≥ 1/10 of the width
```

**Carousel structure:**

1. Cover: one hero photograph, optionally with a short Newsreader title in a calm area.
2. The object in context.
3. Material detail.
4. Form or use (a hand, a scale shot).
5. Making, if relevant.
6. Information frame: the name in Newsreader (product names are always Newsreader), then size, material and price
   in Jost, on Ivory.
7. Optional close: the sign-off and where to find ARANT, no hard sell (see [Close frame](#close-frame)).

### Close frame

**Established** (studio decision; rendered by `build_social.py`, options in `brand/social/posts.json`):

- **One mark:** the stacked lockup by default (`logo`: `stacked`, `horizontal`, `one-line` or `symbol`), the
  unchanged master in the logo colour, with no second mark. It is set at 140 px of artwork as shown on a phone
  (420 px in the 1080 px frame), above its 120 px screen minimum, with at least its clear space around it.
- **Where to find it:** the `line` (`arantdesign.com`) with the Instagram handle `@arantdesign` stacked below it
  (`handle`, default true), in Jost Regular at body size, Earth. The handle is included in feed carousels.
- **No tagline** by default (`tagline`, default false). The option remains for a frame that needs it.
- Everything centred inside the text area and the centre 1:1 crop, on Ivory. No accent, no call to action.

**Reel covers:** a single frame from the reel (the object, calm), with a short Newsreader title if needed. Series
covers share one layout so the grid stays calm.

## Content types

| Type                    | Treatment                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| Launch                  | Teaser (a detail, no name) → cover post with name → carousel → reel. Same crop and type on all    |
| Collection announcement | A designed cover with the collection name, then photography carousels                             |
| Process                 | Honest studio footage: hands, tools, materials, calm pacing, natural sound or quiet music         |
| In the home             | Customer or styled interiors; credit the photographer; no heavy filters                           |
| Promotion               | Rare. Photograph plus one Newsreader line; details in the caption. No "SALE" bursts or countdowns |

## Motion and sound

- Slow, steady camera; cuts on a rhythm, not every beat. Text appears with a simple fade.
- No trending effects, transitions or stickers. Captions on screen for anyone watching without sound.

## Captions

Written in the ARANT voice ([`voice-and-copy.md`](voice-and-copy.md#instagram-captions)): short, specific, about
the object, material or space. A few relevant hashtags at most, at the end.
