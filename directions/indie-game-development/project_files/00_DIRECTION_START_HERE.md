# 00 START HERE - Direction

```yaml
artifact_control:
  artifact_name: "00 START HERE - Direction"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh_after_p0_repository_apply
  last_updated: "2026-05-13"
  next_action: "After G1 repository maintenance apply/read-back and Project Files refresh, run B1_PROBLEM for route-integrity recovery and review handoff repair."
```

## Direction identity

- Direction name: `Indie Game Development`
- Direction ID: `indie_game_development`
- Current state: `active`
- Workflow version: `vNext-R`
- Last updated: `2026-05-13`

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
| Current Phase Brief | `Phase Brief — Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Active Goal | `core-technical-foundation-decision-brief` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief` |
| Active Goal Contract | `Goal Contract — Core Technical Foundation Decision Brief` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md` |
| Existing Goal Artifact | `Core Technical Foundation Decision Brief / Decision Map` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` |
| Direction Map | `initialized / active_horizon: H1_playable_technical_nucleus` | `directions/indie-game-development/project_files/08_DIRECTION_MAP.md` |
| Previous Phase | `Expedition First Playable Proof Slice` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice` |
| Previous Phase status | `paused_superseded_not_closed` | Preserved as context/evidence, not closed by P9 |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Next route | `B1_PROBLEM` route-integrity recovery / review handoff repair | `workflow/stage_prompts/B1_PROBLEM.md` |

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

Run `B1_PROBLEM` for route-integrity recovery / review handoff repair after this G1 repository patch is applied, read back, diff-verified, commit-verified, and refreshed in ChatGPT Project Files.

B1 must resolve the registry route issue created by the fact that the existing decision brief is review-ready, while direct `G1_GOAL_SHAPE` -> `R1_GOAL_REVIEW_DISTILL` is not allowed.

Target outcome:

- confirm the existing `04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md` can proceed to `R1_GOAL_REVIEW_DISTILL`; or
- route to exact blocker stage if not review-ready.

Do not run direct R1 from G1.

Do not start Codex product/project execution until concrete project/tool bindings, runtime surfaces, validators, scope, and execution route are verified.
