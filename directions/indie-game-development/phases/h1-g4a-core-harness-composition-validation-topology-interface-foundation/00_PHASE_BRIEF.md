# H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation

```yaml
artifact_control:
  artifact_name: "H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation Phase Brief"
  schema: phase_brief.v1
  owner_layer: persistence
  status: active_goal_r1_accepted_pending_P9_phase_close
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-23"
  repo_path: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_PHASE_BRIEF.md"

phase:
  id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  name: "H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation"
  status: active_goal_r1_accepted_pending_P9_phase_close
  direction_id: indie_game_development
  parent_horizon: H1_playable_technical_nucleus
  previous_broad_phase_id: h1-g4-durable-technical-nucleus-first-runnable-build
  active_goal_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  next_route: P9_PHASE_CLOSE
  next_route_mode: close_or_pause_h1_g4a_core_harness_composition_validation_topology_interface_foundation_after_r1_acceptance
  active_goal_status: r1_accepted_goal_complete
  review_verdict: completed_verified
  goal_review_verdict: accepted_complete
  completion_scope: parent_goal_complete
  parent_goal_completion_state: complete
  phase_progress_gate_status: phase_close_candidate
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Purpose

H1_G4A is the product-facing first foundation for the H1 playable technical nucleus. It must produce or route-gate a runnable core harness, explicit composition/dependency boundary, validation entry surface, and topology interface contract that future Grid/Topology, Gas, Grid-Gas interaction, and Multiplayer boundaries can extend.

This Phase is not documentation-only. It exists to make the smallest complete foundation result concrete enough for E1 to prepare HOW and validation without reopening the overbroad H1_G4 shape.

## Why this is not a repeat

The previous broad H1_G4 runnable nucleus boundary allowed a gas-focused partial result to look close to acceptance even though the foundation result shape was not explicit enough. A1 determined that direct E1 repair was not basis-valid until WHAT/result shape was repaired.

Existing setup/validation envelope and the X1 TechnicalNucleus output are input evidence. They are not the new H1_G4A result and do not complete this Phase.

## Current Critical Constraint

The Direction needs a compact, result-facing foundation boundary before execution can resume. E1 must not continue from the old all-in-one H1_G4 durable nucleus, a disposable gas-only demo, or stale operator-report-only repair state.

Implementation remains blocked until E1/X1 or another registry-valid route explicitly authorizes product work.

## Minimum Outcome

The minimum complete outcome is one of:

1. A product-local runnable core harness with composition seams, validation entry point, topology interface contract, Unity-as-render/driver separation, and product persistence evidence.
2. A concrete blocker/unblock packet that proves why the H1_G4A foundation cannot be produced safely yet.

The Phase must not be cut below harness, composition boundary, validation surface, topology interface contract, and persistence evidence.

## Validation Signal

Accepted evidence must include:

- product repo committed or otherwise persisted evidence;
- Markdown Codex Operator Report;
- validation command/result or Unity/manual validation checklist;
- changed files and why they matter;
- architecture evidence that Unity scenes drive, visualize, or validate but do not own core domain logic.

## Phase Result Contract

```yaml
phase_result_contract:
  required_result: h1_g4a_product_facing_foundation_or_concrete_blocker_unblock_packet
  accepted_result_requires:
    - runnable_core_harness_or_exact_blocker
    - explicit_composition_dependency_boundary
    - validation_entry_surface
    - topology_interface_contract
    - Unity_as_render_or_driver_not_domain_owner
    - domain_logic_separated_from_multiplayer_transport
    - product_persistence_evidence
  documentation_only_result_allowed: false
  disposable_gas_only_demo_allowed: false
```

## Phase Closure Contract

H1_G4A can close only after a later review accepts product-facing foundation evidence or accepts a concrete blocker/unblock route. Phase close is not available from G1 formalization alone.

Closure evidence must prove:

- the H1_G4A foundation exists in the product repo and can be run or inspected through the validation surface; or
- the blocker packet names the exact blocker, why safe execution cannot continue, smallest unblock route, and next registry-valid stage.

## Scope

In scope:

- core harness foundation;
- composition/dependency seams;
- validation entry point;
- topology interface contract;
- product persistence evidence requirements;
- Markdown Operator Report requirement;
- future phase candidate preservation.

Out of scope:

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

## Future Phase Candidates

Parked candidate boundaries, not current scope:

- H1_G4B_grid_topology_foundation — Grid / Topology Foundation.
- H1_G4C_gas_simulation_foundation — Gas Simulation Foundation.
- H1_G4D_grid_gas_interaction — Grid-Gas Interaction.
- H1_G4E_multiplayer_boundary_foundation — Multiplayer Boundary Foundation.

## Guardrails

- No product code changes are authorized by G1.
- No Codex product execution is authorized by G1.
- No Task Master graph creation.
- No Unity MCP setup.
- No old-code transfer.
- No Game Documentation promotion.
- No broad vertical slice expansion.

Unity may drive, visualize, or validate the foundation, but Unity must not own core domain logic. Domain/business logic must remain separated from multiplayer transport.

## R1 acceptance

R1 accepted H1_G4A as a completed verified product-facing foundation. The accepted evidence is the GasCoopGame commit `236bc30e1cfc9aa081325144d778d1f28283aa63`, `MODULE_MAP.md`, `Assets/Scripts/GasCoopGame/CoreFoundation/**`, `Assets/Editor/GasCoopGame/H1G4A/**`, `.workflow/outbox/H1_G4A_OPERATOR_REPORT.md`, and `.workflow/evidence/h1-g4a-foundation-2026-05-23.md`.

```yaml
r1_acceptance:
  stage_id: R1_GOAL_REVIEW_DISTILL
  review_verdict: completed_verified
  goal_review_verdict: accepted_complete
  active_goal_status: r1_accepted_goal_complete
  completion_scope: parent_goal_complete
  parent_goal_completion_state: complete
  phase_progress_gate_status: phase_close_candidate
  accepted_product_commit: "ainazemtsau/GasCoopGame@236bc30e1cfc9aa081325144d778d1f28283aa63"
  next_route: P9_PHASE_CLOSE
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
```

## Next Route

`P9_PHASE_CLOSE — close_or_pause_h1_g4a_core_harness_composition_validation_topology_interface_foundation_after_r1_acceptance`

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_PHASE_BRIEF.md`
