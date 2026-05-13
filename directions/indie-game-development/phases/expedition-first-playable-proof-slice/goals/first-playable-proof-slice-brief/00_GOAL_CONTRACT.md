# Goal Contract — First Playable Proof Slice Brief

```yaml
artifact_control:
  artifact_name: "Goal Contract — First Playable Proof Slice Brief"
  schema: goal_contract.v1
  owner_layer: workflow_runtime
  status: active
  repo_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md"
  created_by_stage: G1_GOAL_SHAPE
  created_at: "2026-05-12"
  source_phase: "Expedition First Playable Proof Slice"
  next_route: E1_EXECUTION_BRIEF
  freshness: fresh_after_repository_apply_readback
```

## Goal identity

```yaml
goal:
  id: first-playable-proof-slice-brief
  goal_id: first-playable-proof-slice-brief
  title: "Сформировать минимальный playable proof slice для Expedition"
  status: active
  direction_id: indie_game_development
  direction_name: Indie Game Development
  phase_id: expedition-first-playable-proof-slice
  phase_name: Expedition First Playable Proof Slice
  goal_path: "directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief"
  smallest_useful_result: "Accepted First Playable Proof Slice Brief"
```

## Source inputs

Required source inputs:

- `directions/indie-game-development/phases/expedition-first-playable-proof-slice/00_PHASE_BRIEF.md`
- `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

These sources already define proof identity and boundary. This Goal must not create another abstract proof-boundary/readiness artifact.

## Goal Contract

### WHAT

Create a `First Playable Proof Slice Brief` for Expedition: the smallest concrete playable situation that can test the accepted Expedition proof core as one connected co-op judgment loop.

### WHY now

The prior Phase accepted the proof boundary. The current Phase exists to move from that boundary into the smallest concrete playable proof slice without repeating readiness work and without starting implementation.

### DONE

A reviewable `First Playable Proof Slice Brief` exists and defines one minimal playable Expedition situation with enough specificity for later proof design / execution brief / tooling decision, while preserving unresolved mechanics as unresolved.

### Acceptance floor

The brief must define:

- minimal player situation;
- what players do by hand;
- lift/descent boundary;
- minimal route/gas/topology pressure;
- minimal dangerous vessel/value situation;
- co-op shared-state consequence;
- real push / reroute / secure / retreat / abandon judgment point;
- run ending;
- consequence ledger result;
- reason for next descent;
- unresolved mechanics that remain deliberately undecided.

### Validation signal

A later reviewer can say:

> We know the smallest playable slice that should be shaped or built to test Expedition as a connected co-op judgment loop, not as gas simulation alone.

### Validation method

Validate the produced brief by checking:

1. The accepted minimum Expedition loop is present as one connected judgment loop.
2. The six observable proof signals remain testable.
3. Gas is tied to Expedition meaning, not isolated simulation quality.
4. Deferred mechanics are visible but not silently solved.
5. The brief can be routed to `R1_GOAL_REVIEW_DISTILL` for accept / revise / reject.

### Smallest testable slice

One bounded co-op expedition run:

```text
prepare small risk/tool commitment
→ descend by lift
→ read unknown route + gas/topology + dangerous vessel-value pressure
→ make one route/safety intervention
→ recover or stabilize dangerous vessel-value
→ face readable gas/topology/vessel consequence
→ choose push / reroute / secure / retreat / abandon
→ lock result into consequence ledger
→ leave a concrete reason for next descent
```

### Close path

After the `First Playable Proof Slice Brief` is produced, route to `R1_GOAL_REVIEW_DISTILL`.

After R1, run the Phase progress gate before selecting further Goals, starting implementation, promoting Game Documentation, or launching Codex product/project execution.

## Scope in

- Shape the first playable proof slice brief.
- Use accepted proof handoff/core as required source material.
- Identify the smallest game situation that can test the accepted Expedition judgment loop.
- Keep unresolved mechanics visible without silently deciding them.
- Prepare for a later execution brief / proof design / tooling decision.

## Non-goals

This Goal must not produce:

- another abstract proof-readiness or proof-boundary artifact;
- playable prototype implementation;
- code tasks;
- Task Master graph;
- Codex product/project execution;
- prototype scene specification;
- full game design;
- exact cargo mechanics;
- exact carrying model;
- exact death / downing / group failure model;
- exact lift failure or contamination model;
- exact procedural generation model;
- exact tool list or tool stats;
- exact gas recipes, gas taxonomy, or reaction tables;
- exact inventory system;
- economy, progression, reward curve, or base / hub form;
- Game Documentation promotion;
- Expedition versus Containment reopening.

## Scope cuts

Cut from this Goal:

- implementation plan;
- proof build backlog;
- production metrics plan;
- technical project/tool binding readiness;
- durable Game Documentation update;
- broader Expedition concept redesign.

## Deferred candidates

Use only if triggered by later evidence:

- `proof-blocking-decision-map`;
- `project-tool-binding-readiness`;
- `documentation-promotion`.

## Risk triggers / stop rules

Stop, route to `S3_DECIDE`, or route to the appropriate recovery stage if:

- a blocking mechanics decision must be owned by the user;
- the work starts becoming prototype scene specification;
- the work starts becoming implementation planning or code tasks;
- the proof can pass as gas simulation alone;
- exact cargo/carrying/death/lift/procgen/tool/gas mechanics become required for DONE;
- Codex product/project execution is requested before project/tool bindings are verified;
- Game Documentation promotion is requested before artifact acceptance;
- Expedition versus Containment is reopened.

## Goal Working Context

```yaml
phase_fit: >
  This Goal directly satisfies the active Phase minimum outcome: accepted First
  Playable Proof Slice Brief.

assumptions:
  - The proof handoff and accepted proof core are sufficient inputs.
  - No human-owned blocking mechanics decision is required before E1.
  - Exact mechanics remain unresolved unless a later stage routes to S3_DECIDE.

allowed_actions:
  - Produce an execution brief for creating the First Playable Proof Slice Brief.
  - Define brief sections, validation checks, and writing boundaries.
  - Preserve source handoff/core.
  - Keep deferred mechanics visible.

forbidden_actions:
  - Do not implement prototype.
  - Do not create code tasks.
  - Do not run Codex product/project execution.
  - Do not create Task Master graph.
  - Do not promote Game Documentation.
  - Do not reopen Expedition versus Containment.
```

## Next route

`E1_EXECUTION_BRIEF`

E1 should produce the minimum HOW for creating the `First Playable Proof Slice Brief`, including artifact boundaries, validation method, required source context, stop conditions, and whether the work can be direct or must route through a later stage.

## P0 status update — 2026-05-13

Status after `P0_PHASE_START`: `paused_superseded_partial_progress_not_accepted`.

The F0-created First Playable Proof Slice Brief remains useful scaffold/evidence, but it is not accepted as Goal completion.

Reason: the user identified a higher-leverage bottleneck for the new project: core technical foundation selection, including multiplayer technology/architecture, Grid/Topology transfer boundary, and durable Gas Simulation logic architecture.

Do not route this Goal to R1 acceptance or Phase closure unless a later explicit stage reactivates it.
