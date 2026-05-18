# Goal Working Context — nutrition-project-operational-setup-v0

```yaml
artifact_control:
  artifact_name: "Goal Working Context — nutrition-project-operational-setup-v0"
  schema: goal_working_context.v1
  owner_layer: goal
  status: active
  direction: health-and-beauty
  phase_id: ai-nutrition-operating-layer
  goal_id: nutrition-project-operational-setup-v0
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-18"
```

## Direction

Health and Beauty.

## Active Phase

`Собрать AI-операционный слой питания без тяжёлого трекинга`

Phase path:

`directions/health-and-beauty/phases/ai-nutrition-operating-layer`

## Phase fit

This Goal operationalizes the existing AI Nutrition Operating Layer v0 into a separate working ChatGPT Project `Питание`. It removes the current blocker: no confirmed installed Project, no installed Project Instructions, and no installed Snapshot / Current Loop / Active Menu or equivalent working sources.

## Source inputs

Default context:

- Direction Project Files 00-08.
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
- `workflow/stage_registry/STAGE_REGISTRY.md`.

Request/load for E1 or execution if needed:

- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
- `directions/health-and-beauty/phases/ai-nutrition-operating-layer/00_PHASE_BRIEF.md`
- `directions/health-and-beauty/phases/ai-nutrition-operating-layer/01_PHASE_WORKING_CONTEXT.md`
- `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/00_GOAL_CONTRACT.md`
- `directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md`
- existing menu / prior nutrition menu materials
- nutrition baseline and preferences
- kitchen equipment notes
- old nutrition card if available
- storage/tool preference notes

## Operating requirements from G1

- Separate Project `Питание`, not the current Health and Beauty workflow Project.
- Health and Beauty remains the controlling workflow/project.
- Project `Питание` is the operational nutrition workspace.
- Menus must include shopping, recipes, prep, storage, and fallback rules.
- Tracking can use photo, voice, text, approximate or exact values.
- Assistant may ask useful clarifying questions.
- Missing answers must not block the flow.
- Unknown/defaulted values must be explicit with confidence impact.
- Normal menu-following must not become mandatory food logging.
- Durable updates must be summarized for Project Files / GitHub sync.

## Allowed actions for E1

- Define execution shape and artifact list.
- Decide whether work is single direct, gated sequential, or branch/workstream.
- Decide whether nutrition strategy requires D1_DEEP_RESEARCH.
- Define minimum intake needed for Personal Nutrition Base.
- Define manual-install package structure for Project `Питание`.
- Define dry-run validation.
- Prepare execution handoff.

## Forbidden actions for E1 unless explicitly routed/approved

- Do not create clinical nutrition prescription.
- Do not revive MacroFactor/heavy tracking as default.
- Do not create API/database automation.
- Do not claim Project `Питание` is installed without evidence.
- Do not close the Phase.
- Do not execute product/project work without proper execution route.

## Expected E1 outputs

- Minimum HOW.
- Artifact targets.
- Context requirements.
- Validation checklist.
- Execution topology.
- Exact stop conditions.
- Repository/storage decision or explicit unresolved blocker.
- Next launch or execution packet according to registry.

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0/01_GOAL_WORKING_CONTEXT.md`
