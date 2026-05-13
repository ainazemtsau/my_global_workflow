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
  name:
  branch:

branch_policy:
  mode: direct_main
  target_branch: main
  create_branch: false
  create_pr: false
  commit_directly: true
  push_directly: true
  require_clean_worktree: false
  pull_before_apply: true
  conflict_policy: scoped_path_conflicts_only

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
  - commit_sha
  - files_changed
  - validation_command_outputs
  - read_back_anchor_results
  - diff_scope_verification
  - project_files_cache_refresh_required
  - confirmation_no_forbidden_paths_touched

extensions: {}
```

## Required safety text

- Apply only the listed `repository_patch.v1` operations.
- Do not infer extra changes.
- Do not run product/project execution.
- Do not create Task Master graph unless explicitly part of C1/C2 product execution route.
- Do not modify project/tool bindings unless explicitly listed.
- Do not touch sibling Directions.
- Return result to the same ChatGPT stage thread for validation.

## Validation anchors

- `workflow_packet: 1`
- `schema: codex_repository_maintenance_apply.v1`
- `codex_role: repository_maintenance`
- `not_product_project_execution: true`
- `project_files_cache_refresh_required`

## End-of-file marker

`END_OF_FILE: workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md`
