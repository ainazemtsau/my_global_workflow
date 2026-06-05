# Codex Handoff Procedure

status: active_procedure

## Procedure Class

```text
procedure_class: utility_adapter
embedded_use_policy: standalone_or_embedded_utility_schema
```

## Purpose

Use `codex_handoff` to create a self-contained Codex package for bounded repository maintenance or implementation.

The procedure produces a candidate handoff package only. It does not launch Codex invisibly, authorize acceptance, mutate state, or broaden product execution by implication.

## Utility Adapter Mode

When selected by START, this procedure prepares a standalone Codex handoff package.

When embedded inside another selected owner procedure, this file supplies handoff schema and quality checks only.

Embedded use does not change `selected_entrypoint` or `selected_procedure_ref` and does not start a new lifecycle.

Embedded use emits RUN_EXTERNAL_HANDOFF, not FINISH_REQUEST.

## Trigger / When to Use

- User asks to package bounded repository maintenance or implementation work for Codex.
- The work has a known repository, base ref, goal, source-read boundary, allowed paths, forbidden paths, validation, and return fields.
- A later Codex adapter run is appropriate, but the current procedure is only preparing the handoff.

## When Not to Use

- Do not use to execute product work by implication.
- Do not use to mutate repository or runtime state directly.
- Do not use to decide acceptance or permit Codex to decide acceptance.
- Do not use when forbidden paths, validation, stop conditions, or return fields are missing.
- Do not use to launch Codex without a separate explicit handoff/adapter action.

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
- requested_return_fields.

## Source Requirements

The package must identify exact source reads and path boundaries. Source reads should use exact repository paths and refs, with resolved commit SHA where branch refs such as `main` are material. EOF/source integrity requirements must be named for files that require them.

Project Files/Sources, chat memory, snippets, and pasted excerpts are cache/context unless verified against exact repository source.

## Context Classification

Classify inputs as canonical repository source, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

Do not treat Codex output, handoff text, validation output, or Result Packets as accepted state.

## Complexity Selector

- `standard`: default for a complete bounded handoff.
- `checkpointed`: use when path boundaries, validation, branch policy, commit/push policy, or return fields are ambiguous.
- `delegated_or_tool_mediated`: applies because the output is a handoff to Codex; this procedure creates the package only and does not launch Codex by itself.
- `research_backed`: not used by default.

## Stage Cards

```text
stage_id: handoff_fit
purpose: Confirm the requested Codex work is bounded and belongs to Codex.
activation conditions: Always.
inputs: User request, target repository, purpose, goal, known boundaries.
required intermediate output: Fit decision and handoff scope statement.
gate: PASS if the target is bounded repository maintenance or implementation; STOP if scope is product execution by implication, mutation authority is unclear, or target is unbounded.
checkpoint rule: Checkpoint if user must decide whether Codex is actually authorized after the package draft.
expansion rule: Request missing scope only; do not broaden the target.
stop behavior: Return blocked handoff scope result.
```

```text
stage_id: source_and_path_frame
purpose: Identify source files to read, allowed paths, forbidden paths, and source integrity requirements.
activation conditions: handoff_fit passes.
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
expansion rule: Add bounded validation requirements only within the handoff scope.
stop behavior: Return validation/return-contract blocker.
```

```text
stage_id: handoff_package
purpose: Produce the final self-contained Codex handoff.
activation conditions: all prior gates pass.
inputs: Stage outputs.
required intermediate output: Complete Codex handoff package.
gate: PASS only if all required package fields are present.
checkpoint rule: None by default.
expansion rule: None.
stop behavior: Return incomplete package blocker.
```

## Gate Outcomes

- `PASS`: required handoff scope, sources, paths, validation, stop conditions, and return fields are present.
- `PASS_WITH_RISK`: package is usable but limitations are explicit and bounded.
- `REWORK`: revise missing or vague package fields before closure.
- `EXPAND`: inspect exact repository source only to complete source/path boundaries.
- `STOP`: return blocked result when required handoff authority or fields are missing.
- `TRANSFER`: return a candidate handoff packet for a later Codex adapter run.
- `RUN_EXTERNAL_HANDOFF`: when embedded in an owner procedure and the Codex result is required before that owner can complete RUN, return the complete handoff envelope and expected return packet.

## Optional Expansion

Allowed expansion is limited to exact repository source inspection needed for source/path boundaries or validation framing. Expansion must not become product execution, mutation, acceptance, or procedure switching.

## Research Policy

External research is forbidden by default. Exact repository source inspection is allowed or required when needed for source/path boundaries. Do not use research to infer acceptance, Direction runtime state, or Project UI state.

## Checkpoint Policy

No checkpoint is required by default for a complete bounded handoff. Checkpoint when the user must decide path boundaries, commit/push policy, validation scope, return fields, or whether Codex is authorized after the package draft.

## Output Contract

```text
handoff_id:
owner_entrypoint:
owner_procedure_ref:
utility_category: codex_handoff_packet
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
copy_paste_packet:
expected_return_packet:
validation_required_on_return:
resume_rule:
requested_return_fields:
```

## Eval / Quality Checks

- Package identifies exact source reads and path boundaries.
- Package includes validation and stop conditions.
- Package states commit/push policy.
- Package states Project refresh reporting requirements when changed files affect ChatGPT Projects.
- Package includes requested return fields sufficient for later verification.
- Package does not authorize product execution by implication.
- Package does not omit forbidden paths or validation.
- Package does not permit Codex to decide acceptance.
- Package does not instruct Codex to perform ChatGPT lifecycle FINISH.

## Stop Conditions

- requested Codex work is unbounded;
- mutation authority is unclear;
- product execution is implied but not bounded;
- source files to read are missing;
- allowed or forbidden paths are missing;
- validation is missing;
- stop conditions are missing;
- commit/push policy is missing;
- requested return fields are missing;
- package would let Codex accept its own output or mutate outside allowed paths.

## Procedure Closure

Return the handoff package as candidate output. Codex returns evidence only, and that result remains candidate evidence until verification and acceptance.

If lifecycle FINISH is active, close through FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet only for this selected adapter run. Do not launch Codex invisibly and do not ask Codex to close the ChatGPT lifecycle.

END_OF_FILE: workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md
