# 03_FOCUS_REGISTER.md

```yaml
project_file_control:
  file: 03_FOCUS_REGISTER.md
  schema: project_file_projection.v1
  direction: directions/indie-game-development
  source_files:
    - "directions/indie-game-development/project_files/03_FOCUS_REGISTER.md"
  activated_at: "2026-05-13"
  source_freshness: fresh_after_r1_h1_g4a_foundation_acceptance
  canonical_source: GitHub repository file
  conflict_rule: if this file conflicts with another current GitHub Direction file, return Context Request; do not invent state
  default_load: yes
```

```yaml
focus:
  current_focus: "Run P9 phase close for H1_G4A after accepted product-facing foundation."
  route_stage: P9_PHASE_CLOSE
  route_mode: close_or_pause_h1_g4a_core_harness_composition_validation_topology_interface_foundation_after_r1_acceptance
  same_chat_allowed: false
  boundary_trigger: r1_h1_g4a_foundation_accepted
  pending_state_carried: true
  pending_patch_pointer: r1_accept_h1_g4a_foundation_and_prepare_p9_2026_05_23
  last_stage_result_pointer: "R1_GOAL_REVIEW_DISTILL accepted h1-g4a-core-harness-composition-validation-topology-interface-foundation as r1_accepted_goal_complete."
  last_codex_scope_validation: "Codex repository maintenance only; Codex product/project execution remains blocked until project/tool bindings and execution route are verified."
  implementation_allowed_now: false
  codex_product_execution_allowed_now: false
  active_goal:
    goal_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
    status: r1_accepted_goal_complete
    goal_contract: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md"
    previous_goal_id: h1-g4-first-runnable-technical-nucleus-slice
    previous_goal_status: superseded_by_h1_g4a_boundary_repair_partial_evidence_only
  active_phase:
    phase_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
    phase_name: "H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation"
    phase_path: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation"
    status: active_goal_r1_accepted_pending_P9_phase_close
    map_binding: "H1_playable_technical_nucleus / H1_G4A_core_harness_composition_validation_topology_interface_foundation"
    next_route: P9_PHASE_CLOSE
```

## Blockers / required inputs

- Missing context: `repository maintenance read-back and manual Project Files refresh required before P9 launch`
- Human decision: `none pending for P9 launch after refresh`
- Source conflict: `Project Files require R1 acceptance read-back and manual refresh before P9 because this patch changes Project Files`
- Tool/runtime blocker: `project/tool bindings must be verified before Codex product/project execution`
- Required attachments/context for next stage:
  - exact `workflow/stage_prompts/P9_PHASE_CLOSE.md`
  - refreshed Project Files 00-08 after H1_G4A R1 acceptance
  - `directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_PHASE_BRIEF.md`
  - `directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/phase_execution_log.md`
  - `directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md`
  - `directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/execution_log.md`
  - `directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md`
  - `directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md`
  - `directions/indie-game-development/project_files/08_DIRECTION_MAP.md`

## Current focus boundary

G1 formalized `h1-g4a-core-harness-composition-validation-topology-interface-foundation` after A1 determined direct E1 repair of the broad H1_G4 route-gated state was not basis-valid.

H1_G4A is the controlling current focus.

The next focus is `P9_PHASE_CLOSE` for H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation after R1 accepted the product-facing foundation. P9 must close or pause the H1_G4A Phase using the accepted evidence and compact Phase Delivery Graph. It must not start H1_G4B, Grid/Topology implementation, Gas Simulation implementation, Grid-Gas interaction, Multiplayer implementation, Unity MCP setup, Task Master graph creation, old-code transfer, Game Documentation promotion, broad vertical slice expansion, or Codex product/project execution directly.

Forbidden in this focus:

- implementation;
- Unity bootstrap;
- old-code transfer;
- old-code audit as starting point;
- Codex product/project execution;
- Task Master graph creation;
- Game Documentation promotion;
- real internal tool setup;
- broad engineering handbook creation;
- direct X0/X1 launch without E1 readiness envelope and setup-state proof.

## 2026-05-19 G1 H1_G2 formalization

