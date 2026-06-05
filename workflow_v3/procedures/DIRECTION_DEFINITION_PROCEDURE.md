# Procedure: Direction Definition

title: Direction Definition
status: active_procedure
canonical_location: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
entrypoint: launch_direction_definition
run_surface_type: formation_chat
procedure_class: core_material
embedded_use_policy: may_use_global_utility_layer

## Purpose

Direction Definition coordinates the semantic definition sequence after a setup-only root exists.

It verifies setup-only root state, classifies candidate context, and selects or prepares exactly one next semantic procedure step at a time.

The first selected semantic next step is normally `form_direction_spine`.

This procedure is a coordinator and launcher. It does not form Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, product roadmap, or product execution content.

## Trigger / When to Use

Use this procedure when all apply:

- START selected `launch_direction_definition`;
- setup-only root exists for the requested `direction_id`;
- `CURRENT_NEXT_MOVE.md` or an admitted launch packet says `launch_direction_definition`;
- `semantic_definition_status` is `pending_definition` or an accepted equivalent;
- the user is moving from setup-only technical root into semantic Direction Definition.

## When Not to Use

Do not use this procedure to:

- form Direction Spine content directly;
- form Direction Map content directly;
- select Active Front directly;
- create Work Graph or Work Contract;
- execute product work;
- persist state;
- accept candidate state;
- import legacy evidence as accepted state;
- run multiple formation procedures in one RUN;
- continue by chat intuition after selecting the next procedure.

## Required Inputs

- `direction_id`;
- `runtime_root` or exact runtime root path;
- `current_status_path`;
- `current_next_move_path`;
- setup-only root status evidence;
- selected launch boundary or user request normalized to `launch_direction_definition`;
- `candidate_context_for_direction_definition` if present;
- return destination;
- source authority and repository ref.

## Source Requirements

Before material output, read exact repository/runtime sources needed for admission and next-step packet preparation:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`;
- `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md`;
- matching `formation_chat` run surface contract in `workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md`;
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` if transfer, child/check, or utility boundaries are needed;
- `CURRENT_STATUS.md` from `current_status_path`;
- `CURRENT_NEXT_MOVE.md` from `current_next_move_path`;
- Direction Project Binding if available or required by Project context;
- `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` before preparing transfer to `form_direction_spine`;
- packet templates only as needed for Result Packet, Next Move Packet, or Transfer Packet shape.

Missing, truncated, stale, unreadable, or authority-conflicting sources must return a blocked result. If a file has an `END_OF_FILE` marker, verify it before relying on the read.

## Context Classification

Classify sources and inputs before selecting the next semantic step:

- exact repo files at resolved ref are canonical repository source;
- `CURRENT_STATUS.md`, `CURRENT_NEXT_MOVE.md`, and binding records are accepted records only when they show accepted setup/update authority;
- user-supplied goals, outcomes, product ideas, or constraints are current human input and may become `candidate_context_for_direction_definition`;
- old `directions/**` files are `legacy_evidence` only and are not loaded unless separately admitted;
- Project Files/Sources, pasted excerpts, uploads, previous chat memory, and summaries are cache/context unless verified against exact repository state;
- Transfer Packets, Result Packets, and prior chat packets are candidate context unless an accepted update path proves otherwise.

Do not promote candidate context into accepted Direction state inside this procedure.

## Complexity Selector

- `simple`: setup-only status is clean and the only required output is a next-step packet to `form_direction_spine`.
- `standard`: setup-only root and binding require verification, and candidate context must be classified.
- `checkpointed`: status, binding, or next move is ambiguous; legacy pressure appears; or multiple semantic entities are requested.
- `delegated_or_tool_mediated`: a bounded `check_job_packet` or child support check is required for source, binding, or status consistency.
- `research_backed`: not used by default.

Use the smallest complexity that satisfies the output contract.

## Stage Cards

