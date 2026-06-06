# Procedure Authoring and Integration Procedure

status: active_procedure
kind: core
utility_policy: utility_allowed_when_needed

## Local Registry Alignment

This section is a local alignment mirror only. `workflow_v3/control_plane/PROCEDURE_REGISTRY.md` remains the routing authority.

```text
entrypoint: author_workflow_procedure
procedure_path: workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md
kind: core
```

## Purpose

Use this procedure to create, revise, author, or integrate Workflow v3 procedure definitions and their registry/eval/procedure-boundary relationships.

This procedure is non-mutating. It produces candidate definitions, patch plans, utility handoff packets, and integration proposals only.

For non-trivial authoring, it must proceed through staged/checkpointed design before detailed body drafting.

## Runtime Kernel Alignment

This procedure is selected by START and is summarized in `START_CONTRACT`.

Runtime lifecycle:

```text
START -> RUN -> CHECK -> FINISH -> CLOSED
```

Utility flow during RUN:

```text
RUN -> UTILITY_CALL -> UTILITY_RETURN -> RUN
```

RUN emits `STAGE_RESULT` after each material stage. User `CONTINUE` / `ДАЛЬШЕ` is required before the next material stage unless the next step is an `internal_check`.

## Trigger / When to Use

- User asks to create a new Workflow v3 procedure.
- User asks to revise an existing procedure.
- User asks to author a detailed body for a self-contained stub procedure.
- User asks to integrate a procedure into Workflow v3 registry/control-plane setup.
- User asks to prepare a procedure-related repository patch plan or bounded Codex handoff.

## When Not to Use

- Do not use to execute the procedure being authored.
- Do not use to mutate repository/runtime state directly.
- Do not use to accept candidate output.
- Do not use to update actual ChatGPT Project UI.
- Do not use to author unrelated target procedure bodies in the same run.
- Do not use to import legacy evidence, deleted runbooks, or obsolete formation sources as current authority.
- Do not use to start ordinary Direction runtime or accept Direction state.

## Required Inputs

General inputs:

- target procedure name or intent;
- target procedure boundary or candidate procedure boundary;
- expected trigger;
- expected output;
- known boundaries;
- source files to inspect;
- requested integration scope;
- repository/base ref when repository work is requested.

Mode classification:

```text
mode: new_procedure | existing_revision | stub_body_authoring
```

For authoring from a self-contained stub, also require or extract from exact source:

```text
current_registry_entrypoint:
current_registry_procedure_path:
canonical_procedure_path:
target_role:
workflow_integration:
future_body_scope:
future_body_must_not:
required_outputs_when_authored:
stop_behavior_until_authored:
canonical_path_exception_if_any:
```

## Source Requirements

Read exact relevant Workflow v3 framework, registry, control-plane, utility, eval, template, and existing procedure sources needed for the requested design scope. Verify EOF where markers exist.

Required source classes for material procedure authoring:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`
- selected procedure source when revising or authoring a stub body
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` when lifecycle boundaries are involved
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` when closure boundaries are involved
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` when kind, utility category, Codex/check/child/storage package, or utility return is involved
- Procedure Definition Canon, Procedure Authoring Guide, Procedure Template, and eval sources as needed

Source-boundary rules:

- Project Files/Sources are cache/context only.
- Chat memory is cache/context only.
- `directions/**` is `legacy_evidence` or migration evidence only when encountered.
- Legacy or migration evidence is not automatically imported.
- Legacy or migration evidence is not automatically discarded.
- No accepted Workflow v3 state exists by implication.

Do not read or require deleted runbooks or obsolete formation sources as current authority.

## Context Classification

Classify inputs as canonical repository source, accepted record, current human input, candidate context, adapter evidence, verified excerpt, Project Files cache/context, legacy_evidence, or unknown/unverified.

Exact repository files at named repo/path/ref win over cache/context.

## Complexity Selector

Use the smallest authoring path that satisfies the output contract:

- `simple`: compact same-path revision, small source-mechanical correction, or self-contained stub target spec with no disputed method design.
- `standard`: bounded procedure creation/revision using internal Workflow v3 framework sources, no external research, and no user checkpoint before final draft unless ambiguity appears.
- `checkpointed`: non-trivial procedure design where method, target role, integration boundary, source grounding, kind, utility policy, or eval plan should be approved before detailed body drafting.
- `research_backed`: external/current research is required by Stage 3 before final detailed body drafting.
- `delegated_or_tool_mediated`: bounded check, child research, Codex, storage package, provider/tool, or external-return work is needed; this procedure may only produce allowed packets or embedded verification gates.

