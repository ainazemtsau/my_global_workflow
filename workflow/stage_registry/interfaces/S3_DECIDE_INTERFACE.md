# 06 S3 Decide Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 06 S3 Decide Interface

Interface version: stage-interface-v0.1 Stage ID: S3 Stage name: Decide Stage type: decision / option selection

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

S3 resolves a decision point after a goal has been shaped or a blocker has been identified.

S3 compares viable options against explicit criteria and emits a decision record or human decision request.

## Public input contract

Required inputs:

*   Stage Launch Card targeting S3.
*   Decision question.
*   Candidate options.
*   Decision criteria.
*   Relevant goal, phase, or problem context.
*   Known constraints and freshness state.
*   Authority level: recommend, decide, or request human decision.

Optional inputs:

*   Prior research.
*   Audit findings.
*   Risk register.
*   User preference.
*   Cost, time, reversibility, or confidence constraints.

Missing-context behavior:

*   If options are missing, route to G1, D1, or B1 depending on the gap.
*   If criteria are missing and decision impact is material, emit a Human Decision Card.
*   If evidence is stale or insufficient, route to D1 or A1.

## Public output contract

S3 emits a Stage Result Packet containing:

*   Decision Record.
*   Chosen option or recommendation.
*   Rejected options.
*   Rationale.
*   Tradeoffs.
*   Conditions or rollback triggers.
*   Next route.
*   Execution Log Entry.

Required S3 output artifacts:

*   Decision Record
*   Option Comparison
*   Decision Rationale
*   Next Stage Launch Card or Human Decision Card

## Allowed next stages

S3 may route only to:

*   E1 Execution Brief
*   C1 Codex Graph Plan
*   D1 Deep Research
*   A1 Audit
*   G1 Goal Shape
*   F0 Fast Direct
*   P9 Phase Close
*   R0 Recovery Close

## Write targets

S3 may propose or write only to authorized decision targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Decision Record
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Decisions / \[decision\_id\] \[runtime\_target\_root from Launch Card\] / Goals / \[goal\_id\] / Decision Record
*   Execution log mode: \[authorized execution log path from Launch Card\]

S3 must not execute the decision. Execution preparation belongs to E1, C1, C2, or F0.

## Compatibility/core/extensions rules

S3 consumes and emits the shared core fields defined in 00 Stage Interface Index.

S3 may write extension fields only under:

*   extensions.S3.decision\_method
*   extensions.S3.reversibility
*   extensions.S3.confidence\_notes

Unknown extension fields must be tolerated.

## Acceptance anchors

*   S3 has a public input contract.
*   S3 has a public output contract.
*   S3 allowed next stages are defined.
*   S3 write targets are defined.
*   S3 contains no final prompt body.