```text
stage_id: source_lock_and_fit
purpose: Confirm the request belongs to launch_direction_definition, not setup bootstrap, product work, or direct semantic formation.
activation conditions: Always active at RUN start.
inputs: START packet, Procedure Registry entry, this procedure source, run surface contract, source authority/ref, user request or launch packet.
required intermediate output: source lock, selected entrypoint fit, run_surface_type fit, source read limitations.
gate: PASS if request resolves to launch_direction_definition and exact required sources can be read. STOP on missing source, wrong entrypoint, product execution, direct formation request, or source authority conflict.
checkpoint rule: Checkpoint only when source authority or entrypoint fit is ambiguous.
expansion rule: EXPAND only to a bounded source/binding check when exact source consistency cannot be resolved directly.
stop behavior: Return SOURCE_INTEGRITY_STOP, UNREGISTERED_ACTION_EXCEPTION, or BOUNDARY_CROSSING_STOP with exact missing/conflicting source.
```

```text
stage_id: setup_only_root_verification
purpose: Verify setup-only root exists and semantic definition is pending.
activation conditions: source_lock_and_fit passed.
inputs: CURRENT_STATUS.md, CURRENT_NEXT_MOVE.md, runtime_root, direction_id, binding if available.
required intermediate output: setup_status_verified, semantic_definition_status, current_next_move_check, binding_check.
gate: PASS if CURRENT_STATUS shows setup_only_root_created or accepted equivalent, semantic_definition_status is pending_definition or accepted equivalent, and CURRENT_NEXT_MOVE is launch_direction_definition. STOP if no setup-only root, status is missing, semantic definition is already accepted, CURRENT_NEXT_MOVE conflicts, or binding conflicts.
checkpoint rule: Checkpoint when status or binding is ambiguous but may be repairable.
expansion rule: EXPAND only to a bounded check_job_packet for exact status/binding/source consistency.
stop behavior: Return BINDING_CONFLICT, CONTEXT_REQUEST, or SOURCE_INTEGRITY_STOP.
```

```text
stage_id: context_intake_classification
purpose: Classify candidate context for Direction Definition.
activation conditions: setup_only_root_verification passed.
inputs: user input, candidate_context_for_direction_definition, launch packet context, verified repo/runtime sources.
required intermediate output: candidate_context_summary, rejected accepted-state claims, source/read limitations.
gate: PASS if context classification is explicit. PASS_WITH_RISK if candidate context is sparse but non-blocking. STOP if user demands product execution, direct acceptance, or state mutation.
checkpoint rule: Checkpoint when candidate context contains apparent accepted-state claims without accepted evidence.
expansion rule: No product research. A bounded child support check may classify source/evidence consistency only.
stop behavior: Return ACCEPTANCE_AMBIGUITY, LEGACY_BOUNDARY_STOP, or WRITE_NOT_ADMITTED.
```

```text
stage_id: next_semantic_step_selection
purpose: Select exactly one next semantic procedure.
activation conditions: context_intake_classification passed or passed with risk.
inputs: setup verification, semantic_definition_status, accepted Direction Spine/Map/Active Front evidence if any, candidate context summary.
required intermediate output: selected_next_entrypoint, selected_next_procedure_ref, selected_next_run_surface_type, selection_reason.
gate: PASS if exactly one next procedure is selected. REWORK if multiple independent next steps appear. STOP if selection would require invented accepted state.
checkpoint rule: Checkpoint when accepted prerequisite evidence is unclear.
expansion rule: EXPAND only to a bounded check job for accepted-prerequisite evidence consistency.
stop behavior: Return SPLIT_REQUIRED, SOURCE_AUTHORITY_CONFLICT, or VALIDATION_REQUIRED_STOP.
```

Selection rules:

- If no accepted Direction Spine exists, select `form_direction_spine`.
- If accepted Direction Spine exists but accepted Direction Map is missing, the next step may be `form_direction_map`.
- If accepted Direction Spine and Direction Map exist but accepted Active Front is missing, the next step may be `form_active_front`.
- Otherwise produce a blocked or status-specific next move instead of inventing accepted state.

