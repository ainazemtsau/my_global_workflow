# Procedure Authoring and Integration Procedure

status: active_procedure

## Purpose

Use this procedure to design or revise Workflow v3 procedure definitions and their registry/eval integration.

This procedure is non-mutating. It produces candidate definitions, patch plans, and integration proposals only.

## Trigger / When to Use

- User asks to create a new Workflow v3 procedure.
- User asks to revise an existing procedure.
- User asks to migrate a procedure into the new procedure-definition framework.
- User asks to integrate a procedure into Workflow v3 registry/control-plane setup.

## When Not to Use

- Do not use to execute the procedure being authored.
- Do not use to mutate repository directly.
- Do not use to accept candidate output.
- Do not use to update actual ChatGPT Project UI.
- Do not use to migrate complex formation/entity procedures unless separately scoped.

## Required Inputs

- target procedure name or intent;
- target run surface or candidate run surface;
- expected trigger;
- expected output;
- known boundaries;
- source files to inspect;
- requested integration scope.

For migrations from an old runbook/playbook/operational path, also require:

```text
old_source_path:
current_registry_entrypoint:
current_registry_procedure_ref:
proposed_new_procedure_path:
legacy_file_disposition: delete | archive | compatibility_shim
canonical_path_exception_if_any:
```

## Source Requirements

Read exact relevant Workflow v3 framework, registry, control-plane, eval, and existing procedure sources needed for the requested design scope. Verify EOF where markers exist. Treat Project Files/Sources and chat memory as cache/context only.

## Context Classification

Classify inputs as canonical repository source, current human input, candidate context, verified excerpt, Project Files cache/context, legacy_evidence, or unknown/unverified.

## Complexity Selector

- `standard`: default for bounded procedure design or revision.
- `checkpointed`: use when the design boundary, registry mapping, canonical path/naming, legacy file disposition, or eval plan needs user review before final proposal.
- `research_backed`: use only when current external documentation is explicitly needed.
- `delegated_or_tool_mediated`: use only to prepare a bounded handoff/check plan, not to launch it.

## Canonical Location and Naming Policy

New Procedure Definition Framework procedures must live under:

```text
workflow_v3/procedures/**
```

New or migrated procedure files must use procedure naming:

```text
*_PROCEDURE.md
```

When migrating an old runbook/playbook/operational source into the Procedure Definition Framework:

- do not keep the controlling procedure source under `workflow_v3/runbooks/**` merely because the pre-migration registry pointed there;
- do not keep `*_RUNBOOK.md` or `*_PLAYBOOK.md` naming merely to reduce path churn;
- propose a canonical `workflow_v3/procedures/*_PROCEDURE.md` target path;
- propose a registry delta so `procedure_ref` points to the canonical migrated procedure file;
- propose disposition for the old file: `delete`, `archive`, or explicitly bounded `compatibility_shim`;
- mark any non-canonical location or naming as an exception requiring explicit justification.

Existing registry entries may temporarily point to legacy runbook/formation paths only while those entries are not yet migrated. That coexistence is not precedent for migrated procedures.

## Stage Cards

### Fit and Scope

```text
stage_id: fit_and_scope
purpose: Confirm the requested procedure is bounded and belongs in Workflow v3.
activation conditions: Always.
inputs: Target intent, trigger, expected output, known boundaries.
required intermediate output: Scope statement and non-goals.
gate: PASS if bounded; STOP if unbounded or mutation/acceptance is hidden.
checkpoint rule: Checkpoint only if scope is ambiguous.
expansion rule: Ask for missing scope or inspect named sources.
stop behavior: Return blocked scope result.
```

### Existing Workflow Fit

```text
stage_id: existing_workflow_fit
purpose: Map the candidate procedure to existing registry, lifecycle, run surface, and eval rules.
activation conditions: Always.
inputs: Relevant control-plane and procedure sources.
required intermediate output: Fit notes and conflicts.
gate: PASS if compatible; REWORK if wording conflicts; STOP if required sources are missing.
checkpoint rule: None by default.
expansion rule: Inspect only exact relevant sources.
stop behavior: Return source or compatibility blocker.
```

### Canonical Location and Registry Fit

```text
stage_id: canonical_location_and_registry_fit
purpose: For new or migrated procedures, select canonical file path/naming and registry mapping before drafting.
activation conditions: Always for new procedures and migrations; optional for same-path revisions that are already canonical.
inputs: Procedure Definition Canon, Procedure Authoring Guide, Procedure Registry, old source path if any, current procedure_ref if any.
required intermediate output: Canonical path decision, registry delta need, and old-file disposition plan.
gate: PASS if the controlling procedure path is under workflow_v3/procedures/** with *_PROCEDURE.md naming; REWORK if a migration preserves runbook/playbook naming without explicit exception; STOP if registry mapping would remain ambiguous.
checkpoint rule: Checkpoint when changing path, deleting/archiving old files, or using a compatibility shim.
expansion rule: Inspect exact registry/source references only; do not infer migration policy from stale Project Files or chat memory.
stop behavior: Return canonical path or registry blocker.
```

### Procedure Draft

