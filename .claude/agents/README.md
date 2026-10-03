# ARANT DESIGN · Claude Code agents

The specialist agents for the ARANT DESIGN repository. Each is a Markdown file with YAML frontmatter
(`name`, `description`, `model`, optional `tools`) and a long system prompt, auto-discovered by Claude Code from this
directory (`.claude/agents/*.md`). Invoke one with the Agent tool by its `name`, or let Claude route to it from the
`description`.

`arant-orchestrator` is the **coordination layer**: it plans a request, delegates to the right specialists, integrates
their work, runs QA and enforces human-approval gates — it does no specialist work itself.
`arant-brand-designer` is the **brand authority**. The remaining eleven are **specialists** that _consume_ the brand
system and each other's output rather than redefine it. No agent — orchestrator or specialist — overrides the canonical
brand system (identity, tokens, typography, colour, logo, design language) without an explicit, human-approved decision.

This file is a **navigation and architecture document** — it does not duplicate the agents' prompts. Read an agent's own
file for its full scope, protocol and checklist.

## Orchestration layer

`arant-orchestrator` sits above the twelve specialists. It does **no specialist work**; it `PLAN + DELEGATE + INTEGRATE

- VERIFY`.

* **Purpose & roster:** turns a cross-domain request into the minimal set of specialist tasks, in dependency order, and
  routes each to its owner (the 12 agents in the table below). It never does work a specialist owns, and never redefines
  the brand or any domain.
* **Core loop:** UNDERSTAND → CLASSIFY → PLAN → DELEGATE → COLLECT → CHECK → HANDOFF → QA → HUMAN APPROVAL (if required)
  → COMPLETE; independent tasks run in parallel only when they share no dependency.
* **Delegation & handoff:** each delegation carries objective, context, inputs, expected output, constraints,
  may/must-not-modify files, dependencies and acceptance criteria. Each specialist returns its closing report (changed
  files, decisions, assumptions, open questions, recommended next agent); the orchestrator maps that into the
  `# ARANT AGENT HANDOFF` it defines (adding the Status: COMPLETE/PARTIAL/BLOCKED/NEEDS_REVIEW). Source files travel,
  not whole conversations; every specialist re-reads the canonical repo.
* **Scope protection:** out-of-domain proposals are rerouted to the owning agent (file ownership = the table below),
  never executed silently.
* **Brand protection:** all work respects `DESIGN.md`, the tokens, identity and voice; conflicts go to
  `arant-brand-designer`, and to human approval if the canonical system itself must change.
* **QA gate:** significant deliverables pass `arant-qa-reviewer` last before approval; fixes route to the responsible
  specialist by severity (BLOCKER stops the workflow; HIGH back to the owner; MEDIUM judged; LOW/NOTE recorded).
* **Human-approval gates:** it emits `HUMAN_APPROVAL_REQUIRED` and **stops** before strategic/irreversible decisions
  (product launch/retirement, brand/logo/type/colour/`DESIGN.md` changes, major pricing, large spend or supplier orders,
  major collection/campaign, major website IA, irreversible repo-wide changes).
* **Escalation:** the same issue surviving two meaningful attempts triggers `ESCALATE_TO_HUMAN`; it never loops agents
  endlessly.
* **Claude Code mechanics:** specialists resolve **live by name** from `.claude/agents/` — **no version pinning**, no
  cloning, no supported "roster" frontmatter (the roster lives in the prompt). A standard subagent cannot spawn other
  subagents, so the orchestrator delegates with the `Agent` tool when run **at the top level**; invoked as a subagent it
  acts as a **planner/router** that returns the task plan for top-level execution. It inherits all tools (no `tools:`
  field, like the brand authority) and creates **no nested orchestrators**.

## Dependency graph

```
              ARANT ORCHESTRATOR · arant-orchestrator
          (plan · delegate · integrate · QA · approval gates)
                            │ coordinates ▼
                         ARANT BRAND
                    arant-brand-designer
               (brand system → every specialist)
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
       PRODUCT           WEB              VISUAL
       DESIGNER        DESIGNER         PRODUCTION
            │                │                │
            ▼                ▼                ▼
       PRODUCT          FRONTEND          CONTENT
     DEVELOPMENT        ENGINEER         STRATEGIST
            │
            ▼
       COMMERCIAL
        ANALYST
            │
            ▼
       PACKAGING
        DESIGNER
```

- **`arant-researcher`** supports all relevant domains — it provides evidence to any agent, and makes no decision.
- **`arant-operations`** consumes product, manufacturing, packaging and commercial information and turns it into
  repeatable operating procedures.
