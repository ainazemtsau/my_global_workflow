# Active Unresolved Cut Eval

status: active_eval

## Purpose

Validate that Active Unresolved Cut selection identifies the meaningful unresolved graph frontier without activating the whole Direction.

## PASS checks

- Cut derives from unresolved root path nodes.
- Candidate fronts trace to cut nodes.
- Selection criteria include evidence value, risk, dependency, reversibility, WIP/capacity, and success-dimension balance.
- Blocking gates and deferred dimensions are visible.

## WARN checks

- Cut is provisional because graph evidence is incomplete, and the limitation is explicit.
- Multiple candidate cuts exist and the selected one is justified as candidate.

## FAIL checks

- Front is selected by preference only.
- Whole Direction becomes active.
- Cut lacks graph/root path trace.

## Required recovery/repair action

Block Active Front selection, repair graph trace and selection rationale, then rerun or re-enter the Active Front formation boundary.

END_OF_FILE: workflow_v3/evals/ACTIVE_UNRESOLVED_CUT_EVAL.md
