# Procedure: Acceptance Decision Formation

title: Acceptance Decision Formation
status: active_procedure
canonical_location: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md
entrypoint: accept_candidate_entity
procedure_boundary: acceptance_review
kind: core
routing_dependency_policy: dependency_allowed_when_needed
dependency_model_policy: dependency_labels_only_old_labels_unsupported

## Purpose

Review a candidate result and its evidence, then form exactly one explicit scoped acceptance decision:

- `accepted`
- `rejected`
- `repair_required`
- `blocked`
- `parked`

This procedure separates candidate quality from acceptance, acceptance from update authorization, and update authorization from storage execution. It may identify `storage_update_need` and may prepare a bounded candidate or transfer Storage Update Package only when update authority, exact path boundaries, exact changes, EOF requirements, validation, and return fields are explicit.

This procedure must not write repository or runtime state directly. Acceptance is not implied by validation success, file existence, Codex return, storage return, producer confidence, silence, or conversation momentum.

## Trigger / When to Use

Use this procedure when all are true:

- START selected `accept_candidate_entity`.
- The selected procedure boundary is `acceptance_review`.
- A candidate result, artifact, record, return packet, or proposed state change needs explicit review.
- Reviewer authority and affected scope can be supplied or bounded.
- The output needed is an acceptance decision record or a blocked result explaining why a decision cannot be formed.

Typical candidate sources:

- a formation chat result;
- a parent integration result;
- a Codex/code-assistant dependency return after verification as evidence;
- a check-job result;
- a proposed storage update need that still requires acceptance boundary review.

## When Not to Use

Do not use this procedure to:

- mutate repository/runtime state;
- persist accepted state;
- execute a Storage Update Package;
- let an execution surface, Codex run, support dependency, check job, or storage surface accept its own output;
- infer acceptance from silence, validation success, existing files, push status, or returned artifacts;
- accept a scope broader than the reviewed evidence supports;
- continue into a semantic next step;
- use `human_decision` to avoid a materially known required Transfer Packet;
- treat Project Files/Sources cache, chat memory, or legacy Direction files as accepted state;
- repair the candidate directly unless the selected acceptance review only produces a bounded repair next move or packet.

## Required Inputs

Required START/lifecycle inputs:

```text
selected_entrypoint: accept_candidate_entity
selected_procedure_path: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md
procedure_boundary: acceptance_review
kind: core
routing_dependency_policy: dependency_allowed_when_needed
dependency_model_policy: dependency_labels_only_old_labels_unsupported
```

Required review packet:

```text
ACCEPTANCE_REVIEW_PACKET:
  packet_id:
  candidate:
    candidate_id:
    candidate_type:
    candidate_origin:
    candidate_producer:
    candidate_result_ref:
    candidate_result_inline_if_needed:
    candidate_scope:
    candidate_claims:
    candidate_status:
  evidence:
    evidence_refs:
    source_refs:
    validation_refs:
    return_packets:
    exact_excerpts_if_needed:
    evidence_limitations:
    missing_evidence_known:
  reviewer_authority:
    reviewer:
    authority_source:
    authority_scope:
    independence_check:
    authority_limitations:
  affected_state_boundary:
    affected_entities:
    affected_paths:
    allowed_acceptance_scope:
    forbidden_acceptance_scope:
    downstream_dependencies:
  update_context:
    update_authorization:
    storage_update_expected:
    storage_update_package_if_known:
    validation_required_if_storage_needed:
    project_refresh_requirements_if_known:
  return_context:
    parent_handoff_id:
    parent_selected_entrypoint:
    return_destination:
    requested_next_move_boundary:
```

Do not invent missing evidence, authority, scope, or update permission. Missing required inputs produce `ACCEPTANCE_REVIEW_PACKET_MISSING_OR_INCOMPLETE`, `REVIEWER_AUTHORITY_MISSING`, or `ACCEPTANCE_SCOPE_UNBOUNDED`.

## Definitions

Candidate result/evidence:

- The artifact, closure result, return packet, diff, validation, source excerpt, or proposed state that is being reviewed.
- It is candidate context or dependency evidence until this procedure forms an explicit decision.

Reviewer authority:

- The explicit human, parent procedure, governance record, or accepted review role allowed to form the decision for the named scope.
- Reviewer authority must be independent from the producing surface or surface.

