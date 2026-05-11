# 04 G0 Goal Select Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 04 G0 Goal Select Interface

Interface version: stage-interface-v0.1 Stage ID: G0 Stage name: Goal Select Stage type: goal triage / prioritization

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