```yaml
focus_update_after_g1_H1_G2:
  active_goal_id: H1_G2_codex_development_operating_model_and_architecture_protocols
  active_goal_status: goal_shaped_pending_A1_audit
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/codex-development-operating-model-and-architecture-protocols/00_GOAL_CONTRACT.md"
  next_route: A1_AUDIT
  next_route_mode: audit_existing_workflow_codex_project_setup_first_use_fit
  core_correction: >
    This Goal must audit/fit-check the existing workflow Codex/project setup
    procedure. It must not create a second Indie-only workflow layer.
  forbidden:
    - implementation
    - Unity bootstrap
    - Codex product/project execution
    - Task Master graph creation
    - real internal tool setup
    - old-code transfer
    - old-code audit as starting point
    - Game Documentation promotion
```

## Historical focus after G1 reset

The focus after F0 synthesis formalization and evidence repair was R1 parent Goal review for `first-technical-nucleus-functional-spec`.

G1 superseded the transfer-boundary audit as the active Goal after human clarification.

R1 must verify that gas-first sequencing and the user approval gate after `gas_simulation_capability_frame` were preserved before accepting or route-gating the parent Goal.

## 2026-05-20 R1 H1_G2 acceptance focus update

H1_G2 is accepted as complete.

Current focus is repository projection reconciliation and then M0 active-front review.
M0 must determine the next basis-valid route after H1_G2 acceptance.

## 2026-05-20 M0 active-front review focus update

M0 selected:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Next focus:

`G1_GOAL_SHAPE`

G1 must shape the H1_G3 Goal Contract for project bootstrap, tool-binding, and validation-scene readiness.

This focus does not authorize execution. It does not create product repo, Unity project, Codex config, AGENTS.md, Task Master graph, Serena, Basic Memory, Unity MCP, scenes, prefabs, assets, scripts, old-code transfer, or implementation.

## 2026-05-20 G1 H1_G3 formalization focus update

G1 shaped:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Current route:

```yaml
route_stage: E1_EXECUTION_BRIEF
route_mode: prepare_H1_G3_readiness_execution_brief
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/core-coop-technical-foundation-selection/goals/project-bootstrap-tool-binding-validation-scene-readiness/00_GOAL_CONTRACT.md"
same_chat_allowed: false
codex_product_execution_allowed_now: false
```

E1 must plan the readiness envelope only. Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-21 R1 H1_G3 acceptance focus update

R1 accepted:

`H1_G3_project_bootstrap_tool_binding_validation_scene_readiness`

Current route:

```yaml
route_stage: P9_PHASE_CLOSE
route_mode: close_or_pause_core_coop_technical_foundation_selection_after_H1_G3_acceptance
boundary_trigger: r1_H1_G3_readiness_packet_accepted
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: r1_accepted_goal_complete
active_phase:
  status: active_H1_G3_r1_accepted_pending_P9_phase_close
codex_product_execution_allowed_now: false
```

P9 may close or pause the Phase after H1_G3 readiness acceptance. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-21 P9 phase close focus update

P9 closed:

`Core Co-op Technical Foundation Selection`

Current route:

```yaml
route_stage: P0_PHASE_START
route_mode: start_next_phase_after_core_coop_technical_foundation_selection_close
boundary_trigger: p9_core_coop_technical_foundation_selection_closed
active_goal:
  goal_id: H1_G3_project_bootstrap_tool_binding_validation_scene_readiness
  status: closed_with_phase / r1_accepted_goal_complete
active_phase:
  status: closed_complete_by_P9
implementation_allowed_now: false
codex_product_execution_allowed_now: false
required_context_for_next_stage:
  - exact workflow/stage_prompts/P0_PHASE_START.md
  - refreshed Project Files 00-08 after P9 close
  - directions/indie-game-development/phases/core-coop-technical-foundation-selection/phase_close_summary.md
  - directions/indie-game-development/project_files/07_PHASE_MEMORY_INDEX.md
  - directions/indie-game-development/project_files/08_DIRECTION_MAP.md
```

P0 must start/reframe the next Phase. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-21 P0 phase start focus update

P0 started:

`Project Bootstrap and Validation Surface Setup`

Current route:

```yaml
route_stage: G1_GOAL_SHAPE
route_mode: shape_bootstrap_validation_surface_setup_envelope
same_chat_allowed: false
boundary_trigger: p0_project_bootstrap_validation_surface_setup_started
active_phase_id: project-bootstrap-validation-surface-setup
active_phase_status: active_pending_G1_goal_shape
active_goal_id: none_active_pending_G1_goal_shape
selected_first_goal_candidate: bootstrap-validation-surface-setup-envelope
implementation_allowed_now: false
codex_product_execution_allowed_now: false
```

