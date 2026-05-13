# 14 R1 Review Distill Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 14 R1 Review Distill Interface

Interface version: stage-interface-v0.1 Stage ID: R1 Stage name: Review Distill Stage type: review / synthesis / documentation maintenance

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

R1 reviews completed work, distills lessons, identifies reusable outputs, and recommends documentation or state maintenance.

R1 is not a replacement for A1 audit. It may route to A1 when formal validation is required.

## Public input contract

Required inputs:

*   Stage Launch Card targeting R1.
*   Completed artifact, result packet, Codex Return Packet, direct output, or phase output.
*   Original goal or acceptance criteria.
*   Current state reference.
*   Requested review depth.
*   Write authority.

Optional inputs:

*   Audit report.
*   Human feedback.
*   Execution log.
*   Regression log.
*   Prior review notes.
*   Documentation maintenance gate template reference.

Missing-context behavior:

*   If the completed artifact is missing, emit a Context Request Card.
*   If acceptance criteria are missing, route to G1 or A1.
*   If the work appears defective, route to B1 or A1.
*   If the phase is ready to close, route to P9.

## Public output contract

R1 emits a Stage Result Packet containing:

*   Review Distill Packet.
*   Summary of work.
*   What changed or was learned.
*   Reusable decisions or patterns.
*   Documentation maintenance recommendations.
*   Open issues.
*   Next route.
*   Execution Log Entry.

Required R1 output artifacts:

*   Review Distill Packet
*   Lesson / Reuse List
*   Documentation Maintenance Recommendation
*   Open Issue List
*   Next Stage Launch Card or Phase Close route

## Allowed next stages

R1 may route only to:

*   P9 Phase Close
*   G1 Goal Shape
*   E1 Execution Brief
*   D1 Deep Research
*   A1 Audit
*   F0 Fast Direct
*   R0 Recovery Close

## Write targets

R1 may propose or write only to authorized review targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Review Distill
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Reviews / \[review\_id\] / Review Distill \[runtime\_target\_root from Launch Card\] / Lessons / \[lesson\_id\] \[runtime\_target\_root from Launch Card\] / Documentation Maintenance
*   Execution log mode: \[authorized execution log path from Launch Card\]

R1 must not silently mutate canonical documentation. It must use the documentation maintenance gate or patch template.

## Compatibility/core/extensions rules

R1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

R1 may write extension fields only under:

*   extensions.R1.reuse\_candidate
*   extensions.R1.documentation\_impact
*   extensions.R1.review\_depth

Unknown extension fields must be tolerated.

## Acceptance anchors

*   R1 has a public input contract.
*   R1 has a public output contract.
*   R1 allowed next stages are defined.
*   R1 write targets are defined.
*   R1 contains no final prompt body.
