# Procedure: Storage Update

title: Storage Update
status: active_procedure
canonical_location: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
entrypoint: persist_accepted_state
procedure_boundary: storage_update
kind: storage
utility_policy: callable_storage_utility_with_write_gate

## Purpose

Persist accepted state, accepted records, or accepted repository/runtime files only from a complete admitted Storage Update Package.

This procedure is a mechanical storage/write adapter. It verifies write authority, exact path boundaries, exact listed changes, source integrity, EOF requirements, validation requirements, and return evidence. It does not decide whether candidate work should be accepted.

## Trigger / When to Use

Use this procedure when all are true:

- START selected `persist_accepted_state`.
- The selected procedure boundary is `storage_update`.
- A complete Storage Update Package is provided.
- The package names exact allowed files, exact required changes, forbidden paths, validation requirements, and return fields.
- The package carries explicit accepted update authority or admitted storage authority.
- The requested work is persistence only.

Typical upstream sources:

- an Acceptance Decision result that identifies `storage_update_need`;
- a Current NEXT_CHAT_CARD continuation naming `storage_update` with complete transfer content in `context_to_paste`;
- a parent procedure result that already carries admitted storage authority and a complete Storage Update Package.

## When Not to Use

Do not use this procedure to:

- decide acceptance;
- reject or approve candidate work;
- infer acceptance from validation, silence, or user momentum;
- treat an Acceptance Decision record as write execution by itself;
- write from a vague instruction such as "save the previous result";
- use placeholders such as "use prior accepted package", "apply the obvious patch", or "same files as above";
- broaden scope beyond exact listed files and exact listed changes;
- touch unlisted paths;
- create Direction state without admitted setup/adoption authority;
- update actual ChatGPT Project Instructions UI;
- refresh Project Files/Sources directly;
- continue into a semantic next step after storage;
- use Project Files/Sources cache, chat memory, candidate docs, or legacy Direction files as accepted state.

## Required Inputs

Required START/lifecycle inputs:

```text
selected_entrypoint: persist_accepted_state
selected_procedure_path: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
procedure_boundary: storage_update
kind: storage
utility_policy: callable_storage_utility_with_write_gate
```

Required task inputs:

```text
storage_update_package:
repository_or_runtime_target:
base_ref_or_current_state_ref:
exact_return_destination:
mutation_policy:
```

Required package contents:

- package identity;
- update authority;
- source authority;
- path boundaries;
- exact file change set;
- validation requirements;
- EOF requirements;
- expected return evidence;
- project refresh reporting requirements.

Missing required inputs produce `STORAGE_UPDATE_PACKAGE_MISSING_OR_INCOMPLETE`.

## Storage Update Package Schema

A valid Storage Update Package must be complete enough to execute without reading chat memory, Project Files/Sources cache, or unstated prior packets.

