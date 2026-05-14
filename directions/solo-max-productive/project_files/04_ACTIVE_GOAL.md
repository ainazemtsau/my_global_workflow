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
  last_refresh_at: "2026-05-14"
  refresh_source: "P0-2026-05-14-exocortex-app-foundation-repair"

active_goal:
  state: none_pending_G1
  goal_id: null
  goal_name: null
  goal_path: null
  phase_name: EXOCORTEX App Foundation
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_wave: none
  next_route: G1_GOAL_SHAPE
  route_note: "Launch G1 after repository patch apply/read-back and Project Files cache refresh."

superseded_goal:
  goal_id: personal-workflow-app-kernel-min-proof
  goal_name: Personal Workflow App Kernel Min Proof
  goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  status: superseded_provenance_not_executable
  superseded_reason: "The old Goal and prior replacement candidate are misframed after user clarification. The target is the future EXOCORTEX application / personal external brain, not a temporary or merely convenient replacement for the current workflow."
  reactivation_rule: "Only continue if the user explicitly reactivates the weaker current-workflow replacement framing through a later Human Decision."

selected_goal_candidate:
  id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  name: EXOCORTEX Product Foundation Definition
  status: approved_for_G1_GOAL_SHAPE
  expected_route_after_p0: G1_GOAL_SHAPE
  expected_intent: "Define the product/application foundation for EXOCORTEX: target system, principles, core loop, subsystem map, buildable foundation, non-goals, and validation criteria."
  required_for_phase_closure: true

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

There is no active Goal after P0 Phase repair.

The old active Goal is preserved as superseded/replaced provenance.

It must not proceed to `E1_EXECUTION_BRIEF`, and `03_KERNEL_MIN_PROOF_BRIEF.md` must not be created.

The next valid material step is `G1_GOAL_SHAPE` for `EXOCORTEX Product Foundation Definition`.

Core principle preserved: future LLMs are upgradable cognitive engines; EXOCORTEX is the persistent substrate of context, memory, tools, surfaces, feedback loops, rules, and Reality Alignment mechanisms.
