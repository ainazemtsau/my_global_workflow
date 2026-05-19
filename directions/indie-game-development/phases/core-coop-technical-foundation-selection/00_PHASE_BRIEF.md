# Phase Brief — Core Co-op Technical Foundation Selection

```yaml
artifact_control:
  artifact_name: "Phase Brief — Core Co-op Technical Foundation Selection"
  schema: phase_brief.v1
  owner_layer: persistence
  status: active_H1_G2_goal_shaped_pending_A1_audit
  phase_status: active_H1_G2_goal_shaped_pending_A1_audit
  active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  active_goal_status: goal_shaped_pending_A1_audit
  status_after_r1_first_technical_nucleus_spec: active_pending_m0_after_r1_acceptance
  status_after_m0_objective_architecture_migration: active_pending_g1_H1_G2_goal_shape
  status_after_g1_H1_G2_formalization: active_H1_G2_goal_shaped_pending_A1_audit
  last_completed_goal:
    goal_id: first-technical-nucleus-functional-spec
    result: r1_completed_verified_specification_accepted
    accepted_scope: functional_technical_specification_only
  current_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  phase_progress_gate_status: completed_by_R1_then_m0_frontier_review_completed
  phase_closed: false
  p9_allowed_now: false
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md"
  created_by_stage: P0_PHASE_START
  created_at: "2026-05-13"
```

## Phase identity

- Phase ID: `core-coop-technical-foundation-selection`
- Phase name: `Core Co-op Technical Foundation Selection`
- Direction: `Indie Game Development`
- Status: `active_H1_G2_goal_shaped_pending_A1_audit`
- Started by: `P0_PHASE_START`
- Started at: `2026-05-13`

## Why this Phase exists

This is a new project. The old project is evidence/source material, not an automatic production base.

The current blocker is not the playable proof slice brief. The current blocker is the high-lock-in technical foundation: co-op multiplayer technology and architecture, Grid/Topology foundation, and Gas Simulation foundation.

FishNet was used in the old project, but it is not final for the new project. The new project may use FishNet, Unity's multiplayer stack, or another option if evidence supports it.

## Current Critical Constraint

The Direction cannot safely proceed to playable proof work or implementation until the core co-op technical foundation is selected. Multiplayer architecture, Grid/Topology, and Gas Simulation are expensive to replace later and must be chosen as durable foundation, not as disposable prototype scaffolding.

## Minimum Outcome

Accepted `Core Technical Foundation Decision Brief` that defines:

1. multiplayer technology and host-player co-op architecture candidate/decision;
2. Grid/Topology transfer boundary from the old project;
3. Gas Simulation architecture and durable gameplay logic model;
4. smallest durable technical nucleus to build next;
5. what old project material is evidence, reusable, incomplete, unsafe, or request-only;
6. what remains unresolved and which stage should resolve it.

## Validation Signal

R1 can accept the Phase result when there is a reviewable technical foundation decision that lets the next stage proceed without guessing:

- multiplayer stack/architecture is selected or narrowed to an explicit decision gate;
- FishNet is treated as a candidate with evidence, not as default inertia;
- Grid/Topology transfer boundary is clear;
- Gas Simulation logic is specified as durable/extensible from the first real implementation;
- throwaway/hardcoded gas proof is explicitly rejected;
- the next execution route has exact context and validation needs.

## User constraints carried into this Phase

- Solo-dev project.
- New Unity project is not yet created.
- Old project cannot be transferred wholesale.
- Old project can be used as evidence/source material.
- Old Grid/Topology work may be substantially reusable and may include tests.
- Old Gas Simulation existed but was incomplete/not fully tested and has performance/architecture questions.
- Old FishNet use is evidence only; multiplayer technology is open.
- Multiplayer target is host-player/listen-host co-op, not dedicated server by default.
- Multiplayer technology and architecture are part of foundation because this is a co-op game.
- Gas Simulation gameplay logic must not be hardcoded/disposable.
- Visual gas can be simpler than gameplay gas.
- Preferred grid resolution was around 25 cm with possible 50 cm fallback, but this is not final.
- Exact technical facts must come from old docs/code and current research, not memory.

