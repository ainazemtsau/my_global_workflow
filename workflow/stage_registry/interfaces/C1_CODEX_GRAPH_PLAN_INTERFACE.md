# 11 C1 Codex Graph Plan Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 11 C1 Codex Graph Plan Interface

Interface version: stage-interface-v0.1 Stage ID: C1 Stage name: Codex Graph Plan Stage type: Codex planning / wave graph

## Lifecycle role

C1 converts an Execution Brief into a Codex-ready graph plan and wave card draft.

C1 plans Codex work. It does not execute repository or GitHub repository writes.

## Public input contract

Required inputs:

*   Stage Launch Card targeting C1.
*   Execution Brief or equivalent implementation goal.
*   Target repository, GitHub repository root, or filesystem scope.
*   Allowed tools and forbidden paths.
*   Evidence and validator expectations.
*   Rollback expectations.
*   Codex bridge contract references.
*   Write authority for wave plan notes only.

Optional inputs:

*   Existing AGENTS.md guidance.
*   Prior Codex Return Packet.
*   Known dependency graph.
*   Existing tests.
*   Task Master boundary notes.
*   Human sequencing preference.

Missing-context behavior:

*   If target scope is missing, emit a Context Request Card.
*   If acceptance tests are missing, route to E1 or A1.
*   If the task is too vague, route to G1.
*   If a prior Codex attempt failed, route to B1.

## Public output contract

C1 emits a Stage Result Packet containing:

*   Codex Graph Plan.
*   Codex Wave Card draft.
*   Dependency graph.
*   File or note target list.
*   Evidence plan.
*   Validator plan.
*   Rollback plan.
*   Next route.
*   Execution Log Entry.

Required C1 output artifacts:

*   Codex Graph Plan
*   Codex Wave Card Draft
*   Evidence Plan
*   Validator Plan
*   Next Stage Launch Card or Codex Wave Card

## Allowed next stages

C1 may route only to:

*   C2 Codex Execute
*   E1 Execution Brief
*   G1 Goal Shape
*   B1 Problem
*   R0 Recovery Close

## Write targets

C1 may propose or write only to authorized Codex planning targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Codex Graph Plan
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Codex / \[wave\_id\] / Codex Graph Plan \[runtime\_target\_root from Launch Card\] / Codex / \[wave\_id\] / Codex Wave Card Draft
*   Codex bridge mode: \[authorized Codex wave record path from Launch Card\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

C1 must not apply code patches, write GitHub repository changes, or claim implementation completion.

## Compatibility/core/extensions rules

C1 consumes and emits the shared core fields defined in 00 Stage Interface Index and the accepted Codex Bridge contracts.

C1 may write extension fields only under:

*   extensions.C1.graph\_model
*   extensions.C1.wave\_partitioning
*   extensions.C1.validator\_plan

Unknown extension fields must be tolerated.

## Acceptance anchors

*   C1 has a public input contract.
*   C1 has a public output contract.
*   C1 allowed next stages are defined.
*   C1 write targets are defined.
*   C1 contains no final prompt body.