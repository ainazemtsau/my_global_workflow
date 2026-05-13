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
  last_refresh_at: "2026-05-13"
  refresh_source: "B1-2026-05-13-active-goal-misframed-recovery"

focus:
  current_focus: "Repair active Goal framing and shape the replacement Goal: Personal Workflow System Core and MVP Definition."
  route_stage: G1_GOAL_SHAPE
  same_chat_allowed: false
  boundary_trigger: active_goal_misframed
  pending_state_carried: true
  pending_patch_pointer: "B1-2026-05-13-active-goal-misframed-recovery"
  last_stage_result_pointer: "B1_PROBLEM formalized active Goal revision route 2026-05-13"

boundary:
  do_not_start_implementation: true
  do_not_choose_tech_stack: true
  do_not_design_full_architecture: true
  do_not_expand_to_product_roadmap: true
  do_not_run_broad_research_before_explicit_gap: true
  do_not_create_kernel_min_proof_brief: true
  do_not_delete_old_goal_folder: true
```

## Next launch pointer

```yaml
next_launch:
  recommended_next_stage: G1_GOAL_SHAPE
  replacement_goal_candidate: "Personal Workflow System Core and MVP Definition"
  required_inputs:
    - "Active Phase: Personal Workflow App Kernel Exploration"
    - "Old contested Goal: Personal Workflow App Kernel Min Proof"
    - "Old Goal Contract: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/00_GOAL_CONTRACT.md"
    - "Old Goal Working Context: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof/01_GOAL_WORKING_CONTEXT.md"
    - "B1 result: active_goal_misframed; proof framing redundant; replacement Goal should define core/base system or MVP."
  missing_context_behavior: ask_only_if_blocking
```
