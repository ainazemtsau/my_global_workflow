# 02_CURRENT_PHASE.md

```yaml
project_file_control:
  file: 02_CURRENT_PHASE.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/02_CURRENT_PHASE.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
current_phase:
  state: active
  phase_id: first-working-health-body-operator-training-v0
  phase_name: "Первый рабочий Health/Body Operator: тренировочный процесс v0"
  phase_path: "directions/health-and-beauty/phases/first-working-health-body-operator-training-v0"
  started_at: "2026-05-23"
  map_link: n2_first_weekly_body_transformation_correction_loop
  active_goal_pointer: null
  active_goal_title: null
  next_route: G1_GOAL_SHAPE
  next_goal_seed: shape-operational-boundary-and-training-process-v0
  phase_closeable: false
```

## Phase Result Contract

```yaml
phase_result_contract:
  phase_candidate: first-working-health-body-operator-training-v0
  parent_horizon_or_initiative: h_low_friction_evidence_based_body_transformation_loop
  current_real_state: "Nutrition loop works enough to continue, but training/activity process does not yet exist as an autonomous operator capability."
  next_observable_state: "Health/Body Operator Project can autonomously run training process v0."
  primary_result_delta: "Operational Project gains training planning/logging/adjustment capability while workflow remains the system-building layer."
  first_operational_action: "Shape the operational boundary and training-process v0 Goal before E1/U1 execution planning."
  support_artifacts_allowed:
    - "Operational boundary invariant"
    - "Operator Project structure"
    - "Training input contract"
    - "Training process protocol"
    - "Handoff package"
    - "Capability validation note"
    - "Local customization lane"
  max_pre_execution_support_goals: 1
  closure_means: "Capability validation proves the operational Project can perform state -> plan -> log-inside-Project -> adjustment."
  not_closed_by:
    - "Daily training logs in workflow"
    - "Only a training theory document"
    - "Only Project instructions without capability validation"
    - "Separate training Project created by default"
  verdict:
    standalone_phase_allowed: true
    reason: "This is a result-facing operating-process Phase, not a standalone support artifact."
```

## Operational Boundary Invariant

Workflow builds, repairs, audits, and evolves the operational health/body process. It does not run daily nutrition, training, metric logging, or week-to-week plan management.

Daily operation happens inside the separate Health/Body Operator ChatGPT Project. That Project may contain specialist chats for nutrition, training, daily decisions, weekly review/metrics, and process customization.

The operational Project should not know workflow stages, phase IDs, goal IDs, Direction Map mechanics, or workflow routing. It should behave like a practical health/body operator for the user.

Workflow may know the operational Project structure, source files, protocols, and customization boundaries. Small local process fixes can be handled inside the operational Project through a lightweight Codex/save-only maintenance lane scoped to operational project files. Strategic redesign, new tools, major process changes, evidence-heavy decisions, or global dissatisfaction return to the Health and Beauty workflow.

## Phase Delivery Graph