```yaml
storage_update_package:
  package_version: storage_update_package.v1
  package_id: string
  produced_by:
    source_entrypoint: string
    source_procedure_path: string
    source_procedure_boundary: string
    source_result_ref: string
    source_finish_ref: string | not_applicable

  update_authority:
    authority_type: accepted_update_authority | admitted_storage_authority | explicit_human_storage_authority
    authority_ref: string
    authority_statement: string
    authority_scope:
      accepted_entity_ref: string | not_applicable
      accepted_scope_summary: string
      storage_scope_summary: string
    not_accepted_by_storage: true
    not_executed_by_acceptance: true

  repository_target:
    repository: owner/name | runtime_storage_ref
    base_ref: branch | tag | commit | runtime_state_ref
    target_ref: branch | runtime_state_ref
    expected_head_sha_before_write: string | not_applicable
    write_surface: direct_storage_update
    commit_policy: commit_required | commit_not_required | runtime_write
    push_policy: push_required | push_not_required | runtime_write

  source_authority:
    canonical_sources:
      - path: string
        ref: string
        expected_blob_sha: string | unknown_allowed_with_reason
        eof_required: true | false
        eof_marker: string | not_applicable
    forbidden_authority_sources:
      - Project Files/Sources cache
      - chat memory
      - candidate docs unless explicitly accepted and referenced
      - legacy Direction files unless separately admitted as legacy_evidence
    source_conflict_policy: stop_on_conflict

  path_boundaries:
    allowed_files:
      - exact/file/path.md
    forbidden_paths:
      - exact/file/path.md
      - exact/directory/prefix/
    path_rule: exact_allowed_files_only_no_globs_no_wildcards
    unlisted_path_policy: stop

  change_set:
    - change_id: string
      path: exact/file/path.md
      operation: create | update | delete
      change_authority_ref: string
      current_state_requirement:
        expected_exists: true | false
        expected_blob_sha_before: string | null_for_new_file
        expected_eof_marker_before: string | not_applicable
      allowed_change:
        method: complete_file_replacement | exact_patch | exact_create | exact_delete
        complete_final_content: |
          required when method is complete_file_replacement or exact_create
        exact_patch: |
          required when method is exact_patch
        required_eof_marker_after: string | not_applicable
        expected_diff_summary: string
        forbidden_content_changes:
          - string
      no_other_changes_allowed: true

  validation:
    validation_required: true
    commands_or_checks:
      - check_id: string
        command_or_manual_check: string
        expected_success_condition: string
    eof_checks:
      - path: exact/file/path.md
        required_eof_marker: string
    diff_checks:
      - only_listed_files_changed
      - only_listed_change_ids_applied
      - forbidden_paths_untouched
    validation_absent_policy: stop

  project_refresh_requirements:
    project_instruction_ui_update_required: true | false
    project_sources_files_refresh_required: true | false
    request_only_sources_refresh_required: true | false
    do_not_upload_as_project_file: true | false
    refresh_notes: string

  return_contract:
    required_return_fields:
      - status
      - changed_files
      - unchanged_files
      - created_files
      - deleted_files
      - forbidden_paths_touched
      - pre_write_refs
      - post_write_refs
      - diff_summary
      - eof_check_results
      - validation_output
      - commit_sha
      - push_status
      - project_refresh_requirements
      - source_limitations
      - residual_risks
      - exact_next_move
```

Invalid schema examples:

```text
allowed_files: workflow_v3/**
change_set: use prior package
validation: run whatever is appropriate
authority_statement: user accepted above
path: same as previous
exact_next_move: continue with next semantic task
```

## Source Requirements

Before any write, read and verify:

- exact current target file state for every listed file when the storage surface supports readback;
- exact source refs listed in `source_authority.canonical_sources` when they are needed to verify authority or current state;
- EOF markers for listed files when the package requires EOF preservation;
- the selected storage package itself as current human input, accepted record, or verified transfer packet.

Source authority rules:

- exact repository/runtime files at named path/ref win over cache/context;
- Project Files/Sources are cache/context only;
- chat memory is not accepted state;
- candidate docs are candidate context unless the package references an accepted decision/update authority;
- legacy Direction files are legacy_evidence only unless a separate accepted package changes that.

Source conflict policy:

- STOP if the package claims a current blob SHA, EOF marker, or file existence state that does not match readback;
- STOP if accepted update authority and storage package disagree on paths or scope;
- STOP if source authority depends on an unreadable source and no explicit limitation allows continuing;
- STOP if any package field requires inference from chat memory or stale Project Files/Sources.

## Context Classification

Classify all relevant inputs before write:

```text
canonical_repository_source:
  exact files read from repository/runtime refs
accepted_record:
  explicit accepted update authority or admitted storage authority
acceptance_decision_evidence:
  evidence that a candidate was accepted or selected for persistence; not write execution
update_authorization:
  explicit permission/scope to perform storage update
storage_update_package:
  executable package after schema, authority, path, and validation gates pass
actual_write_execution:
  write operation performed only after storage write gate passes
returned_storage_evidence:
  post-write changed files, refs, diff, EOF, validation, and refresh requirements
current_human_input:
  package text, corrections, or explicit direct storage authority in this chat
Project_Files_cache_context:
  non-authoritative cache
candidate_context:
  unaccepted candidate docs or proposed changes
legacy_evidence:
  old Direction or rollback evidence
unknown_unverified:
  any source not read or not matched to authority
```

