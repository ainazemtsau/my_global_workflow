# Transfer Packet Template

status: template

## Transfer Packet

`transfer_packet_type`:

Allowed values:

- `human_decision_request`
- `codex_handoff`
- `codex_result_verification_request`
- `check_job_launch`
- `child_chat_launch`
- `next_material_chat_launch`
- `storage_update_request`
- `stop`
- `blocked_result`

`selected_target`:

`same_chat_allowed`:

`external_run_needed`:

`external_run_type`:

`returns_to_current_chat`:

`next_material_chat_needed`:

`return_destination`:

`copy_paste_packet`:

## Boundary

Transfer Packet is complete copy-paste transport for the selected next move. It remains candidate until explicitly launched or accepted where acceptance is required.

END_OF_FILE: workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md
