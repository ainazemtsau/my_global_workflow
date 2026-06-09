# Procedure Registry

status: active_control_plane

## Purpose

This registry is the owner-procedure routing source for Workflow v3.

It lets START choose exactly one main procedure, then load that procedure file. It does not execute lifecycle stages, define completion, authorize child/adaptor calls, or replace the selected procedure source.

## Registry

| entrypoint | procedure_path | kind | trigger |
| --- | --- | --- | --- |
| `generic_answer` | `workflow_v3/procedures/GENERIC_ANSWER_PROCEDURE.md` | `readonly` | Lightweight non-state-sensitive answer, clarification, or default guidance. |
| `status_review` | `workflow_v3/procedures/STATUS_REVIEW_PROCEDURE.md` | `readonly` | Current status read without executing work. |
| `direction_project_root_bootstrap` | `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md` | `core` | Setup-only runtime root bootstrap for a future Direction. |
| `launch_direction_definition` | `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md` | `core` | Semantic Direction Definition after setup-only root. |
| `form_direction_spine` | `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` | `core` | Candidate Direction Spine formation. |
| `form_direction_map` | `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` | `core` | Candidate Direction Map formation. |
| `form_active_front` | `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` | `core` | Candidate Active Front selection. |
| `form_work_graph` | `workflow_v3/procedures/WORK_GRAPH_FORMATION_PROCEDURE.md` | `core` | Candidate local Work Graph formation. |
| `form_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_FORMATION_PROCEDURE.md` | `core` | Candidate bounded Work Contract formation. |
| `execute_work_contract` | `workflow_v3/procedures/WORK_CONTRACT_EXECUTION_PROCEDURE.md` | `core` | Execute one admitted Work Contract or produce a transfer for an allowed surface. |
| `parent_integration_check` | `workflow_v3/procedures/PARENT_INTEGRATION_CHECK_PROCEDURE.md` | `core` | Integrate returned child/work results into parent target. |
| `impact_propagation` | `workflow_v3/procedures/IMPACT_PROPAGATION_PROCEDURE.md` | `core` | Determine impact of invalidated assumptions or changed parent context. |
| `form_current_next_move` | `workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md` | `core` | Candidate Current Next Move / continuation-card formation. |
| `accept_candidate_entity` | `workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md` | `core` | Acceptance review for candidate entity output. |
| `promote_memory_artifact` | `workflow_v3/procedures/MEMORY_ARTIFACT_PROMOTION_PROCEDURE.md` | `core` | Candidate Memory Artifact promotion. |
| `persist_accepted_state` | `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` | `storage` | Persist from a complete admitted Storage Update Package only. |
| `codex_handoff` | `workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md` | `utility` | Child/adaptor schema for bounded Codex or future code-assistant work under a selected parent RUN. |
| `codex_result_verification` | `workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md` | `verification` | Verify returned code-assistant result evidence. |
| `recovery_review` | `workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md` | `core` | Review suspect state, evidence, or routing. |
| `author_workflow_procedure` | `workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md` | `core` | Author or integrate Workflow v3 procedures. |

## Kind Values

Allowed `kind` values:

- `core` - selectable main procedure for material Workflow v3 work.
- `utility` - child/adaptor schema callable only during RUN under a selected main/core parent; not a standalone material chat or terminal artifact.
- `verification` - child/adaptor verification schema callable during RUN or through an admitted parent/core verification owner; not standalone package completion.
- `storage` - selectable only for an admitted persistence package; writes are bounded by that procedure.
- `readonly` - selectable for non-material reads or answers.

## Lookup Rule

START reads this registry first and selects exactly one entrypoint for the current concrete work item. Selection is exact-fit, not nearest-fit.

After selection, START reads the selected `procedure_path` and uses that procedure's completion block as the completion authority for CHECK and FINISH. If the user asks for multiple independent work items, return `SPLIT_REQUIRED` before material work.

The `trigger` text helps choose the file. It is not execution logic, a child/adaptor call graph, or a completion rule.

Specialized `core`, `storage`, `utility`, or `verification` entries must not be selected by keyword overlap, indirect semantic similarity, user momentum, or closest available match. Before specialized selection, the current concrete work item must fit the entry's trigger, kind, work boundary, and required inputs.

`generic_answer` may be selected only for lightweight, non-material, non-state-sensitive guidance when no more specific exact-fit entry applies.

If no entry matches and the request cannot be safely normalized into one registered entrypoint, return `UNREGISTERED_ACTION_EXCEPTION`. If the unmatched request is material or state-sensitive, return `CONTEXT_REQUEST`, `UNREGISTERED_ACTION_EXCEPTION`, `BOUNDARY_CROSSING_STOP`, or the selected procedure's explicit blocked escalation instead of selecting a nearby procedure.

If the user asks only for a Codex card, handoff, package, check packet, storage packet, or other child/adaptor envelope without an admitted parent/core procedure goal, START must route to a registered owner procedure that can own the material goal, or return `UNREGISTERED_ACTION_EXCEPTION` / blocked scope. A child/adaptor entry must not become a standalone package material chat.

## Boundary

This file must not contain lifecycle execution logic, stage execution rules, child/adaptor call flow, storage mutation rules, or completion semantics. Those live in the selected procedure and the control-plane protocols.

END_OF_FILE: workflow_v3/control_plane/PROCEDURE_REGISTRY.md
