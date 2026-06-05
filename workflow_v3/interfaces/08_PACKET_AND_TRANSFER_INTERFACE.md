# Packet and Transfer Interface

status: interface_summary

## Purpose

This interface summarizes user-visible packets. Runtime authority remains in the control-plane protocols and selected procedure files.

## Packet Summary

| Packet | Purpose | Required signal |
| --- | --- | --- |
| `START_CONTRACT` | Shows selected main procedure, completion contract, stages, and boundaries before RUN. | Waits for START / СТАРТ. |
| `STAGE_RESULT` | Reports one completed material stage. | Waits for CONTINUE / ДАЛЬШЕ before next material stage unless next step is `internal_check`. |
| `UTILITY_CALL` | Sends bounded supporting work to a utility surface. | Must name why, target, packet/call boundary, expected return, verification, and same-procedure resume. |
| `UTILITY_RETURN` | Brings utility evidence back. | Must match the call and verify evidence before reliance. |
| `CLOSURE_CHECK` | Compares actual result to selected procedure completion. | Pass, repair, or blocked decision. |
| `FINISH_PACKET` | Final audit and closure. | Includes result and continuation. |
| `NEXT_CHAT_CARD` | Copy-paste continuation for a new material chat. | Complete enough that the user does not assemble the next prompt manually. |

## NEXT_CHAT_CARD Shape

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

## Transfer Boundary

Transfer packets and next-chat cards are candidates until explicitly launched. They do not accept state or start work invisibly.

END_OF_FILE: workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md