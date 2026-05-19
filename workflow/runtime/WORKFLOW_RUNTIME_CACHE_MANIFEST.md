# Workflow Runtime Cache Manifest

```yaml
artifact_control:
  artifact_name: "Workflow Runtime Cache Manifest"
  schema: workflow_runtime_cache_manifest.v1
  owner_layer: runtime
  status: canonical
  repo_path: "workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md"
  default_load: yes
  freshness: refresh_when_cached_runtime_files_change
  last_updated: "2026-05-13"
```

## Purpose

Define which workflow authority files should be manually loaded into ChatGPT Project Files as runtime cache for reliable full-file access.

GitHub remains the source of truth. Project Files are a runtime cache for files that are needed in every chat or are too important to depend on potentially truncated GitHub connector reads.

## Required Project File cache for all active Direction Projects

Every active Direction ChatGPT Project must manually load the shared runtime cache files plus its own Direction Project Files 00-08.

GitHub remains the source of truth. Project Files are runtime cache only.

### Shared runtime cache files for every Direction Project

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

### Active Direction cache file sets

#### Workflow Governance

```text
directions/workflow-governance/project_files/00_DIRECTION_START_HERE.md
directions/workflow-governance/project_files/01_DIRECTION_STATE.md
directions/workflow-governance/project_files/02_CURRENT_PHASE.md
directions/workflow-governance/project_files/03_FOCUS_REGISTER.md
directions/workflow-governance/project_files/04_ACTIVE_GOAL.md
directions/workflow-governance/project_files/05_PORTFOLIO_QUEUE.md
directions/workflow-governance/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/workflow-governance/project_files/07_PHASE_MEMORY_INDEX.md
directions/workflow-governance/project_files/08_DIRECTION_MAP.md
```

Project Instructions source:

```text
directions/workflow-governance/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

#### Solo Max Productive

```text
directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md
directions/solo-max-productive/project_files/01_DIRECTION_STATE.md
directions/solo-max-productive/project_files/02_CURRENT_PHASE.md
directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md
directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md
directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md
directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md
directions/solo-max-productive/project_files/08_DIRECTION_MAP.md
```

Project Instructions source:

```text
directions/solo-max-productive/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

#### Indie Game Development

```text
directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md
directions/indie-game-development/project_files/01_DIRECTION_STATE.md
directions/indie-game-development/project_files/02_CURRENT_PHASE.md
directions/indie-game-development/project_files/03_FOCUS_REGISTER.md
directions/indie-game-development/project_files/04_ACTIVE_GOAL.md
directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md
directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md
directions/indie-game-development/project_files/08_DIRECTION_MAP.md
```

Project Instructions source:

```text
directions/indie-game-development/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

#### Health and Beauty

```text
directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md
directions/health-and-beauty/project_files/01_DIRECTION_STATE.md
directions/health-and-beauty/project_files/02_CURRENT_PHASE.md
directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md
directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md
directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md
directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md
directions/health-and-beauty/project_files/08_DIRECTION_MAP.md
```

Project Instructions source:

```text
directions/health-and-beauty/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

## Shared workflow change rollout rule

Any repository maintenance patch that changes shared workflow runtime behavior must evaluate whether every active Direction ChatGPT Project needs Project Instructions and Project Files refresh.

