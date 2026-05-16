# Goal Contract — First Technical Nucleus Functional Spec

```yaml
artifact_control:
  artifact_name: "Goal Contract — First Technical Nucleus Functional Spec"
  schema: goal_contract.v1
  owner_layer: persistence
  status: active_goal_contract
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: first-technical-nucleus-functional-spec
  shaped_by_stage: G1_GOAL_SHAPE
  formalized_at: "2026-05-16"
  next_stage: E1_EXECUTION_BRIEF
  execution_model: single_parent_goal_with_gated_sequential_execution
```

## Goal identity

- Goal ID: `first-technical-nucleus-functional-spec`
- Title: `Сформировать функционально-техническую спецификацию первого technical nucleus`
- Direction: `Indie Game Development`
- Phase: `Core Co-op Technical Foundation Selection`
- Initiative: `innovative-commercial-expedition-gas-sim-game`
- Active horizon: `H1_playable_technical_nucleus`
- Next route: `E1_EXECUTION_BRIEF`

## Reset rationale

The previous active Goal, `grid-gas-transfer-boundary-audit`, was misframed after human clarification.

Direct old-code transfer is out of scope.

Old Grid/Gas material is not the starting point for implementation or transfer classification. It may be used later only as targeted reference/evidence after the new game's requirements are clear.

Allowed later use of old material:

- architectural ideas;
- algorithms;
- invariants;
- tests;
- failure modes;
- coupling patterns to avoid.

Not allowed:

- direct code transfer;
- starting from transfer/reuse/discard classification;
- letting old code dictate new requirements;
- requesting old source/tests unless a later block has a targeted question.

## WHAT

Сформировать reviewable функционально-техническую спецификацию первого technical nucleus
для новой co-op gas/3D-space game.

Спецификация должна определить, что первый meaningful technical nucleus обязан уметь across:

- gameplay gas simulation;
- level/spatial needs;
- Grid/topology substrate;
- cross-system interaction;
- minimal future-compatible destructibility boundary;
- validation/demo scenarios.

## WHY now

The active Direction is moving toward `H1_playable_technical_nucleus`.

The old transfer-boundary audit asks the wrong first question. The new game needs a requirements-first capability frame before any old project reference review or implementation planning.

Codex can generate implementation later only if the capability frame, module boundaries, validation surfaces, and execution gates are clear.

## DONE

DONE наступает, когда принят один coherent Goal-level specification artifact, который:

1. фиксирует gas simulation capability frame;
2. содержит explicit human approval gate after gas block;
3. после принятого gas frame определяет level/spatial requirements;
4. затем определяет Grid/topology substrate requirements;
5. затем определяет cross-system interaction requirements;
6. задаёт minimal future-compatible destructibility boundary;
7. задаёт validation/demo requirements;
8. явно запрещает direct old-code transfer and premature implementation;
9. достаточно ясен для `E1_EXECUTION_BRIEF`, чтобы спланировать gated sequential execution.

## Acceptance floor

- One broad parent Goal, not separate active Goals for Gas, Grid, and Destructibility.
- Gas-first sequencing.
- User approval gate after `gas_simulation_capability_frame`.
- No direct old-code transfer.
- Old project material only as targeted reference after requirements are clear.
- Observable validation/demo surfaces before implementation.
- Clear non-goals and scope cuts.
- Next route to `E1_EXECUTION_BRIEF`.

## Required internal sequence

### Block 1 — `gas_simulation_capability_frame`

Purpose: define gameplay gas simulation requirements first.

Must be reviewed and accepted by the user before the next block proceeds.

Required questions:

- What gas behaviors are gameplay-interesting?
- What gas types/properties are needed?
- Heavy/light/neutral categories or continuous density coefficient?
- How should gas spread through rooms, corridors, shafts, vents, openings?
- Are pressure/mass/capacity/flow models required in the first nucleus?
- Are mixing/reactions/transformations required now, minimal, or future?
- Which 2–3 gas types are enough for first demo validation?
- What simulation debug/visualization is required?
- What can be tested without player first?

### Block 2 — `level_and_spatial_requirements`

Depends on: user-accepted `gas_simulation_capability_frame`.

Purpose: define spaces needed to test gas honestly.

Expected surfaces:

- simple rooms and corridors;
- vertical shafts / two-level spaces;
- ventilation paths;
- small technical rooms;
- long corridor;
- optional larger hangar-like room if useful;
- openings / doors / passages;
- complex test level after simple level.

### Block 3 — `grid_topology_substrate_requirements`

Depends on: `level_and_spatial_requirements`.

Purpose: define Grid/topology substrate under gas and future system needs.

Expected surfaces:

- room/zone/cell/chamber concepts;
- stable IDs for rooms, doors, portals, openings;
- connectivity/passability representation;
- topology mutation/effective topology overlays;
- how other systems read/write spatial effects;
- snapshot/delta implications for host-authoritative co-op.

### Block 4 — `cross_system_interaction_requirements`

