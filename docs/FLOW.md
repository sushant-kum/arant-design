# FLOW.md — Flow Catalogue

> **What this is.** The reference for _how_ multi-step processes actually run — code and request
> paths, build/release/deploy pipelines, approval and review chains, onboarding, incident response,
> escalation, recurring operational routines. One entry per flow, each naming the concrete
> participants (files, systems, documents, roles) that carry it out.
>
> **What this is not.** Rationale (that is [DECISION.md](./DECISION.md)) or specs. A flow entry says
> what happens, in order, who or what does it, and what happens when a step fails.
>
> **Conflict rule:** if this document and the source of truth disagree, the source of truth wins —
> then update the affected flow in the same change.

---

## How to use this file

**Write a flow when any of these is true:**

- It spans more than one module, system, team, or person.
- Understanding it today requires opening three or more files, docs, or tools — or asking someone.
- It has non-obvious failure, fallback, or escalation branches.
- It crosses a boundary someone else owns (another team, a vendor, a backend contract, a pipeline,
  an approval).
- It is done rarely enough that people forget the steps (releases, rotations, audits, offboarding).

**Do not write a flow for:** a single component's internal logic, anything a doc comment or an
existing runbook already explains (link it instead), or a sequence that lives entirely in one place.

**Rules of the catalogue:**

1. IDs are sequential (`FLOW-0001`, `FLOW-0002`, …) and never reused.
2. Every flow gets a row in the index table below, in the same change.
3. Unlike DECISION.md, flow entries are **living documents** — edit a flow in place when the
   process changes, and update its `Last verified` date. Delete a flow only when the process is
   gone, and record the removal as a `DEC-XXXX` entry.
4. Every participant must name a **concrete, checkable reference** — a file path, URL, system or
   tool name, document, or owning role/team. The entry is worthless once it drifts, and those
   references are what make drift checkable.
5. Diagrams are optional; use a fenced `mermaid` block when the branching is hard to read as
   prose. Numbered steps are mandatory.
6. Cross-link freely: `FLOW-0002`, `DEC-0001`, runbooks, tickets.

**Vocabularies for this repo** (shared with [DECISION.md](./DECISION.md)):

- **Category** (_what kind_): `engineering` · `design` · `brand` · `content` · `tooling` · `ci` ·
  `process` · `product` · `policy` · `vendor`.
- **Scope** (_where it applies_): `repo-wide` · `brand/identity` · `brand/design-language` ·
  `brand/social` · `brand/mockups` · `packages/tokens` · `apps/website` · `ci` · `.claude/agents`.

---

## Index

| ID        | Title                              | Category    | Scope          | Owner               | Last verified |
| --------- | ---------------------------------- | ----------- | -------------- | ------------------- | ------------- |
| FLOW-0001 | Identity build pipeline            | engineering | brand/identity | Studio (maintainer) | 2026-10-03    |
| FLOW-0002 | Brand pages publish (GitHub Pages) | ci          | ci             | Studio (maintainer) | 2026-10-03    |
| FLOW-0003 | Commit checks (git hooks)          | tooling     | repo-wide      | Studio (maintainer) | 2026-10-03    |

---

## Entry template

Copy this block verbatim for a new flow.

```markdown
## FLOW-XXXX — <Short noun-phrase title>

- **Category:** <engineering | design | brand | content | tooling | ci | process | product | policy | vendor>
- **Scope:** <repo-wide | brand/identity | brand/design-language | brand/social | brand/mockups | packages/tokens | apps/website | ci | .claude/agents>
- **Owner:** <role / team accountable for keeping this flow true>
- **Trigger:** what starts the flow (a user action, a request, a pushed tag, a schedule, an
  incident, a new hire, a customer request).
- **Outcome:** the successful end state.
- **Last verified:** YYYY-MM-DD
- **Related:** DEC-XXXX, FLOW-XXXX

### Participants

| Piece  | Reference (file / system / doc / role) | Role in the flow |
| ------ | -------------------------------------- | ---------------- |
| <name> | `path/to/file`, URL, or team name      | what it does     |

### Steps

1. …
2. …

### Branches & failure modes

- **<Condition>** → what happens instead, and who acts.

### Notes

Anything a reader would otherwise get wrong — ordering constraints, timing/SLA expectations,
environment differences, cross-team assumptions, access needed.
```

