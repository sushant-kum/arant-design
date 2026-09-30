# ARANT DESIGN · Social

Instagram (`@arantdesign`) tiles, carousel frames and story and reel covers, rendered from the design language. Part
of the [ARANT DESIGN monorepo](../../README.md). The rules are in
[`brand/design-language/social.md`](../design-language/social.md); this folder is how they are produced.

| Path         | What                                                              | Edit it?                         |
| ------------ | ----------------------------------------------------------------- | -------------------------------- |
| `posts.json` | The posts to render: copy, layout, photo paths                    | Yes: add an entry for a new post |
| `photos/`    | Photographs the posts use (not in the repo yet)                   | Yes: add photographs here        |
| `templates/` | The reusable set with placeholder copy, each with a `-guides.png` | **No: generated**                |
| `posts/`     | Finished PNGs, one per post, or one folder of frames per carousel | **No: generated**                |

Rebuild after any change:

```bash
pnpm identity:social    # or the whole pipeline: pnpm identity:build
```

The script is [`brand/identity/source/build_social.py`](../identity/source/build_social.py). It lives with the other
build scripts because it shares their renderer, token reader and logo masters.

## Formats

| Format                      | Size        | Safe area                                                                                                                                   |
| --------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `feed` (post, carousel)     | 1080 × 1350 | Text inside the margin and inside the centre 1:1 area (the grid preview crop)                                                               |
| `story` (story, reel cover) | 1080 × 1920 | No text in the top and bottom 250 px (app interface); a reel cover's title inside the centre 1:1 area, so it reads in the 4:5 and 1:1 crops |

The profile picture is not made here: it is `brand/identity/export/symbol/arant-symbol-app-icon-1024.png` (see the
[identity README](../identity/README.md#which-file-do-i-need)).

## Layouts

| Layout  | Use                                                 | Fields                                                                                                                                                                                                |
| ------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tile`  | A designed post: announcement, quote, information   | `ground` (`ivory` or `sand`), `label`, `headline`, `accent` (`terracotta`, `olive` or none), `symbol` (true or false)                                                                                 |
| `photo` | Photography, with or without a short title          | `photo` (path in this folder), `shot` (shown on the placeholder), `title`, `ink` (`dark` or `light`)                                                                                                  |
| `info`  | The carousel's information frame                    | `name`, `details` (a list of `[label, value]` pairs)                                                                                                                                                  |
| `close` | The carousel's close (Established, studio decision) | `logo` (`stacked`, `horizontal`, `one-line` or `symbol`; default `stacked`), `handle` (true or false; default true), `line` (for example `arantdesign.com`), `tagline` (true or false; default false) |

A post is one of these with `slug` and `format`, or `"layout": "carousel"` with a list of `frames`, each with a
`role` (cover, context, material, use, making, information, close: the sequence in `social.md`). `"sample": true`
adds a SAMPLE band across the top: sample posts are for review, never for posting.

While a photograph doesn't exist, its frame renders as a marked placeholder plate (Sand, a dashed edge, the shot and
the expected path). Put the file at that path and rebuild. A title on a photograph needs a calm area of the image;
choose `ink` so it reads, and check it by eye, because the build can't judge a photograph's contrast.

## How it is drawn

- Every frame is an HTML page with Jost and Newsreader embedded, rendered by headless Chrome, so the type is the
  real type. The font files are in `brand/identity/source/fonts/` (SIL Open Font License, which allows embedding and
  redistribution); `pnpm identity:fonts` restores them from a pinned google/fonts commit, and needs network access.
- Colours are the role tokens (`color.role.*`); margins and gaps are the space tokens and label tracking is
  `letterSpacing.label`, all multiplied by 3, because a 1080 px frame is shown about 360 pt wide on a phone. The
  margin is `space.7` × 3 = 144 px, above `social.md`'s minimum of a tenth of the width.
- The symbol is the unchanged master, small (96 px), at the bottom right with its clear space. The one accent is a
  short rule above the label, never text.
- The close frame carries one mark, the stacked lockup by default: the unchanged master in the logo colour, 420 px
  of artwork (140 px on a phone, above the 120 px screen minimum; the build fails if a size would drop below it),
  with at least its clear space (half the ARANT cap height) below. Then `arantdesign.com` above `@arantdesign` in
  Jost, and no tagline. See [`social.md`](../design-language/social.md#close-frame).
- Output is byte-identical from run to run.

## Licence

Everything here is a brand asset, all rights reserved (see [`LICENSE`](../../LICENSE)).
