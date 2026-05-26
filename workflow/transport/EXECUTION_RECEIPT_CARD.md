---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: execution_receipt_card
  status: gate_2_initial
  owner: workflow_os
---

# Execution Receipt Card

## Purpose

Execution Receipt Card serializes the return from one execution Operator invocation.

It is candidate state until Verify and Commit.

## Required Shape

```yaml
execution_receipt_card:
  receipt_id: string
  obligation_id: string
  operator_id: string
  target_project_ref: string
  status: satisfied | partial_success_with_residuals | blocked | failed | validation_gap | setup_gap
  changed_surfaces:
    - surface: string
      change_summary: string
  changed_files:
    - path: string
      change_summary: string
  commands_run:
    - command: string
      result: pass | fail | not_run
      evidence_ref: string
  validation_receipts:
    - receipt_id: string
  subagent_reviewer_receipts:
    - role: string
      receipt_id: string
      required_by_launch: true | false
  unresolved_risks:
    - string
  rollback_notes: string | null
  technical_memory_delta:
    module_map_updated: true | false | not_required
    technical_ledger_updated: true | false | not_required
    known_risks_updated: true | false | not_required
    notes: string | null
  ledger_delta_proposal: object | null
  commit_recommendation: commit | do_not_commit | needs_human_gate | repair_required
```

## Rules

- No validation receipt -> no done.
- Missing required reviewer/subagent receipt invalidates the Execution Receipt.
- Required technical memory updates must be recorded or the receipt is incomplete.
- Business-facing done claims must not exceed accepted validation and commit evidence.

END_OF_FILE: workflow/transport/EXECUTION_RECEIPT_CARD.md
