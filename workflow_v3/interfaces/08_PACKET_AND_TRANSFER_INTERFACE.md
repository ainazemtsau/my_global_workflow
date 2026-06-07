# Packet and Transfer Interface

status: interface_summary

## Purpose

This interface summarizes user-visible packets. Runtime authority remains in the control-plane protocols and selected procedure files.

## Packet Summary

| Packet | Purpose | Required signal |
| --- | --- | --- |
| `START_CONTRACT` | Shows selected main procedure, completion contract, stages, and boundaries before RUN. | Waits for START / СТАРТ. |
| `STAGE_RESULT` | Reports one completed material stage. | Waits for CONTINUE / ДАЛЬШЕ before next material stage unless next step is `internal_check`. |
| `CHILD_PROCEDURE_CALL` | Sends bounded supporting work to a child/adaptor surface. | Must name why, target, packet/call boundary, expected return, verification, same-procedure resume, and unresolved-until-returned status. |
| `CHILD_PROCEDURE_RETURN` | Brings child/adaptor evidence back. | Must match the call, resume the same selected main procedure, and pass verification before reliance. |
| `CLOSURE_CHECK` | Compares actual result to selected procedure completion. | Pass, repair, or blocked decision. |
| `FINISH_PACKET` | Final audit and closure. | Includes result and continuation. |
| `NEXT_CHAT_CARD` | Post-closed copy-paste continuation for a new material chat. | Complete enough that the user does not assemble the next prompt manually; cannot carry unfinished current-goal child work. |

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

Transfer packets may be post-closed continuation content or the body of a visible `CHILD_PROCEDURE_CALL`, depending on lifecycle position. They do not accept state, start work invisibly, or substitute for a required current-goal `CHILD_PROCEDURE_CALL`. `NEXT_CHAT_CARD` is post-closed continuation only and must not carry unfinished child work.

END_OF_FILE: workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md
