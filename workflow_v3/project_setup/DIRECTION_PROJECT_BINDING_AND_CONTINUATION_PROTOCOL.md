# Direction Project Binding and Continuation Protocol

status: active_binding_continuation_protocol

## Purpose

This protocol defines how an ordinary Workflow v3 Direction Project becomes bound to exactly one Direction after root bootstrap, and how later chats continue from current runtime status without relying on Project title, previous chat memory, Project Files/Sources authority, or whole-repository search.

It is repository source only. It does not create a concrete Direction runtime root, update an actual ChatGPT Project Instructions UI, refresh Project Files/Sources, or adopt a Direction.

## Problem statement

The universal ordinary Direction Project setup is intentionally pre-binding. It can start the first setup-only root/bootstrap chat before `direction_id` and `runtime_root` are accepted.

After that first chat, future chats in the same ChatGPT Project have no reliable memory of the bootstrap result. Without a persistent binding artifact and compact Project Instructions UI binding capsule, a new chat cannot safely determine:

- `direction_id`;
- `runtime_root`;
- `CURRENT_STATUS.md`;
- `CURRENT_NEXT_MOVE.md`;
- the per-Direction Project setup source.

The hidden failure mode is repeated guessing from Project title, stale Project Files/Sources, previous chat memory, or broad GitHub search. Those are not binding authority.

## Project Binding definition

Project Binding is the compact repository-backed configuration that connects one ordinary ChatGPT Direction Project to exactly one future Workflow v3 Direction runtime root.

It is not accepted product state, not Direction Map, not Work Graph, not Project title, and not previous chat memory.

## Binding authority order

1. Exact repository runtime binding file after an accepted package:
   `directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md`
2. Project Instructions UI binding capsule generated from the accepted binding.
3. Optional Project File binding cache, if uploaded, as cache/context only.
4. Current user-provided `direction_id` for repair/bootstrap only.

Not authority:

- Project title;
- previous chat memory;
- whole-repository search;
- stale Project Files/Sources;
- generated packs;
- summaries;
- uploaded excerpts that are not verified against exact repository state.

## Pre-binding state

Before accepted Project Binding exists, the universal ordinary Direction Project Instructions are installer instructions only.

The model must:

- ask for and normalize `direction_id` if missing;
- run root/bootstrap behavior from the bounded launch packet and bootstrap procedure;
- avoid product work;
- avoid concrete runtime root creation unless a bounded accepted package authorizes it;
- stop with a Context Request when required source or user decision is missing.

## Setup-only post-bootstrap state

After an accepted setup-only runtime root package creates a concrete runtime root, the package must also create or update the canonical runtime binding file and generate the per-Direction Project setup sources.

Project Binding may exist while semantic Direction definition is still pending. In that state:

- `DIRECTION_SPINE.md` is `pending_definition`;
- `DIRECTION_MAP.md` is `pending_definition`;
- `ACTIVE_FRONT.md` is `none_selected` or `pending_definition`;
- `CURRENT_STATUS.md` reports `setup_status: setup_only_root_created` and `semantic_definition_status: pending_definition`;
- `CURRENT_NEXT_MOVE.md` reports `primary_next_move: launch_direction_definition`.

The binding is stable enough for later chats to resolve status and route to Direction Definition. It is not proof of accepted semantic Direction content.

Later chats are stable only when at least one of these is available:

- the Project Instructions UI binding capsule generated from accepted binding; or
- a binding repair/bootstrap packet naming the exact repository path/ref to repair from.

## Required binding fields

The canonical binding must include:

- `direction_id`;
- `binding_status`;
- `project_type`;
- `runtime_root`;
- `current_status_path`;
- `current_next_move_path`;
- `direction_spine_path`;
- `direction_map_path`;
- `active_front_path`;
- `project_setup_source_path`;
- `project_files_manifest_path`;
- `project_instruction_payload_source_ref`;
- `accepted_root_package_ref`;
- `acceptance_decision_ref`;
- `source_authority`;
- `project_title_hint`;
- `project_title_is_not_authority`;
- `binding_capsule_payload`;
- `optional_project_file_cache_policy`;
- `update_policy`;
- `conflict_policy`;
- `limitations`.

## How binding is created