```text
stage_id: procedure_draft
purpose: Produce the candidate procedure definition or revision plan.
activation conditions: Fit gate and canonical_location_and_registry_fit gate passed.
inputs: Procedure canon, template, guide, existing source if revising.
required intermediate output: Candidate procedure definition or patch plan.
gate: PASS if it has specific purpose, triggers, sources, stages, gates, outputs, stops, and canonical path/registry disposition.
checkpoint rule: Checkpoint for complex or high-impact procedure design.
expansion rule: Use Procedure Definition Eval as a check.
stop behavior: Return rework notes.
```

### Registry Delta

```text
stage_id: registry_delta
purpose: Propose compact registry entry and run_surface_type mapping.
activation conditions: Integration scope includes registry or canonical path/naming migration changes procedure_ref.
inputs: Procedure draft, canonical path decision, Procedure Registry.
required intermediate output: Registry entry proposal.
gate: PASS if one entrypoint is selected with a short selection hint and procedure_ref points to the canonical procedure path after migration; REWORK if the registry would keep a migrated procedure pointed at an obsolete runbook/playbook path; STOP if multiple independent entrypoints are needed.
checkpoint rule: None by default.
expansion rule: Propose SPLIT_REQUIRED when multiple independent entrypoints are needed.
stop behavior: Return routing conflict.
```

### Eval Plan

```text
stage_id: eval_plan
purpose: Propose definition and execution eval checks for the procedure.
activation conditions: Integration scope includes evals or procedure is non-trivial.
inputs: Procedure draft and eval sources.
required intermediate output: Eval proposal.
gate: PASS if checks can catch boundary, source, gate, checkpoint, closure, canonical path/naming, and registry mapping failures.
checkpoint rule: None by default.
expansion rule: Add check job proposal only when validation question is bounded.
stop behavior: Return missing eval coverage.
```

### Integration Plan

```text
stage_id: integration_plan
purpose: Identify run surface compatibility and any future Codex/storage handoff boundary.
activation conditions: Always.
inputs: Registry delta, canonical path decision, legacy file disposition plan, run surface contract, requested integration scope.
required intermediate output: Run surface compatibility statement and allowed/forbidden path proposal if needed.
gate: PASS if integration is non-mutating and bounded; TRANSFER if a separate admitted handoff is needed.
checkpoint rule: Checkpoint before any proposed repository mutation package.
expansion rule: Prepare handoff candidate only when separately requested and bounded.
stop behavior: Return admission blocker.
```

### Closure

```text
stage_id: closure
purpose: Return the candidate design and next move.
activation conditions: Always after completed or stopped stages.
inputs: Stage outputs.
required intermediate output: Result Packet and Next Move Packet.
gate: PASS if required outputs are present; PASS_WITH_RISK if limitations are named.
checkpoint rule: None.
expansion rule: None.
stop behavior: Return blocked result and exact source/scope need.
```

## Gate Outcomes

Use `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, and `TRANSFER`. `TRANSFER` is limited to candidate handoff/update paths; it does not launch them.

## Optional Expansion

Allowed expansion is limited to exact source inspection, bounded eval/check planning, or a candidate Codex/storage handoff when separately requested and bounded.

## Research Policy

Research is forbidden by default. Use external research only when the user asks for current outside documentation and the question remains non-state-mutating.

## Checkpoint Policy

No checkpoint is required for simple bounded procedure edits that remain canonical. Checkpoint when scope, registry mapping, canonical path/naming, legacy file disposition, complex eval design, or future mutation boundaries are ambiguous.

## Output Contract

```text
candidate_procedure_definition_or_patch_plan:
canonical_location_and_legacy_disposition:
registry_entry_proposal:
run_surface_compatibility_statement:
eval_proposal:
allowed_forbidden_path_proposal_if_codex_or_storage_needed:
result_packet:
next_move_packet:
```

## Eval / Quality Checks

- Procedure has distinguishable trigger and non-trigger.
- Required inputs and exact source requirements are explicit.
- Stage Cards produce intermediate outputs and use material gates.
- Stop conditions prevent invention, hidden mutation, self-acceptance, and complex formation migration by implication.
- New or migrated procedures use canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming unless an explicit exception is justified.
- Migrated procedures include registry delta and old-file disposition.
- Registry hint proposal is compact and does not replace procedure source.
- Closure uses FINISH_REQUEST, FINISH_PACKET, Result Packet, and Next Move Packet correctly.

## Stop Conditions

- target procedure is unbounded;
- requested procedure would silently mutate state;
- requested procedure crosses into complex formation migration without separate scope;
- required sources are missing;
- migrated procedure keeps obsolete runbook/playbook path or naming without explicit exception;
- registry delta would leave a migrated procedure pointing to an obsolete controlling source;
- user asks to patch repository without Codex/storage admission.

## Procedure Closure

Close with the candidate design outputs, limitations, canonical path/registry/legacy-file disposition, and exact next move. If repository changes are needed later, return a bounded handoff/update proposal rather than applying changes inside this procedure.

END_OF_FILE: workflow_v3/procedures/PROCEDURE_AUTHORING_AND_INTEGRATION_PROCEDURE.md
