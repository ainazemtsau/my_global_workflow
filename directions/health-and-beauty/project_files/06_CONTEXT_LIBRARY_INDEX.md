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

GitHub remains the source of truth. Project Files are a runtime cache.

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

## Required context for next S3_DECIDE

* Direction Project Files 00-08.
* `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
* `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`.
* `workflow/stage_registry/STAGE_REGISTRY.md`.
* `workflow/stage_prompts/S3_DECIDE.md`.

## Request-only context for S3_DECIDE

* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/00_PHASE_BRIEF.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/01_PHASE_WORKING_CONTEXT.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/00_GOAL_CONTRACT.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md`.
* Prior Project `Питание` Goal Contract / Working Context, only as historical input:
  * `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/00_GOAL_CONTRACT.md`
  * `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md`

* Existing menu / prior nutrition menu materials, if needed for decision context.
* Nutrition baseline/preferences.
* Tool/storage preferences and concrete availability.
* Tracking burden tolerance and minimum acceptable input cadence.
* Cooking/shopping/menu cadence.
* Current training app constraints if relevant to nutrition loop design.
* Current kitchen equipment notes: air fryer, multicooker, vacuum sealer.
* Recipe/prep notes if available.
* Prior MacroFactor Phase and Goal files as historical evidence only:
  * `directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup`
  * `directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

## Parked context until post-S3 implementation target

E1-specific Project `Питание` setup context is not required until `S3_DECIDE` and then `G1_GOAL_SHAPE` produce an accepted implementation target.

## Archive boundary

Archived or historical material is pointer-only and must not be default-loaded.

## Tool boundary

Do not infer that MacroFactor, self-hosted trackers, Notion, Trillium, ChatGPT connections, or automation are available for execution. Verify concrete tool/storage bindings before relying on them.

## Phase Memory Index default context amendment

Required default Project Files now also include:

*   `directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md`
*   `directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`

Use `07_PHASE_MEMORY_INDEX.md` as compact phase-history context before P0 proposes a new Phase after closure.