Quality decision:

- The reviewer's quality assessment of evidence sufficiency, correctness, completeness, and risk.
- Quality can support acceptance, rejection, repair, block, or park, but quality is not acceptance by itself.

Acceptance decision record/candidate:

- The explicit output of this procedure naming one decision value, reviewed scope, evidence, reviewer authority, rationale, consequences, and limitations.
- It is not storage mutation.

Update authorization:

- A separate authority statement that permits persistence planning or execution within exact storage boundaries.
- Acceptance may create a storage update need, but accepted status alone does not execute storage.

Storage update need:

- A consequence stating that accepted state should be persisted or that a rejected/repair/blocked decision does not currently permit persistence.
- It is not a write.

Storage Update Package:

- The executable storage package defined canonically as `storage_update_package.v1` in `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md`.
- This procedure may reference or prepare that canonical package only when exact update authority and package fields are present.

## Acceptance Decision Input Schema

`ACCEPTANCE_REVIEW_PACKET` is the required input envelope. It must identify:

- the candidate identity and producer;
- the evidence and validation available for review;
- the reviewer authority and independence check;
- the affected state boundary;
- update context and whether storage is expected;
- return destination and requested next-move boundary.

Input sufficiency rules:

- If the candidate identity is unclear, return `blocked`.
- If reviewer authority is missing or self-acceptance risk exists, return `blocked`.
- If evidence is missing but repair/evidence collection is possible, return `repair_required` with a bounded next move.
- If scope is too broad to safely accept, return `repair_required` or `blocked`.
- If the human/parent intentionally defers a decision without claiming acceptance, return `parked`.

## Acceptance Decision Output Schema

Return one `acceptance_decision_record`:

```text
acceptance_decision_record:
  decision_id:
  decision:
  decision_status:
  candidate_identity:
    candidate_id:
    candidate_type:
    candidate_origin:
    candidate_producer:
    candidate_scope:
  reviewer_authority:
    reviewer:
    authority_source:
    authority_scope:
    independence_check:
  evidence_review:
    evidence_refs:
    validation_refs:
    source_refs:
    return_packets_reviewed:
    evidence_sufficiency:
    missing_or_conflicting_evidence:
    source_limitations:
  quality_decision:
    value:
    rationale:
  scope_boundary:
    reviewed_scope:
    accepted_scope_if_any:
    explicitly_not_accepted:
    affected_state_boundary:
    downstream_assumptions:
  decision_rationale:
    gate_results:
    decision_reasons:
    forbidden_shortcut_checks:
  consequence:
    storage_update_need:
    update_authorization:
    storage_update_package_if_applicable:
    continuation_target:
    next_chat_card_context_to_paste:
  closure:
    closure_result_status:
    residual_risks:
    exact_next_move:
```

Allowed `decision_status` values:

```text
formed
formed_with_limitations
not_formed_blocked
```

The `decision` field must be exactly one of:

```text
accepted
rejected
repair_required
blocked
parked
```

## Decision Values

`accepted`:

- Use only when candidate identity, evidence, reviewer authority, independence, and scope all pass.
- Accepted scope must be explicit.
- Storage may be needed only as a separate consequence, and storage execution still requires update authorization and `storage_update_package.v1`.

`rejected`:

- Use when the candidate is reviewed and should not be accepted for the reviewed scope.
- Rejection must name the rejected scope and reason.
- Rejection does not mutate state and does not start replacement work.

`repair_required`:

- Use when the candidate may become acceptable after bounded repair, additional evidence, validation, scope reduction, or source correction.
- If the repair surface is known and external, include a complete Transfer Packet in the NEXT_CHAT_CARD continuation.

`blocked`:

- Use when the procedure cannot form an acceptance decision because required source, authority, independence, scope, or evidence is missing or conflicting.
- Blocked is also required when accepting would rely on forbidden shortcuts or would authorize hidden mutation.

`parked`:

- Use when a decision is intentionally deferred without accepting, rejecting, or ordering repair.
- Parked must name the parking reason, owner, and conditions for future review.

## Decision Priority Rule

Apply these rules in order:

