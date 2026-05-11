# 13 B1 Problem Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 13 B1 Problem Interface

Interface version: stage-interface-v0.1 Stage ID: B1 Stage name: Problem Stage type: blocker analysis / repair framing

## Lifecycle role

B1 handles blockers, failed validation, ambiguity, contradictions, regressions, and broken handoffs.

B1 defines the problem and safe repair route. It does not patch forward from confused state without a controlled route.

## Public input contract

Required inputs:

*   Stage Launch Card targeting B1.
*   Problem, blocker, failed result, failed audit, or user-reported issue.
*   Current state reference.
*   Evidence or error context.
*   Impact boundary.
*   Write authority.
*   Recovery tolerance: analyze only, propose repair, or prepare recovery.

Optional inputs:

*   Prior Codex Return Packet.
*   Failed install result.
*   Regression log.
*   Relevant artifacts.
*   Human severity preference.
*   Known attempted fixes.

Missing-context behavior:

*   If evidence is missing, emit a Context Request Card.
*   If the issue may involve partial writes or corrupted state, route to R0.
*   If the issue is a decision rather than a defect, route to S3.
*   If the goal is malformed, route to G1.

## Public output contract

B1 emits a Stage Result Packet containing:

*   Problem Report.
*   Evidence summary.
*   Impact assessment.
*   Likely cause categories.
*   Repair options.
*   Recommended safe next action.
*   Stop conditions.
*   Execution Log Entry.

Required B1 output artifacts:

*   Problem Report
*   Impact Assessment
*   Repair Option List
*   Recommended Next Action
*   Next Stage Launch Card or Recovery Close Packet

## Allowed next stages

B1 may route only to:

*   G1 Goal Shape
*   S3 Decide
*   D1 Deep Research
*   A1 Audit
*   E1 Execution Brief
*   C1 Codex Graph Plan
*   P9 Phase Close
*   R0 Recovery Close

## Write targets

B1 may propose or write only to authorized problem targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Problem Report
*   Rebuild draft amendment mode: Workflow / 20 Workflow vNext-R REBUILD / 10 Draft Amendments / Problem Reports
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Problems / \[problem\_id\] / Problem Report \[runtime\_target\_root from Launch Card\] / Problems / \[problem\_id\] / Repair Plan \[runtime\_target\_root from Launch Card\] / Regression Log
*   Execution log mode: \[authorized execution log path from Launch Card\]

B1 must not delete, overwrite, or mark stale unless R0 or explicit human approval authorizes that action.

## Compatibility/core/extensions rules

B1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

B1 may write extension fields only under:

*   extensions.B1.problem\_category
*   extensions.B1.impact\_scope
*   extensions.B1.repair\_risk

Unknown extension fields must be tolerated.

## Acceptance anchors

*   B1 has a public input contract.
*   B1 has a public output contract.
*   B1 allowed next stages are defined.
*   B1 write targets are defined.
*   B1 contains no final prompt body.