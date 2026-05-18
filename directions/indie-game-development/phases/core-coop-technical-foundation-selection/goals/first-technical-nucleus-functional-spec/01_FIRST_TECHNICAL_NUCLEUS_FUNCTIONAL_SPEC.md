# First Technical Nucleus Functional Specification

```yaml
artifact_control:
  artifact_name: "First Technical Nucleus Functional Specification"
  schema: first_technical_nucleus_functional_spec.v1
  owner_layer: persistence
  status: synthesis_formalized
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: first-technical-nucleus-functional-spec
  source_stage: F0_FAST_DIRECT
  formalized_at: "2026-05-18"
  formalization_trigger: APPROVE_AND_FORMALIZE_F0_SYNTHESIS_BLOCK
  source_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md"
  sequencing_model: gated_sequential
  current_completed_block: synthesis
  next_blocks_state: parent_goal_completion_candidate_pending_apply_readback_diff_commit_main_verification
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

Status: level_and_spatial_requirements_formalized

### 3.1 Purpose

This block defines the minimum spatial surfaces required for the first technical nucleus to validate the accepted Gas Simulation Capability Frame.

The level/spatial requirement is not final level design. It is a validation substrate: enough connected space, passage structure, verticality, ventilation, toggleable openings, and source/sink anchors to make gas behavior observable before Grid/topology, cross-system interaction, destructibility compatibility, validation/demo requirements, or implementation are completed.

### 3.2 Minimum Test Space Set

The first technical nucleus requires a compact no-player validation space composed of the following required spaces.

#### MTS-01 — Simple Connected Room Chain

Required.

Purpose: validate basic gas movement across connected spaces.

Minimum contents:
- Room A: source-capable room.
- Corridor C: narrow connector between rooms.
- Room B: receiving room with sink/vent-capable anchor.
- Door/opening D-01 between Room A and Corridor C, with toggleable open/closed state.
- Door/opening D-02 or permanent opening between Corridor C and Room B.
- Observation/debug points in Room A, Corridor C, and Room B.

Acceptance role:
- Supports simple room-to-corridor propagation.
- Supports closed-door-then-open-door flow.
- Provides the smallest readable gas path: source room → connector → receiving room.

#### MTS-02 — Ventilation / Clearance Path Space

Required.

Purpose: validate that gas has an explicit ventilation or sink route and that the route can be checked separately from ordinary room adjacency.

Minimum contents:
- One small technical room or service alcove.
- One ventilation path connecting the technical room or corridor to a sink/vent location.
- One clear path from a gas-bearing room/corridor to the vent/sink.
- One obstruction-free clearance segment that makes it possible to distinguish “vent path is clear” from “vent path is blocked or unavailable” in later validation.

Acceptance role:
- Supports ventilation path clearance validation.
- Provides the spatial basis for sink/vent behavior without requiring final ventilation gameplay, art, effects, or implementation.

#### MTS-03 — Vertical Shaft or Two-Level Space

Required.

Purpose: validate vertical gas behavior for light/heavy gas expectations.

Minimum contents:
- One vertical shaft, stairwell-like void, lift-like void, duct, or two-level room.
- Distinct lower and upper spatial bands.
- A bottom anchor and a top anchor.
- A vertical connection that is not treated as a normal horizontal doorway.
- Observation/debug points at lower, mid, and upper positions.

Acceptance role:
- Supports light-vs-heavy vertical behavior.
- Provides a minimal spatial basis for upward accumulation, downward accumulation, and vertical path traversal.

#### MTS-04 — Optional Larger Stress Space

Optional.

Purpose: stress capacity, visibility, and propagation behavior after simple validation passes.

Acceptable forms:
- Larger hangar-like room connected to the simple room chain.
- Multi-room loop branching from the corridor.
- Additional room/corridor loop that returns to Room A, Room B, or the technical room.

Acceptance role:
- Supports multi-room capacity stress.
- Must remain optional until the simple required spaces pass validation.
- Must not become final level layout or production map design.

### 3.3 Spatial Archetype List

The first technical nucleus must recognize these spatial archetypes at requirement level:

1. Standard room
   - A bounded space that can hold gas volume and expose observable gas state.

2. Corridor
   - A narrow connector that tests propagation through constrained space.

3. Toggleable door/opening
   - A passage whose gas-transmission state can be represented as open or closed.

4. Permanent opening
   - A passage that remains open and does not require interaction logic.

5. Vertical shaft / two-level connection
   - A non-horizontal connection with lower/upper bands.

6. Ventilation path
   - A directed or semi-directed gas clearance path toward a sink/vent anchor.

7. Small technical room
   - A compact service space used for vent/sink/source adjacency tests.

8. Source anchor
   - A named location where gas can originate for validation.

9. Sink/vent anchor
   - A named location where gas can be cleared, exhausted, or measured as exiting.

10. Optional breach/new-opening placeholder
    - A reserved spatial marker for a future opening/breach compatibility test; not destructibility implementation.

11. Optional large capacity room
    - A larger room used only for stress validation after the required simple scene passes.

12. Optional loop / branch
    - A multi-room route used only for capacity and pathing stress; not required final topology.

### 3.4 Simple Level Requirements

The required simple validation level must include:

- at least two connected rooms;
- one corridor between or adjacent to those rooms;
- one toggleable door/opening along the path from source to sink;
- one permanent or open passage that allows gas to continue after the controlled door;
- one source anchor in the source-side room;
- one sink/vent anchor in the receiving side or ventilation path;
- one small technical room or service alcove connected to the corridor or receiving room;
- one ventilation path connected to the small technical room, corridor, or receiving room;
- one vertical shaft or two-level space reachable from the simple chain;
- enough observation/debug locations to compare gas state before, inside, and after each connection.

The simple level must be small enough that failure can be diagnosed from spatial configuration rather than from map complexity.

### 3.5 Complex Level Requirements

Complex spatial surfaces are allowed only as optional validation extensions.

A complex validation space may include:
- one larger hangar-like room;
- one additional branch room;
- one loop path;
- one second sink/vent location;
- one placeholder breach/new-opening marker.

A complex validation space must not:
- define final game level layout;
- introduce final gameplay encounter design;
- require production art, lighting, navigation, networking, or destructibility;
- require final Grid/topology architecture before Section 4.

Complex spaces exist only to verify that the simple gas behavior remains stable when spatial capacity and path count increase.

### 3.6 Vertical Space Requirements

The vertical shaft or two-level space must support validation of light/heavy gas behavior by providing:

- lower anchor;
- upper anchor;
- observable lower/middle/upper positions;
- a continuous or explicitly connected vertical passage;
- enough separation between lower and upper bands for vertical distribution to be visible;
- no dependency on player movement, ladders, animation, or final traversal design.

The vertical space must allow tests in both directions:
- source low, observation/sink high;
- source high, observation/sink low.

This block does not decide final vertical Grid representation, voxel/cell size, implementation data model, or physics algorithm.

### 3.7 Ventilation and Clearance Path Requirements

The ventilation path must provide:

- one named vent/sink anchor;
- one spatial route from a gas-bearing area to the vent/sink;
- one clear segment where gas should be able to pass;
- one identifiable boundary or passage where later systems can decide whether the path is open, closed, blocked, or unavailable;
- observation/debug positions before the vent path and at/near the sink.

The ventilation path must be sufficient for these validation questions:
- Does gas reach the vent/sink when the route is clear?
- Does gas remain or accumulate differently when the route is unavailable?
- Can the validation scene distinguish ordinary room spread from deliberate ventilation clearance?

This block does not implement fans, pressure machinery, powered ventilation, environmental controls, or final audiovisual treatment.

### 3.8 Doors, Openings, and Passage Requirements

The first technical nucleus requires at least one passage whose gas-flow state can be toggled.

Minimum door/opening states:
- closed: should block or materially restrict gas flow according to the later gas model;
- open: should allow gas to pass according to the later gas model.

The required passage does not need:
- final door art;
- animation;
- player interaction;
- networking;
- lock/key logic;
- sound;
- final gameplay rules.

The passage must expose enough state for later validation to compare gas behavior before and after the state change.

Permanent openings may be used where no state toggle is needed.

### 3.9 Source and Sink / Vent Anchor Requirements

The required validation scene must include named anchors:

- `source_location.primary`
  - Located in Room A or equivalent source-side room.
  - Must be separated from the sink/vent by at least one passage.
  - Must be usable for simple propagation and closed/open door validation.

- `sink_or_vent_location.primary`
  - Located in Room B, the ventilation path, or the small technical room/vent outlet.
  - Must be reachable through the intended gas path.
  - Must allow validation to distinguish “gas reached destination” from “gas remained contained.”

- `source_location.vertical_lower`
  - Located near the lower band of the vertical shaft/two-level space.

- `source_location.vertical_upper`
  - Located near the upper band of the vertical shaft/two-level space.

- `sink_or_vent_location.vertical_counterpart`
  - Located at the opposite vertical band from the active vertical source.

Optional anchors:
- `source_location.stress`
- `sink_or_vent_location.secondary`
- `breach_placeholder.opening_candidate`

Anchors are test fixtures, not final gameplay spawn systems.

### 3.10 Gas Validation Scene Mapping

| Gas validation scenario | Required spatial surface | Minimum scene mapping |
| --- | --- | --- |
| Simple room-to-corridor propagation | MTS-01 Simple Connected Room Chain | Source in Room A; gas crosses into Corridor C; receiving state observable in Corridor C and Room B. |
| Closed-door-then-open-door flow | MTS-01 with D-01 toggleable door/opening | Door D-01 starts closed, limiting/blocking flow; door D-01 opens, allowing measurable movement into Corridor C and then Room B. |
| Vertical shaft light-vs-heavy behavior | MTS-03 Vertical Shaft / Two-Level Space | Source alternates lower/upper anchors; observation compares lower, middle, and upper bands. |
| Ventilation path clearance | MTS-02 Ventilation / Clearance Path Space | Gas-bearing area connects to vent/sink anchor through a clear path; sink/vent behavior is observable separately from ordinary spread. |
| Multi-room capacity stress | MTS-04 Optional Larger Stress Space | Optional larger room, branch, or loop connects to the required simple chain after simple validation passes. |
| Breach/new-opening placeholder | MTS-01 or MTS-04 with reserved opening marker | A non-implemented opening candidate is marked for future compatibility; no destructibility logic is required in this block. |

### 3.11 Dependency Outputs for Grid / Topology Substrate Requirements

This section does not design final Grid/topology architecture. It only defines spatial facts that Section 4 must be able to consume or represent.

Required dependency outputs for the later Grid/topology block:

- spatial region inventory:
  - room IDs;
  - corridor IDs;
  - technical room IDs;
  - vertical space IDs;
  - optional stress-space IDs.

- adjacency inventory:
  - room-to-corridor connection;
  - corridor-to-room connection;
  - room/corridor-to-technical-room connection;
  - room/corridor-to-ventilation-path connection;
  - lower-band-to-upper-band vertical connection.

- passage inventory:
  - toggleable opening ID;
  - permanent opening ID;
  - ventilation path boundary ID;
  - optional breach/new-opening placeholder ID.

- passage state requirement:
  - at minimum, open/closed state must be representable for one gas-relevant passage.

- anchor inventory:
  - source anchors;
  - sink/vent anchors;
  - vertical lower/upper anchors;
  - optional stress/breach anchors.

- observation/debug inventory:
  - positions or region markers before, inside, and after each validation path.

- non-final topology note:
  - cell size, graph model, voxel model, sampling model, data structures, and implementation authority remain blocked until the Grid/topology substrate requirements block.

### 3.12 Explicit Non-Goals and Scope Cuts

This block does not decide or perform:

- final level design;
- production scene layout;
- Unity scene creation;
- code generation;
- player traversal;
- final art, lighting, sound, or VFX;
- final ventilation machinery;
- final destructibility;
- final Grid/topology architecture;
- final cell size or topology data model;
- gas implementation algorithms;
- multiplayer/network authority;
- old-code audit or transfer;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion.

Sections 4-8 remain blocked after this block unless later approved by the gated sequence.

## 4. Grid / Topology Substrate Requirements

Status: grid_topology_substrate_requirements_formalized

### 4.1 Purpose and Boundary

This block defines the minimum topology substrate that the first technical nucleus needs after the accepted Gas Simulation Capability Frame and the formalized Level and Spatial Requirements.

The topology substrate must represent enough stable spatial identity, connectivity, passability, vertical relation, vent availability, and current effective topology state for gas validation to be meaningful.

This block is a requirements layer, not final architecture.

It does not decide:

- final Grid architecture;
- old Grid reuse, GridV2 reuse, rewrite, or discard verdict;
- final cell size;
- final voxel, graph, region, chamber, or hybrid data structure;
- final network replication model;
- Unity scene implementation;
- old-code audit or transfer;
- Codex product/project execution.

The required substrate is only this:

- spatial regions can be named and referenced;
- connections between regions can be represented;
- gas-relevant passage state can be represented;
- vertical and ventilation relationships can be represented;
- the current effective topology can be read by gas and validation systems;
- future topology mutation can be represented as a placeholder event without implementing destructibility.

### 4.2 Required Topology Entities

The first technical nucleus requires these topology entities at requirement level.

#### Spatial Region

A spatial region is a bounded gas-relevant space.

Required region archetypes:

- room;
- corridor;
- small technical room;
- vertical shaft or two-level space;
- ventilation path;
- optional larger stress room;
- optional loop or branch region.

Each spatial region must expose:

- stable region ID;
- region archetype;
- capacity or volume value, estimate, or authored classification;
- optional vertical band information;
- observation/debug marker references;
- source/sink/vent anchor references where applicable.

This does not require final room/chamber/grid implementation.

#### Connection / Portal

A connection is a gas-relevant relation between two spatial regions or between a region and an exit/sink boundary.

Required connection archetypes:

- permanent opening;
- toggleable door/opening;
- ventilation path boundary;
- vertical shaft link;
- optional breach/new-opening placeholder;
- optional stress-loop connection.

Each connection must expose:

- stable connection ID;
- endpoint region IDs;
- connection type;
- open/closed or available/unavailable state when stateful;
- resistance or flow-limit requirement;
- vertical relationship where relevant;
- whether the connection belongs to the normal adjacency graph, ventilation graph, vertical graph, or mutation placeholder surface.

This does not require final portal geometry or final pathfinding representation.

#### Passage State Controller

A passage state controller represents the gas-relevant state of a door, opening, vent boundary, or future breach placeholder.

Minimum required states:

- open / available;
- closed / unavailable;
- restricted or limited, if needed for resistance/flow-limit validation.

For the first nucleus, at least one door/opening must support toggling between closed and open.

Vent path availability must be representable separately from ordinary room adjacency so validation can distinguish “gas spread through rooms” from “gas cleared through a ventilation route.”

#### Source / Sink / Vent Anchor

Anchors are stable named points or region-local markers used by gas validation.

Required anchor families:

- gas source anchor;
- sink or vent anchor;
- vertical lower anchor;
- vertical upper anchor;
- optional stress source/sink anchor;
- optional breach/new-opening candidate anchor.

Anchors are validation fixtures, not final gameplay spawn systems.

#### Observation / Debug Point

Observation points are stable markers for reading topology and gas state during validation.

Required observation points:

- before each required validation path;
- inside or at each meaningful connection;
- after each required validation path;
- lower/middle/upper positions in the vertical validation space;
- near the vent/sink boundary;
- at or near the breach/new-opening placeholder.

Observation points must be addressable by stable ID so debug overlays and validation checks can refer to the same locations across snapshots, events, and test runs.

### 4.3 Stable ID Requirements

Stable IDs are required because gas, validation, debug visualization, future systems, and host-authoritative co-op all need to refer to the same topology facts without depending on Unity object names, old Grid internals, or scene-specific transient references.

Required ID families:

```yaml
stable_topology_ids:
  region_id:
    required_for:
      - rooms
      - corridors
      - small_technical_rooms
      - vertical_spaces
      - vent_paths
      - optional_stress_spaces

  connection_id:
    required_for:
      - room_to_corridor_connection
      - corridor_to_room_connection
      - technical_room_connection
      - vertical_connection
      - ventilation_path_connection
      - permanent_opening
      - toggleable_opening
      - breach_placeholder_connection

  passage_state_id:
    required_for:
      - door_state
      - opening_state
      - vent_boundary_state
      - future_breach_state_placeholder

  door_or_opening_id:
    required_for:
      - toggleable_door_or_opening
      - permanent_opening
      - future_opening_candidate

  vent_path_id:
    required_for:
      - ventilation_path
      - vent_or_sink_boundary
      - vent_availability_query

  source_sink_anchor_id:
    required_for:
      - source_location_primary
      - sink_or_vent_location_primary
      - vertical_lower_source
      - vertical_upper_source
      - vertical_counterpart_sink
      - optional_stress_anchor

  observation_point_id:
    required_for:
      - per_region_debug_read
      - per_connection_debug_read
      - vertical_band_observation
      - vent_path_observation
      - breach_placeholder_observation

  breach_placeholder_id:
    required_for:
      - future_new_opening_representation
      - destructibility_compatibility_boundary
      - breach_opening_validation_surface

  topology_revision_id:
    required_for:
      - effective_topology_snapshot
      - event_ordering
      - host_authoritative_update_order
