# Procedure Authoring and Integration Procedure

status: active_procedure
kind: core
utility_policy: compatibility_alias_for_child_call_policy
child_call_policy: child_call_allowed_when_needed

## Purpose

Use this procedure to create, revise, author, or integrate Workflow v3 procedure definitions and their registry, procedure-local quality-check, and procedure-boundary relationships.

This procedure is non-mutating. It produces candidate definitions/design evidence, patch plans, child-call envelopes, and integration proposals only. If repository mutation is required for the current START goal and the parent chat cannot mutate directly, the visible stage output must emit/open `CHILD_PROCEDURE_CALL` and pause the parent RUN until the matching return is verified.

For non-trivial authoring, it must proceed through staged/checkpointed design before detailed body drafting.

## Trigger / When to Use

- User asks to create a new Workflow v3 procedure.
- User asks to revise an existing procedure.
- User asks to author a detailed body for a self-contained stub procedure.
- User asks to integrate a procedure into Workflow v3 registry/control-plane setup.
- User asks to prepare a procedure-related repository patch plan or bounded Codex child procedure call.

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

Read exact relevant Workflow v3 framework, registry, control-plane, child/adaptor, template, procedure-local quality-check, and existing procedure sources needed for the requested design scope. Verify EOF where markers exist.

Required source classes for material procedure authoring:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`
- selected procedure source when revising or authoring a stub body
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` when lifecycle boundaries are involved
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` when closure boundaries are involved
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` when kind, child/adaptor category, Codex/check/child/storage packet, or child return is involved
- Procedure Definition Canon, Procedure Authoring Guide, Procedure Template, and procedure-local quality-check sections as needed
- Repository validation aids under `workflow_v3/evals/**` only when explicitly in scope; they are not runtime or procedure authority

Treat Project Files/Sources and chat memory as cache/context only.

Do not read or require deleted runbooks or obsolete formation sources as current authority.

## Context Classification

Classify inputs as canonical repository source, accepted record, current human input, candidate context, adapter evidence, verified excerpt, Project Files cache/context, legacy_evidence, or unknown/unverified.

Exact repository files at named repo/path/ref win over cache/context.

## Complexity Selector

Use the smallest authoring path that satisfies the output contract:

- `small_bounded_revision`: compact same-path revision, small source-mechanical correction, or self-contained stub target spec with no disputed method design.
- `standard`: bounded procedure creation/revision using internal Workflow v3 framework sources, no external research, and no user checkpoint before final draft unless ambiguity appears.
- `checkpointed`: non-trivial procedure design where method, target role, integration boundary, source grounding, kind, child-call policy, or quality-check plan should be approved before detailed body drafting.
- `research_backed`: external/current research is required by Stage 3 before final detailed body drafting.
- `delegated_or_tool_mediated`: bounded check, child research, Codex, storage packet, provider/tool, or external-return work is needed; this procedure may only produce `CHILD_PROCEDURE_CALL` envelopes or embedded verification gates.

