# 06_CONTEXT_LIBRARY_INDEX.md

```yaml
project_file_projection: 1
schema: direction_project_file_projection.v1
source_file: "directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md"
canonical_source: GitHub repository file
projection_status: fresh_after_r1_H1_G3_readiness_packet_accepted_pending_p9_phase_close
activated_at: "2026-05-13"
```

## Canon rule

This file is an active GitHub Direction runtime file. If it conflicts with another current GitHub Direction file, return Context Request; do not invent state.

## Default context

Load these files by default for Indie Game Development runtime:

- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`
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
  - Status: `active_H1_G3_r1_accepted_pending_P9_phase_close`
  - Load for `P9_PHASE_CLOSE` and any route working on the current Phase.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_execution_log.md`
  - Status: `active_phase_log`
  - Request only when execution history is needed.

## Active Goal context

Active Goal after R1 H1_G3 acceptance:

```yaml
active_goal_after_r1_H1_G3_acceptance:
  active_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  active_goal_status: r1_accepted_goal_complete
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
  execution_log: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md"
  last_completed_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  accepted_profile_artifact: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md"
  accepted_product_local_artifacts:
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\outbox\\H1_G3_READINESS_PACKET.md"
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\evidence\\h1-g3-readiness-2026-05-21.md"
  recommended_next_stage: P9_PHASE_CLOSE
  recommended_next_mode: close_or_pause_core_coop_technical_foundation_selection_after_H1_G3_acceptance
```

Load for P9 after R1 H1_G3 acceptance:

- `workflow/stage_prompts/P9_PHASE_CLOSE.md`
  - Status: `required_stage_prompt`
  - Reason: exact next stage prompt for phase close; do not bulk-load prompt text into Project Files.
- `directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/01_DIRECTION_STATE.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/02_CURRENT_PHASE.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`
  - Status: `required_E1_context`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md`
  - Status: `r1_accepted_goal_complete`
  - Reason: active H1_G3 Goal Contract.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md`
  - Status: `goal_execution_log`
  - Reason: G1 formalization evidence.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`
  - Status: `accepted_profile_artifact`
  - Reason: accepted H1_G2 profile/addendum.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - Status: `active_H1_G3_r1_accepted_pending_P9_phase_close`
  - Reason: active Phase state and current route guardrails.

## Superseded Goal context

`grid-gas-transfer-boundary-audit` is superseded after human clarification.

Treatment:

- preserve as reset context;
- do not load for default active execution;
- do not run A1 audit unless a later lifecycle stage explicitly reselects a targeted audit;
- old Grid/Gas material is reference/evidence only after requirements are clear.

## Conditionally required technical foundation context

Load/request these when shaping, researching, deciding, or executing the first technical foundation Goal:

- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
  - Status: `required_for_m0_active_front_review`
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

## Superseded context for grid-gas-transfer-boundary-audit

After G1 reset formalization, this Goal is superseded:

`grid-gas-transfer-boundary-audit`

Load for A1 audit:
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/00_GOAL_CONTRACT.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/grid-gas-transfer-boundary-audit/execution_log.md`
- `directions/indie-game-development/domain_docs/game_documentation/technical-foundation-gas-and-grid-contract.md`
- `directions/indie-game-development/domain_docs/game_documentation/clean-start-transfer-boundary.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

Search-discovered old-project technical evidence docs:
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

## Superseded context for A1 grid-gas-transfer-boundary-audit after G1 formalization

Recommended next stage: `A1_AUDIT`.

Recommended next mode: `audit_grid_gas_transfer_boundary`.

## Required context after M0 Objective Architecture migration

Recommended next stage: `G1_GOAL_SHAPE`.

Recommended next mode: `shape_H1_G2_codex_development_operating_model_and_architecture_protocols`.

Required for G1:

- exact `workflow/stage_prompts/G1_GOAL_SHAPE.md` prompt with visible EOF marker or Codex verified local bundle;
- current Project Files 00-08 after M0 Objective Architecture migration repository maintenance read-back and manual refresh;
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`;
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`;
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`.

Old Unity source/code/tests are not default context. Request them only after a later block has a targeted reference question.

Do not run implementation, Unity bootstrap, old-code transfer, old-code audit, Codex product/project execution, Task Master graph creation, or Game Documentation promotion.

## Required context after G1 H1_G2 formalization

Recommended next stage: `A1_AUDIT`.

Recommended next mode: `audit_existing_workflow_codex_project_setup_first_use_fit`.

Load for A1:

- `workflow/stage_prompts/A1_AUDIT.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md`
- `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/first-technical-nucleus-functional-spec/01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/core-technical-foundation-decision-brief/04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md`

A1 must inspect or request exact workflow setup / Codex readiness sources, including:

- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/stage_registry/STAGE_REGISTRY.md`
- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
- `workflow/stage_prompts/X0_EXECUTOR_PROJECT_SETUP.md`
- `workflow/stage_prompts/X1_EXECUTOR_RUN.md`
- `workflow/stage_prompts/U1_USER_GUIDED_EXECUTION.md`
- `workflow/stage_prompts/A1_AUDIT.md`
- `workflow/transport/STAGE_LAUNCH_CARD.md`
- `workflow/transport/CODEX_REPOSITORY_MAINTENANCE_APPLY.md`
- `workflow/transport/CODEX_WAVE_CARD.md`
- `workflow/transport/CODEX_RETURN_PACKET.md`
- `workflow/transport/USER_GUIDED_STEP_CARD.md`
- `docs/CHATGPT_PROJECT_SETUP.md`
- any exact project setup / tool-binding profile template discovered by A1.

A1 must not infer AGENTS.md, `.codex/config.toml`, Task Master, Serena, Basic Memory, validators, project/tool bindings, or product-repo local technical memory surfaces from governance notes. It must verify the existing workflow procedure or return Context Request with exact missing paths.

Do not run implementation, Unity bootstrap, old-code transfer, old-code audit as starting point, Codex product/project execution, Task Master graph creation, internal tool setup, or Game Documentation promotion.

## Required context after R1 H1_G2 acceptance

Recommended next stage: `M0_DIRECTION_MAP`.

Recommended next mode: `active_front_review_after_H1_G2_acceptance`.

M0 must review the active frontier after H1_G2 acceptance and decide whether
H1_G3 project/bootstrap/tool-binding/validation-scene readiness, P9, G0,
or another route is basis-valid.

Do not run implementation, Unity bootstrap, old-code transfer, old-code audit,
Codex product/project execution, Task Master graph creation, internal tool setup,
or Game Documentation promotion.

## Required context after M0 active-front review

Recommended next stage:

`G1_GOAL_SHAPE`

Recommended next mode:

`shape_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Selected next node:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Load for G1:

- `workflow/stage_prompts/G1_GOAL_SHAPE.md`
  - Status: `required_stage_prompt`
  - Reason: exact next stage prompt for shaping H1_G3.
- `directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md`
- `directions/indie-game-development/project_files/01_DIRECTION_STATE.md`
- `directions/indie-game-development/project_files/02_CURRENT_PHASE.md`
- `directions/indie-game-development/project_files/03_FOCUS_REGISTER.md`
- `directions/indie-game-development/project_files/04_ACTIVE_GOAL.md`
- `directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md`
- `directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md`
- `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
- `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/execution_log.md`

G1 must shape H1_G3 only. It must not run implementation, Unity bootstrap, product repository creation, old-code transfer, old-code audit as starting point, Codex product/project execution, Task Master graph creation, internal tool setup, Unity MCP setup, or Game Documentation promotion.

## Required context after G1 H1_G3 formalization

Recommended next stage: `E1_EXECUTION_BRIEF`.

Recommended next mode: `prepare_H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`.

Load for E1:

- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md`
  - Status: `required_stage_prompt`
  - Reason: exact next stage prompt for readiness execution brief.
- `WORKFLOW_SOURCE_OF_TRUTH.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
- `workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
- `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md`
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
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md`
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md`
  - Status: `goal_shaped_pending_E1_execution_brief`
  - Reason: active H1_G3 Goal Contract.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md`
  - Status: `active_goal_execution_log`
  - Reason: G1 formalization evidence.
- `directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md`
  - Status: `accepted_profile_artifact`
  - Reason: H1_G2 accepted profile remains required context for readiness planning.

E1 must prepare the H1_G3 readiness execution brief only. It must not run product execution directly, run Unity bootstrap, create a product repository, write product code, create a Task Master graph, configure real tools, install/configure Unity MCP, transfer old code, or promote Game Documentation.

## Required context after R1 H1_G3 acceptance

Recommended next stage: `P9_PHASE_CLOSE`.

Recommended next mode: `close_or_pause_core_coop_technical_foundation_selection_after_H1_G3_acceptance`.

```yaml
active_goal_after_r1_H1_G3_acceptance:
  active_goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  active_goal_status: r1_accepted_goal_complete
  accepted_product_local_artifacts:
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\outbox\\H1_G3_READINESS_PACKET.md"
    - "C:\\projects\\Unity\\GasCoopGame\\.workflow\\evidence\\h1-g3-readiness-2026-05-21.md"
  recommended_next_stage: P9_PHASE_CLOSE
  recommended_next_mode: close_or_pause_core_coop_technical_foundation_selection_after_H1_G3_acceptance
load_for_P9:
  - workflow/stage_prompts/P9_PHASE_CLOSE.md
  - directions/indie-game-development/project_files/00_DIRECTION_START_HERE.md
  - directions/indie-game-development/project_files/01_DIRECTION_STATE.md
  - directions/indie-game-development/project_files/02_CURRENT_PHASE.md
  - directions/indie-game-development/project_files/03_FOCUS_REGISTER.md
  - directions/indie-game-development/project_files/04_ACTIVE_GOAL.md
  - directions/indie-game-development/project_files/05_PORTFOLIO_QUEUE.md
  - directions/indie-game-development/project_files/06_CONTEXT_LIBRARY_INDEX.md
  - directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md
  - directions/indie-game-development/project_files/08_DIRECTION_MAP.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/execution_log.md
```

The P9 prompt path is listed as a source to acquire in the P9 runtime. Prompt text is not copied into this Project File.
