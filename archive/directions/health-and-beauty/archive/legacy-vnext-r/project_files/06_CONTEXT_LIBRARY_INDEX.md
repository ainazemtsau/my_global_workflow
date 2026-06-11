# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh_after_patch_readback
activated_at: "2026-05-12"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load these files by default for Health and Beauty runtime.

In the ChatGPT Project, these files should be present as Project Files runtime cache so the chat does not depend on potentially truncated GitHub connector reads for core workflow behavior:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md`
- `directions/health-and-beauty/project_files/01_DIRECTION_STATE.md`
- `directions/health-and-beauty/project_files/02_CURRENT_PHASE.md`
- `directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md`
- `directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md`
- `directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`
- `directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`

GitHub markdown files remain the source of truth. Project Files are runtime cache.

If GitHub and Project File cache conflict, use verified full GitHub read-back. If GitHub read is truncated, omitted, lacks tail verification, or cannot be verified, return Context Request instead of treating partial GitHub content as authority.

`08_DIRECTION_MAP.md` is strategic routing context between Direction and Phase; it does not replace Phase, Goal, Queue, Context Loading Index, or Phase Memory state.

## Shared runtime and stage prompts

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

## Required context for next P0_PHASE_START / G1_GOAL_SHAPE

* Direction Project Files 00-08 after repository maintenance/read-back and manual Project Files refresh.
* `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
* `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`.
* `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`.
* `workflow/stage_registry/STAGE_REGISTRY.md`.
* Request exact stage prompt only when entering the stage:
  * `workflow/stage_prompts/P0_PHASE_START.md`
  * `workflow/stage_prompts/G1_GOAL_SHAPE.md`
* Phase close summary: `directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md`.
* Phase Memory Index: `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`.
* Direction Map: `directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`.

The next default route is a result-facing first weekly body-transformation correction loop. A standalone metrics/readiness/documentation packet Phase is not the default allowed shape.

## Request-only context for P0_PHASE_START / G1_GOAL_SHAPE

* Prior AI Nutrition Operating Layer v0 design/protocol artifact, historical input only:
  * `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md`
* Closed Project `Питание` Goal files, historical evidence only:
  * `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md`
  * `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md`
* Prior Project `Питание` setup files, historical input only.
* Existing nutrition project files under `directions/health-and-beauty/projects/nutrition/**`, if needed for state/protocol inventory.
* Existing setup package under `directions/health-and-beauty/project_setup/pitanie/**`, if needed for historical comparison.
* Existing menu / prior nutrition menu materials, if needed.
* Nutrition baseline/preferences, if needed for dry-run realism.
* Tool/storage preferences and concrete availability.
* Tracking burden tolerance and minimum acceptable input cadence.
* Cooking/shopping/menu cadence.
* Current kitchen equipment notes: air fryer, multicooker, vacuum sealer.
* Recipe/prep notes if available.

## Archive boundary

Archived or historical material is pointer-only and must not be default-loaded.

## Tool boundary

Do not infer that MacroFactor, self-hosted trackers, Notion, Trillium, ChatGPT connections, or automation are available for execution. Verify concrete tool/storage bindings before relying on them.

## Phase Memory Index default context amendment

Required default Project Files now also include:

*   `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`
*   `directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`

Use `07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a new Phase after closure.
