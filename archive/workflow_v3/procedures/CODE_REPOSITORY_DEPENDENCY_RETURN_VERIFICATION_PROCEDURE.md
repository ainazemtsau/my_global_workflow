# Procedure: Code Repository Dependency Return Verification

status: active_procedure

## Procedure Kind

```text
kind: verification
dependency_schema_policy: callable_verification
```

## Purpose

Use `verify_code_repository_dependency_return` to verify a Code Assistant Development Runtime `DEPENDENCY_RETURN` for a `code_repository_dependency` before a parent RUN relies on it for CHECK, FINISH, acceptance, or storage update decisions.

Verification is dependency-return verification when embedded. It is candidate evidence, not acceptance by itself. This procedure does not close the parent lifecycle, repair runtime state, launch follow-up work, or treat a code assistant commit as accepted state.

## Embedded Verification Mode

If the current main procedure emitted the code repository dependency and the user returns the Code Assistant Development Runtime result in the same active RUN, use this verification procedure as schema/checklist only.

Do not select `verify_code_repository_dependency_return` as a new `selected_procedure_path` during embedded use.

Embedded verification must verify target integration ref, expected base commit SHA, observed base commit SHA, base match, workspace binding, internal work ref, internal branch if any, changed files, allowed paths, forbidden paths, unlisted paths, validation output, EOF markers, Project refresh categories, result commit, integration requirement, integration status, final target commit, target containment proof, remote verification, push status, residual risks, and match to the emitted `DEPENDENCY_CALL`.

No validation means no done claim.

Verification does not equal acceptance and does not close the parent lifecycle by itself. It may unblock parent RUN only after target integration evidence, result commit, changed files, validation, EOF, refresh, integration status, push status, residual risk evidence, and the matching open dependency id are verified or the result is explicitly blocked. If required code repository repair was detected but no parent `DEPENDENCY_CALL` was opened, verification must block because there is no same-owner call to match. Prior packet labels are unsupported.

Standalone verification remains valid when the user's primary work item is only code assistant result verification.

## Trigger / When to Use

- A code repository dependency run returns target integration evidence, internal work evidence, result commit, diff, changed files, validation output, push status, or residual risk evidence.
- The user asks whether a code assistant result satisfies its dependency boundaries.
- Parent RUN, acceptance, storage, or repair decisions need verified code repository dependency evidence first.

## When Not to Use

- Do not use to accept the code assistant result.
- Do not use to mutate repository/runtime state.
- Do not use to repair the result unless a separate procedure is admitted.
- Do not use when required return evidence, result commit/diff, changed files, integration status, or validation evidence is absent; request missing evidence instead.
- Do not use to close the parent lifecycle, perform ChatGPT FINISH, or convert a handoff/card/package into completion.

## Required Inputs

- Code Assistant Development Runtime return fields;
- original dependency call or allowed/forbidden path boundary;
- matching_dependency_id or exact emitted dependency call packet when embedded;
- target_integration_ref;
- expected_base_commit_sha;
- observed_base_commit_sha;
- base_matches_expected;
- workspace_binding_used;
- internal_work_ref;
- internal_branch_if_any;
- changed_files;
- allowed_paths;
- forbidden_paths;
- forbidden_paths_touched;
- unlisted_paths_touched;
- validation_output;
- result_commit_sha;
- integration_required;
- integration_status;
- final_target_commit_sha;
- target_contains_result_commit;
- target_remote_verification;
- push_status;
- pending_integration_reason;
- exact_next_action_if_not_integrated;
- EOF marker evidence where Markdown files require it;
- payload character counts when Project Instructions sources changed;
- project refresh categories;
- residual risks.

## Source Requirements

Inspect exact repo, target integration ref, result commit, diff, and changed-file evidence where available. Verify EOF markers for modified Markdown files that require them. Project Instructions source changes require measured payload character count and refresh classification.

Project Files/Sources, chat memory, summaries, and unverified snippets are not evidence.

## Context Classification

Classify code assistant return content as dependency evidence. Classify repository files/diffs as canonical repository source only when exact target ref, commit, and path evidence is inspected. Treat FINISH_PACKET results and validation text as candidate evidence until verified.

## Complexity Selector

- `standard`: default for normal code repository dependency result verification.
- `checkpointed`: use when verification evidence is incomplete and the user must request missing evidence.
- `delegated_or_tool_mediated`: not used by default; verification reviews returned evidence and does not launch repair unless separately admitted.
- `research_backed`: not used.

