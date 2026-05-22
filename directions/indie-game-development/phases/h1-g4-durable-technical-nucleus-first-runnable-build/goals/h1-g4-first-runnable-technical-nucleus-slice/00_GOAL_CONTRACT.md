# Goal Contract — H1_G4 First Runnable Technical Nucleus Slice

```yaml
artifact_control:
  artifact_name: "Goal Contract — H1_G4 First Runnable Technical Nucleus Slice"
  schema: goal_contract.v1
  owner_layer: persistence
  status: goal_shaped_pending_E1_execution_brief
  repo_path: "directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/00_GOAL_CONTRACT.md"
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-22"

goal:
  id: h1-g4-first-runnable-technical-nucleus-slice
  title: "Produce or route-gate the first runnable H1_G4 durable technical nucleus slice"
  status: goal_shaped_pending_E1_execution_brief
  phase_id: h1-g4-durable-technical-nucleus-first-runnable-build
  phase_name: "H1_G4 Durable Technical Nucleus — First Runnable Build"
  phase_path: "directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build"
  shaped_by_stage: G1_GOAL_SHAPE
  next_route: E1_EXECUTION_BRIEF
  next_route_mode: prepare_h1_g4_first_runnable_technical_nucleus_slice_execution_brief
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  unity_bootstrap_allowed_now: false
  product_repository_creation_allowed_now: false
  product_code_allowed_now: false
  task_master_graph_allowed_now: false
  real_internal_tool_setup_allowed_now: false
  unity_mcp_setup_allowed_now: false
  old_code_transfer_allowed_now: false
  game_documentation_promotion_allowed_now: false
```

## WHAT

Shape and later produce the smallest first runnable H1_G4 durable technical nucleus slice, or produce a concrete blocker/unblock packet if that runnable slice cannot be safely produced.

This Goal is not a new setup/readiness/envelope repeat. The accepted setup/validation envelope is input evidence. The new output must move toward a runnable H1_G4 technical nucleus slice or exact blocker evidence.

## WHY now

The previous Phase closed the setup/validation envelope. The current Phase exists to move from accepted readiness/envelope state into the first real H1_G4 build campaign.

The current critical constraint is that accepted readiness/envelope state exists, but the Direction has no first runnable durable technical nucleus slice and no reviewed execution Goal that can produce or route-gate it.

## DONE

The Goal can be accepted later only if one of these outcomes exists:

1. A first runnable H1_G4 durable technical nucleus slice exists in the target project/workspace with:
   - setup/tool-binding state evidenced;
   - allowed and forbidden surfaces respected;
   - validation evidence from a scene, harness, automated test, debug evidence, or manual checklist;
   - changed artifact pointers or execution evidence;
   - stop conditions recorded.

2. A blocker/unblock packet exists with:
   - exact blocker;
   - why execution cannot proceed safely;
   - smallest unblock route;
   - recommended next registry-valid stage.

## Minimum complete outcome

One complete usable loop:

- either a runnable validated nucleus slice;
- or a concrete blocker/unblock packet that prevents unsafe guessing.

The Goal must not be cut below this outcome.

## Acceptance floor

E1 must be able to prepare a real execution brief from this Goal Contract without inventing:

- target project/workspace state;
- allowed execution surfaces;
- validation surface;
- evidence requirements;
- stop conditions;
- blocker route;
- forbidden surfaces.

## Validation signal

Concrete runnable/evidence output or exact blocker evidence.

Valid evidence classes include:

- Unity-visible validation scene;
- harness;
- automated test;
- debug evidence;
- manual checklist;
- setup/tool-binding proof;
- changed artifact pointers;
- exact blocker/unblock route.

## Validation method

E1 must choose the minimum validation method required for this first runnable slice.

Acceptable validation surfaces:

- unit/domain tests for pure logic;
- integration tests for linked systems;
- Unity-visible validation scene;
- debug view, inspector, overlay, or state dump;
- network harness only if co-op/network behavior is required for the acceptance floor;
- manual checklist where automation is not yet sensible.

## Smallest testable slice

A single bounded runnable validation surface in the target workspace that exercises the first durable nucleus loop and produces observable state.

