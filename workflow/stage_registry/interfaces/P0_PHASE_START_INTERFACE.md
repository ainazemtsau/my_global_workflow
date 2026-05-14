# 02 P0 Phase Start Interface
artifact_control:
  artifact_name: "P0_PHASE_START Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "P0_PHASE_START"
  repo_path: "workflow/stage_registry/interfaces/P0_PHASE_START_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 02 P0 Phase Start Interface

Interface version: stage-interface-v0.1 Stage ID: P0 Stage name: Phase Start Stage type: phase initialization

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

P0 starts a bounded phase inside an existing Direction.

A phase has an objective, scope boundary, working context, expected outputs, and closure condition.

## Public input contract

Required inputs:

*   Stage Launch Card targeting P0.
*   Direction Charter or Direction State reference.
*   Phase intent, backlog item, user request, or trigger.
*   Current phase state, if any.
*   Known constraints and freshness state.
*   Write authority and runtime target root.

Optional inputs:

*   Prior phase close packet.
*   Candidate goals.
*   Existing backlog.
*   Human deadline or priority.
*   Codex availability flag.

Missing-context behavior:

*   If Direction context is missing, request D0 or emit Context Request Card.
*   If phase objective is too vague to start, route to I0 or G1.
*   If the user asks for immediate execution and the task is narrow, route to F0.

## Public output contract

P0 emits a Stage Result Packet containing:

*   Phase Start Packet.
*   Phase objective.
*   Phase boundary and non-goals.
*   Initial phase state.
*   Suggested first working stage.
*   Execution Log Entry.
*   Next Stage Launch Card or Context Request Card.

Required P0 output artifacts:

*   Phase Start Packet
*   Phase State seed or update
*   Phase Boundary Statement
*   Next Stage Launch Card

## Allowed next stages

P0 may route only to:

*   I0 Capture
*   G0 Goal Select
*   G1 Goal Shape
*   F0 Fast Direct
*   D1 Deep Research
*   A1 Audit
*   C1 Codex Graph Plan
*   P9 Phase Close
*   R0 Recovery Close

## Write targets

P0 may propose or write only to authorized Phase targets:

*   Rebuild scenario test mode: ainazemtsau/my_global_workflow / 08 Scenario Tests / \[scenario\_id\] / Phase Start
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Phases / \[phase\_id\] / Phase Start \[runtime\_target\_root from Launch Card\] / Phases / \[phase\_id\] / Phase State \[runtime\_target\_root from Launch Card\] / Phases / \[phase\_id\] / Phase Log
*   Execution log mode: \[authorized execution log path from Launch Card\]

P0 must not create final stage prompts or alter old active Workflow vNext material.

## Compatibility/core/extensions rules

P0 consumes and emits the shared core fields defined in 00 Stage Interface Index.

P0 may write extension fields only under:

*   extensions.P0.phase\_type
*   extensions.P0.phase\_priority
*   extensions.P0.phase\_start\_rationale

Unknown extension fields must be tolerated.

## Acceptance anchors

*   P0 has a public input contract.
*   P0 has a public output contract.
*   P0 allowed next stages are defined.
*   P0 write targets are defined.
*   P0 contains no final prompt body.
