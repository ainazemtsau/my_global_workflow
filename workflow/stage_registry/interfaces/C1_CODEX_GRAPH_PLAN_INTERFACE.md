# 11 C1 Codex Graph Plan Interface
artifact_control:
  artifact_name: "C1_CODEX_GRAPH_PLAN Stage Registry Interface"
  schema: stage_registry_interface.v1
  owner_layer: stage_registry_reference
  status: derived-reference
  stage_id: "C1_CODEX_GRAPH_PLAN"
  repo_path: "workflow/stage_registry/interfaces/C1_CODEX_GRAPH_PLAN_INTERFACE.md"
  authority: "Derived/reference only; workflow/stage_registry/STAGE_REGISTRY.md wins on conflicts"
  activation_scope: reference_only
  freshness: refresh_when_stage_registry_or_interface_contract_changes
  last_updated: "2026-05-13"

# 11 C1 Codex Graph Plan Interface

Interface version: stage-interface-v0.1 Stage ID: C1 Stage name: Codex Graph Plan Stage type: Codex planning / wave graph

## Interface authority boundary — AD-WF-RT-001

This interface file is a derived/reference surface only.

It is not authority for stage-to-stage `allowed_next` transitions.

If this interface file contains route lists, they are snapshots only and must not override:

```text
workflow/stage_registry/STAGE_REGISTRY.md
```

If this interface conflicts with `STAGE_REGISTRY.md`, the registry wins and this interface should be refreshed in a later cleanup patch.

## Lifecycle role

C1 converts an Execution Brief into a bounded Codex execution envelope and, when needed, a graph plan / wave card draft.

C1 plans the ChatGPT-side execution envelope for Codex work. It does not execute repository or GitHub repository writes, and it does not perform deep product technical planning unless exact technical context is explicitly supplied and scoped.

C1 may require Codex-side technical discovery / architecture reuse preflight in C2 when product-local architecture, module-boundary, reuse-vs-new, public-interface, dependency-direction, or technical-memory decisions are needed.

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
*   Compact pointers to project-local technical sources such as `AGENTS.md`, Project Execution Profile, Validation Profile, Module Map, ADRs, public interface docs, internal module knowledge, or `.codex` memory.

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
*   Technical Context Boundary
*   Technical Discovery Preflight Requirement, when needed
*   Evidence Plan
*   Validator Plan
*   Next Stage Launch Card or Codex Wave Card

## Allowed next stages

This interface is a derived/reference surface only. Registry authority wins.

Current registry-valid C1 terminal outcomes:

*   C2_CODEX_EXECUTE
*   Context Request
*   Human Decision
*   Stop

## Write targets

C1 may propose or write only to authorized Codex planning targets:

*   Rebuild scenario test mode: ainazemtsau/my_global_workflow / 08 Scenario Tests / \[scenario\_id\] / Codex Graph Plan
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
