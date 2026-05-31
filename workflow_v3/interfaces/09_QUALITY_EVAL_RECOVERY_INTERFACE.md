# Quality, Evaluation, and Recovery Interface

status: active_interface_layer

## Purpose

This file defines Workflow v3 quality gates, evaluation boundaries, and recovery paths.

## Owner/surface

Owner/surface: source/context gate, scope gate, evidence gate, acceptance gate, Signal/Handler misuse gate, Progression Router misuse gate, Codex validation gate, Project setup refresh gate, rollback/coexistence gate, and recovery outcomes.

## Persistence target

Persistence target: `workflow_v3/interfaces/09_QUALITY_EVAL_RECOVERY_INTERFACE.md` for shared rules; future adopted Direction recovery records belong under `directions_v3/<direction-id>/runtime/operations/**` after explicit adoption and acceptance.

## Gates

Source/context gate checks source authority, exact repo/path/ref, read completeness, cache/context classification, and stale context visibility.

Scope gate checks bounded target, in-scope and out-of-scope boundaries, allowed and forbidden paths/surfaces, and no unrelated continuation.

Evidence gate checks expected evidence, validation output, limitations, and conflicting evidence.

Acceptance gate checks candidate-state separation, explicit Acceptance Decision, no adapter self-acceptance, and no unconfirmed human action.

Signal/Handler misuse gate checks that Signals remain event/fact records, Handlers create candidate output only, Action Inbox/Q stores candidate actions, Check Jobs remain bounded verification, and Event Loop Closure appears after material work/review.

Progression Router misuse gate checks closure sequencing, one `primary_next_move`, complete transfer packet when needed, Codex return path, no hidden roadmap, and no continuation after blocking signal.

Codex validation gate checks branch name, base SHA, commit SHA when committed, changed files, allowed paths only, forbidden paths unchanged, validation results, EOF markers, residual risks, and project refresh requirements.

Project setup refresh gate checks Project Instructions UI update requirement, Project Files/Sources refresh requirement, request-only source refresh requirement, do-not-upload sources, payload counts when needed, and no implied actual Project update.

Rollback/coexistence gate checks current Workflow OS availability, old files not deleted/renamed/moved/decommissioned, non-adopted Directions under old Workflow OS, and rollback path not weakened.

## Recovery outcomes

`blocked result` returns when safe progress is impossible because source, scope, permission, validation, or acceptance is missing.

`same-package repair` repairs inside the same allowed scope when validation failed and repair does not need broader authority.

`human decision request` asks for a decision when progress depends on judgment, acceptance, scope, permission, credentials, or external action.

`rollback/revert` rejects or undoes a candidate change when it violated boundaries or cannot be repaired safely.

`future package split` parks real work for a later explicit package when outside current scope.

## Validation evidence requirements

A validation report must state:

- source authority and read completeness;
- changed files;
- allowed paths and forbidden paths;
- EOF marker status for Markdown;
- checks run and results;
- Project refresh categories;
- adoption/import/project-update/decommission boundaries;
- contradictions found or none found;
- unresolved questions;
- residual risks.

## Inputs

Inputs are Work Contracts, source reads, Result Packets, Evidence, validation outputs, Acceptance Decisions, Signals, Handler Results, Progression Router output, Codex returns, Project setup reports, and rollback/coexistence context.

## Outputs

Outputs are pass/fail gate findings, blocked results, repair Next Moves, Check Jobs, human decision requests, rollback/revert recommendations, future package splits, and validation evidence.

## State mutation rights

Quality/eval findings do not mutate accepted state.

Recovery may authorize a candidate repair or rollback path only through the applicable acceptance/update, repository-maintenance, or human decision process.

## Allowed producers

Allowed producers are parent review chats, Check Jobs, Codex result verification, CI/validation tools, human reviewers, Event Loop Closure, and quality/eval packages.

## Allowed consumers

Allowed consumers are Acceptance review, Work Contract repair, Codex package repair, Project setup rollout, adoption review, Runtime Console, and Progression Router.

## Validation/evidence requirement

Gate decisions must cite evidence or state explicit limitations. A done claim requires validation evidence sufficient for the claim.

## Forbidden behaviors

- Passing a gate with missing required evidence.
- Treating failed validation as done.
- Hiding blocker signals.
- Treating Project refresh as implied.
- Treating rollback/coexistence as optional when legacy surfaces are touched.
- Repairing by expanding scope into forbidden surfaces.
- Using quality checks to accept state without Acceptance Decision.

## Failure/recovery path

Use the smallest sufficient recovery outcome.

If a gate fails inside allowed scope, repair and revalidate.

If a gate fails because the package lacks authority, stop with a blocked result, Context Request, human decision request, or future package split.

If a candidate change violates a hard boundary, recommend rollback/revert or reject the candidate.

## Dependencies

- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/STORAGE_LAYOUT.md`

END_OF_FILE: workflow_v3/interfaces/09_QUALITY_EVAL_RECOVERY_INTERFACE.md
