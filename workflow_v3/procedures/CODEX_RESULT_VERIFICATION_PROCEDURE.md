# Codex Result Verification Procedure

status: active_procedure

## Procedure Kind

```text
kind: verification
utility_policy: callable_verification
```

## Purpose

Use `codex_result_verification` to verify a Codex return before acceptance or storage update reliance.

Verification is candidate evidence, not acceptance by itself. This procedure does not repair runtime state, launch follow-up work, or treat a Codex commit as accepted state.

## Embedded Verification Mode

If the current main procedure emitted the Codex handoff and the user returns the Codex result in the same active RUN, use this verification procedure as schema/checklist only.

Do not select `codex_result_verification` as a new `selected_procedure_path` during embedded use.

Embedded verification must verify branch, commit SHA, changed files, allowed paths, forbidden paths, validation output, EOF markers, Project refresh categories, push status, and residual risks.

No validation means no done claim.

Verification does not equal acceptance.

Standalone verification remains valid when the user's primary work item is only Codex result verification.

## Trigger / When to Use

- A Codex adapter run returns branch, commit, diff, changed files, validation output, push status, or residual risk evidence.
- The user asks whether a Codex result satisfies its handoff boundaries.
- Acceptance, storage, or repair decisions need verified Codex evidence first.

## When Not to Use

- Do not use to accept the Codex result.
- Do not use to mutate repository/runtime state.
- Do not use to repair the result unless a separate procedure is admitted.
- Do not use when branch, commit/diff, changed files, or validation evidence is absent; request missing evidence instead.

## Required Inputs

- Codex return fields;
- original handoff or allowed/forbidden path boundary;
- matching_handoff_id or exact emitted handoff packet when embedded;
- branch;
- commit_sha;
- changed_files;
- allowed_paths;
- forbidden_paths;
- validation_output;
- EOF marker evidence where Markdown files require it;
- payload character counts when Project Instructions sources changed;
- project refresh categories;
- push status;
- residual risks.

## Source Requirements

Inspect exact repo, branch, commit, diff, and changed-file evidence where available. Verify EOF markers for modified Markdown files that require them. Project Instructions source changes require measured payload character count and refresh classification.

Project Files/Sources, chat memory, summaries, and unverified snippets are not evidence.

## Context Classification

Classify Codex return content as adapter evidence. Classify repository files/diffs as canonical repository source only when exact branch/commit/path evidence is inspected. Treat FINISH_PACKET results and validation text as candidate evidence until verified.

## Complexity Selector

- `standard`: default for normal Codex result verification.
- `checkpointed`: use when verification evidence is incomplete and the user must request missing evidence.
- `delegated_or_tool_mediated`: not used by default; verification reviews returned evidence and does not launch repair unless separately admitted.
- `research_backed`: not used.

## Stage Cards

```text
stage_id: codex_return_intake
purpose: Verify that branch, commit SHA, pushed status, changed files, and return fields are present.
activation conditions: Always.
inputs: Codex return, original handoff if available.
required intermediate output: Intake evidence list and missing fields.
gate: PASS if branch/commit/diff/changed-files evidence is present; STOP if required evidence is missing.
checkpoint rule: Request missing evidence when incomplete instead of guessing.
expansion rule: Inspect exact branch/commit metadata if available.
stop behavior: Return blocked verification result naming missing evidence.
```

```text
stage_id: scope_and_path_verification
purpose: Compare changed files against allowed and forbidden paths.
activation conditions: codex_return_intake passes.
inputs: changed_files, allowed_paths, forbidden_paths, diff/stat evidence.
required intermediate output: Path compliance finding and forbidden path list.
gate: PASS if changed files are within allowed paths and no forbidden paths were touched; STOP if forbidden paths were touched or allowed paths are unclear.
checkpoint rule: Checkpoint if original path boundary is missing.
expansion rule: Inspect exact diff only within returned commit/branch.
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
- `EXPAND`: inspect exact repo/branch/commit/diff evidence within the returned scope.
- `STOP`: block when required evidence is missing, forbidden paths are touched, validation is absent/failed, EOF fails, or payload counts are missing when required.
- `TRANSFER`: return a candidate next move or Transfer Packet for acceptance, storage, or repair; do not launch it.

## Optional Expansion

Allowed expansion is limited to exact repo/branch/commit/diff inspection and bounded evidence checks needed for verification. Repair, acceptance, storage, or new Codex work require separate admission.

## Research Policy

External research is forbidden. Exact repo/branch/commit/diff inspection is allowed or required. Project Files/Sources and chat memory are not evidence.

## Checkpoint Policy

No checkpoint is required by default. Checkpoint or request missing evidence when the Codex return is incomplete instead of guessing.

## Completion Contract

```text
completion:
  result: verification result classifying returned code-assistant evidence as passed, failed, or blocked
  proof: branch/ref, commit/artifact identity, changed files, forbidden-path check, validation, EOF markers, payload counts, refresh categories, push status, and residual risks are verified or missing evidence is named
  blocked_if: required return evidence is missing, forbidden paths were touched, validation is absent or failed, EOF markers are missing, or verification would imply acceptance/storage/repair by itself
```
## Output Contract

```text
verification_status: passed | failed | blocked
branch:
commit_sha:
changed_files:
forbidden_paths_touched:
validation_output:
payload_character_counts:
project_refresh_categories:
residual_risks:
exact_next_move:
```

## Eval / Quality Checks

- Branch, commit SHA, changed files, and push status are verified or missing evidence is named.
- Returned evidence matches the emitted handoff when verification is embedded.
- Changed files are compared against allowed and forbidden paths.
- Validation output is present; no validation means no done claim.
- EOF markers are checked for Markdown files that require them.
- Project Instructions source changes include measured payload count and refresh classification.
- Forbidden path changes block acceptance.
- Verification result does not accept state or launch next work.

## Stop Conditions

- branch, commit, diff, or changed-files evidence is missing;
- original allowed/forbidden path boundary is missing or unclear;
- forbidden paths were touched;
- validation output is missing or failed without clear limitation;
- required EOF marker is missing or mismatched;
- Project Instructions source changed but payload count is missing;
- project refresh categories are missing when relevant;
- embedded return cannot be matched to the emitted handoff;
- verification would imply acceptance, storage mutation, repair, or hidden next launch.

## Procedure Closure

Verification does not accept state. If lifecycle FINISH is active, close through CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed continuation.

If the result needs acceptance, storage, or repair, return the exact next move or Transfer Packet; do not launch it.

END_OF_FILE: workflow_v3/procedures/CODEX_RESULT_VERIFICATION_PROCEDURE.md
