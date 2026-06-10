# Procedure: Current Next Move Formation

title: Current Next Move Formation
status: active_procedure
canonical_location: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
entrypoint: form_current_next_move
procedure_boundary: formation_chat
kind: core
dependency_schema_policy: dependency_only_policy
routing_dependency_policy: dependency_allowed_when_needed_for_this_owner

## Purpose

Form a candidate Current Next Move / NEXT_CHAT_CARD continuation from a completed or blocked material run closure state.

This procedure selects exactly one primary post-closed next move, preserves acceptance and persistence boundaries, and emits a complete Transfer Packet when the selected next move requires another registered owner lifecycle with a nested dependency or next-surface target.

This procedure does not execute, launch, accept, persist, verify by implication, route current-goal dependencies, or continue into the selected next move. Dependency-vs-continuation separation is governed by `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md`.

## Trigger / When to Use

Use this procedure when START selects `form_current_next_move`.

Use it when a completed or blocked material result needs a closure next move, including:

- a FINISH / closure package needs a valid `continuation`;
- a FINISH_PACKET result needs one exact next action;
- a parent or governance run needs to convert current result state into a bounded next-surface routing packet;
- an Acceptance Decision result needs a post-closed next move to storage update, repair, check, Codex/code assistant, dependency chat, next material chat, human decision, or stop;
- a blocked run needs a clear blocked next move without silently launching repair work.

## When Not to Use

Do not use this procedure to:

- execute the selected next move;
- launch Codex, a dependency chat, a check job, storage update, or a next material chat;
- perform repository or runtime mutation;
- accept candidate output;
- persist accepted state;
- verify code repository dependency returns as a standalone verification run;
- replace `DEPENDENCY_CALL` while the current main procedure RUN still needs external evidence before completion;
- use `human_decision` to avoid producing a materially known required Transfer Packet;
- emit multiple primary next moves;
- continue from one steering entity to another by conversation momentum;
- create accepted state by existence of a NEXT_CHAT_CARD continuation.

## Required Inputs

Required closure inputs:

```text
closure_state:
  lifecycle_state:
  selected_entrypoint:
  selected_procedure_path:
  procedure_boundary:
  kind:
  finished_or_blocked_work:
  dependency_return_status:
  unresolved_items:

closure_result:
  status:
  result:
  evidence:
  changed_files:
  validation:
  source_read_limitations:
  not_done:
  project_refresh_requirements:
  residual_risks:
  exact_next_move:
```

Required boundary inputs:

```text
acceptance_boundary:
  accepted_state_status:
  acceptance_authority:
  accepted_scope:
  not_accepted_scope:
  acceptance_record_if_any:
  acceptance_limitations:

persistence_boundary:
  persistence_authority:
  storage_update_authority:
  allowed_paths_if_known:
  forbidden_paths_if_known:
  storage_package_if_any:
  persistence_limitations:
```

Required routing inputs:

```text
return_destination:
  destination_type:
  destination_ref:
  parent_handoff_id_if_any:
  same_owner_resume_relevance:
  closed_chat_boundary:

candidate_next_move_context:
  known_required_surface:
  known_transfer_artifact:
  repair_need_if_any:
  verification_need_if_any:
  storage_need_if_any:
  parent_or_dependency_relationship_if_any:
```

If the procedure lacks enough information to produce a safe NEXT_CHAT_CARD continuation, it must emit a blocked result or a materially correct `human_decision` next move. It must not invent missing acceptance, persistence, destination, or transfer-package content.

## Continuation Schema

Emit exactly one continuation shape from `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`:

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

Field requirements:

- `NEXT_CHAT_CARD.title` must name one and only one next action.
- `NEXT_CHAT_CARD.main_procedure_to_start` must identify the next registered owner procedure or explicit human decision surface.
- `NEXT_CHAT_CARD.context_to_paste` must carry any required Transfer Packet, persistence boundary, acceptance boundary, and return destination.
- `NEXT_CHAT_CARD.expected_result` must state the result expected from the next lifecycle or external surface.
- `NEXT_CHAT_CARD.evidence_or_return_needed` must state the evidence or return packet needed by the current owner.
- `NEXT_CHAT_CARD.start_instruction` must be a start instruction, not a hidden launch.
- Use `no_next_chat_needed` only when no material continuation is required.

## Transfer Packet Schema

`NEXT_CHAT_CARD.main_procedure_to_start` identifies the registered owner procedure for the new independent lifecycle, or an explicit human decision surface when no registered procedure owns the decision.

It must not name dependency surfaces such as Codex/code assistant, `verify_code_repository_dependency_return`, dependency chat, or check job.

