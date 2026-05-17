# 04_ACTIVE_GOAL.md

```yaml
project_file_control:
  file: 04_ACTIVE_GOAL.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
active_goal:
  state: active
  goal_id: ai-nutrition-operating-layer-v0
  goal_name: "Собрать AI Nutrition Operating Layer v0"
  goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0"
  phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
  current_wave: none
  current_stage: state_corrected_after_v0_artifact
  status: design_artifact_ready_but_operational_setup_required
  next_route: G1_GOAL_SHAPE
```

## Goal Contract snapshot

* WHAT: Build a compact AI Nutrition Operating Layer v0: Nutrition State Packet, Active Menu object, operating modes, exception-only correction logic, recipe/prep support, review/state-update protocol, storage/save rules, restart/context-refresh rules, and sample flows.
* WHY: The bottleneck is absence of a stable AI nutrition process without heavy tracking or reliance on one long ChatGPT chat.
* DONE: A fresh next chat can use the v0 layer to create/update menu, advise on current day, correct after overeating/off-menu eating, add recipe/prep notes, run day/week summary, and produce durable state-update/save output.
* Acceptance floor: state packet, active menu object, four modes, exception-only tracking, day correction logic, storage protocol, restart rules, five sample flows, explicit non-goals.
* Validation: paper-test the five sample flows.

## Corrected runtime position

* `03_AI_NUTRITION_OPERATING_LAYER_V0.md` exists as a design/protocol artifact.
* The artifact does not prove that a working ChatGPT Project `Питание` exists.
* Do not treat the prior review direction as formalized `completed_verified -> P9_PHASE_CLOSE`.
* Operational setup remains required before the Phase can be closed.

## Next Goal seed

```yaml
next_goal_seed:
  id_candidate: nutrition-project-operational-setup-v0
  title: "Собрать рабочий ChatGPT Project “Питание” на базе AI Nutrition Operating Layer v0"
  route: G1_GOAL_SHAPE
  done_floor:
    - "Project Instructions for `Питание` drafted or installed."
    - "Snapshot source drafted."
    - "Current Loop source drafted."
    - "Active Menu starter created or missing user inputs listed."
    - "Save/update behavior ready."
    - "2-3 minimal operational scenarios paper-tested or dry-run."
  forbidden:
    - "No clinical nutrition advice."
    - "No MacroFactor-centered workflow."
    - "No heavy calorie/macro ledger."
    - "No tracker/database/API automation."
    - "No full body-transformation plan."
    - "No P9_PHASE_CLOSE."
```

## Scope boundaries

In scope:

* AI nutrition operating layer.
* State packet.
* Active menu object.
* Daily operator.
* Menu architect.
* Recipe/prep builder.
* Review/state update.
* Exception-only tracking.
* Storage and restart rules.

Out of scope:

* MacroFactor-centered workflow.
* Heavy tracker.
* Detailed calorie/macro ledger.
* Food tracker/database setup.
* API/import automation.
* Huge recipe vault.
* Clinical nutrition.
* Menu-only Goal.

## Preserved history

The prior MacroFactor active Goal is preserved as historical evidence under:

`directions/health-and-beauty/phases/macrofactor-nutrition-ai-support-setup/goals/ai-support-nutrition-recipes-menu-macrofactor`

It must not be executed as current work unless explicitly reshaped.
