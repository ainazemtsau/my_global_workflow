# Next Move Packet Template

status: template

## Next Move Packet

`primary_next_move`:

`next_move_type`:

Allowed values:

- `same_chat_continuation`
- `next_material_chat`
- `child_chat`
- `check_job`
- `codex`
- `codex_verification`
- `human_decision`
- `storage_update`
- `stop`

`return_destination`:

`transfer_packet_if_needed`:

`persistence_boundary`:

`acceptance_boundary`:

`blocking_reason_if_any`:

## Boundary

Next Move Packet selects exactly one primary next move for closure or route after the selected procedure completes or stops. It must not launch work invisibly and must include a complete Transfer Packet when another surface is needed.

Mid-RUN external utility handoff uses RUN_EXTERNAL_HANDOFF under `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`, not Next Move Packet.

For `codex`, `codex_verification`, `child_chat`, `check_job`, `storage_update`, or `next_material_chat`, `transfer_packet_if_needed` must include a complete Transfer Packet with all core fields and `copy_paste_packet`.

`human_decision` must not be used merely to avoid preparing a known required transfer packet.

Invalid examples:

```text
transfer_packet_if_needed: "Needed if using Codex"
transfer_packet_if_needed: "Use approved package from this chat"
transfer_packet_if_needed: "Prepare a prompt"
transfer_packet_if_needed: "Create Codex card"
```

END_OF_FILE: workflow_v3/templates/NEXT_MOVE_PACKET_TEMPLATE.md
