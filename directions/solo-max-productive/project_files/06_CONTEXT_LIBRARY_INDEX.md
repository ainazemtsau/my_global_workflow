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

Load the Direction Project Files default set.

Current Phase:

- Personal Workflow App Kernel Exploration

Active Goal: Personal Workflow App Kernel Min Proof

Active Goal path:

- `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof`

Required default Project Files:

- `00_DIRECTION_START_HERE.md`
- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `03_FOCUS_REGISTER.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `07_PHASE_MEMORY_INDEX.md`

Shared runtime and stage prompts:

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

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