```

Stable IDs must be:

- compact enough for snapshot/event use;
- serializable;
- stable across a validation run;
- independent from final Unity hierarchy;
- independent from old Grid/GridV2 internals;
- usable by gas debug overlays and no-player validation scenes.

This block does not decide the final ID implementation format.

### 4.4 Connectivity and Passability Representation

The topology substrate must represent connectivity as an explicit graph or equivalent query surface.

Minimum required connectivity facts:

```yaml
connectivity_requirements:
  adjacency:
    - source_region_id
    - target_region_id
    - connection_id
    - connection_type

  passage_state:
    - open
    - closed
    - restricted_or_limited_if_needed

  flow_properties:
    - connection_resistance_or_flow_limit
    - connection_allows_gas_transfer
    - connection_blocks_or_reduces_gas_transfer

  vertical_relation:
    - same_level
    - lower_to_upper
    - upper_to_lower
    - vertical_band_delta_or_equivalent_requirement

  vent_path_availability:
    - vent_path_available
    - vent_path_unavailable
    - vent_or_sink_boundary_id
    - ordinary_adjacency_distinguished_from_vent_clearance

  mutation_placeholder:
    - possible_new_opening
    - inactive_until_future_event
    - activatable_as_topology_event_without_destructibility_implementation
```

The representation must support these questions:

- Which regions are adjacent?
- Which passage connects them?
- Is the passage open, closed, restricted, or unavailable?
- Does the connection have a flow limit or resistance?
- Is the relationship vertical, horizontal, or vent-directed?
- Is the ventilation route available?
- Has a future placeholder opening been activated?

Passability in this block is gas passability, not final player navigation, AI pathfinding, projectile logic, or line-of-sight.

### 4.5 Effective Topology Overlay Model

The first nucleus needs a readable current topology state, not only an authored base layout.

Represent effective topology as:

```yaml
effective_topology:
  base_topology:
    includes:
      - spatial_regions
      - static_adjacencies
      - permanent_openings
      - authored_vertical_connections
      - authored_ventilation_paths
      - validation_anchors
      - observation_points

  passage_state_overlay:
    includes:
      - door_open_closed_state
      - toggleable_opening_state
      - vent_boundary_state
      - restricted_or_flow_limited_state

  vent_availability_overlay:
    includes:
      - vent_path_available_or_unavailable
      - sink_or_vent_active_or_inactive
      - clearance_path_state

  mutation_placeholder_overlay:
    includes:
      - breach_placeholder_inactive
      - breach_or_new_opening_active_if_future_event_occurs
      - added_connection_id_if_activated

  effective_read:
    meaning: >
      The current gas-readable topology after base layout, current passage
      states, vent availability, and any future mutation placeholder state
      are combined.
```

The gas model and validation/debug surfaces must read effective topology, not only the base topology.

This model keeps the first nucleus future-compatible without forcing final destructibility, final networking, or final Grid architecture.

### 4.6 Topology Mutation Boundary

The topology substrate must be able to represent a future breach/new opening as a topology mutation event.

Required mutation boundary:

```yaml
topology_mutation_boundary:
  can_represent_new_opening: true
  requires_destructibility_implementation_now: false
  mutation_event_minimum_fields:
    - topology_revision_id_before
    - topology_revision_id_after
    - breach_placeholder_id
    - added_or_activated_connection_id
    - source_region_id
    - target_region_id
    - connection_type
    - initial_passage_state
    - connection_resistance_or_flow_limit
    - vertical_relation_if_any
  gas_expectation:
    - gas_can_read_new_effective_connection_after_event
    - gas_can_flow_through_new_opening_if_open_or_available
  blocked_now:
    - damage_model
    - debris_physics
    - wall_fragment_simulation
    - structural_collapse
    - explosion_pressure_wave
    - player_knockdown
    - final_destructibility_networking
```

Update order must be representable:

1. topology state changes;
2. effective topology revision updates;
3. gas reads the new effective topology;
4. gas simulation tick applies flow using the updated connectivity;
5. debug/validation surfaces observe the result.

This is an ordering requirement, not a final implementation or networking design.

### 4.7 Gas Read Boundary

Gas may read topology. Gas must not own topology.

Gas may read:

- region IDs;
- region capacity or volume;
- connection IDs;
- endpoint region IDs;
- connection type;
- open/closed or available/unavailable state;
- resistance or flow limit;
- vertical relationship;
- vent path availability;
- source/sink anchors;
- observation/debug points;
- topology revision ID;
- activated breach/new-opening placeholder state.

Gas may not be required to read:

- Unity scene hierarchy;
- MonoBehaviour references;
- final network transport state;
- old Grid internals;
- old GridV2 internals;
- final rendering/VFX data;
- player-controller state.

Gas may write gas state, gas metrics, and debug outputs.

Gas must not directly write:

- base topology;
- door/opening state;
- vent availability;
- breach activation;
- future destructibility events.

Later systems may write those surfaces through explicit boundaries, but Section 5 owns those cross-system interaction requirements.

### 4.8 Future Systems Read / Write Seed

This block creates seed surfaces for later systems without completing Section 5.

Future systems that may read topology:

- gas simulation;
- debug visualization;
- validation/demo checks;
- doors/openings;
- vents;
- valves;
- fans;
- hazards;
- temperature/airflow systems;
- future reactions/fire;
- future destructibility.

Future systems that may write topology-adjacent state later:

```yaml
future_write_seed:
  doors_or_openings:
    possible_write:
      - passage_open_closed_state
      - passage_restriction_or_flow_limit

  vents_or_sinks:
    possible_write:
      - vent_path_available_unavailable
      - sink_active_inactive
      - clearance_path_state

  fans_or_airflow:
    possible_write:
      - flow_bias_or_flow_modifier
    section_5_required: true

  valves:
    possible_write:
      - connection_resistance_or_flow_limit
      - source_sink_availability
    section_5_required: true

  hazards_or_reactions:
    possible_write:
      - source_activation
      - sink_or_transformation_activation
    section_5_required: true

  destructibility:
    possible_write:
      - breach_placeholder_activation
      - new_opening_connection_event
    section_6_required: true
