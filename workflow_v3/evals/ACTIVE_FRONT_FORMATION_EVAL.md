# Active Front Formation Eval

status: active_eval

## Purpose

Validate Active Front formation quality.

## PASS checks

- Uses `workflow_v3/formation/ACTIVE_FRONT_FORMATION_RUNBOOK.md`.
- Selects from Direction Map areas.
- Shows candidate fronts and rejected/deferred alternatives.
- Includes touched tracks, bottleneck/constraint check, uncertainty reduction, evidence speed, dependency unlock, scope control, reversibility, and exit criteria.
- Does not select by preference or convenience alone.
- Does not open Work Graph before accepted front when acceptance is required.
- Returns candidate front, evidence, risks, cuts, acceptance question, Event Loop Closure, and exact next move.

## WARN checks

- Direction Map is candidate and this limitation is visible.
- Evidence is enough for candidate formation but not final acceptance.

## FAIL checks

- No source map area is named.
- No alternatives are considered.
- Selection is preference-only.
- Front becomes global backlog or roadmap.
- Acceptance is hidden.

END_OF_FILE: workflow_v3/evals/ACTIVE_FRONT_FORMATION_EVAL.md
