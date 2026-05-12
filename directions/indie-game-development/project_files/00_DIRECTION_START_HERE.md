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
  next_action: "Run P9_PHASE_CLOSE for Expedition First Proof Checkpoint after corrected R1 Phase Progress Gate selected formal Phase close."
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
| Current Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Active Goal | `none` | Current Goal accepted; do not select G0 until P9 closes or hands off. |
| Last completed Goal | `Определить минимальное доказательное ядро первого proof Expedition` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof` |
| Accepted Goal artifact | `Minimum Expedition Proof Core` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md` |
| Current focus | Close current checkpoint Phase through P9 after corrected R1 Phase Progress Gate | `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md` |
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

## Last accepted Goal result

R1 accepted the Goal-local artifact:

`directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`

The accepted proof-core rule is:

> The first Expedition proof must prove a connected co-op judgment loop, not gas simulation alone.

## Normal next route

`P9_PHASE_CLOSE` for formal close review of `Expedition First Proof Checkpoint`.

Corrected R1 Phase Progress Gate superseded the old `G0_GOAL_SELECT` route. The old route was premature because a verified Goal must first be checked against Phase closure before selecting another Goal.

Do not launch `G0_GOAL_SELECT` from this state unless P9 or an explicit Phase Continue decision creates required follow-up Goal work.

Do not start Codex product/project execution until concrete project/tool bindings, runtime surfaces, validators, and scope are verified.
