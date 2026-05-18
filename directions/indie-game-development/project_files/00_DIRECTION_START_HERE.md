# 00 START HERE - Direction

```yaml
artifact_control:
  artifact_name: "00 START HERE - Direction"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh_after_f0_synthesis_evidence_integrity_repair
  last_updated: "2026-05-18"
  next_action: "Refresh Project Files from GitHub, then run R1_GOAL_REVIEW_DISTILL for first-technical-nucleus-functional-spec."
```

## Direction identity

- Direction name: `Indie Game Development`
- Direction ID: `indie_game_development`
- Current state: `active`
- Workflow version: `vNext-R`
- Last updated: `2026-05-18`

## Purpose / thesis

Build a commercially viable indie game direction, focused on game concept, product judgment, clean technical base, AI-assisted process, durable documentation, and selective transfer from prior work when it genuinely helps.

## Source-of-truth rule

This file is an active GitHub Direction runtime file. `WORKFLOW_SOURCE_OF_TRUTH.md` is the active source-of-truth marker. If required state is missing, stale, or conflicting, return Context Request; do not invent state.

## Current pointers

| Pointer | Value | Canonical target |
| --- | --- | --- |
| Current Initiative | `innovative-commercial-expedition-gas-sim-game` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Active Horizon | `H1_playable_technical_nucleus` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Current Gate | `H1_G1_core_technical_foundation_decision_brief` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Required Codex / Architecture Gate | `H1_G2_codex_development_operating_model_and_architecture_protocols` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Current Phase | `Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection` |
| Current Phase status | `active_first_technical_nucleus_spec_synthesis_formalized_pending_R1` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Current Phase Brief | `Phase Brief — Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Active Goal | `first-technical-nucleus-functional-spec` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec` |
| Active Goal Contract | `Goal Contract — First Technical Nucleus Functional Spec` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/00_GOAL_CONTRACT.md` |
| Active Goal status | `synthesis_formalized_pending_R1_review` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md` |
| Existing Goal Artifact | `Core Technical Foundation Decision Brief / Decision Map` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` |
| Direction Map | `initialized / active_horizon: H1_playable_technical_nucleus` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Previous Phase | `Expedition First Playable Proof Slice` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice` |
| Previous Phase status | `paused_superseded_not_closed` | Preserved as context/evidence, not closed by P9 |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Next route | `R1_GOAL_REVIEW_DISTILL` for `first-technical-nucleus-functional-spec` | `workflow/stage_prompts/R1_GOAL_REVIEW_DISTILL.md` |

## Current Phase meaning

`Core Co-op Technical Foundation Selection` exists to resolve high-lock-in technical foundation choices before playable proof or implementation work.

Foundation scope includes:

- multiplayer technology and host-player architecture;
- Grid/Topology transfer boundary;
- Gas Simulation durable gameplay logic model;
- smallest durable technical nucleus to build next.

The active Goal adds a goal-local decision surface: `Project Engineering & Codex Development Operating Model`.

This is a staged decision brief / decision map, not one-shot closure of every technical detail.

FishNet is a candidate based on old project evidence, not a final default. Unity multiplayer stack and other viable options may be considered through the proper research/decision route.

Codex-driven implementation must wait until the foundation decision, execution route, concrete project/tool bindings, validators, and scope are verified.

## Default Project Files to load

Load these Direction Project Files by default:

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`
8. `07_PHASE_MEMORY_INDEX.md`
9. `08_DIRECTION_MAP.md`

Also load shared runtime cache files defined in:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

If `08_DIRECTION_MAP.md` is uninitialized or marked `needs_m0_review`, run `M0_DIRECTION_MAP` to migrate/build the map from current `00-07` progress and user-provided initiative context before relying on it for strategic Phase/Goal selection.

## Normal next route

Run `R1_GOAL_REVIEW_DISTILL` for `first-technical-nucleus-functional-spec`.

R1 must review the completed parent Goal outcome against the Goal Contract, including:

1. gas simulation capability frame;
2. user approval gate after gas block;
3. level/spatial requirements;
4. Grid/topology substrate requirements;
5. cross-system interaction requirements;
6. destructibility compatibility boundary;
7. validation/demo requirements;
8. synthesis.

Do not run Unity bootstrap, implementation, old-code transfer, old-code audit, Codex product/project execution, Task Master graph creation, Phase Progress Gate, P9, or Game Documentation promotion in this R1 launch context.

## 2026-05-16 R1 stabilization

R1 accepted the existing `Core Technical Foundation Decision Brief / Decision Map` as an accepted route-gated decision map.

Accepted:
- multiplayer default: FishNet + Steamworks / Steam Networking / Steam Datagram Relay;
- Photon Fusion 2 as fallback / paid acceleration path;
- player-hosted / listen-host co-op architecture for MVP baseline;
- Project Engineering & Codex Development Operating Model at decision-map level.

Not accepted for implementation:
- direct legacy Grid transfer;
- direct GridV2 replacement;
- direct GasV2R production transfer;
- Grid↔Gas interaction production readiness;
- Unity project creation;
- code transfer;
- Codex product/project execution.

Phase Progress Gate selected continuation with required next Goal candidate:

`grid-gas-transfer-boundary-audit`

Next route: `G1_GOAL_SHAPE`.

## 2026-05-16 G1 reset formalization

G1 superseded `grid-gas-transfer-boundary-audit` after human clarification.

New active Goal:

`first-technical-nucleus-functional-spec`

Direct old-code transfer is out of scope. Old project material is reference/evidence only and may be used later as targeted reference after requirements are clear.

Historical next route at G1 reset: `E1_EXECUTION_BRIEF`.

Current next route after F0 synthesis formalization and evidence repair: `R1_GOAL_REVIEW_DISTILL`.
