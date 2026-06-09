# Impact Propagation Eval

status: active_eval

## Purpose

Validate impact radius, lowest absorbing layer reasoning, and visible upstream/downstream packet use after invalidation or parent-context change.

## PASS checks

- Impact radius is stated.
- Lowest absorbing layer is considered.
- Affected parents, children, interfaces, and active work are named.
- Upstream Escalation Packet or Downstream Delta Packet is used when needed.
- Local repair is preferred when parent acceptance policy and higher claims are unaffected.

## WARN checks

- Some affected work cannot be fully assessed from available sources, and limitation is explicit.
- Human decision is required before impact can be closed.

## FAIL checks

- Route changes silently.
- Affected dependency work continues without needed delta.
- Higher claim invalidation is repaired only locally without escalation.

## Required recovery/repair action

Stop affected work, emit the needed escalation or downstream delta candidate, and require explicit next move before continuation.

END_OF_FILE: workflow_v3/evals/IMPACT_PROPAGATION_EVAL.md
