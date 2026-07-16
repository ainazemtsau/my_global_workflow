# Stack profile: typescript-node

First created 2026-06-16 (solmax/g-kernel/t-1). Format: `profiles/README.md`.

## 1. Module conventions

- Modules live under `src/<module>/`; each module exposes only `index.ts`.
- Each module has colocated `AGENTS.md`.
- Cross-module access goes through public `index.ts` exports.
- Dependency boundaries are enforced by dependency-cruiser or equivalent graph lint.

## 2. Default validation.config thresholds

- Retry budget: 3 per gate, then stop and report evidence.
- Required gates: format, lint, typecheck, boundary, hygiene, tests, **G2 diff-scoped mutation
  (Stryker) ≥ the `mutation_kill_floor` config key, score recorded for the deliver check**, deliver report.
- Deliver report path: root `RESULT.md`, with required fields:
  outcome, evidence, assumptions, cuts, cost, manual-acceptance, next.
- Deliver (`-Deliver`/equivalent) also enforces the strong-check enablement gate (PROJECT_SETUP §Strong-check
  enablement): recorded mutation score ≥ floor + a non-empty spec-silence-audit section in the frozen change spec.

- **Contract v24 mutation scope:** `-Deliver` independently derives changed mutation-eligible `src/**` files from the authoritative review diff and fails before score comparison if any is absent from the report's normalized explicit `scopeFiles`. The fresh reviewer derives that scope and runs mutation; builder-authored globs/reports/scores are not evidence. The runner derives exact file inputs from the diff and defaults concurrency to `min(24, max(4, floor(logicalProcessors / 2)))` (explicit override recorded). Scope is file-scoped, not line-scoped: a touched hot source file is mutated whole and may still take a long time.

**Contract v24 diff identity:** the run contract declares the integration-base ref and mutation-input roots (`src/**`, mutation tests/project, mutation/check tooling and config). Independent review evidence pins mutation-reviewed `H`; the report echoes `I` (current base-ref tip), `B = merge-base(I,H)`, and `H`. Deliver recomputes and exact-matches the tuple, rejects any dependency-root change after `H`, mutates rename destinations/current A/C/M/T source files, and exact-matches deleted/rename-source paths in `removedFiles` before score.

## 3. Test layout

- Tests live under `tests/<module-or-scope>/`.
- Test hygiene fails skipped tests, assertion-free tests, and test files outside `tests/`.
- Seeded proof scripts may create temporary violations, but must clean them up.

## 4. Known landmines + mechanical fixes

- Windows-generated npm lockfiles may diverge from Linux CI optional peer metadata.
  Fix by pinning npm in `packageManager` and CI before `npm ci`.
- Seeded proof scripts must not run in parallel with normal gates if they create
  temporary violating files under `src/` or `tests/`.
- RESULT gates must reject under-filled fields, not only missing headings.

## 5. Setup notes

- Use Node 22 for CI and local checks.
- Keep OpenSpec under `openspec/changes/<change-id>/`; archive only after green implementation.
- `_scratch/` is tracked only via `_scratch/.gitignore`; generated scratch contents stay ignored.

END_OF_FILE: os/engineering/profiles/typescript-node.md
