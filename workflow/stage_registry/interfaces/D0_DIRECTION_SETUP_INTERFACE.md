# 01 D0 Direction Setup Interface
artifact_control:
  artifact_name: "D0_DIRECTION_SETUP Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "D0_DIRECTION_SETUP"
  repo_path: "workflow/stage_registry/interfaces/D0_DIRECTION_SETUP_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 01 D0 Direction Setup Interface

Interface version: stage-interface-v0.1 Stage ID: D0 Stage name: Direction Setup Stage type: setup / orientation

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

D0 establishes or revises a Direction before phase work begins.

A Direction is a stable operating container for a body of work. D0 defines the Direction’s purpose, boundaries, activation scope, default storage target, and routing posture.

## Public input contract

Required inputs:

*   Stage Launch Card targeting D0.
*   User request to create, reset, clarify, or revise a Direction.
*   Available current state reference, even if empty.
*   Activation scope selection: rebuild-root-only, direction opt-in, or global.
*   Known constraints, including do-not-touch boundaries.
*   Freshness state for any external or old workflow material.

Optional inputs:

*   Existing Direction Charter.
*   Existing Direction State.
*   Prior phase summaries.
*   User preferences for depth, speed, or Codex involvement.
*   Candidate runtime target root.

Missing-context behavior:

*   If the Direction purpose or boundary is unclear, emit a Context Request Card.
*   If the requested activation scope conflicts with rebuild safety, emit a Human Decision Card.
*   If old active Workflow vNext material would need to be touched, stop and request explicit approval.

## Public output contract

D0 emits a Stage Result Packet containing:

*   Direction Charter candidate or update.
*   Direction State seed.
*   Direction boundary list.
*   Runtime target root recommendation.
*   Activation scope recommendation.
*   Open questions, if any.
*   Write plan or Repository Patch Template if writes are authorized.
*   Execution Log Entry.
*   Next route.

Required D0 output artifacts:

*   Direction Charter
*   Direction State
*   Direction Boundary Register
*   Next Stage Launch Card or Context Request Card

## Allowed next stages

D0 may route only to:

*   P0 Phase Start
*   I0 Capture
*   G0 Goal Select
*   G1 Goal Shape
*   R0 Recovery Close

## Write targets

D0 may propose or write only to authorized Direction setup targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Direction Charter
*   Rebuild draft amendment mode: Workflow / 20 Workflow vNext-R REBUILD / 10 Draft Amendments / Direction Setup Amendments
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Direction Charter \[runtime\_target\_root from Launch Card\] / Direction State \[runtime\_target\_root from Launch Card\] / Direction Boundary Register
*   Execution log mode: \[authorized execution log path from Launch Card\]

D0 must not write to:

*   Workflow / 20 Workflow vNext-R REBUILD / 07 Stage Prompts /
*   old active Workflow vNext material
*   any unapproved external Direction root

## Compatibility/core/extensions rules

D0 consumes and emits the shared core fields defined in 00 Stage Interface Index.

D0 may write extension fields only under:

*   extensions.D0.direction\_mode
*   extensions.D0.activation\_rationale
*   extensions.D0.boundary\_notes

Unknown extension fields must be tolerated and must not control routing unless the Launch Card explicitly declares them authoritative.

## Acceptance anchors

*   D0 has a public input contract.
*   D0 has a public output contract.
*   D0 allowed next stages are defined.
*   D0 write targets are defined.
*   D0 contains no final prompt body.