Boundary rule:

- acceptance decision evidence may justify update need;
- update authorization permits storage attempt within exact bounds;
- Storage Update Package defines executable write instructions;
- actual write execution applies only listed changes;
- returned storage evidence proves what happened;
- none of these boundaries lets this procedure decide acceptance.

## Complexity Selector

Use the smallest sufficient execution shape:

- `inline`: package is missing, invalid, or no-op can be reported without writing.
- `standard`: exact package, exact paths, exact changes, exact validation, no source conflict.
- `checkpointed`: package itself requires an explicit pre-write checkpoint or a human authority statement is provided in-chat but not yet bound to the package.
- `delegated_or_tool_mediated`: direct storage tool execution is required after all write gates pass.
- `research_backed`: not used by default; external research is not required for mechanical storage updates.

If complexity would require semantic decision-making, switch to STOP rather than expanding scope.

## Stage Cards

### Stage 0 - Lifecycle and Surface Admission

```text
stage_id: lifecycle_surface_admission
purpose: Confirm this RUN is the selected storage adapter and not an embedded semantic step.
activation conditions: Always.
inputs: START_CONTRACT, Procedure Registry metadata, procedure boundary type, user/parent packet.
required intermediate output: selected_entrypoint, selected_procedure_path, procedure_boundary, kind, utility_policy.
gate: PASS if selected_entrypoint is persist_accepted_state and procedure_boundary is storage_update; STOP otherwise.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return STORAGE_SURFACE_NOT_SELECTED or BOUNDARY_CROSSING_STOP.
```

### Stage 1 - Package Presence and Schema Gate

```text
stage_id: storage_package_schema_gate
purpose: Confirm the Storage Update Package is present, complete, self-contained, and executable.
activation conditions: Always after Stage 0.
inputs: Storage Update Package.
required intermediate output: package_id, package_version, produced_by, authority block, target block, source authority block, path boundaries, change set, validation, refresh requirements, return contract.
gate: PASS if every required field is present and contains exact values; REWORK only before write if a bounded missing field can be supplied without inference; STOP if placeholders, vague references, globs, missing validation, or missing authority appear.
checkpoint rule: None by default.
expansion rule: May inspect exact packet text only; do not consult chat memory to fill missing fields.
stop behavior: Return STORAGE_UPDATE_PACKAGE_MISSING_OR_INCOMPLETE.
```

### Stage 2 - Authority Boundary Gate

```text
stage_id: storage_authority_gate
purpose: Distinguish acceptance evidence, update authorization, package instructions, write execution, and returned storage evidence.
activation conditions: Always after schema gate.
inputs: update_authority, produced_by, accepted record refs, current human input.
required intermediate output: authority_type, authority_ref, authority_scope, storage_scope, explicit statement that acceptance alone is not write execution.
gate: PASS if accepted update authority or admitted storage authority explicitly authorizes storage within exact package scope; STOP if only acceptance evidence exists or authority is ambiguous.
checkpoint rule: Checkpoint only if current human input provides exact authority but package binding is unclear.
expansion rule: None.
stop behavior: Return WRITE_NOT_ADMITTED or ACCEPTANCE_AMBIGUITY.
```

### Stage 3 - Path Boundary Gate

```text
stage_id: path_boundary_gate
purpose: Prove every requested path is explicitly allowed and no forbidden path can be touched.
activation conditions: Always after authority gate.
inputs: allowed_files, forbidden_paths, change_set paths.
required intermediate output: normalized path list, allowed path match result, forbidden path check result, unlisted path risk.
gate: PASS if every change_set path exactly matches allowed_files and no path matches forbidden_paths; STOP if any glob, wildcard, directory-wide allowance, traversal, unlisted path, or forbidden path appears.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return PATH_BOUNDARY_VIOLATION.
```

