# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh_after_p0_repository_apply_readback
activated_at: "2026-05-13"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load these files by default for Indie Game Development runtime:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
- `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md`
- `directions/indie-game-development/project_files/01_DIRECTION_STATE.md`
- `directions/indie-game-development/project_files/02_CURRENT_PHASE.md`
- `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md`
- `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md`
- `directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
- `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`

GitHub remains the source of truth. Project Files are a runtime cache.

If GitHub and Project File cache conflict, use verified full GitHub read-back. If GitHub read is truncated, omitted, lacks tail verification, or cannot be verified, return Context Request instead of treating partial GitHub content as authority.

`08_DIRECTION_MAP.md` is strategic routing context between Direction and Phase; it does not replace Phase, Goal, Queue, Context Loading Index, or Phase Memory state.

## Shared runtime and stage prompts

```yaml
shared_runtime_file: "workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md"
stage_prompt_source_root: "workflow/stage_prompts/"
stage_prompt_load_rule: "request exact stage prompt by stage ID; do not bulk-load all prompts"
local_runtime_core_copy_required: false
```

Stage prompts are request-only runtime inputs. Do not copy stage prompt files into Direction Project Files.

## Active Phase context

Load for work on the current Phase:

- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - Status: `active_phase_brief`
  - Load for `G1_GOAL_SHAPE`, `A1_AUDIT`, and any route working on the current Phase.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_execution_log.md`
  - Status: `active_phase_log`
  - Request only when execution history is needed.

## Active Goal context

Active Goal after R1 acceptance:

- Goal ID: `core-technical-foundation-decision-brief`
- Goal title: `Сформировать Core Technical Foundation Decision Brief`
- Goal path: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief`
- Goal Contract: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
- Existing Goal Artifact: `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
- Existing artifact treatment: `accepted_route_gated_decision_map`
- Recommended next stage: `G1_GOAL_SHAPE`
- Recommended next mode: `shape_required_grid_gas_transfer_boundary_audit_goal`

Load for work on the active Goal:

- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/00_GOAL_CONTRACT.md`
  - Status: `active_goal_contract`
  - Reason: shaped Goal Contract, staged decision-map scope boundary, decision status model.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`
  - Status: `existing_goal_artifact_r1_accepted_route_gated_decision_map`
  - Reason: existing decision brief was accepted by R1 as a route-gated decision map; Grid/Gas transfer remains routed to A1 audit.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/execution_log.md`
  - Status: `active_goal_log`
  - Request only when execution history is needed.

## Conditionally required technical foundation context

Load/request these when shaping, researching, deciding, or executing the first technical foundation Goal:

- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - Status: `required_for_current_G1`
  - Reason: active Phase frame and closure contract.
- `directions/indie-game-development/domain_docs/game_documentation/technical-foundation-gas-and-grid-contract.md`
  - Status: `request_only`
  - Reason: prior technical foundation/gas/grid documentation candidate.
- `directions/indie-game-development/domain_docs/game_documentation/clean-start-transfer-boundary.md`
  - Status: `request_only`
  - Reason: old-to-new project transfer boundary context.
- `directions/indie-game-development/domain_docs/game_documentation/foundation-docs-index.md`
  - Status: `request_only`
  - Reason: index for relevant foundation docs.
- `directions/indie-game-development/phases/expedition-first-playable-proof-slice/00_PHASE_BRIEF.md`
  - Status: `paused_superseded_phase_context`
  - Reason: previous Phase context; do not treat as current active Phase.
- `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/00_GOAL_CONTRACT.md`
  - Status: `paused_superseded_goal_context`
  - Reason: previous active Goal; not accepted completion.
- `directions/indie-game-development/phases/expedition-first-playable-proof-slice/goals/first-playable-proof-slice-brief/02_FIRST_PLAYABLE_PROOF_SLICE_BRIEF.md`
  - Status: `preserved_scaffold_evidence_not_accepted`
  - Reason: useful scaffold/evidence only.
- `directions/indie-game-development/domain_docs/game_documentation/expedition-proof-handoff.md`
  - Status: `request_only_product_identity_context`
  - Reason: preserve accepted proof direction if product identity becomes unclear.
- `directions/indie-game-development/phases/expedition-first-proof-checkpoint/goals/minimum-proof-core-first-expedition-proof/03_MINIMUM_EXPEDITION_PROOF_CORE.md`
  - Status: `accepted_by_R1_and_closed_by_P9`
  - Reason: accepted proof core; do not treat as prototype design or execution brief.

## Future context not required for G1 but likely required later

- old Unity project code;
- old Grid/Topology implementation files;
- old Grid/Topology tests;
- old Gas Simulation implementation/docs/tests;
- old FishNet integration files;
- old technical documentation;
- profiling notes;
- current external multiplayer technology evidence;
- Unity multiplayer stack documentation;
- FishNet documentation;
- other candidate networking technology documentation;
- Unity/C# testing and project-architecture references;
- Codex development workflow / validation guidance;
- dependency injection / composition-root references for Unity, if the decision brief requires external evidence.

## Tool boundary

Concrete project setup for Gas Coop Game must be verified before Codex product/project execution. Do not infer AGENTS.md, `.codex/config.toml`, Task Master, Serena, Basic Memory, or validators from governance notes.

Repository maintenance is allowed only for approved `repository_patch.v1` application/read-back and is not product/project execution.

## Game Documentation promotion boundary

Foundation decisions may become candidates for future Game Documentation maintenance, but they are not promoted automatically.

## Duplicate-artifact prevention note

Do not create another proof-boundary/readiness artifact unless evidence proves the accepted proof core/handoff are insufficient.

Do not recreate `Expedition First Proof Checkpoint`.

This current Phase has a different delta: high-lock-in technical foundation selection for a new co-op project.

## Required context for grid-gas-transfer-boundary-audit

After R1 accepted the Core Technical Foundation Decision Brief as a route-gated decision map, the next required Goal candidate is:

`grid-gas-transfer-boundary-audit`

Load for shaping/audit:
- `directions/indie-game-development/domain_docs/game_documentation/technical-foundation-gas-and-grid-contract.md`
- `directions/indie-game-development/domain_docs/game_documentation/clean-start-transfer-boundary.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

Search-discovered C2 evidence docs:
- `01_OLD_PROJECT_GRID_TOPOLOGY_TECHNICAL_DOC.md`
- `02_OLD_PROJECT_GAS_SIMULATION_TECHNICAL_DOC.md`
- `03_OLD_PROJECT_GRID_GAS_INTERACTION_DOC.md`

A1 audit target:
- legacy Grid;
- GridV2;
- GasV2R;
- Gas↔Grid interaction.

Known gap:
- old Unity source/code/tests are not present in this repository;
- referenced old source anchors point to `C:\Users\Anton\TheLastExit`;
- A1 may need Context Request or Codex/local-source access if direct code/test inspection is required.
