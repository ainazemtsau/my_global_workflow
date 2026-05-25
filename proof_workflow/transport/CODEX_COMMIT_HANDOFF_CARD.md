---
artifact_control:
  namespace: proof_workflow
  artifact_type: transport_card
  card_type: codex_commit_handoff_card
  status: gate_3_1_initial
  owner: proof_carrying_workflow_os
---

# Codex Commit Handoff Card

## Purpose

Codex Commit Handoff Card serializes repository maintenance instructions generated after a Receipt.

Codex Commit Handoff Card is a transport adapter, not a semantic primitive.

This card is repository maintenance, not product/project execution.

It lets a user paste a complete commit task into Codex without inferring paths, validation, or commit scope from a Receipt.

## Required Shape

```yaml
codex_commit_handoff_card:
  codex_handoff_id: string
  purpose: string
  source_receipt_id: string
  source_obligation_id: string
  target_commit_scope: string
  commit_intent: string
  files_to_create:
    - path: string
      purpose: string
  files_to_update:
    - path: string
      purpose: string
  forbidden_paths: [string]
  receipt_summary: string
  ledger_delta_to_apply: object
  validation_required: [string]
  project_files_refresh_required: [string]
  commit_message: string
  push_required: boolean
  return_format: [string]
```

## Rules

- This card is repository maintenance, not product/project execution.
- It must include exact allowed paths and forbidden paths.
- It must include what must not be changed.
- It must include Project Files refresh requirements.
- It must include validation/read-back requirements.
- It must not ask the user to infer paths from the Receipt.
- It must not create additional strategic work.
- It must not admit Codex product execution, implementation work, release work, roadmap creation, Horizon selection, or Active Frontier selection.

END_OF_FILE: proof_workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md
