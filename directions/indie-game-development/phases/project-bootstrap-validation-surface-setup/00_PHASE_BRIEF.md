# Phase Brief — Project Bootstrap and Validation Surface Setup

```yaml
phase_brief: 1
schema: phase_brief.v1
direction_id: indie_game_development
phase_id: project-bootstrap-validation-surface-setup
phase_name: "Project Bootstrap and Validation Surface Setup"
status: closed_complete_by_P9
started_by_stage: P0_PHASE_START
started_at: "2026-05-21"
previous_phase_id: core-coop-technical-foundation-selection
previous_phase_status: closed_complete_by_P9
previous_phase_summary: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md"
map_link: "H1_playable_technical_nucleus / H1_G3_project_bootstrap_tool_binding_validation_scene_readiness -> H1_G4_durable_technical_nucleus"
basis_validity_status: proven
next_route: P0_PHASE_START
implementation_allowed_now: false
codex_product_execution_allowed_now: false
unity_bootstrap_allowed_now: false
product_repository_creation_allowed_now: false
task_master_graph_allowed_now: false
unity_mcp_setup_allowed_now: false
```

## Purpose

Start the next practical Phase after `Core Co-op Technical Foundation Selection` closed complete by P9.

This Phase exists to convert accepted H1_G3 readiness into a bounded project bootstrap / tool-binding / validation-surface setup campaign before H1_G4 durable technical nucleus work is scoped.

## Current Critical Constraint

The Direction cannot safely proceed from accepted readiness into durable technical nucleus work until concrete project setup boundaries, tool-binding route, validation surfaces, stop rules, and allowed execution route are selected and scoped.

## Minimum Outcome

A reviewed/accepted project bootstrap and validation-surface setup envelope that defines:

- concrete setup target;
- allowed and forbidden setup surfaces;
- validation surface requirements;
- stop conditions;
- evidence requirements;
- next safe route toward H1_G4 without starting product implementation prematurely.

## Validation Signal

The next workflow state can route to `E1_EXECUTION_BRIEF`, `U1_USER_GUIDED_EXECUTION`, `X0_EXECUTOR_PROJECT_SETUP`, `X1_EXECUTOR_RUN`, `A1_AUDIT`, `D1_DEEP_RESEARCH`, `S3_DECIDE`, Context Request, Human Decision, Stop, or later H1_G4 scoping without inventing project/tool state.

## Map link

`H1_playable_technical_nucleus / H1_G3_project_bootstrap_tool_binding_validation_scene_readiness -> H1_G4_durable_technical_nucleus`

## Почему это не повтор прошлой фазы

The closed Phase selected and accepted the foundation decision, first technical nucleus specification, Codex/project execution profile, and H1_G3 readiness packet.

This Phase does not reopen those decisions. It turns the accepted readiness state into a bounded setup/validation campaign needed before H1_G4.

## Phase Closure Contract

```yaml
phase_closure_contract:
  closure_criteria:
    - criterion: "Project bootstrap / validation-surface setup envelope accepted or route-gated."
      evidence_required:
        - "G1-shaped Goal Contract accepted by later review or routed to exact blocker."
    - criterion: "Concrete setup target and validation surfaces are explicit enough for E1/U1/X0/X1 or exact Context Request."
      evidence_required:
        - "setup target"
        - "validation surface inventory"
        - "tool-binding assumptions classified"
        - "stop rules"
    - criterion: "No product implementation is launched without later basis-valid execution route."
      evidence_required:
        - "explicit implementation_allowed_now: false until later route"
  phase_work_map:
    required_for_closure:
      - goal_id: bootstrap-validation-surface-setup-envelope
        status: r1_accepted_goal_complete
        evidence: "R1 accepted the setup/validation envelope."
    optional_expansion:
      - candidate_id: H1_G4_durable_technical_nucleus_planning
        status: optional_not_required_for_closure
        reason_optional: "Only after setup/validation envelope is accepted."
      - candidate_id: Unity_MCP_setup
        status: optional_not_required_for_closure
        reason_optional: "Only if later route proves concrete benefit and safety."
      - candidate_id: Task_Master_graph_creation
        status: optional_not_required_for_closure
        reason_optional: "Only if later X0/E1 route requires it."
  first_phase_closing_candidate_if_known: bootstrap-validation-surface-setup-envelope
  after_goal_gate_policy:
    phase_progress_gate_after_R1: required
    R1_must_not_route_directly_to_G0_only_because_active_goal_is_none: true
    G0_allowed_only_after_phase_continue_decision: true
    P9_required_when_completed_goal_may_satisfy_phase_minimum_outcome: true
    Context_Request_required_when_phase_closure_contract_is_missing: true
```

## 2026-05-22 R1 acceptance note

```yaml
r1_acceptance_note:
  accepted_goal: bootstrap-validation-surface-setup-envelope
  accepted_result: setup/validation envelope
  phase_progress_gate_status: phase_close_candidate
  next_route: P9_PHASE_CLOSE
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## 2026-05-22 P9 close

```yaml
p9_phase_close:
  close_status: closed_complete_by_P9
  closed_phase: project-bootstrap-validation-surface-setup
  closed_goal: bootstrap-validation-surface-setup-envelope
  closure_verdict: close_complete
  closed_at: "2026-05-22"
  basis:
    - "R1 accepted bootstrap-validation-surface-setup-envelope as completed_verified / accepted_complete."
    - "The Phase minimum outcome is satisfied by the accepted setup/validation envelope."
    - "Remaining implementation/setup items are later lifecycle work, not required for this Phase closure."
  next_route: P0_PHASE_START
  next_route_condition: "after repository maintenance and manual Project Files refresh"
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  product_repository_creation_allowed_now: false
  product_code_allowed_now: false
  task_master_graph_allowed_now: false
  unity_mcp_setup_allowed_now: false
  old_code_transfer_allowed_now: false
  game_documentation_promotion_allowed_now: false
```

## First Goal Candidate

```yaml
first_goal_candidate:
  candidate_id: bootstrap-validation-surface-setup-envelope
  name: "Сформировать setup/validation envelope для project bootstrap перед H1_G4"
  recommended_next_stage: G1_GOAL_SHAPE
  smallest_useful_result: >
    A Goal Contract with setup target, validation surfaces, allowed/forbidden
    surfaces, stop rules, evidence requirements, and next route.
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## In Scope

- Phase frame for project bootstrap / validation surface setup.
- First Goal seed for setup/validation envelope.
- Validation surfaces and evidence route selection.
- Concrete stop rules for missing project/tool-binding state.
- Later route preparation for E1/U1/X0/X1 if basis-valid.

## Out of Scope

- Product implementation.
- Unity gameplay code.
- Direct Unity bootstrap from P0.
- Product repository mutation from P0.
- Codex product/project execution from P0.
- Task Master graph creation from P0.
- Unity MCP setup from P0.
- Old-code transfer.
- Game Documentation promotion.
- Broad engineering handbook.
- Commercialization plan.

## End-of-file marker

END_OF_FILE: directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/00_PHASE_BRIEF.md
