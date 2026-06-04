# Recovery Review Procedure

status: active_procedure

## Purpose

Use `recovery_review` when runtime state, acceptance state, routing, evidence, or persistence may be suspect.

This procedure reviews and classifies recovery needs. It must not repair any runtime files unless a later storage update adapter package is admitted.

## Trigger / When to Use

- Runtime state, acceptance state, routing, evidence, or persistence may be contaminated, missing, stale, or conflicting.
- A prior run, Codex result, check job, Signal, Handler, or closure result may be incomplete or unsafe to rely on.
- The user asks to classify recovery need before repair, acceptance, rollback, or storage work.

## When Not to Use

- Do not use to mutate runtime files.
- Do not use to repair repository/runtime state directly.
- Do not use to invent Direction proof state.
- Do not use to retroactively accept state without explicit record.
- Do not use old workflow/runtime evidence as accepted v3 state without accepted import/bridge policy.
- Do not use for product execution.

## Required Inputs

- suspect state refs;
- evidence refs;
- source locks or exact source paths/refs;
- recovery question;
- affected decisions and paths if known;
- relevant legacy boundary or import policy if legacy evidence is involved.

## Source Requirements

Read exact suspect state and evidence required for the recovery question. Verify source integrity and EOF markers where they exist. Classify legacy material as `legacy_evidence` unless an explicit accepted import/bridge policy says otherwise.

Do not infer accepted state from chat memory, Project Files/Sources cache, candidate docs, or old workflow/runtime evidence.

## Context Classification

Classify each input as canonical repository source, accepted record, adapter evidence, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

Recovery claims must name source limitations and unresolved authority gaps.

## Complexity Selector

- `standard`: default for bounded recovery review.
- `checkpointed`: use when suspected contamination scope or affected paths require user confirmation.
- `delegated_or_tool_mediated`: only for proposing a later check job, Codex handoff, or storage update path; do not launch it.
- `research_backed`: not used.

## Stage Cards

```text
stage_id: recovery_fit
purpose: Confirm the issue is recovery review, not repair, storage update, acceptance, or product work.
activation conditions: Always.
inputs: Recovery question and requested outcome.
required intermediate output: Recovery scope and non-goals.
gate: PASS if review is bounded and non-mutating; STOP if user requests direct repair, mutation, acceptance, or product execution.
checkpoint rule: Checkpoint when user intent could imply repair or acceptance.
expansion rule: Request clarification only to separate review from repair/acceptance.
stop behavior: Return boundary blocker.
```

```text
stage_id: suspect_source_frame
purpose: Read and classify suspect state refs, evidence refs, source locks, and legacy boundaries.
activation conditions: recovery_fit passes.
inputs: Suspect refs, evidence refs, source locks, legacy/import policy.
required intermediate output: Source frame, authority classification, read limitations.
gate: PASS if required evidence is available and authority is clear; STOP if required evidence is missing or source authority is unclear.
checkpoint rule: Checkpoint when suspected affected scope is ambiguous.
expansion rule: Request or inspect exact sources only within the recovery question.
stop behavior: Return blocked_context_request.
```

```text
stage_id: contamination_classification
purpose: Classify missing proof, stale source, conflicting state, legacy contamination, acceptance ambiguity, validation failure, or routing contamination.
activation conditions: suspect_source_frame passes.
inputs: Source frame and recovery question.
required intermediate output: Contamination classification and affected decisions/paths.
gate: PASS if classification is supported; PASS_WITH_RISK if classification is bounded but incomplete; STOP if classification would require invented proof state.
checkpoint rule: Checkpoint when affected paths or decisions need user confirmation.
expansion rule: Propose a bounded check job only when evidence question is separate and specific.
stop behavior: Return source limitations and blocked recovery status.
```

```text
stage_id: recovery_outcome
purpose: Propose one recovery outcome and exact next move.
activation conditions: contamination_classification passes or passes with risk.
inputs: Classification, allowed outcomes, storage/acceptance boundaries.
required intermediate output: Recovery review output contract.
gate: PASS only if outcome does not mutate or accept state by itself.
checkpoint rule: None by default.
expansion rule: Propose later check/Codex/storage path only as a candidate next move.
stop behavior: Return blocked_context_request and exact missing source/decision.
```

## Gate Outcomes

- `PASS`: recovery review is bounded, sourced, and non-mutating.
- `PASS_WITH_RISK`: classification is useful but incomplete limitations are explicit.
- `REWORK`: revise scope, source frame, or classification before outcome.
- `EXPAND`: request exact source or propose bounded later check/Codex/storage path without launching it.
- `STOP`: block when required evidence is missing, source authority is unclear, or user requests mutation/acceptance.
- `TRANSFER`: return candidate next move or Transition Packet for separate repair, acceptance, rollback, check job, Codex handoff, or storage update.

## Optional Expansion

Allowed expansion is limited to exact source inspection or proposing a later bounded check job, Codex handoff, or storage update path. Expansion must not repair, mutate, accept, import, or persist state.

## Research Policy

External research is forbidden. Exact repository/runtime/evidence sources are required. Legacy evidence may be classified only as `legacy_evidence` unless explicit accepted import/bridge policy exists.

## Checkpoint Policy

No checkpoint is required by default. Checkpoint when suspected affected scope is ambiguous or a user decision is needed before proposing repair, rollback, acceptance, or storage path.

## Output Contract

```text
recovery_review_status:
suspect_state_refs:
evidence_refs:
source_read_limitations:
outcome:
storage_update_needed:
exact_next_move:
```

Allowed `outcome` values:

```text
accept_retroactively_with_explicit_record
supersede_record
rollback_patch_needed
repair_required
blocked_context_request
```

## Eval / Quality Checks

- Exact suspect state and evidence were read or limitations are stated.
- Source authority and legacy boundaries are classified.
- Recovery outcome is one of the allowed outcomes.
- Review does not mutate files, accept state, import legacy evidence, or repair runtime state directly.
- Next move is a candidate/admitted-path recommendation, not hidden execution.

## Stop Conditions

- required source or evidence is missing;
- source authority is unclear;
- recovery would require direct write or repair;
- acceptance authority is unclear;
- user requests retroactive acceptance without explicit record;
- legacy evidence would be used as accepted v3 state without accepted import/bridge policy;
- procedure would invent Direction proof state.

## Procedure Closure

Recovery review produces candidate outcome only. It does not repair, mutate, accept, import, or persist.

If lifecycle FINISH is active, close through FINISH_REQUEST, Result Packet, and Event Loop Closure.

END_OF_FILE: workflow_v3/procedures/RECOVERY_REVIEW_PROCEDURE.md
