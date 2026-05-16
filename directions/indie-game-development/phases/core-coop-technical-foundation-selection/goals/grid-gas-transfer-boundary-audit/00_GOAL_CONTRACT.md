# Goal Contract — Grid/Gas Transfer Boundary Audit

## Supersession note — 2026-05-16

This Goal is superseded after human clarification.

Do not continue this as a transfer/reuse/discard audit.

Direct old-code transfer is out of scope. Old Grid/Gas material may be used later only as targeted reference/evidence after the first technical nucleus requirements are clear.

Superseding active Goal:

`first-technical-nucleus-functional-spec`

```yaml
artifact_control:
  artifact_name: "Goal Contract — Grid/Gas Transfer Boundary Audit"
  schema: goal_contract.v1
  owner_layer: direction_goal
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: grid-gas-transfer-boundary-audit
  status: superseded_after_human_clarification
  superseded_by_goal_id: first-technical-nucleus-functional-spec
  superseded_reason: >
    Direct old-code transfer is out of scope. Old Grid/Gas material is reference/evidence only.
    Requirements for the new game's first technical nucleus must be defined first.
  active_goal: false
  shaped_by_stage: G1_GOAL_SHAPE
  shaped_at: "2026-05-16"
  source_stage_prompt: "workflow/stage_prompts/G1_GOAL_SHAPE.md"
  next_stage: none
  repository_source: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md"
```

## Goal

`grid-gas-transfer-boundary-audit`

## Title

Провести аудит transfer boundary для legacy Grid, GridV2, GasV2R и Gas↔Grid interaction

## WHAT

Run an A1 audit to determine the transfer/rewrite/reference-only boundary for four separate technical surfaces:

- legacy Grid;
- GridV2;
- GasV2R;
- Gas↔Grid interaction.

The audit must evaluate old project evidence against the new game's bounded co-op expedition concept, not against legacy completeness alone.

## WHY now

R1 accepted the Core Technical Foundation Decision Brief as a route-gated decision map. Multiplayer and player-hosted/listen-host architecture are decided at decision-map level, but Grid/Gas/GridV2/GasV2R transfer safety remains unresolved.

The Direction must not proceed to Unity project creation, old code transfer, durable technical nucleus implementation, or Codex product/project execution until this audit resolves or route-gates the transfer boundary.

## DONE

A1 returns an audit result or exact blocker route. The audit result must separately classify each required surface with:

- evidence inspected;
- fit/mismatch against the new game;
- transfer boundary;
- transfer mode;
- confidence;
- blockers;
- recommended next route.

G1 does not perform the audit and does not decide reuse/rewrite verdicts.

## Product-fit transfer policy

```yaml
product_fit_transfer_policy:
  principle: >
    Transfer verdicts must be made against the new game's concept and MVP technical nucleus,
    not against legacy completeness alone.

  new_game_fit_filter:
    - "The new game uses bounded loaded co-op levels, not huge open-world territories."
    - "Expected scale is dozens to hundreds of logical rooms/zones; low thousands may be a stress upper bound, not design default."
    - "Grid is the primary spatial/topology/interaction substrate for multiple simulations and devices."
    - "Gas is a core gameplay simulation, not decorative effect."
    - "T1/source-of-truth gas layer may need to be more detailed than legacy T1 because target levels are smaller."
    - "Future temperature/reactions/devices should not be blocked, but are not implemented in this Goal."
    - "Host-authoritative co-op requires explicit authority/order/snapshot boundaries."

  transfer_modes:
    - direct_code_reuse
    - refactor_and_port
    - rewrite_from_algorithm
    - rewrite_from_spec
    - reference_only
    - discard
    - needs_source_context

  default_bias:
    old_research_and_structures: "preserve as valuable evidence unless contradicted"
    old_code: "do not directly transfer unless source/test inspection proves fit"
    old_large_scale_optimizations: "suspect until proven useful for bounded loaded levels"
```

## Required audit surfaces

```yaml
required_surfaces:
  - legacy_grid
  - gridv2
  - gasv2r
  - gas_grid_interaction

must_keep_separate:
  - "legacy Grid and GridV2 must not be collapsed into one reuse verdict."
  - "GridV2 is not a silent replacement for legacy Grid."
  - "GasV2R is evidence/candidate architecture, not automatically production-ready."
  - "Gas↔Grid interaction requires authority/order/snapshot boundary review."
```

## Grid audit lens

A1 must treat Grid as a possible game-wide interaction substrate, not merely as a gas helper structure.

Required Grid questions:

- Can legacy Grid/GridV2 represent rooms/zones/subzones, large spaces split into regions, corridors, verticality, portals, doors, vents, openings, and stable spatial IDs?
- Can Grid support future devices/events such as fan, valve, door, leak, vent, temperature source, and later simulations?
- Can Grid remain stable enough for host-authoritative snapshots?
- Does old Grid assume static topology after level load?
- Which parts are valuable topology/research/reference?
- Which parts, if any, are direct-code candidates?
- Which parts should be rewritten from algorithm/spec?

## Gas audit lens

A1 must inspect Gas layering and not treat incomplete legacy Gas as useless by default.

Required Gas questions:

- What exactly did T1, T2, and T3 mean in old Gas architecture?
- What did T1 hold as source of truth?
- Was old T1 intentionally sparse because the old target was huge areas?
- Should new T1 be richer because the new game uses bounded loaded levels?
- Which old Gas structures/invariants/research are valuable?
- Which unfinished parts are core blockers?
- Can the first nucleus use Grid + richer authoritative T1 + minimal presentation/perception layer?
- What belongs to future T2/T3/T4 exploration and must not block this audit?

## Gas↔Grid interaction lens

A1 must explicitly inspect:

- authority;
- order of operations;
- snapshot/state boundary;
- determinism;
- host-authoritative multiplayer implications;
- whether Gas can consume Grid/effective-topology changes without owning Grid;
- whether Grid/device/destruction events can be ordered before Gas tick.

## Future destructibility guardrail

```yaml
future_destructibility_guardrail:
  status: should_not_block_future_feature
  rationale: >
    Gameplay-relevant destructibility may strongly reinforce the expedition/co-op/gas concept:
    destroyed objects, debris, obstacles, tripping hazards, blocked routes, opened passages,
    leaks, ventilation changes, and gas-flow consequences.

  current_goal_boundary: >
    Destructibility is not implemented, fully designed, or promoted into a fifth full audit surface in this Goal.
    It is used as a compatibility lens for Grid/Gas transfer-boundary decisions.

  required_a1_questions:
    - "Does legacy Grid/GridV2 assume static topology after level load?"
    - "Can Grid or a Grid overlay represent opened/closed/blocked connectivity?"
    - "Can debris/obstacles/hazards be represented in Grid-addressable space without forcing Grid to own all destruction?"
    - "Can GasV2R or the future Gas rewrite react to topology/effective-connectivity changes?"
    - "Is there an ordering boundary for destruction event -> Grid/effective topology update -> Gas tick -> network snapshot?"
    - "Would direct transfer of old Grid/Gas code block future destructibility or make it disproportionately expensive?"

  accepted_possible_outcomes:
    - "Grid owns minimal topology mutation API."
    - "A separate Destruction system owns damage/debris and writes effective topology/obstacle overlays."
    - "Gas consumes Grid/effective-topology deltas without owning destruction."
    - "Legacy code is reference-only if it assumes static topology too strongly."

  explicit_non_goals:
    - "No destruction implementation."
    - "No final destruction architecture."
    - "No debris physics."
    - "No structural collapse simulation."
    - "No first-release commitment."
    - "No decision that destructibility must live inside Grid."
```

## Acceptance floor

A1 is DONE only if it returns either a source-backed audit result or exact blocker route with:

1. Separate findings for `legacy_grid`, `gridv2`, `gasv2r`, and `gas_grid_interaction`.
2. For each surface:
   - evidence inspected;
   - new-game fit/mismatch;
   - transfer boundary;
   - transfer mode;
   - confidence;
   - blockers;
   - recommended next route.
3. A target capability matrix covering Grid, Gas, Gas↔Grid, T1/T2/T3, host authority, snapshot, and future destructibility compatibility.
4. Explicit statement whether old Unity source/code/tests are required.
5. Explicit preservation/rejection of old research assumptions.
6. No implementation, code transfer, Unity bootstrap, Codex product/project execution, Task Master graph, or Game Documentation promotion.

## Validation signal

The next workflow state can make a source-backed transfer-boundary decision or route to an exact blocker without guessing and without premature implementation.

## Validation method

A1 audits available documentation/evidence first and records per-surface verdicts and gaps. A1 may request old Unity source/code/tests only if available docs cannot support a safe boundary decision.

## Smallest testable slice

Audit available transfer-boundary documentation and search-discovered C2 evidence docs first:

- `01_OLD_PROJECT_GRID_TOPOLOGY_TECHNICAL_DOC.md`
- `02_OLD_PROJECT_GAS_SIMULATION_TECHNICAL_DOC.md`
- `03_OLD_PROJECT_GRID_GAS_INTERACTION_DOC.md`

Request old local Unity source/tests only when docs cannot support a safe verdict.

## Required context for A1

### Default Project Files

- `directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md`
- `directions/indie-game-development/project_files/01_DIRECTION_STATE.md`
- `directions/indie-game-development/project_files/02_CURRENT_PHASE.md`
- `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md`
- `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md`
- `directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
- `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`

### Shared runtime

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`

### Active phase / completed goal

- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/execution_log.md`

### Game documentation context

- `directions/indie-game-development/domain_docs/game_documentation/technical-foundation-gas-and-grid-contract.md`
- `directions/indie-game-development/domain_docs/game_documentation/clean-start-transfer-boundary.md`

### Request if needed

- Old Unity source/code/tests under `C:\Users\Anton\TheLastExit`.

## Allowed actions in A1

- Audit available docs/evidence.
- Produce transfer/rewrite/reference-only verdicts.
- Identify code/source inspection need.
- Route to E1/S3/D1/R1/Context Request/Stop as justified.
- Flag documentation maintenance candidates.

## Forbidden actions in A1

- Do not implement.
- Do not create Unity project.
- Do not transfer old code.
- Do not run Codex product/project execution.
- Do not create Task Master graph.
- Do not promote Game Documentation.
- Do not decide final destruction architecture.
- Do not design full gas implementation.
- Do not collapse legacy Grid, GridV2, GasV2R, and Gas↔Grid interaction into one vague verdict.

## Route

Next stage: `A1_AUDIT`

## Close path

G1 formalized -> repository maintenance apply/read-back -> Project Files refresh -> A1_AUDIT.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md`
