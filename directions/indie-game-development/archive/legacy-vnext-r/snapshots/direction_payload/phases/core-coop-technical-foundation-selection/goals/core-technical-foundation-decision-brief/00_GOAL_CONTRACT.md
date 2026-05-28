# Goal Contract — Core Technical Foundation Decision Brief

```yaml
artifact_control:
  artifact_name: "Goal Contract — Core Technical Foundation Decision Brief"
  schema: goal_contract.v1
  owner_layer: direction_runtime
  status: active
  repo_path: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md"
  direction_id: indie_game_development
  phase_id: core-coop-technical-foundation-selection
  goal_id: core-technical-foundation-decision-brief
  created_by_stage: G1_GOAL_SHAPE
  last_updated: "2026-05-16"
```

## Goal identity

- Goal ID: `core-technical-foundation-decision-brief`
- Goal title: `Сформировать Core Technical Foundation Decision Brief`
- Direction: `Indie Game Development`
- Phase: `Core Co-op Technical Foundation Selection`
- Recommended next stage: `B1_PROBLEM`

## WHAT

Produce an accepted `Core Technical Foundation Decision Brief` / `Decision Map` for the new co-op project.

This Goal does **not** require closing every technical detail in one stage or one request.

It requires every foundation surface to be classified with a clear decision status and route:

- `decided`
- `decision_gate`
- `research_needed_D1`
- `audit_needed_A1`
- `human_decision_needed_S3`
- `deferred_not_blocking_for_bootstrap`

## WHY now

The current Phase exists to resolve high-lock-in co-op technical foundation choices before playable proof, Unity bootstrap, code transfer, or implementation work.

Project engineering and Codex development process are included because Codex will write the project code, and the project is expected to become large enough that modularity, testability, dependency boundaries, validation gates, and multiplayer/domain separation are foundation risks rather than later cleanup.

## Required foundation surfaces

### 1. Multiplayer technology and host-player architecture

Required output:

- selected approach, or
- narrowed decision gate, or
- `research_needed_D1`, or
- `human_decision_needed_S3`.

FishNet may be considered because of old project evidence, but it is not accepted by default.

### 2. Grid/Topology transfer boundary

Required output:

- reusable candidate classification,
- audit-required classification,
- unsafe-assumption classification,
- or non-transferable classification.

If old project files are required, route to `A1_AUDIT` or return a Context Request naming exact files.

### 3. Gas Simulation durable gameplay logic architecture

Required output:

- durable/extensible architecture direction, or
- decision gate for unresolved modeling choices.

Gameplay gas logic must not be hardcoded or disposable. Visual gas may be simpler than gameplay gas.

### 4. Smallest durable technical nucleus

Required output:

- minimal technical nucleus to build next,
- boundaries/contracts/tests/validators needed first,
- explicit exclusions.

### 5. Project Engineering & Codex Development Operating Model

Required output:

- modular project structure principles;
- dependency injection or composition-root approach at decision level;
- separation between domain/gameplay logic and Unity scene/MonoBehaviour surfaces;
- separation between gameplay/domain logic and multiplayer transport/synchronization;
- ability to test singleplayer/domain behavior separately from multiplayer behavior;
- validation gates required before accepting Codex output;
- constraints that prevent tangled, untestable, one-off implementation.

This surface is decision-brief level only. It is not a full engineering handbook, full coding standard, Unity project template, CI setup, or implementation.

## DONE

This Goal is done when an accepted decision brief / decision map exists and:

- each foundation surface has a status from the decision status model;
- final decisions are evidence-backed or explicitly scoped;
- unresolved surfaces are routed to `D1_DEEP_RESEARCH`, `A1_AUDIT`, `S3_DECIDE`, Context Request, or deferred with rationale;
- the brief prevents bootstrap / implementation planning from relying on guesses;
- `R1_GOAL_REVIEW_DISTILL` can review the result;
- `phase_progress_gate` can decide whether the Phase can close or must continue.

## Acceptance floor

A concise accepted decision brief / decision map exists.

It is acceptable if not every detail is fully decided, provided that unresolved details are converted into explicit gates or deferred as not blocking bootstrap.

The brief must not silently proceed to implementation.

## Validation signal

The Direction can proceed to bootstrap / implementation planning, or to a precise research/audit/decision route, without guessing.

## Validation method

Validate the produced brief against:

