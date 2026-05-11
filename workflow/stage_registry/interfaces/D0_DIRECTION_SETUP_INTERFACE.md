# 01 D0 Direction Setup Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 01 D0 Direction Setup Interface

Interface version: stage-interface-v0.1 Stage ID: D0 Stage name: Direction Setup Stage type: setup / orientation

## Lifecycle role

D0 establishes or revises a Direction before phase work begins.

A Direction is a stable operating container for a body of work. D0 defines the Direction’s purpose, boundaries, activation scope, default storage target, and routing posture.

## Public input contract

Required inputs:

*   Stage Launch Card targeting D0.
*   User request to create, reset, clarify, or revise a Direction.
*   Available current state reference, even if empty.
*   Activation scope: rebuild root only, direction opt-in, or global.
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
*   Write plan or Trilium Patch Template if writes are authorized.
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