1. If candidate identity, source authority, reviewer authority, independence, or affected scope is missing or conflicting, choose `blocked`.
2. If a forbidden shortcut would be needed to accept, choose `blocked` or `repair_required` according to whether bounded repair/evidence collection is available.
3. If evidence shows the candidate should not be used for the reviewed scope, choose `rejected`.
4. If bounded changes or additional evidence are required before acceptance can be safe, choose `repair_required`.
5. If the decision is intentionally deferred by explicit authority, choose `parked`.
6. Choose `accepted` only after all review, authority, independence, evidence, scope, and consequence gates pass.

Exactly one primary decision must be emitted. Do not bundle alternatives as co-equal decisions.

## Source Requirements

Before forming a decision, read and verify:

- exact candidate result or return packet;
- evidence refs, validation refs, source refs, and exact excerpts needed for claims;
- selected producer and surface identity;
- reviewer authority source and independence statement;
- affected state/path boundary;
- update authorization and storage package if persistence may be needed;
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` for `acceptance_review`;
- `workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md` for dependency type selection, execution surface, code/repository routing, and prior-packet-label rejection;
- `workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md` for support-dependency packet shape and prior execution-surface labels;
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` for FINISH_PACKET result and NEXT_CHAT_CARD continuation closure;
- `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` when a Storage Update Package is referenced or prepared.

Source authority rules:

- exact repository/runtime files or accepted records at named path/ref win over cache/context;
- verified excerpts may support the reviewed scope when exact source is not otherwise available;
- current human input may supply intent or authority only within its stated scope;
- Project Files/Sources and chat memory are cache/context only;
- legacy evidence is historical unless separately admitted.

STOP or return `blocked` when required source is unreadable, truncated, stale, conflicting, or lacks required EOF evidence.

## Context Classification

Classify all relevant inputs as:

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

Classification rules:

- candidate output is not accepted state by existence;
- dependency evidence is not accepted state;
- validation success is evidence, not acceptance;
- storage return evidence is evidence, not acceptance;
- update authorization is not storage execution;
- a Storage Update Package is not a write;
- a NEXT_CHAT_CARD continuation is routing, not accepted state.

## Complexity Selector

Use the smallest sufficient path:

- `inline`: invalid or missing packet can be blocked without review.
- `standard`: candidate, evidence, authority, scope, and consequence boundaries are complete.
- `checkpointed`: human/parent authority must decide between materially plausible review outcomes.
- `delegated_or_tool_mediated`: a bounded check, support dependency, Codex verification, or source read is needed before decision formation.
- `research_backed`: not used by default; use only when current external constraints are required for the acceptance judgment and cannot be resolved from internal sources.

Complexity selection does not authorize mutation, self-acceptance, or hidden next work.

## Stage Cards

### Stage 0 - Acceptance Review Source Lock

```text
stage_id: acceptance_review_source_lock
purpose: Lock exact candidate, evidence, authority, scope, and procedure sources before review.
activation conditions: Always.
inputs: ACCEPTANCE_REVIEW_PACKET, Procedure Registry metadata, procedure boundary contract, required source refs.
required intermediate output: source_lock, candidate_ref, evidence_refs, reviewer_authority_ref, affected_scope, source_limitations.
gate: PASS if required sources and EOF/integrity checks are available; REWORK if a bounded missing ref can be supplied; STOP if source authority is missing, stale, unreadable, or conflicting.
checkpoint rule: None by default.
expansion rule: Read only exact sources needed for acceptance review.
stop behavior: Return SOURCE_INTEGRITY_STOP or ACCEPTANCE_REVIEW_PACKET_MISSING_OR_INCOMPLETE.
```

### Stage 1 - Candidate Identity Gate

```text
stage_id: candidate_identity_gate
purpose: Prove what candidate is being reviewed and who or what produced it.
activation conditions: Always after Stage 0.
inputs: candidate block, candidate result refs, producer/surface identity.
required intermediate output: candidate_identity, candidate_scope, producer_surface, candidate_status.
gate: PASS if identity and scope are exact; REWORK if labels can be corrected from exact source; STOP if identity or scope is ambiguous.
checkpoint rule: None.
expansion rule: None beyond exact candidate source readback.
stop behavior: Return CANDIDATE_IDENTITY_UNCLEAR.
```

### Stage 2 - Reviewer Authority and Independence Gate

