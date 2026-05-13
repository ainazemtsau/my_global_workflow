# 04 G0 Goal Select Interface
artifact_control:
  artifact_name: "G0_GOAL_SELECT Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "G0_GOAL_SELECT"
  repo_path: "workflow/stage_registry/interfaces/G0_GOAL_SELECT_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 04 G0 Goal Select Interface

Interface version: stage-interface-v0.1 Stage ID: G0 Stage name: Goal Select Stage type: goal triage / prioritization

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

G0 selects one working goal from multiple candidate goals.

G0 protects the workflow from parallel overcommitment by making selection, deferral, and rejection explicit.

## Public input contract

Required inputs:

*   Stage Launch Card targeting G0.
*   Candidate Goal List or backlog reference.
*   Direction or Phase objective.
*   Selection criteria or user priority.
*   Constraints and current state reference.
*   Freshness state.

Optional inputs:

*   Prior Capture Ledger.
*   Existing backlog.
*   Human ranking signal.
*   Deadline or urgency.
*   Dependencies between goals.

Missing-context behavior:

*   If there is only one viable substantial goal, route to G1.
*   If selection criteria are missing and choice is high-impact, emit a Human Decision Card.
*   If all candidates are too vague, route to I0 or G1 with a clarification request.

## Public output contract

G0 emits a Stage Result Packet containing:

*   Selected goal.
*   Deferred goals.
*   Rejected goals.
*   Selection rationale.
*   Priority and scope flags.
*   Next route.
*   Execution Log Entry.

Required G0 output artifacts:

*   Goal Selection Packet
*   Deferred Goal List
*   Selection Rationale
*   Next Stage Launch Card or Human Decision Card

## Allowed next stages

G0 may route only to:

*   G1 Goal Shape
*   F0 Fast Direct
*   D1 Deep Research
*   A1 Audit
*   R1 Review Distill
*   P9 Phase Close
*   R0 Recovery Close

## Write targets

G0 may propose or write only to authorized goal-selection targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Goal Selection
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Goals / Goal Options \[runtime\_target\_root from Launch Card\] / Goals / Selected Goal \[runtime\_target\_root from Launch Card\] / Backlog / Deferred Goals \[runtime\_target\_root from Launch Card\] / Decisions / Goal Selection Decision
*   Execution log mode: \[authorized execution log path from Launch Card\]

G0 must not produce a fully shaped execution brief. That belongs to G1 and E1.

## Compatibility/core/extensions rules

G0 consumes and emits the shared core fields defined in 00 Stage Interface Index.

G0 may write extension fields only under:

*   extensions.G0.selection\_method
*   extensions.G0.deferred\_goal\_reason
*   extensions.G0.priority\_basis

Unknown extension fields must be tolerated.

## Acceptance anchors

*   G0 has a public input contract.
*   G0 has a public output contract.
*   G0 allowed next stages are defined.
*   G0 write targets are defined.
*   G0 contains no final prompt body.
