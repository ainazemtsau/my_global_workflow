# 12 C2 Codex Execute Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 12 C2 Codex Execute Interface

Interface version: stage-interface-v0.1 Stage ID: C2 Stage name: Codex Execute Stage type: Codex execution / implementation evidence

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