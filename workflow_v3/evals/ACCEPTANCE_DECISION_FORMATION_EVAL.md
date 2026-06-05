# Acceptance Decision Formation Eval

status: active_eval

## Purpose

Validate Acceptance Decision formation quality.

## PASS checks

- Uses the registered canonical `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` source; if the procedure is still a stub, it stops with `PROCEDURE_BODY_NOT_AUTHORED`.
- Separates result quality from acceptance.
- Includes candidate result ref, evidence refs, accepted changes, rejected changes, repair/block/park options, state mutation authorization, and residual risk.
- Prevents adapter self-acceptance.
- Produces explicit next move for storage update, repair, block, park, or stop.

## WARN checks

- Evidence supports repair rather than acceptance.
- Human reviewer must decide before state mutation.

## FAIL checks

- Adapter accepts its own output.
- Evidence refs are missing.
- Acceptance is implied from validation or file existence.
- State mutation authorization is unclear.
- Acceptance review performs direct repository write without Storage Update Package / `storage_update` admission, or external utility write without Utility Use Gate and verified return.
- Producing adapter accepts or writes its own output.

END_OF_FILE: workflow_v3/evals/ACCEPTANCE_DECISION_FORMATION_EVAL.md