### Stage 4 - Source Integrity and Current State Gate

```text
stage_id: source_integrity_current_state_gate
purpose: Verify current file state before write.
activation conditions: Always after path gate.
inputs: repository_target, source_authority, current_state_requirement for each change.
required intermediate output: pre_write_refs, current blob SHAs, existence checks, EOF-before checks, source limitations.
gate: PASS if current state matches package expectations; PASS_WITH_RISK only when package explicitly allows unknown current SHA with reason and no overwrite ambiguity; STOP on mismatch, unreadable required source, EOF mismatch, or source conflict.
checkpoint rule: None.
expansion rule: Read only listed current files and listed canonical sources.
stop behavior: Return SOURCE_INTEGRITY_STOP or CURRENT_STATE_MISMATCH.
```

### Stage 5 - Exact Change Plan and No-op Gate

```text
stage_id: exact_change_plan_noop_gate
purpose: Build a mechanical write plan from the listed change_set only.
activation conditions: Always after source integrity gate.
inputs: change_set, current file contents, allowed_change methods.
required intermediate output: per-file final content or exact delete/create instruction, expected diff summary, no-op detection.
gate: PASS if the exact write plan can be produced without interpretation; PASS_WITH_RISK for declared no-op with evidence; STOP if final content or exact patch is missing, patch does not apply exactly, or unlisted content changes would be required.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return EXACT_CHANGE_PLAN_INVALID.
```

### Stage 6 - Write Execution Gate

```text
stage_id: write_execution_gate
purpose: Apply only listed changes through the selected storage update adapter.
activation conditions: Only after Stages 0-5 PASS or allowed no-op result.
inputs: exact write plan, pre_write_refs, repository_target.
required intermediate output: write_attempt_result, changed files, created files, deleted files, unchanged files, post_write_refs, commit/push status when applicable.
gate: PASS if write succeeded and only listed paths changed; PASS_WITH_RISK only for no-op or non-push runtime write with explicit package policy; STOP/FAIL if write tool is unavailable, write fails, or unexpected paths change.
checkpoint rule: None after write gate passes.
expansion rule: Use only storage write primitives needed for listed paths.
stop behavior: Return STORAGE_WRITE_FAILED or UNEXPECTED_PATH_CHANGE.
```

### Stage 7 - Post-write Verification Gate

```text
stage_id: post_write_verification_gate
purpose: Verify diff, EOF markers, and returned storage evidence.
activation conditions: Always after write execution or no-op.
inputs: post_write_refs, changed files, package diff checks, EOF checks.
required intermediate output: readback results, diff verification, EOF-after results, forbidden path untouched proof.
gate: PASS if post-write state matches the package exactly; STOP/FAIL if EOF is invalid, expected diff is absent, unexpected diff appears, or readback cannot verify required evidence.
checkpoint rule: None.
expansion rule: Read only listed files and storage metadata needed for verification.
stop behavior: Return STORAGE_VERIFICATION_FAILED or EOF_INVALID.
```

### Stage 8 - Validation Gate

```text
stage_id: validation_gate
purpose: Run or verify all listed validation checks.
activation conditions: Always after post-write verification.
inputs: validation.commands_or_checks, eof_checks, diff_checks.
required intermediate output: validation_output, pass/fail status, skipped validation with reason if package permits.
gate: PASS if all required validation succeeds; STOP/FAIL if validation is absent, cannot run, fails, or was skipped without explicit package policy.
checkpoint rule: None.
expansion rule: Run only listed validation checks.
stop behavior: Return VALIDATION_REQUIRED_STOP or VALIDATION_FAILED.
```

### Stage 9 - Storage Evidence and Closure