When the selected continuation requires dependency work, `NEXT_CHAT_CARD.context_to_paste` must carry a complete Transfer Packet that describes the nested dependency target.

`target_surface_type` / `transfer_type` inside the Transfer Packet may name:

```text
codex
verify_code_repository_dependency_return
dependency_chat
check_job
storage_update
next_material_chat
```

only as the transfer target under the owner procedure, not as the selected main procedure.

If the current START goal still requires that dependency result before closure, do not use NEXT_CHAT_CARD; emit `DEPENDENCY_CALL` in RUN and wait for `DEPENDENCY_RETURN` verification.

Minimum schema:

```text
transfer_packet:
  transfer_type:
  source_selected_entrypoint:
  source_selected_procedure_path:
  source_procedure_boundary:
  source_lifecycle_state:
  source_result_summary:
  target_surface_type:
  target_entrypoint_or_dependency_surface:
  target_procedure_path_if_known:
  purpose:
  scope:
  non_goals:
  source_authority:
    repository:
    base_ref:
    required_files_or_records:
    cache_policy:
  required_inputs:
  copy_paste_packet:
  expected_return_packet:
  validation_requirements:
  acceptance_boundary:
  persistence_boundary:
  forbidden_actions:
  stop_conditions:
  return_destination:
```

Field descriptions:

- `target_surface_type`: nested dependency or next-surface target under the owner procedure.
- `target_entrypoint_or_dependency_surface`: registered procedure entrypoint when applicable, or dependency surface name inside the owner context.
- `return_destination`: parent/owner return destination.

`copy_paste_packet` must be directly usable. It cannot be a placeholder.

Invalid transfer packet placeholders include, but are not limited to:

- `Needed if using Codex`
- `use previous approved package`
- `prepare a prompt`
- `create a code repository dependency packet`
- `make a storage package later`
- `continue in a new chat`
- `verify this somehow`
- equivalent incomplete handoffs

If a required transfer packet cannot be produced, the procedure must not emit a fake transfer. It must choose one of:

- `stop`, when the blocker is terminal for this closure;
- `human_decision`, when the missing information is genuinely a human choice and no materially known transfer packet can be completed;
- a bounded repair next move with a complete transfer packet, when repair is materially known and can be bounded.

## Specialized Transfer Packet Requirements

### `codex`

Required additions:

```text
codex_transfer_packet:
  repository:
  base_ref:
  target_ref:
  worktree_policy:
  branch_policy:
  pr_policy:
  purpose:
  goal:
  source_files_to_read:
  allowed_paths:
  forbidden_paths:
  required_changes:
  validation:
  stop_conditions:
  commit_push_instructions:
  requested_return_fields:
    base_main_commit_sha_before_work:
    final_main_commit_sha_after_push:
    branch_used:
    pr_created:
    changed_files:
    validation_outputs:
    residual_risks:
```

Codex must not decide acceptance and must not perform ChatGPT FINISH.

This specialized transfer packet is valid only inside NEXT_CHAT_CARD.context_to_paste or inside a `DEPENDENCY_CALL` body under a registered owner procedure.
It is not a value for `NEXT_CHAT_CARD.main_procedure_to_start`.
It does not create an independent Codex, `code_repository_dependency`, or `verify_code_repository_dependency_return` material lifecycle.

If Codex/code assistant is required before the current owner can complete, the current owner must emit `DEPENDENCY_CALL` and wait for return verification before CHECK/FINISH/CLOSED.

### `verify_code_repository_dependency_return`

Required additions:

```text
verify_code_repository_dependency_return_transfer_packet:
  repository:
  expected_base_ref:
  expected_branch_or_ref:
  expected_commit_sha:
  expected_changed_files:
  allowed_paths:
  forbidden_paths:
  required_validation_outputs:
  required_eof_checks:
  required_payload_counts_if_any:
  required_push_status:
  codex_return_packet_to_verify:
  requested_return_fields:
    verification_result:
    failures:
    missing_evidence:
    residual_risks:
    exact_next_move:
```

Verification does not accept the returned dependency evidence by itself.

This specialized transfer packet is valid only inside NEXT_CHAT_CARD.context_to_paste or inside a `DEPENDENCY_CALL` body under a registered owner procedure.
It is not a value for `NEXT_CHAT_CARD.main_procedure_to_start`.
It does not create an independent Codex, `code_repository_dependency`, or `verify_code_repository_dependency_return` material lifecycle.

If Codex verification is required before the current owner can complete, the current owner must emit `DEPENDENCY_CALL` and wait for return verification before CHECK/FINISH/CLOSED.

