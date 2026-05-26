---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: codex_commit_handoff_card
  status: gate_3_1_initial
  owner: workflow_os
---

# Codex Commit Handoff Card

## Purpose

Codex Commit Handoff Card serializes repository maintenance instructions generated after a Receipt.

Codex Commit Handoff Card is a transport adapter, not a semantic primitive.

This card is repository maintenance, not product/project execution.

It lets a user paste one complete commit task into Codex without inferring repository, worktree, branch, mode, paths, validation, git behavior, or commit scope from a Receipt.

## Required Shape

```yaml
codex_commit_handoff_card:
  codex_handoff_id: string
  codex_run_header:
    run_title: string
    repository: string
    worktree: string
    branch: string
    mode: string
    repository_maintenance_only: true
    product_execution_allowed: false
    merge_to_main_allowed: false
  source:
    source_receipt_id: string
    source_obligation_id: string
    source_chat_context: string
    target_commit_scope: string
  purpose:
    human_summary: string
    commit_intent: string
  path_boundaries:
    allowed_paths:
      - path: string
    forbidden_paths:
      - path: string
    protected_paths:
      - path: string
  files_to_create:
    - path: string
      purpose: string
  files_to_update:
    - path: string
      purpose: string
  files_not_to_touch:
    - path: string
      reason: string
  receipt_summary: string
  ledger_delta_to_apply: object
  validation_required:
    - check: string
  project_files_refresh_required:
    - path_or_instruction: string
  git_behavior:
    confirm_clean_before_write: true
    commit_required: true
    commit_message: string
    push_required: true
    merge_to_main: false
  return_format:
    - files_created
    - files_updated
    - forbidden_paths_touched
    - validation_results
    - commit_sha
    - push_result
    - project_files_refresh_requirements
    - risks_or_deviations
```

## Rules

- The card must be copy-paste runnable as a complete Codex instruction.
- No external wrapper is allowed.
- If repository, worktree, branch, or mode are unknown, the Operator chat must not emit a commit-ready handoff; it must return `CODEX_HANDOFF_BLOCKED` with missing fields.
- A self-contained card must include exact allowed paths and forbidden paths.
- A self-contained card must state whether merge to main is allowed; default is false.
- A self-contained card must state that this is repository maintenance, not product/project execution.
- This card is repository maintenance, not product/project execution.
- It must include exact allowed paths, forbidden paths, and protected paths.
- It must include what must not be changed.
- It must include Project Files refresh requirements.
- It must include validation/read-back requirements.
- It must not ask the user to infer paths from the Receipt.
- It must not create additional strategic work.
- It must not admit Codex product execution, implementation work, release work, roadmap creation, Horizon selection, or Active Frontier selection.
- If files loaded into a ChatGPT Project are changed, the card must include Project Files refresh requirements.
- If the source Receipt is too long, the card may include a compact receipt summary plus explicit instruction to paste or attach the full Receipt below; the run header and path boundaries must still be self-contained.
- A partial handoff must not be labeled copy-paste runnable.

END_OF_FILE: transport/CODEX_COMMIT_HANDOFF_CARD.md
