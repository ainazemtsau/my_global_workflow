# 04_ACTIVE_GOAL.md

```yaml
artifact_control:
  artifact_name: "04 Active Goal"
  schema: active_goal.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/04_ACTIVE_GOAL.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-13"
  refresh_source: "G1-2026-05-13-exocortex-phase-repair"

active_goal:
  state: invalidated_by_phase_repair_pending_p0
  goal_id: personal-workflow-app-kernel-min-proof
  goal_name: Personal Workflow App Kernel Min Proof
  goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_wave: none
  next_route: P0_PHASE_START
  route_note: "Launch via Router/new P0 run; G1 stopped and does not directly execute P0."
  invalidation_reason: "The old Goal and prior replacement candidate are misframed after user clarification. The target is the future EXOCORTEX application / personal external brain, not a temporary or merely convenient replacement for the current workflow."

phase_repair_candidate:
  id: P0-CAND-2026-05-13-EXOCORTEX-APP-FOUNDATION
  name: EXOCORTEX App Foundation
  status: approved_for_p0_phase_repair
  expected_route: P0_PHASE_START
  expected_intent: "Repair or restart the Phase around building the foundation of the future EXOCORTEX application while the current workflow remains the construction workflow."

proposed_first_goal_after_phase_repair:
  id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  name: EXOCORTEX Product Foundation Definition
  status: pending_after_phase_repair
  expected_route_after_p0: G1_GOAL_SHAPE
  expected_intent: "Define the product/application foundation for EXOCORTEX: target system, principles, core loop, subsystem map, buildable foundation, non-goals, and validation criteria."

stale_previous_candidate:
  name: Personal Workflow System Core and MVP Definition
  status: superseded_by_exocortex_phase_repair
  reactivation_rule: "Only continue if the user explicitly reactivates the weaker current-workflow replacement framing."

stale_previous_candidate_2:
  name: Create Lightweight Codex Small-Fix Lane
  status: superseded_not_current
  reactivation_rule: "Only continue if the user explicitly reactivates it."
```

## Active Goal summary

The old active Goal is preserved as superseded/replaced provenance.

It must not proceed to `E1_EXECUTION_BRIEF`, and `03_KERNEL_MIN_PROOF_BRIEF.md` must not be created.

The next valid material step is `P0_PHASE_START` via Router/new stage run, because the Phase itself requires repair.

Core principle preserved: future LLMs are upgradable cognitive engines; EXOCORTEX is the persistent substrate of context, memory, tools, surfaces, feedback loops, rules, and Reality Alignment mechanisms.
