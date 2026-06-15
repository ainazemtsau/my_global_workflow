# Validation — the gate pipeline

The strictest practical validation for autonomously-built code. Gates run cheap-to-expensive; a change is done only when all gates are green with attached evidence. Thresholds live in the repo's `validation.config`; rubric in its `REVIEW.md`. Per-repo customization changes thresholds and rubric content — never the gate order or the independence rules. Threshold and rubric changes follow the repo's `docs/FRICTION.md` discipline: an explicit owner request, or ≥2 entries on the same point.

## Gates

**G0 — Contract freeze (before build).** Acceptance criteria per feature, machine-readable, negotiated with the validator before code exists. The builder cannot edit them. No criteria → no build.

**G1 — Mechanical.** Format, strict lint, typecheck, dependency-boundary check, dead-code / unused-export check, duplicate-helper detection, rules against hardcoded values/secrets/magic literals. One command; runs constantly (hooks), not just at the end.

**G2 — Tests.** Full suite green and deterministic. Coverage % is NOT a gate — agent-written tests look good and lie (measured ~57% mutation kill rate). The gate is **diff-scoped mutation testing** ≥ the configured kill-rate floor, plus property-based tests for core logic.

**G3 — Executed end-to-end.** A scripted scenario per feature (run the app / drive the UI headlessly / hit the API and assert on state), executed by the validator. This covers what line review is structurally blind to: missing behavior, state, sequencing.

**G4 — Independent line-level review.** Fresh-context, read-only reviewer that did not author the code; at least one pass by a different model family (self-preference bias is measured and grows with capability). Driven by REVIEW.md: binary checklist items, `file:line` evidence required for every claim, intent-vs-diff matching against the approved spec, absence checks phrased as required-presence assertions ("every new route has an authz check: yes/no"), value-bearing/measured fields asserted EQUAL to their source rather than merely present ("on-wire bytes == bytes actually sent: yes/no") and tests pinning a claim's MEANING not its form/schema, every negative control shown REACHABLE by a real run rather than a synthetic fixture (a control no real execution or mutant can trip is dead). For critical modules: two heterogeneous reviewers, union of findings (reviewer blind spots barely overlap).

**G5 — Finding verification.** Each candidate finding is confirmed against actual code behavior before it counts as a failure — the false-positive filter that keeps the loop from chasing ghosts.

**G6 — Owner spot-check (the final report).** Severity-tallied summary, diff stats, ledger state, cost — plus **manual acceptance instructions generated from the same scripts G3 ran**. Mandatory owner decisions regardless of gates: new dependencies, contract changes, tier-2 actions, escalations.

## Retry & escalation policy (uniform across gates)

- A failed gate returns its findings verbatim into the next attempt — retries without the findings are wasted.
- ≤2 retries in-context, then 1 fresh-context retry with a rewritten prompt. Hard cap 3 per gate.
- The same finding class recurring twice = non-convergence → stop immediately, don't burn the rest of the budget.
- Escalation to the owner is a designed terminal state, not a failure: budget exhausted, non-convergence, or an out-of-plan decision. The escalation carries the question, the findings, and 2–3 options with a recommendation.

## Test hygiene (mechanical, wired into CI at setup)

1. Tests only under `tests/<module>/` mirroring `src/` (engines: one registered test-scene root). Any test-like file elsewhere fails CI.
2. Orphaned test files (source gone) fail CI.
3. `_scratch/` contents never reach a commit (self-ignoring gitignore + CI assert).
4. No skipped/disabled tests on main (grep-gate).
5. No sleep-waits / real network / real clock in unit tests; changed-file suite runs twice — differing results = flaky = fail.
6. Every test asserts something (assertion-free tests fail lint).
7. Dead-code and duplicate-utility gates (unused exports fail; similarity checker over helper dirs).
8. Test-to-source ratio budget per module — a tripwire that flags sprawl for review instead of letting it accumulate.

Rule 1+3 together are the direct answer to "test scenes multiplied across the game project": scenes have exactly one legal home with a runner, throwaways have exactly one legal home that cannot be committed.

END_OF_FILE: os/engineering/VALIDATION.md
