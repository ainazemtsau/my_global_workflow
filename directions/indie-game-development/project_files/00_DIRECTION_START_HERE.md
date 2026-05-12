# 00 START HERE - Direction

```yaml
artifact_control:
  artifact_name: "00 START HERE - Direction"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: canonical
  repo_path: "directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh
  last_updated: "2026-05-12"
  next_action: "Run P0_PHASE_START to start the next Phase after Expedition First Proof Checkpoint closed through P9."
```

## Direction identity

* Direction name: `Indie Game Development`
* Direction ID: `indie_game_development`
* Current state: `active`
* Workflow version: `vNext-R`
* Last updated: `2026-05-12`

## Purpose / thesis

Build a commercially viable indie game direction, focused on game concept, product judgment, clean technical base, AI-assisted process, durable documentation, and selective transfer from prior work when it genuinely helps.

## Source-of-truth rule

This file is an active GitHub Direction runtime file. `WORKFLOW_SOURCE_OF_TRUTH.md` is the active source-of-truth marker. If required state is missing, stale, or conflicting, return Context Request; do not invent state.

## Current pointers

| Pointer | Value | Canonical target |
| --- | --- | --- |
| Current Phase | `none` | Start next Phase through `P0_PHASE_START` |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Active Goal | `none` | No active Goal until a new Phase/Goal route creates one |
| Last completed Goal | `Определить минимальное доказательное ядро первого proof Expedition` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof` |
| Accepted Goal artifact | `Minimum Expedition Proof Core` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md` |
| Current focus | Start a post-proof-core Phase through P0 | `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md` |
| Context load rules | Direction Context Loading Index | `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md` |
| Project files folder | GitHub Direction project files | `directions/indie-game-development/project_files/` |

## Default Project Files to load

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`

## Shared runtime file

Load shared runtime core separately from `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.

## Active domain documentation

`Game Documentation` remains active domain documentation at:

`directions/indie-game-development/domain_docs/game_documentation`

It is not archive material and must not be hidden during workflow cleanup. Request specific game documentation through `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`; do not bulk-load all game docs by default.

## Last closed Phase result

P9 closed `Expedition First Proof Checkpoint`.

The accepted proof-core rule remains:

> The first Expedition proof must prove a connected co-op judgment loop, not gas simulation alone.

The accepted proof core is not a prototype design, not an implementation plan, and not a Game Documentation promotion.

## Normal next route

`P0_PHASE_START` for starting the next Phase.

Do not launch `G0_GOAL_SELECT` until a new active Phase exists or a valid stage route creates one.

Do not start Codex product/project execution until concrete project/tool bindings, runtime surfaces, validators, and scope are verified.