## Stage Cards

```text
stage_id: dependency_return_intake
purpose: Verify that target integration evidence, result commit, pushed status, changed files, and return fields are present.
activation conditions: Always.
inputs: Code Assistant Development Runtime return, original dependency call if available.
required intermediate output: Intake evidence list and missing fields.
gate: PASS if required return evidence, result commit/diff, and changed-file evidence are present; STOP if required evidence is missing.
checkpoint rule: Request missing evidence when incomplete instead of guessing.
expansion rule: Inspect exact target ref and commit metadata if available.
stop behavior: Return blocked verification result naming missing evidence.
```

```text
stage_id: scope_and_path_verification
purpose: Compare changed files against allowed and forbidden paths.
activation conditions: dependency_return_intake passes.
inputs: changed_files, allowed_paths, forbidden_paths, diff/stat evidence.
required intermediate output: Path compliance finding and forbidden path list.
gate: PASS if changed files are within allowed paths and no forbidden paths were touched; STOP if forbidden paths were touched or allowed paths are unclear.
checkpoint rule: Checkpoint if original path boundary is missing.
expansion rule: Inspect exact diff only within returned result commit or internal work ref.
stop behavior: Return failed or blocked verification result.
```

```text
stage_id: validation_and_integrity_verification
purpose: Check validation output, EOF markers, payload counts when required, and project refresh categories.
activation conditions: scope_and_path_verification passes.
inputs: validation output, modified Markdown files, Project Instructions source changes, refresh fields.
required intermediate output: Validation, EOF, payload, and refresh findings.
gate: PASS if validation and integrity evidence are sufficient; STOP if validation is missing/failed without clear limitation, EOF fails, or payload count is missing when required.
checkpoint rule: Request missing validation, EOF, or payload evidence instead of guessing.
expansion rule: Inspect exact files/diff where needed for EOF or payload verification.
stop behavior: Return failed or blocked verification result.
```

```text
stage_id: integration_verification
purpose: Verify integration requirement, target status, final target commit, target containment proof, remote verification, and push status.
activation conditions: validation_and_integrity_verification passes.
inputs: integration_required, integration_status, final_target_commit_sha, target_contains_result_commit, target_remote_verification, push_status, pending_integration_reason, exact_next_action_if_not_integrated.
required intermediate output: Integration finding and missing or failed integration evidence.
gate: PASS only when integration_required is present and either the result is explicitly blocked or required integration is proven; STOP when integration_required is missing, integration_status is missing, required integration is not complete, final target commit is missing, or target containment is not proven.
checkpoint rule: Request missing integration evidence instead of guessing.
expansion rule: Inspect exact target ref and remote evidence when available.
stop behavior: Return failed or blocked verification result.
```

```text
stage_id: verification_result
purpose: Return verification status, residual risks, and exact next move.
activation conditions: Prior stages pass or stop with findings.
inputs: Stage outputs.
required intermediate output: Verification output contract.
gate: PASS only if verification evidence supports the status.
checkpoint rule: None by default.
expansion rule: None.
stop behavior: Return blocked status and exact missing evidence.
```

## Gate Outcomes

- `PASS`: evidence supports the verification status.
- `PASS_WITH_RISK`: verification can pass with explicit bounded residual risk.
- `REWORK`: same-scope repair is needed before acceptance/storage reliance.
- `EXPAND`: inspect exact repo, target ref, commit, and diff evidence within the returned scope.
- `STOP`: block when required evidence is missing, forbidden paths are touched, validation is absent/failed, EOF fails, or payload counts are missing when required.
- `TRANSFER`: return a candidate next move or Transfer Packet for acceptance, storage, or repair; do not launch it.

## Hard Blockers

- missing validation -> no done;
- validation failed -> no done;
- missing integration_required -> blocked;
- missing integration_status -> blocked;
- integration_required=true and integration_status is not `integrated_to_target_ref` -> no done;
- final_target_commit_sha missing when integration_required=true -> no done;
- target_contains_result_commit not proven when integration_required=true -> no done;
- forbidden path touched -> no done;
- code assistant claims acceptance, CHECK, FINISH, or CLOSED -> reject boundary violation.

`internal_branch_if_any` is return-only evidence:

```text
internal_branch_if_any:
  return_only: true
```

## Optional Expansion

Allowed expansion is limited to exact repo, target ref, commit, diff, and integration evidence checks needed for verification. Repair, acceptance, storage, or new code repository work require separate admission.

