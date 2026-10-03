# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Durable memory:** always read [`docs/DECISION.md`](docs/DECISION.md) and [`docs/FLOW.md`](docs/FLOW.md) before
changing architecture, conventions, policy, tooling, or any recorded process, and write back to them in the same change.
See [Decision & Flow Records](#decision--flow-records).

## What this repo is

The ARANT DESIGN monorepo (a contemporary Indian home-objects brand). Today it holds the finished **brand identity
v1.1** (`brand/identity/`), the shared **design tokens** (`packages/tokens/`), the **design-language** docs
(`brand/design-language/`, summarised in `DESIGN.md`) and the Instagram templates and posts (`brand/social/`). `brand/mockups/` and `apps/website/` are planned; each has only
a README describing its intended contents. There is no JS/TS/CSS source yet: ESLint, Stylelint and knip are configured
ahead of the website.

## Brand and design work

For ARANT DESIGN brand and design-system work — identity, tokens, typography, colour, logo, the design language and
`DESIGN.md` — consult `DESIGN.md` (the concise design contract), preserve the established brand system, and use the
`arant-brand-designer` subagent (`.claude/agents/arant-brand-designer.md`). Finer-grained execution (packaging,
imagery/mockups, website UX, frontend build, social copy) goes to the specialists in **## Specialist agents** below,
which consume the brand rules rather than redefine them.

## Specialist agents

`arant-orchestrator` is the coordination layer above the specialists: for a cross-domain request it plans, delegates to
the right specialists, integrates their work, runs QA and enforces human-approval gates — it does no specialist work
itself. For a single clear specialist task, use that specialist directly.

`arant-brand-designer` is the brand authority. Eleven specialist subagents consume the brand system for their own
domains (see [`.claude/agents/README.md`](.claude/agents/README.md) for the full table — roles, what each reads/writes,
priorities and dependencies): `arant-product-designer` (what to make), `arant-product-development` (can we make it
repeatably — feasibility, CALSO ONE, moulds, finishing, QC), `arant-web-designer` (website UX specs),
`arant-frontend-engineer` (builds `apps/website` from those specs), `arant-visual-production` (photography, mockups, art
direction), `arant-content-strategist` (extends the `brand/social/` content system), `arant-commercial-analyst` (unit
economics and pricing), `arant-packaging-designer` (the physical packaging system), `arant-researcher` (decision-tied
evidence and research), `arant-qa-reviewer` (independent quality gate across all domains) and `arant-operations`
(inventory, production batches, fulfilment and SOPs). No specialist overrides the canonical brand system (identity,
tokens, typography, logo, design language) without an explicit, human-approved decision. See
[DEC-0008](docs/DECISION.md#dec-0008--structure-ai-work-as-a-13-agent-orchestrator-and-specialists-system).

## Commands

Requires Node ≥ 22, pnpm 12 (pinned via `devEngines`), Python 3 (stdlib only), Chrome/Chromium for rendering
(`CHROME=/path` overrides), and Ruff (`pipx install ruff`) for Python linting.

```bash
pnpm install              # also installs the husky git hooks (prepare script)
pnpm identity:build       # check → logo → exports → print → guide → icons → social (regenerates everything)
pnpm identity:check       # fail on a hard-coded brand hex in brand/identity/source/*.py or inconsistent tokens.json
pnpm identity:logo        # one step at a time: identity:logo | exports | print | guide | icons | social
pnpm identity:fonts       # re-fetch the vendored Jost/Newsreader files (needs network; not part of identity:build)
pnpm site:build           # GitHub Pages site → site/ (gitignored; stdlib only, no Chrome)
pnpm lint | lint:fix      # ESLint (flat config, eslint.config.mjs)
pnpm stylelint            # CSS/SCSS
pnpm format:check | format:fix   # Prettier
pnpm lint:py | format:py  # Ruff over the Python build scripts
pnpm secretlint           # secrets in any tracked file
pnpm knip                 # unused files, exports, dependencies
pnpm tool::commit         # commitizen prompt for a Conventional Commit message
```

There are no tests. The verification for identity changes is to rebuild and compare outputs: SVG, PNG, ICO, JPG and
HTML (including the icons and social PNGs) come out byte-for-byte identical when geometry and tokens are unchanged; PDFs differ only in metadata
(`CreationDate`/`ModDate`).

## Architecture: the identity build pipeline

Everything under `brand/identity/{logo,export,print,guide,icons}/` and `brand/social/{templates,posts}/` is
**generated**; never hand-edit it (VS Code marks those paths read-only, and Prettier/ESLint/Stylelint ignore them).
Change the source and rebuild. See [DEC-0003](docs/DECISION.md#dec-0003--generate-brand-assets-from-source-never-hand-edit-the-output).

- **Colour has one source:** `packages/tokens/tokens.json` (W3C Design Tokens, with `{alias}` references and display
  names under `$extensions["com.arantdesign"].name`). `brand/identity/source/brand_tokens.py` loads it and provides
  `color()`, `name()`, `mix()`, `cmyk()`, `contrast()`, `role()`, `tokens()`, `recorded_mix()`. Besides the palette,
  tokens.json holds colour roles (`color.role.*`, dark theme `color.roleDark.*`), spacing, layout, radius, border and
  motion tokens. Every build script imports colours from there; `check_tokens.py` (run first by `identity:build` and
  by lint-staged) fails on any palette hex literal in the scripts, on an `{alias}` that doesn't resolve, and on a role
  stored as a mix (`$extensions["com.arantdesign"].mix`) that no longer matches the current palette.
  Derived shades (guide UI tints, dark theme, mockup materials like kraft/stone) are `tokens.mix(...)` of palette
  colours, never literals. The only allowed literals are black, white and the deliberate off-brand blue in the guide's
  "don't recolour" example. See [DEC-0002](docs/DECISION.md#dec-0002--keep-colour-and-design-values-only-in-tokensjson).
- **Two type and colour rules the builds enforce by convention:** uppercase label tracking comes from
  `letterSpacing.label` (`--tracking-label` in the guide, `TRACK` in the social build), never a literal; Terracotta is
  never a text colour under 24 px (use Earth or `text.muted`, with a Terracotta rule beside it).
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
- **`build_icons.py`** draws the interface icon set (24-unit grid, 1.5 stroke, `currentColor`, no brand colour) into
  `icons/svg/`, `icons/sprite.svg` and `icons/icons-preview.png`.
- **`build_social.py`** renders Instagram tiles, carousel frames and story/reel covers from `brand/social/posts.json`
  (hand-edited; photos go in `brand/social/photos/`) into `brand/social/templates/` and `brand/social/posts/`. Frames
  are self-contained HTML with the fonts embedded, and web tokens are scaled ×3 for a 1080 px frame.
- **Fonts:** Jost and Newsreader (OFL, with `OFL.txt`) are vendored in `brand/identity/source/fonts/`, so builds work
  offline. `fetch_fonts.py` restores them from a pinned google/fonts commit, checked by SHA-256. See [DEC-0007](docs/DECISION.md#dec-0007--vendor-jost-and-newsreader-pinned-by-sha-256).
- **`render.py`** does all rasterising in one headless-Chrome session (SVG → canvas → data URL). It also handles
  SVG → PDF via `--print-to-pdf`, renders HTML pages to PNG with `screenshot()` (used by the social build) and writes
  ICO files by hand. No Python dependencies anywhere.

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

### Brand pages site (GitHub Pages)

`build_site.py` wraps `guide/arant-brand-kit.html` and `brand/design-language/arant-design-language.html` in full HTML
documents and writes them, a landing page, icon and social-template pages and only the assets they reference into
`site/`. `.github/workflows/pages.yml` runs it on push to `main` (paths `brand/**`, `packages/tokens/**`) and deploys to
https://sushant-kum.github.io/arant-design/. Keep every link inside the site relative (it is served under
`/arant-design/`). `brand/design-language/arant-design-language.html` is **hand-edited**, not generated, and
Prettier-ignored on purpose: update it whenever the design-language Markdown changes. It is also the source of the
design-language Claude artifact.

## Repo conventions and tooling quirks

- pnpm workspace: `apps/*`, `packages/*`, packages named `@arant/*`, depend with `"workspace:*"`. Dependency versions
  live in the **catalog** in `pnpm-workspace.yaml` (`catalogMode: prefer`, `minimumReleaseAge: 4320`, so brand-new
  releases are refused). `allowBuilds: unrs-resolver: false` is deliberate (its native binary installs without the
  script). See [DEC-0005](docs/DECISION.md#dec-0005--hold-dependency-versions-in-the-pnpm-catalog-with-a-release-age-gate).
- TypeScript is pinned to `~6.0.3` because typescript-eslint 8 supports TS < 6.1 ([DEC-0004](docs/DECISION.md#dec-0004--pin-typescript-to-603-for-typescript-eslint-8)). ESLint 10 uses
  `eslint-plugin-import-x` (rules are `import-x/*`), not `eslint-plugin-import`. `eslint.config.mjs` auto-discovers
  workspaces with a `tsconfig.json`; framework presets (React/Astro) are intentionally not added until the website's
  stack is chosen (see the comment in the config).
- `.agents/` and `.claude/` contain a third-party Claude Code skill (logo-generator), excluded from Ruff, Prettier,
  Stylelint, ESLint and cspell — **except** `.claude/agents/`, whose Markdown Prettier formats
  ([DEC-0010](docs/DECISION.md#dec-0010--format-claudeagents-with-prettier)). Ruff is invoked with `--force-exclude` in
  lint-staged so explicitly passed excluded files are skipped.
- Ruff: `ruff.toml`, line length 120, Python files only (Markdown code blocks are left to Prettier).
- Prettier: single quotes, printWidth 100; `.czrc` is parsed as JSON via an override.
- Git hooks (husky): pre-commit runs lint-staged (`.lintstagedrc.json`) then knip over the whole project; commit-msg
  runs commitlint (Conventional Commits, e.g. `feat(identity): …`, `fix(tokens): …`). Release tags are per area, e.g.
  `identity-v1.1`.
- No AI attribution: never add "Generated with Claude Code", "Authored by Claude Code",
  `Co-Authored-By: Claude …` / `Claude-Session: …` trailers, a 🤖 footer, or any similar AI-authorship marker to code,
  files, comments, commit messages or PRs. Commits use the human's git identity only; this overrides any default tool
  attribution. See [DEC-0009](docs/DECISION.md#dec-0009--do-not-add-ai-authorship-or-generation-attribution).
- Spelling: British English (`cspell.json`, which holds the brand word list).
- Licence: brand assets (everything in `brand/`, plus any copy of them elsewhere) are all rights reserved. Only
  `brand/identity/source/` and `packages/` are MIT, except the vendored fonts in `brand/identity/source/fonts/`
  (SIL OFL 1.1); `apps/` defaults to all rights reserved. See [DEC-0006](docs/DECISION.md#dec-0006--licence-brand-assets-all-rights-reserved-and-source-code-mit).

## Decision & Flow Records

Two documents under `docs/` carry this repo's durable memory — engineering and otherwise.
**Keeping them current is part of the work, not a follow-up.** Update them in the _same_ change as
whatever they describe — a change that alters a recorded decision or flow without touching these
docs is incomplete.

| Doc                                    | Holds                                                                       | Shape                          |
| -------------------------------------- | --------------------------------------------------------------------------- | ------------------------------ |
| [docs/DECISION.md](./docs/DECISION.md) | **Why** — technical, product, process, and team decisions; rejected options | Append-only `DEC-XXXX` entries |
| [docs/FLOW.md](./docs/FLOW.md)         | **How** — multi-step processes: code paths, pipelines, approvals, ops       | Living `FLOW-XXXX` entries     |

**Write a `DEC-XXXX` entry when:**

- A choice had a plausible alternative a reasonable person would have picked instead.
- A convention, policy, or way of working is introduced or changed.
- A dependency, tool, vendor, or service is adopted, dropped, replaced, or pinned for a non-default reason.
- A constraint or risk is knowingly accepted (cost, deadline, scope cut, tech or process debt).
- Something was tried or proposed and rejected — record it so it is not retried blindly.
- Something was agreed with another team, customer, or partner that changes how work is done here.

**Write or update a `FLOW-XXXX` entry when:**

- A process spans more than one module, system, team, or person, or takes three-plus places to understand.
- It has non-obvious failure/escalation branches, or crosses a boundary someone else owns.
- It is rare enough that people forget the steps (releases, rotations, audits, onboarding).
- An existing documented flow changes — edit it in place and bump its `Last verified` date.

**Do not write an entry for** routine work, obvious fixes, one-off tasks, or anything already
stated verbatim in `CLAUDE.md` / `AGENTS.md` / existing runbooks — link to it instead.

**Mechanics:**

- Use the entry template in each file's header; IDs are sequential and never reused.
- Add the matching row to the file's index table in the same change.
- Absolute dates (`YYYY-MM-DD`), never relative ones.
- DECISION.md is append-only: reverse a decision with a **new** entry and mark the old one
  `Superseded by DEC-XXXX`. Never rewrite an existing entry's history.
- If the source of truth and either doc disagree, the **source of truth wins** — then fix the doc.
- Before starting non-trivial work, check both files for a relevant entry; before finishing, ask
  whether the change produced a new decision or altered a flow.
- When the user states a decision or describes a process in conversation that meets the criteria
  above, offer to record it.
