# 08 Direction Map - Health and Beauty

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Health and Beauty"
  schema: direction_map.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/health-and-beauty/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: objective_architecture_migration_frontier_repair
  last_updated: "2026-05-19"
```

## Purpose

Compact strategic routing context for the Direction's current initiative, active front, horizon slice, and map-linked Phase/Goal selection.

This file does not replace:

- `01_DIRECTION_STATE.md`
- `02_CURRENT_PHASE.md`
- `04_ACTIVE_GOAL.md`
- `05_PORTFOLIO_QUEUE.md`
- `06_CONTEXT_LIBRARY_INDEX.md`
- `07_PHASE_MEMORY_INDEX.md`

## Direction map status

```yaml
direction_map_status:
  map_state: initialized
  current_initiative_id: body-transformation-20kg-strength-health
  map_confidence: medium
  current_execution_state_confidence: medium
  last_reviewed_stage: objective_architecture_migration_review
  migration_status: migrated_with_2026_05_19_objective_architecture_frontier_repair
  migration_source:
    mode: approved_repository_maintenance_formalization
    direction_path: "directions/health-and-beauty"
    source_ref: "codex/direction-health-and-beauty"
    patch_id: health_beauty_objective_architecture_migration_2026_05_19
  corrected_state:
    summary: "S3 selected Project `Питание` v0 as the standalone repo-backed container/tool, and G1 formalized the repaired Goal; E1 execution planning is pending repository maintenance/read-back and Project Files refresh."
    blocks:
      - P9_PHASE_CLOSE
      - claiming_working_project_pitanie_exists
      - claiming_operational_completion
      - launching_stale_project_pitanie_e1_route
    does_not_block:
      - S3_DECIDE_for_minimal_nutrition_loop_shape_and_tooling_policy
      - preserving_current_active_phase
      - using_prior_v0_and_goal_artifacts_as_historical_input
    corrected_paths:
      project_file_projection_paths:
        - "directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md"
        - "directions/health-and-beauty/project_files/01_DIRECTION_STATE.md"
        - "directions/health-and-beauty/project_files/02_CURRENT_PHASE.md"
        - "directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md"
        - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
        - "directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md"
        - "directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md"
      active_goal_artifact_paths:
        - "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/02_EXECUTION_BRIEF.md"
        - "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/03_AI_NUTRITION_OPERATING_LAYER_V0.md"
        - "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0/execution_log.md"
  update_policy: "M0 owns shared map review/update; R1/P9/parent synthesis may propose controlled map deltas after evidence; branch chats emit delta proposals only."
```

## Current Initiative

```yaml
current_initiative:
  id: body-transformation-20kg-strength-health
  title: "Похудеть на 20 кг и вывести силу и здоровье на максимальный уровень"
  status: active
  objective: "Похудеть примерно на 20 кг и устойчиво вывести здоровье, силу, внешний вид, энергию и качество режима на высокий уровень через лучшие практики и удобные инструменты, без лишней ручной нагрузки."
  intent: "Create a sustainable, evidence-based body-transformation process covering nutrition first, then training/cardio, recovery, minimal metrics, and periodic correction while keeping manual routine burden low."
  tooling_policy: "AI/ChatGPT/Project/app/storage are optional tools; use the best available tool mix for the outcome, and do not require everything to live in ChatGPT."
  why_now:
    - "User identified excess weight as the largest current health/beauty problem."
    - "User can sustain a strict process if the process is clear and routine burden is low."
    - "Current active Phase already targets the main documented constraint: no stable nutrition process without heavy tracking."
    - "Manual calorie-app logging is considered too high-friction for the desired process."
  success_signal:
    - "A low-friction, evidence-based nutrition loop exists without detailed manual calorie/macro ledger."
    - "Project `Питание` is a possible container/tool, not the required implementation."
    - "Nutrition loop can plan/update menus or defaults, advise current day, correct after overeating/off-menu eating, add recipe/prep notes, run day/week summary, and produce durable state update/save output."
    - "After nutrition layer validation, the Direction can add minimal metrics and a training/cardio/recovery decision slice without expanding into a broad backlog."
```

## Initiative Registry

```yaml
initiative_registry:
  - initiative_id: body-transformation-20kg-strength-health
    title: "20 kg fat-loss plus strength/health operating system"
    status: active
    active_phase_binding:
      phase_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer"
      phase_name: "Собрать удобный, научно обоснованный процесс питания без тяжёлого трекинга"
      binding_reason: "Nutrition execution without heavy manual tracking is the current documented constraint and directly supports the broader body-transformation initiative."
    active_goal_binding:
      goal_id: nutrition-project-operational-setup-v0
      goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
      goal_name: "Собрать отдельный рабочий ChatGPT Project “Питание” как low-friction nutrition operating system"
      status: goal_shaped_pending_E1
      binding_reason: "S3 selected Project `Питание` v0 as the repaired container/tool; G1 formalized the Goal shape and E1 must define execution envelope and validators before implementation."
    current_risk:
      - "The prior Project `Питание` setup/E1 path can be mistaken for a basis-valid current route."
      - "Broad health/fitness optimization can easily become overbuilt unless S3 narrows the nutrition loop and tooling policy first."
