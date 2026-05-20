# 09 E1 Execution Brief Interface
artifact_control:
  artifact_name: "E1_EXECUTION_BRIEF Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "E1_EXECUTION_BRIEF"
  repo_path: "workflow/stage_registry/interfaces/E1_EXECUTION_BRIEF_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 09 E1 Execution Brief Interface

Interface version: stage-interface-v0.1 Stage ID: E1 Stage name: Execution Brief Stage type: execution planning / handoff

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

E1 converts a shaped goal, decision, research finding, or audit finding into a concrete execution brief.

E1 prepares work for a human, F0, X0, X1, or a later review path. It does not itself perform broad implementation.

## Public input contract

Required inputs:

*   Stage Launch Card targeting E1.
*   Shaped Goal Brief, Decision Record, Audit Report, Research Dossier, or Problem Report.
*   Target executor type: human, ChatGPT direct, executor setup, executor run, or mixed.
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
*   If evidence requirements are missing for code or install work, route to A1, X0, or X1 according to setup state and readiness.
*   If the task is narrow and can be completed directly, route to F0.
*   If the work requires Executor/Codex execution, route to X0 or X1 according to setup state and readiness.

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
*   Next Stage Launch Card, Executor handoff, or Human Decision Card

## Allowed next stages

E1 may route only to:

*   M0 Direction Map
*   F0 Fast Direct
*   U1 User Guided Execution
*   X0 Executor Project Setup
*   X1 Executor Run
*   D1 Deep Research
*   A1 Audit
*   S3 Decide
*   B1 Problem
*   Context Request
*   Human Decision
*   Stop

## Write targets

E1 may propose or write only to authorized execution-brief targets:

*   Rebuild scenario test mode: ainazemtsau/my_global_workflow / 08 Scenario Tests / \[scenario\_id\] / Execution Brief
*   Direction opt-in mode: \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Execution Brief \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Acceptance Tests \[runtime\_target\_root from Launch Card\] / Execution / \[execution\_id\] / Evidence Requirements
*   Executor handoff mode: \[authorized executor handoff record path from Launch Card\]
*   Execution log mode: \[authorized execution log path from Launch Card\]

E1 must not create Executor/Codex implementation changes directly. Product/project execution belongs to X1.

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
