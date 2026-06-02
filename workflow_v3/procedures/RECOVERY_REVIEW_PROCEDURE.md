# Recovery Review Procedure

status: active_procedure

## Purpose

Use `recovery_review` when runtime state, acceptance state, routing, evidence, or persistence may be suspect.

This procedure reviews and classifies recovery needs. It must not repair any runtime files unless a later storage update adapter package is admitted.

## Allowed operations

- read exact suspect state and evidence;
- classify contamination or missing proof;
- identify affected decisions and paths;
- propose recovery outcome and next move.

## Forbidden operations

- mutate runtime files;
- invent Direction proof state;
- retroactively accept state without explicit record;
- use old workflow/runtime evidence as accepted v3 state without accepted import/bridge policy.

## Possible outcomes

```text
accept_retroactively_with_explicit_record
supersede_record
rollback_patch_needed
repair_required
blocked_context_request
```

## Required output

```text
recovery_review_status:
suspect_state_refs:
evidence_refs:
source_read_limitations:
outcome:
storage_update_needed:
exact_next_move:
```

END_OF_FILE: workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md
