# Procedure: Code Repository Dependency

status: active_procedure

## Procedure Kind

```text
kind: dependency_schema
dependency_schema_policy: code_repository_dependency_schema
routing_dependency_policy: callable_code_repository_dependency
```

## Purpose

Use this procedure to define the `code_repository_dependency` packet schema for bounded repository maintenance or implementation work delegated to a Code Assistant Development Runtime inside a parent RUN.

This procedure is not a standalone terminal lifecycle whose only artifact is a package. It defines the required fields, boundaries, and return obligation for a `DEPENDENCY_CALL`. It does not launch a code assistant invisibly, authorize acceptance, mutate state, close the parent lifecycle, or broaden product execution by implication.

## Code Repository Dependency Mode

When embedded inside another selected main procedure, this file supplies the Code Assistant Development Runtime dependency schema and quality checks. Embedded use does not change `selected_entrypoint` or `selected_procedure_path` and does not start a new lifecycle.

Embedded use emits `DEPENDENCY_CALL` with `dependency_type: code_repository_dependency`, not FINISH closure artifacts. The parent RUN enters `RUN_WAITING_FOR_DEPENDENCY_RETURN` and remains unresolved until the matching `DEPENDENCY_RETURN` is received and verified. Prior packet labels are unsupported.

If the user asks only for a code repository dependency packet without an active parent/core procedure goal, require an admitted parent/core procedure goal or return `UNREGISTERED_ACTION_EXCEPTION` / blocked scope. Do not create a lifecycle whose only artifact is a package.

For required current-goal repair, a complete code repository dependency packet emitted by the parent opens a code repository dependency. It is not a draft-only artifact, optional launch instruction, standalone material chat, terminal result, or escape hatch from parent verification. If a parent only wants a documentation example and no current repair is required, label it non-material documentation/example content and do not represent it as RUN repair output.

If this packet is pasted into ChatGPT parent for execution, ChatGPT must not execute it. ChatGPT must return `wrong_execution_surface` and instruct the operator to run the packet in the Code Assistant Development Runtime. ChatGPT parent may draft the packet and verify returned evidence only.

## Trigger / When to Use

- A selected parent RUN needs bounded repository maintenance or implementation work from a Code Assistant Development Runtime.
- The work has a known repository, target integration ref, expected base commit evidence, goal, source-read boundary, allowed paths, forbidden paths, validation, and return fields.
- A code repository dependency is appropriate and the parent has a verification contract for the return.

## When Not to Use

- Do not use to execute product work by implication.
- Do not use to mutate repository or runtime state directly.
- Do not use to decide acceptance or permit the code assistant to decide acceptance.
- Do not use when forbidden paths, validation, stop conditions, or return fields are missing.
- Do not use to launch the Code Assistant Development Runtime without an explicit bounded dependency call and return-verification contract.
- Do not use when the only proposed outcome would be a standalone packet instead of an opened dependency call or clearly non-material documentation example.
- Do not use as a replacement for a parent/core procedure START goal.
- Do not ask the code assistant to perform ChatGPT CHECK, FINISH, or CLOSED.

## Required Inputs

- repository;
- repository_role;
- target_integration_ref;
- expected_base_commit_sha;
- workspace_policy_id;
- workspace_binding_required;
- integration_policy_id;
- integration_required;
- allowed_publication_outcomes;
- runtime_selects_internal_ref_mechanics;
- local_path_is_not_canonical_authority;
- purpose;
- goal;
- source_files_to_read;
- allowed_paths;
- forbidden_paths;
- required_changes;
- validation;
- stop_conditions;
- project_refresh_requirements;
- expected_return_contract;
- parent_verification_contract;
- resume_rule;
- requested_return_fields.

## Source Requirements

The dependency schema must identify exact source reads, path boundaries, target integration evidence requirements, and the acceptance boundary. Source reads should use exact repository paths and refs, with resolved commit SHA where integration refs such as `main` are material. EOF/source integrity requirements must be named for files that require them.

The ChatGPT parent sends intent, source authority, path boundaries, validation, target integration evidence requirements, and acceptance boundary. The Code Assistant Development Runtime owns internal workspace/ref/branch/commit/rebase/merge/push mechanics. Branch, ref, and local workspace details may appear only as return evidence, including `internal_work_ref` and `internal_branch_if_any`.