## Canonical Location and Naming Policy

New Procedure Definition Framework procedures must live under:

```text
workflow_v3/procedures/**
```

Procedure files must use procedure naming:

```text
*_PROCEDURE.md
```

When authoring or revising a procedure in the Procedure Definition Framework:

- do not keep `*_RUNBOOK.md` or `*_PLAYBOOK.md` naming merely to reduce path churn;
- use a canonical `workflow_v3/procedures/*_PROCEDURE.md` target path;
- propose a registry delta so `procedure_path` points to the canonical procedure file when required;
- base detailed body authoring on the canonical stub target spec when a stub exists;
- preserve the stub's target role, workflow integration, future scope, must-not constraints, required outputs, and stop behavior unless explicitly revising the stub itself;
- mark any non-canonical location or naming as an exception requiring explicit justification.

Registry entries must point to canonical procedure files.

## Procedure Kind and Utility Policy

Procedure authoring must decide and document:

```text
kind:
utility_policy:
common_utility_choices:
forbidden_utility_categories:
utility_call_policy:
external_return_policy:
external_return_verification:
embedded_verification_policy:
storage_boundary:
```

Use `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` for utility class, utility category, `UTILITY_CALL`, `UTILITY_RETURN`, and Utility Call Rule semantics.

A procedure may name common utility choices or explicit forbiddances. Absent prelisting does not block bounded utility access through the Utility Call Rule. Utility calls use `UTILITY_CALL` and `UTILITY_RETURN`, resume the same selected main procedure, and treat returned evidence as evidence, not accepted state by itself.

## Stage Model

The following visible stages are material stages. Each material stage emits `STAGE_RESULT`, then waits for user `CONTINUE` / `ДАЛЬШЕ` before the next material stage unless the next step is an `internal_check`.

Mechanical source, EOF, consistency, and validation checks may run as `internal_check` steps inside the current material stage. An `internal_check` does not require a separate continuation unless it changes scope, requires a utility call, or blocks.

### Stage 0 - Source Lock / Procedure Selection

```text
stage_id: source_lock_procedure_selection
stage_type: material stage
purpose: Confirm the selected work belongs to author_workflow_procedure and lock exact source authority before design.
activation conditions: Always.
inputs: User request, Procedure Registry, selected procedure source, procedure boundary contract, utility protocol when relevant, requested source refs.
required_stage_result: selected_entrypoint, selected_procedure_path, procedure_boundary, kind, source_lock, context_classification, source limitations.
gate: PASS if registry entry, selected source, procedure boundary, kind, and source authority are verified; STOP if any required source is missing, stale, unreadable, or conflicting.
utility_allowed_if: exact source access, Git/ref verification, or bounded repository inspection needs an admitted file, GitHub, Codex, or check utility.
blocked_if: any required source is missing, stale, unreadable, conflicting, or outside the selected authoring boundary.
checkpoint rule: None by default.
expansion rule: Read only exact framework/control/eval/procedure sources needed for the admitted authoring task.
stop behavior: Return SOURCE_INTEGRITY_STOP, UNREGISTERED_ACTION_EXCEPTION, or SPLIT_REQUIRED.
```

### Stage 1 - Procedure Identity Brief

```text
stage_id: procedure_identity_brief
stage_type: material stage
purpose: Explain what the target procedure is, why it exists, and how it fits into Workflow before drafting.
activation conditions: Always.
inputs: User target, registry/source facts, existing procedure source or candidate target intent.
required_stage_result: procedure_name, entrypoint, canonical_path, kind, target_role, workflow_integration, when_to_use, when_not_to_use, expected_output, non_goals, mode.
gate: PASS if the identity brief is specific and bounded; REWORK if role or integration is vague; STOP if the target is not a Workflow v3 procedure authoring task.
utility_allowed_if: exact source facts or registry/source consistency require admitted source access or a bounded check.
blocked_if: the target is not a Workflow v3 procedure authoring task, or its role/integration cannot be bounded.
checkpoint rule: Checkpoint if identity, class, integration, or mode is disputed.
expansion rule: Ask for missing target intent only when it cannot be inferred from exact source and current human input.
stop behavior: Return bounded identity blocker.
```

### Stage 2 - Stub / Source Grounding

