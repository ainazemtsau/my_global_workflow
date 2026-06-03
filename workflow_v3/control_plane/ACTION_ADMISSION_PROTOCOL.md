# Action Admission Protocol

status: active_control_plane

## Normative rules

- MUST: No action without admission.
- MUST: No admission without registered procedure or explicit bounded user request normalized into one.
- MUST: No material or state-sensitive RUN without START selecting exactly one procedure.
- MUST: No procedure without exact source read.
- MUST: No material work without run_surface_type.
- MUST: No state mutation without storage_update_adapter admission.
- MUST: No procedure switch during RUN.
- MUST: No route change from chat intuition.
- MUST: No hidden launch from Signal, Handler, Closure, or Progression Router.
- MUST: Tool availability is not workflow admission.
- MUST: User input is current human input until accepted through the admitted procedure.
- MUST: Acceptance signal is not storage authorization.
- MUST: STOP beats guessing.

## Single Procedure Gate

Before procedure registry lookup, classify all requested material and state-sensitive work items.

If more than one independent work item is present, return SPLIT_REQUIRED before procedure execution.

A user request cannot admit multiple procedures by wording alone.

A chat may run exactly one selected procedure after START.

RUN cannot switch to another procedure. Procedure switching requires FINISH or STOP, followed by a new START.

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
allowed_operations:
forbidden_operations:
required_inputs:
required_outputs:
write_admission:
acceptance_admission:
stop_conditions:
return_destination:
```

## STOP conditions

Return an exception packet before action when any condition applies:

- missing or unregistered action;
- compound input with more than one independent material or state-sensitive work item;
- missing procedure;
- selected procedure cannot be resolved through Procedure Registry;
- unreadable or truncated source;
- missing EOF where required;
- binding or state conflict;
- missing run_surface_type;
- missing allowed or forbidden operations;
- write requested without storage update package;
- acceptance ambiguity;
- role boundary crossing;
- RUN attempts to execute a procedure not selected in START;
- FINISH attempted without explicit FINISH or ФИНИШ token;
- legacy boundary ambiguity;
- validation required but absent.

## Material and state-sensitive work

Material or state-sensitive work MUST show START_PACKET before RUN. Existing Admission Packet fields remain valid for non-conflicting admission detail, but START_PACKET controls material lifecycle admission.

END_OF_FILE: workflow_v3/control_plane/ACTION_ADMISSION_PROTOCOL.md