The slice should prove one practical nucleus interaction, not a full vertical slice.

Co-op/network behavior, old-code reuse, Unity MCP, Task Master, and broad tool setup are included only if E1 proves they are necessary for the acceptance floor. Otherwise they remain blocked, parked, or route-gated.

## Scope in

- first H1_G4 runnable nucleus Goal shaping;
- setup/tool-binding state as an entry gate inside the Goal;
- minimal executable slice definition;
- validation scene/harness/test/manual checklist requirements;
- stop rules;
- blocker evidence;
- E1 route for execution-brief planning.

## Non-goals

- implementation inside G1;
- Unity bootstrap inside G1;
- product repository creation inside G1;
- product code;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- Unity MCP setup;
- old-code transfer;
- old-code audit as starting point;
- Game Documentation promotion;
- broad foundation planning;
- broad backlog;
- full vertical slice;
- commercialization/visibility work;
- repeating the setup/validation envelope.

## Scope cuts / deferred candidates

Deferred until later basis-valid route:

- full Gas/Grid architecture implementation;
- final multiplayer stack validation;
- full co-op runtime proof;
- final DI/package choice;
- multi-scene validation suite;
- performance/profiling;
- old project code reuse audit;
- documentation promotion;
- commercial demo identity.

## Constraints

- No product/project execution before E1/X0/X1 readiness.
- No code without an explicit validation surface.
- Old Grid/Gas material is reference/evidence only until requirements are clear.
- Target/workspace/tool-binding state must be explicit before execution.
- E1 must not plan HOW beyond this Goal's acceptance floor.
- Repository maintenance is allowed only for approved workflow/Direction file updates and read-back.

## Escalation triggers

- Missing target workspace/tool-binding proof -> E1, U1, X0, Context Request, or blocker route.
- Current tooling uncertainty blocks planning -> D1_DEEP_RESEARCH.
- Source-of-truth conflict blocks planning -> A1_AUDIT or Context Request.
- Human-owned tradeoff about the first runnable slice -> S3_DECIDE or Human Decision.
- Direct implementation request inside G1 -> Stop.

## Map binding

```yaml
map_binding:
  initiative_id: innovative-commercial-expedition-gas-sim-game
  active_horizon: H1_playable_technical_nucleus
  node_or_edge: >
    H1_playable_technical_nucleus /
    P0_PHASE_START_after_project_bootstrap_validation_surface_setup_close
    -> H1_G4_durable_technical_nucleus
  expected_map_delta: >
    If accepted later, H1_G4 moves from selected/scoped toward runnable
    technical nucleus evidence or an evidence-based blocker/unblock route.
  why_this_goal_is_minimal: >
    The accepted setup/validation envelope is used as input; this Goal
    does not rebuild that envelope.
  why_not_premature_or_optional_expansion: >
    P0 has selected H1_G4 as the active Phase and G1 shapes only
    WHAT/WHY/DONE before E1 plans HOW.
```

## Proof status

```yaml
proof_status:
  map_frontier_binding_status: proven_compact_with_nonblocking_map_projection_staleness
  next_action_proof_status: proven_compact_inherited_from_P0_and_phase_brief
  minimum_complete_outcome_defined: true
  minimum_complete_outcome: runnable_validated_nucleus_slice_or_concrete_blocker_unblock_packet
  mssp_status: proven_compact
  user_example_classification: not_present
  solution_shape: smallest_complete_goal_contract_before_execution_planning
  solution_minimal: true
  complete_enough: true
```

## Close path

```yaml
close_path:
  current_stage: G1_GOAL_SHAPE
  current_result_after_formalization: goal_shaped_pending_E1_execution_brief
  next_stage: E1_EXECUTION_BRIEF
  e1_purpose: >
    Prepare the minimum HOW, validation path, execution route, allowed
    surfaces, forbidden surfaces, context requirements, and blocker
    handling for this Goal.
  r1_allowed_only_after:
    - parent_goal_completion_state_complete
    - runnable_slice_evidence_or_blocker_packet_exists
  phase_progress_gate_after_r1_required: true
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/00_GOAL_CONTRACT.md`
