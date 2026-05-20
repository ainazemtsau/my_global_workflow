# Codex Repository Maintenance Apply Transport Template

```yaml
artifact_control:
  artifact_name: "Codex Repository Maintenance Apply Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md"
  runtime_schema: codex_repository_maintenance_apply.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines the canonical transport template for applying an approved `repository_patch.v1` to the workflow repository and returning read-back / diff verification / commit verification evidence.

Repository maintenance is not product/project execution.

## Transport authority boundary — AD-WF-RT-001

This template applies approved repository maintenance only.

It must not modify product/project workspaces, Task Master graphs, tool bindings, sibling Directions, or any path outside the approved repository patch.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Apply only approved `repository_patch.v1` operations.
- Do not infer extra cleanup.
- Do not run product/project execution.
- Return results to the same ChatGPT stage thread for validation.
- Report Project Files cache refresh requirements after every apply/read-back.

## Canonical packet template

```yaml
workflow_packet: 1
type: codex_repository_maintenance_apply
schema: codex_repository_maintenance_apply.v1
codex_role: repository_maintenance
not_product_project_execution: true

patch_id:

repository:
  name: ainazemtsau/my_global_workflow
  remote: origin
  main_branch: main
  main_worktree_path: C:\my_global_workflow

worktree_policy:
  mode: direction_worktree | workflow_governance_worktree | main_integration_worktree | direct_main_override
  target_direction:
  target_worktree_path:
  target_branch:
  upstream_branch:
  rebase_before_apply: true
  push_branch_after_commit: true
  integrate_to_main: true
  integration_method: merge_or_pr
  main_worktree_path: C:\my_global_workflow
  sibling_direction_edits_allowed: false
  direct_main_requires_explicit_override: true

direction_worktree_map:
  workflow-governance:
    worktree_path: C:\my_global_workflow_worktrees\workflow-governance
    branch: codex/direction-workflow-governance
    upstream: origin/codex/direction-workflow-governance
  solo-max-productive:
    worktree_path: C:\my_global_workflow_worktrees\solo-max-productive
    branch: codex/direction-solo-max-productive
    upstream: origin/codex/direction-solo-max-productive
  indie-game-development:
    worktree_path: C:\my_global_workflow_worktrees\indie-game-development
    branch: codex/direction-indie-game-development
    upstream: origin/codex/direction-indie-game-development
  health-and-beauty:
    worktree_path: C:\my_global_workflow_worktrees\health-and-beauty
    branch: codex/direction-health-and-beauty
    upstream: origin/codex/direction-health-and-beauty

branch_policy:
  mode: worktree_branch_then_main_integration
  target_branch:
  upstream_branch:
  rebase_before_apply: true
  commit_in_worktree_branch: true
  push_branch_after_commit: true
  merge_or_pr_into_main: true
  require_clean_worktree: true
  pull_or_fetch_before_apply: true
  conflict_policy: scoped_path_conflicts_only
  direct_main_allowed: explicit_override_only

source_stage:

allowed_paths:
  - path:
    reason:

forbidden_paths:
  - path:
    reason:

repository_patch:
  reference_or_inline_patch:

read_back_anchors:
  - file_path:
    anchors:
      - text:

lifecycle_state_reconciliation:
  required: true | false
  instruction: Report whether approved changes or verified artifacts changed logical runtime state and whether Project Files are updated, stale-but-nonblocking, stale-blocking, or unchanged.

structural_integrity_validation:
  required: true
  instruction: For every changed file with an END_OF_FILE marker, verify the marker appears exactly once and is the last non-whitespace content. Append operations must insert before EOF, not below it.

diff_verification:
  required: true
  instruction: Apply only the listed repository_patch.v1 operations and verify the diff contains no extra changes.

commit_verification:
  required: true
  instruction: Report commit hash, PR link, or explicit no-commit reason.

project_files_cache_refresh_required:
  expected: true | false
  reason:

return_to_chat_instruction: Return result to the same ChatGPT stage thread for validation.
do_not_auto_launch_next_stage: true

required_return:
  - final_state
  - worktree_used
  - target_branch
  - upstream_branch
  - rebase_result
  - commit_sha
  - push_result
  - main_integration_status
  - main_commit_sha_or_pr
  - files_changed
  - validation_command_outputs
  - read_back_anchor_results
  - structural_integrity_validation
  - lifecycle_state_reconciliation
  - diff_scope_verification
  - project_files_cache_refresh_required
  - confirmation_no_forbidden_paths_touched

extensions: {}
```

## Required safety text

- Apply only the listed `repository_patch.v1` operations.
- Do not infer extra changes.
- Use the required Direction worktree for Direction-specific work.
- Use `C:\my_global_workflow` as the clean integration worktree for `main`.
- Run `git fetch origin && git rebase origin/main` before applying work in a Direction worktree.
- Commit and push the Direction branch after scoped work.
- Merge, PR, or report explicit unmerged reason for main integration.
- Do not use the main worktree as an ordinary Direction working tree.
- Do not run product/project execution.
- Do not create Task Master graph unless explicitly part of a registry-valid Executor product/project execution route.
- Do not modify project/tool bindings unless explicitly listed.
- Do not touch sibling Directions unless explicitly listed.
- If a logical lifecycle state changes, report whether Project Files were updated, intentionally stale for a named next stage, or stale-blocking.
- If a changed file has an `END_OF_FILE` marker, verify the marker appears exactly once and remains the last non-whitespace content.
- Insert append operations before EOF markers, not below them.
- Return result to the same ChatGPT stage thread for validation.

## Validation anchors

- `workflow_packet: 1`
- `schema: codex_repository_maintenance_apply.v1`
- `codex_role: repository_maintenance`
- `not_product_project_execution: true`
- `project_files_cache_refresh_required`

## End-of-file marker

`END_OF_FILE: workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md`
