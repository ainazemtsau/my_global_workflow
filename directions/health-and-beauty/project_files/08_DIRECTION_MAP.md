# 08 Direction Map - Health and Beauty

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Health and Beauty"
  schema: direction_map.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/health-and-beauty/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: p9_phase_close_complete
  last_updated: "2026-05-22"
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
  last_reviewed_stage: P9_PHASE_CLOSE
  migration_status: migrated_with_2026_05_19_objective_architecture_frontier_repair
  migration_source:
    mode: approved_repository_maintenance_formalization
    direction_path: "directions/health-and-beauty"
    source_ref: "codex/direction-health-and-beauty"
    patch_id: health_beauty_objective_architecture_migration_2026_05_19
  corrected_state:
    summary: "P9 closed the repo-backed multi-chat Project `Питание` nutrition loop Phase complete; next route is P0_PHASE_START to select the next non-duplicate Phase."
    blocks:
      - reopening_accepted_project_pitanie_setup_goal_without_new_evidence
      - launching_stale_project_pitanie_e1_route
    does_not_block:
      - P0_PHASE_START
      - using_phase_memory_bridge
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
      phase_memory_paths:
        - "directions/health-and-beauty/project_files/07_PHASE_MEMORY_INDEX.md"
        - "directions/health-and-beauty/phases/ai-nutrition-operating-layer/phase_close_summary.md"
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
      status: closed_complete
      binding_reason: "Nutrition execution without heavy manual tracking is the current documented constraint and directly supports the broader body-transformation initiative."
    active_goal_binding:
      goal_id: null
      goal_path: null
      goal_name: null
      status: none
      latest_completed_goal_id: nutrition-project-operational-setup-v0
      latest_completed_goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/nutrition-project-operational-setup-v0"
      latest_completed_goal_status: closed_under_closed_phase
      binding_reason: "P9 closed the Phase after R1 accepted the repo-backed multi-chat Project `Питание` nutrition loop Goal complete based on U1/setup/real-use validation."
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
    - path_id: first_weekly_body_transformation_correction_loop
      verdict: selected_next_frontier
      rationale: "Result-First repair requires the next frontier to face the body-transformation result directly: collect only the necessary state and produce the first weekly correction decision."
    - path_id: standalone_minimal_body_metrics_packet
      verdict: rejected_as_standalone_phase
      rationale: "A metrics/readiness packet is useful only as an internal gate inside the correction loop, not as a standalone support-artifact Phase."
    - path_id: decide_minimal_nutrition_loop_shape_and_tooling
      verdict: selected
      rationale: "Repaired the active frontier after user correction and led to an accepted basis-valid nutrition loop before phase close review."
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
  selected_path_rationale: "R1 accepted the repaired repo-backed multi-chat Project `Питание` nutrition loop Goal complete and P9 closed the Phase; run P0_PHASE_START to shape the first result-facing weekly body-transformation correction loop."
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
    - "No reopening the accepted nutrition setup Goal before the P9 phase gate."
    - "No stale Project `Питание` E1 launch."
    - "No standalone metrics/readiness/documentation packet Phase that does not produce a correction decision."
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes:
    - node_id: d_nutrition_loop_shape_and_tooling
      initiative_id: body-transformation-20kg-strength-health
      label: "Decide minimal nutrition loop shape and tool/container policy"
      type: active_front
      status: done_accepted_phase_closed
      purpose: "Choose the minimal low-friction nutrition loop and the tool/container mix before shaping or executing any implementation Goal."
      success_signal:
        - "R1 accepted the repo-backed multi-chat Project `Питание` nutrition loop based on U1/setup/real-use validation."
        - "User-confirmed real use: Project `Питание` is in process, menu has been composed, and setup works."
        - "Next routing is Phase close review, not more nutrition setup by default."
      human_burden_policy: "No detailed calorie-app ledger; use exception-only tracking and compact state updates."

    - node_id: n2_first_weekly_body_transformation_correction_loop
      initiative_id: body-transformation-20kg-strength-health
      label: "First weekly body-transformation correction loop"
      type: active_front
      status: candidate_next_frontier_for_P0
      purpose: "Shape the smallest recurring body-transformation loop that gathers the minimum necessary state and produces a weekly correction decision."
      internal_gate: "Minimal metrics/state packet is required inside the loop, not as its own standalone Phase."
      success_signal:
        - "Weekly state inputs are small enough to sustain."
        - "The loop produces the first body-transformation correction decision."
        - "The output can inform later training/cardio/recovery choices without creating a broad tracker."
      non_goal: "Do not create a standalone n2_minimal_body_metrics_packet Phase framing, full quantified-self tracker, or food database."

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
      to: n2_first_weekly_body_transformation_correction_loop
      relation: enables
      reason: "An accepted nutrition loop needs a result-facing weekly correction loop, with the state packet as its internal input gate."
    - from: n2_first_weekly_body_transformation_correction_loop
      to: n3_training_cardio_recovery_decision_slice
      relation: informs
      reason: "Training/cardio/recovery choice should reflect the first weekly correction decision and its minimal state inputs."
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
  primary_node: n2_first_weekly_body_transformation_correction_loop
  reason: "The nutrition loop node is accepted and Phase-closed; the next smallest non-duplicate frontier is a result-facing weekly correction loop. The minimal metrics/state packet is an internal gate for that loop, not a standalone support artifact."
  current_route_binding:
    route_state: post_phase_close_pending_P0
    route: P0_PHASE_START
    rule: "Run P0 after repository maintenance/read-back and Project Files refresh; candidate frontier is n2_first_weekly_body_transformation_correction_loop, not a selected Goal."
  parallel_candidate_nodes: []
  parked_nodes:
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
    - n5_supplements_fasting_brain_diet_research_gate
    - n6_macrofactor_or_heavy_tracking_revival
  completed_nodes:
    - d_nutrition_loop_shape_and_tooling
  candidate_next_frontier:
    - n2_first_weekly_body_transformation_correction_loop
  superseded_nodes:
    - "stale Project `Питание` setup route"
    - "MacroFactor/heavy tracking default path"
    - "standalone n2_minimal_body_metrics_packet Phase framing"