```text
stage_id: transfer_packet_preparation
purpose: Prepare complete Transfer Packet and Next Move Packet for the selected next procedure.
activation conditions: next_semantic_step_selection selected one next procedure.
inputs: selected next procedure source, Transfer Packet template shape, Next Move Packet template shape, source context, return destination.
required intermediate output: transfer_packet_if_needed and next_move_packet.
gate: PASS if packet is complete and the user does not need to assemble a prompt manually. REWORK if packet is placeholder, vague, or missing core fields. STOP if required packet source is missing.
checkpoint rule: Checkpoint when the packet cannot be completed from verified context.
expansion rule: No expansion into semantic content formation. Only source/packet consistency checks are allowed.
stop behavior: Return CONTEXT_REQUEST or VALIDATION_REQUIRED_STOP.
```

Required Transfer Packet core fields:

```text
transfer_target:
why_transfer_needed:
source_context:
exact_task:
allowed_scope:
forbidden_scope:
required_sources:
required_outputs:
return_destination:
copy_paste_packet:
```

For the first Direction Definition run, `transfer_target` should be `form_direction_spine`.

```text
stage_id: closure
purpose: Return Direction Definition next-step packet or blocked result.
activation conditions: transfer_packet_preparation passed, reworked to pass, or stopped with blocked result.
inputs: stage outputs, unresolved items, transfer packet, next move packet, result packet fields.
required intermediate output: direction_definition_result, FINISH_REQUEST readiness.
gate: PASS if closure has exact next move, explicit boundaries, and no pending required external return.
checkpoint rule: None by default after packet completion.
expansion rule: No expansion after closure.
stop behavior: Return blocked Result Packet and Next Move Packet with exact blocking reason.
```

## Gate Outcomes

Allowed gate outcomes:

- `PASS`;
- `PASS_WITH_RISK`;
- `REWORK`;
- `EXPAND`;
- `STOP`;
- `TRANSFER`;
- `RUN_EXTERNAL_HANDOFF`;
- `RUN_EXTERNAL_RETURN`.

This procedure should normally return `PASS` or `TRANSFER` with a complete next-step Transfer Packet. `RUN_EXTERNAL_HANDOFF` is allowed only for a bounded source/binding/status consistency utility needed before closure; it must resume the same selected `launch_direction_definition` RUN.

## Optional Expansion

Allowed expansion:

- exact source inspection;
- bounded `check_job_packet` for source, binding, status, or next-move consistency only;
- bounded child support check only if needed for source/evidence consistency.

Not allowed expansion:

- research for product direction content;
- direct Direction Spine, Direction Map, or Active Front content formation;
- Work Graph or Work Contract creation;
- repository/runtime state mutation;
- acceptance or persistence routing unless a later accepted update path is explicit and separately admitted.

## Research Policy

External research is forbidden by default.

Direction Definition does not need external research to select `form_direction_spine`.

Research may be proposed only later inside the selected semantic formation procedure when that procedure's authored body requires it and the Utility Use Gate passes.

## Utility / Adapter Policy

common_utility_choices:
- `check_job_packet` for exact status, binding, source, or next-move consistency;
- `child_chat_packet` only for bounded support checks, not semantic formation;
- `project_refresh_instruction_packet` for reporting only.

forbidden_utility_categories:
- `codex_handoff_packet` for product work;
- `storage_update_package` unless a later accepted update path is explicit and separately admitted;
- any utility that forms Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, product roadmap, or product execution content inside this RUN.

external_handoff_policy:
- use `RUN_EXTERNAL_HANDOFF` only when an allowed utility result is required before Direction Definition can close;
- the handoff must include a complete `copy_paste_packet`, expected return packet, validation required on return, and same-owner resume rule.

external_return_policy:
- `RUN_EXTERNAL_RETURN` must match the emitted handoff and resume `launch_direction_definition`, not a new owner procedure.

embedded_verification_policy:
- returned utility evidence is candidate evidence only and must be verified before reliance.

storage_boundary:
- this procedure must not mutate repository/runtime state directly;
- accepted state changes require a separate accepted update path.

## Checkpoint Policy

No checkpoint is required for a clean simple run that verifies setup-only root and prepares the `form_direction_spine` packet.

Checkpoint when:

- source authority, binding, or current next move is ambiguous;
- candidate context appears to claim accepted Direction state;
- multiple semantic entities or next steps are requested;
- a bounded check job or child support check changes the evidence available to this RUN;
- the Transfer Packet cannot be completed without user-visible repair.

