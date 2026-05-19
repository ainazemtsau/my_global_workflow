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
- ChatGPT Project Instructions for Workflow Governance
- runtime file-read, prompt-loading, repository-patch, or context-loading rules

## Required chat behavior when cache is missing

If a required cached runtime file is missing from Project Files and GitHub read is unavailable, truncated, stale, or contradictory, return Context Request.

Do not continue material workflow work by relying on memory or partial GitHub output.

## Codex repository maintenance reporting rule

When Codex repository maintenance creates or updates any file listed in this manifest, or any file required by a Direction's ChatGPT Project Files runtime cache, Codex must explicitly report that the corresponding ChatGPT Project File cache must be manually refreshed.

Codex must include this return section after every repository maintenance apply/read-back:

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
manual_action:
```

If no cached file changed, Codex must explicitly report:

```yaml
project_files_cache_refresh_required: false
reason: "No runtime cache or Direction Project File cache file changed."
```

A GitHub commit does not update ChatGPT Project Files. Manual refresh remains required when cached files change.

## End-of-file marker

`END_OF_FILE: workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
