# Acceptance Decision Formation Runbook

status: active_formation_runbook

## Trigger

Use when a candidate result, entity, Codex output, evidence packet, or state update needs explicit accept/reject/repair/block/park decision.

## Inputs

- candidate result reference;
- evidence references;
- proposed state changes;
- reviewer or decision source;
- known risks and limitations;
- return destination.

## Source reads

Read the candidate result, evidence, validation output, affected state/templates, and allowed path/surface boundaries. Do not allow the producing adapter to accept its own output.

## Formation steps

1. Confirm the target is Acceptance Decision only.
2. Classify candidate, evidence, reviewer authority, and affected state.
3. Frame what may change if accepted.
4. Generate decision options: accept, reject, repair, block, park.
5. Define criteria: evidence sufficiency, scope compliance, validation, residual risk, reversibility, and state mutation authority.
6. Identify evidence gaps and failure conditions.
7. Attack result quality separately from acceptance, adapter self-acceptance, hidden state mutation, and unverified claims.
8. Cut unrelated changes and future improvements.
9. Draft the decision fields.
10. Record rejected/deferred options.
11. State read limitations.
12. Ask the human or authorized reviewer to confirm when required.
13. Close the event loop.
14. Provide exact next move for storage update, repair, block, or stop.

## Must include

- candidate result ref;
- evidence refs;
- accepted changes;
- rejected changes;
- repair/block/park options;
- state mutation authorization;
- residual risk;
- no adapter self-acceptance.

## Outputs

Return an Acceptance Decision candidate compatible with `workflow_v3/templates/ACCEPTANCE_DECISION_TEMPLATE.md`.

## Acceptance boundary

The Acceptance Decision itself must be explicit and sourced before mutating accepted state.

## Stop conditions

Stop if evidence is missing, reviewer authority is unclear, the producing adapter is trying to self-accept, or affected state paths are unclear.

## Run-surface boundary

`acceptance_review` is separate from `storage_update_adapter`.

The producing adapter cannot accept or write its own output.

State mutation authorization must dispatch to a Storage Update Package and storage update adapter admission, not self-execute.

Acceptance review must not mutate repository state, update CURRENT_STATUS, update CURRENT_NEXT_MOVE, persist Event Loop Closure files, launch Codex, or continue to the semantic next step.

END_OF_FILE: workflow_v3/formation/ACCEPTANCE_DECISION_FORMATION_RUNBOOK.md