G1 must shape the setup/validation envelope Goal before any bootstrap, setup, product repository creation, product code, Codex product/project execution, Task Master graph creation, Unity MCP setup, old-code transfer, or Game Documentation promotion.

## 2026-05-22 G1 formalization focus update

G1 shaped:

`bootstrap-validation-surface-setup-envelope`

Current route:

```yaml
route_stage: E1_EXECUTION_BRIEF
route_mode: prepare_bootstrap_validation_surface_setup_envelope_execution_brief
boundary_trigger: g1_bootstrap_validation_surface_setup_envelope_formalized
active_goal:
  goal_id: bootstrap-validation-surface-setup-envelope
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/00_GOAL_CONTRACT.md"
active_phase:
  status: active_goal_shaped_pending_E1_execution_brief
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

E1 must prepare the setup/validation envelope execution brief only. Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-22 R1 acceptance focus update

R1 accepted:

`bootstrap-validation-surface-setup-envelope`

Current route:

```yaml
route_stage: P9_PHASE_CLOSE
route_mode: close_or_pause_project_bootstrap_validation_surface_setup_after_envelope_acceptance
boundary_trigger: r1_bootstrap_validation_surface_setup_envelope_accepted
active_goal:
  goal_id: bootstrap-validation-surface-setup-envelope
  status: r1_accepted_goal_complete
  accepted_artifact: "directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/goals/bootstrap-validation-surface-setup-envelope/01_BOOTSTRAP_VALIDATION_SURFACE_SETUP_ENVELOPE.md"
active_phase:
  status: active_goal_r1_accepted_pending_P9_phase_close
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

P9 must close or pause the Project Bootstrap and Validation Surface Setup Phase after acceptance. Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-22 P9 phase close focus update

P9 closed:

`Project Bootstrap and Validation Surface Setup`

Current route:

```yaml
route_stage: P0_PHASE_START
route_mode: start_next_phase_after_project_bootstrap_validation_surface_setup_close
same_chat_allowed: false
boundary_trigger: p9_project_bootstrap_validation_surface_setup_closed
active_goal:
  goal_id: bootstrap-validation-surface-setup-envelope
  status: closed_with_phase
active_phase:
  phase_id: project-bootstrap-validation-surface-setup
  status: closed_complete_by_P9
required_context_for_next_stage:
  - exact workflow/stage_prompts/P0_PHASE_START.md
  - refreshed Project Files 00-08 after P9 close
  - directions/indie-game-development/phases/project-bootstrap-validation-surface-setup/phase_close_summary.md
codex_product_execution_allowed_now: false
```

P0 must start/reframe the next Phase. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-22 P0 H1_G4 first runnable build focus update

P0 started:

`H1_G4 Durable Technical Nucleus — First Runnable Build`

Current route:

```yaml
route_stage: G1_GOAL_SHAPE
route_mode: shape_h1_g4_first_runnable_technical_nucleus_slice
boundary_trigger: p0_h1_g4_first_runnable_build_phase_started
active_goal:
  goal_id: none_active_pending_G1_goal_shape
  status: none_active_pending_G1_goal_shape
  selected_first_goal_candidate: h1-g4-first-runnable-technical-nucleus-slice
  selected_first_goal_candidate_status: selected_for_G1_goal_shape
active_phase:
  phase_id: h1-g4-durable-technical-nucleus-first-runnable-build
  status: active_pending_G1_goal_shape
required_context_for_next_stage:
  - exact workflow/stage_prompts/G1_GOAL_SHAPE.md
  - refreshed Project Files 00-08 after P0 phase start
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/phase_execution_log.md
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

G1 must shape the first runnable H1_G4 technical nucleus Goal. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-22 G1 H1_G4 first runnable Goal formalization focus update

G1 formalized:

`h1-g4-first-runnable-technical-nucleus-slice`

Current route:

```yaml
route_stage: E1_EXECUTION_BRIEF
route_mode: prepare_h1_g4_first_runnable_technical_nucleus_slice_execution_brief
boundary_trigger: g1_h1_g4_first_runnable_technical_nucleus_slice_formalized
active_goal:
  goal_id: h1-g4-first-runnable-technical-nucleus-slice
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/00_GOAL_CONTRACT.md"
active_phase:
  phase_id: h1-g4-durable-technical-nucleus-first-runnable-build
  status: active_goal_shaped_pending_E1_execution_brief
