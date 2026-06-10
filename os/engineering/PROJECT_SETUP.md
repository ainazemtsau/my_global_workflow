# Project setup — bootstrap an agent-ready product repo

A procedure executed by a coding agent (as an engineering CALL) when a direction needs a product repository. Its product is not code — it is the **feedback loop**: a repo where autonomous builds converge fast and entropy is mechanically contained. Run once per repo; revisit only via friction.

## Step 1 — Stack interview (with the owner, short)

Check `os/engineering/profiles/<stack>.md` first: an existing profile is the entry point (conventions, boundary tooling, default thresholds, known landmines). Then ask only what the direction's CALL and profile don't answer: target platform, hard constraints, owner's stack preferences. Propose the stack with an outside view (what do shipped projects of this kind use) and record the choice as ADR-0001. If no profile exists for the chosen stack, create one as a byproduct of this setup (≤100 lines, format in `profiles/README.md`) and return it in the RESULT's `state_changes` — the writer commits it to the workflow repo (the executor never writes there directly).

## Step 2 — Architecture skeleton

- **Modular monorepo.** Modules under `src/<module>/`; each module small enough that module + its docs fit one agent context.
- **Boundaries enforced by the build graph**, not by docs: dependency-graph linting (import-linter / dep-cruiser / engine equivalent); module visibility is opt-in; violations fail CI. Agents can ignore documentation; they cannot ignore a failing check.
- **Per-module docs colocated**: each module gets its own `AGENTS.md` (nearest-file-wins): public API surface, internal conventions, gotchas. Project-wide docs live in the repo (`docs/`), never outside it.

## Step 3 — Root contract files

- `AGENTS.md` (root, ≤150 lines, command-first): what the project is, exact build/test/lint commands (single-command AND file-scoped variants), conventions, definition of done. `CLAUDE.md` = one line importing AGENTS.md + platform-specific notes. Prune on every agent mistake — this file is a feedback loop, not documentation.
- `REVIEW.md` — the validation rubric (see VALIDATION.md §rubric): severity definitions for THIS repo, always-check rules, skip rules, nit cap, file:line evidence bar.
- `docs/adr/` — architecture decision records; the agent proposes an ADR whenever it makes a decision a future session would otherwise re-litigate.
- `validation.config` — gate thresholds: retry budget, mutation kill-rate floor, escalation rules (machine-readable; the run loop reads it).
- `docs/FRICTION.md` — the repo's friction log (same format as os/FRICTION.md). Change discipline mirrors os/MAINTENANCE.md: REVIEW.md, validation.config, and the stack profile change only on an explicit owner request or ≥2 entries on the same point. Factual corrections in AGENTS.md (wrong command, wrong path) stay immediate — facts are fixed on sight, rules by friction.
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
- [ ] REVIEW.md, validation.config, docs/adr/ADR-0001, docs/FRICTION.md, openspec/ exist
- [ ] stack profile created or updated, returned in the RESULT's state_changes
- [ ] `_scratch/` exists and a seeded file in it cannot be committed
- [ ] test-hygiene gates fail on seeded violations (test outside tests/, skipped test, assertion-free test)
- [ ] notification hook fires a test push
- [ ] evaluator subagent answers a smoke question read-only

The setup CALL's RESULT reports this checklist with evidence per item.

END_OF_FILE: os/engineering/PROJECT_SETUP.md
