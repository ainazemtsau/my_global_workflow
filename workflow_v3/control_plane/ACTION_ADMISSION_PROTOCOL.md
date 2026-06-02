# Action Admission Protocol

status: active_control_plane

## Normative rules

- MUST: No action without admission.
- MUST: No admission without registered procedure or explicit bounded user request normalized into one.
- MUST: No procedure without exact source read.
- MUST: No material work without run_surface_type.
- MUST: No state mutation without storage_update_adapter admission.
- MUST: No route change from chat intuition.
- MUST: No hidden launch from Signal, Handler, Closure, or Progression Router.
- MUST: Tool availability is not workflow admission.
- MUST: User input is current human input until accepted through the admitted procedure.
- MUST: Acceptance signal is not storage authorization.
- MUST: STOP beats guessing.

## Before-action sequence

```text
Intake
-> procedure registry lookup
-> source integrity check
-> run surface contract
-> Admission Packet
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
- missing procedure;
- unreadable or truncated source;
- missing EOF where required;
- binding or state conflict;
- missing run_surface_type;
- missing allowed or forbidden operations;
- write requested without storage update package;
- acceptance ambiguity;
- role boundary crossing;
- legacy boundary ambiguity;
- validation required but absent.

## Material and state-sensitive work

Material or state-sensitive work MUST show an Admission Packet and Work Plan before execution unless the admitted procedure explicitly allows immediate non-mutating answer behavior.

END_OF_FILE: workflow_v3/control_plane/ACTION_ADMISSION_PROTOCOL.md
