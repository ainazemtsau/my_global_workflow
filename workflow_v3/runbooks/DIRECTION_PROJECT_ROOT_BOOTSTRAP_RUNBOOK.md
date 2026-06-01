# Direction Project Root Bootstrap Runbook

status: active_project_bootstrap_runbook

## Purpose

This runbook defines the operational path for the first chat in a newly created ordinary Workflow v3 Direction Project.

It is setup/root bootstrap only. It does not execute product work, import legacy state, or create runtime root files by itself.

## Trigger

Use this runbook when a newly created ordinary Direction Project has no accepted runtime root.

The assumed missing root is:

```text
directions_v3/<direction-id>/runtime/**
```

## Signals

- `direction_runtime_missing`
- `direction_adoption_needed`
- `direction_spine_missing`
- `direction_map_missing`
- `active_front_missing`
- `blocked_lifecycle_transition`

## Handlers

- `direction_adoption_guard_handler`: blocks implicit adoption, legacy import, and unauthorized root creation.
- `direction_spine_creation_handler`: prepares or reviews a candidate initial Direction Spine only after required inputs are clear.
- `direction_map_creation_handler`: prepares or reviews a candidate initial Direction Map without flattening it into Spine, roadmap, backlog, Work Graph, or Action Inbox.
- `active_front_selection_handler`: prepares or reviews a candidate Active Front selected from Direction Map areas.

## Expected path

1. Identify and normalize `direction_id`.
2. Check whether exact repository evidence proves an accepted runtime root already exists.
3. If no accepted runtime root exists, emit `direction_runtime_missing`.
4. Classify `adoption_mode`; default only when the user decision is clear.
5. Stop if the Direction identity, adoption mode, legacy evidence policy, or initial root outcome is missing.
6. Ask whether old `directions/**` files are read-only `legacy_evidence` or not used.
7. Do not treat old `workflow/**` or `directions/**` as v3 target state.
8. Produce a clean-start adoption/root package only after the user confirms that this is the desired next step.
9. If the user confirms a clean-start root package, require the package to include runtime binding config and per-Direction Project setup source generation.
10. Do not create actual runtime root files until a bounded Codex package is accepted and merged.
11. Treat root bootstrap as incomplete for later chats until binding capsule/manual UI update is planned or completed.
12. Return a bounded root bootstrap status, missing inputs or candidate package, binding installation next move, and exact next move.

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
```

`primary_next_move` must be exactly one of:

- request missing Direction identity or adoption decision;
- request explicit user confirmation for a clean-start adoption/root package;
- prepare a bounded Codex package for accepted runtime root creation;
- prepare or apply post-bootstrap Project Binding and per-Direction Project Instructions source;
- perform acceptance review of a returned package;
- stop.

## Hard boundaries

- No product execution during setup/root bootstrap.
- No legacy import during setup/root bootstrap.
- No accepted state without explicit acceptance/update path.
- No Project Files/Sources refresh from this runbook alone.
- No actual Project UI update from this runbook alone.

END_OF_FILE: workflow_v3/runbooks/DIRECTION_PROJECT_ROOT_BOOTSTRAP_RUNBOOK.md
