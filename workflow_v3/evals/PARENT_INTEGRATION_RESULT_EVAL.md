# Parent Integration Result Eval

status: active_eval

## Purpose

Validate parent integration fan-in, evidence comparison, missing evidence handling, and typed output boundaries.

## PASS checks

- Required child/work results are accounted for.
- Evidence is compared to parent criteria.
- Missing and conflicting evidence are visible.
- Decision is one of continue, repair, replan, close, escalate, delta, or stop.
- Any Graph Delta, Upstream Escalation Packet, or Downstream Delta Packet is referenced instead of hidden route change.

## WARN checks

- Parent closure is partial, and the parent acceptance policy explicitly permits partial closure.
- Conflicts remain but are named and routed to repair, escalation, or stop.

## FAIL checks

- Missing evidence is synthesized.
- Child output accepts parent.
- Parent closure occurs without required child/work results.

## Required recovery/repair action

Block synthesis, request missing evidence or repair, and keep parent state candidate until explicit acceptance/update path.

END_OF_FILE: workflow_v3/evals/PARENT_INTEGRATION_RESULT_EVAL.md
