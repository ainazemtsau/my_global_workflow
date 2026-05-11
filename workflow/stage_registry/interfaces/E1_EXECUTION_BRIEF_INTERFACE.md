# 09 E1 Execution Brief Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 09 E1 Execution Brief Interface

Interface version: stage-interface-v0.1 Stage ID: E1 Stage name: Execution Brief Stage type: execution planning / handoff

## Lifecycle role

E1 converts a shaped goal, decision, research finding, or audit finding into a concrete execution brief.

E1 prepares work for a human, F0, C1, C2, or a later review path. It does not itself perform broad implementation.

## Public input contract

Required inputs:

*   Stage Launch Card targeting E1.
*   Shaped Goal Brief, Decision Record, Audit Report, Research Dossier, or Problem Report.
*   Target executor type: human, ChatGPT direct, Codex plan, Codex execute, or mixed.
*   Acceptance criteria.
*   Constraints and do-not-touch boundaries.
*   Evidence or validator expectations.
*   Write authority.

Optional inputs:

*   Existing task list.
*   Repository or GitHub repository context.
*   Deadline.
*   Tool constraints.
*   Risk or rollback notes.
*   Preferred handoff format.

Missing-context behavior:

*   If acceptance criteria are missing, route to G1.
*   If evidence requirements are missing for code or install work, route to A1 or C1.
*   If the task is narrow and can be completed directly, route to F0.
*   If the work requires Codex planning, route to C1.

## Public output contract

E1 emits a Stage Result Packet containing:

*   Execution Brief.
*   Task breakdown.
*   Acceptance tests.
*   Evidence requirements.
*   Dependencies.
*   Handoff instructions.
*   Risk and rollback notes.
*   Next route.
*   Execution Log Entry.

Required E1 output artifacts:

*   Execution Brief
*   Task Breakdown
*   Acceptance Test List
*   Evidence Requirement List
*   Next Stage Launch Card, Codex Wave Card, or Human Decision Card

## Allowed next stages

E1 may route only to:

*   C1 Codex Graph Plan
*   C2 Codex Execute
*   F0 Fast Direct
*   R1 Review Distill
*   P9 Phase Close
*   B1 Problem
*   R0 Recovery Close

## Write targets

E1 may propose or write only to authorized execution-brief targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Execution Brief
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Execution Brief \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Acceptance Tests \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Evidence Requirements
*   Codex bridge mode: \[authorized Codex wave record path from Launch Card\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

E1 must not create Codex implementation changes directly. Codex implementation belongs to C2.

## Compatibility/core/extensions rules

E1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

E1 may write extension fields only under:

*   extensions.E1.executor\_type
*   extensions.E1.acceptance\_test\_model
*   extensions.E1.handoff\_notes

Unknown extension fields must be tolerated.

## Acceptance anchors

*   E1 has a public input contract.
*   E1 has a public output contract.
*   E1 allowed next stages are defined.
*   E1 write targets are defined.
*   E1 contains no final prompt body.