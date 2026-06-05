# Chat Finish Protocol

status: active_control_plane

## Purpose

FINISH closes the selected chat procedure after RUN reaches completion or a terminal blocked state.

## Load rule

CHAT_FINISH_PROTOCOL.md is read only when the chat enters FINISH after explicit user token FINISH or ФИНИШ.

## FINISH_REQUEST

RUN must emit exactly these fields when ready for FINISH:

```text
FINISH_REQUEST:
  lifecycle_state:
  selected_work:
  run_result_summary:
  unresolved_items:
  finish_gate:
```

finish_gate:
Must be WAITING_FOR_USER_FINISH.

## FINISH confirmation

FINISH may begin only after the user sends a standalone message equal to FINISH or ФИНИШ.

## FINISH_PACKET

FINISH must emit exactly these fields:

```text
FINISH_PACKET:
  lifecycle_state:
  finished_work:
  finish_self_audit:
  result_packet:
  next_move_packet:
```

## finish_self_audit

finish_self_audit must contain exactly these checks:

```text
finish_self_audit:
  selected_one_procedure_in_START:
  executed_only_selected_procedure_in_RUN:
  no_procedure_switch:
  no_unadmitted_state_mutation:
  no_hidden_acceptance:
  required_outputs_present:
  source_limitations_stated:
  next_move_single:
```

Each check value must be PASS or FAIL.

If any check is FAIL, result_packet.status must be repair_required or blocked.

## result_packet

result_packet must contain exactly these fields:

```text
result_packet:
  status:
  result:
  evidence:
  changed_files:
  validation:
  source_read_limitations:
  not_done:
  project_refresh_requirements:
  residual_risks:
  exact_next_move:
```

## next_move_packet

next_move_packet must contain exactly these fields:

```text
next_move_packet:
  primary_next_move:
  next_move_type:
  return_destination:
  transfer_packet_if_needed:
  persistence_boundary:
  acceptance_boundary:
  blocking_reason_if_any:
```

`next_move_type` allowed values:

- `same_chat_continuation`
- `next_material_chat`
- `child_chat`
- `check_job`
- `codex`
- `codex_verification`
- `human_decision`
- `storage_update`
- `stop`

`transfer_packet_if_needed` is `not needed` only when the next move can be completed in the same chat without an external surface.

If `next_move_type` is `codex`, `codex_verification`, `child_chat`, `check_job`, `storage_update`, or `next_material_chat`, `transfer_packet_if_needed` must include or reference a complete Transfer Packet with a complete `copy_paste_packet`.

`Needed if using X`, `use previous approved package`, `prepare a prompt`, and equivalent placeholders are invalid transfer packets.

END_OF_FILE: workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md