### `dependency_chat`

Required additions:

```text
dependency_chat_transfer_packet:
  parent_handoff_id:
  dependency_id:
  parent_selected_entrypoint:
  dependency_task_type:
  dependency_scope:
  dependency_non_goals:
  required_sources:
  source_authority:
  expected_dependency_closure_result:
  parent_return_destination:
  stop_conditions:
```

A dependency chat must not decide the parent target unless explicitly scoped as a candidate-only dependency output.

### `check_job`

Required additions:

```text
check_job_transfer_packet:
  check_id:
  bounded_question:
  exact_sources:
  evidence_required:
  validation_method:
  expected_return_packet:
  return_destination:
  stop_conditions:
```

A check job answers a bounded source, evidence, consistency, or validation question. It must not execute material work, mutate state, or accept output.

### `storage_update`

Required additions:

```text
storage_update_transfer_packet:
  target_entrypoint: persist_accepted_state
  target_procedure_boundary: storage_update
  target_procedure_path: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
  admitted_storage_update_package:
    package_version: storage_update_package.v1
    canonical_schema_ref: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
    update_authority:
      authority_type:
      authority_ref:
      authority_statement:
      authority_scope:
    repository_target:
      repository:
      base_ref:
      target_ref:
      expected_head_sha_before_write:
      write_surface:
      commit_policy:
      push_policy:
    source_authority:
      canonical_sources:
      forbidden_authority_sources:
      source_conflict_policy:
    path_boundaries:
      allowed_files:
      forbidden_paths:
      path_rule:
      unlisted_path_policy:
    change_set:
      - change_id:
        path:
        operation:
        current_state_requirement:
        allowed_change:
        no_other_changes_allowed: true
    validation:
      validation_required: true
      commands_or_checks:
      eof_checks:
      diff_checks:
      validation_absent_policy:
    project_refresh_requirements:
      project_instruction_ui_update_required:
      project_sources_files_refresh_required:
      request_only_sources_refresh_required:
      do_not_upload_as_project_file:
    return_contract:
      required_return_fields:
  copy_paste_packet:
  expected_return_packet:
    changed_files:
    validation_output:
    commit_or_write_evidence:
    source_limitations:
    residual_risks:
```

`storage_update_package.v1` from `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` is the canonical executable schema. Local shorthand such as allowed paths, exact changes, validation checks, EOF checks, or refresh requirements may be used only as narrative aliases mapped to `path_boundaries.allowed_files`, `change_set`, `validation.commands_or_checks`, `validation.eof_checks`, and `project_refresh_requirements`.

If the admitted Storage Update Package is incomplete, do not emit a placeholder storage transfer. Choose blocked, bounded repair, or human decision only when materially correct.

### `next_material_chat`

Required additions:

```text
next_material_chat_transfer_packet:
  target_project_or_context:
  target_entrypoint:
  target_procedure_path:
  target_procedure_boundary:
  kind:
  routing_dependency_policy:
  purpose:
  source_authority:
  required_sources:
  task:
  required_inputs:
  boundaries:
  copy_paste_packet:
  expected_closure_result:
  expected_continuation:
  stop_conditions:
```

A next material chat must start its own START lifecycle. This procedure only prepares the transfer.

## Source Requirements

Required source classes:

- exact closure source or closure packet being transformed into a NEXT_CHAT_CARD continuation;
- exact FINISH_PACKET result;
- exact selected procedure context;
- exact acceptance boundary, if acceptance is relevant;
- exact persistence/storage boundary, if storage or accepted state is relevant;
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` for NEXT_CHAT_CARD continuation fields and allowed values;
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` when lifecycle state or same-chat closure matters;
- `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md` when dependency-vs-continuation, dependency type, wrong-surface, Codex/code-assistant, core lifecycle, storage, or human decision boundaries are relevant;
- `workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md` when non-mutating support dependency packet or prior packet label boundaries are relevant;
- exact target execution surface/procedure stub or active procedure source when the next move names a specific target surface.

EOF or source-integrity checks are required where the source being relied on has an EOF marker.

Source authority order:

1. exact repository files or exact accepted runtime records at a named path/ref;
2. verified excerpts supplied by the user;
3. current human input for intent and decision;
4. Project Files/Sources only as cache/context;
5. legacy evidence only as rollback or historical context, not current authority.

## Context Classification

Classify relevant context as:

```text
canonical_repository_source
accepted_record
current_human_input
verified_excerpt
dependency_evidence
candidate_context
Project_Files_cache_context
legacy_evidence
unknown_unverified
```

