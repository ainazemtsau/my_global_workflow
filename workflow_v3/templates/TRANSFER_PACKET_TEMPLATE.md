# Transfer Packet Template

status: template

## Core Transfer Packet

```text
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
```

## Continuation Boundary

When transfer starts a new material chat, include the complete continuation card:

```text
NEXT_CHAT_CARD:
  title:
  why:
  main_procedure_to_start:
  context_to_paste:
  expected_result:
  evidence_or_return_needed:
  start_instruction:
```

## Boundary

A Transfer Packet is complete copy-paste transport for the selected next surface. It remains candidate until explicitly launched or accepted where acceptance is required.

`copy_paste_packet` must be standalone. Do not tell the user to reconstruct a prompt or package from previous chat memory.

END_OF_FILE: workflow_v3/templates/TRANSFER_PACKET_TEMPLATE.md