Complexity selection is not runtime stage compression. RUN must execute the declared stages below. A stage may end quickly or be marked not_applicable with evidence, but START/RUN must not invent ad hoc simple, compact, shortcut, or single-stage compression that bypasses declared stages.

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
child_call_policy:
common_child_call_choices:
forbidden_child_call_categories:
child_call_envelope_policy:
external_return_policy:
external_return_verification:
embedded_verification_policy:
storage_boundary:
```

Use `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` for class, child/adaptor category, and child-call gate semantics.

A procedure may name common child/adaptor choices or explicit forbiddances. Absent prelisting does not block global child/adaptor access through the child-call gate. Embedded child/adaptor use is not a new main procedure and must not become hidden procedure switching.

## Stage Cards

### Stage 0 - Source Lock / Procedure Selection

```text
stage_id: source_lock_procedure_selection
purpose: Confirm the selected work belongs to author_workflow_procedure and lock exact source authority before design.
activation conditions: Always.
inputs: User request, Procedure Registry, selected procedure source, procedure boundary contract, child/adaptor protocol when relevant, requested source refs.
required intermediate output: selected_entrypoint, selected_procedure_path, procedure_boundary, kind, source_lock, context_classification.
gate: PASS if registry entry, selected source, procedure boundary, kind, and source authority are verified; STOP if any required source is missing, stale, unreadable, or conflicting.
checkpoint rule: None by default.
expansion rule: Read only exact framework/control/procedure-local quality/procedure sources needed for the admitted authoring task.
stop behavior: Return SOURCE_INTEGRITY_STOP, UNREGISTERED_ACTION_EXCEPTION, or SPLIT_REQUIRED.
```

### Stage 1 - Procedure Identity Brief

```text
stage_id: procedure_identity_brief
purpose: Explain what the target procedure is, why it exists, and how it fits into Workflow before drafting.
activation conditions: Always.
inputs: User target, registry/source facts, existing procedure source or candidate target intent.
required intermediate output: procedure_name, entrypoint, canonical_path, kind, target_role, workflow_integration, when_to_use, when_not_to_use, expected_output, non_goals, mode.
gate: PASS if the identity brief is specific and bounded; REWORK if role or integration is vague; STOP if the target is not a Workflow v3 procedure authoring task.
checkpoint rule: Checkpoint if identity, class, integration, or mode is disputed.
expansion rule: Ask for missing target intent only when it cannot be inferred from exact source and current human input.
stop behavior: Return bounded identity blocker.
```

### Stage 2 - Stub / Source Grounding

```text
stage_id: stub_source_grounding
purpose: Ground authoring in the canonical existing source or self-contained stub target spec.
activation conditions: Always.
inputs: Selected procedure source, existing procedure file, stub target spec when present, requested revision scope.
required intermediate output: existing_source_status, stub_status, extracted_target_role, extracted_workflow_integration, extracted_future_body_scope, extracted_future_body_must_not, extracted_required_outputs_when_authored, source_limitations.
gate: PASS if the source or stub is self-contained enough to support the requested authoring; REWORK if target spec needs repair; STOP if the task depends on deleted, stale, or non-authoritative sources.
checkpoint rule: Checkpoint when stub meaning, source authority, or deleted-source independence is unclear.
expansion rule: Do not infer from Project Files, chat memory, or obsolete context. Use exact repository source or verified excerpts only.
stop behavior: Return source grounding blocker.
```

### Stage 3 - Complexity and Research Need Gate

```text
stage_id: complexity_research_need_gate
purpose: Select the smallest sufficient authoring path and decide whether external/current research is forbidden, optional, or required.
activation conditions: Always after Stage 2.
inputs: Identity brief, source grounding, requested output, target impact, method uncertainty.
required intermediate output: complexity_class, research_decision, research_reason, research_questions_if_required, evidence_plan_if_required, source_policy_if_required.
gate: PASS if complexity and research policy are justified; CHILD_PROCEDURE_CALL, TRANSFER, or STOP if required research/check/tool work is outside current scope.
checkpoint rule: If research is required, stop before final body drafting until user approves the research questions/evidence plan or provides approved research context.
expansion rule: Research is required only for complex method design, high-impact decision logic, non-obvious best practices, external tooling/provider behavior, current external constraints, or explicit user request. Do not make research mandatory for small bounded procedure edits.
stop behavior: Return research approval checkpoint, bounded research/check child-call framing, or a blocked result.
```

### Stage 4 - Method / Best-Practice Design Plan

```text
stage_id: method_best_practice_design_plan
purpose: Explain the planned procedure logic before drafting the detailed body.
activation conditions: Required for checkpointed, research_backed, delegated_or_tool_mediated, new non-trivial procedures, major revisions, or stub body authoring with high impact.
inputs: Stage 1 identity, Stage 2 grounding, Stage 3 complexity/research decision, Procedure Definition Canon, Procedure Authoring Guide, Utility Adapter Protocol.
required intermediate output: method_summary, applicable_techniques_patterns_or_workflow_principles, overcomplexity_control, integration_with_START_RUN_CHECK_FINISH, integration_with_CLOSURE_CHECK_and_NEXT_CHAT_CARD, integration_with_child_call_boundaries, integration_with_parent_or_evidence_boundaries_where_relevant, acceptance_and_update_boundaries, approval_checkpoint_question.
gate: PASS only after user approval when the procedure is non-trivial; REWORK if the method is too vague, too complex, or violates boundaries.
checkpoint rule: User approval required before Stage 5 for non-trivial procedure body authoring.
expansion rule: May frame bounded check/research/child-call needs, but must not launch them invisibly.
stop behavior: Return method checkpoint requiring user approval.
```

### Stage 5 - Detailed Procedure Body Draft

```text
stage_id: detailed_procedure_body_draft
purpose: Create or revise the actual procedure body after source, complexity, research, child-call, and method gates pass.
activation conditions: Stage 4 passed or was explicitly not required for small bounded revision or standard work.
inputs: Approved method plan when required, Procedure Definition Canon, template, guide, selected source, child/adaptor protocol, procedure-local quality checks, and explicitly scoped repository validation aids.
required intermediate output: candidate_procedure_body_or_revision_package, changed_sections, retained_sections, removed_or_replaced_sections, kind, child_call_policy, stop_conditions, output_contract.
gate: PASS if the body includes purpose, triggers, non-triggers, required inputs, source requirements, context classification, complexity selector, declared stage cards, gates, checkpoint policy, optional expansion, research policy, child-call policy, output contract, quality checks, stop conditions, and closure.
checkpoint rule: Checkpoint only if the draft introduces new boundaries, new handoff paths, new quality-check requirements, or unresolved design choices.
expansion rule: Use procedure-local quality checks as checks; repository eval files under `workflow_v3/evals/**` are non-runtime validation aids only and must not broaden into authoring unrelated procedure bodies. Stage 5 may identify `repair_needed` and draft exact patch content internally, but if applying that repair is required for the current START goal and the parent cannot mutate directly, the visible output must open `CHILD_PROCEDURE_CALL`, not stop at a package or plan.
stop behavior: Return draft insufficiency or boundary blocker.
```

### Stage 6 - Quality / Registry / Integration Plan

```text
stage_id: quality_registry_integration_plan
purpose: Identify required or optional changes outside the procedure body.
activation conditions: Always after Stage 5.
inputs: Candidate body/revision package, Procedure Registry, procedure boundary contract, Utility Adapter Protocol, procedure-local quality checks, explicitly scoped repository validation aids, closure templates.
required intermediate output: quality_implications, registry_delta_if_required, kind_delta_if_required, project_refresh_categories, codex_or_storage_child_call_need, allowed_paths_if_later_child_call_needed, forbidden_paths_if_later_child_call_needed.
gate: PASS if integration impact is explicit and bounded; CHILD_PROCEDURE_CALL or TRANSFER only as an allowed typed output; STOP if required integration cannot be bounded.
checkpoint rule: Checkpoint before optional future mutation planning, but not before opening a required current-goal child call when the task already requires it and boundaries are complete.
expansion rule: If Codex/storage/check work is required for current START-goal repair, emit/open `CHILD_PROCEDURE_CALL`; otherwise frame optional future work as non-material context or transfer content. Hidden launch is forbidden.
stop behavior: Return integration blocker, opened child call, or explicit blocked result.
```

### Stage 7 - Closure

```text
stage_id: closure
purpose: Return the candidate revision package, limitations, residual risks, and exact next move.
activation conditions: Always after completed or stopped stages and after required child returns are resolved or blocked.
inputs: Stage outputs.
required intermediate output: candidate_revision_package, exact_patch_plan, quality_implications, child_calls, source_limitations, residual_risks, CLOSURE_CHECK.
gate: PASS if the revision/design evidence is complete, required child returns are verified, and CLOSURE_CHECK can compare it to this procedure's completion contract; PASS_WITH_RISK if limitations are explicit; STOP if required outputs are absent, required child/adaptor repair was identified but no child call is open/returned/verified, or required child returns are pending.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return blocked result and exact missing requirement.
```

## Gate Outcomes

Use `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, `TRANSFER`, `CHILD_PROCEDURE_CALL`, and `CHILD_PROCEDURE_RETURN`.