Rules:

- A FINISH_PACKET result is candidate or accepted only according to its explicit acceptance boundary.
- Dependency evidence is not accepted state.
- A selected next move is not accepted state.
- A storage update need is not storage authorization unless explicit update authority and a complete Storage Update Package exist.
- Current human input may select intent, but it does not override exact accepted boundaries unless the procedure is an admitted acceptance or update-authority path.

## Complexity Selector

Use the smallest sufficient path:

```text
inline:
  Use only for a trivial non-state-sensitive pointer where no formal NEXT_CHAT_CARD continuation is required.

standard:
  Use for ordinary closure next-move formation from complete closure state and clear boundaries.

checkpointed:
  Use when the primary next move is materially ambiguous and choosing it would affect acceptance, persistence, external execution, or parent routing.

research_backed:
  Normally not used. Use only if the next move depends on current external constraints that cannot be resolved from Workflow source.

delegated_or_tool_mediated:
  Use when forming the next move requires a bounded dependency/check/Codex/storage transfer packet or verification of returned dependency evidence before closure.
```

Complexity selection does not authorize procedure switching or next move launch.

## Stage Cards

### Stage 0 - Source and Closure Lock

```text
stage_id: source_and_closure_lock
purpose: Confirm exact closure state, FINISH_PACKET result, selected owner context, and relevant boundary sources before forming the next move.
activation conditions: Always.
inputs: closure_state, closure_result, selected procedure context, acceptance_boundary, persistence_boundary, source refs.
required intermediate output: source_lock, closure_state_summary, result_status, boundary_sources, source_limitations.
gate: PASS if required closure and boundary sources are present and internally consistent; REWORK if a field can be repaired from exact source; STOP if required closure state, closure result, accepted boundary, required transfer source, or destination is missing.
checkpoint rule: None by default.
expansion rule: May inspect exact target procedure/dependency-surface source needed to complete a transfer packet.
stop behavior: Return SOURCE_INTEGRITY_STOP or BLOCKED_NEXT_MOVE_SOURCE_MISSING.
```

### Stage 1 - Boundary Classification

```text
stage_id: boundary_classification
purpose: Separate acceptance, persistence, dependency evidence, candidate output, and blocked state.
activation conditions: Always after Stage 0.
inputs: closure_result, acceptance_boundary, persistence_boundary, dependency_return_status, validation, changed_files, not_done.
required intermediate output: acceptance_boundary_final, persistence_boundary_final, dependency_evidence_status, unresolved_items, prohibited_next_moves.
gate: PASS if acceptance and persistence boundaries are explicit and separate; REWORK if labels are present but ambiguous; STOP if selecting a next move would create acceptance or persistence by implication.
checkpoint rule: Checkpoint if human authority is required to decide acceptance or persistence and no accepted boundary exists.
expansion rule: May produce a bounded human_decision only when the missing item is genuinely a human decision rather than a materially known transfer packet.
stop behavior: Return ACCEPTANCE_BOUNDARY_MISSING, PERSISTENCE_BOUNDARY_MISSING, or SELF_ACCEPTANCE_RISK.
```

### Stage 2 - Next Move Candidate Set

```text
stage_id: next_move_candidate_set
purpose: Identify materially valid next move candidates without launching any of them.
activation conditions: Always after Stage 1.
inputs: result status, exact_next_move if present, unresolved_items, accepted/rejected/blocked/parked/repair state, required surfaces.
required intermediate output: candidate_next_moves, invalid_next_moves, preferred_primary_candidate, rationale.
gate: PASS if at least one valid candidate exists and invalid candidates are excluded with reasons; REWORK if the candidate set mixes multiple independent work items; STOP if no valid next move can be formed.
checkpoint rule: Checkpoint if two or more candidates are materially plausible and neither is dominated by the result state.
expansion rule: May inspect target procedure stubs/contracts to decide whether a transfer packet is required.
stop behavior: Return NEXT_MOVE_UNDETERMINED or SPLIT_REQUIRED.
```

Candidate selection priority:

1. If required source, closure state, closure result, accepted boundary, destination, or required transfer packet is missing, choose a blocked/repair/human decision path according to material cause.
2. If a required mid-RUN dependency return is still pending, missing, or unverified, do not form closure next move; stop because FINISH is premature.
3. If accepted decision plus explicit update authority and complete `storage_update_package.v1` exist, choose `storage_update` as the registered owner procedure.
4. If repair is required and the repair surface is known, choose a registered repair owner procedure and place `codex`, `check_job`, `dependency_chat`, or `next_material_chat` as a nested Transfer Packet target when needed.
5. If code repository dependency return verification is required and evidence is available but unverified, choose a registered owner procedure for the verification lifecycle and place `verify_code_repository_dependency_return` as a nested Transfer Packet target when needed.
6. If parent/dependency integration is required, choose the registered owner procedure and place `dependency_chat` or `next_material_chat` as a nested Transfer Packet target according to the parent return contract.
7. If no further work should occur, choose `stop`.
8. Use `human_decision` only when a real human choice is missing and no materially known transfer packet can be completed.

