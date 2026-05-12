# 00 Phase Brief

## Phase identity

```yaml
phase:
  name: Expedition First Playable Proof Slice
  id: expedition-first-playable-proof-slice
  state: active
  started_at: "2026-05-12"
  created_by_stage: P0_PHASE_START
  direction: Indie Game Development Direction
```

## Critical constraint

The Direction already has proof identity and proof boundary through `expedition-proof-handoff.md` and the accepted `03_MINIMUM_EXPEDITION_PROOF_CORE.md`.

The current constraint is that the Direction does not yet have the smallest playable proof slice that turns that accepted proof core into a concrete game situation.

This Phase must not create another abstract proof-boundary/readiness layer.

## Minimum outcome

Accepted `First Playable Proof Slice Brief`.

The brief must define the smallest playable situation that can test the accepted Expedition proof core:

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

## Validation signal

This Phase is useful when a later stage can say:

> We know the smallest playable slice that should be shaped or built to test Expedition as a connected co-op judgment loop, not as gas simulation alone.

The Phase is invalid if it repeats proof-boundary work already contained in the proof handoff/core, starts implementation, promotes Game Documentation automatically, or silently decides broad mechanics.

## Phase Closure Contract

```yaml
closure_criteria:
  - One accepted First Playable Proof Slice Brief exists.
  - The slice preserves the accepted proof core and proof handoff.
  - The slice is concrete enough for later proof design / execution brief / tooling decision.
  - The slice does not become implementation plan, prototype backlog, or full game design.
  - R1 accepts the Goal result and runs the phase_progress_gate before any further Goal selection.

required_goal_map:
  - goal_candidate_id: first-playable-proof-slice-brief
    name: Сформировать минимальный playable proof slice для Expedition
    required_for_closure: true
    purpose: Turn accepted proof handoff/core into the smallest concrete playable proof slice.

optional_expansion_candidates:
  - goal_candidate_id: proof-blocking-decision-map
    name: Expedition Proof-Blocking Decision Map
    required_for_closure: false
    trigger: Use only if slice shaping exposes blocking mechanics decisions.
  - goal_candidate_id: project-tool-binding-readiness
    name: Expedition Project Bootstrap / Tool Binding Readiness
    required_for_closure: false
    trigger: Use only if execution readiness becomes the next bottleneck after the slice is shaped.
  - goal_candidate_id: documentation-promotion
    name: Expedition Durable Skeleton Documentation Promotion
    required_for_closure: false
    trigger: Use only after proof/slice truth is accepted as durable enough for Game Documentation.

first_phase_closing_candidate:
  stage: P9_PHASE_CLOSE
  trigger: After the required playable-slice Goal is accepted by R1 and phase_progress_gate selects closure.

after_goal_gate_policy:
  - After R1, run phase_progress_gate before selecting any new G0/G1 work.
  - Do not auto-continue into implementation, documentation promotion, or Codex product/project execution.
```

## In scope

- Shape the next Goal around the first playable proof slice.
- Use existing proof handoff/core as required source material.
- Identify the smallest game situation that can test the accepted Expedition judgment loop.
- Keep unresolved mechanics visible without silently solving all of them.

## Out of scope

- Creating another abstract readiness/boundary artifact.
- Prototype implementation.
- Codex product/project execution.
- Task Master graph creation.
- Full mechanics design.
- Exact cargo, carrying, death/downing, lift, procgen, tool, economy, progression, inventory, or gas taxonomy decisions unless G1 routes to a decision stage.
- Game Documentation promotion.
- Expedition versus Containment reopening.

## Source inputs

Required for next proof-slice shaping:

- `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

Request only if product identity becomes unclear:

- `directions/indie-game-development/domain_docs/game_documentation/expedition-experience-model.md`
- `directions/indie-game-development/domain_docs/game_documentation/primary-product-bet-expedition.md`

## Recommended first Goal candidate

```yaml
candidate:
  id: first-playable-proof-slice-brief
  name: Сформировать минимальный playable proof slice для Expedition
  recommended_next_stage: G1_GOAL_SHAPE
  smallest_useful_result: Accepted First Playable Proof Slice Brief
  confidence: high
```

## Next route

`G1_GOAL_SHAPE`

Do not run the next stage until this Phase start patch is applied, read back, diff-verified, commit-verified, and refreshed in context.
