# Direction Definition Eval

status: active_eval

## Purpose

Validate that Direction Definition coordinates the first semantic step after setup-only root without forming semantic entity content, mutating state, or bypassing lifecycle closure.

## Evidence Required

- Procedure Registry selected `launch_direction_definition`.
- `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` were read from exact resolved paths.
- Setup-only root evidence was checked.
- `semantic_definition_status` was confirmed pending or equivalent.
- Candidate context was classified and kept candidate-only.
- Exactly one next semantic procedure was selected.
- `form_direction_spine` was selected when no accepted Direction Spine exists.
- Transfer Packet uses required core fields: transfer_target, why_transfer_needed, source_context, exact_task, allowed_scope, forbidden_scope, required_sources, required_outputs, return_destination, and copy_paste_packet.
- Result Packet and Next Move Packet preserve acceptance and persistence boundaries.

## PASS Criteria

- Verifies setup-only root before selecting the next semantic step.
- Confirms semantic definition pending or accepted equivalent.
- Selects exactly one next semantic procedure.
- Selects `form_direction_spine` as the first next procedure when no accepted Direction Spine exists.
- Does not run Direction Spine, Direction Map, or Active Front formation inside Direction Definition.
- Produces a complete Transfer Packet using simplified core fields.
- `copy_paste_packet` is complete and standalone.
- Does not persist state.
- Does not accept candidate state.
- Output explicitly says it does not persist state.
- Output explicitly says it does not accept candidate state.
- Blocks product work and Work Graph creation.
- Closes through FINISH_REQUEST before FINISH, then FINISH_PACKET, Result Packet, and Next Move Packet.

## WARN Criteria

- Candidate context is sparse but explicitly labeled as non-blocking.
- Binding or source evidence is limited but the limitation is stated and does not affect first-step selection.
- A bounded check job or child support check is proposed only for source/status consistency.
- Later semantic step selection is status-specific because accepted Spine, Map, or Active Front evidence is present.

## FAIL Criteria

- Direction Definition starts before setup-only root exists.
- `CURRENT_STATUS.md` or `CURRENT_NEXT_MOVE.md` is not read.
- Semantic definition is not pending but the procedure proceeds by assumption.
- More than one next semantic procedure is selected.
- `form_direction_spine` is skipped when no accepted Direction Spine exists.
- Direction Spine, Direction Map, or Active Front content is formed inside Direction Definition.
- Candidate context is treated as accepted state.
- Transfer Packet is missing transfer_target or copy_paste_packet.
- Transfer Packet tells the user to prepare a prompt, use previous approved package, create a card, or reconstruct context manually.
- Procedure persists state, accepts state, imports legacy evidence as accepted state, starts product work, creates Work Graph, or starts another material lifecycle invisibly.

## Required Result Fields

```text
verdict: PASS | WARN | FAIL
setup_only_root_check:
semantic_definition_pending_check:
current_status_read_check:
current_next_move_read_check:
candidate_context_check:
single_next_procedure_check:
first_step_form_direction_spine_check:
no_spine_map_front_execution_check:
transfer_packet_core_shape_check:
copy_paste_packet_check:
no_persistence_check:
no_acceptance_check:
product_work_block_check:
closure_packet_check:
unresolved_questions:
residual_risks:
```

## Recovery Action

Block continuation, repair the Direction Definition result or Transfer Packet, and rerun the eval before any next semantic procedure is launched. If setup status, next move, or binding cannot be verified, return a source/context request instead of inventing accepted state.

END_OF_FILE: workflow_v3/evals/DIRECTION_DEFINITION_EVAL.md
