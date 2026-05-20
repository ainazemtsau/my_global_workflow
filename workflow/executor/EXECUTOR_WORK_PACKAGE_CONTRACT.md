# Executor Work Package Contract

## Purpose

This document defines what ChatGPT sends to an Executor for normal product/project execution through `X1_EXECUTOR_RUN`. The package is human-readable first and should be mappable to `workflow/transport/EXECUTION_WORK_PACKAGE.md`.

The work package carries intent, target, scope, acceptance, and evidence expectations. It points to project-local technical artifacts instead of copying full technical context into ChatGPT history.

Setup action is separate: Project Setup Wizard runs through `X0_EXECUTOR_PROJECT_SETUP` using an Executor Setup Request, not this work package.

## Human-Readable First

The primary work package is written for a human reviewer and an executor to understand before work begins. It should be compact, explicit, and target-bound.

The package must not rely on hidden chat context for critical acceptance, target, scope, or forbidden-change rules.

## Target Project Reference

Required `target_project_ref` fields:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

The executor confirms these fields before reading project-local context or changing files. A mismatch blocks execution.

## Required Package Content

The work package includes:

- WHAT: the requested change or investigation
- WHY: concise reason or user/business objective when relevant
- DONE: concrete completion condition
- acceptance criteria
- scope in
- scope out
- forbidden changes
- validation expectations
- evidence requirements
- target project reference
- setup status expectation
- project-local artifact pointers
- plan approval requirement for nontrivial autonomous work
- repair limits or escalation triggers when stricter than default

## Project-Local Artifact Pointers

The work package should point to local project artifacts such as:

- `AGENTS.md`
- `PROJECT_PROFILE.md`
- `EXECUTOR_PROFILE.md`
- `VALIDATION_PROFILE.md`
- `MODULE_MAP.md`
- `docs/architecture/ADR-*.md`
- `docs/modules/*.md`
- `docs/public-interfaces/*.md`
- `changes/<change-id>/*`
- optional `.codex/*`

Do not mirror full technical context into the work package. The executor reads the project-local files after confirming target binding.

## Readiness Requirements Before Handoff

Before handoff, ChatGPT verifies that:

- the target project is identified
- the setup status is known
- the requested scope is bounded
- acceptance criteria are testable or reviewable
- forbidden changes are explicit
- validation expectations are named
- evidence requirements are clear
- the work does not require missing approval, credentials, or setup

If readiness is missing, ChatGPT should request setup, clarification, or research instead of sending executable work.

## Relationship to Objective Architecture Execution Readiness

Objective Architecture may define execution readiness, architecture constraints, and module ownership for a Direction. The Executor Work Package references that readiness at a compact level and points to project-local artifacts for technical detail.

The package must not copy the full Objective Architecture file. It should include only the approval-relevant summary needed to guide execution and review.

## Simple Work Package Example

```text
Executor Work Package

target_project_ref:
  direction_id: DIR-example
  project_id: web-dashboard
  project_name: Web Dashboard
  project_root_pointer: C:\work\web-dashboard
  expected_repo_or_workspace: ainazemtsau/web-dashboard
  executor_setup_status: complete

WHAT:
Fix the empty-state copy on the reports page.

DONE:
The reports page shows the approved empty-state message when no reports exist.

Acceptance:
- Empty state appears only when the reports list is empty.
- Existing populated-list behavior is unchanged.

Scope in:
- Reports page UI copy and directly affected test.

Scope out:
- Data fetching behavior.
- Navigation changes.

Forbidden changes:
- Do not modify authentication, billing, or shared router behavior.

Validation expectations:
- Run the targeted reports page test or explain why unavailable.
- Run patch sanity checks defined in VALIDATION_PROFILE.md.

Evidence requirements:
- Files changed.
- Test command and output summary.
- Screenshot only if UI validation requires it.
```

## Complex Work Package Example

```text
Executor Work Package

target_project_ref:
  direction_id: DIR-example
  project_id: api-platform
  project_name: API Platform
  project_root_pointer: C:\work\api-platform
  expected_repo_or_workspace: ainazemtsau/api-platform
  executor_setup_status: complete

WHAT:
Add support for a new billing event ingestion path using the existing event pipeline.

DONE:
The billing event is accepted, validated, persisted, and covered by targeted behavior tests without changing public API behavior outside the approved event type.

Acceptance:
- Reuses the existing event ingestion pipeline where possible.
- Adds or updates module docs if the event boundary changes.
- Handles invalid event payloads with existing error conventions.
- Adds targeted tests for valid and invalid payloads.

Scope in:
- Event ingestion module.
- Billing event schema or mapper.
- Targeted tests and docs for the changed boundary.

Scope out:
- New queue infrastructure.
- Billing UI.
- Public API expansion beyond the approved event type.

Forbidden changes:
- Do not replace the ingestion pipeline.
- Do not change unrelated event types.
- Do not add a new external dependency without approval.

Planning:
- P2 complexity.
- Create a Task Master graph before implementation.
- Provide a Plan Preview and wait for approval.

Validation expectations:
- V0_READINESS through V3_INTEGRATION_BUILD unless a validator is unavailable.
- Use VALIDATION_PROFILE.md and MODULE_MAP.md.

Evidence requirements:
- Target binding confirmation.
- Task Master graph summary.
- Files changed.
- Tests and output summary.
- Acceptance mapping.
- Repair attempts, if any.
- Remaining risk.
```

END_OF_FILE: workflow/executor/EXECUTOR_WORK_PACKAGE_CONTRACT.md