```text
stage_id: stub_source_grounding
stage_type: material stage
purpose: Ground authoring in the canonical existing source or self-contained stub target spec.
activation conditions: Always.
inputs: Selected procedure source, existing procedure file, stub target spec when present, requested revision scope.
required_stage_result: existing_source_status, stub_status, extracted_target_role, extracted_workflow_integration, extracted_future_body_scope, extracted_future_body_must_not, extracted_required_outputs_when_authored, source_limitations.
gate: PASS if the source or stub is self-contained enough to support the requested authoring; REWORK if target spec needs repair; STOP if the task depends on deleted, stale, or non-authoritative sources.
utility_allowed_if: exact source or stub availability, EOF, or consistency requires admitted file, GitHub, Codex, or check utility access.
blocked_if: the task depends on deleted, stale, or non-authoritative sources, or the source/stub is not self-contained enough for the requested authoring.
checkpoint rule: Checkpoint when stub meaning, source authority, or deleted-source independence is unclear.
expansion rule: Do not infer from Project Files, chat memory, or obsolete context. Use exact repository source or verified excerpts only.
stop behavior: Return source grounding blocker.
```

### Stage 3 - Complexity and Research Need Gate

```text
stage_id: complexity_research_need_gate
stage_type: material stage
purpose: Select the smallest sufficient authoring path and decide whether external/current research is forbidden, optional, or required.
activation conditions: Always after Stage 2.
inputs: Identity brief, source grounding, requested output, target impact, method uncertainty.
required_stage_result: complexity_class, research_decision, research_reason, research_questions_if_required, evidence_plan_if_required, source_policy_if_required.
gate: PASS if complexity and research policy are justified; UTILITY_CALL, TRANSFER, or STOP if required research/check/tool work is outside current scope.
utility_allowed_if: approved research, check, or tool-mediated evidence is needed to resolve a required design or validation question.
blocked_if: required research/check evidence is absent, unapproved, or outside the selected procedure boundary.
checkpoint rule: If research is required, stop before final body drafting until user approves the research questions/evidence plan or provides approved research context.
expansion rule: Research is required only for complex method design, high-impact decision logic, non-obvious best practices, external tooling/provider behavior, current external constraints, or explicit user request. Do not make research mandatory for simple procedure edits.
stop behavior: Return research approval checkpoint or bounded research/check handoff candidate.
```

### Stage 4 - Method / Best-Practice Design Plan

```text
stage_id: method_best_practice_design_plan
stage_type: material stage
purpose: Explain the planned procedure logic before drafting the detailed body.
activation conditions: Required for checkpointed, research_backed, delegated_or_tool_mediated, new non-trivial procedures, major revisions, or stub body authoring with high impact.
inputs: Stage 1 identity, Stage 2 grounding, Stage 3 complexity/research decision, Procedure Definition Canon, Procedure Authoring Guide, Utility Adapter Protocol.
required_stage_result: method_summary, applicable_techniques_patterns_or_workflow_principles, overcomplexity_control, integration_with_START_RUN_CHECK_FINISH, integration_with_CLOSURE_CHECK_and_NEXT_CHAT_CARD, integration_with_utility_boundaries, integration_with_parent_or_evidence_boundaries_where_relevant, acceptance_and_update_boundaries, approval_checkpoint_question.
gate: PASS only after user approval when the procedure is non-trivial; REWORK if the method is too vague, too complex, or violates boundaries.
utility_allowed_if: a bounded check, research, or handoff candidate is needed to explain or verify the method under the Utility Call Rule.
blocked_if: a non-trivial method requires approval and approval is absent, or the method violates source, utility, acceptance, or update boundaries.
checkpoint rule: User approval required before Stage 5 for non-trivial procedure body authoring.
expansion rule: May propose bounded check/research/handoff candidates, but must not launch them invisibly.
stop behavior: Return method checkpoint requiring user approval.
```

### Stage 5 - Detailed Procedure Body Draft

```text
stage_id: detailed_procedure_body_draft
stage_type: material stage
purpose: Create or revise the actual procedure body after source, complexity, research, utility, and method gates pass.
activation conditions: Stage 4 passed or was explicitly not required for simple/standard work.
inputs: Approved method plan when required, Procedure Definition Canon, template, guide, selected source, utility protocol, eval sources.
required_stage_result: candidate_procedure_body_or_revision_package, changed_sections, retained_sections, removed_or_replaced_sections, kind, utility_policy, utility_call_policy, stop_conditions, output_contract.
gate: PASS if the body includes purpose, triggers, non-triggers, required inputs, source requirements, context classification, complexity selector, stage model, gates, checkpoint policy, optional expansion, research policy, utility policy, output contract, eval checks, stop conditions, and closure.
utility_allowed_if: approved drafting work needs bounded source access, validation, Codex support, or check evidence within the selected procedure boundary.
blocked_if: required source, approved method, research/check evidence, or utility return is missing or cannot be verified.
checkpoint rule: Checkpoint only if the draft introduces new boundaries, new handoff paths, new eval requirements, or unresolved design choices.
expansion rule: Use eval sources as checks; do not broaden into authoring unrelated procedure bodies.
stop behavior: Return draft insufficiency or boundary blocker.
```