- this Goal Contract;
- active Phase closure criteria;
- explicit route gates for unresolved surfaces;
- non-goals and forbidden actions.

Final acceptance occurs through `R1_GOAL_REVIEW_DISTILL`, then `phase_progress_gate`.

## Smallest testable slice

One accepted technical foundation decision brief / decision map with per-surface statuses and route gates.

Not included:

- Unity project;
- implementation;
- code transfer;
- full engineering handbook;
- Task Master graph;
- Codex product/project execution.

## Scope in

- Multiplayer technology and host-player architecture.
- Grid/Topology transfer boundary.
- Durable Gas Simulation gameplay architecture.
- Smallest durable technical nucleus.
- Project Engineering & Codex Development Operating Model.
- Decision status model per foundation surface.
- Route gates for D1/A1/S3.
- Validation and close path.

## Non-goals

- Unity project creation.
- Code transfer.
- Product/project Codex execution.
- Task Master graph.
- Final multiplayer stack without evidence.
- Full engineering handbook.
- Full coding standard.
- Exact Unity folder layout unless required for the brief.
- Exact DI package/container selection unless evidence is sufficient.
- Exact CI/test implementation.
- Game Documentation promotion.
- Visual gas proof.
- Throwaway gas/grid prototype.

## Scope cuts

The Goal closes the foundation decision layer, not implementation detail.

E1 must decompose the work into decision packets and gates. It must not attempt to resolve all surfaces in one monolithic pass when evidence, audit, or human decision is required.

## Expected E1 decomposition

E1 should prepare a compact execution decomposition such as:

1. Decision frame and acceptance matrix.
2. Multiplayer evidence gate.
3. Grid/Topology and old-project transfer audit gate.
4. Gas durable logic architecture gate.
5. Project Engineering & Codex Development Operating Model gate.
6. Smallest durable technical nucleus synthesis.
7. Final decision brief synthesis and validation against Phase closure.

If a packet is blocked by current external facts, route to `D1_DEEP_RESEARCH`.

If a packet is blocked by old project evidence, route to `A1_AUDIT` or Context Request.

If a packet is blocked by a human-owned tradeoff, route to `S3_DECIDE`.

## Risk triggers

- Current external multiplayer/tooling evidence is required.
- Old project code/docs are necessary to determine transfer boundary.
- Owner-level tradeoff blocks the technical direction.
- Work drifts into implementation, Unity bootstrap, code transfer, or Codex product/project execution.
- Codex operating model expands into a full engineering handbook.

## Route recommendation

Next stage: `B1_PROBLEM`.

Route reason: the decision brief artifact now exists and is classified by G1 as a review-ready candidate, but direct `G1_GOAL_SHAPE` -> `R1_GOAL_REVIEW_DISTILL` is not registry-valid.

`B1_PROBLEM` is selected narrowly for route-integrity recovery and review handoff repair. It must not reopen the technical foundation decision unless it discovers a real blocker.

## Close path

`B1_PROBLEM` -> registry-valid review handoff -> likely `R1_GOAL_REVIEW_DISTILL` if no blocker is found -> `phase_progress_gate` -> `P9_PHASE_CLOSE` if the Phase minimum outcome is satisfied.

Downstream gates remain valid:
- `A1_AUDIT` for Grid/GridV2 and GasV2R transfer safety if review requires source-backed challenge;
- `D1_DEEP_RESEARCH` if current external evidence is required;
- `S3_DECIDE` if a human-owned tradeoff is reopened;
- `E1_EXECUTION_BRIEF` before implementation planning or Codex execution.

## 2026-05-16 G1 repair/update formalization

G1 classified the existing decision brief artifact as:

```yaml
existing_decision_brief_classification:
  artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md"
  status: review_ready_candidate
  accepted_by_g1: false
  accepted_by_r1: false
  stale_by_default: false
  duplicate_or_rewrite_required: false
```

The Goal Contract remains valid in substance. The repaired state is route/state only:

- immediate next route is `B1_PROBLEM`, not direct `R1_GOAL_REVIEW_DISTILL`;
- B1 scope is route-integrity recovery and review handoff repair;
- the existing decision brief should be reviewed, not duplicated blindly;
- A1/D1/S3/E1 remain downstream gates only if review or route repair finds a blocker;
- no Unity project creation, code transfer, Codex product/project execution, Task Master graph, or Game Documentation promotion is authorized by this G1 formalization.

## End-of-file marker

`END_OF_FILE: directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
