# Codex Handoff Procedure

status: active_procedure
procedure_class: utility_adapter

## Purpose

Use `codex_handoff` to create a self-contained Codex package for bounded repository maintenance or implementation.

The procedure produces a candidate handoff package only. It does not launch Codex invisibly, authorize acceptance, mutate state, or broaden product execution by implication.

Class and embedded utility semantics are governed by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

## Utility Adapter Mode

standalone_selection:

- START may select `codex_handoff` directly only when the user's primary request is to prepare a Codex handoff artifact.
- Standalone mode follows START -> RUN -> FINISH and returns a handoff package as candidate output.
- Standalone mode does not execute Codex, decide acceptance, perform storage mutation, or open follow-up material work.

embedded_packet_schema:

- A selected owner procedure may use this file as a packet schema/quality gate only when its procedure source and run surface allow `codex_handoff_packet`.
- Embedded use does not change `selected_entrypoint`, does not change `selected_procedure_ref`, and does not open a new lifecycle.
- Embedded use returns a typed `codex_handoff_packet`; when the owner procedure requires the Codex result before completion, the gate outcome is `RUN_EXTERNAL_HANDOFF`.
- Codex must return evidence to the owner procedure. Codex must not perform ChatGPT lifecycle FINISH or decide acceptance.

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
- Do not use embedded mode unless the selected owner procedure and run surface allow `codex_handoff_packet`.

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

Embedded mode also requires:

- owner_entrypoint;
- owner_procedure_ref;
- utility_category: `codex_handoff_packet`;
- handoff_purpose;
- expected_return_packet;
- validation_required_before_resume;
- resume_rule.

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
- `RUN_EXTERNAL_HANDOFF`: in embedded mode, pause the same selected owner procedure with a complete Codex handoff packet when returned evidence is required before owner completion.

## Optional Expansion

Allowed expansion is limited to exact repository source inspection needed for source/path boundaries or validation framing. Expansion must not become product execution, mutation, acceptance, or procedure switching.

## Research Policy

External research is forbidden by default. Exact repository source inspection is allowed or required when needed for source/path boundaries. Do not use research to infer acceptance, Direction runtime state, or Project UI state.

## Utility / Adapter Policy

allowed_utility_categories:

- produces `codex_handoff_packet`;
- no embedded child utility categories.

external_handoff_policy:

- Standalone mode returns a Codex package for a later external action.
- Embedded mode may emit `RUN_EXTERNAL_HANDOFF` only for the same selected owner procedure.

external_return_policy:

- Returned Codex content is adapter evidence until verified.
- The owner procedure resumes only after `RUN_EXTERNAL_RETURN` matches the pending handoff and required verification passes or blocks.

embedded_verification_policy:

- This procedure does not verify returned Codex results.
- Same-run verification uses the `codex_return_verification` category as an embedded RUN gate when the selected owner procedure and run surface allow it.

storage_boundary:

- The handoff may ask Codex to edit allowed repository paths, but accepted Workflow state still requires later verification and acceptance/update authority.
- Storage execution is never embedded in this procedure.

## External Handoff and Resume Policy

Embedded `RUN_EXTERNAL_HANDOFF` output must include:

```text
RUN_EXTERNAL_HANDOFF:
  lifecycle_state: RUN_WAITING_FOR_EXTERNAL_RETURN
  owner_entrypoint:
  owner_procedure_ref:
  utility_category: codex_handoff_packet
  external_surface: Codex
  handoff_purpose:
  copy_paste_packet:
  expected_return_packet:
  validation_required_before_resume:
  resume_rule: resume the same selected owner procedure after RUN_EXTERNAL_RETURN
```

FINISH_REQUEST is forbidden while a required embedded Codex return is pending.

## Checkpoint Policy

No checkpoint is required by default for a complete bounded handoff. Checkpoint when the user must decide path boundaries, commit/push policy, validation scope, return fields, or whether Codex is authorized after the package draft.

## Output Contract

```text
standalone_or_embedded_mode:
owner_entrypoint_if_embedded:
owner_procedure_ref_if_embedded:
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
requested_return_fields:
resume_rule_if_embedded:
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
- Embedded mode preserves the selected owner procedure and emits `RUN_EXTERNAL_HANDOFF` only when external evidence is required before owner completion.

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

In standalone mode, return the handoff package as candidate output and close through FINISH when lifecycle FINISH is active.

In embedded mode, return `RUN_EXTERNAL_HANDOFF` to the same selected owner procedure when returned Codex evidence is required before completion. This is not FINISH_REQUEST, FINISH, or Next Move closure.

Codex result remains adapter evidence until verification and acceptance.

If lifecycle FINISH is active, close through FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet. Do not launch Codex invisibly.

END_OF_FILE: workflow_v3/procedures/CODEX_HANDOFF_PROCEDURE.md