Project Files/Sources, chat memory, snippets, and pasted excerpts are cache/context unless verified against exact repository source.

## Context Classification

Classify inputs as canonical repository source, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

Do not treat code assistant output, dependency-call text, validation output, or FINISH_PACKET results as accepted state.

## Complexity Selector

- `standard`: default for a complete bounded dependency call schema.
- `checkpointed`: use when path boundaries, validation, integration evidence requirements, workspace binding, or return fields are ambiguous.
- `delegated_or_tool_mediated`: applies because the output is a code repository dependency call to a Code Assistant Development Runtime; this file creates the schema only and does not launch the runtime by itself.
- `research_backed`: not used by default.

## Stage Cards

```text
stage_id: dependency_call_fit
purpose: Confirm the requested repository/code work is bounded and belongs to a Code Assistant Development Runtime.
activation conditions: Always.
inputs: User request, target repository, purpose, goal, known boundaries.
required intermediate output: Fit decision and dependency scope statement.
gate: PASS if the target is bounded repository maintenance or implementation; STOP if scope is product execution by implication, mutation authority is unclear, or target is unbounded.
checkpoint rule: Checkpoint if user must decide whether code repository dependency execution is actually authorized after the dependency-call draft.
expansion rule: Request missing scope only; do not broaden the target.
stop behavior: Return blocked dependency-call scope result.
```

```text
stage_id: source_and_path_frame
purpose: Identify source files to read, allowed paths, forbidden paths, and source integrity requirements.
activation conditions: dependency_call_fit passes.
inputs: Source files, allowed paths, forbidden paths, repository/base ref.
required intermediate output: Source-read list, path boundary list, source integrity requirements.
gate: PASS if required sources and path boundaries are explicit; STOP if required sources or path boundaries are missing.
checkpoint rule: Checkpoint when allowed/forbidden paths are ambiguous.
expansion rule: Inspect exact repository source when needed to frame boundaries.
stop behavior: Return source/path boundary blocker.
```

```text
stage_id: validation_and_return_contract
purpose: Define validation checks, stop conditions, integration evidence requirements, project refresh reporting, and requested return fields.
activation conditions: source_and_path_frame passes.
inputs: Required changes, validation needs, stop conditions, workspace policy, integration policy, Project refresh categories, return fields.
required intermediate output: Validation and return contract.
gate: PASS if validation and requested return fields are complete; STOP if validation or return fields are missing.
checkpoint rule: Checkpoint when workspace binding, integration evidence, or validation responsibility is ambiguous.
expansion rule: Add bounded validation requirements only within the dependency-call scope.
stop behavior: Return validation/return-contract blocker.
```

```text
stage_id: dependency_call_schema
purpose: Produce the final self-contained Code Assistant Development Runtime dependency call schema.
activation conditions: all prior gates pass.
inputs: Stage outputs.
required intermediate output: Complete Code Assistant Development Runtime dependency schema with expected return and parent verification contract.
gate: PASS only if all required dependency fields are present and the return obligation is explicit.
checkpoint rule: None by default.
expansion rule: None.
stop behavior: Return incomplete dependency-call blocker.
```

## Gate Outcomes

- `PASS`: required dependency scope, sources, paths, validation, stop conditions, and return fields are present.
- `PASS_WITH_RISK`: schema is usable but limitations are explicit and bounded.
- `REWORK`: revise missing or vague dependency-call fields before closure.
- `EXPAND`: inspect exact repository source only to complete source/path boundaries.
- `STOP`: return blocked result when required dependency authority or fields are missing.
- `TRANSFER`: return only clearly non-material documentation/example content, or post-closed continuation content, when no current-goal repair is required and the selected parent admits that output.
- `DEPENDENCY_CALL`: when embedded in a main procedure and the code repository dependency result is required before that owner can complete RUN, return the complete dependency envelope and expected return packet.

## Optional Expansion

Allowed expansion is limited to exact repository source inspection needed for source/path boundaries or validation framing. Expansion must not become product execution, mutation, acceptance, or procedure switching.