`CHILD_PROCEDURE_CALL` is limited to registered child/adaptor resources and does not launch them invisibly. `UTILITY_CALL` may be used only as an adapter-level compatibility alias.

## Optional Expansion

Allowed expansion is limited to exact source inspection, bounded quality/check planning, bounded research planning, embedded verification of returned evidence, optional non-material future transfer framing, or required current-goal `CHILD_PROCEDURE_CALL` opening.

Expansion must remain subordinate to the selected main procedure.

Required current-goal repair is not optional expansion. When repository mutation is required for the current START goal and the parent chat cannot mutate directly, the same `STAGE_RESULT` must emit/open `CHILD_PROCEDURE_CALL`, show `open_child_calls` with the call id, set `next_state: RUN_WAITING_FOR_CHILD_RETURN`, and require matching `CHILD_PROCEDURE_RETURN` / `CODEX_RETURN_PACKET`. Stage progression pauses until the matching return is verified.

## Research Policy

Research is not mandatory by default.

Use the smallest sufficient research posture:

- `forbidden`: small bounded procedure edits, source-mechanical revisions, registry/path cleanup, or cases where exact internal Workflow v3 framework sources are sufficient.
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

## Child / Adapter Policy

Common child/adaptor choices for this procedure through the child-call gate:

- `codex_child_call_packet` for bounded repository maintenance patches derived from the selected authoring run;
- `codex_return_verification` for returned results from a Codex handoff emitted by the same selected authoring run;
- `check_job_packet` for bounded source/evidence/consistency/validation questions;
- `child_research_packet` for approved research questions/evidence plans;
- `storage_update_package` only as a candidate next-surface package after acceptance/update authority is clear;
- `project_refresh_instruction_packet` for reporting refresh requirements only.

