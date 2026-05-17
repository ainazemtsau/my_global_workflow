# First Technical Nucleus Functional Specification

```yaml
artifact_control:
  artifact_name: "First Technical Nucleus Functional Specification"
  schema: first_technical_nucleus_functional_spec.v1
  owner_layer: persistence
  status: draft_gas_block_formalized_pending_apply_readback
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: first-technical-nucleus-functional-spec
  source_stage: F0_FAST_DIRECT
  formalized_at: "2026-05-17"
  formalization_trigger: APPROVE_AND_FORMALIZE_F0_ARTIFACT
  source_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md"
  sequencing_model: gated_sequential
  current_completed_block: gas_simulation_capability_frame
  next_blocks_state: blocked_until_valid_stage_after_apply_readback
```

## 1. Gas Simulation Capability Frame

### 1.1 Purpose

The first technical nucleus must prove that gas is a gameplay system, not only a visual effect and not an isolated simulation toy.

This frame defines the minimum gas capability surface needed before later blocks can safely specify level/spatial requirements, Grid/topology substrate requirements, cross-system interaction requirements, destructibility compatibility, validation/demo requirements, or implementation planning.

This block does not finalize the Gas Simulation architecture, does not choose a final Grid/topology architecture, does not transfer old code, and does not authorize implementation.

### 1.2 Gameplay-interesting gas behaviors

The first nucleus must support these gameplay-relevant gas behaviors:

1. Propagation through bounded spaces.

   Gas moves between rooms, corridors, shafts, vents, doors, breaches, and openings.

   The player-relevant question is: where will the gas go, and what can change that path?

2. Accumulation and clearing.

   Gas can build up in enclosed spaces, drain through openings, be vented, be scrubbed, or remain trapped when topology blocks escape.

3. Density-biased vertical behavior.

   Heavy gas tends to sink or occupy lower connected spaces.

   Light gas tends to rise into shafts, upper volumes, or high ventilation paths.

   Neutral gas spreads more evenly.

4. Source / sink behavior.

   Leaks, emitters, vents, scrubbers, and open boundaries can add or remove gas over time.

5. Topology-sensitive behavior.

   Door state, vent state, corridor openness, room connectivity, and future breach/opening events affect gas flow.

6. Observable hazard state.

   Gas must produce a readable gameplay state: concentration, unsafe zones, flow direction, and clearing progress must be visible through debug tools before final visual gas exists.

Cut for first nucleus:

- complex CFD;
- explosion shockwaves;
- full fire chemistry;
- debris physics;
- structural collapse;
- final network replication design;
- player ability design.

### 1.3 Gas types and properties needed

The first nucleus should model gas as typed mass/concentration distributed across spatial containers.

Minimum property set:

```yaml
gas_type:
  id:
  display_name:
  density_coefficient:
    meaning: "relative to normal air; 1.0 = neutral"
  hazard_profile:
    examples:
      - toxic
      - asphyxiant
      - obscuring
      - inert
  visibility_profile:
    debug_required: true
    final_visual_required_now: false
  spread_profile:
    flow_coefficient:
    diffusion_bias:
    vertical_bias_from_density:
  source_sink_profile:
    source_rate:
    sink_or_decay_rule:
  reaction_profile:
    first_nucleus: none_or_minimal_hook_only
```

This is a capability requirement, not an implementation schema.

### 1.4 Heavy / light / neutral model

Use a continuous `density_coefficient` with three named validation bands:

```yaml
density_model:
  baseline_air: 1.0
  light_gas: "< 1.0"
  neutral_gas: "= 1.0"
  heavy_gas: "> 1.0"
```

Reason:

- named bands make first validation readable;
- a continuous coefficient preserves future extensibility;
- a pure enum would be easier immediately but would likely become too rigid once temperature, buoyancy, pressure, or future reactions matter.

### 1.5 Spread through rooms, corridors, shafts, vents, and openings

The gas model should treat the world as connected spatial containers and portals/openings.

Required first-frame behavior:

