# Tooling — adopt / adapt / skip (June 2026)

Research-based verdicts for the owner's current and candidate tools. Revisit only on friction or major ecosystem shifts.

## Verdicts

| Tool | Verdict | Why |
|---|---|---|
| **OpenSpec** | **ADOPT** (every product repo) | Spec-driven change flow (propose → apply → verify → archive) producing pure git-markdown artifacts — exactly our state model. The change folder is the natural contract surface for an engineering CALL; `verify` is a free validation hook. Lighter than alternatives (~250 lines per change vs ~800 for spec-kit). Known trap: forgetting `archive` leaves specs stale → archive is part of done_when. |
| **GitHub spec-kit** | **SKIP, steal one idea** | Same niche as OpenSpec but ~3x ceremony per change; built for greenfield teams. The idea worth keeping: the **constitution** — a short immutable-principles list the validator checks against — implemented as an AGENTS.md section, no toolkit needed. |
| **External review bot** (CodeRabbit / Greptile class) | **OPTIONAL** | An external pass can add diversity when available, but freshness and non-authorship define independence. It is never a required gate, and model/provider availability never blocks delivery. |
| **Beads** | **WATCH** | Git-backed dependency-aware issue graph for agents. Overlaps with our ledger + OS tasks today; adopt only if intra-repo issue tracking outgrows the ledger (multi-agent parallelism in one repo). |
| **BMAD / Conductor-class orchestrators** | **SKIP** | Role-simulation ceremony and GUI orchestration solve problems our OS already owns (the OS is the orchestrator; worktrees cover parallelism). |

## Net effect on the owner's current Codex setup

The default executor surface is repo-native: OpenSpec plus git-tracked project files and the platform's native capabilities. No separate execution substrate or second memory/task authority is installed by default.

## Execution entry guard

Tool discovery is not tool authorization. For a Direction OS engineering CALL, the required runtime
is defined only by the CALL, the product repo's `AGENTS.md`, its frozen plan/spec, and
`validation.config`. A globally installed or discoverable skill/tool must not translate a generic
`to: executor`, `kind: engineering`, PLAN, or BUILD leg into another workflow or inject another
state or tool substrate. The required-tool STOP applies only to a tool explicitly required by those
authorities; discovery or installation alone adds no requirement and an undeclared tool is never a
blocker.

## Native capabilities to use instead (already in the platforms)

- Claude Code: plan mode, Tasks, subagents with per-agent model routing, skills (lazy-loaded procedures), hooks (deterministic enforcement), `/goal` bounded loops, cloud sessions with mobile monitoring, Auto-fix on PRs.
- Codex: AGENTS.md, `codex exec` sandbox profiles, cloud tasks with best-of-N attempts, PLANS.md convention, native compaction for long runs.
- Both read the same root AGENTS.md (CLAUDE.md imports it) — executor stays swappable, per R-12.

END_OF_FILE: os/engineering/TOOLING.md
