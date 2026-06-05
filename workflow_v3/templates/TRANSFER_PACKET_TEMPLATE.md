# Transfer Packet Template

status: template

## Core Transfer Packet

transfer_target:
why_transfer_needed:
source_context:
exact_task:
allowed_scope:
forbidden_scope:
required_sources:
required_outputs:
return_destination:
copy_paste_packet:

## Optional transport metadata

transfer_packet_type:
external_surface:
same_chat_allowed:
external_run_needed:
returns_to_current_chat:
next_material_chat_needed:
selected_target_or_ref:

## Boundary

Core fields are required whenever a Transfer Packet is needed.

Optional transport metadata is used only when it clarifies transport mechanics.

Transfer Packet is complete copy-paste transport for the selected next move. It remains candidate until explicitly launched or accepted where acceptance is required.

`copy_paste_packet` must be complete and standalone.

For Codex, `copy_paste_packet` must include the complete Codex package. It must not be a placeholder.

Do not tell the user to reconstruct a prompt or package from previous chat memory.

END_OF_FILE: workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md
