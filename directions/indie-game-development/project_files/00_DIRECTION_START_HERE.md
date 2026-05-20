# 00 START HERE - Direction

```yaml
artifact_control:
  artifact_name: "00 START HERE - Direction"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh_after_r1_H1_G2_acceptance_pending_m0_review
  last_updated: "2026-05-20"
  next_action: "Run M0_DIRECTION_MAP after R1 H1_G2 acceptance repository maintenance apply/read-back and manual Project Files refresh."
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
| Current Gate | `H1_G2_codex_development_operating_model_and_architecture_protocols` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Required Codex / Architecture Gate | `H1_G2_codex_development_operating_model_and_architecture_protocols` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Current Phase | `Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection` |
| Current Phase status | `active_H1_G2_r1_accepted_pending_M0_active_front_review` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Current Phase Brief | `Phase Brief — Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Active Goal | `H1_G2_codex_development_operating_model_and_architecture_protocols` | `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md` |
| Active Goal status | `r1_accepted_goal_complete` | `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md` |
| Last completed Goal | `H1_G2_codex_development_operating_model_and_architecture_protocols` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols` |
| Last completed Goal status | `r1_accepted_goal_complete` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md` |
| Last completed Goal Artifact | `Gas Coop Game Project Execution Profile` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md` |
| Existing Goal Artifact | `Core Technical Foundation Decision Brief / Decision Map` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` |
| Direction Map | `initialized / active_horizon: H1_playable_technical_nucleus` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Previous Phase | `Expedition First Playable Proof Slice` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice` |
| Previous Phase status | `paused_superseded_not_closed` | Preserved as context/evidence, not closed by P9 |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Next route | `M0_DIRECTION_MAP — active-front review after H1_G2 acceptance` | `workflow/stage_prompts/M0_DIRECTION_MAP.md` |

## Current Phase meaning

`Core Co-op Technical Foundation Selection` exists to resolve high-lock-in technical foundation choices before playable proof or implementation work.

Foundation scope includes:

- multiplayer technology and host-player architecture;
- Grid/Topology transfer boundary;
- Gas Simulation durable gameplay logic model;
- smallest durable technical nucleus to build next.

The accepted specification preserves a goal-local decision surface: `Project Engineering & Codex Development Operating Model`.

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

Run `M0_DIRECTION_MAP` after R1 H1_G2 acceptance repository maintenance apply/read-back and manual Project Files refresh.

M0 must review the active frontier after H1_G2 acceptance before selecting H1_G3 project/bootstrap/tool-binding/validation-scene readiness, P9, G0, E1, bootstrap, or implementation.

Do not run Unity bootstrap, implementation, old-code transfer, old-code audit as starting point, Codex product/project execution, Task Master graph creation, real internal tool setup, direct E1 launch, or Game Documentation promotion before a later basis-valid route authorizes concrete work.

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

## 2026-05-18 R1 acceptance — first technical nucleus functional specification

R1 accepted `first-technical-nucleus-functional-spec` as `completed_verified` at functional/technical specification level.

Accepted: gas simulation capability frame, user approval gate after gas, level/spatial requirements, Grid/topology substrate, cross-system interaction, destructibility compatibility, validation/demo requirements, and synthesis.

Not authorized: Unity bootstrap, implementation, old-code transfer, old-code audit as starting point, Codex product/project execution, Task Master graph creation, or Game Documentation promotion.

Next route: `M0_DIRECTION_MAP` to review active front before P9, G0, E1, or implementation planning.

## 2026-05-19 M0 Objective Architecture migration

M0 formalized the Objective Architecture layer for the initialized Direction Map.

Accepted:
- Direction Objective is explicit.
- `H1_playable_technical_nucleus` remains the active accepted horizon.
- Horizon is strategically accepted but locked for direct execution.
- Objective Graph / Active Frontier / Next Action Proof are now explicit in `08_DIRECTION_MAP.md`.
- Selected next frontier node: `H1_G2_codex_development_operating_model_and_architecture_protocols`.
- Next safe route: `G1_GOAL_SHAPE`.

Not authorized:
- Unity bootstrap;
- implementation;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion.

## 2026-05-19 G1 H1_G2 formalization

G1 formalized `H1_G2_codex_development_operating_model_and_architecture_protocols` as a Goal.

Goal contract:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`

Key correction:

- The Goal is not to create a second Codex/workflow layer.
- The Goal is to audit/fit-check the existing workflow Codex/project setup and execution-readiness procedure on first real use.
- A1 must decide whether the existing workflow is sufficient, needs a minimal Indie project-specific addendum/profile, needs Workflow Governance repair, or requires missing context.

Next route:

`A1_AUDIT`

Still not authorized:

- Unity bootstrap;
- implementation;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- Game Documentation promotion.

## 2026-05-20 R1 acceptance — H1_G2 profile/addendum

R1 accepted `H1_G2_codex_development_operating_model_and_architecture_protocols`
as `completed_verified`.

Accepted artifact:

`directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`

Accepted scope:
- minimal Gas Coop Game zero-state project execution profile/addendum;
- future H1_G3 bootstrap-readiness targets;
- validation profile;
- memory/tool-binding policy;
- module/documentation requirements;
- bounded Codex slice contract;
- Unity MCP deferred until H1_G3;
- stop rules.

Not authorized:
- Unity bootstrap;
- product repository creation;
- implementation;
- product code;
- Codex product/project execution;
- Task Master graph creation;
- real internal tool setup;
- old-code transfer or old-code audit as starting point;
- Game Documentation promotion.

Next route: `M0_DIRECTION_MAP`.

Reason: H1_G2 acceptance changes the active frontier. M0 must review whether
H1_G3 project/bootstrap/tool-binding/validation-scene readiness, P9, G0, or
another route is basis-valid before any material continuation.
