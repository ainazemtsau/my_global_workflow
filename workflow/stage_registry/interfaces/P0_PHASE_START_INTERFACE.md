# 02 P0 Phase Start Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 02 P0 Phase Start Interface

Interface version: stage-interface-v0.1 Stage ID: P0 Stage name: Phase Start Stage type: phase initialization

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

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Phase Start
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