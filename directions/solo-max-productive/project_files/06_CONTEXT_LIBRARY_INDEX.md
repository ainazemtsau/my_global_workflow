# 06\_CONTEXT\_LIBRARY\_INDEX.md

```yaml
artifact_control:
  artifact_name: "06_CONTEXT_LIBRARY_INDEX.md"
  schema: context_loading_index.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-11"
  refresh_source: "P0-2026-05-11-personal-workflow-app-kernel-start"

```

## Default context

Load the Direction Project Files default set.

Current Phase:

*   Personal Workflow App Kernel Exploration

Active Goal:

*   none

Selected Goal candidate:

*   Shape Personal Workflow App Kernel Min Proof

Required default Project Files:

*   00\_DIRECTION\_START\_HERE.md
*   01\_DIRECTION\_STATE.md
*   02\_CURRENT\_PHASE.md
*   03\_FOCUS\_REGISTER.md
*   04\_ACTIVE\_GOAL.md
*   05\_PORTFOLIO\_QUEUE.md
*   06\_CONTEXT\_LIBRARY\_INDEX.md
*   07_PHASE_MEMORY_INDEX.md

Shared runtime and stage prompts:

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

Request-only context:

*   `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration` when phase working context is needed.
*   `directions/solo-max-productive/knowledge` when accepted knowledge or canon candidates are needed.
*   If exact source wording is missing from GitHub, return a Context Request naming the required GitHub path or export.

Archive boundary:

*   Archived or historical material is pointer-only and must not be default-loaded.
*   vNext One-Goal Smoke Test is historical/test state for this route, not current active work.

## Phase Memory Index default context amendment

Required default Project Files now also include:

*   07_PHASE_MEMORY_INDEX.md

Use `directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a new Phase after closure.