```yaml
spread_requirements:
  spatial_containers:
    - room
    - corridor
    - shaft
    - vent_path
    - small_technical_room
    - larger_volume_optional
  connections:
    - door
    - opening
    - vent
    - shaft_link
    - breach_placeholder
  flow_inputs:
    - gas_mass_or_concentration_per_container
    - container_capacity_or_volume
    - connection_open_closed_state
    - connection_resistance_or_flow_limit
    - vertical_relationship
    - density_coefficient
    - source_and_sink_rates
  expected_behavior:
    - gas flows from high concentration/mass regions toward lower concentration/mass regions
    - open passages allow transfer
    - closed passages block or reduce transfer
    - vents and shafts can create strong directional validation cases
    - density affects vertical distribution enough to test heavy/light behavior
```

Not required now:

- final Grid topology architecture;
- exact 25 cm vs 50 cm cell implementation;
- final host-authoritative network replication;
- final Unity scene implementation.

### 1.6 Pressure / mass / capacity / flow boundary

The first nucleus should include a simplified mass/capacity/flow model, not full physical pressure simulation.

Required:

```yaml
first_nucleus_flow_model:
  mass_or_concentration_conservation: required
  container_capacity_or_volume: required
  source_rate: required
  sink_or_vent_rate: required
  connection_flow_limit: required
  pressure_like_gradient: simplified_required
  full_compressible_pressure_simulation: not_required
  shockwaves_or_blast_pressure: not_required
```

This is enough to test accumulation, clearing, overfilled spaces, shafts, vents, and topology changes without turning the nucleus into a physics research project.

### 1.7 Mixing / reactions / transformations

Boundary:

```yaml
mixing_and_reactions:
  multiple_gases_in_same_container: allowed
  independent_concentration_tracking: required
  full_reaction_system: deferred
  fire_or_explosion_reactions: deferred
  neutralization_or_scrubber_transformation: optional_minimal_hook
```

The first nucleus should allow more than one gas type to coexist for validation, but it should not require a chemistry system.

### 1.8 Two to three gas types for first demo validation

Recommended first validation set:

```yaml
demo_gas_types:
  - id: heavy_hazard_gas
    role: "Tests sinking behavior, low-room accumulation, shaft behavior, and clearing from lower spaces."
    density_band: heavy
    gameplay_read: "Danger accumulates in low / poorly ventilated areas."

  - id: light_hazard_gas
    role: "Tests rising behavior, upper vents, vertical shafts, and two-level spaces."
    density_band: light
    gameplay_read: "Danger migrates upward and may surprise players through vertical connectivity."

  - id: neutral_obscuring_or_asphyxiant_gas
    role: "Tests baseline spread, room/corridor propagation, source/sink behavior, and readable debug overlay."
    density_band: neutral
    gameplay_read: "Area denial / obscuring / atmosphere degradation without vertical bias."
```

`Clean air` should be treated as the baseline atmosphere, not counted as one of the demo gas types unless later validation requires explicit oxygen/air simulation.

### 1.9 Simulation debug / visualization requirements

Debug visibility is mandatory before final visual gas.

Required debug surfaces:

```yaml
debug_visualization:
  overlays:
    - per_room_or_zone_concentration
    - gas_type_presence
    - unsafe_thresholds
    - flow_arrows_between_connections
    - source_and_sink_markers
    - door_vent_open_closed_state
    - capacity_or_saturation_indicator
    - vertical_bias_indicator_for_light_heavy_gases
  metrics:
    - total_mass_per_gas_type
    - mass_added_removed_per_tick
    - mass_conservation_error_or_tolerance
    - highest_concentration_container
    - flow_rate_per_connection
  controls:
    - pause_step_tick
    - spawn_gas_source
    - toggle_door_or_vent
    - clear_or_scrub_gas
    - switch_gas_type
```

Final visual gas may be simpler than gameplay gas.

The debug layer is the acceptance surface for early correctness.

### 1.10 No-player validation surfaces

The first gas validation must work without player mechanics.

Required no-player tests / scenes:

