---
artifact_control:
  namespace: workflow
  artifact_type: transport_card
  card_type: codex_commit_handoff_card
  status: project_instruction_budget_hardened
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
    branch_policy: "review_branch_required|direct_to_main_allowed"
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
  worktree_policy:
    use_existing_direction_worktree: boolean
    do_not_switch_to_local_main: true
    do_not_use_global_main_worktree: true
    ignore_unrelated_untracked_paths_unless_they_overlap_allowed_paths: true
    stop_on_unrelated_tracked_changes_unless_explicitly_allowed: true
  main_update_policy:
    auto_update_origin_main_after_validation: boolean
    method: "review_branch_push|push_HEAD_to_origin_main_after_fetch_and_rebase"
    require_clean_rebase_onto_origin_main: boolean
    retry_once_on_non_fast_forward_push_rejection: boolean
    verify_origin_main_sha_after_push: boolean
    stop_on_conflict: true
    stop_on_validation_failure: true
    stop_on_forbidden_paths_changed: true
    stop_on_unexpected_changed_files: true
  receipt_summary: string
  ledger_delta_to_apply: object
  validation_required:
    - check: string
  project_instruction_ui_payload_char_counts:
    - path: string
      chars: integer
      status: "target|warning|pass|fail"
  project_refresh_instructions_after_commit:
    project_instruction_ui_update_required:
      - instruction: string
    project_sources_files_refresh_required:
      - path_or_instruction: string
    request_only_sources_refresh_required:
      - path_or_instruction: string
    do_not_upload_as_project_file:
      - path: string
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
    - project_instruction_ui_payload_char_counts
    - commit_sha
    - push_result
    - branch_policy_used
    - worktree_policy_used
    - main_update_policy_used
    - auto_main_update_attempted
    - rebase_result
    - push_target
    - origin_main_sha_after_push
    - local_head_sha
    - direct_to_main_eligibility_result
    - direct_to_main_blockers
    - whether_user_merge_turn_required
    - project_instruction_ui_update_required
    - project_sources_files_refresh_required
    - request_only_sources_refresh_required
    - do_not_upload_as_project_file
    - risks_or_deviations