## In scope

- Technology/architecture selection for multiplayer foundation.
- Read-only audit of old Grid/Topology/Gas/FishNet material as a future Goal.
- Current external/current technology research as needed.
- Durable foundation transfer boundary.
- Smallest durable nucleus definition.
- Stage routing for unresolved decisions/research/audit.

## Out of scope

- Creating a Unity project.
- Product/project execution.
- Code transfer.
- Full implementation.
- Full gas taxonomy/reaction table.
- Final performance profiling.
- Visual gas proof beyond acknowledging simplification.
- Dedicated server design unless research proves it necessary.
- Game Documentation promotion.
- Closing the previous Phase as successful.

## Phase Closure Contract

```yaml
phase_closure_contract:
  closure_criteria:
    - criterion: "Accepted Core Technical Foundation Decision Brief exists."
      evidence_required: "R1 accepts the Goal result or routes exact unresolved blocker."
    - criterion: "Multiplayer technology and host-player architecture are selected or narrowed to a named S3/D1 decision."
      evidence_required: "Decision brief includes options, tradeoffs, and chosen/default route."
    - criterion: "Grid/Topology transfer boundary from old project is clear."
      evidence_required: "Decision brief identifies reusable modules/tests/evidence and unsafe assumptions."
    - criterion: "Gas Simulation architecture is durable/extensible and not hardcoded/disposable."
      evidence_required: "Decision brief defines the smallest real logic model and explicitly rejects throwaway simulation."
    - criterion: "Smallest durable technical nucleus to build next is identified."
      evidence_required: "Decision brief names next nucleus, validation signal, and execution prerequisites."
    - criterion: "After R1, phase_progress_gate runs before selecting any further Goal."
      evidence_required: "R1 or follow-up route checks whether Phase can close, continue, or needs S3/D1/A1."
  required_goal_map:
    - goal_candidate_id: core-technical-foundation-decision-brief
      name: "Сформировать Core Technical Foundation Decision Brief"
      required_for_closure: true
      status: first_goal_candidate_pending_G1
      recommended_next_stage: G1_GOAL_SHAPE
    - goal_id: first-technical-nucleus-functional-spec
      title: "Сформировать функционально-техническую спецификацию первого technical nucleus"
      required_for_closure: true
      status: r1_completed_verified_specification_accepted
      review_stage: R1_GOAL_REVIEW_DISTILL
      accepted_scope: "Functional/technical specification accepted; implementation remains blocked."
      purpose: >
        Define first technical nucleus capabilities across gas, spatial/level needs,
        Grid/topology substrate, cross-system interaction, destructibility compatibility,
        and validation/demo scenarios.
    - goal_id: grid-gas-transfer-boundary-audit
      status: superseded_after_human_clarification
      required_for_closure: false
      treatment: "reference/evidence only"
  optional_expansion_candidates:
    - candidate_id: unity-project-bootstrap
      status: optional_not_required_for_closure
      reason_optional: "Can only proceed after foundation decision and execution route."
    - candidate_id: durable-technical-nucleus-implementation
      status: optional_not_required_for_closure
      reason_optional: "Likely next Phase or later Goal after decision."
    - candidate_id: visual-gas-proof
      status: optional_not_required_for_closure
      reason_optional: "Visual gas can be simplified and is not the foundation blocker."
    - candidate_id: performance-profiling-pass
      status: optional_not_required_for_closure
      reason_optional: "Requires concrete implementation or candidate nucleus."
    - candidate_id: game-documentation-promotion
      status: optional_not_required_for_closure
      reason_optional: "Requires explicit documentation maintenance route."
  first_phase_closing_candidate_if_known:
    stage: P9_PHASE_CLOSE
    trigger: "Only after required Goal is accepted by R1 and phase_progress_gate selects closure."
  after_goal_gate_policy:
    phase_progress_gate_after_R1: required
    R1_must_not_route_directly_to_G0_only_because_active_goal_is_none: true
    G0_allowed_only_after_phase_continue_decision: true
    P9_required_when_completed_goal_may_satisfy_phase_minimum_outcome: true
    Context_Request_required_when_phase_closure_contract_is_missing: true
```