```

This seed does not define final authority, gameplay rules, UI, networking, or implementation for those systems.

### 4.9 Host-Authoritative Co-op Implications

The topology substrate must be compatible with a host-authoritative co-op direction without finalizing networking.

Minimum implications:

```yaml
host_authoritative_topology_implications:
  stable_ids_required: true

  compact_snapshot_possible:
    required: true
    snapshot_contains:
      - base_topology_reference_or_version
      - topology_revision_id
      - current_passage_state_overlay
      - current_vent_availability_overlay
      - active_mutation_placeholder_overlay_if_any

  event_or_delta_surface_possible:
    required: true
    candidate_events:
      - door_or_opening_state_changed
      - vent_path_availability_changed
      - connection_flow_limit_changed
      - breach_placeholder_activated
      - topology_revision_advanced

  update_order_representable:
    required: true
    order:
      - topology_event_or_state_change
      - effective_topology_revision_update
      - gas_reads_effective_topology
      - gas_simulation_tick
      - gas_state_snapshot_or_delta
      - debug_or_validation_observation

  final_network_replication_model:
    status: not_required_in_this_block
```

This block requires that snapshot/delta/event surfaces be possible. It does not decide bandwidth strategy, prediction, rollback, interest management, transport serialization, or final replication schema.

### 4.10 Dependency Outputs for Cross-System Interaction Requirements

Section 5 must receive these dependency outputs from this block:

```yaml
dependency_outputs_for_section_5:
  topology_read_surfaces:
    - effective_topology_read
    - region_inventory_read
    - connection_inventory_read
    - passage_state_read
    - vent_path_availability_read
    - source_sink_anchor_read
    - observation_point_read

  topology_adjacent_write_surfaces_to_define_later:
    - door_or_opening_state_write
    - vent_path_availability_write
    - connection_flow_modifier_write
    - source_sink_activation_write
    - airflow_or_fan_modifier_write
    - valve_flow_limit_write
    - hazard_or_reaction_source_write

  ordering_questions_for_section_5:
    - which system owns each write
    - when writes occur relative to gas tick
    - whether writes are authoritative, predicted, debug-only, or validation-only
    - how conflicting writes are resolved
```

Section 5 remains blocked until a valid later stage completes it.

### 4.11 Dependency Outputs for Destructibility Compatibility Boundary

Section 6 must receive these dependency outputs from this block:

```yaml
dependency_outputs_for_section_6:
  breach_placeholder_id_required: true
  new_opening_can_be_represented: true
  activated_breach_has_connection_id: true
  activated_breach_has_endpoint_region_ids: true
  activated_breach_has_initial_passage_state: true
  activated_breach_has_flow_limit_or_resistance: true
  activated_breach_advances_topology_revision: true
  gas_can_read_breach_after_effective_topology_update: true
  explicit_non_goals:
    - no_full_destructibility_implementation
    - no_debris_physics
    - no_structural_collapse
    - no_final_damage_model
    - no_final_destruction_networking
```

This makes destructibility future-compatible without allowing destructibility to become an implemented first-nucleus feature.

### 4.12 Dependency Outputs for Validation / Demo Requirements

Section 7 must receive these dependency outputs from this block:

```yaml
dependency_outputs_for_section_7:
  validation_checks_needed:
    - topology_region_inventory_visible
    - connection_inventory_visible
    - stable_ids_visible_or_loggable
    - door_closed_blocks_or_restricts_gas_path
    - door_open_allows_gas_path
    - vertical_connection_reports_lower_upper_relation
    - vent_path_availability_affects_clearance
    - effective_topology_snapshot_visible
    - topology_revision_changes_after_state_change
    - breach_placeholder_can_be_activated_as_new_opening_for_validation
    - gas_reads_effective_topology_not_base_topology_only

  debug_surfaces_needed:
    - region_id_overlay
    - connection_id_overlay
    - passage_state_overlay
    - vent_path_status_overlay
    - vertical_relation_overlay
    - topology_revision_display
    - active_breach_placeholder_marker
```

Validation/demo requirements remain blocked until the gas, level/spatial, and topology blocks have been accepted.

### 4.13 Explicit Non-Goals and Scope Cuts

This block does not decide or perform:

- final Grid architecture;
- old Grid reuse verdict;
- old GridV2 reuse verdict;
- Grid/GridV2 rewrite/discard decision;
- final topology data structures;
- final cell size;
- final room/chamber/voxel/graph implementation model;
- Unity scene creation;
- code generation;
- old-code audit;
- old-code transfer;
- player navigation;
- AI pathfinding;
- final multiplayer replication;
- bandwidth/prediction/rollback design;
- final destructibility;
- final ventilation machinery;
- cross-system interaction completion;
- validation/demo completion;
- synthesis;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion.

Sections 5-8 remain blocked after this block unless later completed through the gated workflow sequence.

## 5. Cross-System Interaction Requirements

Status: cross_system_interaction_requirements_formalized

### 5.1 Purpose and Boundary

This block defines how gas, topology, topology-adjacent systems, player/actor interaction surfaces, environmental modifier hooks, debug, validation, and future systems may interact in the first technical nucleus.

The purpose is to prevent system interactions from becoming ambiguous ownership, hidden implementation coupling, or premature final architecture.

The first technical nucleus needs these boundaries:

- topology state can change before gas reads it;
- systems may influence topology only through explicit owning boundaries;
- source/sink modifiers can add or remove gas through explicit anchors;
- flow modifiers can bias or limit gas movement without owning gas state;
- environmental and future simulation hooks can interact through explicit modifier surfaces without requiring full temperature, pressure, fire, reaction, or chemistry implementation;
- gas may expose player/actor hazard or exposure state without owning player health, player controller state, or final gameplay effects;
- player/actor interactions may trigger gas-relevant systems only through the owning system boundary;
- systems may communicate through requirement-level events, commands, state changes, signals, or modifiers, but this block does not choose a final event-bus implementation;
- debug and validation systems can observe the combined state without owning simulation state.

This block is a requirements layer.

It does not implement:

- final system architecture;
- final event-bus architecture;
- final Grid/topology architecture;
- final gas architecture;
- final player health/effects system;
- final network replication model;
- final Unity scene;
- full temperature simulation;
- full pressure simulation;
- full fire/reaction chemistry;
- full destructibility;
- old-code audit or transfer;
- Codex product/project execution.

### 5.2 System Category Map

The first technical nucleus must recognize these system categories at requirement level.

#### Topology State Writers

Topology state writers affect the current effective topology or topology-adjacent state that gas may read.

Required categories:

- doors or openings;
- vents or vent boundaries;
- valves;
- future breach or destructibility seed, reserved for Section 6 only.

Topology state writers may submit state changes. They do not own gas simulation state.

A future non-gas system may influence a topology state writer only through that writer's explicit boundary. It must not silently mutate effective topology unless that later system is explicitly assigned ownership by a valid later stage.

#### Gas Source / Sink Modifiers

Gas source/sink modifiers affect where gas enters, exits, is scrubbed, or is activated.

Required categories:

- leaks or emitters;
- scrubbers;
- vents or sinks;
- hazards as source activators.

Gas source/sink modifiers may expose source/sink rates and activation state. They do not directly mutate topology.

#### Flow Modifiers

Flow modifiers influence gas movement across regions, connections, or vent paths.

Required categories:

- fans;
- airflow;
- pressure-like directional modifiers;
- valves as flow-limit modifiers.

Flow modifiers may bias, limit, or direct transfer. They do not own base topology or gas mass.

#### Environmental and Cross-Simulation Modifier Hooks

Environmental and cross-simulation modifier hooks expose future-compatible state that may later affect gas, topology-adjacent behavior, player/actor effects, or other simulation surfaces.

Required categories:

- temperature;
- future pressure-like environmental state;
- future fire or reactions;
- future chemical transformation hooks;
- future system-to-system modifier hooks.

For the first nucleus, these remain hooks unless a later valid stage explicitly routes them into required behavior.

#### Player / Actor Interaction Consumers and Effect Receivers

Player/actor systems may consume gas exposure or hazard state.

Required categories:

- player or actor exposure readers;
- health/effect/debuff candidates;
- interaction command sources routed through owning systems;
- future equipment/protection candidates if later required.

Gas may expose hazard/exposure outputs. Gas must not own final player health, input, controller state, animation, networking, or final gameplay effect logic.

#### Read-Only Consumers

Read-only consumers observe topology, modifiers, gas state, player/actor exposure state where relevant, and validation state.

Required categories:

- debug visualization;
- validation/demo checks;
- UI or telemetry candidates.

Read-only consumers must not own or mutate topology, gas, flow, source/sink, environmental, or player/effect state.

### 5.3 General Interaction Surface Rule

Cross-system interaction must be representable through explicit requirement-level surfaces.

Acceptable interaction surface types:

```yaml
interaction_surface_types:
  state_change:
    meaning: "An owning system changes its own gas-relevant state."
    examples:
      - passage_open_closed_state
      - vent_available_unavailable_state
      - source_active_inactive_state
      - flow_modifier_active_inactive_state

  command_or_request:
    meaning: "A non-owning system asks an owning system to perform a state change."
    examples:
      - player_interaction_requests_door_toggle
      - validation_requests_source_activation
      - system_requests_valve_state_change

  modifier:
    meaning: "A system contributes a readable effect without owning the target simulation."
    examples:
      - flow_bias
      - source_rate_modifier
      - sink_rate_modifier
      - environmental_modifier_hook

  signal_or_event:
    meaning: "A system reports that something happened and other systems may react through their own ownership boundaries."
    examples:
      - topology_revision_advanced
      - source_activated
      - gas_exposure_threshold_crossed
      - conflict_resolution_record_created
```

This does not require a final event bus, message bus, ECS event stream, Unity event system, observer pattern, or networking event schema.

Minimum interaction record requirements:

```yaml
interaction_record_requirement:
  source_system_id: required
  target_owner_system_id: required
  target_id: required
  interaction_type: required
  value_or_payload_summary: required
  tick_id_or_revision_id: required
  authority_or_scope: required
  debug_visibility: required
```

A system must not bypass another system's ownership boundary merely because it can technically reach the data.

### 5.4 Topology State Writer Boundaries

Topology state writers may affect effective topology through explicit state surfaces.

#### Doors or Openings

Doors/openings may write:

- passage open/closed state;
- passage restricted/unrestricted state if needed;
- connection resistance or flow-limit contribution;
- current passage state revision metadata.

Doors/openings must not write:

- gas concentration;
- gas mass;
- source/sink rate;
- final network state;
- Unity scene hierarchy;
- base topology identity;
- player health/effect state.

Gas reads the resulting effective topology after door/opening state is resolved.

Player/actor interaction, validation, debug controls, or future systems may request a door/opening state change only through the door/opening ownership boundary.

#### Vents or Vent Boundaries

Vents or vent boundaries may write:

- vent path available/unavailable state;
- sink or exhaust active/inactive state;
- clearance path state;
- vent boundary flow-limit contribution.

Vents must distinguish ordinary adjacency from deliberate clearance or sink behavior.

Vents must not directly write gas mass. Gas consumes vent/sink state during its tick.

#### Valves

Valves may write:

- connection resistance or flow-limit modifier;
- source/sink availability modifier;
- open/closed or restricted state when the valve is topology-relevant.

Valves may participate as topology-adjacent writers and flow modifiers.

Valves must not own gas state, base topology identity, player interaction rules, or final network authority.

#### Future Breach / Destructibility Seed

Future breach or destructibility may later write:

- breach placeholder activation;
- new opening connection event;
- initial passage state for the new opening;
- topology revision advancement.

This block does not complete destructibility compatibility.

Section 6 must define the destructibility compatibility boundary before breach/destructibility is treated as a completed requirement.

### 5.5 Gas Source / Sink Modifier Boundaries

Gas source/sink modifiers expose inputs that the gas simulation consumes during the gas tick.

#### Leaks or Emitters

Leaks/emitters may write source modifier records:

```yaml
source_modifier_requirement:
  source_anchor_id: required
  gas_type_id: required
  source_rate: required
  activation_state: required
  duration_or_tick_scope: required
  source_owner_system: required
