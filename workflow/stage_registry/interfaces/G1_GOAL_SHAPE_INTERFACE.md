# 05 G1 Goal Shape Interface
artifact_control:
  artifact_name: "G1_GOAL_SHAPE Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "G1_GOAL_SHAPE"
  repo_path: "workflow/stage_registry/interfaces/G1_GOAL_SHAPE_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 05 G1 Goal Shape Interface

Interface version: stage-interface-v0.1 Stage ID: G1 Stage name: Goal Shape Stage type: goal definition / ruthless cut

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

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