Checkpoints are internal RUN gates and must return typed outcomes. They are not separate lifecycle phases and do not switch procedures.

## Output Contract

Return this shape:

```text
direction_definition_result:
  status:
  direction_id:
  setup_status_verified:
  semantic_definition_status:
  selected_next_entrypoint:
  selected_next_procedure_ref:
  selected_next_run_surface_type:
  candidate_context_summary:
  source_read_limitations:
  transfer_packet_if_needed:
  result_packet:
  next_move_packet:
```

`selected_next_entrypoint` should normally be `form_direction_spine` when no accepted Direction Spine exists.

When transfer is needed, `transfer_packet_if_needed` must include a complete Transfer Packet. For the normal first semantic step:

```text
transfer_target: form_direction_spine
why_transfer_needed: Direction Definition coordinates the sequence and must hand off the first semantic content formation to the registered Direction Spine Formation procedure.
source_context: direction_id, runtime_root, setup_status_verified, semantic_definition_status, candidate_context_summary, source refs, read limitations.
exact_task: Run the registered form_direction_spine procedure to form candidate Direction Spine content only.
allowed_scope: Direction Spine candidate formation, source/context classification, evidence limitations, acceptance question, FINISH_REQUEST, FINISH_PACKET, Result Packet, Next Move Packet.
forbidden_scope: Direction Map formation, Active Front selection, Work Graph, Work Contract, product execution, state mutation, acceptance, persistence, legacy import as accepted state.
required_sources: Procedure Registry, Direction Spine Formation procedure, relevant run surface contract, CURRENT_STATUS.md, CURRENT_NEXT_MOVE.md, candidate context, packet templates as needed.
required_outputs: candidate Direction Spine package or blocked result, evidence/source limitations, acceptance question, Result Packet, Next Move Packet.
return_destination: parent Direction Definition return destination or the specified Direction Project chat.
copy_paste_packet: complete standalone launch packet for form_direction_spine, including role, source authority, required reads, boundaries, expected result, FINISH closure requirement, and return fields.
```

## Eval / Quality Checks

- START selected exactly one owner procedure: `launch_direction_definition`.
- This procedure source, Procedure Registry, matching run surface contract, and required runtime records were read or limitations were stated.
- Setup-only root was verified before semantic next-step selection.
- `semantic_definition_status` was pending or equivalent before selecting first semantic step.
- Candidate context remained candidate-only.
- Exactly one next semantic procedure was selected.
- First next procedure is `form_direction_spine` when no accepted Direction Spine exists.
- Direction Spine, Direction Map, and Active Front content were not formed inside this procedure.
- No Work Graph, Work Contract, product work, persistence, or acceptance occurred.
- Transfer Packet uses required core fields and complete `copy_paste_packet`.
- FINISH_REQUEST is emitted before FINISH when lifecycle closure applies.
- FINISH emits FINISH_PACKET, Result Packet, and Next Move Packet with exactly one primary next move.

## Stop Conditions

Stop when any applies:

- setup-only root is missing;
- `CURRENT_STATUS.md` is missing, truncated, unreadable, stale, or lacks required authority;
- `CURRENT_NEXT_MOVE.md` is missing, truncated, unreadable, stale, or conflicts with `launch_direction_definition`;
- Direction Project Binding conflict;
- semantic definition is already accepted and no status-specific next move can be safely selected;
- user asks for product execution;
- user asks to form multiple semantic entities in the same RUN;
- user asks to persist or accept state;
- legacy import pressure appears;
- required source authority is missing or conflicting;
- a complete Transfer Packet cannot be produced;
- the procedure would invent accepted state.

## Procedure Closure

This procedure produces candidate next-step packet output only.

It does not form semantic entity content, mutate state, accept state, persist state, or launch the selected next procedure invisibly.

RUN closes with FINISH_REQUEST before FINISH when complete or blocked.

After explicit FINISH, emit FINISH_PACKET, Result Packet, and Next Move Packet. The Next Move Packet must select exactly one primary next move and include a complete Transfer Packet when another surface or material lifecycle is needed.

After FINISH, the same chat must not begin a new material START.

END_OF_FILE: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