- **`arant-qa-reviewer`** evaluates outputs across every domain against the established ARANT rules.

Flows in words: **Product:** product-designer → product-development → commercial-analyst → packaging-designer (with a
commercial-feedback loop upward). **Brand:** brand-designer → every visual/digital agent. **Website:** brand-designer +
web-designer → frontend-engineer. **Content:** brand-designer + product-designer + visual-production →
content-strategist.

## All agents

| Agent                       | Priority    | Owns                                                                                                                  | Does not own                                                                                                 | Key dependencies                                                                                            |
| --------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `arant-orchestrator`        | Coordinator | Planning, delegation, integration, conflict detection, QA gating, human-approval gates, final synthesis               | Specialist work of any kind; redefining the brand or any domain; approving strategic decisions for the human | Delegates to all 12 specialists; reads repo canon + this registry                                           |
| `arant-brand-designer`      | ★★★★★       | Brand identity, `tokens.json`, typography, colour, logo, the design language, `DESIGN.md`                             | Product, manufacturing, commercial, packaging or operations decisions                                        | Authority for all; reads `brand/`, `packages/tokens/`                                                       |
| `arant-product-designer`    | ★★★★★       | What to make: concepts, geometry, dimensions, collections, SKU/variants, briefs (`products/`)                         | Brand, manufacturing feasibility, final pricing, code, imagery, social                                       | Reads brand-designer; feeds product-development, commercial, visual, content                                |
| `arant-product-development` | ★★★★★       | How to make it: feasibility, CALSO/casting process, moulds, finishing, QC criteria, yield (`products/active/<slug>/`) | Aesthetics, brand, final pricing, code                                                                       | Reads the product brief; feeds commercial, packaging, operations; loops design changes back                 |
| `arant-web-designer`        | ★★★★★       | Website UX specs: IA, pages, PLP/PDP, components, interaction (`apps/website/design/`)                                | Brand tokens/type/logo, frontend code, imagery production, content                                           | Reads brand-designer + tokens; feeds frontend-engineer                                                      |
| `arant-visual-production`   | ★★★★½       | Imagery and art direction, mockups, image-gen prompts (`brand/mockups/`, `brand/social/photos/`)                      | Brand rules, product design, code, commercial                                                                | Reads brand-designer + product brief; feeds content, web, packaging mockups                                 |
| `arant-content-strategist`  | ★★★★½       | Content strategy and editorial; authors `brand/social/posts.json`, `brand/social/strategy/`                           | Brand/voice authority, imagery production, the render pipeline, product, code                                | Reads brand + product + visual; extends the `brand/social/` system                                          |
| `arant-frontend-engineer`   | ★★★★        | `apps/website` implementation, `@arant/tokens` integration, a11y, build, CI                                           | Brand, UX design, product, commercial, imagery                                                               | Reads web-designer specs + tokens; surfaces conflicts upward                                                |
| `arant-commercial-analyst`  | ★★★★        | Unit economics: COGS, contribution, pricing, break-even (`commercial/`)                                               | Brand, aesthetics, code, manufacturing SOPs, social                                                          | Reads product-development BOM + product brief + packaging cost; feeds product + web/packaging               |
| `arant-packaging-designer`  | ★★★½        | Packaging system: boxes, cartons, protection, paper goods, packaging BOM (`packaging/`)                               | Identity, products, manufacturing processes, final finance                                                   | Reads brand packaging rules + dimensions + fragility + cost; feeds visual (mockups), commercial, operations |
| `arant-researcher`          | ★★★½        | Decision-tied evidence: market, competitors, materials, suppliers, benchmarks (`research/`)                           | Any decision — it provides evidence, not authority                                                           | Reads repo canon; supports all domains with sourced briefs                                                  |
| `arant-qa-reviewer`         | ★★★         | Independent review and verdict across all domains; severity-tagged findings (`qa/reviews/`)                           | The domains it reviews; it does not fix or redefine the work                                                 | Reads all canon + outputs; runs repo checks; defers external verification to the researcher                 |
| `arant-operations`          | ★★★         | Inventory, suppliers, batches, fulfilment, QC records, SOPs (`operations/`)                                           | Products, brand, pricing, manufacturing processes, marketing                                                 | Consumes product, development, packaging, commercial; QC records reviewed by qa-reviewer                    |

### Priority tiers

