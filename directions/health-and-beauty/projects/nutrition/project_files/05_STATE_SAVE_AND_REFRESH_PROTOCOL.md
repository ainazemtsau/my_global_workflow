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

The Project may propose a single-file or multi-file save packet only after the user approves the content to preserve. Multi-file packets must keep each artifact separate and list each target file explicitly.

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

The Project may emit one compact `PITANIE_CODEX_CARD` instead of a long manual prompt. The card must identify the operation, target files, content payload, validation expectations, and whether Mealie sync is requested.

Codex performs the GitHub save and, when requested by an approved card, Mealie recipe sync and meal planner sync through existing MCP server `mealie`.

The Project must not claim GitHub save or Mealie sync without Codex read-back, diff evidence, and Mealie sync evidence.

Allowed Global Strategy artifact targets:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
research/DEEP_RESEARCH_REQUEST.md
research/DEEP_RESEARCH_RESULT.md
research/DEEP_RESEARCH_SYNTHESIS.md
state/GLOBAL_NUTRITION_PLAN.md
```

Allowed menu, preference, recipe, and sync targets:

```text
state/USER_PROFILE_AND_CONSTRAINTS.yml
weeks/current/ACTIVE_WEEK_MENU.md
weeks/current/MEALIE_RECIPE_BUNDLE.json
weeks/current/NEXT_WEEK_INPUTS.md
recipes/RECIPE_TAXONOMY.yml
recipes/RECIPE_CATALOG_INDEX.md
recipes/catalog/*.json
recipes/bundles/*/MEALIE_RECIPE_BUNDLE.json
```

The Project must not claim a save happened until Codex returns read-back and diff evidence for the changed files.

The Project must not claim Mealie sync happened until Codex returns Mealie recipe and meal planner sync evidence from MCP server `mealie`.

## Refresh After Save

After Codex returns read-back/diff evidence:

1. Refresh exactly the changed files in ChatGPT Project Files from GitHub.
2. Start a fresh chat with the relevant mode.
3. Verify it resumes from the refreshed files, not hidden memory.

## Stale File Rule

If Project Files are stale, ask for refresh of the exact stale files. Do not continue from memory.

END_OF_FILE: directions/health-and-beauty/projects/nutrition/project_files/05_STATE_SAVE_AND_REFRESH_PROTOCOL.md
