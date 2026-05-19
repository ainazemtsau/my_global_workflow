# 01_DIRECTION_STATE.md

```yaml
artifact_control:
  artifact_name: "01 Direction State"
  schema: direction_state.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/01_DIRECTION_STATE.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-19"
  refresh_source: "OA-MIGRATION-SMP-EXOCORTEX-CORE-FOUNDATION-2026-05-19"

direction:
  id: solo-max-productive
  name: directions/solo-max-productive
  state: active
  workflow_version: vNext-R
  direction_objective: "Build EXOCORTEX as a persistent personal AI brain / external-brain application that preserves memory, compiles context, uses tools and workspace surfaces, learns from outcomes, maintains Reality Alignment, and compounds with future LLM improvements."
  current_phase_pointer: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_phase_name: "EXOCORTEX App Foundation"
  current_phase_status: active
  phase_repair:
    repair_mode: repair_existing_phase_path_in_place
    previous_phase_name: "Personal Workflow App Kernel Exploration"
    repaired_phase_name: "EXOCORTEX App Foundation"
    repair_reason: "User clarified that the strategic target is EXOCORTEX as a persistent personal AI brain / external-brain application. The active migration target is EXOCORTEX Core Foundation, not implementation, stack choice, full architecture, or product execution."
    path_note: "Legacy folder slug retained temporarily to avoid duplicate active Phase state before foundation definition."
  active_goal_pointer: null
  active_goal_name: null
  active_goal_status: none_pending_G1
  superseded_goal_pointer: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  superseded_goal_name: "Personal Workflow App Kernel Min Proof"
  superseded_goal_status: superseded_provenance_not_executable
  selected_goal_candidate: "EXOCORTEX Product Foundation Definition"
  selected_goal_candidate_id: "G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION"
  selected_goal_candidate_status: approved_for_G1_GOAL_SHAPE
  next_route: G1_GOAL_SHAPE
  route_note: "Launch G1 only after repository patch apply/read-back, Project Files cache refresh, exact G1 prompt availability, and EXOCORTEX concept source availability."
  last_updated: "2026-05-19"

state_note:
  old_phase_pointer: "directions/solo-max-productive/phases/vnext-one-goal-smoke-test"
  old_phase_status: "superseded_obsolete_test_state"
  old_selected_candidate: "Create Lightweight Codex Small-Fix Lane"
  old_candidate_status: "not_current_unless_user_reactivates"
  previous_phase_intent: "Develop the current personal Workflow toward a possible custom workflow app/kernel."
  corrected_phase_intent: "Define EXOCORTEX Core Foundation as expandable product substrate for the personal AI brain."
  old_goal_recovery_status: "superseded provenance; not executable unless explicitly reactivated by later Human Decision."
  corrected_foundation_intent: "Define the EXOCORTEX Core Foundation before implementation, stack choice, full architecture, product execution, or broad roadmap work."
  critical_constraint: "Do not implement, choose stack, design full architecture, create product execution graph, or attempt full roadmap execution before G1 shapes the first Goal."

project_files_export_state:
  canonical_folder: "directions/solo-max-productive/project_files"
  last_refresh_at: "2026-05-19"
  last_refresh_source: "OA-MIGRATION-SMP-EXOCORTEX-CORE-FOUNDATION-2026-05-19"
  stale_files: []
  required_refresh: []
```

## Current state summary

- Current Phase: `EXOCORTEX App Foundation`
- Current Phase path: `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration`
- Current Phase status: active / repaired in place by `P0_PHASE_START`
- Old Active Goal: `Personal Workflow App Kernel Min Proof`
- Old Goal status: superseded provenance; not executable.
- Active Goal: none pending `G1_GOAL_SHAPE`
- Direction Objective: build EXOCORTEX as a persistent personal AI brain / external-brain application.
- Current focus: shape EXOCORTEX Core Foundation.
- Required first Goal after Phase repair: `EXOCORTEX Product Foundation Definition`, now interpreted as EXOCORTEX Core Foundation Definition.
- Next route: `G1_GOAL_SHAPE` after repository patch, Project Files refresh, exact G1 prompt availability, and `EXOCORTEX_CONCEPT_SEED_FULL.md` availability.