```text
stage_id: reviewer_authority_independence_gate
purpose: Confirm the reviewer can decide this scope and is not the producing surface/surface accepting its own output.
activation conditions: Always after Stage 1.
inputs: reviewer_authority block, candidate producer, authority source, independence check.
required intermediate output: authority_scope, independence_result, self_acceptance_risk.
gate: PASS if authority is explicit and independent; STOP if authority is missing, scope does not cover the candidate, or self-acceptance risk exists.
checkpoint rule: Checkpoint if current human input can supply exact authority but has not done so.
expansion rule: None.
stop behavior: Return REVIEWER_AUTHORITY_MISSING or SELF_ACCEPTANCE_RISK.
```

### Stage 3 - Evidence Sufficiency Gate

```text
stage_id: evidence_sufficiency_gate
purpose: Review whether evidence supports the candidate claims and requested acceptance scope.
activation conditions: Always after Stage 2.
inputs: evidence refs, validation refs, source refs, return packets, evidence limitations.
required intermediate output: evidence_sufficiency, missing_or_conflicting_evidence, quality_decision.
gate: PASS if evidence is sufficient for the reviewed scope; PASS_WITH_RISK only when limitations are explicit and accepted scope excludes unsupported claims; REWORK if bounded missing evidence can be collected; STOP if required evidence is absent or conflicting.
checkpoint rule: Checkpoint if accepting with limitations requires explicit reviewer choice.
expansion rule: May produce bounded check/verification packet; do not accept until returned evidence is verified.
stop behavior: Return EVIDENCE_INSUFFICIENT or EVIDENCE_CONFLICT.
```

### Stage 4 - Scope Boundary Gate

```text
stage_id: scope_boundary_gate
purpose: Separate reviewed, accepted, rejected, not accepted, and downstream affected scopes.
activation conditions: Always after Stage 3.
inputs: affected_state_boundary, candidate_scope, evidence_sufficiency, authority_scope.
required intermediate output: reviewed_scope, accepted_scope_if_any, explicitly_not_accepted, affected paths/entities, downstream assumptions.
gate: PASS if reviewed scope is bounded and no scope broadening occurs; REWORK if scope can be narrowed from exact evidence; STOP if safe scope cannot be formed.
checkpoint rule: Checkpoint if the reviewer must choose a reduced acceptance scope.
expansion rule: None.
stop behavior: Return ACCEPTANCE_SCOPE_UNBOUNDED or SCOPE_BROADENING_BLOCKED.
```

### Stage 5 - Decision Classification Gate

```text
stage_id: decision_classification_gate
purpose: Select exactly one decision value from the allowed set.
activation conditions: Always after Stage 4.
inputs: gate results, quality_decision, authority, evidence, scope, reviewer intent if any.
required intermediate output: decision, decision_status, rationale, rejected_alternatives.
gate: PASS if exactly one allowed decision is selected with reasons; REWORK if decision wording is ambiguous; STOP if no valid decision can be selected.
checkpoint rule: Checkpoint if two or more valid outcomes require human/parent choice.
expansion rule: None.
stop behavior: Return ACCEPTANCE_DECISION_UNFORMED.
```

### Stage 6 - Consequence and Storage Boundary Gate

```text
stage_id: consequence_storage_boundary_gate
purpose: Determine storage update need, update authorization, and next move without executing storage or hidden work.
activation conditions: Always after Stage 5.
inputs: decision, update_context, affected paths, Storage Update Package if known, return destination.
required intermediate output: storage_update_need, update_authorization, storage package completeness, continuation_target, next_chat_card_context_to_paste.
gate: PASS if consequences match the decision and storage boundaries remain separate; REWORK if a candidate package can be completed from exact fields; STOP if storage-ready status would require missing authority, missing paths, missing validation, or direct mutation.
checkpoint rule: Checkpoint if update authorization is possible but not explicit.
expansion rule: May prepare a complete `storage_update_package.v1` candidate or transfer packet only from exact fields.
stop behavior: Return STORAGE_UPDATE_BOUNDARY_MISSING or WRITE_NOT_ADMITTED.
```

### Stage 7 - Closure

