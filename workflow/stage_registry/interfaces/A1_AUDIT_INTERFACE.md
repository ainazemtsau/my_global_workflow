# 08 A1 Audit Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: GitHub repository canonical after file read-back / diff verification / commit verification Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 08 A1 Audit Interface

Interface version: stage-interface-v0.1 Stage ID: A1 Stage name: Audit Stage type: validation / quality review

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

A1 audits an artifact, plan, workflow state, evidence set, or Codex result against explicit standards.

A1 reports findings, severity, evidence, and recommended remediation. It does not silently repair unless a downstream route authorizes repair.

## Public input contract

Required inputs:

*   Stage Launch Card targeting A1.
*   Artifact, plan, packet, note, or result to audit.
*   Audit standard, checklist, acceptance criteria, or test harness reference.
*   Current state reference.
*   Freshness state.
*   Write authority.

Optional inputs:

*   Prior audit report.
*   Known risk areas.
*   Evidence references.
*   Regression log.
*   Human severity threshold.
*   Requested output format.

Missing-context behavior:

*   If the audit standard is absent, emit a Context Request Card.
*   If the artifact is missing, route to B1 or emit a Context Request Card.
*   If evidence is insufficient to validate, return partial with evidence gaps.

## Public output contract

A1 emits a Stage Result Packet containing:

*   Audit Report.
*   Finding list.
*   Severity ratings.
*   Evidence references.
*   Pass/fail or confidence result.
*   Recommended fixes.
*   Regression or test implications.
*   Next route.
*   Execution Log Entry.

Required A1 output artifacts:

*   Audit Report
*   Finding Register
*   Evidence Register
*   Recommended Remediation
*   Next Stage Launch Card or Problem Report route

## Allowed next stages

A1 may route only to:

*   G1 Goal Shape
*   S3 Decide
*   E1 Execution Brief
*   C1 Codex Graph Plan
*   B1 Problem
*   R1 Review Distill
*   R0 Recovery Close

## Write targets

A1 may propose or write only to authorized audit targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Audit Report
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Audits / \[audit\_id\] / Audit Report \[runtime\_target\_root from Launch Card\] / Evidence / \[audit\_id\] \[runtime\_target\_root from Launch Card\] / Regression Log
*   Execution log mode: \[authorized execution log path from Launch Card\]

A1 must not mark work as passed without evidence or explicit uncertainty.

## Compatibility/core/extensions rules

A1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

A1 may write extension fields only under:

*   extensions.A1.audit\_standard
*   extensions.A1.severity\_model
*   extensions.A1.evidence\_notes

Unknown extension fields must be tolerated.

## Acceptance anchors

*   A1 has a public input contract.
*   A1 has a public output contract.
*   A1 allowed next stages are defined.
*   A1 write targets are defined.
*   A1 contains no final prompt body.
