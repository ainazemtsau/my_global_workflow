# No Hollow Layer Eval

status: active_eval

## Purpose

Validate that each parent layer has evidence requirements, integration policy, and closure/escalation rules instead of merely passing messages.

## PASS checks

- Parent layer has evidence requirement.
- Parent layer has integration rule.
- Parent layer has escalation or closure rule.
- Missing child/work evidence blocks closure or is explicitly permitted by parent policy.

## WARN checks

- Parent layer is intentionally thin, and the evidence/integration/closure boundary is still explicit.
- Closure is deferred because child/work results are incomplete.

## FAIL checks

- Parent only passes messages.
- No acceptance or evidence policy exists.
- Parent closure occurs by child output alone.

## Required recovery/repair action

Block parent closure, define the missing evidence/integration/closure boundary, and require explicit acceptance/update for any state change.

END_OF_FILE: workflow_v3/evals/NO_HOLLOW_LAYER_EVAL.md
