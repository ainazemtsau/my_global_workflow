# Codex Handoff Procedure

status: active_procedure

## Procedure Kind

```text
kind: utility
utility_policy: compatibility_alias_for_child_adapter
child_call_policy: callable_child_adapter
```

## Purpose

Use `codex_handoff` as the child procedure call schema for bounded Codex repository maintenance or implementation work inside a parent RUN.

This file may remain at the same path for registry/path stability, but it is not a standalone terminal lifecycle whose only artifact is a package. It defines the required fields, boundaries, and return obligation for a `CHILD_PROCEDURE_CALL` to Codex. It does not launch Codex invisibly, authorize acceptance, mutate state, close the parent lifecycle, or broaden product execution by implication.

## Child Adapter Mode

When embedded inside another selected main procedure, this file supplies the Codex child-call schema and quality checks. Embedded use does not change `selected_entrypoint` or `selected_procedure_path` and does not start a new lifecycle.

Embedded use emits `CHILD_PROCEDURE_CALL`, not FINISH closure artifacts. The parent RUN enters `RUN_WAITING_FOR_CHILD_RETURN` and remains unresolved until the matching `CHILD_PROCEDURE_RETURN` is received and verified.

If the user asks only for a Codex card without an active parent/core procedure goal, require an admitted parent/core procedure goal or return `UNREGISTERED_ACTION_EXCEPTION` / blocked scope. Do not create a lifecycle whose only artifact is a package.

For required current-goal repair, a complete Codex packet emitted by the parent opens a child call. It is not a draft-only artifact, optional launch instruction, standalone material chat, terminal result, or escape hatch from parent verification. If a parent only wants a documentation example and no current repair is required, label it non-material documentation/example content and do not represent it as RUN repair output.

## Trigger / When to Use

- A selected parent RUN needs bounded repository maintenance or implementation work from Codex.
- The work has a known repository, base ref, goal, source-read boundary, allowed paths, forbidden paths, validation, and return fields.
- A Codex child procedure call is appropriate and the parent has a verification contract for the return.

## When Not to Use

- Do not use to execute product work by implication.
- Do not use to mutate repository or runtime state directly.
- Do not use to decide acceptance or permit Codex to decide acceptance.
- Do not use when forbidden paths, validation, stop conditions, or return fields are missing.
- Do not use to launch Codex without an explicit bounded child call and return-verification contract.
- Do not use when the only proposed outcome would be a standalone packet instead of an opened child call or clearly non-material documentation example.
- Do not use as a replacement for a parent/core procedure START goal.
- Do not ask Codex to perform ChatGPT CHECK, FINISH, or CLOSED.

## Required Inputs

- repository;
- base_ref;
- target_branch_or_branch_policy;
- purpose;
- goal;
- source_files_to_read;
- allowed_paths;
- forbidden_paths;
- required_changes;
- validation;
- stop_conditions;
- commit_push_instructions;
- project_refresh_requirements;
- expected_return_contract;
- parent_verification_contract;
- resume_rule;
- requested_return_fields.

## Source Requirements

The child-call schema must identify exact source reads and path boundaries. Source reads should use exact repository paths and refs, with resolved commit SHA where branch refs such as `main` are material. EOF/source integrity requirements must be named for files that require them.

Project Files/Sources, chat memory, snippets, and pasted excerpts are cache/context unless verified against exact repository source.

## Context Classification

Classify inputs as canonical repository source, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

Do not treat Codex output, child-call text, validation output, or FINISH_PACKET results as accepted state.

## Complexity Selector

- `standard`: default for a complete bounded child call schema.
- `checkpointed`: use when path boundaries, validation, branch policy, commit/push policy, or return fields are ambiguous.
- `delegated_or_tool_mediated`: applies because the output is a child procedure call to Codex; this file creates the schema only and does not launch Codex by itself.
- `research_backed`: not used by default.

## Stage Cards

```text
stage_id: child_call_fit
purpose: Confirm the requested Codex work is bounded and belongs to Codex.
activation conditions: Always.
inputs: User request, target repository, purpose, goal, known boundaries.
required intermediate output: Fit decision and child-call scope statement.
gate: PASS if the target is bounded repository maintenance or implementation; STOP if scope is product execution by implication, mutation authority is unclear, or target is unbounded.
checkpoint rule: Checkpoint if user must decide whether Codex is actually authorized after the child-call draft.
expansion rule: Request missing scope only; do not broaden the target.
stop behavior: Return blocked child-call scope result.
```

```text
stage_id: source_and_path_frame
purpose: Identify source files to read, allowed paths, forbidden paths, and source integrity requirements.
activation conditions: child_call_fit passes.
inputs: Source files, allowed paths, forbidden paths, repository/base ref.
required intermediate output: Source-read list, path boundary list, source integrity requirements.
gate: PASS if required sources and path boundaries are explicit; STOP if required sources or path boundaries are missing.
checkpoint rule: Checkpoint when allowed/forbidden paths are ambiguous.
expansion rule: Inspect exact repository source when needed to frame boundaries.
stop behavior: Return source/path boundary blocker.
```

