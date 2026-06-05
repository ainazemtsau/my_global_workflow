# Result Packet Template

status: template

## Result Packet

```text
result_packet_id:
selected_entrypoint:
selected_procedure_path:
completion_contract:
result_summary:
material_output:
evidence_refs:
validation_results:
limitations:
out_of_scope_not_done:
candidate_state_changes:
closure_check:
continuation:
```

`continuation` must include either:

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

or:

```text
no_next_chat_needed:
  reason:
```

## Boundary

Result Packet is candidate until accepted by an explicit acceptance/update path. It does not mutate accepted state, accept evidence, or launch next work by itself.

END_OF_FILE: workflow_v3/templates/RESULT_PACKET_TEMPLATE.md