## Research Policy

External research is forbidden by default. Exact repository source inspection is allowed or required when needed for source/path boundaries. Do not use research to infer acceptance, Direction runtime state, or Project UI state.

## Checkpoint Policy

No checkpoint is required by default for a complete bounded dependency-call schema. Checkpoint when the user must decide path boundaries, integration evidence requirements, validation scope, return fields, or whether code repository dependency execution is authorized after the dependency-call draft.

## Completion Contract

```text
completion:
  result: Code Assistant Development Runtime repository dependency schema is valid only when embedded under a parent RUN, with open return obligation
  proof: repository, repository role, target integration ref, expected base commit SHA, workspace policy, integration policy, purpose, goal, source reads, allowed/forbidden paths, required changes, validation, stop conditions, refresh requirements, expected return contract, parent verification contract, resume rule, and requested return fields are present
  blocked_if: no admitted parent/core procedure goal exists, work is unbounded, mutation authority is unclear, paths or validation are missing, expected return or parent verification is missing, or the schema would let the code assistant accept its own output or close ChatGPT lifecycle
```
## Output Contract

```text
DEPENDENCY_CALL:
dependency_id:
dependency_type: code_repository_dependency
selected_entrypoint:
selected_procedure_path:
execution_surface: Code Assistant Development Runtime
repository:
repository_role:
target_integration_ref:
expected_base_commit_sha:
workspace_policy_id:
workspace_binding_required:
integration_policy_id:
integration_required:
allowed_publication_outcomes:
runtime_selects_internal_ref_mechanics: true
local_path_is_not_canonical_authority: true
purpose:
goal:
source_files_to_read:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_conditions:
project_refresh_requirements:
expected_return_contract:
  target_integration_ref:
  expected_base_commit_sha:
  observed_base_commit_sha:
  base_matches_expected:
  workspace_binding_used:
  internal_work_ref:
  internal_branch_if_any:
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
  project_refresh_requirements:
  residual_risks:
parent_verification_contract:
resume_rule:
requested_return_fields:
unresolved_until_returned: true
```

## Eval / Quality Checks

- Dependency schema identifies exact source reads and path boundaries.
- Dependency schema includes validation and stop conditions.
- Dependency schema states workspace binding and integration evidence requirements.
- Dependency schema states Project refresh reporting requirements when changed files affect ChatGPT Projects.
- Dependency schema includes expected return and parent verification fields sufficient for later verification.
- Dependency schema does not authorize product execution by implication.
- Dependency schema does not omit forbidden paths or validation.
- Dependency schema does not permit the code assistant to decide acceptance.
- Dependency schema does not instruct the code assistant to perform ChatGPT CHECK, FINISH, or CLOSED.
- Branch, ref, and local workspace details appear only as return evidence.
- Emitting the schema is not parent lifecycle completion; parent RUN waits for return verification when code repository dependency work is required.
- ChatGPT parent wrong-surface execution is blocked with `wrong_execution_surface`.

## Stop Conditions

- requested code repository work is unbounded;
- mutation authority is unclear;
- product execution is implied but not bounded;
- source files to read are missing;
- allowed or forbidden paths are missing;
- validation is missing;
- stop conditions are missing;
- workspace policy or integration evidence requirements are missing;
- expected return, parent verification, or requested return fields are missing;
- schema would let the code assistant accept its own output, mutate outside allowed paths, or close ChatGPT lifecycle.

## Procedure Closure

Return the dependency schema only under a parent procedure boundary. When required for the current START goal, emitting the complete schema opens `DEPENDENCY_CALL` and the parent waits for `DEPENDENCY_RETURN`. The Code Assistant Development Runtime returns evidence only, and that result remains dependency evidence until matched, verified by the parent, and routed through the selected parent completion contract.

If code repository dependency work is required for the current START goal, the parent cannot CHECK, FINISH, or CLOSED until the matching `DEPENDENCY_RETURN` is verified. NEXT_CHAT_CARD is post-closed continuation only and must not carry unfinished code repository dependency work from the current START goal.

END_OF_FILE: workflow_v3/procedures/CODE_REPOSITORY_DEPENDENCY_PROCEDURE.md
