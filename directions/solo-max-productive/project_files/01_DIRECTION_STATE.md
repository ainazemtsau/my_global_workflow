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
  last_refresh_at: "2026-05-13"
  refresh_source: "G1-2026-05-13-exocortex-phase-repair"

direction:
  id: solo-max-productive
  name: directions/solo-max-productive
  state: active
  workflow_version: vNext-R
  current_phase_pointer: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_phase_status: repair_required_pending_p0
  proposed_phase_repair:
    proposed_phase_name: "EXOCORTEX App Foundation"
    proposed_phase_status: pending_P0_PHASE_START
    repair_reason: "User clarified that the strategic target is the future EXOCORTEX application / personal external brain. The current workflow remains the construction workflow and is not being replaced now."
  active_goal_pointer: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  active_goal_name: "Personal Workflow App Kernel Min Proof"
  active_goal_status: invalidated_by_phase_repair_pending_p0
  selected_goal_candidate: "EXOCORTEX Product Foundation Definition"
  selected_goal_candidate_status: pending_after_phase_repair
  next_route: P0_PHASE_START
  route_note: "Launch via Router/new P0 run after repository patch apply/read-back and Project Files cache refresh. G1 stopped and did not launch P0 directly."
  last_updated: "2026-05-13"

state_note:
  old_phase_pointer: "directions/solo-max-productive/phases/vnext-one-goal-smoke-test"
  old_phase_status: "superseded_obsolete_test_state"
  old_selected_candidate: "Create Lightweight Codex Small-Fix Lane"
  old_candidate_status: "not_current_unless_user_reactivates"
  previous_phase_intent: "Develop the current personal Workflow toward a possible custom workflow app/kernel."
  corrected_phase_intent: "Build the foundation for the future EXOCORTEX app / personal external brain while the current ChatGPT + GitHub + Codex workflow remains the construction workflow."
  old_goal_recovery_status: "superseded because the current ChatGPT + GitHub + Codex workflow has already proven the kernel/workflow loop enough."
  corrected_replacement_intent: "Define the EXOCORTEX product/application foundation, not a merely convenient current-workflow replacement."
  critical_constraint: "Do not implement, choose stack, design full architecture, create product execution graph, or attempt full roadmap execution before P0 repairs the Phase and G1 shapes the first Goal."

project_files_export_state:
  canonical_folder: "directions/solo-max-productive/project_files"
  last_refresh_at: "2026-05-13"
  last_refresh_source: "G1-2026-05-13-exocortex-phase-repair"
  stale_files: []
  required_refresh: []
```

## Current state summary

- Current Phase: `Personal Workflow App Kernel Exploration`
- Current Phase status: repair required / pending `P0_PHASE_START`
- Proposed repaired Phase: `EXOCORTEX App Foundation`
- Old Active Goal: `Personal Workflow App Kernel Min Proof`
- Old Goal status: invalidated by Phase repair; preserve as superseded provenance.
- Current focus: repair/restart the Phase around the future EXOCORTEX application foundation.
- Proposed first Goal after Phase repair: `EXOCORTEX Product Foundation Definition`
- Next route: `P0_PHASE_START` via Router/new stage run after repository patch and Project Files refresh.
