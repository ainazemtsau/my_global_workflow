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
  last_refresh_at: "2026-05-19"
  refresh_source: "OA-MIGRATION-SMP-EXOCORTEX-CORE-FOUNDATION-2026-05-19"

focus:
  current_focus: "Prepare E1 execution brief for EXOCORTEX Core Foundation Definition."
  route_stage: E1_EXECUTION_BRIEF
  route_note: "Run E1 only after G1 repository patch apply/read-back and Project Files cache refresh. E1 must prepare minimum HOW for the definition artifact, not implementation."
  same_chat_allowed: false
  boundary_trigger: exocortex_foundation_goal_shaped_pending_E1
  pending_state_carried: true
  pending_patch_pointer: "P0-2026-05-14-exocortex-app-foundation-repair"
  last_stage_result_pointer: "G1 formalized EXOCORTEX Core Foundation Definition on 2026-05-19."

boundary:
  do_not_start_implementation: true
  do_not_choose_tech_stack: true
  do_not_design_full_architecture: true
  do_not_expand_to_product_roadmap: true
  do_not_run_broad_research_before_explicit_gap: true
  do_not_create_kernel_min_proof_brief: true
  do_not_delete_old_goal_folder: true
  do_not_create_task_master_graph: true
  do_not_run_codex_product_execution: true
  do_not_treat_EXOCORTEX_CONCEPT_SEED_FULL_as_execution_roadmap: true
```

## Next launch pointer

```yaml
next_launch:
  recommended_next_stage: E1_EXECUTION_BRIEF
  launch_method: new E1 run after G1 repository patch apply/read-back and Project Files refresh
  current_phase_name: "EXOCORTEX App Foundation"
  current_phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  active_goal: EXOCORTEX Core Foundation Definition
  active_goal_path: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition
  required_inputs:
    - "Direction: Solo Max Productive"
    - "Current Phase: EXOCORTEX App Foundation"
    - "Current focus: Prepare E1 execution brief for EXOCORTEX Core Foundation Definition"
    - "Phase path: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
    - "Old superseded Goal: Personal Workflow App Kernel Min Proof"
    - "EXOCORTEX concept source: directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/source_materials/EXOCORTEX_CONCEPT_SEED_FULL.md"
    - "Accepted Direction Objective: EXOCORTEX persistent personal AI brain / external-brain application."
    - "Next Action Proof: basis_valid true; route_valid true; launch_allowed false until G1 repository patch apply/read-back and refreshed Project Files are available."
  missing_context_behavior: ask_only_if_blocking
```