### Stage 6 - Eval / Registry / Integration Plan

```text
stage_id: eval_registry_integration_plan
stage_type: material stage
purpose: Identify required or optional changes outside the procedure body.
activation conditions: Always after Stage 5.
inputs: Candidate body/revision package, Procedure Registry, procedure boundary contract, Utility Adapter Protocol, definition/execution evals, closure templates.
required_stage_result: eval_implications, registry_delta_if_required, kind_delta_if_required, lifecycle_kernel_delta_if_required, project_refresh_requirements, codex_or_storage_handoff_need, allowed_paths_if_later_handoff_needed, forbidden_paths_if_later_handoff_needed.
project_refresh_requirements: project_instruction_ui_update_required, project_sources_files_refresh_required, request_only_sources_refresh_required, do_not_upload_as_project_file.
gate: PASS if integration impact is explicit and bounded; UTILITY_CALL or TRANSFER only as an allowed typed output; STOP if required integration cannot be bounded.
utility_allowed_if: Codex, storage, source, GitHub, or check work is needed and can be emitted as a bounded `UTILITY_CALL`.
blocked_if: required integration cannot be bounded, or a repository/project mutation would be implied without an admitted utility or storage boundary.
checkpoint rule: Checkpoint before any proposed repository mutation package.
expansion rule: Propose Codex/storage/check work only as candidate packet or allowed UTILITY_CALL, not as hidden launch.
stop behavior: Return integration blocker or handoff-needed candidate.
```

### Stage 7 - Closure

```text
stage_id: closure
stage_type: material stage
purpose: Return the candidate revision package, limitations, residual risks, and exact next move.
activation conditions: Always after completed or stopped stages and after required utility returns are resolved or blocked.
inputs: Stage outputs.
required_stage_result: candidate_revision_package, exact_patch_plan, eval_implications, handoff_need, source_limitations, residual_risks, CLOSURE_CHECK.
gate: PASS if the candidate package is complete and CLOSURE_CHECK can compare it to this procedure's completion contract; PASS_WITH_RISK if limitations are explicit; STOP if required outputs are absent or required utility returns are pending.
utility_allowed_if: returned evidence from an earlier `UTILITY_CALL` must be matched and verified before reliance.
blocked_if: required outputs are absent, a required utility return is pending, or CLOSURE_CHECK cannot compare actual result to the completion contract.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return blocked result and exact missing requirement.
```

## Gate Outcomes

Use `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, `TRANSFER`, `UTILITY_CALL`, and `UTILITY_RETURN`.

`UTILITY_CALL` is limited to registered utility resources and does not launch them invisibly.

## Optional Expansion

Allowed expansion is limited to exact source inspection, bounded eval/check planning, bounded research planning, embedded verification of returned evidence, or a candidate Codex/storage handoff when requested and bounded.

Expansion must remain subordinate to the selected main procedure.

## Research Policy

Research is not mandatory by default.

Use the smallest sufficient research posture:

- `forbidden`: simple procedure edits, source-mechanical revisions, registry/path cleanup, or cases where exact internal Workflow v3 framework sources are sufficient.
- `optional`: design may benefit from outside methods, but internal sources are enough to produce a safe candidate if limitations are stated.
- `required`: the procedure involves complex method design, high-impact decision logic, non-obvious best practices, external tooling/provider behavior, current external constraints, or the user explicitly requests research.

When research is required, do not draft the final detailed procedure body immediately. First return:

```text
research_questions:
evidence_plan:
source_policy:
approval_checkpoint:
```

Proceed to detailed body drafting only after user approval or after the user provides approved research context.

## Utility / Adapter Policy

Common utility choices for this procedure through the Utility Call Rule:

- `codex_handoff_packet` for bounded repository maintenance patches derived from the selected authoring run;
- `codex_return_verification` for returned results from a Codex handoff emitted by the same selected authoring run;
- `check_job_packet` for bounded source/evidence/consistency/validation questions;
- `child_research_packet` for approved research questions/evidence plans;
- `storage_update_package` only as a candidate next-surface package after acceptance/update authority is clear;
- `project_refresh_instruction_packet` for reporting refresh requirements only.

If this procedure emits `UTILITY_CALL`, it must include the complete packet, expected return fields, validation requirements, same selected main procedure resume, and the required `UTILITY_RETURN` verification boundary. Returned evidence is not accepted state by itself.

Do not select `codex_handoff`, `codex_result_verification`, `check_job`, or any other utility adapter as a new main procedure during this RUN.

## Checkpoint Policy

No checkpoint is required for simple bounded procedure edits that remain canonical.

Checkpoint when scope, registry mapping, canonical path/naming, stub/body status, deleted-source independence, kind, utility policy, complex method design, eval design, or future mutation boundaries are ambiguous.

For non-trivial procedure authoring, Stage 4 method approval is required before Stage 5 detailed body drafting.

## Completion Contract

```text
completion:
  result: candidate procedure revision package, exact patch plan, utility package if needed, eval update plan, and NEXT_CHAT_CARD or no_next_chat_needed
  proof: target identity, source basis, method design, kind/utility policy, candidate body or patch plan, eval/registry impact, limitations, and residual risks are recorded
  blocked_if: target procedure is unbounded, required sources are missing, requested patch lacks selected/utility write path, research/check evidence is absent, or utility return cannot be verified
