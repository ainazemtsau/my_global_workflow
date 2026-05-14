# 03 I0 Capture Interface
artifact_control:
  artifact_name: "I0_CAPTURE Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "I0_CAPTURE"
  repo_path: "workflow/stage_registry/interfaces/I0_CAPTURE_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 03 I0 Capture Interface

Interface version: stage-interface-v0.1 Stage ID: I0 Stage name: Capture Stage type: intake / triage

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

I0 captures raw user material, separates signal from noise, identifies candidate goals, and routes to the smallest safe next stage.

I0 does not solve large tasks by default. It structures incoming material so a later stage can act safely.

## Public input contract

Required inputs:

*   Stage Launch Card targeting I0.
*   Raw user material, transcript, notes, request, or imported context.
*   Current Direction or Phase state reference when available.
*   Freshness state for provided material.
*   Constraints and do-not-touch rules.
*   Requested output shape.

Optional inputs:

*   Existing Capture Ledger.
*   Backlog reference.
*   User priority.
*   Attachment index.
*   Known target stage preference.

Missing-context behavior:

*   If the raw material is insufficient to identify an ask, emit a Context Request Card.
*   If the material contains a clear narrow task, route to F0.
*   If the material contains multiple possible goals, route to G0.
*   If the material contains one substantial goal, route to G1.

## Public output contract

I0 emits a Stage Result Packet containing:

*   Capture Ledger.
*   Extracted facts.
*   User asks.
*   Candidate goals.
*   Constraints.
*   Context gaps.
*   Noise or out-of-scope material.
*   Recommended next route.
*   Execution Log Entry.

Required I0 output artifacts:

*   Capture Ledger
*   Candidate Goal List
*   Context Gap List
*   Next Stage Launch Card or Context Request Card

## Allowed next stages

I0 may route only to:

*   G0 Goal Select
*   G1 Goal Shape
*   F0 Fast Direct
*   D1 Deep Research
*   A1 Audit
*   B1 Problem
*   R1 Review Distill
*   P9 Phase Close
*   R0 Recovery Close

## Write targets

I0 may propose or write only to authorized capture targets:

*   Rebuild scenario test mode: ainazemtsau/my_global_workflow / 08 Scenario Tests / \[scenario\_id\] / Capture Ledger
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Inbox / \[capture\_id\] \[runtime\_target\_root from Launch Card\] / Captures / \[capture\_id\] / Capture Ledger \[runtime\_target\_root from Launch Card\] / Backlog / Candidate Goals
*   Execution log mode: \[authorized execution log path from Launch Card\]

I0 must not make durable decisions that belong to G0, G1, S3, or a human decision card.

## Compatibility/core/extensions rules

I0 consumes and emits the shared core fields defined in 00 Stage Interface Index.

I0 may write extension fields only under:

*   extensions.I0.capture\_source\_type
*   extensions.I0.noise\_summary
*   extensions.I0.attachment\_index

Unknown extension fields must be tolerated.

## Acceptance anchors

*   I0 has a public input contract.
*   I0 has a public output contract.
*   I0 allowed next stages are defined.
*   I0 write targets are defined.
*   I0 contains no final prompt body.