```

Leaks/emitters must not directly write gas concentration. The gas simulation applies source rates during the gas tick.

#### Scrubbers

Scrubbers may write sink or removal modifier records:

```yaml
scrubber_modifier_requirement:
  sink_anchor_id_or_region_id: required
  affected_gas_type_or_profile: required
  sink_rate_or_removal_capacity: required
  activation_state: required
  duration_or_tick_scope: required
```

Scrubbers may remove or transform gas only through a gas-consumed sink/modifier surface.

Full chemistry or transformation logic is not required in this block.

#### Vents or Sinks

Vents/sinks may write:

- sink active/inactive state;
- sink rate or exhaust capacity;
- vent path availability;
- target region, connection, or anchor reference.

The gas simulation must read vent/sink state and apply removal or clearance during the gas tick.

#### Hazards as Source Activators

Hazards may activate source behavior through explicit source activation records.

Hazards may write:

- source active/inactive state;
- source intensity or rate modifier;
- source gas type reference;
- source anchor reference.

Hazards must not directly write gas concentration, topology mutation, player health/effect state, or fire/reaction outcomes in this block.

### 5.6 Flow Modifier Boundaries

Flow modifiers affect transfer behavior but do not own gas state.

#### Fans

Fans may write flow modifier records:

```yaml
flow_modifier_requirement:
  target_connection_id_or_region_pair: required
  direction_or_bias: required
  magnitude_or_strength: required
  active_state: required
  flow_limit_or_boost: optional
  duration_or_tick_scope: required
  owner_system: required
```

Fans may bias movement through an available connection or vent path.

Fans must not create new topology connections. If a path is closed or unavailable, fan effect must not silently override topology state unless a later valid requirement explicitly allows it.

#### Airflow

Airflow may write region-level or connection-level flow bias.

Airflow may express:

- preferred flow direction;
- flow strength;
- local or global bias;
- active/inactive state.

Airflow must remain a modifier surface, not a final atmospheric simulation or CFD model.

#### Pressure-Like Directional Modifiers

Pressure-like directional modifiers may influence gas movement through simplified gradients.

Required boundary:

- pressure-like modifiers may bias flow;
- they do not require full compressible pressure simulation;
- they must be visible in debug/validation when active;
- they must be resolved before the gas tick reads them.

#### Valves as Flow-Limit Modifiers

Valves may restrict, cap, or block transfer rates across a connection, vent boundary, or source/sink channel.

Valve flow limits must be represented as modifiers that gas can read. Valves do not directly write gas mass.

### 5.7 Environmental and Cross-Simulation Modifier Boundaries

Environmental and cross-simulation modifiers are future-compatible hooks unless later routed otherwise.

#### Temperature

Temperature may expose:

- region-level temperature state;
- connection-level temperature modifier if relevant;
- optional effect hook for density, buoyancy, reaction, hazard behavior, player/actor exposure, or other future simulation behavior.

For the first nucleus:

- temperature may be visible as a debug/validation hook;
- temperature does not require a full thermal simulation;
- temperature does not require final fire or reaction implementation;
- gas behavior must not depend on temperature unless a later accepted block explicitly requires it.

#### Future Pressure-Like Environmental State

Future pressure-like environmental state may expose:

- region-level pressure-like modifier;
- connection-level directional bias;
- environmental constraint affecting flow modifiers.

For the first nucleus, this remains a hook. It does not require a full pressure simulation.

#### Future Fire or Reactions

Future fire/reaction systems may later influence:

- source activation;
- gas transformation;
- hazard escalation;
- sink/neutralization behavior;
- environmental state;
- player/actor exposure effects;
- topology-adjacent state if a later valid stage assigns that boundary.

In this block, fire/reactions remain hooks only.

Required now:

- the interaction surface must not prevent future fire/reaction systems;
- current Section 5 must not implement or require them;
- future fire/reaction writes must use explicit modifier, source/sink, environmental, or owning-system boundaries.

#### Future Chemical Transformation Hooks

Chemical transformations may later consume and produce gas types.

For this block:

- transformation is represented only as a future hook;
- no reaction graph is required;
- no final chemistry taxonomy is required;
- scrubber/neutralization behavior may remain a minimal sink or transformation placeholder.

#### Future System-to-System Modifier Hooks

Future systems may interact with each other through explicit records.

Examples of allowed requirement-level patterns:

- one system requests another owning system to change its state;
- one system contributes a modifier read by another system;
- one system emits a signal that another system may consume through its own boundary;
- one system blocks, enables, or limits another system only through an explicit target owner and target ID.

This block does not decide the final technical mechanism for those interactions.

### 5.8 Player / Actor Interaction Boundaries

Player/actor interaction is important, but this block does not require a player controller, health system, final co-op behavior, animation, or final gameplay effect implementation.

The first nucleus must remain compatible with player/actor interactions by exposing explicit boundaries.

#### Gas to Player / Actor Exposure

Gas may expose:

- gas type presence near or inside a player/actor-relevant region;
- concentration or exposure value;
- unsafe threshold state;
- exposure duration or tick count if needed later;
- hazard profile reference;
- debug-readable exposure record.

Gas must not directly own:

- player health;
- player damage application;
- debuff state;
- equipment/protection behavior;
- player controller state;
- player animation;
- final network replication of player effects.

Player/effect systems may later consume gas exposure state and apply effects through their own ownership boundary.

#### Player / Actor to Gas-Relevant Systems

Player/actor interaction may later request:

- door/opening toggle;
- vent/sink activation;
- valve state change;
- source/sink activation;
- hazard interaction;
- debug or validation test command if explicitly routed.

These requests must route through the owning system boundary.

Player/actor interaction must not directly mutate:

- gas concentration;
- gas mass;
- base topology;
- effective topology;
- vent availability;
- flow modifier state;
- source/sink state.

#### No-Player Validation Compatibility

The accepted earlier gas frame requires no-player validation surfaces.

This Section 5 player/actor boundary does not replace no-player validation. It only ensures that later player-facing behavior can attach to gas/topology/system state without forcing player implementation now.

### 5.9 System-to-System Interaction Boundaries

Systems may interact with other systems only through explicit ownership boundaries.

Required rules:

- the target owner must be identifiable;
- the target ID must be stable enough for validation/debug;
- the interaction must be represented as state change, command/request, modifier, or signal/event;
- the receiving owner decides whether and how its state changes;
- gas-readable consequences are visible only after the owning system resolves its state;
- debug/validation can show both the requested input and the resolved output.

A system must not secretly mutate another system's internal state.

This is a requirement-level interaction rule, not a final architecture choice.

### 5.10 Read-Only Consumer Boundaries

Read-only systems may observe combined simulation state.

#### Debug Visualization

Debug visualization may read:

- effective topology;
- passage state;
- vent availability;
- source/sink modifiers;
- flow modifiers;
- environmental modifier hooks;
- player/actor exposure records if present;
- gas concentration/mass state;
- topology revision ID;
- gas tick ID;
- conflict-resolution outputs;
- interaction records where debug visibility is enabled.

Debug visualization must not write simulation state.

#### Validation / Demo Checks

Validation/demo checks may read the same surfaces as debug visualization.

Validation may trigger controlled test actions only when the action is routed through the owning system boundary, such as opening a door, activating a source, toggling a fan, or placing a player/actor exposure probe.

Validation checks must not bypass ownership boundaries.

#### UI or Telemetry Candidates

UI/telemetry candidates may read summarized state:

- unsafe region indicators;
- player/actor exposure indicators if later required;
- source/sink active indicators;
- flow direction indicators;
- topology or modifier revision;
- validation status.

UI/telemetry must not become a gameplay system or state owner in this block.

### 5.11 Read / Write / Non-Ownership Matrix

| System category | May read | May write | Must not own |
| --- | --- | --- | --- |
| Gas simulation | Effective topology, source/sink modifiers, flow modifiers, environmental hooks, player/actor exposure probe locations if later required | Gas state, gas metrics, gas exposure/hazard read surface, debug gas outputs | Base topology, passage state, vent availability, breach activation, player health/effects, final network state |
| Doors/openings | Passage IDs, current passage state, validation or player-routed commands | Passage open/closed/restricted state | Gas mass, gas concentration, source/sink rates, base topology identity, player state |
| Vents/sinks | Vent path IDs, sink anchors, current vent state, owning-system commands | Vent availability, sink active state, sink/removal rate | Gas state, ordinary adjacency, final ventilation machinery, player state |
| Fans/airflow | Connection IDs, region IDs, current topology availability | Flow bias, flow direction, flow strength, active/inactive state | Base topology, gas mass, source/sink identity, player state |
| Valves | Connection IDs, source/sink channels, current valve state | Flow limit, resistance, source/sink availability, valve state | Gas concentration, final network authority, unrelated topology, player state |
| Leaks/emitters | Source anchors, activation controls, gas type IDs | Source activation, gas type reference, source rate | Gas state application, topology state, player state |
| Scrubbers | Sink anchors, gas type/profile references | Sink/removal modifier, active state | Gas state application, topology state, player state |
| Hazards | Source anchors, hazard activation state, future environmental hooks | Source activation or intensity modifier | Full reaction/fire system, gas state, topology mutation, player health/effect application |
| Temperature / environmental hooks | Region/connection IDs, environmental state | Environmental modifier hook | Full thermal simulation, fire/reaction completion, gas ownership, player effect ownership |
| Future fire/reactions | Future source/sink/environmental hooks | Deferred hook outputs only after later routing | Current Section 5 completion, full chemistry, final fire logic, destructibility completion |
| Player/actor interaction | Exposure state, interaction targets, owning-system command surfaces | Interaction requests routed through owning systems; later player/effect state through player/effect owner | Gas state, topology state, source/sink state, flow modifier state |
| Player/effect systems | Gas exposure/hazard records, player/actor state, future equipment/protection state | Player health/effect/debuff state if later implemented | Gas state, topology, vent state, source/sink state, flow modifiers |
| Future non-gas system controller | Target owner boundaries, stable target IDs, relevant modifier records | Commands, requests, modifiers, or signals through explicit target owner | Another system's internal state unless explicitly assigned ownership |
| Debug visualization | Effective topology, modifiers, gas state, player/actor exposure records, revisions, interaction records | Debug display state only | Simulation ownership |
| Validation/demo checks | Effective topology, modifiers, gas state, player/actor exposure records, revisions | Test commands routed through owning systems | Simulation ownership, implementation authority |
| UI/telemetry candidates | Summaries of topology/modifier/gas/player-exposure state | UI/telemetry display state only | Simulation ownership |

### 5.12 Update Order Boundary

The first technical nucleus must support a deterministic update order for cross-system effects.

Required order:

```yaml
cross_system_update_order:
  1_collect_commands_state_changes_and_modifier_inputs:
    examples:
      - player_or_actor_interaction_request
      - validation_test_command
      - door_or_opening_state_change
      - vent_availability_change
      - valve_flow_limit_change
      - fan_or_airflow_modifier_change
      - source_or_sink_activation_change
      - environmental_modifier_change
      - system_to_system_command_or_signal
      - future_breach_placeholder_event_if_section_6_allows

  2_resolve_owning_system_state:
    includes:
      - door_or_opening_owner_resolves_passage_state
      - vent_owner_resolves_vent_availability
      - valve_owner_resolves_flow_limit
      - source_sink_owner_resolves_activation
      - environmental_owner_resolves_modifier_hooks
      - target_owner_resolves_system_to_system_requests

  3_resolve_effective_topology_and_modifier_state:
    includes:
      - passage_state_overlay
      - vent_availability_overlay
      - flow_modifier_overlay
      - source_sink_modifier_overlay
      - environmental_modifier_overlay
      - topology_revision_id_or_modifier_revision_id_update

  4_gas_reads_effective_state:
    gas_reads:
      - effective_topology
      - source_sink_modifiers
      - flow_modifiers
      - environmental_hooks_if_enabled
      - topology_revision_id
      - modifier_revision_id_if_present

  5_gas_simulation_tick:
    gas_writes:
      - gas_mass_or_concentration_state
      - gas_flow_metrics
      - source_sink_application_metrics
      - gas_exposure_or_hazard_read_surface_if_present
      - mass_conservation_or_tolerance_metrics

  6_player_actor_effect_consumers_read_exposure_if_enabled:
    consumers:
      - player_effect_system_candidates
      - actor_exposure_check_candidates
    writes_allowed_only_to:
      - player_or_actor_effect_state_if_later_implemented

  7_debug_validation_and_ui_read:
    consumers:
      - debug_visualization
      - validation_demo_checks
      - ui_or_telemetry_candidates