- **Coordinator:** `arant-orchestrator` — the coordination layer above all specialists (invoke for cross-domain work).
- **★★★★★ Core:** `arant-brand-designer`, `arant-product-designer`, `arant-product-development`, `arant-web-designer`
- **★★★★½ Core production:** `arant-visual-production`, `arant-content-strategist`
- **★★★★ Implementation / commercial:** `arant-frontend-engineer`, `arant-commercial-analyst`
- **★★★½ Supporting:** `arant-packaging-designer`, `arant-researcher`
- **★★★ Quality / later-stage:** `arant-qa-reviewer`, `arant-operations`

Priority indicates _when_ an agent is most useful (by business stage), not the quality or completeness of its
definition.

## Conventions every agent follows

- **Shared operating protocol** (inspect first · read canon first · search before creating · reuse, don't duplicate ·
  don't invent facts · mark assumptions · label Established/Recommended/Experimental · stay in scope · explain conflicts ·
  small changes · validate · report changed files · report unresolved issues and assumptions).
- **Established / Recommended / Experimental** labelling, as in `DESIGN.md`. The researcher additionally uses evidence
  labels (fact / source / observation / interpretation / assumption / hypothesis / unknown); the commercial analyst
  separates fact / assumption / estimate / scenario / recommendation; the QA reviewer uses severity labels (BLOCKER /
  HIGH / MEDIUM / LOW / NOTE); operations uses maturity labels (current / proposed / temporary workaround / SOP).
- **Human-approval gates.** Strategic or irreversible actions — product/collection launch or retirement,
  brand/logo/typography/colour/`DESIGN.md` changes, major pricing, significant spend, large inventory or supplier
  orders, major website IA, major campaigns — require human sign-off. The orchestrator centralises this
  (`HUMAN_APPROVAL_REQUIRED`); a specialist invoked **directly** still prepares the recommendation and stops for
  approval in its own domain rather than acting unilaterally.
- **No automatic git.** Agents report changed files; they never `git add`, unstage or commit unless explicitly asked
  (repo rule; see `CLAUDE.md`).
- **British English**, and prices as `₹1,800`.

## File format and model/tools

- Frontmatter: `name` (must equal the filename stem, kebab-case), `description` (a `>-` folded routing sentence),
  `model`, and (for the specialists) a scoped `tools` list. Body: single `#` H1 sections separated by `---`.
- **Model:** all agents use `model: inherit` — matching the repository's template (`arant-brand-designer`) and the only
  proven, portable value. They run on whatever model the session uses, so run reasoning/strategy sessions on a strong
  reasoning model and implementation sessions on a capable coding model. _Optional posture:_ pin `model:` to a supported
  alias (`opus`/`sonnet`) per agent if you want it fixed regardless of session.
- **Tools:** the brand authority and `arant-orchestrator` inherit all tools (no `tools` field) — the orchestrator needs
  the subagent (`Agent`) tool to delegate at the top level. The specialists are scoped:
  - Research/design/build/commercial agents (`product-designer`, `product-development`, `web-designer`,
    `visual-production`, `content-strategist`, `frontend-engineer`, `commercial-analyst`, `packaging-designer`,
    `researcher`) → `Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch` (file I/O, search, repo validation,
    external research).
  - Internal-only agents (`qa-reviewer`, `operations`) → `Read, Write, Edit, Grep, Glob, Bash` (no web: they work
    against internal artefacts and defer external verification to `arant-researcher`).
  - None are granted MCP, PR, publishing or sub-agent-spawning tools — honouring "don't grant every agent every tool".
- Files under `.claude/` are excluded from the linters and the spell-checker, so they are authored by hand — keep them
  clean and British-English. Prettier, though, **does** format this folder
  ([DEC-0010](../../docs/DECISION.md#dec-0010--format-claudeagents-with-prettier)), so keep it Prettier-clean too.

## Proposed (future) directories

Several agents own output that does not exist in the repo yet; they create these **on first real use** and mark them
Recommended until then: `products/` (product + development), `commercial/` (commercial), `apps/website/design/` (web),
`brand/mockups/briefs/` (visual), `brand/social/strategy/` (content), `packaging/` (packaging), `research/`
(researcher), `qa/reviews/` (QA, optional), `operations/` (operations).

## Not created (deliberately)

Per the design brief, these are **not** created and should not be added without an explicit request — the architecture
stays one coordinator (`arant-orchestrator`) above the specialists, with no further roles until the system has been used
and a need is shown: `arant-creative-director`, `arant-generalist`, `arant-marketing-agent`, `arant-business-agent`.
