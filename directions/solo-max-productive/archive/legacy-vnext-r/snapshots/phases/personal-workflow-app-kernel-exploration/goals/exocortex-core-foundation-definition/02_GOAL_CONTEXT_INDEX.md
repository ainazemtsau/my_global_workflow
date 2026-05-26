# 02 Goal Context Index — EXOCORTEX Core Foundation Definition

```yaml
artifact_control:
  artifact_name: "02 Goal Context Index — EXOCORTEX Core Foundation Definition"
  schema: goal_context_index.v1
  owner_layer: persistence
  status: active
  source_file: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/02_GOAL_CONTEXT_INDEX.md"
  freshness: fresh
  created_at: "2026-05-19"
  created_by_stage: G1_GOAL_SHAPE

goal:
  id: exocortex-core-foundation-definition
  title: EXOCORTEX Core Foundation Definition
  lifecycle_state: goal_shaped_pending_E1
  next_route: E1_EXECUTION_BRIEF
```

## Default context for next stage

Load these for E1:

```text
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/00_GOAL_CONTRACT.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/01_GOAL_WORKING_CONTEXT.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition/02_GOAL_CONTEXT_INDEX.md
directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md
directions/solo-max-productive/project_files/01_DIRECTION_STATE.md
directions/solo-max-productive/project_files/02_CURRENT_PHASE.md
directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md
directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md
directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md
directions/solo-max-productive/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/solo-max-productive/project_files/07_PHASE_MEMORY_INDEX.md
directions/solo-max-productive/project_files/08_DIRECTION_MAP.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md
workflow/stage_registry/STAGE_REGISTRY.md
```

## Request-only context

Required for E1:

```text
workflow/stage_prompts/E1_EXECUTION_BRIEF.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/source_materials/EXOCORTEX_CONCEPT_SEED_FULL.md
```

## Superseded comparison context

Request only if E1 needs comparison/provenance:

```text
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/00_GOAL_CONTRACT.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/01_GOAL_WORKING_CONTEXT.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/02_GOAL_CONTEXT_INDEX.md
directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/execution_log.md
```

Use old Goal files only as superseded comparison material.

## Do not load by default

- old chats;
- archive notes;
- old Wave JSON;
- Task Master JSON;
- deprecated workflow exports;
- old vNext smoke-test state;
- product/code repositories;
- implementation evidence dumps.

## Missing context behavior

If `E1_EXECUTION_BRIEF.md` or `EXOCORTEX_CONCEPT_SEED_FULL.md` is missing, truncated, or lacks tail verification, return Context Request with the exact repository path or ask for a current-chat attachment.