```yaml
phase_delivery_graph:
  version: phase_delivery_graph.v1

  phase_outcome:
    outcome_id: first_working_health_body_operator_training_v0_live
    one_sentence_result: "The Health/Body Operator Project can autonomously run the first training/activity process v0, while workflow remains the system-builder and escalation layer."
    direction_visible_result: "The user has an operational Project that can plan training, accept training logs inside the Project, adjust the process, and support small local customization without using workflow as the daily tracking surface."
    definition_of_done:
      - predicate: "Workflow/operator boundary is explicit and persistent."
        evidence_required: "Operational Boundary Invariant is present in current Phase state and handoff package."
      - predicate: "Unified operator structure supports nutrition continuation plus training v0."
        evidence_required: "Operator role/chats/source-file structure is defined enough for setup."
      - predicate: "Training process v0 is specified."
        evidence_required: "Process contract covers intake, weekly plan, fallback, log format, adjustment behavior, and local customization lane."
      - predicate: "Capability validation passes."
        evidence_required: "Dry-run or first Project run demonstrates state -> plan -> log -> adjustment inside the Operational Project."
    not_done_if:
      - "Workflow becomes the place where daily nutrition/training logs are maintained."
      - "Only a generic training theory document exists."
      - "Only Project instructions exist without plan/log/adjustment capability."
      - "A separate training Project is created without explicit user decision."

  completion_logic:
    closure_mode: all_required_nodes_done
    required_nodes:
      - operational_boundary_gate
      - operator_project_structure_gate
      - training_process_input_contract
      - training_process_v0_design
      - operational_project_handoff_package
      - capability_validation_gate
      - local_customization_lane
    optional_nodes_do_not_block_closure: true

  flow_policy:
    max_active_goals: 1
    branch_workstreams_are_not_active_goals: true
    optional_expansion_policy: park_by_default
    support_gate_policy: embed_unless_primary_or_blocking
    parallel_policy: sequential_by_default_parallel_by_admission

  nodes:
    - node_id: operational_boundary_gate
      node_type: support_gate
      status: ready
      required_for_closure: true
      why_needed_for_phase_outcome: "Prevents workflow from becoming the daily execution surface."
      done_when: "Boundary is explicit: workflow builds/changes the system; Operational Project runs nutrition, training, logs, adjustments, and daily/weekly operations."
      evidence_required: "Boundary invariant appears in Phase state and later operator handoff."
      owner_stage: G1_GOAL_SHAPE
      next_allowed_stage: G1_GOAL_SHAPE

    - node_id: operator_project_structure_gate
      node_type: support_gate
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "Training v0 must live inside a unified Health/Body Operator, not a separate default Project."
      done_when: "Specialist chats/roles are specified for nutrition, training, daily decisions, weekly review/metrics later, and process customization."
      evidence_required: "Compact operator structure accepted."

    - node_id: training_process_input_contract
      node_type: support_gate
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "Training specialist needs minimal safe inputs without creating a heavy tracker."
      done_when: "Minimum input contract exists for schedule, time, location/equipment, limitations, level, goals, preferences, and fallback rules."
      evidence_required: "Training intake contract."

    - node_id: training_process_v0_design
      node_type: result_slice
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "This is the actual designed training operating process."
      done_when: "Process defines weekly planning, minimum viable workout, fallback day, log format, adjustment behavior, pain/fatigue/skip handling, and local plan change behavior."
      evidence_required: "Training process v0 protocol."

    - node_id: operational_project_handoff_package
      node_type: execution_package
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "The operational Project needs loadable instructions/protocols."
      done_when: "Handoff package is ready for Project setup/update without workflow jargon."
      evidence_required: "Project instruction/protocol file set or equivalent."

    - node_id: capability_validation_gate
      node_type: validation_gate
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "Proves the Project can operate, not just describe a process."
      done_when: "Dry-run or first Project run demonstrates: minimal state -> first-week plan -> sample/real log inside Operational Project -> adjustment."
      evidence_required: "Capability validation note; no daily logs stored in workflow."

    - node_id: local_customization_lane
      node_type: support_gate
      status: candidate
      required_for_closure: true
      why_needed_for_phase_outcome: "Small process annoyances should be fixable inside the Operational Project without full workflow restart."
      done_when: "Local customization lane distinguishes daily operation, local process tweaks, and strategic redesign escalation."
      evidence_required: "Customization/escalation rules."

    - node_id: nutrition_polish_by_real_problem
      node_type: optional_expansion
      status: parked
      required_for_closure: false
      why_needed_for_phase_outcome: "Nutrition can be improved later from concrete friction, not reopened by default."

    - node_id: minimal_metrics_weekly_review
      node_type: optional_expansion
      status: parked
      required_for_closure: false
      why_needed_for_phase_outcome: "Metrics/review become next layer after training v0 or when real friction demands them."

    - node_id: supplements_fasting_brain_diet_research
      node_type: parked
      status: parked
      required_for_closure: false

    - node_id: macrofactor_or_heavy_tracking_revival
      node_type: parked
      status: rejected
      required_for_closure: false

  next_node:
    node_id: operational_boundary_gate
    route: G1_GOAL_SHAPE
    reason: "The first Goal must shape the operational boundary and training-process v0 contract before any execution/handoff work."

  graph_delta_policy:
    seed_owner: P0_PHASE_START
    next_node_selection_owner: G0_GOAL_SELECT
    goal_binding_owner: G1_GOAL_SHAPE
    execution_topology_owner: E1_EXECUTION_BRIEF
    post_goal_delta_owner: R1_GOAL_REVIEW_DISTILL
    closure_owner: P9_PHASE_CLOSE
```

## First Goal seed

```yaml
first_goal_candidate:
  candidate_id: shape-operational-boundary-and-training-process-v0
  name: "Сформировать границу workflow/operator и Goal-контракт тренировочного процесса v0"
  target_graph_node: operational_boundary_gate
  recommended_next_stage: G1_GOAL_SHAPE
  confidence: high
```

## Guard state

* Active Goal unresolved: `no`
* Active Goal shaped: `no`
* Phase can close now: `no`
* Current blocker: repository patch apply/read-back and Project Files refresh before G1.
* Tooling policy: AI/ChatGPT/Project/app/storage are tools, not the objective.
* Workflow boundary: workflow does not run daily training/nutrition logs.
* Operational Project boundary: Project runs daily processes and local process customization; it does not know workflow stages.
* Direction Map note: `08_DIRECTION_MAP.md` Active Front remains `n2_first_weekly_body_transformation_correction_loop`; old route-binding text is stale-but-nonblocking for named next stage `G1_GOAL_SHAPE`.
