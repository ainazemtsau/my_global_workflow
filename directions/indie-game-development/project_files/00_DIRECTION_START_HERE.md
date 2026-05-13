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
  next_action: "After P0 repository maintenance apply/read-back and Project Files refresh, run G1_GOAL_SHAPE for candidate core-technical-foundation-decision-brief."
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
| Current Phase | `Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection` |
| Current Phase Brief | `Phase Brief — Core Co-op Technical Foundation Selection` | `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md` |
| Active Goal | `none_pending_G1` | `N/A` |
| Recommended first Goal candidate | `Сформировать Core Technical Foundation Decision Brief` | To be shaped by `G1_GOAL_SHAPE` |
| Previous Phase | `Expedition First Playable Proof Slice` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice` |
| Previous Phase status | `paused_superseded_not_closed` | Preserved as context/evidence, not closed by P9 |
| Previous Goal | `first-playable-proof-slice-brief` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief` |
| Previous Goal status | `paused_superseded_partial_progress_not_accepted` | Preserved as scaffold/evidence, not accepted completion |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Accepted Goal artifact | `Minimum Expedition Proof Core` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md` |
| Context load rules | Direction Context Loading Index | `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md` |
| Next route | `G1_GOAL_SHAPE` | `workflow/stage_prompts/G1_GOAL_SHAPE.md` |

## Current Phase meaning

`Core Co-op Technical Foundation Selection` exists to resolve high-lock-in technical foundation choices before playable proof or implementation work.

Foundation scope includes:

- multiplayer technology and host-player architecture;
- Grid/Topology transfer boundary;
- Gas Simulation durable gameplay logic model;
- smallest durable technical nucleus to build next.

FishNet is a candidate based on old project evidence, not a final default. Unity multiplayer stack and other viable options may be considered through the proper research/decision route.

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

Also load shared runtime cache files defined in:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

## Normal next route

Run `G1_GOAL_SHAPE` for the candidate Goal:

`Сформировать Core Technical Foundation Decision Brief`

Do not run G1 until this P0 patch is applied, read back, diff-verified, commit-verified, and refreshed in ChatGPT Project Files.

Do not start Codex product/project execution until concrete project/tool bindings, runtime surfaces, validators, scope, and execution route are verified.
