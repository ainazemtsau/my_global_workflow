# FINISH_PACKET Template

status: template

## FINISH_PACKET

```text
FINISH_PACKET:
  selected_entrypoint:
  selected_procedure_path:
  completion_contract:
  closure_check:
  finish_audit:
  result:
  evidence:
  validation:
  project_refresh_requirements:
  residual_risks:
  continuation:
```

`continuation` must contain either `NEXT_CHAT_CARD` or `no_next_chat_needed` with reason.

## Required Audit Fields

```text
finish_audit:
  start_selected_exactly_one_main_procedure:
  selected_completion_contract_was_shown:
  run_executed_only_selected_main_procedure:
  material_stages_emitted_stage_result:
  utility_returns_verified_before_reliance:
  closure_check_passed:
  no_hidden_launch_or_acceptance:
```

## Boundary

FINISH_PACKET closes the selected chat procedure after explicit FINISH and passed audit. It is not acceptance, persistence, launch authority, or permission to switch procedures.

END_OF_FILE: workflow_v3/templates/FINISH_PACKET_TEMPLATE.md