```

No system may silently mutate gas-readable topology or modifiers midway through a gas tick.

If a state change occurs during a tick, it is applied at the next defined update boundary unless a later implementation-stage decision explicitly defines sub-step behavior.

Player/actor effect consumption is represented as a boundary, not as a required implementation of health, damage, debuffs, or player controller logic.

### 5.13 Conflict Policy for Multiple System Effects

The first nucleus must expose deterministic conflict resolution for multiple systems affecting one connection, modifier, source, sink, player/actor exposure interpretation, or system-to-system target.

Required conflict policy:

```yaml
cross_system_conflict_policy:
  deterministic: required
  conflict_inputs_visible_in_debug: required
  resolved_output_visible_in_debug: required
  target_owner_required: true
  target_id_required:
    - connection_id
    - passage_state_id
    - vent_path_id
    - source_sink_anchor_id
    - flow_modifier_target_id
    - environmental_modifier_target_id
    - player_actor_exposure_target_id_if_present
    - system_interaction_target_id

  default_rules:
    passage_or_vent_availability:
      rule: "blocking_or_unavailable_wins_over_open_or_available unless a single explicit owner is assigned later"
    connection_flow_limit:
      rule: "most_restrictive_limit_wins unless a later owner-specific rule overrides"
    flow_direction_or_bias:
      rule: "combine compatible directional modifiers; opposing modifiers resolve to net bias or flagged conflict according to deterministic merge"
    source_rates:
      rule: "aggregate compatible sources by gas type and anchor; conflicting activation state uses explicit owner priority or validation-visible conflict flag"
    sink_rates:
      rule: "aggregate compatible sinks within configured capacity; conflicting activation state uses explicit owner priority or validation-visible conflict flag"
    environmental_hooks:
      rule: "store latest resolved hook state by owner priority; do not trigger full reactions in this block"
    player_actor_exposure:
      rule: "gas exposes hazard/exposure state; player/effect owner decides final effect application if later implemented"
    system_to_system_requests:
      rule: "target owner resolves requests; non-owning systems cannot directly mutate target state"

  required_conflict_record:
    - target_owner_system_id
    - target_id
    - input_systems
    - input_values
    - resolved_value
    - resolution_rule
    - topology_or_modifier_revision_id
    - gas_tick_id_if_relevant
```

Conflict resolution must be good enough for validation and debugging. It does not need to be a final production architecture.

### 5.14 Dependency Outputs for Destructibility Compatibility Boundary

Section 6 must receive these dependency outputs from Section 5:

```yaml
dependency_outputs_for_section_6:
  destructibility_writer_boundary:
    future_breach_or_destructibility_may_write:
      - breach_placeholder_activation
      - new_opening_connection_event
      - initial_passage_state
      - initial_connection_flow_limit_or_resistance
      - topology_revision_advance

  required_integration_questions_for_section_6:
    - how_breach_activation_competes_with_door_or_opening_state
    - whether_breach_creates_a_new_connection_or_activates_an_authored_placeholder
    - what_initial_passage_state_a_breach_or_new_opening_receives
    - how_gas_reads_the_new_effective_topology_after_the_breach_event
    - how_debug_validation_and_player_actor_exposure_surfaces_see_breach_activation_and_gas_flow_afterward
    - how_breach_events_participate_in_system_to_system_interaction_records_without_becoming_full_destructibility

  explicit_section_5_non_completion:
    - section_5_does_not_define_damage_model
    - section_5_does_not_define_debris_physics
    - section_5_does_not_define_structural_collapse
    - section_5_does_not_define_explosion_pressure_wave
    - section_5_does_not_complete_section_6
```

### 5.15 Dependency Outputs for Validation / Demo Requirements

Section 7 must receive these dependency outputs from Section 5:

```yaml
dependency_outputs_for_section_7:
  validation_checks_needed:
    - door_or_opening_state_change_occurs_before_gas_tick
    - vent_availability_change_affects_clearance_before_gas_tick
    - leak_or_emitter_source_rate_is_applied_by_gas_tick
    - scrubber_or_sink_removal_rate_is_applied_by_gas_tick
    - fan_or_airflow_modifier_biases_flow_without_owning_gas
    - valve_flow_limit_restricts_transfer_without_owning_gas
    - hazard_source_activation_uses_source_boundary
    - temperature_or_environmental_hook_is_visible_without_requiring_full_fire_reactions
    - future_system_to_system_interaction_can_be_represented_without_final_event_bus
    - player_actor_exposure_surface_can_be_read_without_requiring_player_health_implementation
    - player_or_validation_commands_route_through_owning_system_boundaries
    - gas_reads_effective_topology_and_modifiers_not_base_topology_only
    - debug_visualization_reads_state_without_owning_state
    - validation_commands_route_through_owning_system_boundaries
    - conflict_resolution_output_is_visible_for_shared_targets

  debug_surfaces_needed:
    - system_writer_overlay
    - source_sink_modifier_overlay
    - flow_modifier_overlay
    - environmental_hook_overlay
    - player_actor_exposure_overlay_if_present
    - system_interaction_record_overlay_or_log
    - conflict_resolution_overlay_or_log
    - update_order_step_display
    - topology_revision_and_gas_tick_display