```text
stage_id: validation_and_return_contract
purpose: Define validation checks, stop conditions, commit/push instructions, project refresh reporting, and requested return fields.
activation conditions: source_and_path_frame passes.
inputs: Required changes, validation needs, stop conditions, commit/push policy, Project refresh categories, return fields.
required intermediate output: Validation and return contract.
gate: PASS if validation and requested return fields are complete; STOP if validation or return fields are missing.
checkpoint rule: Checkpoint when commit/push policy or validation responsibility is ambiguous.
expansion rule: Add bounded validation requirements only within the child-call scope.
stop behavior: Return validation/return-contract blocker.
```

```text
stage_id: child_call_schema
purpose: Produce the final self-contained Codex child procedure call schema.
activation conditions: all prior gates pass.
inputs: Stage outputs.
required intermediate output: Complete Codex child-call schema with expected return and parent verification contract.
gate: PASS only if all required child-call fields are present and the return obligation is explicit.
checkpoint rule: None by default.
expansion rule: None.
stop behavior: Return incomplete child-call blocker.
```

## Gate Outcomes

- `PASS`: required child-call scope, sources, paths, validation, stop conditions, and return fields are present.
- `PASS_WITH_RISK`: schema is usable but limitations are explicit and bounded.
- `REWORK`: revise missing or vague child-call fields before closure.
- `EXPAND`: inspect exact repository source only to complete source/path boundaries.
- `STOP`: return blocked result when required child-call authority or fields are missing.
- `TRANSFER`: return only clearly non-material documentation/example content, or post-closed continuation content, when no current-goal repair is required and the selected parent admits that output.
- `CHILD_PROCEDURE_CALL`: when embedded in a main procedure and the Codex result is required before that owner can complete RUN, return the complete child-call envelope and expected return packet.

## Optional Expansion

Allowed expansion is limited to exact repository source inspection needed for source/path boundaries or validation framing. Expansion must not become product execution, mutation, acceptance, or procedure switching.

## Research Policy

External research is forbidden by default. Exact repository source inspection is allowed or required when needed for source/path boundaries. Do not use research to infer acceptance, Direction runtime state, or Project UI state.

## Checkpoint Policy

No checkpoint is required by default for a complete bounded child-call schema. Checkpoint when the user must decide path boundaries, commit/push policy, validation scope, return fields, or whether Codex is authorized after the child-call draft.

## Completion Contract

```text
completion:
  result: Codex child-call schema is valid only when embedded under a parent RUN, with open return obligation
  proof: repository, base ref, target branch or branch policy, purpose, goal, source reads, allowed/forbidden paths, required changes, validation, stop conditions, commit/push policy, refresh requirements, expected return contract, parent verification contract, resume rule, and requested return fields are present
  blocked_if: no admitted parent/core procedure goal exists, work is unbounded, mutation authority is unclear, paths or validation are missing, expected return or parent verification is missing, or the schema would let Codex accept its own output or close ChatGPT lifecycle
```
## Output Contract

```text
CHILD_PROCEDURE_CALL:
child_call_id:
selected_entrypoint:
selected_procedure_path:
child_category: codex_repository_work
external_surface: Codex
repository:
base_ref:
target_branch_or_branch_policy:
purpose:
goal:
source_files_to_read:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_conditions:
commit_push_instructions:
project_refresh_requirements:
expected_return_contract:
parent_verification_contract:
resume_rule:
requested_return_fields:
unresolved_until_returned: true
```

## Eval / Quality Checks

- Child-call schema identifies exact source reads and path boundaries.
- Child-call schema includes validation and stop conditions.
- Child-call schema states commit/push policy.
- Child-call schema states Project refresh reporting requirements when changed files affect ChatGPT Projects.
- Child-call schema includes expected return and parent verification fields sufficient for later verification.
- Child-call schema does not authorize product execution by implication.
- Child-call schema does not omit forbidden paths or validation.
- Child-call schema does not permit Codex to decide acceptance.
- Child-call schema does not instruct Codex to perform ChatGPT CHECK, FINISH, or CLOSED.
- Emitting the schema is not parent lifecycle completion; parent RUN waits for return verification when Codex work is required.

## Stop Conditions

- requested Codex work is unbounded;
- mutation authority is unclear;
- product execution is implied but not bounded;
- source files to read are missing;
- allowed or forbidden paths are missing;
- validation is missing;
- stop conditions are missing;
- commit/push policy is missing;
- expected return, parent verification, or requested return fields are missing;
- schema would let Codex accept its own output, mutate outside allowed paths, or close ChatGPT lifecycle.

## Procedure Closure

Return the child-call schema only under a parent procedure boundary. When required for the current START goal, emitting the complete schema opens `CHILD_PROCEDURE_CALL` and the parent waits for `CODEX_RETURN_PACKET` / `CHILD_PROCEDURE_RETURN`. Codex returns evidence only, and that result remains child evidence until matched, verified by the parent, and routed through the selected parent completion contract.

If Codex work is required for the current START goal, the parent cannot CHECK, FINISH, or CLOSED until the matching `CHILD_PROCEDURE_RETURN` is verified. NEXT_CHAT_CARD is post-closed continuation only and must not carry unfinished Codex child work from the current START goal.

END_OF_FILE: workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md