```

## Rules

- The card must be copy-paste runnable as a complete Codex instruction.
- No external wrapper is allowed.
- If repository, worktree, branch, or mode are unknown, the Operator chat must not emit a commit-ready handoff; it must return `CODEX_HANDOFF_BLOCKED` with missing fields.
- A self-contained card must include exact allowed paths and forbidden paths.
- A self-contained card must state whether merge to main is allowed; default is false.
- A self-contained card must include `branch_policy`; valid values are `review_branch_required` and `direct_to_main_allowed`.
- If `branch_policy` is absent, ambiguous, or unsupported, Codex must assume `review_branch_required`.
- `merge_to_main_allowed` and `git_behavior.merge_to_main` describe a separate merge step or local-main workflow. Direct-to-main fast path authorization requires `branch_policy: direct_to_main_allowed` plus `main_update_policy`.
- A self-contained card must state that this is repository maintenance, not product/project execution.
- This card is repository maintenance, not product/project execution.
- It must include exact allowed paths, forbidden paths, and protected paths.
- It must include what must not be changed.
- It must include separated project refresh requirements for Project Instructions UI, Project Files/Sources, request-only sources, and do-not-upload instruction sources.
- It must include validation/read-back requirements.
- It must not ask the user to infer paths from the Receipt.
- It must not create additional strategic work.
- It must not admit Codex product execution, implementation work, release work, roadmap creation, Horizon selection, or Active Frontier selection.
- If files loaded into a ChatGPT Project are changed, the card must include `project_sources_files_refresh_required`.
- If Project Instructions source files change, the card must include `project_instruction_ui_update_required` and `do_not_upload_as_project_file`.
- If Project Instructions source files change, the card must include `project_instruction_ui_payload_char_counts` for every changed instruction source.
- If request-only packs or exact sources change, the card must include `request_only_sources_refresh_required`.
- The card must not list `project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md` under Project Files/Sources refresh.
- The card must not group Project Instructions UI updates under Project Files/Sources refresh.
- Project Instructions UI payload count status must use: `target` for <= 6,500 chars, `warning` for > 7,200 chars and <= 8,000 chars, `pass` for > 6,500 chars and <= 7,200 chars, and `fail` for > 8,000 chars.
- If the source Receipt is too long, the card may include a compact receipt summary plus explicit instruction to paste or attach the full Receipt below; the run header and path boundaries must still be self-contained.
- A partial handoff must not be labeled copy-paste runnable.

## Branch Policy Semantics

`review_branch_required` is the default and fallback.

Use `review_branch_required` for workflow core changes, docs/setup changes, Project setup changes, migrations, multi-Direction changes, product implementation, execution packages, legacy imports, risky commits, uncertain validation, conflicts, ambiguous policy, or any case where exact changed paths cannot be verified.

`direct_to_main_allowed` may be used only for a future eligible simple single-Direction proof-state Codex commit.

Direct-to-main eligibility requires all criteria to pass:

- the commit is a simple single-Direction proof-state commit;
- every changed path is inside one Direction's active workflow payload path;
- the handoff has exact `allowed_paths` and `forbidden_paths`;
- no `workflow/**`, `docs/**`, `project_setup/**`, `project_files/**`, `archive/**`, product implementation, execution package, migration, multi-Direction, or legacy import paths are changed;
- validation passes;
- the current worktree can be cleanly rebased onto `origin/main`;
- `origin/main` can be updated safely.

Simple single-Direction proof-state shape is limited to the exact paths authorized by the handoff within this general area:

```text
directions/<direction-id>/workflow/LEDGER.md
directions/<direction-id>/workflow/OBLIGATIONS.md
directions/<direction-id>/workflow/RECEIPTS_INDEX.md
directions/<direction-id>/workflow/DASHBOARD.md
directions/<direction-id>/workflow/COMMIT_SCOPES.md
directions/<direction-id>/workflow/MIGRATION_RECEIPT.md
directions/<direction-id>/workflow/receipts/**
directions/<direction-id>/workflow/projections/**
```

This general shape defines eligibility only. The exact handoff `allowed_paths` still controls each run. Codex must not edit every listed file by default.

## Direct-To-Main Algorithm

When `branch_policy: direct_to_main_allowed` and eligibility passes, Codex may update `origin/main` directly from the existing Direction worktree after validation.

Codex must not switch to local `main`.

Codex must not use the global main worktree.

Algorithm:

1. Record starting branch and status with `git status --short --branch` and `git branch --show-current`.
2. Stay in the current Direction worktree/branch unless the handoff explicitly says otherwise.
3. Fetch main with `git fetch origin main`.
4. If current branch is behind or `origin/main` advanced, run `git rebase origin/main`; on conflict, stop and return `NEEDS_INPUT` with exact conflicted files.
5. Apply only the requested edits.
6. Validate before commit: `git status --short`, `git diff --check`, verify only allowed paths changed, verify no forbidden paths changed, verify `END_OF_FILE` markers where applicable, and run all handoff-specific proof-state consistency checks.
7. Stage only exact allowed changed files with `git add -- <exact allowed changed files>`.
8. Validate staged state with `git diff --cached --check` and verify staged files are only allowed paths.
9. Commit with the handoff commit message.
10. Fetch and rebase again with `git fetch origin main` and `git rebase origin/main`; on conflict, stop and return `NEEDS_INPUT`.
11. Re-run post-rebase validation on the final commit: `git diff --check HEAD^ HEAD`, verify only allowed paths are in `HEAD^..HEAD`, verify no forbidden paths, and run handoff-specific consistency checks again.
12. Push current HEAD directly to `origin/main` with `git push origin HEAD:main`.
13. If non-fast-forward push rejection occurs, retry once: fetch, rebase, re-run validation, and push `HEAD:main`; if it still fails, stop and return `NEEDS_INPUT`.
14. Verify remote main with `git rev-parse HEAD` and `git ls-remote --heads origin main`; the `origin/main` SHA must equal local HEAD.
15. Return `DONE` and do not ask the user to send a separate "merge to main" command.

Stop conditions include validation failure, rebase conflict, forbidden paths changed, unexpected changed files, unrelated tracked changes that would be affected, `origin/main` update failure after one retry, explicit `review_branch_required`, core/setup/product/migration/multi-Direction/legacy paths changed, or inability to verify the exact changed-file set.

## Examples

Simple proof-state handoff:

```yaml
branch_policy: direct_to_main_allowed
worktree_policy:
  use_existing_direction_worktree: true
  do_not_switch_to_local_main: true
  do_not_use_global_main_worktree: true
  ignore_unrelated_untracked_paths_unless_they_overlap_allowed_paths: true
  stop_on_unrelated_tracked_changes_unless_explicitly_allowed: true
main_update_policy:
  auto_update_origin_main_after_validation: true
  method: push_HEAD_to_origin_main_after_fetch_and_rebase
  require_clean_rebase_onto_origin_main: true
  retry_once_on_non_fast_forward_push_rejection: true
  verify_origin_main_sha_after_push: true
```

Workflow core/setup handoff:

```yaml
branch_policy: review_branch_required
worktree_policy:
  use_existing_direction_worktree: false
  do_not_switch_to_local_main: true
  do_not_use_global_main_worktree: true
main_update_policy:
  auto_update_origin_main_after_validation: false
  method: review_branch_push
```

END_OF_FILE: workflow/transport/CODEX_COMMIT_HANDOFF_CARD.md