```

## Strategy Basis

```yaml
strategy_basis:
  map_generation_mode: m0_post_rollout_migration_from_project_files_codex_bundle_and_user_input
  strategic_question: "What is the shortest credible path from the current nutrition work to a broader low-friction body transformation process for losing 20 kg and improving strength/health?"
  optimization_criteria:
    - shortest_credible_path
    - constraint_removal
    - evidence_value
    - scope_minimization
    - reversibility
    - human_burden_minimization
  candidate_paths_considered:
    - path_id: decide_minimal_nutrition_loop_shape_and_tooling
      verdict: selected
      rationale: "Repairs the active frontier after user correction, keeps the Phase open, and decides the smallest basis-valid nutrition loop before execution planning."
    - path_id: execute_existing_project_pitanie_setup_goal
      verdict: rejected_stale_blocked
      rationale: "The current saved Project `Питание` E1 route is stale / blocked / not basis-valid after Objective Architecture correction."
    - path_id: restart_full_body_transformation_master_plan
      verdict: rejected_for_now
      rationale: "Too broad and likely to create planning bloat before the current nutrition layer is usable."
    - path_id: macrofactor_or_detailed_tracker_default
      verdict: rejected_for_default
      rationale: "Conflicts with low-friction constraint and current files mark MacroFactor-centered work as superseded/paused."
    - path_id: research_training_cardio_supplements_first
      verdict: parked
      rationale: "Valuable later, but requires evidence and decisions; should not precede current state reconciliation."
    - path_id: parallel_training_cardio_before_nutrition_loop_decision
      verdict: parked
      rationale: "Adds scope before the nutrition loop shape and tooling policy are basis-valid."
  selected_path_rationale: "Run E1_EXECUTION_BRIEF on the shaped Project `Питание` v0 Goal; do not claim operational completion or route to Phase close."
  major_assumptions:
    - "User can sustain a strict process if the process is clear and routine work is offloaded."
    - "Low-burden execution is more important than perfect measurement at the current stage."
    - "Nutrition remains the first practical bottleneck because the active Phase targets it and the user identifies weight as the main problem."
    - "Training/cardio/recovery/supplement decisions need later scoped evidence or decision work after the nutrition loop is accepted."
  scope_cuts:
    - "No calendar roadmap."
    - "No broad backlog."
    - "No detailed calorie/macro ledger."
    - "No MacroFactor revival as default."
    - "No supplement/fasting/brain-diet recommendation inside M0."
    - "No P9_PHASE_CLOSE from this correction."
    - "No stale Project `Питание` E1 launch."
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes:
    - node_id: d_nutrition_loop_shape_and_tooling
      initiative_id: body-transformation-20kg-strength-health
      label: "Decide minimal nutrition loop shape and tool/container policy"
      type: active_front
      status: implementation_goal_shaped_pending_E1
      purpose: "Choose the minimal low-friction nutrition loop and the tool/container mix before shaping or executing any implementation Goal."
      success_signal:
        - "S3_DECIDE selects whether Project `Питание` is kept, repaired, reduced, or superseded."
        - "Minimum recurring nutrition inputs and state update rules are clear."
        - "Tool/storage policy is explicit and outcome-first."
        - "A repaired/new Goal can be shaped only after the decision."
      human_burden_policy: "No detailed calorie-app ledger; use exception-only tracking and compact state updates."

    - node_id: n2_minimal_body_metrics_packet
      initiative_id: body-transformation-20kg-strength-health
      label: "Minimal body-transformation metrics packet"
      type: horizon
      status: not_started
      purpose: "Define the smallest recurring input packet for AI correction: weight trend, optional waist/photos, training completion, VR/cardio minutes, sleep/energy, and exceptions."
      non_goal: "Do not create a full quantified-self tracker or food database."

    - node_id: n3_training_cardio_recovery_decision_slice
      initiative_id: body-transformation-20kg-strength-health
      label: "Training/cardio/recovery decision slice"
      type: horizon
      status: not_started
      purpose: "Choose the smallest evidence-backed training/cardio/recovery structure compatible with user effort capacity and low routine burden."
      evidence_need: "Current external evidence and/or decision stage likely required before prescription."

    - node_id: n4_integrated_daily_weekly_ai_operator
      initiative_id: body-transformation-20kg-strength-health
      label: "Integrated daily/weekly AI operator"
      type: horizon
      status: not_started
      purpose: "Combine nutrition, training/cardio, recovery, minimal metrics, exceptions, and weekly correction into one low-burden operating loop."

    - node_id: n5_supplements_fasting_brain_diet_research_gate
      initiative_id: body-transformation-20kg-strength-health
      label: "Supplements / fasting / brain-diet research gate"
      type: parked_future
      status: parked
      purpose: "Evaluate only after core process is stable and only through evidence/safety-aware research or decision route."

    - node_id: n6_macrofactor_or_heavy_tracking_revival
      initiative_id: body-transformation-20kg-strength-health
      label: "MacroFactor / heavy tracking revival"
      type: parked_or_rejected_default
      status: parked
      purpose: "Available only if explicitly reshaped later; not default due low-friction constraint and superseded Phase status."

  edges:
    - from: d_nutrition_loop_shape_and_tooling
      to: n2_minimal_body_metrics_packet
      relation: enables
      reason: "An accepted nutrition loop needs a minimal state input format for ongoing correction."
    - from: n2_minimal_body_metrics_packet
      to: n3_training_cardio_recovery_decision_slice
      relation: informs
      reason: "Training/cardio/recovery choice should reflect baseline and minimal metrics."
    - from: n3_training_cardio_recovery_decision_slice
      to: n4_integrated_daily_weekly_ai_operator
      relation: enables
      reason: "The integrated operator should combine validated nutrition and selected training/cardio/recovery structure."
    - from: n5_supplements_fasting_brain_diet_research_gate
      to: n4_integrated_daily_weekly_ai_operator
      relation: optional_after_evidence
      reason: "Optional practices should enter the operator only after evidence and safety review."
