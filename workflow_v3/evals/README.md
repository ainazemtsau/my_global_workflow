# Workflow v3 Evals

status: active_repository_validation_aids
runtime_authority: false
procedure_authority: false
load_rule: do_not_load_for_runtime; use only when an exact procedure or repository validation task explicitly names an eval file
conflict_rule: selected procedure and lifecycle/control-plane protocols win

## Purpose

This directory contains repository-side validation aids for Workflow v3 packages and future Direction runtime packages.

Evals do not create accepted state, define runtime stages, define completion, or override selected `*_PROCEDURE.md` files. Procedure-local `Quality Checks`, gates, stop conditions, completion contracts, `CLOSURE_CHECK`, and `FINISH` compatibility are the primary validation surface for runtime procedure work.

Individual eval files may classify evidence as PASS, WARN, or FAIL for repository review only. A file marked `status: active_eval` is active only as a repository validation aid; it is not runtime or procedure authority. Domain-specific eval files must not require work that belongs to registered procedures. Useful checks from a retired eval should be migrated into procedure-local `Quality Checks`, template guidance, or returned as material for the owning authoring run.

## Eval index

- `WORKFLOW_V3_COMPLETION_VALIDATION_CHECKLIST.md`
- `DIRECTION_RUNTIME_BOOTSTRAP_EVAL.md`
- `DIRECTION_MAP_FRONT_GRAPH_EVAL.md`
- `GOAL_EVIDENCE_GRAPH_EVAL.md`
- `ACTIVE_UNRESOLVED_CUT_EVAL.md`
- `PARENT_INTEGRATION_RESULT_EVAL.md`
- `IMPACT_PROPAGATION_EVAL.md`
- `DERIVED_GATE_CHECK_EVAL.md`
- `MEMORY_INDEX_EVAL.md`
- `NO_HOLLOW_LAYER_EVAL.md`
- `NO_SINGLE_TRACK_COLLAPSE_EVAL.md`
- `FINISH_PACKET_EVAL.md`
- `NEXT_MOVE_PACKET_EVAL.md`
- `CHAT_LIFECYCLE_HANDOFF_EVAL.md`
- `CODEX_HANDOFF_RESULT_EVAL.md`
- `PROJECT_SETUP_ROLLOUT_EVAL.md`
- `LEGACY_EVIDENCE_BOUNDARY_EVAL.md`
- `NO_HIDDEN_STATE_OR_ROUTE_EVAL.md`
- `PROCEDURE_DEFINITION_EVAL.md`
- `PROCEDURE_EXECUTION_EVAL.md`

END_OF_FILE: workflow_v3/evals/README.md
