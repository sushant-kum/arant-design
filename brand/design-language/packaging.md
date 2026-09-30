# Packaging

A packaging language for a growing Indian D2C brand: minimal, tactile, warm, practical, premium. Back to the
[design-language index](README.md).

---

## What is established

**Established** (guide section 06 "In use"; identity README):

| Item                 | As shown in the guide                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------- |
| Product box          | Kraft box, one-colour print of the stacked lockup, a Terracotta band                         |
| Hang tag             | Symbol, product name in Newsreader, colour, finish and price in Jost                         |
| Seal sticker         | Terracotta circle, reversed symbol, ring text "ARANT DESIGN · OBJECTS FOR CONSIDERED SPACES" |
| Tissue               | The symbol pattern in Sand, with an Earth Brown wrapping band carrying the one-line lockup   |
| Thank-you card       | Symbol, "Thank you for giving this object a place in your home.", ARANT DESIGN label         |
| Business card        | Reversed symbol on the front; horizontal lockup, name, email and web on the back             |
| Stamps, dies, moulds | Black PDF or SVG; the stamp column of the minimum-size table                                 |

Kraft is the board itself (`color.kraft` is reference only). On kraft, print in dark brown: the guide uses
`mix(earth, #000000, 0.20)` at 5.9 : 1; Earth Brown alone gives 4.9 : 1.

## Principles for packaging

**Recommended:**

- **One mark, one message, one accent** per surface.
- **The material is the finish.** Kraft, uncoated ivory stock and corrugated board, printed in one colour, carry the
  premium feeling through touch. No lamination, foil, spot UV or metallics.
- **Operationally realistic.** Stock box sizes from local suppliers, printed or stamped in-house or in short runs;
  labels and stickers that can be applied by hand; nothing that needs a custom insert per product.
- **Material-neutral.** No packaging line names a material or process; product-specific information goes on the
  product label or card.
- **Protective first.** The object must arrive intact; the design works with the protection, not against it.

## Colour and print

| Method                    | Colour                                      | Use                               |
| ------------------------- | ------------------------------------------- | --------------------------------- |
| One colour on kraft       | Dark brown (Earth or the guide's kraft ink) | Boxes, cartons, mailers           |
| One colour on ivory stock | Earth Brown                                 | Cards, labels, tags               |
| Two colour                | Earth Brown + Terracotta (one element)      | Seal, band, the price on a tag    |
| Rubber stamp              | Black or Earth ink                          | Short runs, cartons, tissue seals |
| Blind emboss or deboss    | No ink                                      | Premium cards, box lids, tags     |

- Follow the print notes in [`colour.md`](colour.md#print): confirm CMYK and Pantone on a proof.
- Stamps and dies from `print/pdf/*-black.pdf`, above the stamp minimum sizes.

## Typography on packs

- Jost for all information: product name on the label is the only exception, set in Newsreader.
- Uppercase Jost labels with `letterSpacing.label` for short headers (CARE, MATERIAL, SIZE).
- Minimum text size: 6 pt for legal lines, 7–8 pt for information, larger for anything a customer should read
  first (proposed values; confirm on a proof).

## Logo placement

- **Product box:** stacked or horizontal lockup, centred on the lid or on one face, small (a quarter to a third of
  the face width at most), with full clear space.
- **Shipping carton:** the symbol or one-line lockup, stamped or printed once, small, near one corner or centred on
  the top. Cartons carry little else: they are for handling.
- **Band or wrap:** the one-line lockup (**Established**, guide tissue mockup).
- **Seal:** the reversed symbol in the Terracotta seal (**Established**).
- **Tags and small labels:** the symbol, or ARANT only.
- Never more than one logo per face, and never the pattern and a lockup at similar sizes.

## The pieces

| Piece             | Recommended construction and content                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Shipping carton   | Plain brown corrugated; one small stamped symbol; handling marks in Jost; the shipping label                       |
| Mailer            | Kraft, one-colour print or stamp; closed with the seal sticker                                                     |
| Product box       | Kraft or ivory rigid or folding box; lockup on the lid; a paper band (Terracotta or Earth) as the one accent       |
| Tissue            | Plain Sand or ivory tissue, closed with the seal; the printed symbol pattern when volumes justify it               |
| Paper band / wrap | Earth Brown or Terracotta band with the one-line lockup, reversed                                                  |
| Product label     | Ivory stock; product name (Newsreader), colour, size, material, care, and statutory details (Jost)                 |
| Hang tag          | As the guide mockup: symbol, name, colour or finish, price                                                         |
| Product card      | A5 or A6, ivory: the object's name, one paragraph about form and making, care, and the web address                 |
| Thank-you card    | A6, ivory: symbol, one Newsreader line, ARANT DESIGN label; optional handwritten note space                        |
| Sticker           | Circular seal (Terracotta, reversed symbol) for closing; a small Earth-on-ivory symbol sticker as a neutral option |
| Gift packaging    | The standard box with tissue, band and seal, plus a plain gift card; no prices inside; no separate gift range      |

**Statutory information.** Retail packs sold in India carry mandatory declarations (for example under the Legal
Metrology (Packaged Commodities) Rules: manufacturer or packer details, net quantity, MRP, month and year of
manufacture, consumer care contact). Confirm the current requirements with an advisor. Set them in Jost on the
product label, legible and complete, never hidden to keep a face clean.

## Examples

**Product label** (example names and values):

```
Plinth Tray                         ← Newsreader Light
SAND · 32 × 18 CM                   ← Jost Medium, uppercase, letterSpacing.label
Mineral composite, hand-finished.   ← Jost Regular (product-level material line)
Wipe clean with a damp cloth.
MRP ₹1,800 (incl. of all taxes)
[Net quantity] · [Month and year of manufacture]
[Manufacturer or packer name and address] · [Consumer care contact]
ARANT DESIGN · arantdesign.com
```

Square-bracketed lines are placeholders for the statutory declarations; confirm their exact wording.

**Thank-you card** (**Established** line, guide mockup):

```
[symbol]
Thank you for giving this object a place in your home.
ARANT DESIGN
```