required_context_for_next_stage:
  - exact workflow/stage_prompts/E1_EXECUTION_BRIEF.md
  - refreshed Project Files 00-08 after G1 Goal formalization
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/phase_execution_log.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/execution_log.md
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

E1 must prepare the execution brief for the shaped Goal. Implementation, Unity bootstrap, product repository creation, product code, Codex product/project execution, Task Master graph creation, real internal tool setup, Unity MCP setup, old-code transfer, and Game Documentation promotion remain blocked.

## 2026-05-22 focus update — E1 repair after R1 route gate

Current focus:

Prepare `E1_EXECUTION_BRIEF` for the H1_G4 Codex Operator Report and Unity validation contract repair.

The goal is not a new test task. The subject is the existing H1_G4 TechnicalNucleus slice.

E1 must require X1/Codex to return a user-facing Markdown report with:
- plain-language implementation summary;
- architecture summary without code dump;
- Unity-as-render-engine self-check;
- changed files and why they matter;
- validation commands and evidence;
- exact Unity manual verification steps;
- scene/editor setup steps if needed;
- product persistence state;
- unresolved risks.

YAML is forbidden as the user-facing Codex report format. YAML is not a user-facing Codex Operator Report format. YAML may be used only as hidden/technical workflow transport when required.

## 2026-05-23 focus update — H1_G4A boundary formalized

Current focus:

Prepare E1 execution brief for H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation.

```yaml
route_stage: E1_EXECUTION_BRIEF
route_mode: prepare_h1_g4a_core_harness_composition_validation_topology_interface_foundation_execution_brief
boundary_trigger: g1_h1_g4a_core_harness_boundary_formalized
active_goal:
  goal_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  status: goal_shaped_pending_E1_execution_brief
  goal_contract: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md"
active_phase:
  phase_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  status: active_goal_shaped_pending_E1_execution_brief
required_context_for_next_stage:
  - exact workflow/stage_prompts/E1_EXECUTION_BRIEF.md
  - refreshed Project Files 00-08 after H1_G4A repository maintenance
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/phase_execution_log.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/execution_log.md
superseded_context_request_only:
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/phase_execution_log.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/h1-g4-durable-technical-nucleus-first-runnable-build/goals/h1-g4-first-runnable-technical-nucleus-slice/execution_log.md
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

E1 must preserve the forbidden surfaces: Unity MCP setup, Task Master graph creation, old-code transfer, Game Documentation promotion, broad vertical slice expansion, and product execution before a valid execution route.

## 2026-05-23 focus update — H1_G4A foundation accepted

Current focus:

Run P9 phase close for H1_G4A Core Harness / Composition / Validation / Topology Interface Foundation.

```yaml
route_stage: P9_PHASE_CLOSE
route_mode: close_or_pause_h1_g4a_core_harness_composition_validation_topology_interface_foundation_after_r1_acceptance
boundary_trigger: r1_h1_g4a_foundation_accepted
active_goal:
  goal_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  status: r1_accepted_goal_complete
  goal_contract: "directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md"
active_phase:
  phase_id: h1-g4a-core-harness-composition-validation-topology-interface-foundation
  status: active_goal_r1_accepted_pending_P9_phase_close
required_context_for_next_stage:
  - exact workflow/stage_prompts/P9_PHASE_CLOSE.md
  - refreshed Project Files 00-08 after H1_G4A R1 acceptance repository maintenance
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_PHASE_BRIEF.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/phase_execution_log.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/00_GOAL_CONTRACT.md
  - directions/indie-game-development/phases/h1-g4a-core-harness-composition-validation-topology-interface-foundation/goals/h1-g4a-core-harness-composition-validation-topology-interface-foundation/execution_log.md
product_evidence_pointers:
  - ainazemtsau/GasCoopGame@236bc30e1cfc9aa081325144d778d1f28283aa63
  - MODULE_MAP.md
  - .workflow/outbox/H1_G4A_OPERATOR_REPORT.md
  - .workflow/evidence/h1-g4a-foundation-2026-05-23.md
codex_product_execution_allowed_now: false
implementation_allowed_now: false
```

P9 must preserve the forbidden surfaces: H1_G4B start, Grid/Topology implementation, Gas Simulation implementation, Grid-Gas interaction, Multiplayer implementation, Unity MCP setup, Task Master graph creation, old-code transfer, Game Documentation promotion, and product execution.