Depends on: `grid_topology_substrate_requirements`.

Purpose: define how future systems can influence gas/topology without implementing them now.

Expected systems:

- temperature;
- airflow;
- fans;
- valves;
- doors;
- vents;
- leaks/sources;
- hazards;
- future reactions/fire.

### Block 5 — `destructibility_compatibility_boundary`

Depends on: `grid_topology_substrate_requirements`.

Purpose: define minimal future-compatible destructibility boundary.

Required now:

- opening/breach can appear in topology;
- gas can flow through new opening;
- topology/effective connectivity update order is representable.

Not required now:

- full destruction implementation;
- debris physics;
- fragments knocking players down;
- explosion wave as required nucleus feature;
- structural collapse simulation.

### Block 6 — `validation_demo_requirements`

Depends on:

- user-accepted `gas_simulation_capability_frame`;
- `level_and_spatial_requirements`;
- `grid_topology_substrate_requirements`.

Candidate scenarios:

- no-player simulation demo;
- simple propagation scene;
- vertical shaft scene;
- ventilation path scene;
- complex multi-room scene;
- breach/opening gas-flow scene;
- stress scenario with multiple gases or larger volume.

### Block 7 — `synthesis`

Depends on accepted prior blocks.

Purpose: produce final coherent first technical nucleus functional specification.

## Validation signal

A later E1 run can produce a gated sequential execution brief without guessing:

- gas capability frame first;
- user approval gate;
- then spatial/level needs;
- then Grid/topology;
- then cross-system/destructibility;
- then validation/synthesis.

## Validation method

Validate the Goal output by review, not by implementation.

The accepted specification must be checked against:

- block sequence;
- user approval gate after gas block;
- no-direct-transfer policy;
- scope cuts;
- validation/demo scenarios;
- sufficient clarity for E1 planning.

## Smallest testable slice

First useful internal output: `gas_simulation_capability_frame`.

This is not a toy prototype and not a gas-only active Goal. It is the first gated block inside the single parent Goal.

## Scope in

- Functional capability specification for first technical nucleus.
- Gas-first requirements framing.
- Human approval gate after gas block.
- Spatial/level requirements needed for honest validation.
- Grid/topology substrate requirements derived after gas/spatial needs.
- Cross-system interaction boundary.
- Minimal destructibility compatibility boundary.
- Validation/demo requirements.
- Old project reference policy.

## Non-goals

- No Unity project creation.
- No implementation.
- No Codex product/project execution.
- No Task Master graph.
- No old code transfer.
- No old code audit inside G1.
- No final gas architecture.
- No final Grid/topology architecture.
- No full destructibility architecture.
- No final multiplayer implementation model.
- No Game Documentation promotion.
- No tiny toy-only prototype Goal.

## Scope cuts

- Cut direct legacy `Grid`, `GridV2`, `GasV2R`, and Gas↔Grid transfer classification.
- Cut production-readiness audit of old code.
- Cut final module implementation plan.
- Cut exact Unity folder structure / DI package / CI setup.
- Cut full reaction/fire/destruction model.
- Cut player mechanics unless needed to define validation surfaces.
- Cut commercialization, trailer, Steam, audience testing, and vertical slice planning.

## Deferred candidates

- Targeted old-project reference review after requirements are clear.
- Codex technical discovery after E1/C1 readiness.
- Project bootstrap/tool-binding validation.
- Durable technical nucleus implementation.
- Game Documentation promotion after accepted durable truths exist.

## Escalation triggers

- User wants direct old-code transfer restored.
- User wants separate active Goals for Gas/Grid/Destructibility.
- Gas frame reveals incompatible requirements that make one parent Goal unsafe.
- Grid/topology requirements require external technical research before shaping.
- Destructibility becomes a required implemented feature rather than compatibility boundary.
- Validation cannot be made observable without implementation.

## Constraints

- Single parent Goal.
- Gated sequential execution.
- Gas block must be user-accepted before Grid/topology proceeds.
- Old project material cannot dictate new requirements.
- No implementation in G1 or E1.

## Map binding

```yaml
map_binding:
  initiative_id: innovative-commercial-expedition-gas-sim-game
  node_or_edge: H1_playable_technical_nucleus
  expected_map_delta: >
    Replace current active-front gate from legacy transfer-boundary audit
    to first-technical-nucleus-functional-spec as the repaired foundation
    specification gate.
  why_this_goal_is_minimal: >
    It repairs the misframed audit without jumping to implementation,
    Unity bootstrap, architecture finalization, or code transfer.
  why_not_premature_or_optional_expansion: >
    The active horizon requires gas/grid/co-op nucleus clarity before implementation.
    This Goal defines WHAT/DONE/validation, not final architecture or code.
```

## Close path

After the specification is produced and reviewed, route to `R1_GOAL_REVIEW_DISTILL`
or the appropriate lifecycle stage.

Implementation still requires later E1/C1/C2 readiness, project/tool bindings,
validators, and explicit execution envelope.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md`