```
## Output Contract

```text
candidate_revision_package:
  target_file:
  revision_type:
  source_basis:
  procedure_identity_brief:
  stub_or_source_grounding:
  complexity_and_research_decision:
  method_design_plan:
  kind_and_utility_policy:
  candidate_body_or_patch_plan:
  eval_registry_integration_plan:
  source_limitations:
  residual_risks:

exact_patch_plan:
  files_to_change:
  sections_to_replace:
  sections_to_add:
  sections_to_preserve:
  validation_checks:

eval_implications:
  procedure_definition_eval:
  procedure_execution_eval:
  additional_eval_changes_required:

project_refresh_requirements:
  project_instruction_ui_update_required:
  project_sources_files_refresh_required:
  request_only_sources_refresh_required:
  do_not_upload_as_project_file:

handoff_need:
  needed:
  handoff_type:
  reason:
  candidate_allowed_paths:
  candidate_forbidden_paths:
  copy_paste_packet_if_required:

closure:
  utility_return_status:
  CLOSURE_CHECK:
  FINISH_PACKET_after_explicit_FINISH_or_ФИНИШ:
  NEXT_CHAT_CARD_or_no_next_chat_needed:
```

## Eval / Quality Checks

- Procedure has distinguishable trigger and non-trigger.
- Required inputs and exact source requirements are explicit.
- Context classification includes adapter evidence where relevant.
- Kind matches registry metadata.
- Utility decision gate and adapter policy are explicit when utility boundaries matter.
- Material stages emit `STAGE_RESULT`, carry required stage fields, and use material gates.
- Non-trivial authoring explains method before drafting detailed body.
- Research posture is justified and does not force research for simple edits.
- Stop conditions prevent invention, hidden mutation, self-acceptance, hidden procedure switching, and complex body authoring by implication.
- Procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming unless an explicit exception is justified.
- Stub procedure body authoring preserves target role, workflow integration, output contract, future scope, must-not constraints, and STOP behavior until authored.
- Registry hint proposal is compact and does not replace procedure source.
- Closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed correctly.
- CLOSURE_CHECK does not pass while a required utility return is pending.

## Stop Conditions

- target procedure is unbounded;
- requested procedure would silently mutate state;
- requested procedure crosses into unrelated body authoring without separate scope;
- required sources are missing;
- procedure keeps obsolete runbook/playbook path or naming without explicit exception;
- registry delta would leave a procedure pointing outside canonical procedure files;
- user asks to patch repository without admitted utility handoff or storage boundary;
- research is required but questions/evidence/source policy are not approved;
- embedded utility use would become hidden procedure switching, acceptance, mutation, or unbounded external wait;
- required utility return is missing or cannot be matched to the emitted handoff.

## Procedure Closure

Close with the candidate design outputs, limitations, canonical path/registry/stub status, kind/utility status, and exact next move.

If repository changes are needed later, return a bounded Codex/storage/update packet or UTILITY_CALL rather than applying changes directly inside this procedure.

CLOSURE_CHECK may pass only after required utility calls have returned, been verified, or been explicitly stopped/abandoned.

After CLOSURE_CHECK passes or explicitly blocks under this procedure's completion contract, FINISH may proceed only after explicit `FINISH` / `ФИНИШ`. Passing FINISH emits `FINISH_PACKET`, includes `NEXT_CHAT_CARD` or `no_next_chat_needed`, and leaves the same chat CLOSED for material work.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md
