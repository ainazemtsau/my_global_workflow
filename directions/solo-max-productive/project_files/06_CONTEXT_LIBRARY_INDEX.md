# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
artifact_control:
  artifact_name: "06_CONTEXT_LIBRARY_INDEX.md"
  schema: context_loading_index.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-12"
  refresh_source: "G1-2026-05-12-personal-workflow-app-kernel-min-proof"
```

## Default context

Load these files by default for Solo Max Productive runtime.

In the ChatGPT Project, these files should be present as Project Files runtime cache so the chat does not depend on potentially truncated GitHub connector reads for core workflow behavior:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md`
- `directions/solo-max-productive/project_files/01_DIRECTION_STATE.md`
- `directions/solo-max-productive/project_files/02_CURRENT_PHASE.md`
- `directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md`
- `directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md`
- `directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md`

GitHub remains the source of truth. Project Files are a runtime cache.

If GitHub and Project File cache conflict, use verified full GitHub read-back. If GitHub read is truncated, omitted, lacks tail verification, or cannot be verified, return Context Request instead of treating partial GitHub content as authority.

## Goal context

Default-load for active Goal when needed by E1:

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/00_GOAL_CONTRACT.md`
- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/01_GOAL_WORKING_CONTEXT.md`

Request if needed:

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/02_GOAL_CONTEXT_INDEX.md`
- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/execution_log.md`

## Request-only context

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/source_materials/EXOCORTEX_CONCEPT_SEED_FULL.md`

Load only if exact concept detail is needed. Do not treat as roadmap.

## Archive boundary

- Archived or historical material is pointer-only and must not be default-loaded.
- vNext One-Goal Smoke Test is historical/test state for this route, not current active work.
- Create Lightweight Codex Small-Fix Lane is not current active Goal state unless explicitly reactivated.

## Phase Memory Index default context amendment

Required default Project Files include:

- `07_PHASE_MEMORY_INDEX.md`

Use `directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a materially new Phase after closure.
