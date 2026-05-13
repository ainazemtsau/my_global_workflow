# 12 C2 Codex Execute Interface
artifact_control:
  artifact_name: "C2_CODEX_EXECUTE Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "C2_CODEX_EXECUTE"
  repo_path: "workflow/stage_registry/interfaces/C2_CODEX_EXECUTE_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 12 C2 Codex Execute Interface

Interface version: stage-interface-v0.1 Stage ID: C2 Stage name: Codex Execute Stage type: Codex execution / implementation evidence

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

C2 executes an accepted Codex Wave Card and returns evidence-backed results.

C2 is the execution-facing stage boundary. It must not claim completion without file read-back / diff verification / commit verification, tests, or evidence appropriate to the task.

## Public input contract

Required inputs:

*   Stage Launch Card targeting C2 or accepted Codex Wave Card.
*   Codex Wave Card Contract reference.
*   Target repository, GitHub repository root, or authorized write scope.
*   Exact allowed actions.
*   Exact forbidden paths.
*   Validator expectations.
*   Evidence requirements.
*   Rollback expectations.

Optional inputs:

*   Prior C1 graph plan.
*   Existing patch context.
*   Known failing tests.
*   Human apply approval.
*   Codex environment limitations.

Missing-context behavior:

*   If write authority is missing, emit a Context Request Card.
*   If validation expectations are missing, route to C1, E1, or A1.
*   If target access is unavailable, return blocked.
*   If partial writes occur and safe correction is unclear, route to R0.

## Public output contract

C2 emits a Stage Result Packet or Codex Return Packet containing:

*   Final state: done, partial, blocked, or stuck.
*   Files or notes changed.
*   Patch summary.
*   Tests run.
*   Evidence and file read-back / diff verification / commit verification results.
*   Known limitations.
*   Rollback notes.
*   Next route.
*   Execution Log Entry.

Required C2 output artifacts:

*   Codex Return Packet
*   Patch Summary
*   Evidence Register
*   Validator Result
*   Read-back Result when GitHub repository or persistent notes are modified
*   Next Stage Launch Card or Recovery Close Packet

## Allowed next stages

C2 may route only to:

*   R1 Review Distill
*   P9 Phase Close
*   B1 Problem
*   C1 Codex Graph Plan
*   E1 Execution Brief
*   R0 Recovery Close

## Write targets

C2 may write only to explicitly authorized Codex execution targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Codex Execute Result
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Codex / \[wave\_id\] / Codex Return Packet \[runtime\_target\_root from Launch Card\] / Codex / \[wave\_id\] / Evidence
*   Codex bridge mode: \[authorized Codex wave record path from Launch Card\]
*   Repository mode: \[authorized repository paths from Codex Wave Card\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

C2 must not write outside explicit authorization and must not overwrite old active Workflow vNext material.

## Compatibility/core/extensions rules

C2 consumes and emits the shared core fields defined in 00 Stage Interface Index and the accepted Codex Bridge contracts.

C2 may write extension fields only under:

*   extensions.C2.execution\_environment
*   extensions.C2.validator\_output
*   extensions.C2.rollback\_notes

Unknown extension fields must be tolerated.

## Acceptance anchors

*   C2 has a public input contract.
*   C2 has a public output contract.
*   C2 allowed next stages are defined.
*   C2 write targets are defined.
*   C2 contains no final prompt body.
