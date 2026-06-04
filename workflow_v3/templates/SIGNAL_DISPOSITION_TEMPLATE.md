# Typed Gate Output Template

status: template

## Typed Gate Output

`gate_output_id`:

`procedure_ref`:

`stage_id`:

`gate_outcome`:

Allowed values:

- `PASS`
- `PASS_WITH_RISK`
- `REWORK`
- `EXPAND`
- `STOP`
- `TRANSFER`

`observed_fact`:

`required_action_if_any`:

`result_packet_ref_if_any`:

`next_move_packet_ref_if_any`:

`transfer_packet_ref_if_any`:

`limitations`:

## Boundary

Typed Gate Output is an internal procedure output. It does not mutate accepted state, switch procedures, or launch work by itself.

END_OF_FILE: workflow_v3/templates/SIGNAL_DISPOSITION_TEMPLATE.md
