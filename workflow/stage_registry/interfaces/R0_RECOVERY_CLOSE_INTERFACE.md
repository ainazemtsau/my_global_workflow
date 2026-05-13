# 16 R0 Recovery Close Interface
artifact_control:
  artifact_name: "R0_RECOVERY_CLOSE Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "R0_RECOVERY_CLOSE"
  repo_path: "workflow/stage_registry/interfaces/R0_RECOVERY_CLOSE_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 16 R0 Recovery Close Interface

Interface version: stage-interface-v0.1 Stage ID: R0 Stage name: Recovery Close Stage type: recovery / containment / repair closure

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

R0 contains failed installs, confused outputs, partial writes, corrupted state, invalid routes, or uncontrolled changes.

R0 closes the failed attempt safely before any retry. It does not patch forward from a confused install.

## Public input contract

Required inputs:

*   Stage Launch Card targeting R0 or Recovery Close trigger.
*   Failure description.
*   Last known valid state.
*   Failed output, failed install packet, or corrupted state evidence.
*   Write authority.
*   Boundary of affected notes, files, or state.
*   Desired outcome: diagnose, mark stale, quarantine, rollback guidance, or retry launch.

Optional inputs:

*   Codex Install Result Packet.
*   Audit Report.
*   Human manual check result.
*   Draft amendment path.
*   Prior recovery attempt.
*   Rollback plan.

Missing-context behavior:

*   If affected write scope is unknown, stop and emit a Context Request Card.
*   If partial writes occurred and file read-back / diff verification / commit verification is unavailable, return NEEDS\_INPUT.
*   If deletion is requested without explicit approval, refuse deletion and propose mark\_stale or quarantine.
*   If active Workflow vNext may have been touched, escalate to Human Decision Card.

## Public output contract

R0 emits a Recovery Close Packet containing:

*   Failure summary.
*   Last known valid state.
*   Affected scope.
*   Damage assessment.
*   Notes to mark stale or quarantine.
*   Repair or retry recommendation.
*   Required human checks.
*   Stop or retry route.
*   Execution Log Entry.

Required R0 output artifacts:

*   Recovery Close Packet
*   Damage Assessment
*   Stale / Quarantine Plan
*   Retry Launch Card or Stop route

## Allowed next stages

R0 may route only to:

*   retry\_previous\_stage
*   P0 Phase Start
*   G1 Goal Shape
*   E1 Execution Brief
*   C1 Codex Graph Plan
*   P9 Phase Close
*   stop

## Write targets

R0 may propose or write only to authorized recovery targets:

*   Rebuild draft amendment mode: Workflow / 20 Workflow vNext-R REBUILD / 10 Draft Amendments / Failed Installs Workflow / 20 Workflow vNext-R REBUILD / 10 Draft Amendments / Recovery Notes
*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Recovery Close
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Recovery / \[recovery\_id\] / Recovery Close Packet \[runtime\_target\_root from Launch Card\] / Recovery / \[recovery\_id\] / Damage Assessment
*   Execution log mode: \[authorized execution log path from Launch Card\]

R0 may mark stale or superseded only when explicit write authority names the affected path. R0 must not physically delete notes unless explicit human approval is present.

## Compatibility/core/extensions rules

R0 consumes and emits the shared core fields defined in 00 Stage Interface Index and the Recovery Close Packet Template.

R0 may write extension fields only under:

*   extensions.R0.failure\_class
*   extensions.R0.quarantine\_method
*   extensions.R0.retry\_constraints

Unknown extension fields must be tolerated.

## Acceptance anchors

*   R0 has a public input contract.
*   R0 has a public output contract.
*   R0 allowed next stages are defined.
*   R0 write targets are defined.
*   R0 contains no final prompt body.