---

## FLOW-0001 — Identity build pipeline

- **Category:** engineering
- **Scope:** brand/identity
- **Owner:** Studio (maintainer)
- **Trigger:** a change to `packages/tokens/tokens.json` or `brand/identity/source/*.py`, then running
  `pnpm identity:build` (or an individual `identity:*` step) from the repo root.
- **Outcome:** every generated brand asset is regenerated from source and consistent with the tokens;
  SVG/PNG/ICO/JPG/HTML come out byte-for-byte identical when geometry and tokens are unchanged (PDFs
  differ only in `CreationDate`/`ModDate`).
- **Last verified:** 2026-10-03
- **Related:** [DEC-0001](./DECISION.md#dec-0001--record-decisions-in-decisionmd-and-flows-in-flowmd), [DEC-0002](./DECISION.md#dec-0002--keep-colour-and-design-values-only-in-tokensjson), [DEC-0003](./DECISION.md#dec-0003--generate-brand-assets-from-source-never-hand-edit-the-output), [DEC-0007](./DECISION.md#dec-0007--vendor-jost-and-newsreader-pinned-by-sha-256), [CLAUDE.md § Architecture: the identity build pipeline](../CLAUDE.md#architecture-the-identity-build-pipeline)

### Participants

| Piece        | Reference (file / system / doc / role)                 | Role in the flow                                                         |
| ------------ | ------------------------------------------------------ | ------------------------------------------------------------------------ |
| scripts      | `package.json` (`identity:*` scripts)                  | Define and order the pipeline steps                                      |
| token source | `packages/tokens/tokens.json`                          | The single source of colour/type/spacing/etc. values                     |
| token reader | `brand/identity/source/brand_tokens.py`                | Loads tokens; `color()`, `mix()`, `cmyk()`, `contrast()`, `role()`, …    |
| token check  | `brand/identity/source/check_tokens.py`                | Fails on hard-coded palette hex, unresolved `{alias}`, or stale mix      |
| geometry     | `brand/identity/source/build_logo.py`, `glyphs.py`     | Writes the 7 logo masters to `brand/identity/logo/svg/`                  |
| exports      | `brand/identity/source/build_exports.py`               | Recolours masters → `export/<version>/`; web icons → `export/symbol/`    |
| print        | `brand/identity/source/build_print.py`                 | PDFs (`print/pdf/`) and JPGs on ivory (`print/jpg/`) from export SVGs    |
| guide        | `brand/identity/source/build_guide.py`                 | `guide/arant-brand-kit.html` and `guide/palette.svg`                     |
| icons        | `brand/identity/source/build_icons.py`                 | `icons/svg/`, `icons/sprite.svg`, `icons/icons-preview.png`              |
| social       | `brand/identity/source/build_social.py`                | `brand/social/templates/` and `brand/social/posts/` from `posts.json`    |
| renderer     | `brand/identity/source/render.py`                      | Headless-Chrome rasterising (SVG→PNG, SVG→PDF, HTML→PNG) and ICO writing |
| fonts        | `brand/identity/source/fonts/` (Jost, Newsreader, OFL) | Vendored fonts embedded by the renderer so builds work offline           |

### Steps

1. Run `pnpm identity:build` (repo root). It runs the steps below in order via `&&` (`package.json`).
2. **`identity:check`** → `check_tokens.py`: abort if a palette hex is hard-coded in `source/*.py`, an
   `{alias}` doesn't resolve, or a recorded `mix` no longer matches the palette.
3. **`identity:logo`** → `build_logo.py` (+`glyphs.py`): write the 7 masters to `logo/svg/` in
   `logo.default` colour.
4. **`identity:exports`** → `build_exports.py`: recolour masters into `export/<version>/arant-<version>-<token>.svg|png`, and build the web icon set in `export/symbol/` (favicon.ico/.svg, PWA icons, `site.webmanifest`, `head-snippet.html`).
5. **`identity:print`** → `build_print.py`: make vector PDFs and ivory JPGs **from the export SVGs** (so it runs after exports).
6. **`identity:guide`** → `build_guide.py`: write the brand guide and `palette.svg`.
7. **`identity:icons`** → `build_icons.py`: draw the interface icon set, sprite and preview.
8. **`identity:social`** → `build_social.py`: render the Instagram templates and posts from `brand/social/posts.json`.

### Branches & failure modes

- **`identity:check` fails** → the `&&` chain stops immediately; nothing downstream is rebuilt. Fix the
  hex/alias/mix in source or tokens and re-run.
- **Chrome/Chromium missing** → the steps that rasterise (exports, print, guide, icons, social) can't
  run; set `CHROME=/path/to/chrome` (read by `render.py`).
- **Vendored fonts missing** → run `pnpm identity:fonts` (`fetch_fonts.py`) to restore pinned Jost and
  Newsreader from a pinned `google/fonts` commit (verified by SHA-256). This step **needs network** and
  is deliberately **not** part of `identity:build`.

### Notes

- **Order matters:** `print` consumes `exports`' SVGs, so never run it before `exports`.
- Everything under `brand/identity/{logo,export,print,guide,icons}/` and `brand/social/{templates,posts}/`
  is **generated — never hand-edit it**; change the source (`*.py`, `tokens.json`, `posts.json`) and rebuild.
- Verification is **rebuild-and-compare**, not a test suite: identical output means no unintended change.

---

## FLOW-0002 — Brand pages publish (GitHub Pages)

- **Category:** ci
- **Scope:** ci
- **Owner:** Studio (maintainer)
- **Trigger:** a push to `main` touching `brand/**`, `packages/tokens/**`, or `.github/workflows/pages.yml`
  (or a manual `workflow_dispatch`).
- **Outcome:** the brand pages are live at <https://sushant-kum.github.io/arant-design/>.
- **Last verified:** 2026-10-03
- **Related:** [DEC-0001](./DECISION.md#dec-0001--record-decisions-in-decisionmd-and-flows-in-flowmd), [DEC-0003](./DECISION.md#dec-0003--generate-brand-assets-from-source-never-hand-edit-the-output), [CLAUDE.md § Brand pages site (GitHub Pages)](../CLAUDE.md#brand-pages-site-github-pages), [FLOW-0001](#flow-0001--identity-build-pipeline)

### Participants

| Piece       | Reference (file / system / doc / role)                                                                                         | Role in the flow                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| workflow    | `.github/workflows/pages.yml`                                                                                                  | The `Pages` GitHub Actions workflow (build + deploy jobs)        |
| site build  | `brand/identity/source/build_site.py`                                                                                          | Wraps committed identity files into the site (stdlib, no Chrome) |
| output      | `site/` (gitignored)                                                                                                           | The built static site uploaded as the Pages artifact             |
| Actions     | `actions/checkout`, `actions/setup-python`, `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages` | Standard Pages build/deploy actions                              |
| destination | <https://sushant-kum.github.io/arant-design/>                                                                                  | The published site                                               |

### Steps

1. A push to `main` matching the path filters (or a manual dispatch) starts the `Pages` workflow.
2. **build** job: `checkout@v7` → `setup-python@v7` (Python `3.13`) → run `build_site.py` in
   `brand/identity/source` → `configure-pages@v6` → `upload-pages-artifact@v5` with `path: site`.
3. **deploy** job (`needs: build`): `deploy-pages@v5` publishes the artifact to the `github-pages`
   environment and exposes the `page_url`.

### Branches & failure modes

- **A newer push arrives mid-run** → `concurrency: { group: pages, cancel-in-progress: true }` cancels
  the waiting/running job so the latest push wins.
- **Committed identity files are stale** → `build_site.py` only wraps what is already committed (no
  Chrome, no regeneration), so the site will be stale; fix by running FLOW-0001 and committing the output.
- **Pages source not configured** → one-time setup: Settings → Pages → Build and deployment → Source:
  GitHub Actions (noted in the workflow header comment).

### Notes

- Keep every link inside the site **relative** — it is served under `/arant-design/`.
- The workflow runs only on `main`; branch pushes don't deploy.

---

## FLOW-0003 — Commit checks (git hooks)

- **Category:** tooling
- **Scope:** repo-wide
- **Owner:** Studio (maintainer)
- **Trigger:** `git commit` (hooks are installed by `pnpm install` via the `prepare: husky` script).
- **Outcome:** a commit is created only if the staged files pass lint-staged, the project passes knip,
  and the message is a valid Conventional Commit.
- **Last verified:** 2026-10-03
- **Related:** [DEC-0001](./DECISION.md#dec-0001--record-decisions-in-decisionmd-and-flows-in-flowmd), [DEC-0005](./DECISION.md#dec-0005--hold-dependency-versions-in-the-pnpm-catalog-with-a-release-age-gate), [README.md § Committing](../README.md#committing), [CLAUDE.md § Repo conventions and tooling quirks](../CLAUDE.md#repo-conventions-and-tooling-quirks)

### Participants

| Piece       | Reference (file / system / doc / role)                      | Role in the flow                                                  |
| ----------- | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| pre-commit  | `.husky/pre-commit`                                         | Runs lint-staged, then knip; aborts the commit on failure         |
| commit-msg  | `.husky/commit-msg`                                         | Runs commitlint on the message                                    |
| lint-staged | `.lintstagedrc.json`                                        | Per-glob tasks on staged files (eslint/prettier/stylelint/ruff/…) |
| token check | `pnpm run identity:check` (via lint-staged)                 | Runs when `tokens.json` or `source/*.py` are staged               |
| secretlint  | `secretlint` (via lint-staged `*`)                          | Scans every staged file for committed secrets                     |
| knip        | `knip.json`                                                 | Whole-project unused files/exports/dependencies scan              |
| commitlint  | `commitlint.config.mjs` (`@commitlint/config-conventional`) | Enforces Conventional Commits                                     |

### Steps

1. `git commit` → `.husky/pre-commit` runs `pnpm exec lint-staged --relative --concurrent false`.
2. lint-staged runs the matching tasks (`.lintstagedrc.json`): `*.{ts,tsx,mts,cts}` → `eslint --fix` +
   `prettier --write`; `*.{css,scss}` → `stylelint --fix` + `prettier --write`;
   `*.{js,mjs,cjs,html,json,md,yml,yaml}` → `prettier --write`; `*.py` → `ruff format` + `ruff check --fix`;
   `tokens.json` or `source/*.py` → `pnpm run identity:check`; `*` → `secretlint`.
3. If lint-staged passes, pre-commit runs `knip --no-config-hints` over the whole project.
4. `.husky/commit-msg` runs `commitlint --edit` to validate the message against Conventional Commits.

### Branches & failure modes

- **lint-staged fails** → the hook aborts (husky runs with `sh -e`); **knip never runs** and the commit
  is blocked.
- **knip finds unused files/exports/deps** → it prints guidance and exits 1; remove them or add an ignore
  to `knip.json`, then retry (`pnpm run knip` shows the full report).
- **Non-Conventional message** → commitlint rejects it; use `pnpm tool::commit` (commitizen) for a guided
  message such as `feat(identity): …` / `fix(tokens): …`.
- **Caveat (from the hook comment):** knip sees the **working tree**, not the staged snapshot, so an
  unstaged edit can fail the commit.

### Notes

- Committing Python files needs Ruff on `PATH` (`pipx install ruff`).
- `.claude/` and `.agents/` are excluded from the linters and cspell, so files there are hand-authored
  (secretlint still scans them) — except `.claude/agents/`, whose Markdown Prettier now formats
  ([DEC-0010](./DECISION.md#dec-0010--format-claudeagents-with-prettier)).
- Release tags are per area (e.g. `identity-v1.1`, `website-v0.1`).
