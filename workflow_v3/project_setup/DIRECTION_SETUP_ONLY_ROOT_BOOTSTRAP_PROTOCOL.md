# Direction Setup-Only Root Bootstrap Protocol

status: active_setup_only_bootstrap_protocol

## Purpose

This protocol separates ordinary Direction Project technical setup from semantic Direction Definition.

Setup-only root bootstrap creates the technical continuation surface for a future Direction. It does not accept Direction Spine, Direction Map, Active Front, product strategy, business strategy, or product execution.

## Setup-only root bootstrap versus Direction Definition

Setup-only root bootstrap may decide technical identity and setup shape.

Direction Definition is the later material entity-formation process that forms candidate Direction Spine, Direction Map, and Active Front.

## Setup may decide

- `direction_id`;
- `setup_mode: setup_only_root_bootstrap`;
- `legacy_policy: no_import | read_only_legacy_evidence`;
- `runtime_root_path`;
- Project Binding plan;
- per-Direction Project setup source plan;
- placeholder runtime state with pending statuses;
- `CURRENT_STATUS = setup_only_root_created`;
- `CURRENT_NEXT_MOVE = launch_direction_definition`.

## Setup must not decide

- root outcome;
- Direction Spine content;
- Direction Map content;
- Active Front;
- Work Graph;
- product strategy;
- business strategy;
- product execution.

## Candidate context handling

If the user supplies outcome, tracks, product ideas, goals, constraints, or strategy during setup, record them only as:

```text
candidate_context_for_direction_definition:
```

This context may be passed to Direction Definition. It is not accepted state and does not bypass formation.

## Setup-only runtime root package requirements

A future accepted setup-only root package must create only technical placeholder state and binding/setup surfaces. It must not store accepted semantic Direction content.

Required placeholder statuses:

```text
DIRECTION_SPINE.md = pending_definition
DIRECTION_MAP.md = pending_definition
ACTIVE_FRONT.md = none_selected or pending_definition
CURRENT_STATUS.md = setup_only_root_created
CURRENT_NEXT_MOVE.md = launch_direction_definition
```

## Binding requirement

The setup-only package must include Project Binding config so future chats can resolve `direction_id`, runtime root, `CURRENT_STATUS.md`, and `CURRENT_NEXT_MOVE.md` without relying on Project title or previous chat memory.

## Per-Direction Project setup source requirement

The setup-only package must include per-Direction Project Instructions source and Project Files manifest source for future manual Project setup.

## Manual Project Instructions UI update requirement

After the setup-only root package is merged, the human must manually update the Project Instructions UI from the generated per-Direction source. Repository commit alone does not perform that update.

## Event Loop Closure requirements

Setup-only bootstrap closes with:

```text
result:
candidate_context_for_direction_definition:
setup_status: setup_only_root_created | blocked
semantic_definition_status: pending_definition
project_binding_status:
project_refresh_requirements:
primary_next_move: launch_direction_definition
transition_packet_or_next_chat_prompt:
```

## Boundary

This protocol is repository source only. It does not create a concrete runtime root.

END_OF_FILE: workflow_v3/project_setup/DIRECTION_SETUP_ONLY_ROOT_BOOTSTRAP_PROTOCOL.md
