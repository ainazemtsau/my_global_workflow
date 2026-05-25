---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: validation_receipt_card
  status: gate_2_initial
  owner: proof_carrying_workflow_os
---

# Validation Receipt Card

## Purpose

Validation Receipt Card serializes validation evidence for one validation Obligation or execution return.

## Required Shape

```yaml
validation_receipt_card:
  receipt_id: string
  validation_obligation_id: string
  target_project_ref: string
  validation_matrix:
    - level: L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7
      required: true | false
      omitted_status: not_omitted | not_required | unavailable
      reason: string | null
      result: pass | fail | not_run | blocked
  commands_or_checks_run:
    - command_or_check: string
      level: string
      result: pass | fail | not_run | blocked
      evidence_ref: string
  evidence:
    - evidence_id: string
      summary: string
      source_ref: string
  failures:
    - failure: string
      affected_level: string
      repair_required: true | false
  validation_gaps:
    - gap: string
      recovery_route: string
      human_action_card_required: true | false
  commit_allowed: true | false
```

## Rules

- Each required validation level must pass or block commit.
- Each omitted level must be marked `not_required` with reason.
- Validation unavailable must be recorded as `validation_gap`.
- No validation receipt -> no done.

END_OF_FILE: proof_workflow/transport/VALIDATION_RECEIPT_CARD.md
