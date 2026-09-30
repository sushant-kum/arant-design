# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The ARANT DESIGN monorepo (a contemporary Indian home-objects brand). Today it holds the finished **brand identity
v1.1** (`brand/identity/`) and the shared **design tokens** (`packages/tokens/`). `brand/design-language/`,
`brand/mockups/` and `apps/website/` are planned; each has only a README describing its intended contents. There is no
JS/TS/CSS source yet: ESLint, Stylelint and knip are configured ahead of the website.

## Commands

Requires Node ≥ 22, pnpm 12 (pinned via `devEngines`), Python 3 (stdlib only), Chrome/Chromium for rendering
(`CHROME=/path` overrides), and Ruff (`pipx install ruff`) for Python linting.

```bash
pnpm install              # also installs the husky git hooks (prepare script)
pnpm identity:build       # check → logo → exports → print → guide (regenerates all identity files)
pnpm identity:check       # fail if a brand colour hex is hard-coded in brand/identity/source/*.py
pnpm identity:logo        # one step at a time: identity:logo | identity:exports | identity:print | identity:guide
pnpm lint | lint:fix      # ESLint (flat config, eslint.config.mjs)
pnpm stylelint            # CSS/SCSS
pnpm format:check | format:fix   # Prettier
pnpm lint:py | format:py  # Ruff over the Python build scripts
pnpm secretlint           # secrets in any tracked file
pnpm knip                 # unused files, exports, dependencies
pnpm tool::commit         # commitizen prompt for a Conventional Commit message
```

There are no tests. The verification for identity changes is to rebuild and compare outputs: SVG, PNG, ICO, JPG and
HTML come out byte-for-byte identical when geometry and tokens are unchanged; PDFs differ only in metadata
(`CreationDate`/`ModDate`).

## Architecture: the identity build pipeline

Everything under `brand/identity/{logo,export,print,guide}/` is **generated**; never hand-edit it (VS Code marks those
paths read-only, and Prettier/ESLint/Stylelint ignore them). Change the source and rebuild.

- **Colour has one source:** `packages/tokens/tokens.json` (W3C Design Tokens, with `{alias}` references and display
  names under `$extensions["com.arantdesign"].name`). `brand/identity/source/brand_tokens.py` loads it and provides
  `color()`, `name()`, `mix()`, `cmyk()`, `contrast()`. Every build script imports colours from there;
  `check_tokens.py` (run first by `identity:build` and by lint-staged) fails on any palette hex literal in the scripts.
  Derived shades (guide UI tints, dark theme, mockup materials like kraft/stone) are `tokens.mix(...)` of palette
  colours, never literals. The only allowed literals are black, white and the deliberate off-brand blue in the guide's
  "don't recolour" example.
- **Geometry lives in `build_logo.py`** (with primitives from `glyphs.py`: `Sub`, `poly`, `rect`, `rounded_poly`). It
  writes the 7 masters in `logo/svg/`, all in `logo.default` colour. Everything downstream is derived from these masters.
- **`build_exports.py`** recolours masters into `export/<version>/arant-<version>-<token>.svg|png` (earth, charcoal,
  terracotta, ivory, black, white). Files are named by **token name, not hex**, so names stay stable if a value changes.
  It also builds the web icon set in `export/symbol/` (favicon.ico/.svg, PWA icons, `site.webmanifest`,
  `head-snippet.html`), with theme colours taken from tokens.
- **`build_print.py`** makes vector PDFs (`print/pdf/`) and JPGs on ivory (`print/jpg/`) from the export SVGs, so run it
  after `build_exports.py`.
- **`build_guide.py`** writes `guide/arant-brand-kit.html` and `guide/palette.svg`. The page is one large f-string
  HTML/CSS template (Ruff's E501 is disabled for this file only), and SVG masters are inlined with
  `fill="currentColor"`. The HTML has no `<!doctype>`/`<head>` on purpose: it is also published as a Claude artifact,
  which supplies the skeleton.
- **`render.py`** does all rasterising in one headless-Chrome session (SVG → canvas → data URL). It also handles
  SVG → PDF via `--print-to-pdf` and writes ICO files by hand. No Python dependencies anywhere.

### Logo invariants (brand decisions; don't change without being asked)

- Symbol "Balance": two mirrored slabs with a split of 5 units (100-unit grid), rounded caps and feet, and a pebble
  lifted until its clearance to each slab, **measured perpendicular to the slab edge**, also equals 5.
- In the wordmark, **every A is the symbol itself**, scaled by `K_A = 100/74` to cap height. R, N and T use the slab
  stroke (`W_STEM` ≈ 18 % of cap) and corner radius (`R_CORNER`). The N diagonal is exactly 60°. DESIGN is 27 % of the
  ARANT cap height, spaced to ARANT's exact width.
- There is no separate small-size or reversed-thinned symbol: the reversed master is the same drawing in ivory.
- Minimum sizes derive from one rule, **every opening ≥ 0.8 mm**. The table appears in both
  `brand/identity/README.md` and `build_guide.py`; recompute and update both if geometry changes.

Hex values and minimum sizes are also written by hand in the READMEs (documentation only, not read by any build);
update them when the palette or geometry changes.

## Repo conventions and tooling quirks

- pnpm workspace: `apps/*`, `packages/*`, packages named `@arant/*`, depend with `"workspace:*"`. Dependency versions
  live in the **catalog** in `pnpm-workspace.yaml` (`catalogMode: prefer`, `minimumReleaseAge: 4320`, so brand-new
  releases are refused). `allowBuilds: unrs-resolver: false` is deliberate (its native binary installs without the
  script).
- TypeScript is pinned to `~6.0.3` because typescript-eslint 8 supports TS < 6.1. ESLint 10 uses
  `eslint-plugin-import-x` (rules are `import-x/*`), not `eslint-plugin-import`. `eslint.config.mjs` auto-discovers
  workspaces with a `tsconfig.json`; framework presets (React/Astro) are intentionally not added until the website's
  stack is chosen (see the comment in the config).
- `.agents/` and `.claude/` contain a third-party Claude Code skill (logo-generator). They are excluded from Ruff,
  Prettier, Stylelint, ESLint and cspell. Ruff is invoked with `--force-exclude` in lint-staged so explicitly passed
  excluded files are skipped.
- Ruff: `ruff.toml`, line length 120, Python files only (Markdown code blocks are left to Prettier).
- Prettier: single quotes, printWidth 100; `.czrc` is parsed as JSON via an override.
- Git hooks (husky): pre-commit runs lint-staged (`.lintstagedrc.json`) then knip over the whole project; commit-msg
  runs commitlint (Conventional Commits, e.g. `feat(identity): …`, `fix(tokens): …`). Release tags are per area, e.g.
  `identity-v1.1`.
- Spelling: British English (`cspell.json`, which holds the brand word list).
- Licence: brand assets (everything in `brand/`, plus any copy of them elsewhere) are all rights reserved. Only
  `brand/identity/source/` and `packages/` are MIT; `apps/` defaults to all rights reserved.
