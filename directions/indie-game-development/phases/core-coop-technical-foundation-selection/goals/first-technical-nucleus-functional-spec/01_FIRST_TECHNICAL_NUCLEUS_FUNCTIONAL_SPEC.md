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
