# ARANT DESIGN · Website

**Status: planned.** The site for [arantdesign.com](https://arantdesign.com).

## Ready to use

- **Design tokens:** [`packages/tokens/tokens.json`](../../packages/tokens/tokens.json): colour and colour roles
  (with an optional dark theme), type, spacing, containers, gutters, grid, breakpoints, radius, borders and motion.
  Import these rather than hard-coding values.
- **Logo:** [`brand/identity/logo/svg/`](../../brand/identity/logo/svg/). Use `arant-one-line.svg` or
  `arant-horizontal.svg` for the header.
- **Favicon and app icons:** [`brand/identity/export/symbol/`](../../brand/identity/export/symbol/). Copy
  `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `maskable-512.png` and
  `site.webmanifest` into the site's public folder, and paste `head-snippet.html` into the page `<head>`.
- **Interface icons:** [`brand/identity/icons/`](../../brand/identity/icons/): one SVG per icon, or `sprite.svg`. See
  the [identity README](../../brand/identity/README.md#icons) for sizes and stroke widths.
- **Fonts:** Jost and Newsreader from Google Fonts (SIL Open Font License).

## When the site is set up

The repo is already a pnpm workspace that includes `apps/*`. Create the site's `package.json` here (name it
`@arant/website`) and add the tokens as a dependency:

```json
"dependencies": { "@arant/tokens": "workspace:*" }
```

Then run `pnpm install` at the repo root, and run the site's scripts with `pnpm --filter @arant/website <script>`.

Knip picks up the new workspace automatically and has plugins for Next.js, Astro and Vite. If it reports framework
entry files (routes, pages, lazy-loaded components) as unused, add a `workspaces."apps/website"` entry with their
`entry` globs to `knip.json` at the repo root.