### Stage 3 - Single Primary Next Move Selection

```text
stage_id: single_primary_next_move_selection
purpose: Select exactly one primary next move and map it to a continuation target.
activation conditions: Always after Stage 2.
inputs: candidate_next_moves, result status, boundaries, destination, transfer requirements.
required intermediate output: selected_primary_next_move, selected_main_procedure_to_start, selection_reason, rejected_alternatives.
gate: PASS if exactly one primary next move is selected; REWORK if multiple next moves remain bundled; STOP if selection would launch work, accept state, persist state, or hide procedure switching.
checkpoint rule: Checkpoint if user/parent selection is materially required.
expansion rule: None except bounded target-source inspection.
stop behavior: Return MULTIPLE_NEXT_MOVES_BLOCKED or INVALID_CONTINUATION_TARGET.
```

### Stage 4 - Transfer Packet Completeness Gate

```text
stage_id: transfer_packet_completeness_gate
purpose: Ensure required external-surface next moves include complete Transfer Packets.
activation conditions: Required when the selected continuation requires a nested transfer target such as codex, verify_code_repository_dependency_return, dependency_chat, check_job, storage_update, or next_material_chat.
inputs: selected next move, target surface requirements, source authority, acceptance_boundary, persistence_boundary.
required intermediate output: complete_transfer_packet or transfer_blocker.
gate: PASS if the required Transfer Packet includes complete copy_paste_packet, expected return packet, validation, boundaries, stop conditions, and return destination; REWORK if minor exact fields can be completed from source; STOP if only a placeholder or materially incomplete packet can be produced.
checkpoint rule: Checkpoint if a human must supply a missing target, authority, or destination.
expansion rule: May inspect the exact target procedure source or execution surface contract.
stop behavior: Return REQUIRED_TRANSFER_PACKET_MISSING, TRANSFER_PACKET_PLACEHOLDER_INVALID, or STORAGE_PACKAGE_INCOMPLETE.
```

### Stage 5 - NEXT_CHAT_CARD continuation Assembly

```text
stage_id: continuation_assembly
purpose: Assemble the final NEXT_CHAT_CARD continuation using the Chat Finish Protocol fields.
activation conditions: Always after Stage 3 and Stage 4 where applicable.
inputs: selected primary next move, selected owner procedure or decision surface, transfer packet, boundaries, return destination, blockers.
required intermediate output: continuation.
gate: PASS if NEXT_CHAT_CARD or no_next_chat_needed has all required fields, exactly one continuation target when continuation is needed, complete transfer content in context_to_paste when required, and separate acceptance/persistence boundaries; REWORK if field naming or continuation shape is incomplete; STOP if closure would launch next work or mutate/accept state.
checkpoint rule: None by default.
expansion rule: None.
stop behavior: Return CONTINUATION_INVALID.
```

### Stage 6 - Closure Readiness

```text
stage_id: closure_readiness
purpose: Verify the procedure can close without pending required dependency returns or hidden continuation.
activation conditions: Always.
inputs: continuation, result status, dependency_return_status, unresolved_items.
required intermediate output: closure_readiness_result, unresolved_items_final, CLOSURE_CHECK readiness.
gate: PASS if no required DEPENDENCY_CALL return is pending, missing, or unverified and the NEXT_CHAT_CARD continuation is complete; STOP if closure would happen before required dependency return verification; PASS_WITH_RISK if limitations are explicit and non-blocking.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return EXTERNAL_RETURN_REQUIRED_STOP or CLOSURE_BLOCKED.
```

## Gate Outcomes

Use these gate outcomes:

```text
PASS
PASS_WITH_RISK
REWORK
EXPAND
STOP
TRANSFER
DEPENDENCY_CALL
DEPENDENCY_RETURN
```

`TRANSFER` in this procedure means producing a closure transfer packet as part of the NEXT_CHAT_CARD continuation. It does not launch the transfer.

`DEPENDENCY_CALL` is allowed only if this selected `form_current_next_move` RUN itself requires an external dependency result before it can complete the NEXT_CHAT_CARD continuation. It is not the same as closure transfer content carried inside `NEXT_CHAT_CARD.context_to_paste`. Prior packet labels are unsupported.

