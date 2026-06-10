# Project setup — bootstrap an agent-ready product repo

A procedure executed by a coding agent (as an engineering CALL) when a direction needs a product repository. Its product is not code — it is the **feedback loop**: a repo where autonomous builds converge fast and entropy is mechanically contained. Run once per repo; revisit only via friction.

## Step 1 — Stack interview (with the owner, short)

Ask only what the direction's CALL doesn't answer: target platform, hard constraints, owner's stack preferences. Then propose the stack with an outside view (what do shipped projects of this kind use) and record the choice as ADR-0001.

## Step 2 — Architecture skeleton

- **Modular monorepo.** Modules under `src/<module>/`; each module small enough that module + its docs fit one agent context.
- **Boundaries enforced by the build graph**, not by docs: dependency-graph linting (import-linter / dep-cruiser / engine equivalent); module visibility is opt-in; violations fail CI. Agents can ignore documentation; they cannot ignore a failing check.
- **Per-module docs colocated**: each module gets its own `AGENTS.md` (nearest-file-wins): public API surface, internal conventions, gotchas. Project-wide docs live in the repo (`docs/`), never outside it.

## Step 3 — Root contract files

- `AGENTS.md` (root, ≤150 lines, command-first): what the project is, exact build/test/lint commands (single-command AND file-scoped variants), conventions, definition of done. `CLAUDE.md` = one line importing AGENTS.md + platform-specific notes. Prune on every agent mistake — this file is a feedback loop, not documentation.
- `REVIEW.md` — the validation rubric (see VALIDATION.md §rubric): severity definitions for THIS repo, always-check rules, skip rules, nit cap, file:line evidence bar.
- `docs/adr/` — architecture decision records; the agent proposes an ADR whenever it makes a decision a future session would otherwise re-litigate.
- `validation.config` — gate thresholds: retry budget, mutation kill-rate floor, escalation rules (machine-readable; the run loop reads it).
- Constitution section in AGENTS.md (3–7 immutable principles, e.g. "modular always", "no second source of truth", "reuse before write") — the validator checks changes against it.

## Step 4 — Toolchain (the feedback loop itself)

- Strict formatter + linter + typechecker, single command, fast; wired as save/pre-commit/CI AND as agent hooks (PostToolUse format/typecheck with failures fed back).
- Test layout: `tests/<module>/` mirroring `src/` (game engines: ONE registered test-scene root with a runner — never ad-hoc scenes). Hygiene gates from VALIDATION.md §hygiene wired into CI from day one.
- `_scratch/` — the only home for exploratory scripts/scenes; tracked dir, self-ignoring `.gitignore`; CI asserts nothing from it is committed.
- CI running mechanical + test gates on every PR.
- **OpenSpec** initialized (`openspec/`): living specs + per-change proposal/tasks/delta-specs; the change-folder lifecycle (propose → apply → verify → archive) is the contract surface with the workflow OS. Archive is part of done — stale specs are the known failure mode.
- Agent platform config: permission profile for autonomous runs (deny-list for hard nevers: force-push, secret paths, destructive ops; allow-list for project commands); evaluator subagent (read-only tools, instructed to report correctness gaps only) and cheap investigator subagent; verification procedures packaged as skills as they stabilize (side-effectful ones human-trigger-only); notification hooks (needs-input / finished) to the owner's push channel; stop-file and steer-file conventions.

## Step 5 — Harness state files

`SPEC` (per-change, from OpenSpec), feature **ledger** (machine-readable, all entries failing, not writable by the builder), `PROGRESS.md` (session handoff log), first commit.

## Done when (mechanically checkable)

- [ ] one-command check passes locally and in CI (format+lint+type+tests)
- [ ] dependency-boundary check exists and fails on a seeded violation
- [ ] root AGENTS.md ≤150 lines with working commands; ≥1 module AGENTS.md
- [ ] REVIEW.md, validation.config, docs/adr/ADR-0001, openspec/ exist
- [ ] `_scratch/` exists and a seeded file in it cannot be committed
- [ ] test-hygiene gates fail on seeded violations (test outside tests/, skipped test, assertion-free test)
- [ ] notification hook fires a test push
- [ ] evaluator subagent answers a smoke question read-only

The setup CALL's RESULT reports this checklist with evidence per item.

END_OF_FILE: os/engineering/PROJECT_SETUP.md