```text
stage_id: closure
purpose: Return the decision record, FINISH_PACKET result, NEXT_CHAT_CARD continuation, limitations, residual risks, and CLOSURE_CHECK readiness.
activation conditions: Always after decision or blocked result.
inputs: all prior stage outputs.
required intermediate output: acceptance_decision_record, closure_result, continuation, source_limitations, residual_risks, CLOSURE_CHECK.
gate: PASS if decision record and closure packets are complete; PASS_WITH_RISK if limitations are explicit; STOP if closure would hide acceptance, mutation, next work, or pending dependency return.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return ACCEPTANCE_CLOSURE_INCOMPLETE.
```

## Gate Outcomes

Use:

- `PASS` when the stage is sufficient to continue or close.
- `PASS_WITH_RISK` only for explicit limitations that do not broaden acceptance.
- `REWORK` only before decision when exact missing fields can be supplied without inference.
- `EXPAND` only for bounded evidence, verification, or source checks needed for this acceptance review.
- `STOP` when source, authority, independence, scope, evidence, or storage boundary is unsafe.
- `TRANSFER` only as a closure NEXT_CHAT_CARD continuation artifact; it does not launch the transfer.
- `DEPENDENCY_CALL` only when this selected acceptance review needs external evidence before forming the decision.
- `DEPENDENCY_RETURN` only to resume this same selected review after matching returned evidence.
- Prior packet labels are unsupported for dependency call/return fields.

## Forbidden Shortcut Checks

Every acceptance decision must explicitly record these checks:

```text
no_acceptance_from_silence
no_acceptance_from_validation_success_alone
no_acceptance_from_file_existence
no_acceptance_from_codex_return_alone
no_acceptance_from_storage_return_alone
no_execution surface_self_acceptance
no_scope_broadening
no_direct_storage_mutation
no_hidden_next_work
no_human_decision_as_transfer_packet_avoidance
```

All checks must be `PASS` for `accepted`. Any `FAIL` requires `blocked`, `repair_required`, `rejected`, or `parked` according to the material cause.

## Optional Expansion

Allowed expansion:

- read exact candidate/evidence/source refs named in the review packet;
- request a bounded check job or verification packet for missing evidence;
- prepare a complete repair, check, Codex, dependency, next material chat, or storage transfer packet as a closure artifact when the next surface is materially known;
- prepare a candidate `storage_update_package.v1` only when update authority and exact boundaries exist.

Forbidden expansion:

- direct storage mutation;
- acceptance by producing surface or external surface;
- hidden repair execution;
- hidden next work launch;
- broad repository search to invent accepted scope;
- Project UI update or Project Files/Sources refresh.

## Research Policy

Research posture is `forbidden` by default for ordinary acceptance review.

Use `optional` or `required` research only when the acceptance question depends on current external facts that cannot be resolved from exact internal sources and verified evidence. If research is required, emit a bounded check/research transfer or blocked result; do not invent external facts.

## Routing / Dependency Decision Gate

This procedure is a `core` owner and may use global dependency support only through the routing/dependency gate.

Dependency use is allowed only when needed to complete this acceptance review. It must not become procedure switching, hidden mutation, hidden acceptance, hidden next work, or an unbounded external wait.

Common dependency choices:

```text
common_dependency_choices:
  - support_dependency for bounded evidence/source/consistency checks
  - verify_code_repository_dependency_return for returned Codex evidence supplied to this review
  - support_dependency only for bounded supporting evidence collection
  - storage_update_package only as a candidate or closure transfer artifact after acceptance/update boundaries are explicit
  - project_refresh_instruction_packet for reporting refresh requirements only

forbidden_dependency_categories:
  - any dependency used to accept its own output
  - any dependency used to mutate state directly from this procedure
  - any dependency used to bypass update authorization or Storage Update Package v1
  - any dependency used to launch the selected next move invisibly
```

## Routing / Dependency Policy

```text
routing_dependency_policy:
  DEPENDENCY_CALL may be emitted only when this selected acceptance review cannot form the decision without external evidence.

external_return_policy:
  DEPENDENCY_RETURN must resume this same selected procedure and match the emitted dependency call.

external_return_verification:
  Returned evidence must be classified as dependency evidence and verified before it affects the acceptance decision.

embedded_verification_policy:
  Verification supports evidence review; it does not accept the result by itself.

storage_boundary:
  Acceptance Decision may produce storage_update_need or a candidate/transfer `storage_update_package.v1` only when update authority and exact package fields are explicit. It must not perform storage mutation.
```