## Optional Expansion

Allowed expansion is limited to:

- reading exact target procedure, dependency surface, or procedure-boundary sources needed to complete the selected Transfer Packet;
- producing a bounded check/dependency/Codex/storage transfer packet as a closure artifact;
- asking for a human decision only when the missing information is genuinely not derivable and not a materially known required transfer;
- verifying a returned external result only if the same selected RUN emitted a `DEPENDENCY_CALL` and the return is needed before closure.

Expansion must not:

- execute the next move;
- start a new material lifecycle;
- mutate storage;
- accept output;
- turn this procedure into a general router;
- broaden beyond the closure next-move problem.

## Research Policy

External/current research is not required by default.

Use:

```text
forbidden:
  Default for ordinary NEXT_CHAT_CARD continuation formation from Workflow closure state.

optional:
  Only when external tool/provider behavior affects packet wording but internal Workflow sources are sufficient.

required:
  Only when a next move depends on current external constraints that cannot be safely specified from internal source, such as provider-specific availability, legal/regulatory constraints, or current repository protection behavior not present in source.
```

If research is required, this procedure must not invent the answer. It must produce a bounded check/research handoff or blocked/human decision path, according to the material blocker.

## Dependency / Continuation Decision Gate

This procedure is a `core` owner and may use dependency support only through the Routing and Dependency Protocol.

Dependency use is allowed only when needed to complete the current NEXT_CHAT_CARD continuation formation work. It must not become procedure switching, hidden mutation, hidden acceptance, hidden next work, or an unbounded external wait.

Common dependency choices:

```text
common_dependency_choices:
  - check_job_packet for bounded source/evidence/consistency checks needed before selecting the next move
  - dependency_chat_packet for bounded supporting work needed before selecting the next move
  - code_repository_dependency_packet only as a closure transfer artifact nested under an owner procedure, not as a launched run
  - verify_code_repository_dependency_return only for evidence from a matching dependency call when verification is part of current owner work and remains nested under the owner
  - storage_update_package only as closure transfer artifact after acceptance/update authority is clear
  - project_refresh_instruction_packet for reporting refresh requirements only

forbidden_dependency_categories:
  - any dependency used to launch the selected next move invisibly
  - any dependency used to mutate state without admitted write gate and verified return
  - any dependency used to accept this procedure's own output
  - any dependency used to convert NEXT_CHAT_CARD continuation into a mid-RUN dependency call
```

## Dependency Policy

```text
routing_dependency_policy:
  DEPENDENCY_CALL may be emitted only when this selected main procedure RUN cannot complete NEXT_CHAT_CARD continuation formation without an external dependency result.

external_return_policy:
  DEPENDENCY_RETURN must resume the same selected main procedure and match the emitted dependency call.

external_return_verification:
  Returned evidence must be classified as dependency evidence and verified before it affects the NEXT_CHAT_CARD continuation.

embedded_verification_policy:
  Embedded verification may check a returned Codex/check/dependency/storage result only when it belongs to the current selected RUN or was explicitly supplied as the object to route.

storage_boundary:
  This procedure may produce a storage_update Transfer Packet when acceptance/update authority and a complete Storage Update Package exist. It must not perform storage mutation.
```

## Dependency Call and Return Policy

Distinguish two different mechanisms:

1. `DEPENDENCY_CALL` during RUN:
   - used only before this procedure can complete;
   - requires complete copy-paste packet, expected return packet, validation, and same-owner resume rule;
   - blocks FINISH until returned, verified, or explicitly abandoned as blocked.

2. `NEXT_CHAT_CARD.context_to_paste` at closure:
   - used after this procedure has selected the next move;
   - is part of FINISH / closure;
   - does not launch the next move;
   - does not keep this RUN open;
   - must include complete transfer content for external next surfaces.

The NEXT_CHAT_CARD continuation must never be used as the substitute for a required mid-RUN `DEPENDENCY_CALL`.

## Project Refresh Reporting

Report refresh requirements for the scoped current-next-move formation context as:

```yaml
project_instruction_ui_update_required: false
project_sources_files_refresh_required: false
request_only_sources_refresh_required: true
do_not_upload_as_project_file: true
```

Do not update ChatGPT Project Instructions UI or Project Files/Sources from this procedure. Report refresh requirements only.

## Checkpoint Policy

No checkpoint is required when:

- closure state is complete;
- result status and exact next move are clear;
- acceptance and persistence boundaries are explicit;
- a required transfer packet can be fully produced.

