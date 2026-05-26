---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: codex_execution_launch_card
  status: gate_2_initial
  owner: workflow_os
---

# Codex Execution Launch Card

## Purpose

Codex Execution Launch Card serializes one CodexRun over one execution Obligation.

It is a transport adapter, not semantic authority.

It is distinct from Codex Commit Handoff Card, which is repository maintenance after a Receipt.

## Required Shape

```yaml
codex_execution_launch_card:
  card_id: string
  obligation_id: string
  operator: string
  target_project:
    project_ref: string
    repository: string
    worktree: string
    branch: string
  mode: plan_only | read_only_discovery | workspace_write | validate_only | repair | review_only | project_setup
  accepted_receipts:
    - receipt_id: string
  task_statement: string
  acceptance_predicate: string
  proof_policy_ref: string
  non_goals:
    - string
  allowed_changes:
    - path_or_surface: string
  forbidden_changes:
    - path_or_surface: string
  files_or_areas_to_inspect_first:
    - path_or_surface: string
  validation_required:
    - level: L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7
      requirement: string
  subagent_reviewer_requirements:
    required:
      - role: string
        purpose: string
        receipt_required: true
    optional:
      - role: string
        purpose: string
  return_receipt_schema: execution_receipt_card
  stop_conditions:
    - string
```

## Rules

- Launch is invalid without target binding, setup status, acceptance predicate, validation plan, allowed/forbidden surfaces, verification policy, and return schema.
- Required reviewers/subagents must appear in the Execution Receipt.
- Parallel write requires proven disjoint paths or worktrees and an integration plan.
- The card does not create proof and does not mutate the Ledger.

END_OF_FILE: workflow/transport/CODEX_EXECUTION_LAUNCH_CARD.md
