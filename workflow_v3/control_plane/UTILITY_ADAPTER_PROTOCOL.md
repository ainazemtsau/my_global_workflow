# Utility Adapter Protocol

status: active_control_plane

## Purpose

Defines Workflow v3 procedure classes, embedded utility/adapter use, RUN external handoff/return, and related closure boundaries.

## Procedure classes

Allowed `procedure_class` values:

- `core_material`
- `utility_adapter`
- `verification_adapter`
- `storage_adapter`
- `readonly_console`

## Owner procedure rule

START selects exactly one owner procedure. Embedded utility/adapter use during RUN does not change `selected_entrypoint` or `selected_procedure_ref`.

Core procedures do not call other procedures. They may emit typed utility packets only when the selected procedure source and run surface allow the relevant utility category.

## Utility categories

Allowed `utility_category` values:

- `codex_handoff_packet`
- `codex_return_verification`
- `check_job_packet`
- `child_chat_packet`
- `child_research_packet`
- `storage_update_package`
- `project_refresh_instruction_packet`

## RUN external handoff

`RUN_EXTERNAL_HANDOFF` is an internal RUN gate used when the selected owner procedure requires an external utility result before completion. It is not FINISH_REQUEST, not FINISH, not a Next Move Packet, and not procedure switching.

Required shape:

```text
RUN_EXTERNAL_HANDOFF:
  lifecycle_state: RUN_WAITING_FOR_EXTERNAL_RETURN
  owner_entrypoint:
  owner_procedure_ref:
  utility_category:
  external_surface:
  handoff_purpose:
  copy_paste_packet:
  expected_return_packet:
  validation_required_before_resume:
  resume_rule:
```

While a required `RUN_EXTERNAL_HANDOFF` is pending, RUN must not emit FINISH_REQUEST.

## RUN external return

`RUN_EXTERNAL_RETURN` resumes the same selected owner procedure after the user returns evidence from a prior `RUN_EXTERNAL_HANDOFF`. Returned content is adapter evidence until verified. It is not accepted state.

## Storage boundary

Storage execution is never embedded inside another owner procedure. A selected owner procedure may emit a `storage_update_package` only as candidate next-surface output.

## FINISH boundary

FINISH_REQUEST may be emitted only after required external handoffs have returned, been verified, or been explicitly abandoned as blocked/stopped.

After FINISH, the chat is closed for material work. A new material START in the same chat is forbidden.

END_OF_FILE: workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