Shared workflow files include at least:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
docs/CHATGPT_PROJECT_SETUP.md
```

Objective Architecture Model changes affect horizon/frontier/next-action and solution-shape selection behavior and require Project Files cache refresh review for all active Direction Projects.

If any shared workflow file changes, Codex must report Project Files / Project Instructions refresh requirements for all active Direction Projects.

If only one Direction is intentionally updated, Codex must explicitly report why sibling Directions do not need refresh.

## Cache authority rule

GitHub repository files remain canonical.

The Project File cache is valid only as a runtime-access copy of those GitHub files. If a verified full GitHub read contradicts a cached Project File, GitHub wins and the Project File cache must be refreshed.

If GitHub read is truncated, omitted, lacks a tail anchor, or cannot be verified, the truncated GitHub read does not override the Project File cache. If the task depends on current freshness and current freshness cannot be verified, return Context Request.

## Manual refresh triggers

Refresh the Project File cache when any of these change in GitHub:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- any active Direction `project_files/00-08` file listed in this manifest
- ChatGPT Project Instructions for any active Direction Project
- runtime file-read, prompt-loading, repository-patch, lifecycle-state reconciliation, structural-integrity, or context-loading rules

Refresh or explicitly classify Project Files state when a verified repository change produces a logical lifecycle transition that affects active runtime state, even if the Direction `project_files/00-08` files were not physically changed in the same patch.

Logical lifecycle transition triggers include:

- active Goal state changes;
- active Phase state changes;
- next route changes;
- parent Goal completion candidate creation;
- R1 acceptance, rejection, or route-gating;
- Phase Progress Gate result changes;
- Phase closure or pause state changes;
- Direction Map active front changes;
- fresh source evidence contradicts Project Files cache.

## Required chat behavior when cache is missing

If a required cached runtime file is missing from Project Files and GitHub read is unavailable, truncated, stale, or contradictory, return Context Request.

Do not continue material workflow work by relying on memory or partial GitHub output.

## Codex repository maintenance reporting rule

When Codex repository maintenance creates or updates any file listed in this manifest, or any file required by a Direction's ChatGPT Project Files runtime cache, Codex must explicitly report that the corresponding ChatGPT Project File cache must be manually refreshed.

Codex must also report semantic lifecycle staleness even when no cached file was physically changed.

Physical cached-file change is not the only refresh trigger. If a repository maintenance run updates or verifies a Goal artifact, Phase artifact, execution log, Direction Map artifact, or stage output such that the active runtime route or lifecycle state has logically changed, Codex must classify whether the Direction Project Files are updated, intentionally stale for a named next stage, or blocking.

Required return section after every repository maintenance apply/read-back:

```yaml
project_files_cache_refresh_required: true | false
target_chatgpt_project:
manual_refresh_required: true | false
blocking_before_next_material_run: true | false
changed_cached_files:
  - repository_path:
    project_file_cache_name:
    refresh_reason:
    blocking_before_next_material_run: true | false
logical_runtime_state:
  changed: true | false
  triggers:
    - next_route_changed
    - active_goal_lifecycle_state_changed
    - active_phase_lifecycle_state_changed
    - parent_goal_completion_candidate_created
    - parent_goal_completion_state_changed
    - r1_acceptance_or_rejection
    - phase_progress_gate_result_changed
    - phase_closure_or_pause_state_changed
    - direction_map_active_front_changed
  old_state_summary:
  new_state_summary:
project_files_runtime_projection:
  state: updated | stale_but_nonblocking_for_named_next_stage | stale_blocking | unchanged_not_stale | unknown
  affected_project_files:
    - repository_path:
      stale_field:
      stale_value:
      fresh_value:
      action: updated | stale_override | checked_no_change_needed | requires_reconciliation
  allowed_next_stage_when_stale:
  fresh_sources_for_next_stage:
    - path:
  blocking_before_next_material_run: true | false
structural_integrity_validation:
  eof_marker_validation:
    - file_path:
      marker_count:
      marker_is_last_non_whitespace: true | false
      content_after_marker: true | false
      result: pass | fail | not_applicable
manual_action:
```

If no cached file changed and no logical runtime state changed, Codex must explicitly report:

```yaml
project_files_cache_refresh_required: false
reason: "No runtime cache or Direction Project File cache file changed, and no logical runtime state transition made Project Files stale."
logical_runtime_state:
  changed: false
project_files_runtime_projection:
  state: unchanged_not_stale
```

A GitHub commit does not update ChatGPT Project Files. Manual refresh remains required when cached files change. A stale-but-nonblocking override can authorize only the named next stage and only when the launch bundle includes fresh source evidence.

## End-of-file marker

`END_OF_FILE: workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
