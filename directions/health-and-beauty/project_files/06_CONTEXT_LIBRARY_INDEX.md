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

Load the Direction Project Files default set.

Current Phase: `Собрать AI-операционный слой питания без тяжёлого трекинга`

Active Goal: `Собрать AI Nutrition Operating Layer v0`

Active Goal path:

`directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0`

Next route: `E1_EXECUTION_BRIEF`

## Shared runtime and stage prompts

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

## Required context for next E1

* Direction Project Files 00-06.
* `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
* `workflow/stage_registry/STAGE_REGISTRY.md`.
* `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/00_PHASE_BRIEF.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/01_PHASE_WORKING_CONTEXT.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/00_GOAL_CONTRACT.md`.
* `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/01_GOAL_WORKING_CONTEXT.md`.

## Request-only context for E1

* Existing menu / prior nutrition menu materials.
* Nutrition baseline and preferences.
* Current kitchen equipment notes: air fryer, multicooker, vacuum sealer.
* Recipe/prep notes if available.
* Storage/tool preference notes: Trillium, Notion, GitHub, ChatGPT connections, or other.
* Prior MacroFactor Phase and Goal files as historical evidence only:
  * `directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup`
  * `directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

## Archive boundary

Archived or historical material is pointer-only and must not be default-loaded.

## Tool boundary

Do not infer that MacroFactor, self-hosted trackers, Notion, Trillium, ChatGPT connections, or automation are available for execution. Verify concrete tool/storage bindings before relying on them.
