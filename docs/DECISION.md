# DECISION.md — Decision Log

> **What this is.** The durable record of _why_ things are the way they are. Every non-obvious
> decision — technical, product, process, operational, organisational, commercial — and every
> trade-off consciously accepted gets one entry here, in the format below.
>
> **What this is not.** A changelog, a task tracker, meeting minutes, or a spec. Multi-step
> processes live in [FLOW.md](./FLOW.md). Operative rules live in [CLAUDE.md](../CLAUDE.md); the
> repo-wide design contract in [DESIGN.md](../DESIGN.md); the overview in [README.md](../README.md).
>
> **Why it exists.** So that nobody — a new teammate, a reviewer, or an AI agent — has to re-derive a
> decision from scattered history, and so a decision is re-opened deliberately rather than by
> accident.
>
> **Conflict rule:** if this document and the source of truth (code, config, policy, contract, or
> the owning person/team) disagree, the source of truth wins — then update the affected entry (or
> supersede it) in the same change.

---

## How to use this file

**Write an entry when any of these is true:**

- A choice has a plausible alternative that a reasonable person would have picked instead.
- A convention, policy, or way of working is being introduced or changed.
- A dependency, tool, vendor, or service is adopted, dropped, replaced, or pinned for a
  non-default reason.
- A constraint or risk is accepted knowingly (cost ceiling, deadline trade-off, coverage floor,
  tech or process debt, a scope cut).
- Something was tried or proposed and rejected — record the rejection so it is not retried blindly.
- Something was agreed with another team, customer, or partner that affects how work is done here.

**Do not write an entry for:** routine work, obvious fixes, one-off tasks, or anything already
captured verbatim in `CLAUDE.md` / `AGENTS.md` / other docs. Link instead.

**Rules of the log:**

1. Entries are **append-only**. Never rewrite history — to reverse a decision, add a new entry and
   mark the old one `Superseded by DEC-XXXX`.
2. IDs are sequential (`DEC-0001`, `DEC-0002`, …) and never reused.
3. Every entry gets a row in the index table below, in the same change.
4. Dates are absolute (`YYYY-MM-DD`), never "last week".
5. Keep an entry short — context, decision, consequences. If it needs more than a screen, the detail
   belongs in a doc under `docs/` that the entry links to.
6. Record **who decided** (role or team, not just a name) when it isn't obvious.
7. Cross-link freely: `DEC-0003`, `FLOW-0002`, other doc sections, tickets, threads.

**Vocabularies for this repo** (keep in sync as the repo grows):

- **Category** (_what kind_): `engineering` · `design` · `brand` · `content` · `tooling` · `ci` ·
  `process` · `product` · `policy` · `vendor`.
- **Scope** (_where it applies_): `repo-wide` · `brand/identity` · `brand/design-language` ·
  `brand/social` · `brand/mockups` · `packages/tokens` · `apps/website` · `ci` · `.claude/agents`.

**Statuses:** `Accepted` · `Superseded by DEC-XXXX` · `Deprecated` · `Proposed` (only while the
change is under review — nothing stays `Proposed` on `main`).

---

## Index

| ID       | Date       | Title                                                                | Category    | Status   | Scope           |
| -------- | ---------- | -------------------------------------------------------------------- | ----------- | -------- | --------------- |
| DEC-0001 | 2026-10-03 | Record decisions in DECISION.md and flows in FLOW.md                 | process     | Accepted | repo-wide       |
| DEC-0002 | 2026-10-03 | Keep colour and design values only in tokens.json                    | engineering | Accepted | packages/tokens |
| DEC-0003 | 2026-10-03 | Generate brand assets from source; never hand-edit the output        | process     | Accepted | brand/identity  |
| DEC-0004 | 2026-10-03 | Pin TypeScript to ~6.0.3 for typescript-eslint 8                     | tooling     | Accepted | repo-wide       |
| DEC-0005 | 2026-10-03 | Hold dependency versions in the pnpm catalog with a release-age gate | tooling     | Accepted | repo-wide       |
| DEC-0006 | 2026-10-03 | Licence brand assets all-rights-reserved and source code MIT         | policy      | Accepted | repo-wide       |
| DEC-0007 | 2026-10-03 | Vendor Jost and Newsreader, pinned by SHA-256                        | vendor      | Accepted | brand/identity  |
| DEC-0008 | 2026-10-03 | Structure AI work as a 13-agent orchestrator-and-specialists system  | process     | Accepted | .claude/agents  |
| DEC-0009 | 2026-10-03 | Do not add AI-authorship or generation attribution                   | policy      | Accepted | repo-wide       |
| DEC-0010 | 2026-10-03 | Format .claude/agents with Prettier                                  | tooling     | Accepted | .claude/agents  |

