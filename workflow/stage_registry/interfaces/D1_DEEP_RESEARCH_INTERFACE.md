# 07 D1 Deep Research Interface
Status: test-active Workflow version: vNext-R REBUILD Installed from roadmap step: Step 6 — Stage Interface Registry Installed at: 2026-05-07T16:43:14.1696924+03:00 Source input: ChatGPT Step 6 output generated 2026-05-07 from validated current state after Step 5 Authority: Trilium canonical after read-back Activation scope: rebuild root only Freshness: fresh Supersedes: Superseded by:

# 07 D1 Deep Research Interface

Interface version: stage-interface-v0.1 Stage ID: D1 Stage name: Deep Research Stage type: research / evidence synthesis

## Lifecycle role

D1 investigates questions that require evidence, freshness checks, source comparison, or synthesis before decision or execution.

D1 produces research outputs only. It does not silently convert research into implementation without a downstream route.

## Public input contract

Required inputs:

*   Stage Launch Card targeting D1.
*   Research question or information gap.
*   Desired depth and output shape.
*   Freshness requirement.
*   Source constraints or citation requirements.
*   Relevant goal, decision, audit, or problem context.
*   Write authority.

Optional inputs:

*   Known sources.
*   Prior research.
*   User hypotheses.
*   Exclusion criteria.
*   Confidence threshold.
*   Time or scope boundary.

Missing-context behavior:

*   If the research question is too broad, route to G1 or emit a Context Request Card.
*   If the issue is actually a decision with known options, route to S3.
*   If the issue is a defect or failure, route to B1.
*   If freshness cannot be established from available context, mark freshness as unknown and request research authority.

## Public output contract

D1 emits a Stage Result Packet containing:

*   Research Dossier.
*   Source Map.
*   Findings.
*   Confidence and uncertainty notes.
*   Freshness assessment.
*   Open questions.
*   Recommended next route.
*   Execution Log Entry.

Required D1 output artifacts:

*   Research Dossier
*   Source Map
*   Findings Summary
*   Freshness Assessment
*   Next Stage Launch Card or Context Request Card

## Allowed next stages

D1 may route only to:

*   G1 Goal Shape
*   S3 Decide
*   E1 Execution Brief
*   A1 Audit
*   R1 Review Distill
*   B1 Problem
*   R0 Recovery Close

## Write targets

D1 may propose or write only to authorized research targets:

*   Rebuild scenario test mode: Workflow / 20 Workflow vNext-R REBUILD / 08 Scenario Tests / \[scenario\_id\] / Research Dossier
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Research / \[research\_id\] / Research Dossier \[runtime\_target\_root from Launch Card\] / Research / \[research\_id\] / Source Map \[runtime\_target\_root from Launch Card\] / Evidence / \[research\_id\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

D1 must not fabricate source authority or treat stale context as fresh.

## Compatibility/core/extensions rules

D1 consumes and emits the shared core fields defined in 00 Stage Interface Index.

D1 may write extension fields only under:

*   extensions.D1.source\_policy
*   extensions.D1.confidence\_model
*   extensions.D1.freshness\_notes

Unknown extension fields must be tolerated.

## Acceptance anchors

*   D1 has a public input contract.
*   D1 has a public output contract.
*   D1 allowed next stages are defined.
*   D1 write targets are defined.
*   D1 contains no final prompt body.