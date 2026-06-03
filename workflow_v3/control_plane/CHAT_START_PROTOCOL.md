# Chat Start Protocol

status: active_control_plane

## Purpose

START selects one procedure for the current chat and blocks execution until explicit user start confirmation.

## START_PACKET

A material or state-sensitive chat must show exactly these fields before RUN:

```text
START_PACKET:
  lifecycle_state:
  requested_work_items:
  selected_work:
  procedure:
  source_lock:
  surface_contract:
  execution_boundaries:
  run_plan:
  next_transition:
```

## Field rules

lifecycle_state:
Must be START.

requested_work_items:
List every independent material or state-sensitive work item detected in the user input.

selected_work:
Exactly one work item, or none when START returns STOP.

procedure:
Must include selected_entrypoint, selected_procedure_ref, and run_surface_type.

source_lock:
Must list exact files read for lifecycle, registry, surface contract, selected procedure, and required state sources. Each listed markdown file must include EOF status.

surface_contract:
Must list allowed_operations, forbidden_operations, required_inputs, required_outputs, and stop_conditions from the selected run_surface_type.

execution_boundaries:
Must state write_admission, acceptance_admission, procedure_switch_policy, and return_destination.

run_plan:
Must list only actions allowed by selected_procedure_ref and run_surface_type.

next_transition:
Must be WAITING_FOR_USER_START when START passes.
Must be STOP when START fails.

## START confirmation

RUN may begin only after the user sends a standalone message equal to START or СТАРТ.

## START failure

If START fails, emit STOP_PACKET instead of START_PACKET.

## STOP_PACKET

```text
STOP_PACKET:
  lifecycle_state:
  stop_type:
  blocked_transition:
  reason:
  required_user_action:
```

END_OF_FILE: workflow_v3/control_plane/CHAT_START_PROTOCOL.md