```

## Horizon Slice

```yaml
horizon_slice:
  id: h_low_friction_evidence_based_body_transformation_loop
  statement: "Do not jump to a perfect full-body plan. The nutrition loop is accepted and Phase-closed; next shape the first weekly body-transformation correction loop, with minimal body metrics/state as its internal gate, then run one evidence-backed training/cardio/recovery decision slice, then integrate into a daily/weekly operator."
  node_ids:
    - d_nutrition_loop_shape_and_tooling
    - n2_first_weekly_body_transformation_correction_loop
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
  not_a_calendar_roadmap: true
  backlog_expansion_allowed: false
```

## Parked/Future Nodes

```yaml
parked_future_nodes:
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
    - n5_supplements_fasting_brain_diet_research_gate
    - n6_macrofactor_or_heavy_tracking_revival
```

```yaml
parked_future_node_details:
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

## Map Delta Notes

```yaml
map_delta:
  type: result_first_local_direction_migration
  node_id: n2_first_weekly_body_transformation_correction_loop
  date: "2026-05-22"
  summary: "Active front changed from standalone n2_minimal_body_metrics_packet Phase framing to a result-facing first weekly body-transformation correction loop."
  previous_frontier_node: n2_minimal_body_metrics_packet
  new_frontier_node: n2_first_weekly_body_transformation_correction_loop
  lifecycle_state_reconciliation:
    active_phase_created: false
    active_goal_created: false
    route_remains: P0_PHASE_START
  horizon_slice_delta: "Minimal body metrics/state becomes the first internal gate inside the weekly correction loop, not a standalone Phase."
  active_front_delta: "Advance from support-artifact packet framing to P0 selection of a result-facing correction loop."
  nodes_completed:
    - d_nutrition_loop_shape_and_tooling
  nodes_unblocked:
    - n2_first_weekly_body_transformation_correction_loop
  nodes_parked:
    - n3_training_cardio_recovery_decision_slice
    - n4_integrated_daily_weekly_ai_operator
    - n5_supplements_fasting_brain_diet_research_gate
    - n6_macrofactor_or_heavy_tracking_revival
  nodes_superseded:
    - "stale Project `Питание` setup route"
    - "MacroFactor/heavy tracking default path"
    - "standalone n2_minimal_body_metrics_packet Phase framing"
  m0_review_needed: false
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
    - "After P0_PHASE_START selects the next non-duplicate Phase."
    - "After G1_GOAL_SHAPE defines the first weekly body-transformation correction loop."
    - "After the minimal metrics/state packet is accepted as the first internal gate inside that loop."
    - "After a scoped training/cardio/recovery evidence or decision slice is completed."
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`
