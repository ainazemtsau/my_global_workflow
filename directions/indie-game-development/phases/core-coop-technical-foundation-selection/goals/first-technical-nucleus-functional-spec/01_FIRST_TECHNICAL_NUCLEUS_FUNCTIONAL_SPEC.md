# First Technical Nucleus Functional Specification

```yaml
artifact_control:
  artifact_name: "First Technical Nucleus Functional Specification"
  schema: first_technical_nucleus_functional_spec.v1
  owner_layer: persistence
  status: draft_grid_topology_substrate_requirements_formalized_pending_apply_readback
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: first-technical-nucleus-functional-spec
  source_stage: F0_FAST_DIRECT
  formalized_at: "2026-05-17"
  formalization_trigger: APPROVE_AND_FORMALIZE_F0_GRID_TOPOLOGY_BLOCK
  source_goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md"
  sequencing_model: gated_sequential
  current_completed_block: grid_topology_substrate_requirements
  next_blocks_state: sections_5_to_8_blocked_until_valid_stage_after_apply_readback
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
