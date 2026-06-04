# Transition Packet Template

status: template

## Transition Packet

`transition_packet_id`:

`transition_packet_type`:

`source_authority`:

`runtime_root`:

`selected_next_step_target`:

`entrypoint`:

`run_surface_type`:

`procedure_ref`:

`required_source_reads`:

`allowed_operations`:

`forbidden_operations`:

`closure_fact`:

`same_chat_allowed`:

`external_run_needed`:

`external_run_type`:

`returns_to_current_chat`:

`next_material_chat_needed`:

`context_supplied`:

`in_scope`:

`out_of_scope`:

`expected_result`:

`validation_or_evidence_required`:

`finish_packet_required`:

`return_destination`:

`parent_chat_id_or_return_destination`:

`child_or_next_chat_boundary`:

`required_return_fields`:

`copy_paste_packet`:

`limitations`:

## transition_packet_type enum

- `human_decision_request`;
- `codex_handoff`;
- `codex_result_verification_request`;
- `check_job_launch`;
- `child_chat_launch`;
- `next_material_chat_launch`;
- `stop`;
- `blocked_result`.

## Boundary

Codex handoff returns to the same current chat for verification and closure.

Next material chat starts only after the current material target is accepted, persisted, verified, or explicitly stopped.

Do not make the user build Codex, check, child-chat, or next-chat prompts manually.

Transfer packets must include entrypoint, run surface, procedure ref, required source reads, allowed/forbidden operations, return destination, and copy-paste packet.

END_OF_FILE: workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md
