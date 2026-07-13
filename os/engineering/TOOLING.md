# Tooling — adopt / adapt / skip (June 2026)

Research-based verdicts for the owner's current and candidate tools. Revisit only on friction or major ecosystem shifts.

## Verdicts

| Tool | Verdict | Why |
|---|---|---|
| **OpenSpec** | **ADOPT** (every product repo) | Spec-driven change flow (propose → apply → verify → archive) producing pure git-markdown artifacts — exactly our state model. The change folder is the natural contract surface for an engineering CALL; `verify` is a free validation hook. Lighter than alternatives (~250 lines per change vs ~800 for spec-kit). Known trap: forgetting `archive` leaves specs stale → archive is part of done_when. |
| **Taskmaster AI** | **SKIP / retire** | Its core (PRD → task graph) is absorbed by native Claude Code Tasks + plan mode + OpenSpec's tasks.md. Worse: its JSON store is a *third* task source of truth next to the workflow OS and the repo — drift by construction. Releases slowing. |
| **Basic Memory** | **SKIP / retire** | Well-built, but duplicates what we already have: knowledge as git markdown in the repo (direction `knowledge/`, repo docs, ADRs). A second knowledge store = split brain. If semantic search over our own docs is ever missed, add a search index over existing files, not a second system. |
| **Serena MCP** | **ADAPT** (off by default) | Native code navigation covers small/modular repos (which PROJECT_SETUP deliberately produces). Residual value: reference-accurate cross-file refactoring on large single-language codebases — enable per-project for exactly that, with only symbolic tools loaded. Not in the default profile (token tax). |
| **GitHub spec-kit** | **SKIP, steal one idea** | Same niche as OpenSpec but ~3x ceremony per change; built for greenfield teams. The idea worth keeping: the **constitution** — a short immutable-principles list the validator checks against — implemented as an AGENTS.md section, no toolkit needed. |
| **External review bot** (CodeRabbit / Greptile class) | **ADAPT** (one gate) | Heterogeneous reviewers have barely-overlapping blind spots; one external/cross-model pass on autonomous PRs materially raises catch rate (VALIDATION G4). One bot, as a PR gate — not an MCP inside the builder's context. |
| **Beads** | **WATCH** | Git-backed dependency-aware issue graph for agents. Overlaps with our ledger + OS tasks today; adopt only if intra-repo issue tracking outgrows the ledger (multi-agent parallelism in one repo). |
| **BMAD / Conductor-class orchestrators** | **SKIP** | Role-simulation ceremony and GUI orchestration solve problems our OS already owns (the OS is the orchestrator; worktrees cover parallelism). |

## Net effect on the owner's current Codex setup

From three always-on MCP servers (Serena, Taskmaster, Basic Memory) to **zero by default**: OpenSpec initialized per repo (files, not a server), Serena available per-project on demand, knowledge consolidated in git. Fewer tool definitions per run = lower token tax and one source of truth.

## Execution entry guard

Tool discovery is not tool authorization. For a Direction OS engineering CALL, the required runtime
is defined only by the CALL, the product repo's `AGENTS.md`, its frozen plan/spec, and
`validation.config`. A globally installed or discoverable skill/tool must not translate a generic
`to: executor`, `kind: engineering`, PLAN, or BUILD leg into another workflow or inject another
state substrate. In particular, do not infer S_E `wave_graph_plan` / `wave_execute`, Taskmaster,
Basic Memory, Serena, a Project Context Packet, or Trail of Bits bindings unless one of those
authorities explicitly opts in. The required-tool STOP applies only to a tool required by those
authorities; an unselected global tool being unbound is not a blocker.

## Native capabilities to use instead (already in the platforms)

- Claude Code: plan mode, Tasks, subagents with per-agent model routing, skills (lazy-loaded procedures), hooks (deterministic enforcement), `/goal` bounded loops, cloud sessions with mobile monitoring, Auto-fix on PRs.
- Codex: AGENTS.md, `codex exec` sandbox profiles, cloud tasks with best-of-N attempts, PLANS.md convention, native compaction for long runs.
- Both read the same root AGENTS.md (CLAUDE.md imports it) — executor stays swappable, per R-12.

END_OF_FILE: os/engineering/TOOLING.md