## First Goal candidate

```yaml
candidate:
  id: core-technical-foundation-decision-brief
  name: "Сформировать Core Technical Foundation Decision Brief"
  recommended_next_stage: G1_GOAL_SHAPE
  smallest_useful_result: "Accepted Goal Contract for producing a technical foundation decision brief."
  required_decision_surface:
    - "multiplayer stack and host-player architecture"
    - "Grid/Topology transfer boundary"
    - "Gas Simulation durable logic architecture"
    - "old project evidence/reuse/unsafe assumptions"
    - "smallest durable technical nucleus"
  route_expectation:
    - "G1 shapes the Goal."
    - "If current external technology evidence is needed, route to D1_DEEP_RESEARCH."
    - "If human-owned tradeoff remains, route to S3_DECIDE."
    - "If old material needs challenge, route to A1_AUDIT or read-only Codex audit through the correct execution route."
```

## Why this is not a repeat of the previous closed Phase

`Expedition First Proof Checkpoint` established proof identity and rejected gas-only proof. This Phase does not re-decide Expedition proof identity. It addresses a different blocker: high-lock-in technical foundation selection for a new co-op project.

## Previous Phase / Goal handling

- Previous Phase: `Expedition First Playable Proof Slice`
- Handling: `paused_superseded_not_closed`
- Previous Goal: `first-playable-proof-slice-brief`
- Handling: `paused_superseded_partial_progress_not_accepted`
- F0 artifact: preserved as scaffold/evidence, not accepted completion.
- P9: not launched.

## Next route

Run `A1_AUDIT` for `H1_G2_codex_development_operating_model_and_architecture_protocols` after G1 H1_G2 formalization repository maintenance apply/read-back and manual Project Files refresh.

A1 must audit/fit-check the existing workflow Codex/project setup and execution-readiness procedure on first real use.

A1 must not create a second Indie-only workflow layer. It must decide whether the existing workflow is sufficient, needs a minimal project-specific input/profile, needs Workflow Governance repair, or requires exact missing context.

Do not proceed to P9, E1, project bootstrap, durable technical nucleus implementation, Codex product/project execution, old-code audit or transfer, Task Master graph creation, real internal tool setup, or Game Documentation promotion until a later basis-valid lifecycle route authorizes that work.

## 2026-05-15 P0 map-alignment repair

P0 kept this Phase active after M0 initialized `08_DIRECTION_MAP.md`.

### Map binding

- Active Horizon: `H1_playable_technical_nucleus`
- Current Gate: `H1_G1_core_technical_foundation_decision_brief`
- Required inside current gate or next gate before implementation: `H1_G2_codex_development_operating_model_and_architecture_protocols`

### Updated Critical Constraint

The Direction cannot safely move toward the playable technical nucleus while foundation choices and Codex-development architecture protocols are not reconciled into an accepted, reviewable foundation decision.

### Updated Minimum Outcome

Accepted or review-routed `Core Technical Foundation Decision Brief / Decision Map` that either satisfies the current Phase closure criteria or names exact A1/D1/S3/E1 gates.

### Updated Validation Signal

The next workflow state can choose R1 review, A1 audit, D1 research, S3 decision, or E1 execution planning without guessing and without premature implementation.

### Existing artifact treatment

Existing artifact:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

Treatment:

- review candidate / evidence artifact;
- not stale by default;
- not accepted by P0;
- not duplicated blindly;
- must be reconciled by `G1_GOAL_SHAPE` repair/update.

### Next route after P0

Run `G1_GOAL_SHAPE` in repair/update mode.

Do not route directly from P0 to `E1_EXECUTION_BRIEF` or `R1_GOAL_REVIEW_DISTILL`.