1. A setup-only root package or later authorized semantic adoption/root package prepares the future runtime root package.
2. The package includes `directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md` from `workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md`.
3. The package records the accepted root package ref and acceptance decision ref.
4. The package derives the compact binding capsule payload from the canonical runtime binding source.
5. The package reports separated Project refresh requirements.

The binding is accepted only through the same explicit acceptance/update path that accepts the runtime root package. This protocol does not accept or create any concrete binding by itself.

## How per-Direction Project Instructions source is created

After an accepted runtime root package exists, create the future concrete source at:

```text
directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Use repository template:

```text
workflow_v3/project_setup/PER_DIRECTION_PROJECT_INSTRUCTIONS_SOURCE_TEMPLATE.md
```

The generated source must include the compact binding capsule in the UI payload and must classify itself as a Project Instructions UI source, not a Project File/Source upload.

## How human applies Project Instructions UI update

Repository commit does not update the ChatGPT Project UI.

The human applies the concrete per-Direction Project Instructions UI payload manually by copying only the trimmed payload between:

```text
BEGIN_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
END_CHATGPT_PROJECT_INSTRUCTIONS_UI_PAYLOAD
```

The measured character count must be recorded. The payload must be generated from the canonical binding source, not typed from memory.

## How future chats resolve binding

A later chat in a bound ordinary Direction Project must:

1. Read the Project Instructions UI binding capsule visible in the current chat context.
2. Treat the capsule as a locator, not final proof, and use it to name exact repository paths.
3. Verify exact repository reads for the bound runtime root paths when material status or continuation depends on them.
4. Read only the bound Direction runtime root paths by default.
5. Stop with a binding repair request if binding is missing, conflicting, stale, or unreadable.

The chat must not search all Directions or all GitHub to infer the Direction.

## Status request protocol

For a status request such as `какой статус проекта?`, `what is the project status?`, or equivalent:

1. Resolve Project Binding first.
2. Read or request exact repository source for `current_status_path`.
3. Read or request exact repository source for `current_next_move_path`.
4. Do not read other Directions by default.
5. Return:
   - bound `direction_id`;
   - status summary from `CURRENT_STATUS.md`;
   - `semantic_definition_pending` when setup-only root exists and Direction Definition has not been accepted;
   - exact next move from `CURRENT_NEXT_MOVE.md`;
   - source/read limitations;
   - terminal outcome: answered, Context Request, binding repair required, or blocked.

## Missing binding behavior

If no binding capsule or canonical binding source is available:

- stop;
- do not answer status from memory;
- do not infer from Project title;
- do not search all Directions;
- ask for `direction_id` or a binding repair/bootstrap packet naming exact repo/path/ref.

## Conflicting binding behavior

If binding fields conflict across capsule, runtime binding, optional Project File cache, or user input:

- stop;
- report the conflicting fields and sources;
- ask for a binding repair package or exact repository binding path/ref to verify;
- do not continue status or product work until resolved.

## Missing GitHub access behavior

If exact repository state cannot be read:

- stop with a Context Request;
- name the exact repo/path/ref required;
- state that Project Files/Sources and pasted excerpts are cache/context until verified;
- do not proceed from stale or unverified binding.

## No whole-repo search rule

No chat may search the whole repository, all GitHub, all Directions, or all Project Files to infer which Direction the Project serves.

Whole-repository search is allowed only for bounded repository maintenance when the task explicitly authorizes it, not for binding inference.

## No other-Directions default-load rule

A bound ordinary Direction Project loads only its bound Direction runtime root by default.

Other Directions may be read only when a bounded task, accepted Direction Map relation, Check Job, or explicit user request names them.

## FINISH closure requirements

Material binding, repair, bootstrap, status review, and continuation work must close with:

- result;
- sources read;
- source/read limitations;
- candidate-state notice where applicable;
- unresolved questions;
- residual risks;
- binding status;
- exact next move or Context Request;
- terminal outcome.

## Setup-only continuation route

When binding resolves and exact state shows:

```text
setup_status: setup_only_root_created
semantic_definition_status: pending_definition
primary_next_move: launch_direction_definition
```

the next admitted material step is Direction Definition through `workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md` and `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md`.

Do not start product work, Work Graph, or Work Contract from setup-only state.

END_OF_FILE: workflow_v3/project_setup/DIRECTION_PROJECT_BINDING_AND_CONTINUATION_PROTOCOL.md