If this procedure emits `CHILD_PROCEDURE_CALL`, it must include the complete packet, expected return fields, validation requirements, and same-owner resume rule. The parent RUN enters `RUN_WAITING_FOR_CHILD_RETURN` and remains unresolved until a matching `CHILD_PROCEDURE_RETURN` is verified.

Do not select `codex_handoff`, `codex_result_verification`, `check_job`, or any other adapter as a new main procedure during this RUN.

## Checkpoint Policy

No checkpoint is required for small bounded procedure edits that remain canonical.

Checkpoint when scope, registry mapping, canonical path/naming, stub/body status, deleted-source independence, kind, child-call policy, complex method design, quality-check design, or future mutation boundaries are ambiguous.

For non-trivial procedure authoring, Stage 4 method approval is required before Stage 5 detailed body drafting.

## Completion Contract

```text
completion:
  result: verified candidate procedure revision/design evidence or explicit blocked result with exact missing sources, child returns, or validation
  proof: target identity, source basis, method design, kind/child-call policy, candidate body or patch plan, quality/registry impact, child-call status, limitations, and residual risks are recorded
  blocked_if: target procedure is unbounded, required sources are missing, repository mutation requires an open child call, research/check evidence is absent, required validation is missing, or child return cannot be verified
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
  kind_and_child_call_policy:
  candidate_body_or_patch_plan:
  quality_registry_integration_plan:
  source_limitations:
  residual_risks:

exact_patch_plan:
  files_to_change:
  sections_to_replace:
  sections_to_add:
  sections_to_preserve:
  validation_checks:

quality_implications:
  procedure_definition_quality:
  procedure_execution_quality:
  additional_quality_changes_required:

child_calls:
  opened:
  returned:
  verified:
  open_blockers:
  expected_return_contract:
  parent_verification_contract:

closure:
  child_return_status:
  CLOSURE_CHECK:
  FINISH_PACKET_after_explicit_FINISH:
  NEXT_CHAT_CARD_or_no_next_chat_needed:
```

## Quality Checks

- Procedure has distinguishable trigger and non-trigger.
- Required inputs and exact source requirements are explicit.
- Context classification includes adapter evidence where relevant.
- Kind matches registry metadata.
- Child-call decision gate and adapter policy are explicit when child/adaptor boundaries matter.
- Stage Cards produce intermediate outputs and use material gates.
- Non-trivial authoring explains method before drafting detailed body.
- Research posture is justified and does not force research for small bounded edits.
- Stop conditions prevent invention, hidden mutation, self-acceptance, hidden procedure switching, and complex body authoring by implication.
- Procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming unless an explicit exception is justified.
- Stub procedure body authoring preserves target role, workflow integration, output contract, future scope, must-not constraints, and STOP behavior until authored.
- Registry hint proposal is compact and does not replace procedure source.
- Closure uses CLOSURE_CHECK, FINISH_PACKET, and post-closed NEXT_CHAT_CARD_or_no_next_chat_needed correctly.
- CLOSURE_CHECK does not pass while a required child return is pending, missing, unverified, or required validation/evidence is absent.
- CLOSURE_CHECK fails when `repair_needed = true`, the parent cannot mutate directly, and no opened/returned/verified child call evidence exists.
- A patch plan, child-call packet, handoff, card, package, or copy-paste packet is intermediate only and not terminal parent completion.

## Stop Conditions

- target procedure is unbounded;
- requested procedure would silently mutate state;
- requested procedure crosses into unrelated body authoring without separate scope;
- required sources are missing;
- procedure keeps obsolete runbook/playbook path or naming without explicit exception;
- registry delta would leave a procedure pointing outside canonical procedure files;
- user asks to patch repository without admitted child-call or storage boundary;
- research is required but questions/evidence/source policy are not approved;
- embedded child/adaptor use would become hidden procedure switching, acceptance, mutation, or unbounded external wait;
- required repository mutation for the current START goal is identified but no `CHILD_PROCEDURE_CALL` can be opened with exact boundaries and return verification;
- required child return is missing, unverified, or cannot be matched to the emitted call.

## Procedure Closure

Close with the candidate design outputs, limitations, canonical path/registry/stub status, kind/child-call status, and exact next move.

If repository mutation is required for the current START goal, emitting the Codex child call is not completion; it opens a child call and blocks CHECK/FINISH until return verification. A patch plan may be an intermediate result, not terminal completion.

CLOSURE_CHECK may pass only after required child calls have returned and been verified, or after the selected result is explicitly blocked with exact missing child returns/validation. NEXT_CHAT_CARD is post-closed continuation only and must not carry unfinished child work from the current START goal.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md