Checkpoint or stop when:

- acceptance or persistence authority is unclear;
- the destination is missing;
- multiple primary next moves are materially plausible;
- the required transfer packet cannot be completed;
- the closure state indicates a pending, missing, or unverified required `DEPENDENCY_CALL` return;
- selecting the next move would decide acceptance, mutate storage, or launch work.

## Completion Contract

```text
completion:
  result: next move formation result with one primary next move and complete NEXT_CHAT_CARD or no_next_chat_needed
  proof: source closure state, boundary classification, rejected alternatives, transfer/card completeness, validation, and limitations are recorded
  blocked_if: closure state, selected procedure context, acceptance/persistence boundary, return destination, transfer/card content, or required dependency return is missing or unverified
```
## Output Contract

Primary output:

```text
next_move_formation_result:
  status:
  source_lock:
  closure_state_summary:
  boundary_classification:
  selected_primary_next_move:
  rejected_alternatives:
  transfer_packet_completeness:
  NEXT_CHAT_CARD or no_next_chat_needed:
  validation:
  source_limitations:
  residual_risks:
```

Required continuation:

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

Closure output:

```text
CLOSURE_CHECK:
  lifecycle_state:
  selected_work:
  run_result_summary:
  unresolved_items:
  dependency_return_status:
  finish_gate:
```

After explicit FINISH / ФИНИШ, closure must include:

```text
FINISH_PACKET:
  lifecycle_state:
  finished_work:
  finish_self_audit:
  result:
  continuation:
    NEXT_CHAT_CARD or no_next_chat_needed
```

## Quality Checks

Procedure Definition checks:

- Purpose is specific and bounded.
- Trigger and non-trigger are distinguishable.
- Required inputs are explicit.
- Source requirements are explicit.
- Context classification exists.
- Complexity selector exists.
- Stage Cards use material gates.
- Gate outcomes include STOP, REWORK, EXPAND, TRANSFER, DEPENDENCY_CALL, and DEPENDENCY_RETURN where applicable.
- Output contract is downstream-usable.
- Stop conditions prevent invention, boundary crossing, hidden mutation, hidden acceptance, and hidden next launch.
- Dependency decision gate is explicit.
- External dependency/resume policy is explicit.
- Closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed continuation correctly.
- Canonical path matches registry metadata, and kind matches registry metadata.

Procedure Execution checks:

- START selected exactly one main procedure.
- RUN executed only this selected procedure.
- No procedure switch occurred.
- Required sources were read or limitations stated.
- Closure next move selects exactly one primary next move.
- The selected next move is justified from FINISH/CLOSURE evidence, accepted decision state, pending blockers, or current bottleneck.
- Required nested transfer packet is complete for `codex`, `verify_code_repository_dependency_return`, `dependency_chat`, `check_job`, `storage_update`, or `next_material_chat`.
- Vague continuation, multiple simultaneous next steps, and hidden procedure launch are invalid.
- `human_decision` is not used as transfer avoidance.
- NEXT_CHAT_CARD continuation is not used for mid-RUN `DEPENDENCY_CALL`.
- FINISH is not requested while a required dependency return is pending, missing, or unverified.
- Final closure does not launch next work.

Cross-boundary checks:

- Compatible with Acceptance Decision:
  - accepted decision plus explicit update authority may route to `storage_update` with complete Storage Update Package;
  - `repair_required` may route to bounded repair through an allowed next surface with complete transfer packet where required;
  - blocked, parked, or rejected decisions preserve acceptance and persistence boundaries and do not silently start work.
- Compatible with Storage Update:
  - `storage_update` next move requires complete copy-paste packet for `storage_update`;
  - full admitted `storage_update_package.v1` must be included;
  - incomplete storage package blocks or routes to materially correct repair/human decision, not placeholder transfer.

## Stop Conditions

Stop or return blocked result when:

- required closure state is missing;
- FINISH_PACKET result is missing;
- selected procedure context is missing;
- acceptance boundary is missing where acceptance affects next move;
- persistence boundary is missing where storage affects next move;
- required return destination is missing;
- selected continuation target is not allowed;
- more than one primary next move remains selected;
- required transfer packet is missing or incomplete;
- transfer packet contains placeholders instead of copy-paste content;
- Storage Update Package is incomplete for `storage_update`;
- `human_decision` is being used to avoid a known required transfer packet;
- next move selection would mutate repository/runtime state;
- next move selection would accept candidate output;
- next move selection would launch work;
- NEXT_CHAT_CARD continuation is being used as mid-RUN `DEPENDENCY_CALL`;
- required dependency return is still pending, missing, or unverified before FINISH is requested;
- exact repository/source authority cannot support the selected packet.

