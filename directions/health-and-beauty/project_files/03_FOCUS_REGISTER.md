# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/health-and-beauty
  source_files:
    - "directions/health-and-beauty/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-12"
  source_freshness: active_git_file
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Shape the first Goal for the active Phase: Health/Body Operator training process v0."
  route_stage: G1_GOAL_SHAPE
  same_chat_allowed: false
  boundary_trigger: p0_phase_start_complete
  pending_state_carried: true
  pending_patch_pointer: "p0_create_first_working_health_body_operator_training_v0_2026_05_23"
  last_stage_result_pointer: "P0_PHASE_START created active Phase first-working-health-body-operator-training-v0 after user approval."
  human_correction: "Workflow builds and changes the operational process. The Health/Body Operator Project runs daily nutrition/training/logging/adjustment. Workflow does not track daily execution."
  stale_prior_focus: "Post-close P0 Phase Start is complete after repository patch/read-back. Old P0 route and Project `Питание` setup routes are historical only."
```

## Active Goal

No active Goal.

## Recommended next route

`G1_GOAL_SHAPE`

Shape the first Goal:

`shape-operational-boundary-and-training-process-v0`

The Goal must bind to graph node `operational_boundary_gate` and preserve the invariant that daily logs and corrections happen in the Operational Project, not in workflow.
