# Packet and Transfer Interface

status: interface_summary

## Purpose

This interface summarizes user-visible packets. Runtime authority remains in the control-plane protocols and selected procedure files.

## Packet Summary

| Packet | Purpose | Required signal |
| --- | --- | --- |
| `START_CONTRACT` | Shows selected main procedure, completion contract, stages, and boundaries before RUN. | Waits for START / СТАРТ. |
| `STAGE_RESULT` | Reports one completed material stage. | Waits for CONTINUE / ДАЛЬШЕ before next material stage unless next step is `internal_check`. |
| `DEPENDENCY_CALL` | Sends bounded supporting work to a typed dependency surface. | Must name why, dependency type, execution surface, packet/call boundary, expected return, verification, same-procedure resume, and unresolved-until-returned status. |
| `DEPENDENCY_RETURN` | Brings dependency evidence back. | Must match the call, resume the same selected main procedure, and pass verification before reliance. |
| `CLOSURE_CHECK` | Compares actual result to selected procedure completion. | Pass, repair, or blocked decision. |
| `FINISH_PACKET` | Final audit and closure. | Includes result and continuation. |
| `NEXT_CHAT_CARD` | Post-closed copy-paste continuation for a new material chat. | Complete enough that the user does not assemble the next prompt manually; cannot carry unfinished current-goal dependency work. |

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

Transfer packets may be post-closed continuation content or the body of a visible `DEPENDENCY_CALL`, depending on lifecycle position. They do not accept state, start work invisibly, or substitute for a required current-goal dependency. `NEXT_CHAT_CARD` is post-closed continuation only and must not carry unfinished dependency work.

Dependency type selection is controlled by `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`. In particular, code/repository mutation uses `code_repository_dependency` and runs only on Codex/code assistant.

END_OF_FILE: workflow_v3/interfaces/08_PACKET_AND_TRANSFER_INTERFACE.md
