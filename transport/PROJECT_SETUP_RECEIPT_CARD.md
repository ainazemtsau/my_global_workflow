---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: project_setup_receipt_card
  status: gate_2_initial
  owner: workflow_os
---

# Project Setup Receipt Card

## Purpose

Project Setup Receipt Card serializes setup or setup-gap evidence for a target product/project repository.

## Required Shape

```yaml
project_setup_receipt_card:
  receipt_id: string
  target_project:
    project_ref: string
    repository: string
    worktree: string
    branch: string
  project_type_profile:
    setup_mode: adapt_existing_project | create_new_project
    stack_summary: string
    examples_only_stack_labels: [string]
  agents_md_status: present | created | updated | missing | not_required
  execution_directory_status:
    project_profile: present | created | updated | missing
    validation_profile: present | created | updated | missing
    module_map: present | created | updated | missing
    technical_ledger: present | created | updated | missing
    receipts_directory: present | created | missing
  validation_profile_status: ready | partial | missing | blocked
  module_map_status: ready | partial | missing | blocked
  setup_checks:
    - check: string
      result: pass | fail | not_run
      evidence_ref: string
  setup_gaps:
    - gap: string
      blocker: true | false
      recovery_route: string
  next_allowed_execution: none | discovery_only | validate_only | workspace_write | project_setup_repair
```

## Rules

- Existing projects use `adapt_existing_project` unless an Obligation authorizes new project creation.
- `setup_gap` blocks CodexRun when the gap affects target binding, validation, allowed surfaces, or technical memory.
- Project-specific technical memory belongs in the target product/project repository.

END_OF_FILE: transport/PROJECT_SETUP_RECEIPT_CARD.md