## Research Policy

External research is forbidden. Exact repo, target ref, commit, diff, and integration evidence inspection is allowed or required. Project Files/Sources and chat memory are not evidence.

## Checkpoint Policy

No checkpoint is required by default. Checkpoint or request missing evidence when the dependency return is incomplete instead of guessing.

## Completion Contract

```text
completion:
  result: verification result classifying returned code-assistant dependency evidence as passed, failed, or blocked
  proof: target integration ref, base commit evidence, workspace binding, internal work evidence, result commit identity, changed files, forbidden-path check, validation, EOF markers, payload counts, refresh categories, integration status, final target commit, target containment proof, remote verification, push status, and residual risks are verified or missing evidence is named
  blocked_if: required return evidence is missing, forbidden paths were touched, validation is absent or failed, EOF markers are missing, required integration is missing or unproven, the code assistant claims acceptance/CHECK/FINISH/CLOSED, or verification would imply acceptance/storage/repair by itself
```
## Output Contract

```text
verification_status: passed | failed | blocked
dependency_id:
target_integration_ref:
expected_base_commit_sha:
observed_base_commit_sha:
base_matches_expected:
workspace_binding_used:
internal_work_ref:
internal_branch_if_any:
  return_only: true
changed_files:
forbidden_paths_touched:
unlisted_paths_touched:
validation_output:
result_commit_sha:
integration_required:
integration_status:
final_target_commit_sha:
target_contains_result_commit:
target_remote_verification:
push_status:
pending_integration_reason:
exact_next_action_if_not_integrated:
payload_character_counts:
project_refresh_categories:
project_refresh_requirements:
residual_risks:
exact_next_move:
```

## Eval / Quality Checks

- Target integration ref, base commit evidence, result commit, changed files, integration status, final target commit, target containment proof, remote verification, and push status are verified or missing evidence is named.
- Returned evidence matches the emitted `DEPENDENCY_CALL` when verification is embedded.
- Required code repository repair cannot be verified as complete unless the parent opened `DEPENDENCY_CALL`, waited in `RUN_WAITING_FOR_DEPENDENCY_RETURN`, and received matching `DEPENDENCY_RETURN`.
- Prior packet labels are unsupported and must not be treated as matchable dependency identifiers.
- Changed files are compared against allowed and forbidden paths.
- Validation output is present; no validation means no done claim.
- Integration-required returns cannot be verified as done unless `integration_status: integrated_to_target_ref`, `final_target_commit_sha`, and `target_contains_result_commit` are proven.
- EOF markers are checked for Markdown files that require them.
- Project Instructions source changes include measured payload count and refresh classification.
- Forbidden path changes block acceptance.
- Verification result does not accept state, close parent lifecycle, or launch next work.
- Missing target integration, result commit, changed files, validation, EOF, refresh, integration, or push evidence makes verification blocked, not passed.

## Stop Conditions

- target integration evidence, result commit, diff, or changed-files evidence is missing;
- original allowed/forbidden path boundary is missing or unclear;
- forbidden paths were touched;
- validation output is missing or failed without clear limitation;
- integration_required is missing;
- integration_status is missing;
- integration_required=true and integration_status is not `integrated_to_target_ref`;
- final_target_commit_sha is missing when integration_required=true;
- target_contains_result_commit is not proven when integration_required=true;
- required EOF marker is missing or mismatched;
- Project Instructions source changed but payload count is missing;
- project refresh categories are missing when relevant;
- embedded return cannot be matched to the emitted dependency call;
- required code repository repair has no emitted parent dependency call to match;
- code assistant claims acceptance, CHECK, FINISH, or CLOSED authority;
- verification would imply acceptance, storage mutation, parent FINISH, repair, or hidden next launch.

## Procedure Closure

Verification does not accept state and does not close the parent lifecycle by itself. When embedded, it returns dependency-return verification evidence to the parent RUN. The parent may proceed toward CHECK only after required return evidence is matched and verified, or after the result is explicitly blocked.

If the result needs acceptance, storage, or repair, return the exact next move or Transfer Packet; do not launch it.

NEXT_CHAT_CARD is post-closed continuation only. It is not a dependency call, not a support launch, and not evidence that the current START goal has completed.

END_OF_FILE: workflow_v3/procedures/CODE_REPOSITORY_DEPENDENCY_RETURN_VERIFICATION_PROCEDURE.md
