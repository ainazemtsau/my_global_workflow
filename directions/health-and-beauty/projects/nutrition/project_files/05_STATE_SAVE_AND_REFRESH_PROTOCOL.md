# 05 - State Save and Refresh Protocol

Status: active

Purpose: define the boundary between Project `Питание`, Codex save operations, GitHub durable state, and Project Files refresh.

## Authority

```yaml
github: durable_source_of_truth
project_files: refreshable_runtime_cache
chat_memory: non_authoritative
codex: save_only_repository_maintenance_writer
```

## Save Packet

The Project may propose a save packet only after the user approves the content to preserve.

```yaml
nutrition_state_update_packet:
  schema: nutrition_state_update_packet.v1
  packet_status: proposed_for_user_approval
  external_write_claimed: false
  reason:
  target_files:
    - path:
      operation: create_or_update
      content_summary:
  validation_expectations:
    - file_read_back
    - git_diff_scoped_to_nutrition_paths
    - project_files_refresh_required_after_save
```

Codex may write only when `packet_status: approved_by_user`.

## Refresh After Save

After Codex returns read-back/diff evidence:

1. Refresh the changed files in ChatGPT Project Files from GitHub.
2. Start a fresh chat with the relevant mode.
3. Verify it resumes from the refreshed files, not hidden memory.

## Stale File Rule

If Project Files are stale, ask for refresh of the exact stale files. Do not continue from memory.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