```text
stage_id: storage_evidence_closure
purpose: Return storage evidence without choosing the next semantic step.
activation conditions: Always after validation gate or blocked/no-op result.
inputs: all stage outputs.
required intermediate output: storage_update_result, changed files, validation, source limitations, refresh requirements, residual risks, CLOSURE_CHECK.
gate: PASS if output contract is complete; PASS_WITH_RISK if limitations are explicit; STOP if required return evidence is missing.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return incomplete evidence blocker.
```

## Gate Outcomes

Use:

- `PASS` when the stage is sufficient to continue or close.
- `PASS_WITH_RISK` only for explicitly bounded no-op, package-permitted unknown current SHA, or declared limitation that does not affect write safety.
- `REWORK` only before any write when exact missing package fields can be supplied without inference.
- `EXPAND` only for exact listed source readback or listed validation checks.
- `STOP` for missing package, missing authority, path broadening, source conflict, validation absence/failure, EOF invalidity, or write boundary violation.
- `TRANSFER` only as closure output if the package cannot be executed in this surface and a complete next-surface packet is included.
- `UTILITY_CALL` is not used by default by this selected storage adapter.
- `UTILITY_RETURN` is not used unless a separately admitted storage execution policy explicitly requires same-owner return verification.

## Optional Expansion

Allowed expansion:

- read exact listed files;
- read exact listed source authority files;
- inspect exact current blob SHA or runtime state identity;
- run exact listed validation commands/checks;
- perform exact post-write readback;
- report project refresh instruction categories.

Forbidden expansion:

- semantic acceptance review;
- Direction runtime adoption;
- Codex handoff by implication;
- child chat/research by implication;
- broad repository search to discover files to write;
- Project UI update or Project Files/Sources refresh;
- next semantic task execution.

## Research Policy

Research posture: `forbidden` by default.

Storage Update is a mechanical persistence procedure. It should rely on exact internal Workflow v3 authority, admitted storage package contents, exact repository/runtime readback, and listed validation. External/current research is not required to apply exact storage packages.

If external tool/provider behavior is uncertain and affects write safety, STOP with `STORAGE_SURFACE_UNVERIFIED` rather than researching during storage execution.

## Utility Decision Gate

This procedure is itself a `storage`.

Utility use rules:

- Direct in-chat storage mutation is allowed only because START selected `storage_update`.
- The storage write gate must pass before any write.
- No additional material utility is available by default.
- Validation tools may be used only when they are listed in the package and needed to verify the write.
- Project refresh instructions may be reported but not executed.

Utility use must not become procedure switching, hidden mutation outside allowed paths, hidden acceptance, or hidden next work.

## Utility / Adapter Policy

```text
common_utility_choices:
  - direct repository/runtime file readback for listed files
  - direct repository/runtime write primitive for listed changes
  - listed validation command/check execution
  - project_refresh_instruction_packet for reporting only

forbidden_utility_categories:
  - codex_handoff_packet by implication
  - codex_return_verification by implication
  - child_chat_packet by implication
  - child_research_packet by implication
  - check_job_packet unless separately admitted before storage and not used to decide acceptance
  - project refresh execution

utility_call_policy:
  - not used by default
  - missing direct write capability produces STOP unless a complete admitted Transfer Packet is already present

external_return_policy:
  - not used by default
  - returned external evidence is not accepted state unless separately verified and accepted by the appropriate boundary

external_return_verification:
  - verify branch/commit/diff/changed files/EOF/validation only when a separately admitted same-owner external storage policy exists

embedded_verification_policy:
  - post-write verification is mandatory before FINISH is requested

storage_boundary:
  - write only exact listed paths
  - apply only exact listed changes
  - never decide acceptance
  - never continue to semantic next step
```

## Utility Call and Resume Policy

This procedure should normally execute directly or stop.

It must not emit `UTILITY_CALL` merely because another tool such as Codex could perform the write. If storage cannot execute directly, return a blocked result or a complete closure Transfer Packet only when the selected context requires it.

