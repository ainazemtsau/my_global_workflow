# H1_G4 Durable Technical Nucleus — First Runnable Build

```yaml
artifact_control:
  artifact_name: "H1_G4 Durable Technical Nucleus — First Runnable Build Phase Brief"
  schema: phase_brief.v1
  owner_layer: persistence
  status: active
  repo_path: "directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/00_PHASE_BRIEF.md"
  created_by_stage: P0_PHASE_START
  created_at: "2026-05-22"

phase:
  id: h1-g4-durable-technical-nucleus-first-runnable-build
  name: "H1_G4 Durable Technical Nucleus — First Runnable Build"
  status: active_pending_G1_goal_shape
  direction_id: indie_game_development
  map_link: "H1_playable_technical_nucleus / P0_PHASE_START_after_project_bootstrap_validation_surface_setup_close -> H1_G4_durable_technical_nucleus"
  previous_closed_phase: project-bootstrap-validation-surface-setup
  previous_closed_phase_summary: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md"
  selected_first_goal_candidate: h1-g4-first-runnable-technical-nucleus-slice
  next_route: G1_GOAL_SHAPE
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Purpose

Phase ID: h1-g4-durable-technical-nucleus-first-runnable-build

Move from accepted setup/readiness/envelope work into the first real H1_G4 build campaign.

This Phase is not another setup-validation microphase. The accepted setup/validation envelope is an input. The Phase target is the first runnable durable technical nucleus slice, or an evidence-based blocker/unblock route if producing that slice is not yet safe.

## Current Critical Constraint

Accepted readiness/envelope state exists, but the Direction has no first runnable durable technical nucleus slice and no reviewed execution Goal that can produce or route-gate it.

## Minimum Outcome

Accepted or route-gated first runnable H1_G4 durable technical nucleus slice in the target project/workspace, with:

- concrete setup/tool-binding state;
- allowed and forbidden surfaces;
- validation evidence;
- stop conditions;
- exact blocker/unblock route if the runnable slice cannot be produced safely.

## Validation Signal

Later R1 can review concrete runnable/evidence output or exact blocker evidence:

- validation scene, harness, automated test, or manual checklist result;
- setup/tool-binding proof;
- changed artifact pointers;
- route decision for continuation, blocker, or Phase close.

## Map Link

`H1_playable_technical_nucleus / P0_PHASE_START_after_project_bootstrap_validation_surface_setup_close -> H1_G4_durable_technical_nucleus`

## Почему это не повтор прошлой фазы

Прошлая фаза закрыла accepted setup/validation envelope. Эта фаза не пересобирает envelope; она использует его как вход и двигает Direction к первому runnable H1_G4 technical nucleus slice, либо к evidence-based blocker с точным unblock route.

## Basis-validity

```yaml
basis_validity_status: proven_compact
next_action_proof_status: proven_compact
solution_shape_status: proven_compact
reason: >
  H1_G4 remains premature until selected/scoped by P0/G1/E1 or a later route.
  This Phase performs that selection at the phase level without executing implementation inside P0.
```

## Phase Closure Contract

```yaml
phase_closure_contract:
  closure_criteria:
    - criterion: "First runnable H1_G4 durable technical nucleus slice is accepted by R1."
      evidence_required:
        - "Runnable scene/harness/test/manual checklist evidence."
        - "Setup/tool-binding evidence."
        - "Allowed/forbidden surfaces respected."
        - "Stop conditions and validation result recorded."
    - criterion: "Or the first runnable slice is route-gated by concrete blocker evidence."
      evidence_required:
        - "Exact blocker."
        - "Why execution cannot proceed safely."
        - "Smallest unblock route."
        - "Recommended next stage."
  phase_work_map:
    required_for_closure:
      - goal_id: h1-g4-first-runnable-technical-nucleus-slice
        name: "Produce or route-gate the first runnable H1_G4 durable technical nucleus slice"
        status: selected_for_G1_goal_shape
        evidence: "Pending G1/E1/later execution evidence."
    optional_expansion:
      - candidate_id: unity_mcp_setup
        status: optional_not_required_for_closure
        reason_optional: "Only needed if later execution proves it is required."
      - candidate_id: task_master_graph_creation
        status: optional_not_required_for_closure
        reason_optional: "Only allowed after later route explicitly authorizes it."
      - candidate_id: old_code_transfer_or_audit
        status: optional_not_required_for_closure
        reason_optional: "Old material remains reference/evidence only until targeted question exists."
      - candidate_id: game_documentation_promotion
        status: optional_not_required_for_closure
        reason_optional: "Promotion requires explicit later documentation-maintenance route."
      - candidate_id: commercialization_visibility
        status: optional_not_required_for_closure
        reason_optional: "Parked until credible playable/showable proof exists."
  first_phase_closing_candidate_if_known: h1-g4-first-runnable-technical-nucleus-slice
  after_goal_gate_policy:
    phase_progress_gate_after_R1: required
    R1_must_not_route_directly_to_G0_only_because_active_goal_is_none: true
    G0_allowed_only_after_phase_continue_decision: true
    P9_required_when_completed_goal_may_satisfy_phase_minimum_outcome: true
    Context_Request_required_when_phase_closure_contract_missing: true
```

## First Goal Candidate

```yaml
first_goal_candidate:
  candidate_id: h1-g4-first-runnable-technical-nucleus-slice
  name: "Produce or route-gate the first runnable H1_G4 durable technical nucleus slice"
  recommended_next_stage: G1_GOAL_SHAPE
  leverage_rationale: >
    Converts accepted foundation/readiness/envelope work into a real project artifact
    or a concrete execution blocker.
  smallest_useful_result: >
    A shaped Goal Contract whose accepted outcome is either a first runnable nucleus
    slice with validation evidence or a concrete blocker/unblock packet.
  confidence: medium_high
```

## Scope

In scope:

- first H1_G4 runnable nucleus Goal shaping;
- setup/tool-binding state as an entry gate inside the Goal;
- minimal executable slice definition;
- validation scene/harness/test/manual checklist requirements;
- stop rules and blocker evidence.

Out of scope:

- broad roadmap;
- repeat setup/validation envelope;
- full vertical slice;
- commercialization planning;
- Game Documentation promotion;
- old-code transfer as starting point;
- product/project execution inside P0.

## Guardrails

Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked until a later basis-valid route authorizes them.

## Next Route

`G1_GOAL_SHAPE — shape h1-g4-first-runnable-technical-nucleus-slice`

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/00_PHASE_BRIEF.md`
