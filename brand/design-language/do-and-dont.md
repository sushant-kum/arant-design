# Do and don't

A review checklist with specific examples. Back to the [design-language index](README.md). Labels: **E** =
Established, **R** = Recommended.

| Area            | Do                                                                                       | Don't                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Logo            | Place a generated file from `brand/identity/`; horizontal lockup by default (E)          | Retype ARANT in Jost or any font; redraw, trace or "clean up" the artwork (E)             |
| Logo            | Keep half the ARANT cap height clear on every side; stay above the minimum sizes (E)     | Stretch, rotate, outline, add a shadow or gradient, close the split, move the pebble (E)  |
| Logo            | Use `-ivory` or `-white` files on dark grounds (E)                                       | Place the logo on a busy photograph without a calm area or solid panel (E)                |
| Logo            | Choose the lockup the space needs: one-line for a band, symbol for a stamp (E)           | Switch lockups for variety, or use two logos on one face (E, R)                           |
| Colour          | Ivory or Sand grounds, Charcoal or Earth text, one Terracotta element (E, R)             | Terracotta and Olive together; Terracotta as a large screen ground (R)                    |
| Colour          | Import colours from `tokens.json`; derive shades with `tokens.mix(...)` (E)              | Type a hex value into code, or pick a tint by eye (E)                                     |
| Colour          | Check new text pairs with `tokens.contrast()` against WCAG AA (R)                        | Terracotta text under 24 px (E); Sand text or borders on Ivory (R)                        |
| Colour          | Flat colour (R)                                                                          | Gradients, glows, duotones (E for the logo, R elsewhere)                                  |
| Typography      | Jost for function (nav, labels, prices, specs); Newsreader for headlines and stories (E) | Newsreader in capitals, ever (E); a third typeface (E)                                    |
| Typography      | Uppercase Jost labels with `letterSpacing.label`, read from the token (E)                | Tracking by eye, or the value typed as a literal (E)                                      |
| Typography      | Hierarchy from size, weight and space; body at 16 px or more (R)                         | Bold 700, underlines or colour to force emphasis; text under 12 px (R)                    |
| Layout          | One dominant element per section; generous, scale-based spacing (R, scale E)             | Filling space because it's there; dense grids of equal cards (R)                          |
| Layout          | A 64-character measure for reading text; a shared left edge (R)                          | Full-width paragraphs; centring long text (R)                                             |
| Shape           | Square images and panels; `radius.soft` on controls; circles for seals and avatars (E)   | Pill buttons, rounded cards, blobs, wavy dividers (R)                                     |
| Photography     | Daylight, soft shadow, stone and plaster surfaces, one subject, space around it (R)      | Studio strobes on white, heavy HDR or filters, stock images, prop clutter (R)             |
| Photography     | True material colour; one detail shot per product (R)                                    | Retouching away the object's genuine variation (R)                                        |
| Materiality     | Show texture in photographs of real materials (R)                                        | Paper-grain overlays, faux stone, texture behind body text (R)                            |
| Packaging       | Kraft or ivory stock, one-colour print or stamp, a seal or band as the accent (E, R)     | Foil, lamination, spot UV, full-bleed print, a logo on every face (R)                     |
| Packaging       | Stamps and dies from `print/pdf/*-black.pdf`, above the stamp minimum sizes (E)          | Specifying `color.kraft` as an ink; it is reference only (E)                              |
| UI              | Text links, quiet buttons, hairlines, square images, the icon set (E), subtle fades (R)  | Shadows, glassmorphism, gradients, auto-carousels, arrival pop-ups, countdowns (R)        |
| UI              | Visible focus, 44 px or larger targets, labelled fields, reduced-motion support (R)      | Colour as the only signal; placeholder-only labels; motion that can't be switched off (R) |
| Social          | Mostly photography; designed tiles on Ivory or Sand with one Newsreader line (R)         | A logo on every post; "SALE" bursts; trending effects and stickers (R)                    |
| Copy            | Write about form, material, space and use; one precise adjective; British English (R)    | "Luxury", "stunning", "must-have", "elevate", exclamation marks, fake scarcity (R)        |
| Copy            | Name materials and processes in product descriptions only (R)                            | "Hand-cast" or any process in brand-level lines, packaging frames or navigation (R)       |
| Cultural        | Indian sensibility through architecture, materials, light and making (R)                 | Mandalas, lotus, paisley, temple silhouettes or other motifs used to signal "Indian" (R)  |
| Future-proofing | Test that a layout works for a ceramic, wooden or metal object too (R)                   | Anything that ties the brand to one material, process or category (R)                     |