If a separately admitted future storage policy allows same-owner external storage execution, the handoff must include:

```text
external_surface:
copy_paste_packet_required: complete storage update package
expected_return_packet:
  - changed_files
  - forbidden_paths_touched
  - pre_write_refs
  - post_write_refs
  - diff_summary
  - eof_check_results
  - validation_output
  - commit_sha
  - push_status
  - residual_risks
validation_required_on_return:
  - match handoff id
  - verify only listed paths changed
  - verify EOF
  - verify listed validation
resume_rule: resume the same selected main procedure
```

FINISH must not be requested while a required utility return is pending.

## Project Refresh Reporting

For this Phase 1 system blocker procedure persistence batch, report refresh requirements as:

```yaml
project_instruction_ui_update_required: false
project_sources_files_refresh_required: false
request_only_sources_refresh_required: true
do_not_upload_as_project_file: true
```

Do not update ChatGPT Project Instructions UI or Project Files/Sources from this procedure. Report refresh requirements only.

## Checkpoint Policy

No checkpoint is required for a complete, admitted, exact Storage Update Package.

Checkpoint before write only when:

- the package explicitly requires pre-write confirmation;
- current human input provides exact authority but it has not been bound into the package;
- a safe no-op result should be confirmed before closure and the package demands confirmation.

Do not use checkpoints to repair vague packages after write starts. Missing authority, missing paths, missing validation, or ambiguous scope must STOP.

## Completion Contract

```text
completion:
  result: storage update result with applied, no-op, blocked, or failed status and exact changed/no-op evidence
  proof: authority, exact paths, pre/post refs, diff or no-op evidence, validation, EOF checks, refresh categories, and residual risks are recorded
  blocked_if: storage package is missing or incomplete, authority is absent, paths are broad or unlisted, source state mismatches, validation is absent, forbidden paths are touched, or requested action would update actual Project UI
```
## Output Contract

```yaml
storage_update_result:
  status: applied | no_op | blocked | failed
  package_id:
  authority_ref:
  repository_target:
  changed_files:
    - path:
      operation:
      pre_write_ref:
      post_write_ref:
      change_id:
  unchanged_files:
    - path:
      reason:
  created_files:
    - path:
      post_write_ref:
  deleted_files:
    - path:
      pre_write_ref:
  forbidden_paths_touched: []
  unexpected_changes: []
  diff_summary:
  eof_check_results:
    - path:
      required_marker:
      status:
  validation_output:
    - check_id:
      command_or_manual_check:
      status:
      output_or_evidence:
  commit_status:
    commit_sha:
    push_status:
    branch_or_ref:
  project_refresh_requirements:
    project_instruction_ui_update_required:
    project_sources_files_refresh_required:
    request_only_sources_refresh_required:
    do_not_upload_as_project_file:
  source_read_limitations:
  residual_risks:
  CLOSURE_CHECK:
  FINISH_PACKET_after_explicit_FINISH:
  FINISH_PACKET_result_after_explicit_FINISH:
  NEXT_CHAT_CARD_or_no_next_chat_needed_after_explicit_FINISH:
```

Output rules:

- return changed files and validation even on partial failure when available;
- report no-op explicitly when final content already matches the package;
- report project refresh categories separately;
- do not choose the next semantic task;
- return evidence usable by parent, Acceptance Decision, Current Next Move, or verification surfaces.

## Eval / Quality Checks

Procedure Definition checks:

- Purpose is specific and bounded.
- Trigger and non-trigger are distinguishable.
- Required inputs and Storage Update Package schema are explicit.
- Source requirements and context classification are explicit.
- Complexity selector exists.
- Stage Cards produce intermediate outputs and real gates.
- Stop conditions prevent invention, hidden mutation, hidden acceptance, and boundary crossing.
- Utility/storage policy is explicit.
- External handoff/resume policy is explicit.
- Closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed continuation.
- Canonical path and `*_PROCEDURE.md` naming are preserved.
- Procedure class matches registry metadata.

