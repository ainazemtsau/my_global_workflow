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
  last_refresh_at: "2026-05-19"
  refresh_source: "G1-2026-05-19-exocortex-core-foundation-definition"

active_goal:
  state: goal_shaped_pending_E1
  goal_id: exocortex-core-foundation-definition
  goal_name: EXOCORTEX Core Foundation Definition
  goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition"
  phase_name: EXOCORTEX App Foundation
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  current_wave: none
  next_route: E1_EXECUTION_BRIEF
  route_note: "Run E1 after G1 repository patch apply/read-back and manual Project Files cache refresh. E1 prepares minimum HOW for producing the Core Foundation Definition artifact."

goal_contract:
  source_candidate_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  source_candidate_name: EXOCORTEX Product Foundation Definition
  clarified_name: EXOCORTEX Core Foundation Definition
  what: "Define EXOCORTEX Core Foundation: the expandable product-level core of the persistent personal AI brain."
  done: "A coherent Core Foundation Definition exists and is ready for R1 review after execution."
  acceptance_floor: "Definition covers memory/context persistence, model interoperability, tools/actions extensibility, interaction/process loops, workspace surfaces, learning from outcomes, Reality Alignment, first buildable foundation boundary, non-goals, and validation criteria."
  validation_signal: "Reviewer can distinguish core, extension/future surface, first buildable foundation, Max Vision, and not-now."
  implementation_allowed_now: false

superseded_goal:
  goal_id: personal-workflow-app-kernel-min-proof
  goal_name: Personal Workflow App Kernel Min Proof
  goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  status: superseded_provenance_not_executable
  superseded_reason: "The old Goal is preserved as superseded provenance after the EXOCORTEX Core Foundation migration. It is not the current execution target."
  reactivation_rule: "Only continue if the user explicitly reactivates that legacy Goal through a later Human Decision."

selected_goal_candidate:
  id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
  name: EXOCORTEX Product Foundation Definition
  status: shaped_as_active_goal_pending_E1
  expected_route_after_g1: E1_EXECUTION_BRIEF
  expected_intent: "Define EXOCORTEX Core Foundation: core substrate, memory/context persistence, model interoperability, tools/actions extensibility, interaction/process loops, workspace surfaces, learning from outcomes, Reality Alignment, first buildable boundary, non-goals, and validation criteria."
  required_for_phase_closure: true

stale_previous_candidate:
  name: Personal Workflow System Core and MVP Definition
  status: superseded_by_exocortex_phase_repair
  reactivation_rule: "Only continue if the user explicitly reactivates this legacy candidate."

stale_previous_candidate_2:
  name: Create Lightweight Codex Small-Fix Lane
  status: superseded_not_current
  reactivation_rule: "Only continue if the user explicitly reactivates it."
```

## Active Goal summary

The active Goal is now `EXOCORTEX Core Foundation Definition`.

Lifecycle state: `goal_shaped_pending_E1`.

The old active Goal is preserved as superseded/replaced provenance.

It must not proceed to `E1_EXECUTION_BRIEF`, and `03_KERNEL_MIN_PROOF_BRIEF.md` must not be created.

The next valid material step is `E1_EXECUTION_BRIEF` for `exocortex-core-foundation-definition`.

Core principle preserved: future LLMs are upgradable cognitive engines; EXOCORTEX is the persistent substrate of context, memory, tools, surfaces, feedback loops, rules, and Reality Alignment mechanisms.
