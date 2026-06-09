# Typed Gate Output Template

status: template

## Typed Gate Output

`gate_output_id`:

`procedure_path`:

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

## Quality Checks

- Gate output is generated from a boundary crossing, evidence gap, risk, or required decision.
- Required evidence or decision, visible outcome, blocked action, and residual risk or defer trigger are explicit when applicable.
- Gate type is one of strategy, discovery, delivery_flow, verification, interface_dependency, risk_gate, or memory_learning.
- Gate output remains an internal check and must not become separate route authority.

END_OF_FILE: workflow_v3/templates/TYPED_GATE_OUTPUT_TEMPLATE.md
