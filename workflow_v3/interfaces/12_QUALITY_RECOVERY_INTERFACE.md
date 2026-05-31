# Quality and Recovery Interface

status: active_interface_layer

## Purpose

This interface defines interface-level quality gates and recovery outcomes.

## Quality gates

| Gate | Checks |
| --- | --- |
| source/context gate | Exact source authority, read completeness, cache classification, missing-source visibility. |
| entity coverage gate | Every registry entity has definition, storage if any, signals/handlers/packets where relevant, mutation rights, and recovery coverage. |
| direction lifecycle gate | Lifecycle transitions are signal/handler/closure/acceptance visible and candidate until accepted. |
| scope gate | Work has bounded target, allowed/forbidden surfaces, and no unrelated continuation. |
| evidence gate | Result claims are backed by validation/evidence or explicit no-evidence limitation. |
| acceptance gate | Candidate result remains candidate until explicit Acceptance Decision/update path. |
| signal/handler misuse gate | Signal is fact only, Handler candidate only, Action Inbox candidate only. |
| progression router misuse gate | One primary next move, no hidden launches, no chat-intuition routing. |
| chat lifecycle/handoff gate | Child/parent/next chat boundaries and return destinations are explicit. |
| Codex validation gate | Branch, commit/diff, changed files, allowed paths, forbidden paths, validation, EOF markers, refresh report. |
| Project setup refresh gate | Project UI, Project Files/Sources, request-only refresh, and do-not-upload status are reported separately. |
| rollback/coexistence gate | Old Workflow OS is not deleted, renamed, moved, decommissioned, or weakened. |

## Recovery outcomes

Use the smallest sufficient recovery outcome:

- `blocked result` - stop when source, scope, permission, validation, lifecycle, or acceptance is missing.
- `same-package repair` - repair within current allowed scope when validation fails.
- `human decision request` - request judgment, acceptance, permission, or scope decision.
- `rollback/revert` - undo or reject a candidate change when it violated boundaries or cannot be repaired safely.
- `future package split` - park real but out-of-scope work for a later explicit package.

## Hard rules

- No validation means no done claim.
- No hidden state change.
- Candidate docs remain design evidence only.
- Legacy files remain `legacy_evidence` unless imported through explicit process.
- A blocked lifecycle transition blocks product work until resolved or split.

END_OF_FILE: workflow_v3/interfaces/12_QUALITY_RECOVERY_INTERFACE.md
