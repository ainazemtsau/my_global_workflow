# Action Admission Protocol

status: active_control_plane

## Normative rules

- MUST: No action without admission.
- MUST: No admission without registered procedure or explicit bounded user request normalized into one.
- MUST: No material or state-sensitive RUN without START selecting exactly one owner procedure.
- MUST: No procedure without exact source read.
- MUST: No material work without run_surface_type.
- MUST: No utility invocation unless the selected owner, registered utility, source/policy/safety/write boundaries, and Utility Adapter Protocol pass the Utility Use Gate.
- MUST: No direct in-chat state mutation without storage_update_adapter admission.
- MUST: No external utility write without Utility Use Gate, write gate, exact allowed paths, validation, and return verification.
- MUST: No procedure switch during RUN.
- MUST: No FINISH_REQUEST while a required external return is unresolved.
- MUST: No route change from chat intuition.
- MUST: No hidden launch from FINISH output, Result Packet, Next Move Packet, or Transfer Packet.
- MUST: Tool availability is not workflow admission.
- MUST: User input is current human input until accepted through the admitted procedure.
- MUST: Human acceptance input is not storage authorization.
- MUST: STOP beats guessing.

## Single Procedure Gate

Before procedure registry lookup, classify all requested material and state-sensitive work items.

If more than one independent work item is present, return SPLIT_REQUIRED before procedure execution.

A user request cannot admit multiple procedures by wording alone.

A chat may run exactly one selected owner procedure after START.

RUN cannot switch to another owner procedure. RUN_EXTERNAL_HANDOFF and RUN_EXTERNAL_RETURN are same-owner internal RUN gates, not procedure switches.

A different material owner procedure requires a fresh material lifecycle after STOP or in a new material chat. After FINISH, the same chat is closed for material work and must not open a new material START.

## Before-action sequence

```text
Intake
-> Single Procedure Gate
-> procedure registry lookup
-> source integrity check
-> run surface contract
-> START_PACKET or Admission Packet
-> Work Plan
-> execution or blocked exception
```

## Admission Packet minimum

```text
requested_action:
normalized_entrypoint:
procedure_ref:
source_lock:
run_surface_type:
procedure_class:
embedded_use_policy:
allowed_operations:
forbidden_operations:
utility_decision_gate:
utility_policy:
required_inputs:
required_outputs:
write_admission:
acceptance_admission:
external_handoff_status:
stop_conditions:
return_destination:
```

## STOP conditions

Return an exception packet before action when any condition applies:

- missing or unregistered action;
- compound input with more than one independent material or state-sensitive work item;
- missing procedure;
- selected procedure cannot be resolved through Procedure Registry;
- procedure_class or embedded_use_policy cannot be resolved where material;
- unreadable or truncated source;
- missing EOF where required;
- binding or state conflict;
- missing run_surface_type;
- missing allowed or forbidden operations;
- utility invocation fails the Utility Use Gate;
- RUN_EXTERNAL_HANDOFF is incomplete or lacks expected return fields;
- required RUN_EXTERNAL_RETURN is unresolved;
- write requested without storage_update_adapter admission or gated external utility write package;
- acceptance ambiguity;
- role boundary crossing;
- RUN attempts to execute a procedure not selected in START;
- RUN attempts to treat an embedded utility adapter as a new selected owner procedure;
- FINISH attempted without explicit FINISH or ФИНИШ token;
- legacy boundary ambiguity;
- validation required but absent.

## Material and state-sensitive work

Material or state-sensitive work MUST show START_PACKET before RUN. Existing Admission Packet fields remain valid for non-conflicting admission detail, but START_PACKET controls material lifecycle admission.

END_OF_FILE: workflow_v3/control_plane/ACTION_ADMISSION_PROTOCOL.md