Do not run Unity project creation, code transfer, technical audit, external research synthesis, Codex product/project execution, Task Master graph creation, Game Documentation promotion, or implementation inside P0.

## 2026-05-16 G1 repair/update formalization

G1 kept this Phase active and classified the existing Core Technical Foundation Decision Brief / Decision Map as a review-ready candidate, not an accepted result.

Updated active Goal status:

```yaml
active_goal_status_after_g1:
  goal_id: core-technical-foundation-decision-brief
  status: review_ready_candidate_pending_B1_route_repair_not_R1_accepted
  existing_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  artifact_classification: review_ready_candidate
```

Next route after G1:

`B1_PROBLEM`

Reason:

Direct `G1_GOAL_SHAPE` -> `R1_GOAL_REVIEW_DISTILL` is not registry-valid. B1 is selected narrowly for route-integrity recovery and review handoff repair.

G1 did not authorize Unity project creation, code transfer, technical audit execution, external research synthesis, Codex product/project execution, Task Master graph creation, Game Documentation promotion, or implementation.

## 2026-05-16 R1 stabilization / Phase Progress Gate

R1 accepted the existing `Core Technical Foundation Decision Brief / Decision Map` as an accepted route-gated decision map.

Accepted within this Goal:
- FishNet + Steamworks / Steam Networking / Steam Datagram Relay as multiplayer default;
- Photon Fusion 2 as fallback / paid acceleration path;
- player-hosted / listen-host co-op architecture;
- Project Engineering & Codex Development Operating Model at decision-map level;
- Grid/Gas/GridV2/GasV2R transfer surfaces explicitly routed to A1 audit rather than silently approved.

Phase Progress Gate result:

```yaml
phase_progress_gate:
  result: continue_with_required_goal
  p9_allowed_now: false
  required_next_goal_candidate:
    id: grid-gas-transfer-boundary-audit
    title: "Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction"
    recommended_next_stage: G1_GOAL_SHAPE
    expected_route_after_G1: A1_AUDIT
  implementation_allowed_now: false
```

This R1 result does not authorize Unity project creation, code transfer, Codex product/project execution, Task Master graph creation, Game Documentation promotion, or implementation planning.

## 2026-05-16 G1 reset — first technical nucleus functional specification

G1 superseded `grid-gas-transfer-boundary-audit` after human clarification.

New active Goal:

`first-technical-nucleus-functional-spec`

The Phase remains valid. The active foundation-selection question is now requirements-first:
define the first technical nucleus capability/specification before implementation or old project reference review.

Required route:

Historical route at G1 reset time: `E1_EXECUTION_BRIEF`.

Current route after F0 synthesis formalization and evidence repair: `R1_GOAL_REVIEW_DISTILL`.

Current route after R1 acceptance: `M0_DIRECTION_MAP`.

R1 Phase Progress Gate after `first-technical-nucleus-functional-spec`: the Goal is accepted and may satisfy a closure-relevant Phase surface, but M0 review is required before P9, G0, E1, or implementation route selection.

Required internal gate:

User approval after `gas_simulation_capability_frame` before Grid/topology work proceeds.

Blocked:

- implementation;
- Unity bootstrap;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph;
- Game Documentation promotion.

## 2026-05-19 G1 H1_G2 formalization

G1 formalized `H1_G2_codex_development_operating_model_and_architecture_protocols` as the active Goal.

Goal contract:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`

Current state:

```yaml
active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
active_goal_status: goal_shaped_pending_A1_audit
next_route: A1_AUDIT
next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
implementation_allowed_now: false
codex_product_execution_allowed_now: false
unity_bootstrap_allowed_now: false
task_master_graph_allowed_now: false
```

Key correction:

- This Goal must audit/fit-check the existing workflow Codex/project setup and execution-readiness procedure on first real use.
- It must not create a second Indie-only workflow layer.
- A1 must decide whether the existing workflow is sufficient, needs a minimal project-specific input/profile, needs Workflow Governance repair, or requires exact missing context.

Still not authorized:

- Unity bootstrap;
- implementation;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- Game Documentation promotion.
