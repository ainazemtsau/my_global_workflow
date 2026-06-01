# Direction Project Root Bootstrap Runbook

status: active_project_bootstrap_runbook

## Purpose

This runbook defines the operational path for the first chat in a newly created ordinary Workflow v3 Direction Project.

It is setup-only root bootstrap. It does not define semantic Direction content, execute product work, import legacy state, or create runtime root files by itself.

## Trigger

Use this runbook when a newly created ordinary Direction Project has no accepted runtime root.

The assumed missing root is:

```text
directions_v3/<direction-id>/runtime/**
```

## Signals

- `direction_runtime_missing`
- `direction_adoption_needed`
- `blocked_lifecycle_transition`

## Handlers

- `direction_adoption_guard_handler`: blocks implicit adoption, legacy import, product work, and unauthorized root creation.
- `progression_router_handler`: routes setup-only closure to `launch_direction_definition` after a setup-only root package exists.

## Expected path

1. Identify and normalize `direction_id`.
2. Check whether exact repository evidence proves an accepted runtime root already exists.
3. If no accepted runtime root exists, emit `direction_runtime_missing`.
4. Classify setup mode as `setup_only_root_bootstrap`.
5. Ask whether old `directions/**` files are read-only `legacy_evidence` or not used.
6. Do not require root outcome, Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.
7. If the user provides semantic content, store it only as `candidate_context_for_direction_definition`.
8. Do not treat old `workflow/**` or `directions/**` as v3 target state.
9. Produce a setup-only runtime root package only after the user confirms that this is the desired next step.
10. Require the package to include placeholder pending semantic statuses, runtime binding config, and per-Direction Project setup source generation.
11. Do not create actual runtime root files until a bounded Codex package is accepted and merged.
12. Treat root bootstrap as incomplete for later chats until binding capsule/manual UI update is planned or completed.
13. Return setup-only root status, missing inputs or candidate package, binding installation next move, and exact next move `launch_direction_definition`.

## Closure

Every bootstrap run ends with Event Loop Closure.

The closure must include:

```text
closure_signal:
handlers_considered:
primary_next_move:
return_destination:
blocked_reason_if_any:
project_refresh_requirements:
binding_installation_next_move:
semantic_definition_status:
candidate_context_for_direction_definition:
```

`primary_next_move` must be exactly one of:

- request missing Direction identity or adoption decision;
- request explicit user confirmation for a setup-only root package;
- prepare a bounded Codex package for accepted setup-only runtime root creation;
- prepare or apply post-bootstrap Project Binding and per-Direction Project Instructions source;
- launch Direction Definition;
- perform acceptance review of a returned package;
- stop.

## Hard boundaries

- No product execution during setup/root bootstrap.
- No legacy import during setup/root bootstrap.
- No setup-time acceptance of Direction Spine, Direction Map, Active Front, Work Graph, or product strategy.
- No accepted state without explicit acceptance/update path.
- No Project Files/Sources refresh from this runbook alone.
- No actual Project UI update from this runbook alone.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_PROJECT_ROOT_BOOTSTRAP_RUNBOOK.md
