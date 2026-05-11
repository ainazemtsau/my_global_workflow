# 10 F0 Fast Direct Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 10 F0 Fast Direct Interface

Interface version: stage-interface-v0.1 Stage ID: F0 Stage name: Fast Direct Stage type: direct response / small execution

## Lifecycle role

F0 handles narrow, bounded tasks that can be completed directly without broader workflow planning.

F0 protects the workflow from unnecessary stage overhead while preserving traceability and escalation options.

## Public input contract

Required inputs:

*   Stage Launch Card targeting F0.
*   Narrow task or user request.
*   Requested output format.
*   Constraints and do-not-touch boundaries.
*   Freshness state.
*   Write authority.

Optional inputs:

*   Shaped Goal Brief.
*   Execution Brief.
*   Prior capture context.
*   Relevant artifact.
*   User style or format constraints.

Missing-context behavior:

*   If the task is not narrow, route to G1 or E1.
*   If execution would require research or current facts, route to D1.
*   If execution would require audit, route to A1.
*   If a defect or ambiguity blocks safe action, route to B1.

## Public output contract

F0 emits a Stage Result Packet containing:

*   Direct output.
*   Inputs used.
*   Constraints applied.
*   Any assumptions.
*   Whether the task is complete.
*   Escalation recommendation if needed.
*   Execution Log Entry.
*   Next route.

Required F0 output artifacts:

*   Direct Output Packet
*   Assumption List when applicable
*   Completion or Escalation Status
*   Next Stage Launch Card or Stop route

## Allowed next stages

F0 may route only to:

*   R1 Review Distill
*   P9 Phase Close
*   G1 Goal Shape
*   E1 Execution Brief
*   B1 Problem
*   R0 Recovery Close

## Write targets

F0 may propose or write only to authorized direct-output targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Fast Direct Output
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Outputs / \[output\_id\] \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Direct Output
*   Execution log mode: \[authorized execution log path from Launch Card\]

F0 must not expand a narrow task into a multi-stage plan unless escalation is required.

## Compatibility/core/extensions rules

F0 consumes and emits the shared core fields defined in 00 Stage Interface Index.

F0 may write extension fields only under:

*   extensions.F0.directness\_rationale
*   extensions.F0.assumption\_flags
*   extensions.F0.escalation\_reason

Unknown extension fields must be tolerated.

## Acceptance anchors

*   F0 has a public input contract.
*   F0 has a public output contract.
*   F0 allowed next stages are defined.
*   F0 write targets are defined.
*   F0 contains no final prompt body.