```

Section 7 remains blocked until a valid later stage completes validation/demo requirements.

### 5.16 Explicit Non-Goals and Scope Cuts

This block does not decide or perform:

- final cross-system architecture;
- final event-bus implementation;
- Unity scene creation;
- code generation;
- old-code audit;
- old-code transfer;
- final Grid/topology architecture;
- final gas architecture;
- final player controller;
- final player health/effects/debuff system;
- final equipment/protection mechanics;
- final network replication model;
- final host/client prediction, rollback, or bandwidth design;
- full fire/reaction chemistry;
- full temperature simulation;
- full pressure simulation;
- full destructibility;
- damage model;
- debris physics;
- structural collapse;
- final ventilation machinery;
- player ability design;
- final UI/telemetry design;
- validation/demo completion;
- synthesis;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion.

Sections 6-8 remain blocked after this block unless later completed through the gated workflow sequence.

## 6. Destructibility Compatibility Boundary

### 6.1 Purpose and boundary

The first technical nucleus does not implement full destructibility.

This block defines only the compatibility boundary required so that a future destructibility-capable system can introduce a breach, new opening, or other topology-relevant barrier change into the accepted Grid/topology substrate without forcing a rewrite of Gas, topology, player/actor exposure, debug validation, or cross-system interaction records.

For this nucleus, destructibility is treated as a future writer boundary. The nucleus must be able to represent and observe a breach/new-opening activation, but it must not define the final damage model, debris behavior, structural simulation, explosion pressure model, visual destruction pipeline, or destruction networking model.

The compatibility target is narrow:

- a breach placeholder can exist;
- a breach or new opening can activate;
- the activation can mutate effective topology;
- Gas can read the updated topology after the mutation;
- validation/debug surfaces can prove that the new opening affected topology and Gas in the correct order;
- the representation does not block future runtime topology mutation types beyond the first breach/new-opening case.

### 6.2 Minimal compatibility surface

The first nucleus must support a minimal destructibility compatibility surface with these capabilities:

1. A breach placeholder may exist in the topology substrate as an addressable future-opening candidate.
2. A breach/new-opening activation may be represented as a cross-system event or record.
3. An activated breach must have a stable activated connection ID.
4. An activated breach must identify endpoint region IDs.
5. An activated breach must define an initial passage state.
6. An activated breach must define an initial flow limit or resistance value.
7. An activated breach must advance the topology revision.
8. Gas must read the new effective topology only after the topology update is applied.
9. Gas may flow through the new opening when the opening is open, available, leaking, partially open, or otherwise passable under the initial passage state and flow limit/resistance.
10. The record shape must remain compatible with future topology mutations such as connection closure, passage-state change, flow-resistance/permeability change, barrier/door state change, obstruction changes, material-layer-driven barrier updates, region split, and region merge.

This surface is compatibility-level only. It does not require arbitrary wall destruction, fracture simulation, authored debris, structural collapse, visual mesh cutting, damage accumulation, pressure-wave gameplay, or final replicated destruction state.

### 6.3 Breach placeholder definition

A breach placeholder is a topology-level compatibility marker that represents a possible future opening between spatial/topology regions.

A breach placeholder is not a destructible object implementation. It is not a damage receiver. It is not a visual destruction asset. It is not a physics fragment source.

A breach placeholder must be sufficient to answer:

- which future opening candidate is being referenced;
- which regions may become connected;
- what connection should be created or activated when the placeholder is triggered;
- what initial passage state and flow limit/resistance Gas should see after topology mutation;
- what topology revision should be observed before and after activation;
- what debug/validation surfaces should display.

The placeholder may be authored, test-created, or otherwise declared by the topology substrate for validation purposes. The first nucleus must not require player action, explosion logic, or a damage model to create arbitrary breach placeholders.

### 6.4 Breach/new-opening activation record requirements

A breach/new-opening activation record must include, at minimum:

- `breach_placeholder_id`;
- `activated_connection_id`;
- `endpoint_region_ids`;
- `initial_passage_state`;
- `initial_flow_limit_or_resistance`;
- `topology_revision_before`;
- `topology_revision_after`;
- activation source classification, limited to future destructibility writer boundary or validation/debug trigger;
- debug visibility fields sufficient to inspect activation order and resulting topology;
- cross-system interaction record participation, without requiring full destructibility implementation.

The activation record must be readable by validation/debug tooling and by any cross-system interaction log used by the nucleus.

The record must not require final damage values, fragment state, debris bodies, structural stress, final visual destruction state, or final network replication state.

### 6.5 Future scalable topology mutation compatibility

Breach/new-opening activation is the first required compatibility case of a broader future runtime topology mutation model.

The first nucleus validates only the minimal new-opening path. However, the representation must not make `ActivateBreach()` or equivalent breach-only behavior the only possible shape of future topology change.

The compatibility model should allow breach/new-opening activation to be treated as a specific topology mutation type, such as:

- create or activate a connection between endpoint regions;
- set the initial passage state for that connection;
- set the initial flow limit or resistance;
- advance the effective topology revision;
- expose the result to Gas, debug/validation, and player/actor exposure readers.

The same general mutation boundary should remain compatible with future mutation types, including:

- closing, sealing, blocking, or removing an existing connection;
- changing a connection's passage state;
- changing a connection's flow limit, resistance, permeability, or leakage state;
- adding or removing an obstruction;
- changing a door, hatch, vent, barricade, or barrier state;
- representing a partially open, leaking, obstructed, or collapsed opening;
- representing material-layer-driven barrier state changes as effective topology/permeability changes;
- splitting a region when a new wall or barrier meaningfully divides space;
- merging regions or increasing connectivity when a wall or barrier is removed;
- preserving before/after topology revision evidence for every topology-relevant mutation.

These future mutation types are not required first-nucleus features. They are compatibility constraints on the shape of the current breach/new-opening boundary.

The required model is:

```text
base topology
+ dynamic topology overlay
= effective topology read by Gas and exposure systems
```

Gas must read effective topology. Gas must not own the dynamic topology overlay or directly author destructibility mutations.

### 6.6 Topology mutation and update order

The required update order is:

1. A breach/new-opening activation is requested through the allowed writer boundary or validation/debug trigger.
2. The activation record is created with placeholder ID, endpoint region IDs, activated connection ID, passage state, flow limit/resistance, and topology revision-before.
3. Grid/topology applies the mutation to the dynamic topology overlay or effective topology representation.
4. Grid/topology advances the effective topology revision and records topology revision-after.
5. Gas reads the new effective topology after the topology revision has advanced.
6. Gas tick processes the new connection according to passage state and flow limit/resistance.
7. Debug/validation surfaces observe the activation, topology revision change, and first Gas read/tick using the new topology.
8. Player/actor exposure surfaces may read the resulting topology/exposure state, but do not own breach activation.

Gas must not read the breach as active before the effective topology mutation is complete.

### 6.7 Gas flow after new opening

Gas does not own breach activation.

Gas owns only its normal simulation response after it reads the effective topology revision containing the activated connection.

After the breach/new-opening topology mutation is applied:

- Gas may treat the activated connection as a valid flow path if the initial passage state is open, available, leaking, partially open, or otherwise passable.
- Gas must respect the initial flow limit or resistance value exposed by the topology/breach activation record.
- Gas may later contribute events such as pressure, heat, reaction, or explosion-like signals, but those signals must be consumed by a future destructibility/material/barrier writer boundary before topology mutates.
- Gas must not infer destructibility semantics from the opening.
- Gas must not decide whether a breach exists.
- Gas must not create, close, remove, split, merge, or otherwise mutate topology connections or regions.
- Gas must not require debris, damage, visual destruction, structural collapse, or explosion pressure-wave data to flow through the new opening.

The compatibility requirement is satisfied when Gas can observe and respond to the updated effective topology in a deterministic, debug-visible order.

### 6.8 Cross-system ownership and non-ownership rules

Ownership boundaries:

- Future destructibility writer boundary owns the decision that a breach, new opening, barrier change, or other topology-relevant destruction result is activated.
- Future material/barrier systems may own material-layer, integrity, pressure-resistance, heat-resistance, or permeability decisions before topology mutation.
- Grid/topology owns the representation of regions, connections, endpoint region IDs, topology mutation, dynamic topology overlay, effective topology revision, and passage/flow metadata exposed to Gas.
- Gas owns simulation through the effective topology after the mutation is applied.
- Debug/validation owns observability of activation, mutation, Gas read order, and cross-system record consistency.
- Player/actor exposure may observe resulting exposure or reachability effects, but does not create, own, or directly author breach behavior in this block.

Non-ownership rules:

- Gas must not activate breaches or directly mutate topology.
- Player/actor interaction must not directly create or own breach behavior in this block.
- Debug tools may trigger or inspect validation activations, but this must remain a validation surface, not production destructibility design.
- Cross-system interaction records may include breach activation, but they must not become the final destruction networking or gameplay-authority model.

### 6.9 Player/actor exposure compatibility note

Player/actor systems may need to observe that a new opening changes exposure, accessibility, line-of-effect, environmental risk, or reachability after topology mutation.

For Section 6, the requirement is limited to compatibility:

- player/actor exposure surfaces can read the post-mutation effective topology or derived exposure result;
- they can observe that the breach/new opening exists after the topology update;
- they can observe future-compatible states such as blocked, leaking, partially open, obstructed, or open when those states are exposed by topology;
- they do not decide that the breach exists;
- they do not author the connection;
- they do not own the activation record;
- they do not require player knockdown, explosion impulse, debris collision, or final destructible interaction logic.

Any future player-caused destruction is outside this block and must be handled by a later accepted destructibility design.

### 6.10 Debug and validation observability requirements

Debug/validation must be able to show or assert:

- breach placeholder ID;
- endpoint region IDs;
- activated connection ID;
- initial passage state;
- initial flow limit or resistance;
- topology revision before activation;
- topology revision after activation;
- whether effective topology includes the new connection;
- when Gas first reads the post-mutation topology revision;
- whether Gas flow through the new opening is possible under the exposed passage/flow metadata;
- whether player/actor exposure surfaces see the post-mutation state only after topology update;
- whether the breach/new-opening event is present in cross-system interaction records;
- whether the event shape remains compatible with future runtime topology mutation records rather than a breach-only special case.

Validation should fail if:

- activation does not advance topology revision;
- the activated connection lacks endpoint regions;
- Gas reads stale topology after activation;
- Gas owns, creates, closes, removes, splits, merges, or directly mutates topology;
- player/actor interaction directly creates or owns breach behavior;
- the block requires damage, debris, structural collapse, explosion pressure wave, final visual destruction, or final destruction networking;
- the breach/new-opening representation prevents future mutation types from using the same topology mutation boundary.

### 6.11 Explicit non-goals

This block explicitly excludes:

- full destructibility implementation;
- final destructibility architecture;
- final runtime topology mutation architecture;
- final damage model;
- final material-layer simulation;
- debris physics;
- fragment simulation;
- structural collapse;
- explosion pressure wave as a required first-nucleus feature;
- player knockdown;
- final visual destruction;
- final destruction networking;
- arbitrary runtime wall cutting;
- final region split/merge implementation;
- final Gas architecture;
- final Grid/topology architecture;
- final network replication model;
- Unity scene creation;
- implementation or code generation;
- old-code audit or transfer as the basis for requirements.

### 6.12 Dependency outputs for Section 7 validation/demo requirements

This block provides the following dependency outputs for the later validation/demo requirements section:

- validation can include a controlled breach/new-opening activation;
- validation can verify that a breach placeholder exists before activation;
- validation can verify activation record completeness;
- validation can verify topology revision-before and revision-after;
- validation can verify that the effective topology contains the activated connection after mutation;
- validation can verify that Gas reads the new effective topology after the topology revision advances;
- validation can verify that Gas may flow through the new opening when the opening is passable under the initial passage state and flow limit/resistance;
- validation can verify that debug surfaces expose the activation and update order;
- validation can verify that player/actor exposure reads the post-mutation topology/exposure state without owning breach activation;
- validation can verify that the breach/new-opening shape is compatible with broader future topology mutation records;
- validation must not require full destructibility, debris, structural collapse, explosion pressure wave, player knockdown, final visual destruction, final destruction networking, Unity implementation, or old-code transfer.

### 6.13 Sections 7–8 remain blocked

Completing this Section 6 block does not complete Section 7 validation/demo requirements and does not complete Section 8 synthesis.

Sections 7–8 remain blocked until this destructibility compatibility boundary is applied, read-back verified, and the next gated execution slice is launched through the proper route.

## 7. Validation / Demo Requirements

### 7.1 Purpose and Boundary

The Validation / Demo Requirements block defines how the first technical nucleus must be proven observable before implementation planning proceeds.

Validation is not an implementation plan, Unity scene plan, test harness design, networking plan, player-health plan, or final architecture. It is a requirements surface for what the first technical nucleus must be able to demonstrate once implemented.

This section validates that the accepted gas, level/spatial, Grid/topology, cross-system interaction, and destructibility compatibility requirements can be observed through controlled scenarios, debug surfaces, pass/fail assertions, and no-player validation flows.

Section 7 completes only the validation/demo requirements block. Section 8, synthesis, remains blocked until this block is accepted and formalized.

### 7.2 Validation Principles

1. Validation must be observable before production gameplay is layered on top.
2. Validation must be possible without player mechanics.
3. Validation must use small controlled spatial surfaces before any larger stress surface.
4. Validation must expose effective topology, not only base topology.
5. Validation must show update order where cross-system changes affect gas behavior.
6. Validation must distinguish source behavior, transfer behavior, modifier behavior, sink/removal behavior, and read-only exposure behavior.
7. Validation must include breach/new-opening compatibility without requiring full destruction.
8. Validation must show debug telemetry sufficient to diagnose why a pass/fail result occurred.
9. Validation must avoid finalizing exact Gas, Grid/topology, networking, destructibility, or player-health architecture.

### 7.3 Scenario Record Template

Every validation/demo scenario must be recorded with this shape:

- `id`
- `purpose`
- `required_prior_blocks`
- `spatial_surface`
- `topology_surface`
- `system_interaction_surface`
- `observable_debug_outputs`
- `pass_condition`
- `fail_condition`
- `explicit_non_goals`

### 7.4 Minimum Validation / Demo Scenario Set

#### VD_01_simple_propagation

- `id`: VD_01_simple_propagation
- `purpose`: Validate baseline gas propagation from a source through a simple connected space.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Level and Spatial Requirements
  - Grid / Topology Substrate Requirements
- `spatial_surface`: MTS_01 simple connected room chain or equivalent room-to-corridor-to-room surface.
- `topology_surface`: Region inventory, connection inventory, stable region/connection IDs, effective topology snapshot.
- `system_interaction_surface`: Gas source activation and gas tick progression only.
- `observable_debug_outputs`:
  - gas type presence
  - concentration or mass per region
  - source state and source rate
  - flow arrows or transfer rates between connected regions
  - region IDs
  - connection IDs
  - gas tick ID
- `pass_condition`: Gas appears at the source region, propagates only through passable connections, and concentration/mass changes are visible per tick in expected connected regions.
- `fail_condition`: Gas appears in disconnected regions, does not propagate through valid open connections, lacks visible concentration/mass, or cannot be traced by region/connection ID.
- `explicit_non_goals`:
  - no player actor required
  - no hazard damage
  - no final gas taxonomy
  - no final gas algorithm selection
  - no production performance benchmark

#### VD_02_closed_door_then_open_door_flow

- `id`: VD_02_closed_door_then_open_door_flow
- `purpose`: Validate that passage state changes affect gas transfer through effective topology.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Grid / Topology Substrate Requirements
  - Cross-System Interaction Requirements
- `spatial_surface`: Two rooms or room-corridor-room with a controllable door/opening.
- `topology_surface`: Base connection, passage state, effective topology snapshot before and after state change, topology revision.
- `system_interaction_surface`: Door/opening state change occurs before the next gas tick.
- `observable_debug_outputs`:
  - open/closed passage state
  - topology revision before and after state change
  - effective topology snapshot
  - gas tick ID
  - flow arrows/rates
  - concentration/mass per region
  - cross-system interaction record for door/opening change
- `pass_condition`: Gas does not flow through the closed passage; after the passage opens and topology revision advances, gas may flow through that connection on the subsequent gas tick.
- `fail_condition`: Gas flows through a closed passage, fails to flow through an open passable connection, or gas reads stale topology after the passage-state change.
- `explicit_non_goals`:
  - no final door implementation
  - no animation requirements
  - no network authority model
  - no player interaction requirement

#### VD_03_vertical_light_heavy_neutral_behavior

- `id`: VD_03_vertical_light_heavy_neutral_behavior
- `purpose`: Validate vertical relation handling for light, heavy, and neutral gas behavior.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Level and Spatial Requirements
  - Grid / Topology Substrate Requirements
- `spatial_surface`: MTS_03 vertical shaft or two-level space with at least upper/lower connected regions.
- `topology_surface`: Vertical relation between connected regions, connection IDs, effective topology snapshot.
- `system_interaction_surface`: Gas type or gas behavior category is visible enough to classify light/heavy/neutral movement expectations.
- `observable_debug_outputs`:
  - gas type/category presence
  - vertical relation marker
  - region IDs for upper/lower regions
  - connection IDs
  - concentration/mass by region over ticks
  - flow direction indicators
  - gas tick ID
- `pass_condition`: Light, heavy, and neutral gas behavior can be distinguished through observable vertical distribution or transfer tendencies according to the accepted requirement level.
- `fail_condition`: Vertical relation is not visible, gas behavior cannot be distinguished, or gas movement ignores the vertical relation in a way that invalidates the requirement.
- `explicit_non_goals`:
  - no final fluid simulation model
  - no exact gas chemistry
  - no full environmental reaction system
  - no production balancing

#### VD_04_ventilation_path_clearance

- `id`: VD_04_ventilation_path_clearance
- `purpose`: Validate that vent availability, clearance, source/sink state, and removal behavior can affect gas behavior before the relevant gas tick.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Level and Spatial Requirements
  - Cross-System Interaction Requirements
- `spatial_surface`: MTS_02 ventilation clearance path space or equivalent source-to-vent/sink path.
- `topology_surface`: Region and connection inventory, vent availability state, effective topology snapshot when vent availability changes.
- `system_interaction_surface`: Vent availability change, scrubber/sink removal rate, optional fan/airflow bias if present as modifier.
- `observable_debug_outputs`:
  - vent availability
  - sink/scrubber state
  - removal rate
  - source state and source rate
  - flow arrows/rates
  - concentration/mass per region
  - cross-system interaction records
  - gas tick ID
- `pass_condition`: Changing vent/sink availability or removal rate visibly affects gas distribution/removal according to the accepted requirement before or on the next relevant gas tick.
- `fail_condition`: Vent/sink state is not observable, clearance has no visible effect, or gas behavior uses stale availability data.
- `explicit_non_goals`:
  - no final ventilation architecture
  - no final fan simulation
  - no production HVAC system
  - no Unity scene implementation requirement

#### VD_05_multi_room_capacity_stress

- `id`: VD_05_multi_room_capacity_stress
- `purpose`: Validate that the gas/topology/debug surface remains observable under a modest multi-room stress case.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Level and Spatial Requirements
  - Grid / Topology Substrate Requirements
- `spatial_surface`: MTS_04 optional larger stress space or a small multi-room chain/cluster.
- `topology_surface`: Multiple regions, multiple connections, stable IDs, effective topology snapshot, concentration/mass per region.
- `system_interaction_surface`: Multiple source/sink or source/transfer observations, without requiring full cross-system stack.
- `observable_debug_outputs`:
  - gas concentration/mass per region
  - gas type presence
  - source/sink state
  - flow arrows/rates across multiple connections
  - region IDs
  - connection IDs
  - effective topology snapshot
  - gas tick ID
- `pass_condition`: The scenario remains diagnosable: gas movement, mass/concentration distribution, and topology path behavior can be inspected across multiple rooms without ambiguous debug output.
- `fail_condition`: Debug output becomes unreadable, IDs cannot be correlated, mass/concentration cannot be inspected, or effective topology cannot explain observed flow.
- `explicit_non_goals`:
  - no production-scale performance benchmark
  - no final level size target
  - no stress automation
  - no multiplayer validation

#### VD_06_cross_system_modifier_validation

- `id`: VD_06_cross_system_modifier_validation
- `purpose`: Validate that cross-system modifiers can influence gas without owning gas simulation authority.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Cross-System Interaction Requirements
  - Grid / Topology Substrate Requirements
- `spatial_surface`: Minimal connected room/vent/path surface that can expose modifier effects.
- `topology_surface`: Effective topology snapshot plus visible modifier target region/connection.
- `system_interaction_surface`:
  - door/opening state change
  - vent availability change
  - source/emitter rate
  - sink/removal rate
  - fan/airflow bias
  - valve flow limit
  - hazard source activation boundary
  - optional temperature/environment hook visibility
  - conflict-resolution output for shared targets
- `observable_debug_outputs`:
  - cross-system interaction records
  - conflict records for shared targets
  - modifier type and target
  - pre-gas-tick update order
  - gas tick ID
  - source/sink state
  - flow arrows/rates
  - concentration/mass per region
- `pass_condition`: At least one source, one sink/removal, one passage/availability, and one transfer modifier can be observed affecting gas behavior in the required update order without becoming the gas owner.
- `fail_condition`: Modifier effects are invisible, update order is ambiguous, gas ownership is implied by non-gas systems, or conflicts on shared targets cannot be diagnosed.
- `explicit_non_goals`:
  - no final event bus
  - no final cross-system architecture
  - no full fire/temperature reaction system
  - no production hazard system

#### VD_07_breach_new_opening_compatibility_validation

- `id`: VD_07_breach_new_opening_compatibility_validation
- `purpose`: Validate compatibility with controlled breach/new-opening activation without requiring full destructibility.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Grid / Topology Substrate Requirements
  - Cross-System Interaction Requirements
  - Destructibility Compatibility Boundary
- `spatial_surface`: Two adjacent regions separated by a non-passable boundary with a predefined breach placeholder.
- `topology_surface`: Breach placeholder marker, activation record, topology revision before/after activation, effective topology snapshot after mutation, activated connection ID.
- `system_interaction_surface`: Controlled activation of a predefined breach/new opening before gas reads topology.
- `observable_debug_outputs`:
  - breach placeholder state
  - activation record completeness
  - topology revision before and after activation
  - new/activated connection ID
  - effective topology snapshot
  - gas tick ID
  - flow arrows/rates through new opening
  - concentration/mass per region
  - cross-system update-order record
- `pass_condition`: Before activation, gas cannot use the placeholder as a passable connection. After controlled activation, topology revision advances, effective topology includes the new passable connection, and gas may flow through it on the post-mutation gas read.
- `fail_condition`: Gas uses an inactive placeholder, the activation record is incomplete, topology revision does not advance, effective topology omits the activated connection, or gas reads stale topology after activation.
- `explicit_non_goals`:
  - no full destruction simulation
  - no voxel/mesh destruction requirement
  - no damage model
  - no player breach tool
  - no final destructibility architecture

#### VD_08_player_actor_exposure_read_surface_validation_optional_boundary_only

- `id`: VD_08_player_actor_exposure_read_surface_validation_optional_boundary_only
- `purpose`: Validate that a player/actor exposure read surface can observe post-mutation gas/topology state without requiring player health implementation.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Cross-System Interaction Requirements
  - Destructibility Compatibility Boundary
- `spatial_surface`: Any prior validation surface with a readable actor sample point or placeholder actor region.
- `topology_surface`: Current effective topology snapshot, region ID at actor/sample location, gas concentration/mass at that region.
- `system_interaction_surface`: Read-only exposure query after gas tick and after topology mutation where relevant.
- `observable_debug_outputs`:
  - optional player/actor exposure read surface
  - sampled region ID
  - sampled gas type and concentration/mass
  - gas tick ID
  - topology revision used for read
  - breach/new-opening state if relevant
- `pass_condition`: A read-only actor exposure query can report gas exposure from the current post-mutation state without requiring health, damage, inventory, animation, or player-controller mechanics.
- `fail_condition`: Exposure reads require player-health implementation, read stale topology/gas state, or cannot report the region/topology revision used.
- `explicit_non_goals`:
  - no player health
  - no damage rules
  - no player controller
  - no networked player replication
  - no gameplay balancing

#### VD_09_debug_telemetry_validation_surface

- `id`: VD_09_debug_telemetry_validation_surface
- `purpose`: Validate that the required debug and telemetry surfaces are sufficient to diagnose all prior scenarios.
- `required_prior_blocks`:
  - Gas Simulation Capability Frame
  - Level and Spatial Requirements
  - Grid / Topology Substrate Requirements
  - Cross-System Interaction Requirements
  - Destructibility Compatibility Boundary
- `spatial_surface`: Any minimum validation scenario plus at least one multi-surface scenario involving topology state change or modifier state.
- `topology_surface`: Region inventory, connection inventory, passage states, effective topology snapshot, topology revision, breach placeholder/activation state where relevant.
- `system_interaction_surface`: Source/sink/modifier records, update-order records, conflict records.
- `observable_debug_outputs`:
  - gas concentration/mass
  - gas type presence
  - source/sink state
  - flow arrows/rates
  - region IDs
  - connection IDs
  - passage state
  - vent availability
  - vertical relation
  - topology revision
  - gas tick ID
  - cross-system interaction records
  - conflict records
  - breach placeholder / activated connection
  - optional player/actor exposure read surface
- `pass_condition`: The full required telemetry set can explain observed gas behavior, topology state, modifier effects, update order, and breach/new-opening activation without hidden assumptions.
- `fail_condition`: Any required telemetry category is missing, stale, ambiguous, or insufficient to diagnose pass/fail results for scenarios VD_01 through VD_08.
- `explicit_non_goals`:
  - no final debug UI design
  - no production telemetry stack
  - no automated test framework
  - no logging format finalization

### 7.5 Required Debug / Observable Surfaces

The first technical nucleus validation surface must expose at minimum:

- gas concentration or mass per region;
- gas type presence;
- source state and source rate;
- sink/scrubber/removal state and removal rate;
- flow arrows or transfer rates;
- region IDs;
- connection IDs;
- passage open/closed state;
- vent availability;
- vertical relation between relevant regions;
- effective topology snapshot;
- topology revision;
- gas tick ID;
- cross-system interaction records;
- conflict records for shared targets;
- breach placeholder state;
- activated breach/new-opening connection ID when relevant;
- optional player/actor exposure read surface.

These surfaces may be debug overlays, logs, inspectors, exported records, or equivalent observable evidence. The requirement is observability, not a final UI implementation.

### 7.6 Required Validation Assertions

Validation must be able to assert at least:

1. Gas source creates gas in the intended source region.
2. Gas transfers through open/passable connections.
3. Gas does not transfer through closed/non-passable passages.
4. A door/opening state change is applied before the gas tick that should read it.
5. Light/heavy/neutral gas behavior can be distinguished on a vertical surface.
6. Vent availability and sink/removal state affect gas distribution/removal.
7. Cross-system modifiers affect gas without owning gas simulation authority.
8. Shared-target conflicts produce visible conflict records.
9. Topology revision advances after controlled topology mutation.
10. Effective topology contains activated breach/new-opening connection after mutation.
11. Gas reads the post-mutation effective topology after topology revision advances.
12. A breach/new opening remains placeholder-only until controlled activation.
13. Optional actor exposure reads can read post-mutation gas/topology state without requiring player health implementation.
14. Debug/validation reads identify which topology revision and gas tick they used.

### 7.7 No-Player Validation Requirements

No-player validation remains required.

The validation/demo set must be runnable or inspectable without:

- player controller;
- player input;
- player inventory;
- player health/damage;
- player animation;
- networked player replication;
- playable mission flow.

Player/actor exposure is allowed only as a read-only boundary surface. It must not pull player mechanics into the technical nucleus validation requirement.

### 7.8 Demo Boundaries and Non-Goals

This validation/demo block does not require:

- implementation;
- Unity scene creation;
- code generation;
- test harness implementation;
- old-code audit or transfer;
- final Gas architecture;
- final Grid/topology architecture;
- final cross-system architecture;
- full destructibility;
- final networking;
- player health/damage systems;
- visual polish;
- production debug UI;
- Game Documentation promotion;
- Codex product/project execution;
- Task Master graph creation.

### 7.9 Dependency Outputs for Synthesis

This section contributes the following synthesis inputs for Section 8:

- The first technical nucleus must include enough observable state to validate gas propagation, topology state, cross-system modifiers, controlled breach/new-opening compatibility, and optional exposure reads.
- The minimum validation set is scenario-driven, not implementation-driven.
- Debug surfaces are acceptance requirements, not optional polish.
- No-player validation is a hard boundary for the first validation layer.
- Breach/new-opening compatibility is required only as controlled placeholder activation and post-mutation topology/gas read behavior.
- Cross-system validation is required only at the boundary/modifier/update-order level, not as final architecture.
- Section 8 may synthesize the nucleus requirements only after Section 7 is accepted and formalized.

### 7.10 Section 8 Status

Section 8 remains blocked until Section 7 is accepted, formalized, applied, read back, diff-verified, and commit-verified.

## 8. Synthesis

Status: `synthesis_formalized`

### 8.1 Purpose and Boundary

This synthesis integrates the accepted prior blocks into one coherent first technical nucleus functional specification.

The first technical nucleus is a requirements-and-validation definition for the minimum durable technical foundation where gameplay gas, spatial layout, topology, cross-system modifiers, breach/new-opening compatibility, and observable validation can exist together.

This synthesis is not an implementation plan, Unity scene plan, Codex execution brief, test harness design, final architecture decision, or Game Documentation promotion.

The synthesis preserves these boundaries:

- the nucleus must be gameplay-directed, not gas-only;
- the nucleus must be observable through no-player validation before player mechanics are layered on top;
- Gas, topology, cross-system interaction, and breach/new-opening compatibility must remain separated by explicit ownership boundaries;
- implementation remains blocked until later execution planning, project/tool bindings, validators, and explicit execution envelope are approved;
- old project material remains reference/evidence only after requirements are clear and must not dictate implementation or transfer decisions.

### 8.2 Integrated Requirement Stack

The first technical nucleus is defined by the following accepted stack.

#### Gas layer

The nucleus must support gameplay-relevant gas behavior: propagation through bounded spaces, accumulation and clearing, density-biased vertical behavior, source/sink behavior, topology-sensitive behavior, and debug-observable hazard state.

Gas is modeled at requirement level as typed mass or concentration distributed across spatial containers. Heavy, light, and neutral behavior use a continuous density coefficient with named validation bands. The first validation set may use heavy hazard gas, light hazard gas, and neutral obscuring/asphyxiant gas.

Gas requires simplified mass/capacity/flow behavior, source and sink rates, connection flow limits, and pressure-like gradients, but not full CFD, compressible pressure simulation, fire chemistry, shockwaves, structural collapse, final replication, or player abilities.

#### Spatial layer

The nucleus requires a compact validation space, not final level design.

Required spatial surfaces are:

- simple connected room chain;
- ventilation / clearance path space;
- vertical shaft or two-level space;
- optional larger stress space after simple validation passes.

These spaces must expose source anchors, sink/vent anchors, toggleable openings, permanent openings, vertical lower/upper anchors, observation/debug points, and optional breach/new-opening placeholders.

The simple validation space must stay small enough that failure can be diagnosed from spatial configuration rather than map complexity.

#### Grid / topology layer

The nucleus requires a gas-readable topology substrate, not final Grid architecture.

The topology substrate must represent:

- stable spatial region IDs;
- stable connection/portal IDs;
- passage state IDs;
- door/opening IDs;
- vent path IDs;
- source/sink anchor IDs;
- observation point IDs;
- breach placeholder IDs;
- topology revision IDs.

Gas must read effective topology, not only base topology. Effective topology combines base layout, passage-state overlay, vent-availability overlay, and dynamic mutation placeholder overlay.

Topology must support compact snapshot/event/delta surfaces in principle, but this synthesis does not decide bandwidth strategy, prediction, rollback, transport serialization, interest management, or final replication schema.

#### Cross-system layer

The nucleus must make cross-system interaction explicit enough to avoid hidden coupling.

Systems may interact through requirement-level state changes, commands/requests, modifiers, and signals/events. Each interaction record must expose source system, target owner, target ID, interaction type, payload summary, tick/revision, authority/scope, and debug visibility.

The accepted update order is:

1. collect commands, state changes, and modifier inputs;
2. resolve owning-system state;
3. resolve effective topology and modifier state;
4. gas reads effective state;
5. gas simulation tick runs;
6. optional player/actor effect consumers read exposure;
7. debug, validation, and UI/telemetry read observable state.

Gas owns gas state and gas metrics. It does not own topology, doors/openings, vent availability, breach activation, source/sink ownership, player health, final effects, or final network state.

#### Destructibility compatibility layer

The nucleus does not implement full destructibility.

It must be compatible with a future breach/new-opening writer boundary by supporting:

- an addressable breach placeholder;
- controlled breach/new-opening activation;
- activated connection ID;
- endpoint region IDs;
- initial passage state;
- initial flow limit or resistance;
- topology revision before and after activation;
- Gas reading the post-mutation effective topology only after the topology revision advances;
- debug/validation observability of the activation, update order, and resulting flow.

The breach/new-opening shape must remain compatible with broader future topology mutation records and must not become a breach-only special case.

#### Validation / demo layer

The nucleus must be validated through observable scenarios and debug surfaces, not through implementation claims.

Minimum validation scenarios:

- `VD_01_simple_propagation`
- `VD_02_closed_door_then_open_door_flow`
- `VD_03_vertical_light_heavy_neutral_behavior`
- `VD_04_ventilation_path_clearance`
- `VD_05_multi_room_capacity_stress`
- `VD_06_cross_system_modifier_validation`
- `VD_07_breach_new_opening_compatibility_validation`
- `VD_08_player_actor_exposure_read_surface_validation_optional_boundary_only`
- `VD_09_debug_telemetry_validation_surface`

The validation layer must preserve no-player validation as the first hard boundary. Player/actor exposure is allowed only as a read-only boundary surface unless a later valid stage explicitly routes player mechanics into scope.

### 8.3 Coherent First Technical Nucleus Definition

The first technical nucleus is:

> A minimal, durable, no-player-observable technical requirements nucleus where typed gameplay gas moves through a small authored spatial/topology substrate, reads effective topology and explicit modifier/state surfaces, responds to controlled topology changes such as door/vent state and breach/new-opening activation, and exposes enough debug/validation telemetry to prove correctness before implementation, player mechanics, final networking, final architecture, or Game Documentation promotion.

This definition intentionally includes gas, space, topology, cross-system ownership, breach compatibility, and validation together. It is not a gas-only prototype and not a final game slice.

### 8.4 First Technical Nucleus Capability Summary

The first technical nucleus must be capable of demonstrating:

1. Gas can originate from a named source and become visible as mass/concentration in a source region.
2. Gas can propagate through passable topology connections.
3. Gas can be blocked or materially restricted by closed/non-passable passages.
4. Gas can distinguish light, heavy, and neutral vertical behavior at requirement level.
5. Gas can accumulate, clear, or be removed through source/sink/vent surfaces.
6. Stable topology IDs can connect gas state, debug surfaces, validation assertions, and future host-authoritative snapshots.
7. Effective topology can differ from base topology through passage state, vent availability, and controlled mutation overlays.
8. Cross-system modifiers can affect Gas without owning Gas.
9. Shared-target conflicts can be diagnosed through visible conflict records.
10. A breach/new-opening placeholder can become a passable connection only through controlled activation and topology revision advancement.
11. Gas reads post-mutation topology after topology update, not before.
12. Optional player/actor exposure reads can observe resulting gas/topology state without requiring player health, damage, inventory, animation, controller, or replication mechanics.
13. Debug/validation telemetry can explain pass/fail outcomes for scenarios `VD_01` through `VD_09`.

### 8.5 Required Validation Surface Summary

The required validation surface must expose at minimum:

- gas concentration or mass per region;
- gas type presence;
- source state and source rate;
- sink/scrubber/removal state and removal rate;
- flow arrows or transfer rates;
- region IDs;
- connection IDs;
- passage open/closed state;
- vent availability;
- vertical relation;
- effective topology snapshot;
- topology revision;
- gas tick ID;
- cross-system interaction records;
- conflict records;
- breach placeholder state;
- activated breach/new-opening connection ID when relevant;
- optional player/actor exposure read surface.

Validation must be scenario-driven and pass/fail observable. Debug surfaces are acceptance requirements, not optional polish.

### 8.6 Implementation Readiness Boundary

This specification makes the parent Goal reviewable, but it does not authorize implementation.

Before any code, Unity project work, Codex product/project execution, Task Master graph, or durable nucleus implementation, later workflow stages must still establish:

- execution route;
- concrete project/tool bindings;
- allowed and forbidden product/project paths;
- validators and validation commands;
- Codex execution envelope;
- implementation slice boundaries;
- project-local architecture and module boundaries;
- read-back, diff, validation, and evidence requirements.

This synthesis is sufficient to review the first technical nucleus functional specification. It is not sufficient to begin product/project mutation.

### 8.7 Explicit Non-Goals Preserved

This synthesis preserves the following non-goals:

- no Unity bootstrap;
- no Unity scene creation;
- no implementation;
- no code generation;
- no test harness implementation;
- no Codex product/project execution;
- no Task Master graph creation;
- no direct old-code transfer;
- no old-code audit as the starting point;
- no final Gas architecture;
- no final Grid/topology architecture;
- no final cross-system architecture;
- no final event-bus architecture;
- no final network replication model;
- no final destructibility architecture;
- no full destructibility implementation;
- no full fire/reaction chemistry;
- no full temperature or pressure simulation;
- no player controller, player health, damage, inventory, animation, or gameplay balancing;
- no visual polish or production debug UI;
- no Game Documentation promotion.

### 8.8 Unresolved or Deferred Items

The following remain unresolved or deferred by design:

- final Gas architecture and data structures;
- final Grid/topology architecture and cell/region/chamber model;
- old Grid/GridV2/GasV2R reuse, rewrite, or discard classification;
- final host-authoritative replication model;
- final bandwidth, prediction, rollback, serialization, and interest-management strategy;
- final cross-system implementation mechanism;
- final event/message architecture;
- final destructibility implementation and topology mutation architecture;
- final player-facing hazard/effect rules;
- exact Unity folder structure, DI package, CI setup, and validators;
- project bootstrap/tool-binding readiness;
- Codex product/project execution planning;
- Game Documentation promotion.

These items may be routed later only through valid lifecycle stages and explicit approval.

### 8.9 Parent Goal Completion Candidate Marker

```yaml
parent_goal_completion_candidate:
  state: candidate_after_f0_apply_readback
  artifact: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md
  completed_blocks:
    - gas_simulation_capability_frame
    - user_approval_gate_after_gas_block
    - level_and_spatial_requirements
    - grid_topology_substrate_requirements
    - cross_system_interaction_requirements
    - destructibility_compatibility_boundary
    - validation_demo_requirements
    - synthesis
  completion_scope: parent_goal_complete_after_apply_readback_diff_commit_main_verification
  parent_goal_completion_state: complete_after_apply_readback_diff_commit_main_verification
  review_route_after_successful_f0_verification: R1_GOAL_REVIEW_DISTILL
```

This marker becomes effective only after this Section 8 synthesis is applied, read back, diff-verified, commit-verified, and integrated to `main`.

Before that evidence exists, the parent Goal remains open and F0 must not route to R1.

### 8.10 Next Review Route After Successful Apply / Read-Back

After Section 8 synthesis is approved, applied, read back, diff-verified, commit-verified, and integrated to `main`, the next valid route is:

```yaml
next_stage_after_successful_synthesis_apply_readback: R1_GOAL_REVIEW_DISTILL
reason: >
  The completed artifact becomes reviewable as the parent Goal outcome only
  after the final synthesis block is repository-verified.
```

R1 must review the whole parent Goal outcome against the Goal Contract and acceptance floor. R1 must not assume unrefreshed Project Files are canonical.

### 8.11 Phase Progress Gate and Documentation Promotion Boundary

F0 does not run the Phase Progress Gate.

The Phase Progress Gate remains blocked until R1 accepts, rejects, or route-gates the parent Goal outcome.

This synthesis does not promote any durable truth into Game Documentation. Any Game Documentation promotion requires a later explicit documentation-maintenance stage or approved documentation-maintenance patch.

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
