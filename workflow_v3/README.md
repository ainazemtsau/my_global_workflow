# Workflow v3

status: active_skeleton_namespace_corrected

## Purpose

`workflow_v3/**` is the clean-start Workflow v3 skeleton namespace.

Workflow v3 is now main-procedure driven: the registry selects one main procedure, the selected procedure defines completion, lifecycle executes visible stages, utilities support the same procedure, CHECK verifies completion, and FINISH closes only after audit passes.

## Runtime Kernel

Active runtime authority:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` - compact procedure selector with `entrypoint`, `procedure_path`, `kind`, and `trigger`.
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` - START, RUN, UTILITY, CHECK, FINISH, CLOSED.
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` - provider-neutral utility calls and returns.
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` - final audit and closure.
- `workflow_v3/procedures/PROCEDURE_DEFINITION_CANON.md` - procedure completion, material stages, internal checks, and utility policy.

There is no separate start protocol, before-action protocol, or old operation-surface contract in active Workflow v3 authority.

## Required Runtime Signals

- `START_CONTRACT` before material work.
- `STAGE_RESULT` after each material stage.
- `UTILITY_CALL` / `UTILITY_RETURN` when supporting utility work is needed.
- `CLOSURE_CHECK` before FINISH.
- `NEXT_CHAT_CARD` when a closed material workflow needs continuation.

## Procedure Completion

Procedure implementation status is authoritative only in each procedure file header. README, interface, and completion files summarize routing and coverage; they do not define procedure readiness.

Every selectable procedure contains:

```text
completion:
  result:
  proof:
  blocked_if:
```

CHECK compares actual result to that selected procedure block. Workflow v3 does not define a global fixed done/result enum.

## Project Setup

Project Instructions sources are compact bootstraps. They are not accepted state and should not duplicate full procedure bodies.

When changed files affect ChatGPT Projects, report:

- `project_instruction_ui_update_required`
- `project_instruction_ui_payload_char_counts`
- `project_sources_files_refresh_required`
- `request_only_sources_refresh_required`
- `do_not_upload_as_project_file`

## Key Directories

- `workflow_v3/control_plane/**` - runtime kernel and supporting source/storage/exception protocols.
- `workflow_v3/procedures/**` - selectable procedure source and framework.
- `workflow_v3/templates/**` - user-visible packet/card templates.
- `workflow_v3/interfaces/**` - summaries that point back to authority.
- `workflow_v3/evals/**` - invariant checks.
- `workflow_v3/project_setup/**` - Project Instructions and setup sources.
- `workflow_v3/completion/**` - completion and coverage summaries.

END_OF_FILE: workflow_v3/README.md
