# Digital

Components and behaviour for [arantdesign.com](https://arantdesign.com) and other screens. Back to the
[design-language index](README.md).

**Status.** The website is planned (`apps/website/README.md`); no component or style code exists. What is
**Established** is the plumbing, the brand guide's website mockup, the design tokens (colour roles, spacing, layout,
radius, borders, motion) and the icon set. Components and states are **Recommended**. Layout tokens are explained in
[`layout.md`](layout.md), radius in [`shape-language.md`](shape-language.md), colour roles in
[`colour.md`](colour.md).

---

## Established foundations

- Colour and type come from `@arant/tokens` (`workspace:*`). Generate CSS variables or JS from `tokens.json` (for
  example with Style Dictionary); don't hard-code hex values or font names, and don't build a parallel token system
  (`apps/website/README.md`).
- Header logo: `arant-one-line.svg` or `arant-horizontal.svg` from `brand/identity/logo/svg/`.
- Favicon, app icons and manifest: `brand/identity/export/symbol/`. Copy the listed files to the site's public
  folder and paste `head-snippet.html` into the `<head>`. Theme colour is `logo.default` (Earth Brown) and the
  manifest background is Warm Ivory; both are written by the build from the tokens.
- Icons: the line set in `brand/identity/icons/` (SVG files and a sprite, painted in `currentColor`); see
  [Icons](visual-language.md#icons).
- Fonts: Jost and Newsreader from Google Fonts. Load Jost 400 and 500, Newsreader 300 and 400 with the `opsz` axis,
  as the guide does, with `display=swap`.
- The guide's website mockup: one-line lockup left, uppercase Jost navigation right (Objects · Studio · Journal), a
  hairline under the bar, and a hero with an uppercase Earth collection label, marked by a short Terracotta rule, over a
  Newsreader Light line.

## The feel

A contemporary design studio's site, not an e-commerce template. Typography, large photography and whitespace do
the work; components are few and quiet.

**Never:** gradients, glassmorphism or backdrop blur, drop shadows on cards or buttons, pill buttons, oversized
rounded containers, countdown timers, pop-ups on arrival, auto-playing carousels, marquees, confetti, parallax, star
ratings in grids, "only 2 left" badges unless the stock count is true and useful.

## Header and navigation

- One-line lockup on the left (horizontal on large, calm headers; the symbol alone only where a lockup would be too
  small to read). Keep the logo at or above its screen minimum from the identity README (the one-line lockup: 190 px
  wide).
- Three to five top-level links in Jost 500, uppercase, `letterSpacing.label`: for example Objects, Collections,
  Studio, Journal. Utility links (search, account, bag) on the right, as words or line icons with labels available
  to assistive technology.
- Ivory ground, Earth or Charcoal text, a single hairline below. On scroll, the header may become sticky and compact
  (the one-line lockup is established for the sticky bar); no blur, no shadow.
- Mobile: lockup, bag and a "Menu" button. The menu opens as a full-screen Ivory panel with large Newsreader links;
  focus moves into it and returns on close.
- Current page: a 1 px underline or Earth text, not a pill or a filled box.

## Footer

- On Sand, or Charcoal with Ivory text (reversed logo files). Symbol or horizontal lockup, grouped plain links in
  Jost, newsletter field, `@arantdesign`, legal links.
- The one place the symbol pattern may appear on the web, as a quiet band.

## Links and buttons

| Element          | Recommended treatment                                                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text link        | Inherits text colour (Earth or Charcoal), 1 px underline offset from the text; on hover the underline thickens or the colour shifts one step                   |
| Primary button   | Charcoal (or Earth) fill, Ivory Jost 500 uppercase label with `letterSpacing.label`, `radius.soft`, min height 48 px, padding about 2× the height horizontally |
| Secondary button | Transparent, 1 px Earth border, Earth label; same size and radius                                                                                              |
| Tertiary action  | A text link with an arrow (→), no box                                                                                                                          |
| Disabled         | Reduced contrast plus `aria-disabled` and a reason in text; never the only signal                                                                              |

- One primary button per view.
- Hover: a colour step (for example Charcoal to Earth) or an underline change; no lift, scale or shadow.
- Terracotta is not a button or link colour: Terracotta text is for 24 px and larger only (see
  [`colour.md`](colour.md)).

## Product card

```
┌───────────────────────────┐
│                           │   image: 4:5, on Sand or a photographed surface,
│          [image]          │   square corners, no border, no shadow
│                           │
└───────────────────────────┘
Plinth Tray                      Newsreader 400, ~20px
Sand · 32 × 18 cm                Jost 400, small, text.muted
₹1,800                           Jost 400/500
```

- No container, border or background around the text. The card is the image and three lines.
- The whole card is one link; the image has meaningful alt text.
- Hover (pointer devices only): swap to the in-context image with a short cross-fade, or no change. No zoom, no
  "quick add" overlay by default.
- Labels such as "New" or "Sold out" as a small uppercase Jost label under the image or above the name, not a
  coloured badge on the photograph.

## Product grid and collection pages

- 3 across on desktop, 2 on tablet and phone (see [`layout.md`](layout.md#grid)).
- A collection page opens with an uppercase label, a Newsreader heading and a short introduction, then the grid.
  Every 6–9 products the grid may be interrupted by one editorial moment: a full-width image or a short story.
- Filters, if needed, as a single row of Jost text buttons, not chips. Sorting as a plain select.
- No infinite scroll without a visible end and a way to reach the footer.

## Product page

1. Gallery: large images (hero, in context, detail, variants), square corners. Swipe on phones, thumbnails or a
   vertical stack on desktop. No auto-advance.
2. Name in Newsreader (the page's only display line), price in Jost, then colour or finish options as labelled
   swatches (a colour dot plus its name, never colour alone).
3. One primary "Add to bag" button; quantity as a simple stepper.
4. A short description (two or three sentences about form, use and material), then details in Jost: dimensions,
   weight, material, finish, care, and a note that hand-finished pieces vary.
5. Delivery and returns in plain language, in expandable sections with visible headings.
6. "You might also like" limited to three objects.

## Forms

- Labels above fields, always visible, in Jost 400; never placeholder-only labels.
- Inputs: Ivory or white-tint ground, 1 px Earth border (3 : 1 or more), `radius.soft`, min height 48 px, 16 px text
  so phones don't zoom.
- Errors: text below the field explaining the fix, linked with `aria-describedby`, plus an icon or prefix; the
  border changes too. Not colour alone.
- Group long forms (checkout) into short steps with clear headings.

## Banners and announcements

- One announcement bar at most: one line of Jost, Ivory on Earth or Charcoal on Sand, dismissible, static (no
  scrolling ticker).
- Promotional banners are editorial: a photograph with a calm area, one Newsreader line, one link. No bursts,
  percent-off stickers or countdowns.

## Modals, drawers and dialogs

- Use sparingly: the bag (as a side drawer), the mobile menu, image zoom, and confirmations.
- No newsletter or discount pop-ups on arrival. Invite sign-ups inline and in the footer.
- Ivory panel, square corners, a hairline or a solid Charcoal scrim at about 40–60 % opacity; no blur.
- Focus moves into the dialog, is trapped while open, returns to the trigger on close; Esc closes; a visible close
  button with a text label.

## Borders, radius and elevation

**Established** (`tokens.json`):

| Token           | Treatment                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------- |
| `border.subtle` | A 1 px hairline in `color.role.line.subtle` (a light Sand tint, as the guide): dividers           |
| `border.strong` | A 1 px line in `color.role.line.strong` (Earth): inputs, secondary buttons, interactive           |
| `radius.*`      | `none` by default, `soft` for controls, `round` for circles ([shape-language](shape-language.md)) |

There is no shadow token: elevation is none. Layers are separated by colour and hairlines.

The brand guide's mockups use shadows only to render physical objects (a tray, a card) sitting on a surface. That is
illustration, not a UI pattern.

## Motion

**Established** (`duration.*`, `easing.*` and the `motion.*` transitions that combine them):

| Token             | Duration · easing                  | Use                                        |
| ----------------- | ---------------------------------- | ------------------------------------------ |
| `motion.quick`    | `duration.quick` · `easing.out`    | Hover colour and underline changes         |
| `motion.standard` | `duration.standard` · `easing.out` | Drawers, menus, accordions                 |
| `motion.gentle`   | `duration.gentle` · `easing.inOut` | Image cross-fades, section fade-in on load |

**Recommended:**

- Motion confirms an action or eases a change of state. It never decorates.
- Fade and short slide only (no more than about 16 px of travel). No bounce, spring, parallax, scroll-jacking or
  pinned scroll stories.
- Honour `prefers-reduced-motion: reduce`: replace movement with an instant change or a simple fade.

## Dark theme

Optional. Use the `color.roleDark.*` tokens (**Established**, the guide's dark mixes; see
[`colour.md`](colour.md#light-and-dark-contexts)) and the reversed logo files. Light stays the default and photography
stays unchanged (**Recommended**).

## Email

**Recommended:** the one-line lockup in the footer (**Established** use), Ivory ground, Jost text with web-safe
fallbacks from the token stacks, one image, one button. Plain-text version always.
