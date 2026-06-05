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

Next Move Packet selects exactly one primary next move at closure. It must not launch work invisibly and must include a complete Transfer Packet when another surface is needed.

Next Move Packet is closure routing, not mid-RUN handoff. Mid-RUN external work uses `RUN_EXTERNAL_HANDOFF` and later `RUN_EXTERNAL_RETURN` under the same selected owner procedure.

For `codex`, `codex_verification`, `child_chat`, `check_job`, `storage_update`, or `next_material_chat`, `transfer_packet_if_needed` must include a complete Transfer Packet with `copy_paste_packet`.

Invalid examples:

```text
transfer_packet_if_needed: "Needed if using Codex"
transfer_packet_if_needed: "Use approved package from this chat"
```

`human_decision` must not be used to avoid a required packet when the external surface is materially known and the selected procedure is responsible for producing that packet.

END_OF_FILE: workflow_v3/templates/NEXT_MOVE_PACKET_TEMPLATE.md
