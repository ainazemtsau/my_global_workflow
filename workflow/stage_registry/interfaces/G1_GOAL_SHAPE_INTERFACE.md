# 05 G1 Goal Shape Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 05 G1 Goal Shape Interface

Interface version: stage-interface-v0.1 Stage ID: G1 Stage name: Goal Shape Stage type: goal definition / ruthless cut

## Lifecycle role

G1 turns a selected or implied goal into an executable shaped goal.

G1 defines outcome, scope, non-goals, acceptance criteria, risks, dependencies, and the smallest safe next route.

## Public input contract

Required inputs:

*   Stage Launch Card targeting G1.
*   Selected goal or single candidate goal.
*   Direction or Phase context.
*   User constraints and requested output shape.
*   Known acceptance requirements.
*   Freshness state.
*   Write authority.

Optional inputs:

*   Capture Ledger.
*   Goal Selection Packet.
*   Prior research or audit findings.
*   Existing artifacts.
*   User-supplied done criteria.
*   Deadline, budget, tool, or format constraints.

Missing-context behavior:

*   If the goal cannot be shaped without more user input, emit a Context Request Card.
*   If several competing goals remain, route to G0.
*   If the goal needs a decision between options, route to S3.
*   If the goal is already narrow and executable, route to F0 or E1.

## Public output contract

G1 emits a Stage Result Packet containing:

*   Shaped Goal Brief.
*   Outcome statement.
*   Scope and non-goals.
*   Acceptance criteria.
*   Definition of done.
*   Risks and assumptions.
*   Dependencies.
*   Recommended next route.
*   Execution Log Entry.

Required G1 output artifacts:

*   Shaped Goal Brief
*   Acceptance Criteria
*   Definition of Done
*   Scope Cut List
*   Next Stage Launch Card or Context Request Card

## Allowed next stages

G1 may route only to:

*   S3 Decide
*   E1 Execution Brief
*   F0 Fast Direct
*   D1 Deep Research
*   A1 Audit
*   B1 Problem
*   G0 Goal Select
*   R0 Recovery Close

## Write targets

G1 may propose or write only to authorized goal-shaping targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Shaped Goal Brief
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Goals / \[goal\_id\] / Shaped Goal Brief \[runtime\_target\_root from Launch Card\] / Goals / \[goal\_id\] / Acceptance Criteria \[runtime\_target\_root from Launch Card\] / Goals / \[goal\_id\] / Scope Cut List
*   Execution log mode: \[authorized execution log path from Launch Card\]

G1 must not produce a Codex implementation plan. That belongs to E1 and C1.

## Compatibility/core/extensions rules

G1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

G1 may write extension fields only under:

*   extensions.G1.ruthless\_cut\_notes
*   extensions.G1.acceptance\_risk\_flags
*   extensions.G1.goal\_shape\_confidence

Unknown extension fields must be tolerated.

## Acceptance anchors

*   G1 has a public input contract.
*   G1 has a public output contract.
*   G1 allowed next stages are defined.
*   G1 write targets are defined.
*   G1 contains no final prompt body.