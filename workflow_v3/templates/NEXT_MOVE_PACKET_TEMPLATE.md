# Next Move Packet Template

status: template

## Purpose

Next Move Packet is a closure summary of the exact next move. When the next move requires a new material chat, the primary user-facing continuation is `NEXT_CHAT_CARD`.

## Next Move Packet

```text
primary_next_move:
why:
continuation_needed: yes | no
transfer_packet_if_needed:
NEXT_CHAT_CARD_if_needed:
no_next_chat_needed_if_applicable:
blocking_reason_if_any:
```

## NEXT_CHAT_CARD

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

Next Move Packet must select one primary next move and must not launch work invisibly. If another surface or chat is needed, include a complete Transfer Packet or `NEXT_CHAT_CARD` with copy-paste-ready content.

## Quality Checks

- Closure derives continuation from the selected main procedure, actual result, CLOSURE_CHECK outcome, resolved dependency status, and next intended workflow step.
- If continuation is needed, NEXT_CHAT_CARD has title, why, main procedure to start, complete context to paste, expected result, evidence or return needed, and start instruction.
- If continuation is not needed, closure states `no_next_chat_needed` with reason.
- The packet is not a placeholder, hardcoded global next-step enum, terminal completion substitute, or carrier for unfinished dependency work.

END_OF_FILE: workflow_v3/templates/NEXT_MOVE_PACKET_TEMPLATE.md
