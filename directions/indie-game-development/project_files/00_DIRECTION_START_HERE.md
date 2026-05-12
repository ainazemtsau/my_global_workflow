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
  next_action: "After G1 repository maintenance apply/read-back, run E1_EXECUTION_BRIEF for the active Goal first-playable-proof-slice-brief."
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
| Current Phase | `Expedition First Playable Proof Slice` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice` |
| Last closed Phase | `Expedition First Proof Checkpoint` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint` |
| Active Goal | `first-playable-proof-slice-brief` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief` |
| Active Goal Contract | `Goal Contract — First Playable Proof Slice Brief` | `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md` |
| Recommended first Goal candidate | `Сформировать минимальный playable proof slice для Expedition` | Shaped by `G1_GOAL_SHAPE`; active Goal now exists |
| Last completed Goal | `Определить минимальное доказательное ядро первого proof Expedition` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof` |
| Accepted Goal artifact | `Minimum Expedition Proof Core` | `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md` |
| Required proof-slice handoff input | `Expedition Proof Handoff` | `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md` |
| Current focus | Prepare E1 execution brief for the First Playable Proof Slice Brief | `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md` |
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

For the next proof-slice shaping route, load the exact proof handoff:

`directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`

This targeted load is not Game Documentation promotion.

## Last closed Phase result

P9 closed `Expedition First Proof Checkpoint`.

The accepted proof-core rule remains:

> The first Expedition proof must prove a connected co-op judgment loop, not gas simulation alone.

The accepted proof core is not a prototype design, not an implementation plan, and not a Game Documentation promotion.

## Current Phase result expected

`Expedition First Playable Proof Slice` should produce the smallest playable proof slice that can test the accepted Expedition proof core as a concrete game situation.

It must not create another abstract readiness/boundary document.

## Normal next route

`E1_EXECUTION_BRIEF` for the active Goal:

`Сформировать минимальный playable proof slice для Expedition`

Do not run `E1_EXECUTION_BRIEF` until the G1 repository maintenance patch is applied, read back, diff-verified, commit-verified, and refreshed in context.

Do not start Codex product/project execution until concrete project/tool bindings, runtime surfaces, validators, and scope are verified.
