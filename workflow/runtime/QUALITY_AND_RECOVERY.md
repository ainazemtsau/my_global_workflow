# Workflow v3 Quality and Recovery

status: active_skeleton

## Core rules

No hidden state change.

No validation means no done claim.

Chat output, Codex output, Project Files/Sources, Signals, Handler results, Action Inbox items, Check Jobs, and document existence do not create accepted state.

## Context/source gate

Checks:

- source authority is identified;
- exact repo/path/ref is known when exact state matters;
- read completeness and limitations are stated;
- Project Files/Sources are classified as cache/context;
- missing or stale source is visible.

Fails when required source is missing, stale cache is treated as truth, or repository state is guessed.

## Scope gate

Checks:

- work has one bounded target;
- in-scope and out-of-scope boundaries are explicit;
- allowed and forbidden paths/surfaces are known;
- no unrelated continuation or phase jump occurs.

Fails when scope expands, mixes independent jobs, or requires forbidden surfaces.

## Evidence gate

Checks:

- expected evidence is defined;
- result includes evidence or an explicit no-evidence reason;
- validation output supports the claim;
- conflicting evidence is named.

Fails when a done claim lacks validation or evidence.

## Acceptance gate

Checks:

- result remains candidate unless explicitly accepted;
- Acceptance Decision is separate and visible;
- no adapter accepts its own output;
- human action is not assumed complete without confirmation.

Fails when acceptance is inferred or hidden.

## Codex validation gate

Checks:

- branch name;
- commit SHA when committed;
- changed files;
- allowed paths only;
- forbidden paths unchanged;
- validation results;
- EOF markers for Markdown;
- residual risks;
- project refresh requirements.

Fails when Codex changes forbidden paths, omits evidence, returns unverifiable changes, or claims done after failed validation.

## Project setup refresh gate

Checks:

- Project Instructions UI update requirement is reported separately;
- Project Files/Sources refresh requirement is reported separately;
- request-only source refresh requirement is reported separately;
- do-not-upload sources are identified;
- actual Project updates are not implied by repository commits.

Fails when a file change implies a Project UI update or Project Files/Sources refresh without a separate authorized rollout package.

## Rollback/coexistence gate

Checks:

- current Workflow OS remains available as legacy/rollback;
- old files are not deleted, renamed, moved, or decommissioned;
- non-adopted Directions remain under the old Workflow OS;
- rollback path is not weakened.

Fails when a package silently replaces old Workflow OS behavior or old Direction state.

## Recovery outcomes

Use the smallest sufficient recovery outcome.

`blocked result` - return when work cannot safely continue because source, scope, permission, validation, or acceptance is missing.

`same-package repair` - repair within the same allowed scope when validation failed and the repair does not need broader authority.

`human decision request` - ask for a decision when safe progress depends on judgment, acceptance, scope, permission, or credentials.

`rollback/revert` - undo or reject a candidate change when it violated boundaries or cannot be repaired safely.

`future package split` - park work for a later explicit package when the need is real but outside current scope.

END_OF_FILE: workflow/runtime/QUALITY_AND_RECOVERY.md
