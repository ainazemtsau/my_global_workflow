# 03_FOCUS_REGISTER.md

```yaml
artifact_control:
  artifact_name: "03 Focus Register"
  schema: focus_register.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/03_FOCUS_REGISTER.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-12"
  refresh_source: "G1-2026-05-12-personal-workflow-app-kernel-min-proof"

focus:
  current_focus: "Prepare the minimum execution basis for the Personal Workflow App Kernel Min Proof."
  route_stage: E1_EXECUTION_BRIEF
  same_chat_allowed: false
  boundary_trigger: active_goal_execution_basis_needed
  pending_state_carried: true
  pending_patch_pointer: "G1-2026-05-12-personal-workflow-app-kernel-min-proof"
  last_stage_result_pointer: "G1_GOAL_SHAPE formalized output 2026-05-12"

boundary:
  do_not_start_implementation: true
  do_not_choose_tech_stack: true
  do_not_design_full_architecture: true
  do_not_expand_to_product_roadmap: true
  do_not_run_broad_research_before_explicit_gap: true
```

## Next launch pointer

```yaml
next_launch:
  recommended_next_stage: E1_EXECUTION_BRIEF
  required_inputs:
    - "Active Phase: Personal Workflow App Kernel Exploration"
    - "Active Goal: Personal Workflow App Kernel Min Proof"
    - "Goal Contract: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/00_GOAL_CONTRACT.md"
    - "Goal Working Context: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/01_GOAL_WORKING_CONTEXT.md"
  missing_context_behavior: ask_only_if_blocking
```