## Procedure Closure

This procedure closes by returning:

- source lock and limitations;
- boundary classification;
- selected single primary next move;
- rejected alternatives;
- complete Transfer Packet if required;
- valid NEXT_CHAT_CARD continuation;
- FINISH_PACKET result;
- CLOSURE_CHECK before FINISH;
- FINISH_PACKET only after explicit FINISH / ФИНИШ.

After FINISH, the same chat is closed for material work. The selected next move may be started only through its emitted Transfer Packet or through a new admitted lifecycle, never by hidden continuation.

## Examples

### Example: accepted result needs storage update

```text
NEXT_CHAT_CARD:
  title: Persist the accepted procedure update through storage_update.
  why: Accepted result has admitted storage update need and a complete package.
  main_procedure_to_start: storage_update
  context_to_paste:
    return_destination: parent governance run
    transfer_packet:
      transfer_type: storage_update
      target_entrypoint: persist_accepted_state
      target_procedure_boundary: storage_update
      admitted_storage_update_package:
        package_version: storage_update_package.v1
        canonical_schema_ref: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
        update_authority:
          authority_type: accepted_update_authority
          authority_ref: explicit accepted decision
        path_boundaries:
          allowed_files:
            - workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
          forbidden_paths:
            - all other paths
        change_set:
          - change_id: replace_current_next_move_stub
            path: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
            operation: update
        validation:
          commands_or_checks:
            - EOF marker present
            - registry metadata unchanged
            - no placeholder transfer text
        project_refresh_requirements:
          project_instruction_ui_update_required: false
          project_sources_files_refresh_required: false
          request_only_sources_refresh_required: true
          do_not_upload_as_project_file: true
      copy_paste_packet: complete storage_update_package.v1 packet
    persistence_boundary: Storage allowed only for listed accepted file/package.
    acceptance_boundary: Acceptance already granted by separate accepted decision.
  expected_result: storage update result with evidence or typed blocker.
  evidence_or_return_needed: changed files or no-op evidence, validation, refresh requirements, and commit/branch if applicable.
  start_instruction: START with storage_update using the pasted package.
```

### Example: repair required but dependency packet is known

```text
NEXT_CHAT_CARD:
  title: Start bounded repair owner run.
  why: Current lifecycle is explicitly blocked or completed, and a separate repair owner run is required.
  main_procedure_to_start: author_workflow_procedure
  context_to_paste:
    repair_goal: apply bounded repair through the registered owner procedure.
    current_goal_boundary: If repair is still required for the current START goal, emit DEPENDENCY_CALL before closure and do not use NEXT_CHAT_CARD.
    dependency_needed_if_repair_requires_codex:
      DEPENDENCY_CALL:
        dependency_type: code_repository_dependency
        execution_surface: Codex/code assistant
        unresolved_until_returned: true
        expected_return_packet:
          changed_files:
          validation_outputs:
          final_commit_sha:
        parent_verification_required:
          - branch/commit/changed files
          - allowed/forbidden paths
          - validation
          - EOF markers
          - refresh categories
    boundary: Codex/code-assistant output is dependency evidence only, not selected main procedure and not completion.
  expected_result: owner procedure completes or blocks after dependency return verification.
  evidence_or_return_needed: verified dependency return evidence or explicit blocked result.
  start_instruction: START with the registered core owner procedure for the repair goal.
```

### Example: missing human choice is real

```text
NEXT_CHAT_CARD:
  title: Ask human to choose between mutually exclusive accepted routing targets.
  why: ROUTING_TARGET_CHOICE_REQUIRED.
  main_procedure_to_start: human_decision
  context_to_paste:
    return_destination: current governance operator
    persistence_boundary: No persistence authority yet.
    acceptance_boundary: Candidate remains unaccepted until explicit decision.
  expected_result: one explicit routing target or blocked escalation.
  evidence_or_return_needed: human selection with any required authority.
  start_instruction: Ask the human for the routing decision before starting material continuation.
```

This is valid only when the procedure cannot materially know the target. It is invalid when a required Codex, storage, check, dependency, or next-chat transfer packet is already materially known.

### Example: invalid placeholder

```text
NEXT_CHAT_CARD.context_to_paste: Needed if using Codex
```

This is invalid. The procedure must instead emit a complete Codex transfer packet or block with the exact missing fields.

END_OF_FILE: workflow_v3/procedures/CURRENT_NEXT_MOVE_FORMATION_PROCEDURE.md
