# 15 P9 Phase Close Interface
artifact_control:
  artifact_name: "P9_PHASE_CLOSE Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "P9_PHASE_CLOSE"
  repo_path: "workflow/stage_registry/interfaces/P9_PHASE_CLOSE_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 15 P9 Phase Close Interface

Interface version: stage-interface-v0.1 Stage ID: P9 Stage name: Phase Close Stage type: closure / state rollup

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

P9 closes a phase by summarizing outputs, checking unresolved items, updating phase state, and identifying the next route.

P9 prevents work from remaining open without a close report or explicit carry-forward.

## Public input contract

Required inputs:

*   Stage Launch Card targeting P9.
*   Phase Start Packet or Phase State reference.
*   Work outputs or result packets from the phase.
*   Acceptance status.
*   Open issue list.
*   Write authority.

Optional inputs:

*   Review Distill Packet.
*   Audit Report.
*   Human feedback.
*   Regression log.
*   Next-phase suggestion.
*   Direction State reference.

Missing-context behavior:

*   If phase state is missing, emit a Context Request Card.
*   If acceptance status is unknown, route to R1 or A1.
*   If unresolved blockers exist, route to B1 or R0.
*   If the Direction itself needs revision, route to D0.

## Public output contract

P9 emits a Stage Result Packet containing:

*   Phase Close Packet.
*   Completed outputs.
*   Acceptance status.
*   Open carry-forward items.
*   State updates.
*   Recommended next phase or stop.
*   Execution Log Entry.

Required P9 output artifacts:

*   Phase Close Packet
*   Phase State Update
*   Carry-forward List
*   Next Phase Recommendation or Stop route

## Allowed next stages

P9 may route only to:

*   P0 Phase Start
*   D0 Direction Setup
*   R1 Review Distill
*   R0 Recovery Close
*   stop

## Write targets

P9 may propose or write only to authorized phase-close targets:

*   Rebuild scenario test mode: ainazemtsau/my_global_workflow / 08 Scenario Tests / \[scenario\_id\] / Phase Close
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Phases / \[phase\_id\] / Phase Close \[runtime\_target\_root from Launch Card\] / Phases / \[phase\_id\] / Phase State \[runtime\_target\_root from Launch Card\] / Direction State
*   Execution log mode: \[authorized execution log path from Launch Card\]

P9 must not start a new phase without emitting a clear P0 Launch Card or stop route.

## Compatibility/core/extensions rules

P9 consumes and emits the shared core fields defined in 00 Stage Interface Index.

P9 may write extension fields only under:

*   extensions.P9.close\_reason
*   extensions.P9.carry\_forward\_summary
*   extensions.P9.next\_phase\_hint

Unknown extension fields must be tolerated.

## Acceptance anchors

*   P9 has a public input contract.
*   P9 has a public output contract.
*   P9 allowed next stages are defined.
*   P9 write targets are defined.
*   P9 contains no final prompt body.
