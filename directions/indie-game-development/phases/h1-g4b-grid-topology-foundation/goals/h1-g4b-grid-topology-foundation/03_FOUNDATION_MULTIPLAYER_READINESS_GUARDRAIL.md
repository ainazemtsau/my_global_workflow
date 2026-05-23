# Foundation Multiplayer-Readiness Guardrail

```yaml
artifact_control:
  artifact_name: "Foundation Multiplayer-Readiness Guardrail"
  schema: foundation_multiplayer_readiness_guardrail.v1
  owner_layer: direction_goal
  status: accepted_user_intent
  direction_id: indie_game_development
  phase_id: h1-g4b-grid-topology-foundation
  goal_id: h1-g4b-grid-topology-foundation
  formalized_at: "2026-05-23"
  applies_until: "H1_G4E multiplayer boundary is implemented and accepted, or a later lifecycle stage explicitly replaces this guardrail."
```

## Rule

Foundational/domain systems must be designed as multiplayer-ready authoritative simulation cores from their first real implementation.

This does not mean building full multiplayer first. It means Grid, Gas, Grid-Gas interaction, and simulation-affecting devices must expose stable, observable, testable command/snapshot/delta/change-set boundaries so multiplayer can be layered later without rewriting the foundation.

## Applies to

```yaml
scope:
  - Grid / Topology Core
  - Gas Simulation Core
  - Grid-Gas Interaction
  - vents
  - fans
  - gas sources
  - gas sinks
  - blockers
  - doors
  - openings
  - destruction surfaces that affect simulation
  - any domain system that owns, mutates, or publishes authoritative simulation state
```

## Required for foundation acceptance

```yaml
required_for_foundation_acceptance:
  - stable_domain_or_spatial_IDs_where_replicated_or_observed_state_depends_on_identity
  - command_or_intent_input_boundary
  - authoritative_tick_or_explicit_step_boundary
  - deterministic_or_server_authoritative_consistency_model
  - snapshot_delta_or_change_set_output_boundary
  - validation_surface
  - performance_or_scale_evidence_when_the_system_is_foundational_or_hot_path
  - no_transport_dependency_inside_domain_core
  - no_Unity_presentation_dependency_as_source_of_truth
```

## Forbidden

```yaml
forbidden:
  - local_single_player_only_core_assumptions
  - FishNet_or_Steam_or_RPC_dependencies_inside_domain_core
  - NetworkObject_as_domain_identity
  - hidden_Unity_scene_state_as_authoritative_simulation_state
  - accepting_Grid_or_Gas_as_complete_without_future_multiplayer_observation_or_replication_boundary
```

## H1_G4B effect

H1_G4B Grid / Topology Core cannot be accepted as complete if it only works as a local single-player topology store. It must include a future network-observation/replication boundary through stable IDs, command/commit, version/change-set, and snapshot/delta or equivalent export surfaces.

## H1_G4C carryover

H1_G4C Gas Simulation Core must follow the same guardrail. Gas must be authoritative/tickable, snapshot/delta exportable, performance-tested on relevant scale, decoupled from Unity presentation, and decoupled from multiplayer transport.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/h1-g4b-grid-topology-foundation/goals/h1-g4b-grid-topology-foundation/03_FOUNDATION_MULTIPLAYER_READINESS_GUARDRAIL.md`