External repository/code writes require visible `DEPENDENCY_CALL` with `dependency_type: code_repository_dependency`, write gate, exact paths, validation, and verified `DEPENDENCY_RETURN`. This procedure does not execute those writes directly.

## Dependency Call and Return Policy

`DEPENDENCY_CALL` is a mid-RUN gate for missing evidence before decision formation. It must include:

```text
dependency_type:
external_surface:
copy_paste_packet_required:
expected_return_packet:
validation_required_on_return:
resume_rule: resume the same selected main procedure
```

`NEXT_CHAT_CARD.context_to_paste` is a closure artifact after this procedure forms or blocks the decision. It does not launch work and must carry complete transfer content when the next surface is `codex`, `verify_code_repository_dependency_return`, `support_dependency`, `check_job`, `storage_update`, or `next_material_chat`.

FINISH must not be requested while a required dependency return is pending, missing, or unverified.

## Checkpoint Policy

No checkpoint is required when candidate identity, evidence, authority, scope, and consequences are complete and one decision is materially required.

Checkpoint or stop when:

- reviewer authority can be supplied by current human input but is not explicit;
- a reduced accepted scope requires human/parent choice;
- two or more decision values remain materially plausible;
- update authorization is possible but not explicit;
- required evidence can be collected but the collection path needs approval.

Do not use checkpoints to imply acceptance or storage authority.

## Completion Contract

```text
completion:
  result: acceptance decision result with exactly one scoped decision or blocked decision record
  proof: candidate identity, reviewer authority, evidence review, scope boundary, consequence, storage/update need, validation, and limitations are recorded
  blocked_if: candidate identity is ambiguous, evidence is insufficient, reviewer authority is absent, update boundary is missing, direct mutation is requested, or required dependency return is pending, missing, or unverified
```
## Output Contract

```yaml
acceptance_decision_result:
  status: formed | formed_with_limitations | blocked
  acceptance_decision_record:
    decision_id:
    decision:
    decision_status:
    candidate_identity:
    reviewer_authority:
    evidence_review:
    quality_decision:
    scope_boundary:
    decision_rationale:
    consequence:
    closure:
  storage_update_need:
    value: needed_and_authorized | needed_but_not_authorized | not_needed | blocked_missing_update_boundary
    reason:
  storage_update_package_if_applicable:
    package_version: storage_update_package.v1 | not_applicable
    canonical_schema_ref: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
  continuation:
  validation:
  source_limitations:
  residual_risks:
  CLOSURE_CHECK:
```

After explicit FINISH or ФИНИШ, closure must include FINISH_PACKET and a NEXT_CHAT_CARD or no_next_chat_needed continuation as defined by `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`.

## Storage Update Package Requirements

Storage Update Package v1 is canonical in `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md`. This procedure must not define a second executable schema.

When this procedure prepares a storage consequence, any local shorthand must map to the canonical fields:

```text
path_boundaries.allowed_files
path_boundaries.forbidden_paths
change_set
validation.commands_or_checks
validation.eof_checks
project_refresh_requirements
return_contract.required_return_fields
```

Storage-ready status is allowed only when all are true:

- decision is `accepted` within exact scope;
- update authorization is explicit;
- the Storage Update Package uses `package_version: storage_update_package.v1`;
- exact allowed files and forbidden paths are present;
- exact changes are present in `change_set`;
- EOF and validation checks are present;
- project refresh requirements are present;
- expected return fields are present.

If any required storage field is missing, set:

```text
storage_update_need: needed_but_not_authorized | blocked_missing_update_boundary
storage_update_package_if_applicable: not_applicable
```

## Project Refresh Reporting

Report refresh requirements for the scoped acceptance decision context as:

```yaml
project_instruction_ui_update_required: false
project_sources_files_refresh_required: false
request_only_sources_refresh_required: true
do_not_upload_as_project_file: true
```

Do not update ChatGPT Project Instructions UI or Project Files/Sources from this procedure. Report refresh requirements only.

## Eval / Quality Checks

Procedure Definition checks:

- Purpose is specific and bounded.
- Trigger and non-trigger are distinguishable.
- Required inputs and `ACCEPTANCE_REVIEW_PACKET` schema are explicit.
- Decision values are exactly `accepted`, `rejected`, `repair_required`, `blocked`, and `parked`.
- Source requirements and context classification are explicit.
- Complexity selector exists.
- Stage Cards produce intermediate outputs and real gates.
- Forbidden shortcut checks are mandatory.
- Candidate quality, acceptance, update authorization, and storage execution are separate.
- Dependency decision gate and execution surface policy are explicit.
- External dependency-call/resume policy is explicit.
- Closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed continuation.
- Canonical path matches registry metadata, and kind matches registry metadata.

Procedure Execution checks:

- START selected exactly one main procedure.
- RUN executed only this selected procedure.
- No producing surface or external surface accepted its own output.
- Evidence review occurred before acceptance decision.
- Acceptance scope did not broaden beyond evidence and authority.
- No direct storage mutation occurred.
- Storage Update Package v1 was used as canonical executable storage schema.
- FINISH was requested only after decision or blocked result and no pending, missing, or unverified required dependency return.
- NEXT_CHAT_CARD continuation selected exactly one primary next move and did not launch it.

Cross-boundary checks:

- Storage Update verifies and executes storage packages; Acceptance Decision does not write state directly.
- Current Next Move may route an acceptance result to storage only with a complete Storage Update Package v1 transfer packet.
- External repository/code writes require visible `DEPENDENCY_CALL`, `code_repository_dependency` routing to Codex/code assistant, exact paths, validation, and verified `DEPENDENCY_RETURN`.

## Stop Conditions

Stop or return `blocked` when:

- `ACCEPTANCE_REVIEW_PACKET` is missing or incomplete;
- candidate identity is ambiguous;
- candidate result/evidence is unreadable, truncated, stale, or conflicting;
- reviewer authority is absent or outside scope;
- independence check fails or self-acceptance risk exists;
- evidence is insufficient and no bounded repair/evidence path exists;
- accepted scope would exceed reviewed evidence or authority;
- acceptance would rely on silence, validation success alone, file existence, Codex return alone, storage return alone, or producer confidence;
- update authorization is absent but storage-ready status is requested;
- direct storage mutation is requested;
- a Storage Update Package would require alternate schema fields instead of `storage_update_package.v1`;
- a required Transfer Packet is missing or a placeholder;
- required dependency return is pending, missing, or unverified before FINISH is requested;
- the procedure would launch repair, storage, Codex, dependency, check, or next material work directly.

## Procedure Closure

RUN completion requests FINISH only after:

- exactly one decision is formed or a blocked result explains why not;
- forbidden shortcut checks are recorded;
- evidence and source limitations are listed;
- acceptance scope and explicitly not accepted scope are separated;
- storage/update consequence is explicit;
- any required Transfer Packet is complete or the blocker is stated;
- no required dependency return is pending, missing, or unverified;
- FINISH_PACKET result and NEXT_CHAT_CARD continuation are ready.

After explicit FINISH or ФИНИШ, close with:

- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

After FINISH, the same chat is closed for material work. The selected next move may be started only through its emitted Transfer Packet or a new admitted lifecycle, never by hidden continuation.

## Examples

### Example: accepted with storage needed and authorized

```text
decision: accepted
accepted_scope_if_any: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md procedure body only
storage_update_need: needed_and_authorized
storage_update_package_if_applicable:
  package_version: storage_update_package.v1
  canonical_schema_ref: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
  path_boundaries.allowed_files:
    - workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
  validation.commands_or_checks:
    - EOF marker present
    - no forbidden wrapper metadata
```

### Example: repair required

```text
decision: repair_required
reason: Evidence supports the target role, but storage package lacks validation.commands_or_checks.
continuation_target: code_repository_dependency
next_chat_card_context_to_paste: complete bounded repair packet required
storage_update_need: blocked_missing_update_boundary
```

### Example: blocked self-acceptance

```text
decision: blocked
reason: Producing surface attempted to accept its own return.
forbidden_shortcut_checks.no_execution surface_self_acceptance: FAIL
```

### Example: parked

```text
decision: parked
reason: Authorized reviewer intentionally deferred the decision pending a named governance checkpoint.
storage_update_need: not_needed
```

END_OF_FILE: workflow_v3/procedures/ACCEPTANCE_DECISION_FORMATION_PROCEDURE.md