```yaml
no_player_validation:
  - id: simple_room_to_corridor_propagation
    validates:
      - source emission
      - spread through open connection
      - accumulation
      - debug concentration display

  - id: closed_door_then_open_door_flow
    validates:
      - topology gate blocks flow
      - opening a connection changes flow
      - flow arrows and mass transfer update

  - id: vertical_shaft_light_vs_heavy
    validates:
      - light gas rises
      - heavy gas sinks
      - neutral gas baseline behavior remains understandable

  - id: ventilation_path_clearance
    validates:
      - vent/opening acts as sink or path
      - gas clears over time
      - source/sink rates are visible

  - id: multi_room_capacity_stress
    validates:
      - multiple connected containers
      - mass conservation
      - concentration gradients
      - debug remains readable

  - id: breach_or_new_opening_placeholder
    validates:
      - a new opening can be represented
      - gas can flow through it
      - later destructibility boundary has a minimal compatibility surface
```

No player controller, co-op, animation sync, final networking, or Unity production implementation is required by this block.

### 1.11 Dependency outputs captured from gas frame

#### What the level / spatial block needs from this gas frame

The next block must define spaces that can honestly validate:

```yaml
level_spatial_needs_from_gas:
  required:
    - at least two connected rooms
    - one corridor
    - one vertical_shaft_or_two_level_space
    - one ventilation path
    - one small technical room
    - doors_or_openings_that_can_toggle_state
    - source_location
    - sink_or_vent_location
  optional:
    - larger_hangar_like_room
    - complex_multi_room_loop
```

#### What the Grid / topology block needs from this gas frame

The Grid/topology substrate must eventually provide:

```yaml
grid_topology_needs_from_gas:
  stable_ids:
    - room_or_zone_id
    - connection_or_portal_id
    - door_or_vent_id
    - source_sink_anchor_id
  required_properties:
    - container_capacity_or_volume
    - connectivity_graph
    - connection_open_closed_state
    - connection_resistance_or_flow_limit
    - vertical_relationship
    - topology_mutation_event_for_new_opening
  future_network_relevance:
    - compact_snapshot_possible
    - delta_or_event_surface_possible
    - host_authoritative_update_order_representable
```

This does not decide whether old Grid, GridV2, or a new topology design is used.

#### What the validation demo block needs from this gas frame

The validation/demo block must include:

```yaml
validation_demo_needs_from_gas:
  debug_overlay_required: true
  no_player_scene_required: true
  mass_or_concentration_assertions_required: true
  flow_path_visualization_required: true
  source_sink_controls_required: true
  vertical_behavior_validation_required: true
  breach_opening_placeholder_validation_required: true
```

## 2. User Approval Gate After Gas Block

```yaml
gas_block_approval_gate:
  status: user_approved_for_f0_artifact_formalization
  approval_trigger_received: APPROVE_AND_FORMALIZE_F0_ARTIFACT
  approved_at: "2026-05-17"
  meaning: >
    The Gas Simulation Capability Frame may be persisted as the first
    gated block of the first technical nucleus functional specification.
    Later blocks must still proceed only through a valid workflow stage
    after repository apply/read-back, diff verification, and commit/main
    integration evidence.
  still_forbidden_inside_this_F0_run:
    - level_and_spatial_requirements_completion
    - grid_topology_substrate_requirements_completion
    - cross_system_interaction_completion
    - destructibility_compatibility_completion
    - validation_demo_synthesis_completion
    - implementation
    - Unity_bootstrap
    - old_code_audit_as_starting_point
    - old_code_transfer
    - Codex_product_project_execution
    - Task_Master_graph_creation
```

The workflow must not proceed to later substantive blocks inside this F0 run.

After this artifact is applied and verified, the next valid lifecycle route may decide how to continue from the accepted gas frame.

## 3. Level and Spatial Requirements

Status: `blocked_until_valid_stage_after_gas_frame_apply_readback`

Dependency:

- accepted `gas_simulation_capability_frame`;
- repository apply/read-back verification;
- valid next workflow stage.

Placeholder only.

Expected later surfaces:

- simple rooms and corridors;
- vertical shafts / two-level spaces;
- ventilation paths;
- small technical rooms;
- long corridor;
- optional larger hangar-like room if useful;
- openings / doors / passages;
- complex test level after simple level.

## 4. Grid / Topology Substrate Requirements

Status: `blocked_until_level_and_spatial_requirements`

Dependency:

- accepted gas frame;
- level/spatial requirements;
- valid later workflow stage.

Placeholder only.

Expected later surfaces:

