# Typography

Jost and Newsreader, and how to set them. Back to the [design-language index](README.md).

The logo is drawn, never typed (**Established**). Everything below is about the type around it.

---

## The two families

**Established** (`tokens.json` `font.*`, `letterSpacing.label`; identity README; guide section 05):

| Token               | Family     | Character                    | Use                                                         | Weights                                                         |
| ------------------- | ---------- | ---------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| `font.family.sans`  | Jost       | Geometric, like the wordmark | Labels, navigation, product details, prices, packaging copy | `font.weight.regular` 400, `font.weight.medium` 500             |
| `font.family.serif` | Newsreader | Editorial serif              | Headlines, product names, stories, cards, editorial         | `font.weight.light` 300 display, `font.weight.regular` 400 text |

- Jost is the primary family; Newsreader the secondary (token descriptions).
- Uppercase Jost labels take `letterSpacing.label` (0.2em).
- Newsreader is never set in all caps.
- Both are SIL Open Font License 1.1, from Google Fonts. Use the fallback stacks in the tokens.
- The guide loads Newsreader with its optical-size axis (`opsz` 6..72) so display sizes use the display cut. Load it
  the same way on the web.
- No other typefaces in brand communication. The guide also loads IBM Plex Mono for code samples; it is not a brand
  face.

## Who does what

**Recommended**, extending the established use lists:

**Jost is the voice of function.** Navigation, buttons, labels, form fields, prices, product specifications
(material, size, finish, care), metadata, legal text, packaging information, UI body copy.

**Newsreader is the voice of the object and the story.** Page and section headlines, product and collection names,
collection introductions, journal articles, pull quotes, the thank-you card line.

Don't use Newsreader for:

- buttons, navigation, form labels, prices or tables;
- uppercase labels (never, in any size);
- dense product specifications.

Don't use Jost for:

- long-form editorial reading (articles, stories longer than a paragraph or two);
- large display headlines, except a deliberate uppercase label set large for signage.

## Hierarchy

**Established** (the hierarchy sample in guide section 05): an uppercase Jost label, a Newsreader Light title, Jost
body, and uppercase Jost metadata. For example:

> NEW · THE PLINTH COLLECTION  
> A tray with the weight of stone  
> Body copy in Jost Regular.  
> SAND · 32 × 18 CM · ₹1,800

(Names and prices are examples, as the guide marks them.)

**Recommended** type roles for the web. Sizes in the "Observed" column come from the brand guide page, which is the
only implementation so far; the rest are proposed values, not tokens.

| Role             | Family · weight       | Size / line height                        | Casing, tracking                         | Observed in guide           |
| ---------------- | --------------------- | ----------------------------------------- | ---------------------------------------- | --------------------------- |
| `display`        | Newsreader 300        | proposed: `clamp(40px, 6vw, 72px)` / 1.05 | Sentence case, no tracking               | —                           |
| `heading`        | Newsreader 300        | `clamp(30px, 4.4vw, 44px)` / 1.1          | Sentence case, balanced wrap             | `h2`                        |
| `title`          | Newsreader 300 or 400 | proposed: 24–38px / 1.15                  | Title case for product names             | hierarchy title 38 px       |
| `lede`           | Newsreader 300        | 21px / 1.5, measure 58ch                  | Sentence case                            | `.lede`                     |
| `body-editorial` | Newsreader 400        | proposed: 18–19px / 1.6, measure ≤ 64ch   | Sentence case                            | —                           |
| `body`           | Jost 400              | 16px / 1.6, measure ≤ 64ch                | Sentence case                            | `body`, `p`                 |
| `small`          | Jost 400              | 14px / 1.5                                | Sentence case                            | notes, captions             |
| `label`          | Jost 500              | 12–13px / 1.3                             | UPPERCASE, `letterSpacing.label` (0.2em) | eyebrows, `h3`, table heads |
| `price`          | Jost 400 or 500       | same size as the adjacent body or meta    | Figures as written: `₹1,800`             | hierarchy meta              |

Rules (**Recommended**):

- Build hierarchy from size, weight and space. Don't add colour, boxes or underlines to make something important.
- Never go below 12 px for any text, and use 12–13 px only for uppercase labels. Body text is at least 16 px.
- Keep a measure of 45–75 characters (about 64ch) for reading text.
- On screen, Newsreader Light (300) is for sizes of about 21 px and up; below that use Regular (400), whose strokes
  hold up better. In print, Light works for short lines at card and tag sizes, as the guide mockups show.
- Jost Medium (500) is for labels, buttons and emphasis. Don't use a bold (700) weight: it isn't part of the system.
- Italic Newsreader may mark a title or a quotation in running text; don't use it for whole headlines.
- One display headline per view. Section headings sit one clear step below it.

## Casing

- **Established:** ARANT and ARANT DESIGN are written in capitals in running text, as throughout the repo. Newsreader
  is never all caps.
- **Established:** the tagline is always written **Objects for Considered Spaces.**, in title case with the full stop,
  as a fixed brand line; it is the one exception to sentence case. Set in an uppercase Jost label, the capitals
  replace the case.
- **Recommended:** sentence case for headlines and body; title case for product and collection names (Plinth Tray,
  the Plinth collection); uppercase only for short Jost labels, navigation and metadata, never for a sentence.

## Letter spacing

- **Established:** every uppercase Jost label (eyebrows, table heads, navigation, buttons, taglines set as labels,
  metadata) uses `letterSpacing.label` (0.2em). Read it from the token; never write the value as a literal. The
  brand guide (`--tracking-label` in `build_guide.py`) and the Instagram build (`build_social.py`) both read it.
- **Established:** the only exceptions are ring text fitted to a circle (the seal and the maker's stamp, whose
  spacing is set to fill the ring), and lowercase or mono text, which is not a label.
- **Recommended:** sentence-case Jost and all Newsreader take no added tracking.

## Responsive behaviour

**Recommended:**

- Scale display and heading sizes fluidly with `clamp()`, as the guide does; keep body at 16 px on every screen.
- On phones, drop `display` to the `heading` range rather than letting it wrap into more than four lines.
- Use `text-wrap: balance` for headlines (the guide does) and `pretty` for short paragraphs.
- Don't shrink labels below 12 px on small screens; shorten the text instead.

## Pairings in practice

| Context          | Pairing                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| Product card     | Name in Newsreader 400; material and size in Jost 400 small; price in Jost        |
| Collection intro | Uppercase Jost label; Newsreader Light heading; Newsreader or Jost lede           |
| Hang tag         | Product name in Newsreader Light; colour, finish and price in Jost (guide mockup) |
| Thank-you card   | One Newsreader Light line; ARANT DESIGN as an uppercase Jost label (guide mockup) |
| Navigation       | Jost 500 uppercase with `letterSpacing.label` (guide website mockup)              |
| Button           | Jost 500 uppercase with `letterSpacing.label`, 13–14 px                           |
