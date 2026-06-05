# FINISH_PACKET Template

status: template

## FINISH_PACKET

`lifecycle_state`:

`finished_work`:

`finish_self_audit`:

```text
selected_one_owner_procedure_in_START:
executed_only_selected_owner_procedure_in_RUN:
no_procedure_switch:
no_unadmitted_state_mutation:
no_hidden_acceptance:
no_pending_required_external_return:
utility_outputs_were_not_procedure_switches:
required_outputs_present:
source_limitations_stated:
next_move_single:
no_hidden_next_launch:
```

`result_packet`:

`next_move_packet`:

## Boundary

FINISH_PACKET closes the selected chat owner procedure after explicit FINISH. It is not acceptance, persistence, launch authority, or permission to switch procedures.

FINISH_PACKET must not be emitted while a required external return is pending.

END_OF_FILE: workflow_v3/templates/FINISH_PACKET_TEMPLATE.md