Procedure Execution checks:

- START selected exactly one main procedure.
- RUN did not switch procedures.
- Direct mutation occurred only under `storage_update`.
- No write occurred before package, authority, path, source, and validation gates passed.
- Only listed files changed.
- Forbidden paths were untouched.
- EOF markers were verified where required.
- Listed validation ran or produced a typed stop.
- FINISH was requested only after all required write/verification evidence resolved.
- NEXT_CHAT_CARD continuation selected exactly one closure move and did not launch it.

Cross-boundary checks:

- Acceptance Decision may produce storage update need or a candidate Storage Update Package, but Storage Update independently verifies authority and package completeness.
- Acceptance alone is not write execution.
- Current Next Move may route to storage_update only when its transfer packet contains a complete Storage Update Package.
- Placeholders in transfer packets are invalid.
- Storage Update returns evidence to parent/next surfaces without deciding the next semantic task.

## Stop Conditions

Stop before write when:

- Storage Update Package is missing;
- package is incomplete;
- package uses placeholders;
- authority is absent or ambiguous;
- acceptance evidence is present but update authorization is absent;
- allowed files are broad, globbed, wildcarded, directory-level, or missing;
- a change touches an unlisted path;
- a change touches a forbidden path;
- current state does not match expected SHA/existence/EOF;
- required source is unreadable or conflicting;
- exact final content or exact patch is missing;
- validation is absent;
- package requires Project Files/Sources cache or chat memory as accepted state;
- requested write would create Direction state without admitted setup/adoption authority;
- requested action would update actual ChatGPT Project UI;
- requested action would continue into a semantic next step.

Stop after write or during verification when:

- write tool reports failure;
- unexpected path changed;
- expected diff is absent;
- EOF marker is invalid or missing;
- listed validation fails;
- post-write readback cannot prove required evidence;
- commit/push status required by package is missing.

Block/no-op outcomes:

- `blocked`: no write attempted because pre-write gate failed.
- `no_op`: target already matched exact final content and validation/EOF checks passed or were package-permitted.
- `failed`: write attempted but post-write verification or validation failed.
- `applied`: write, verification, and validation passed.

## Procedure Closure

RUN completion requests FINISH only after:

- no required utility return is pending;
- write was applied, blocked, failed, or confirmed no-op;
- changed files or no-op evidence are listed;
- validation output or validation blocker is listed;
- EOF check results are listed;
- project refresh categories are reported separately;
- source limitations and residual risks are stated.

After explicit FINISH or ФИНИШ, close with:

- CLOSURE_CHECK;
- FINISH_PACKET;
- NEXT_CHAT_CARD or no_next_chat_needed.

NEXT_CHAT_CARD continuation must not launch the next semantic step. It may return storage evidence to the parent, acceptance, current-next-move, verification, or human review boundary.

After FINISH, the same chat is closed for material work.

## Examples

Good use:

```text
START selected persist_accepted_state.
Package lists:
- authority_ref: acceptance_decision_2026_...
- allowed_files: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
- forbidden_paths: workflow_v3/runtime/
- exact final content
- EOF marker
- validation checks
Storage Update verifies package, writes only that file, verifies EOF and validation, then returns changed file evidence.
```

Bad use:

```text
User says: "Looks accepted, save the previous procedure changes."
Missing exact package, exact paths, validation, and update authority.
Result: STOP with STORAGE_UPDATE_PACKAGE_MISSING_OR_INCOMPLETE.
```

Bad use:

```text
Acceptance Decision says candidate is accepted, but no storage package is provided.
Result: STOP with WRITE_NOT_ADMITTED or package-needed return.
```

Bad use:

```text
Current Next Move says storage_update but NEXT_CHAT_CARD.context_to_paste says "use previous approved package".
Result: STOP because placeholders are invalid.
```

END_OF_FILE: workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md