---

## Entry template

Copy this block verbatim for a new entry.

```markdown
## DEC-XXXX — <Short imperative title>

- **Date:** YYYY-MM-DD
- **Status:** Accepted
- **Category:** <engineering | design | brand | content | tooling | ci | process | product | policy | vendor>
- **Scope:** <repo-wide | brand/identity | brand/design-language | brand/social | brand/mockups | packages/tokens | apps/website | ci | .claude/agents>
- **Decided by:** <role / team>
- **Related:** DEC-XXXX, FLOW-XXXX, <doc / ticket / PR / thread links>

### Context

What forced a choice. The problem, the constraints, what was true at the time.

### Decision

What we decided, stated in one or two sentences, in the active voice.

### Alternatives considered

- **<Option>** — why it was rejected.
- **<Option>** — why it was rejected.

### Consequences

- What this makes easy, and what it makes hard.
- What now has to be maintained, enforced, or watched — and by whom.
- Any follow-up work this creates, and where it is tracked.
```

---

## DEC-0001 — Record decisions in DECISION.md and flows in FLOW.md

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** process
- **Scope:** repo-wide
- **Decided by:** Studio (maintainer)
- **Related:** [FLOW.md](./FLOW.md), [CLAUDE.md § Decision & Flow Records](../CLAUDE.md#decision--flow-records)

### Context

Rationale lived only in commit messages, PR threads, chat, meetings, and people's heads. The existing
docs (`CLAUDE.md`, `DESIGN.md`, `README.md`, `brand/design-language/`) say _what_ the rules are, not
_why_. Decisions got re-litigated, and multi-step processes (the identity build, the Pages deploy,
the commit checks) had to be re-traced on every visit.

### Decision

Keep two ID-indexed documents under `docs/`, updated in the same change as what they describe:
[DECISION.md](./DECISION.md) is **append-only** (the _why_); [FLOW.md](./FLOW.md) is **edited in
place** with a `Last verified` date (the _how_).

### Alternatives considered

- **Put everything in `CLAUDE.md`** — it is an instruction file; history would drown the operative
  rules.
- **Use a wiki** — it drifts, agents can't see it, and it isn't reviewed alongside the change.
- **Rely on commit/PR messages or chat alone** — no index, and effectively invisible after the fact.

### Consequences

- Changes to architecture, conventions, policy, tooling, or a recorded process must carry a doc
  change in the same commit.
- `CLAUDE.md` stays operative and points here for rationale.
- The two index tables must stay in sync with their entries.

---

## DEC-0002 — Keep colour and design values only in tokens.json

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** engineering
- **Scope:** packages/tokens
- **Decided by:** Studio (maintainer)
- **Related:** [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline), [DEC-0003](#dec-0003--generate-brand-assets-from-source-never-hand-edit-the-output), [DESIGN.md § Canonical sources](../DESIGN.md#canonical-sources), [packages/tokens/README.md](../packages/tokens/README.md)

### Context

Colour (and other design values) could easily be written as hex literals across the Python build
scripts and, later, in website CSS/JS. That drifts, and a palette change becomes an error-prone hunt
through every file. The repo needed one authoritative place.

### Decision

Keep every colour, type, spacing, layout, radius, border and motion value in
`packages/tokens/tokens.json` (W3C Design Tokens). Build scripts read them through
`brand/identity/source/brand_tokens.py`; derived shades are `tokens.mix(...)` of palette colours,
never new literals. `check_tokens.py` fails on a hard-coded palette hex in `source/*.py`, an
unresolved `{alias}`, or a recorded `mix` that no longer matches the palette.

### Alternatives considered

- **Hex literals in each script** — drifts; a palette change means editing every file by hand.
- **A second colour source for the web (CSS vars / JS written by hand)** — a parallel system that
  diverges from `tokens.json`.

### Consequences

- One edit point for colour; `pnpm identity:check` and the pre-commit hook enforce it (see
  [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline) and
  [FLOW-0003](./FLOW.md#flow-0003--commit-checks-git-hooks)).
- The website must consume `@arant/tokens` (`workspace:*`) or generate CSS/JS from `tokens.json`
  (e.g. Style Dictionary), never hard-code values.
- `tokens.json` sits near the top of `DESIGN.md`'s "Canonical sources" hierarchy.

---

## DEC-0003 — Generate brand assets from source; never hand-edit the output

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** process
- **Scope:** brand/identity
- **Decided by:** Studio (maintainer)
- **Related:** [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline), [FLOW-0002](./FLOW.md#flow-0002--brand-pages-publish-github-pages), [DEC-0002](#dec-0002--keep-colour-and-design-values-only-in-tokensjson), [CLAUDE.md § Architecture: the identity build pipeline](../CLAUDE.md#architecture-the-identity-build-pipeline)

### Context

Logos, exports, print files, the guide, icons and social frames could be edited directly, but then
the artwork and its source diverge and the outputs stop being reproducible.

### Decision

Treat everything under `brand/identity/{logo,export,print,guide,icons}/` and
`brand/social/{templates,posts}/` as **generated**. Never hand-edit it; change the source
(`brand/identity/source/*.py`, `tokens.json`, `brand/social/posts.json`) and rebuild with
`pnpm identity:build`. VS Code marks those paths read-only and Prettier/ESLint/Stylelint ignore them.

### Alternatives considered

- **Hand-edit the artwork** — fast once, but unreproducible and drifts from source.
- **Commit only outputs, no source** — no way to regenerate, diff, or audit a change.

### Consequences

- A visual change is a source/token change plus a rebuild; verification is **rebuild-and-compare**
  (byte-identical when unchanged; PDFs differ only in metadata). See
  [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline).
- The Pages site wraps the committed generated files, so they must be rebuilt and committed to
  publish (see [FLOW-0002](./FLOW.md#flow-0002--brand-pages-publish-github-pages)).

---

## DEC-0004 — Pin TypeScript to ~6.0.3 for typescript-eslint 8

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** tooling
- **Scope:** repo-wide
- **Decided by:** Studio (maintainer)
- **Related:** [DEC-0005](#dec-0005--hold-dependency-versions-in-the-pnpm-catalog-with-a-release-age-gate), [CLAUDE.md § Repo conventions and tooling quirks](../CLAUDE.md#repo-conventions-and-tooling-quirks)

### Context

ESLint's type-aware linting runs through typescript-eslint, whose v8 line supports TypeScript below
6.1. A newer TypeScript would outrun the linter's supported range.

### Decision

Pin TypeScript to `~6.0.3` in the pnpm catalog so type-aware ESLint keeps working.

### Alternatives considered

- **Track the latest TypeScript (6.1+)** — breaks typescript-eslint 8's supported range.
- **Drop type-aware linting to free the version** — loses a class of checks.

### Consequences

- Don't bump TypeScript past 6.0.x casually; revisit when typescript-eslint supports the next TS.
- The pin lives in the catalog ([DEC-0005](#dec-0005--hold-dependency-versions-in-the-pnpm-catalog-with-a-release-age-gate)), one version for every workspace.

---

## DEC-0005 — Hold dependency versions in the pnpm catalog with a release-age gate

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** tooling
- **Scope:** repo-wide
- **Decided by:** Studio (maintainer)
- **Related:** [DEC-0004](#dec-0004--pin-typescript-to-603-for-typescript-eslint-8), [FLOW-0003](./FLOW.md#flow-0003--commit-checks-git-hooks), [CLAUDE.md § Repo conventions and tooling quirks](../CLAUDE.md#repo-conventions-and-tooling-quirks)

### Context

Dependency versions scattered across `package.json` files drift, and brand-new releases are a
supply-chain risk window.

### Decision

Centralise versions in the pnpm **catalog** (`pnpm-workspace.yaml`, `catalogMode: prefer`) and gate
freshness with `minimumReleaseAge: 4320` (3 days), refusing brand-new releases. Also
`cleanupUnusedCatalogs`, `blockExoticSubdeps`, `trustPolicy: no-downgrade`, and
`allowBuilds: { unrs-resolver: false }` (its native binary installs without the postinstall script).

### Alternatives considered

- **Per-package ranges, latest accepted immediately** — drift, plus exposure to a compromised
  just-published release.
- **Allow every postinstall build script** — unnecessary execution and security surface.

### Consequences

- A release younger than 3 days is refused until it ages; add or bump versions in the catalog, not
  per package.
- New workspaces depend via `"@arant/*": "workspace:*"` and `catalog:` entries.

---

## DEC-0006 — Licence brand assets all-rights-reserved and source code MIT

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** policy
- **Scope:** repo-wide
- **Decided by:** Studio (maintainer)
- **Related:** [DEC-0007](#dec-0007--vendor-jost-and-newsreader-pinned-by-sha-256), [LICENSE](../LICENSE)

### Context

The repo mixes all-rights-reserved brand assets with reusable, shareable source code, so a single
licence can't be right for everything.

### Decision

Split licensing (see `LICENSE`): brand assets (everything in `brand/`, and any copy elsewhere) are
**all rights reserved**; `brand/identity/source/` and `packages/` are **MIT**; the vendored fonts are
**SIL OFL 1.1**; `apps/` defaults to all rights reserved unless its folder carries its own licence.

### Alternatives considered

- **One permissive licence for everything** — would give away the brand assets.
- **One restrictive licence for everything** — would stop the tokens and build code being reused or
  shared.

### Consequences

- Contributors and consumers must respect the per-area licence; new code under `apps/` is
  all-rights-reserved unless it adds a licence file.
- Press, printers and manufacturers may use the brand assets only with written permission (identity
  README).

---

## DEC-0007 — Vendor Jost and Newsreader, pinned by SHA-256

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** vendor
- **Scope:** brand/identity
- **Decided by:** Studio (maintainer)
- **Related:** [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline), [DEC-0006](#dec-0006--licence-brand-assets-all-rights-reserved-and-source-code-mit), [CLAUDE.md § Architecture: the identity build pipeline](../CLAUDE.md#architecture-the-identity-build-pipeline)

### Context

The identity build renders real type (Jost, Newsreader). Fetching fonts at build time makes builds
network-dependent and non-reproducible; relying on system fonts renders inconsistently.

### Decision

Vendor Jost and Newsreader (with `OFL.txt`) in `brand/identity/source/fonts/` so builds work offline.
`fetch_fonts.py` restores them from a pinned `google/fonts` commit, verified by SHA-256.
`pnpm identity:fonts` does the refresh, needs network, and is deliberately **not** part of
`pnpm identity:build`.

### Alternatives considered

- **Download fonts during each build** — network dependency; non-reproducible; breaks offline.
- **Rely on system-installed fonts** — inconsistent metrics and rendering across machines and CI.

### Consequences

- Builds are offline and reproducible; the renderer embeds the vendored files (see
  [FLOW-0001](./FLOW.md#flow-0001--identity-build-pipeline)).
- Updating fonts means running `pnpm identity:fonts` (network) and re-pinning the commit/SHA.
- The fonts keep their SIL OFL 1.1 licence ([DEC-0006](#dec-0006--licence-brand-assets-all-rights-reserved-and-source-code-mit)).

---

## DEC-0008 — Structure AI work as a 13-agent orchestrator-and-specialists system

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** process
- **Scope:** .claude/agents
- **Decided by:** Studio (maintainer)
- **Related:** [.claude/agents/README.md](../.claude/agents/README.md), [CLAUDE.md § Specialist agents](../CLAUDE.md#specialist-agents), [DEC-0002](#dec-0002--keep-colour-and-design-values-only-in-tokensjson), [DEC-0003](#dec-0003--generate-brand-assets-from-source-never-hand-edit-the-output)

### Context

The studio wanted repeatable, scoped AI assistance across brand, product, manufacturing, web, visual,
content, commercial, packaging, research, QA and operations. A single general-purpose agent would blur
domain ownership, could silently redefine the brand system, and would be hard to keep in scope or review.

### Decision

Run AI work through a 13-agent Claude Code system under `.claude/agents/`: one coordination layer
(`arant-orchestrator`) above 12 domain specialists (`arant-brand-designer` as brand authority plus
eleven consuming specialists). Specialists consume the brand system rather than redefine it; frontmatter
uses `model: inherit` with scoped `tools` (the orchestrator and brand authority inherit all); each
specialist has single-owner scope and an explicit "what you do NOT own" boundary; human-approval and QA
gates are centralised in the orchestrator.

### Alternatives considered

- **One general-purpose ARANT agent** — blurs ownership, easily redefines the brand, hard to keep scoped or review.
- **Pin each agent to a specific model (opus/sonnet per role)** — deviates from the repo's `model: inherit` template and is less portable; the recommended per-role posture is documented in the registry instead.
- **Grant every agent all tools** — against least-privilege; the eleven specialists are scoped (orchestrator and brand authority inherit all).
- **Nested orchestrators / sub-coordinators** — standard Claude Code subagents can't spawn subagents, and it adds complexity; kept a single coordination layer.

### Consequences

- New or changed agent behaviour is a change under `.claude/agents/` (excluded from the linters, so authored by hand); keep `.claude/agents/README.md` in sync.
- The orchestrator delegates at the **top level** (a subagent can't spawn subagents); invoked as a subagent it acts as a planner/router.
- `model: inherit` means agents follow the session's model; pin per agent only to override.
- Specialists defer out-of-domain work to its owner, and no agent overrides the canonical brand system (tokens, identity, voice) without human approval.

---

## DEC-0009 — Do not add AI-authorship or generation attribution

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** policy
- **Scope:** repo-wide
- **Decided by:** Studio (owner)
- **Related:** [CLAUDE.md § Repo conventions and tooling quirks](../CLAUDE.md#repo-conventions-and-tooling-quirks)

### Context

Tools (Claude Code included) default to stamping AI attribution onto their output — commit trailers
like `Co-Authored-By: Claude …` / `Claude-Session: …`, a "🤖 Generated with Claude Code" pull-request
footer, or "generated/authored by Claude" markers in code or files. The studio does not want that
noise in the repository's history, files, or pull requests.

### Decision

Never add AI-authorship or generation attribution — "Generated with Claude Code", "Authored by Claude
Code", `Co-Authored-By: Claude …` / `Claude-Session: …` trailers, a 🤖 footer, or anything similar — to
code, files, comments, commit messages, or pull requests. Commits and PRs are authored under the
human's identity only. This overrides any default Claude Code attribution guidance.

### Alternatives considered

- **Keep the tool's default attribution trailers/footers** — rejected: unwanted noise in history and
  PRs, and it advertises the tooling.
- **Decide case by case** — rejected: inconsistent and easy to forget; a blanket rule is clearer.

### Consequences

- Commit messages carry no `Co-Authored-By` / `Claude-Session` (or similar) trailers; PR descriptions
  carry no "Generated with Claude Code" footer; no "generated by" markers in code or files.
- Agents and contributors must strip such lines even when a tool adds them by default.
- Supersedes the session-start attribution reminder, which itself defers to the user's own
  instructions (`CLAUDE.md` / this entry).

---

## DEC-0010 — Format .claude/agents with Prettier

- **Date:** 2026-10-03
- **Status:** Accepted
- **Category:** tooling
- **Scope:** .claude/agents
- **Decided by:** Studio (owner)
- **Related:** [CLAUDE.md § Repo conventions and tooling quirks](../CLAUDE.md#repo-conventions-and-tooling-quirks), [DEC-0008](#dec-0008--structure-ai-work-as-a-13-agent-orchestrator-and-specialists-system)

### Context

`.agents/` and `.claude/` were excluded from every formatter and linter because `.claude/skills/` holds
a vendored third-party skill that must not be reformatted. But `.claude/agents/` now holds the 13
maintained ARANT agent definitions ([DEC-0008](#dec-0008--structure-ai-work-as-a-13-agent-orchestrator-and-specialists-system)) — real, reviewed Markdown that benefits from the same consistent formatting as the rest of the repo.

### Decision

Format `.claude/agents/` with Prettier. `.prettierignore` ignores `.claude/*` but re-includes
`!.claude/agents/`, so the agent definitions are checked and formatted (directly and via lint-staged)
while the third-party skills under `.claude/skills/` and all of `.agents/` stay ignored.

### Alternatives considered

- **Keep all of `.claude/` excluded** — rejected: the agent definitions drift in style and are never
  auto-checked.
- **Un-ignore all of `.claude/`** — rejected: would reformat the vendored third-party skill under
  `.claude/skills/`.

### Consequences

- `.claude/agents/*.md` are formatted by Prettier and checked on commit (lint-staged); keep them clean.
- Only Prettier changed — ESLint/Stylelint/Ruff don't apply to these Markdown files, and cspell still
  excludes `.claude/`.
- The "authored by hand / excluded from formatters" notes in `CLAUDE.md`, the agent registry and
  FLOW-0003 are updated to record the exception.