- room/zone/cell/chamber concepts;
- stable IDs for rooms, doors, portals, openings;
- connectivity/passability representation;
- topology mutation/effective topology overlays;
- how other systems read/write spatial effects;
- snapshot/delta implications for host-authoritative co-op.

## 5. Cross-System Interaction Requirements

Status: `blocked_until_grid_topology_substrate_requirements`

Placeholder only.

Expected later systems:

- temperature;
- airflow;
- fans;
- valves;
- doors;
- vents;
- leaks/sources;
- hazards;
- future reactions/fire.

## 6. Destructibility Compatibility Boundary

Status: `blocked_until_grid_topology_substrate_requirements`

Placeholder only.

Required later compatibility surface:

- opening/breach can appear in topology;
- gas can flow through new opening;
- topology/effective connectivity update order is representable.

Not required now:

- full destruction implementation;
- debris physics;
- fragments knocking players down;
- explosion wave as required nucleus feature;
- structural collapse simulation.

## 7. Validation / Demo Requirements

Status: `blocked_until_gas_level_and_topology_blocks`

Placeholder only.

Candidate later scenarios:

- no-player simulation demo;
- simple propagation scene;
- vertical shaft scene;
- ventilation path scene;
- complex multi-room scene;
- breach/opening gas-flow scene;
- stress scenario with multiple gases or larger volume.

## 8. Synthesis

Status: `blocked_until_prior_blocks_are_accepted`

Placeholder only.

The final synthesis must integrate accepted prior blocks into one coherent first technical nucleus functional specification.

## 9. Explicit Non-Goals and Old Project Reference Policy

This specification does not approve direct old-code transfer.

Old Grid, GridV2, GasV2R, and Grid↔Gas material may be used later only as targeted reference/evidence after the new requirements are clear.

This gas frame does not decide:

- final Gas Simulation architecture;
- final Grid/topology architecture;
- old GasV2R reuse / rewrite / discard classification;
- Unity project setup;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- full destructibility implementation;
- final multiplayer replication model.

## 10. Acceptance Checks for This Artifact

This artifact passes the F0 gas-frame floor if:

- the only completed substantive block is `gas_simulation_capability_frame`;
- the gas behaviors and properties are specified or explicitly deferred;
- heavy/light/neutral behavior uses a continuous density coefficient with named validation bands;
- rooms, corridors, shafts, vents, doors, openings, and breach placeholders are represented as required spread surfaces;
- pressure is bounded to simplified mass/capacity/flow behavior, not full pressure physics;
- mixing is allowed but full reactions are deferred;
- two to three gas types are specified for first validation;
- debug/visualization and no-player validation surfaces are listed;
- dependency outputs for level/spatial, Grid/topology, and validation/demo blocks are captured;
- later blocks are marked blocked, not completed;
- old project material is reference/evidence only;
- implementation, Unity bootstrap, Codex product/project execution, Task Master graph, and Game Documentation promotion are not included.

## 11. Alternatives Considered

### Start from old GasV2R transfer/reuse classification

Rejected.

Requirements must come first. Old material is evidence only after the new game's requirements are clear.

### Finalize gas architecture now

Rejected.

This F0 slice is a capability frame, not final architecture.

### Create a throwaway gas prototype

Rejected.

Gas-only proof is insufficient. This block exists inside a broader first technical nucleus specification.

### Define full reactions, fire, explosions, and destructibility now

Rejected.

This would over-expand the first gas block and prematurely consume later cross-system/destructibility work.

### Use visual gas as the acceptance surface

Rejected.

Visual gas may be simpler than gameplay gas. The first acceptance surface is debug-visible gameplay gas state.

## 12. Risks and Assumptions

Main assumption:

- a room/zone/chamber-level gas model is sufficient for the first technical nucleus.

Main risk:

- the gas frame could become too generic.

Countermeasure:

- force observable no-player validation scenes and two to three concrete gas types.

What would change the recommendation:

- fire/reactions become first-nucleus gameplay instead of future-compatible hooks;
- player mechanics become required for immediate gas validation;
- old GasV2R is allowed to dictate requirements;
- final Grid/topology architecture is required before accepting gas requirements;
- gas validation scale requires current external research or performance evidence.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`
