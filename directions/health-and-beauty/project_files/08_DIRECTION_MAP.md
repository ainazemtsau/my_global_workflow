# 08 Direction Map - Health and Beauty

```yaml
artifact_control:
  artifact_name: "08 Direction Map - Health and Beauty"
  schema: direction_map.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/health-and-beauty/project_files/08_DIRECTION_MAP.md"
  default_load: yes
  freshness: m0_migrated
  last_updated: "2026-05-16"
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
  current_execution_state_confidence: low
  last_reviewed_stage: M0_DIRECTION_MAP
  migration_status: migrated_with_downstream_state_conflict_recorded
  migration_source:
    mode: post_rollout_m0_migration
    direction_path: "directions/health-and-beauty"
    source_ref: "main"
    source_commit_or_head_sha: "d170a8c703034ea44285d88a3abaedf36c21b9cd"
  known_state_conflict:
    summary: "Default Project Files 00-06 project next_route E1_EXECUTION_BRIEF / execution_brief_pending, while the Codex-verified migration bundle reports that active goal artifacts include an E1 brief, an F0 v0 artifact, and an execution_log latest entry where F0 returned PARTIAL with apply/read-back validation still required before R1."
    blocks:
      - downstream_route_selection
      - claiming_current_goal_ready_for_review
      - claiming_project_files_are_fully_fresh
    does_not_block:
      - compact_direction_map_initialization
      - recording_current_initiative
      - selecting_active_front_at_strategy_level
    conflicting_paths:
      project_file_projection_paths:
        - "directions/health-and-beauty/project_files/00_DIRECTION_START_HERE.md"
        - "directions/health-and-beauty/project_files/01_DIRECTION_STATE.md"
        - "directions/health-and-beauty/project_files/02_CURRENT_PHASE.md"
        - "directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md"
        - "directions/health-and-beauty/project_files/04_ACTIVE_GOAL.md"
        - "directions/health-and-beauty/project_files/05_PORTFOLIO_QUEUE.md"
        - "directions/health-and-beauty/project_files/06_CONTEXT_LIBRARY_INDEX.md"
      active_goal_artifact_paths_reported_by_bundle:
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
  intent: "Build a hard but sustainable AI-assisted body-transformation operating system covering nutrition, training/cardio, recovery, minimal metrics, and periodic correction while keeping manual routine burden low."
  why_now:
    - "User identified excess weight as the largest current health/beauty problem."
    - "User can sustain a strict process if the process is clear and routine burden is low."
    - "Current active Phase already targets the main documented constraint: no stable AI nutrition process without heavy tracking."
    - "Manual calorie-app logging is considered too high-friction for the desired process."
  success_signal:
    - "A low-friction AI-assisted process exists and can be run through ChatGPT or approved storage without detailed manual calorie/macro ledger."
    - "Nutrition layer can create/update menu, advise current day, correct after overeating/off-menu eating, add recipe/prep notes, run day/week summary, and produce durable state update/save output."
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
      phase_name: "Собрать AI-операционный слой питания без тяжёлого трекинга"
      binding_reason: "Nutrition execution without heavy manual tracking is the current documented constraint and directly supports the broader body-transformation initiative."
    active_goal_binding:
      goal_id: ai-nutrition-operating-layer-v0
      goal_path: "directions/health-and-beauty/phases/ai-nutrition-operating-layer/goals/ai-nutrition-operating-layer-v0"
      goal_name: "Собрать AI Nutrition Operating Layer v0"
      binding_reason: "The Goal creates the low-friction nutrition operating layer needed before broader training/cardio/recovery integration."
    current_risk:
      - "Project File projections and active goal artifact state disagree; downstream route must not be inferred until reconciled."
      - "Broad health/fitness optimization can easily become overbuilt unless sliced after the nutrition layer is validated."
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
    - path_id: continue_repair_validate_current_nutrition_layer_then_integrate
      verdict: selected
      rationale: "Reuses current active Phase/Goal, removes the highest-friction constraint, and avoids restarting into a broad plan."
    - path_id: restart_full_body_transformation_master_plan
      verdict: rejected_for_now
      rationale: "Too broad and likely to create planning bloat before the current nutrition layer is usable."
    - path_id: macrofactor_or_detailed_tracker_default
      verdict: rejected_for_default
      rationale: "Conflicts with low-friction constraint and current files mark MacroFactor-centered work as superseded/paused."
    - path_id: research_training_cardio_supplements_first
      verdict: parked
      rationale: "Valuable later, but requires evidence and decisions; should not precede current state reconciliation."
    - path_id: parallel_training_cardio_while_nutrition_conflicted
      verdict: parked
      rationale: "Adds scope before the current active goal state is safe to route."
  selected_path_rationale: "Use the current AI Nutrition Operating Layer as the first constraint-removal node under the broader body-transformation initiative; record the state conflict; do not invent downstream route; after validation/review, add only the next narrow evidence-backed slice."
  major_assumptions:
    - "User can sustain a strict process if the process is clear and routine work is offloaded."
    - "Low-burden execution is more important than perfect measurement at the current stage."
    - "Nutrition remains the first practical bottleneck because the active Phase/Goal already targets it and the user identifies weight as the main problem."
    - "Training/cardio/recovery/supplement decisions need later scoped evidence or decision work, not M0."
  scope_cuts:
    - "No calendar roadmap."
    - "No broad backlog."
    - "No detailed calorie/macro ledger."
    - "No MacroFactor revival as default."
    - "No supplement/fasting/brain-diet recommendation inside M0."
    - "No downstream route assertion until state conflict is reconciled."
```

## Compact Initiative Graph

```yaml
compact_initiative_graph:
  nodes:
    - node_id: n1_repair_validate_ai_nutrition_layer_v0
      initiative_id: body-transformation-20kg-strength-health
      label: "Repair/validate AI Nutrition Operating Layer v0 state"
      type: active_front
      status: active_with_state_conflict
      purpose: "Make the current low-friction nutrition layer usable and validated before broader body-transformation integration."
      success_signal:
        - "Project File projections and active goal artifacts are reconciled or a precise blocker is named."
        - "AI Nutrition Operating Layer v0 is either validated/review-ready or returned to the correct execution/repair route."
        - "The layer supports menu, day advice, exception correction, recipe/prep notes, review/state update, and restart/context refresh flows."
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
    - from: n1_repair_validate_ai_nutrition_layer_v0
      to: n2_minimal_body_metrics_packet
      relation: enables
      reason: "A validated nutrition layer needs a minimal state input format for ongoing correction."
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
  primary_node: n1_repair_validate_ai_nutrition_layer_v0
  reason: "This is the smallest credible path because it preserves current progress, removes the known low-friction nutrition constraint, and avoids a broad restart."
  current_route_binding:
    route_state: unresolved_due_state_conflict
    rule: "Do not infer E1/F0/R1/B1 or other next route from this map. Resolve by verified read-back / appropriate lifecycle stage."
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
  statement: "Do not jump to a perfect full-body plan. First make the low-friction AI nutrition layer usable/validated; then define minimal body metrics; then run one evidence-backed training/cardio/recovery decision slice; then integrate into a daily/weekly AI operator."
  node_ids:
    - n1_repair_validate_ai_nutrition_layer_v0
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
    - "After active goal state conflict is reconciled."
    - "After AI Nutrition Operating Layer v0 is accepted, returned for repair, or explicitly blocked."
    - "After a scoped training/cardio/recovery evidence or decision slice is completed."
```

## End-of-file marker

`END_OF_FILE: directions/health-and-beauty/project_files/08_DIRECTION_MAP.md`
