# Goal Contract — H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation

```yaml
artifact_control:
  artifact_name: "Goal Contract — H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation"
  schema: goal_contract.v1
  owner_layer: persistence
  status: goal_shaped_pending_E1_execution_brief
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-23"
  repo_path: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md"

goal:
  id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  title: "Produce H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation"
  status: goal_shaped_pending_E1_execution_brief
  phase_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  phase_name: "H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation"
  shaped_by_stage: G1_GOAL_SHAPE
  next_route: E1_EXECUTION_BRIEF
  next_route_mode: prepare_h1_g4a_core_harness_composition_validation_topology_interface_foundation_execution_brief
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  task_master_graph_allowed_now: false
  unity_mcp_setup_allowed_now: false
  old_code_transfer_allowed_now: false
  game_documentation_promotion_allowed_now: false
```

## WHAT

Produce or route-gate the product-facing first foundation for H1_G4A:

- runnable core harness foundation;
- explicit composition/dependency boundary;
- validation entry surface;
- topology interface contract;
- product persistence evidence.

The result must establish a foundation that future Grid/Topology, Gas, Grid-Gas interaction, and Multiplayer boundaries can extend.

## WHY now

The previous broad H1_G4 runnable nucleus boundary was too wide and allowed a gas-focused partial result to be treated as close to acceptance. A1 required WHAT/result-shape repair before E1 can safely resume.

H1_G4A narrows the next result to the harness, composition, validation, and topology-interface substrate needed before implementation-specific H1_G4B/C/D/E work.

## DONE

The Goal can be accepted only when one of these exists:

1. Accepted product-facing H1_G4A foundation evidence, including runnable or inspectable harness, composition boundary, validation surface, topology interface contract, and product persistence evidence.
2. A concrete blocker/unblock packet proving why the H1_G4A foundation cannot be produced safely, with exact blocker, impact, smallest unblock route, and next registry-valid route.

Documentation alone is not DONE.

## Minimum Complete Outcome

A runnable core harness with composition seams, validation entry point, topology interface contract, Unity-as-render/driver separation, and product persistence evidence; or a concrete blocker/unblock packet.

## Acceptance Floor

- Product-facing result, not documentation-only.
- Core harness exists or exact blocker exists.
- Composition/dependency boundary explicit.
- Validation surface mandatory.
- Topology interface contract mandatory.
- Unity scene may drive, visualize, or validate but must not own core domain logic.
- Domain/business logic separated from multiplayer transport.
- Product persistence evidence mandatory.
- No disposable gas-only demo.

## Validation Signal

Required signal:

- product repo committed or persisted evidence;
- Markdown Codex Operator Report;
- validation command/result or Unity/manual validation checklist;
- changed files and why they matter;
- architecture evidence for Unity-as-render-engine boundary.

## Validation Method

E1 must define the smallest validation route that can prove the foundation. Acceptable methods include:

- domain/unit tests for pure harness or topology-interface contracts;
- integration test or local runner for composition boundary;
- Unity-visible validation scene or driver surface;
- debug output or state dump proving topology interface and validation flow;
- manual Unity validation checklist where automation is not yet sensible.

## Smallest Testable Slice

One bounded product-local technical validation surface that proves the harness, composition seam, validation flow, and topology interface can run or be inspected without requiring full Grid/Gas/Multiplayer implementation.

## Scope In

- core harness foundation;
- composition/dependency seams;
- validation entry point;
- topology interface contract;
- product persistence evidence requirements;
- Markdown Operator Report requirement;
- future phase candidate preservation.

## Non-goals

- disposable gas-only demo;
- full Grid/Topology implementation;
- full Gas Simulation foundation;
- Grid-Gas interaction implementation;
- Multiplayer implementation;
- Unity MCP setup;
- Task Master graph creation;
- Game Documentation promotion;
- old-code transfer;
- full vertical slice expansion.

## Scope Cuts / Deferred Candidates

Deferred until selected by later route:

- H1_G4B — Grid / Topology Foundation;
- H1_G4C — Gas Simulation Foundation;
- H1_G4D — Grid-Gas Interaction;
- H1_G4E — Multiplayer Boundary Foundation.

## Constraints

- No product code changes in G1.
- No Codex product execution in G1.
- No Task Master graph creation.
- No Unity MCP setup.
- No old-code transfer.
- No Game Documentation promotion.
- No broad vertical slice expansion.
- E1 must not plan beyond H1_G4A acceptance floor.

## Escalation Triggers

- Product repo persistence cannot be verified -> blocker/unblock packet or Context Request.
- Unity must own domain logic to make the slice work -> blocker or architecture repair.
- Topology interface cannot be contracted without implementing full topology -> scope repair.
- Validation surface cannot be run or inspected -> blocker/unblock packet.
- Required permissions, credentials, or local access are missing before material execution -> NEEDS INPUT.

## Map Binding

```yaml
map_binding:
  active_horizon: H1_playable_technical_nucleus
  active_node: H1_G4A_core_harness_composition_validation_topology_interface_foundation
  previous_broad_node: H1_G4_durable_technical_nucleus
  old_broad_phase_treatment: superseded_by_h1_g4a_boundary_repair
  future_phase_candidates_not_active_scope:
    H1_G4B: Grid / Topology Foundation
    H1_G4C: Gas Simulation Foundation
    H1_G4D: Grid-Gas Interaction
    H1_G4E: Multiplayer Boundary Foundation
```

## Proof Status

```yaml
proof_status:
  result_first_verdict: pass
  mssp_status: proven_compact
  outcome_classification: primary_result
  documentation_admission_required: true
  documentation_admission_status: admitted_as_execution_unlocking_goal_contract_and_runtime_projection
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Existing X1 Partial Evidence Treatment

```yaml
existing_x1_treatment:
  status: candidate_partial_evidence_only
  not_goal_completion: true
  reusable_only_if_E1_X1_preflight_proves_fit: true
  old_grid_gas_code_treatment: constraint_reference_only_not_transfer_source
```

Existing X1 TechnicalNucleus progress may inform E1 only if E1/X1 preflight proves it fits the H1_G4A foundation boundary. It is not accepted complete.

## Future Phase Candidate Handling

```yaml
future_phase_candidates:
  H1_G4B: "Grid / Topology Foundation"
  H1_G4C: "Gas Simulation Foundation"
  H1_G4D: "Grid-Gas Interaction"
  H1_G4E: "Multiplayer Boundary Foundation"
  current_scope: H1_G4A_only
```

## Close Path

```yaml
close_path:
  current_stage: G1_GOAL_SHAPE
  current_result_after_formalization: goal_shaped_pending_E1_execution_brief
  next_stage: E1_EXECUTION_BRIEF
  next_route_mode: prepare_h1_g4a_core_harness_composition_validation_topology_interface_foundation_execution_brief
  r1_allowed_only_after:
    - accepted_product_facing_h1_g4a_foundation_evidence
    - or_concrete_blocker_unblock_packet
  phase_close_allowed_now: false
  implementation_allowed_now: false
```

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md`