```

## Active Front

```yaml
active_front:
  primary_node: d_nutrition_loop_shape_and_tooling
  reason: "This is the smallest credible path because it repairs the stale Project `Питание` route, preserves useful prior artifacts as input, and avoids a broad restart."
  current_route_binding:
    route_state: shaped_goal_pending_execution_planning
    route: E1_EXECUTION_BRIEF
    rule: "Run E1 only after repository maintenance/read-back and Project Files refresh."
  parallel_candidate_nodes: []
  parked_nodes:
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
    - n5_supplements_fasting_brain_diet_research_gate
    - n6_macrofactor_or_heavy_tracking_revival
```

## Horizon Slice

```yaml
horizon_slice:
  id: h_low_friction_evidence_based_nutrition_loop
  statement: "Do not jump to a perfect full-body plan. First decide a low-friction evidence-based nutrition loop and tool/container policy; then shape a repaired/new implementation Goal; then define minimal body metrics; then run one evidence-backed training/cardio/recovery decision slice; then integrate into a daily/weekly operator."
  node_ids:
    - d_nutrition_loop_shape_and_tooling
    - n2_minimal_body_metrics_packet
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
  not_a_calendar_roadmap: true
  backlog_expansion_allowed: false
```

## Parked/Future Nodes

```yaml
parked_future_nodes:
  - node_id: n5_supplements_fasting_brain_diet_research_gate
    parked_reason: "Requires external evidence and safety framing; not needed to unblock current process."
  - node_id: n6_macrofactor_or_heavy_tracking_revival
    parked_reason: "Conflicts with low-friction constraint unless explicitly reshaped later."
  - node_id: full_food_database_or_api_automation
    parked_reason: "High setup burden; deferred by current Goal/Queue scope."
  - node_id: perfect_full_body_transformation_plan
    parked_reason: "Too broad; would create planning bloat before core process validation."
  - node_id: clinical_nutrition_or_medical_protocol
    parked_reason: "Out of current scope and would require a different evidence/safety standard."
```

## Map Update Policy

```yaml
map_update_policy:
  branch_chats_may_mutate_map: false
  allowed_mutation_points:
    - M0_DIRECTION_MAP
    - R1_GOAL_REVIEW_DISTILL
    - P9_PHASE_CLOSE
    - parent_synthesis_after_parallel_branches
  forbidden_behavior:
    - branch_chat_direct_map_mutation
    - backlog_expansion_without_active_front_reason
    - calendar_roadmap_creation
    - replacing_phase_or_goal_state
    - inventing_downstream_route_from_conflicted_state
  next_update_triggers:
    - "After S3_DECIDE on nutrition loop/tooling policy."
    - "After a repaired/new nutrition implementation Goal is shaped."
    - "After the accepted nutrition loop is installed/setup, returned for repair, or explicitly blocked."
    - "After a scoped training/cardio/recovery evidence or decision slice is completed."
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`
