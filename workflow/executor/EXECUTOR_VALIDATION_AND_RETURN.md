# Executor Validation and Return

## Purpose

This document defines the executor validation ladder, quality gates, bounded repair loop, and human-readable return evidence. It is a contract document only and does not create a canonical transport template.

## Validation Ladder

V0_READINESS verifies target, setup, scope, local context, plan, and validators before material execution.

V1_PATCH_SANITY verifies that changed files are limited to the approved scope and basic static or formatting checks pass where available.

V2_TARGETED_BEHAVIOR verifies directly affected behavior with targeted tests, scripts, screenshots, or manual evidence appropriate to the project.

V3_INTEGRATION_BUILD verifies broader integration such as full test subsets, build, package checks, or service-level checks.

V4_RELEASE_CONFIDENCE verifies high-confidence release readiness through broader regression, performance, stability, security, or deployment-adjacent checks when the work warrants it.

The work package names the expected validation level. The executor may run stronger validation when safe and useful.

## Quality Gates

### Target Gate

The executor confirms target binding before work:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Wrong target, missing setup, or ambiguous workspace blocks execution.

### Existing-Code / Reuse Gate

The executor checks project-local context and existing code before adding new modules or patterns. It should reuse or extend existing behavior when that satisfies acceptance.

### Architecture Gate

The executor verifies module boundaries, public interfaces, ADRs, and architecture constraints relevant to the work. Out-of-scope architecture decisions stop execution.

### Scope Gate

The executor confirms changed files remain inside approved scope. Forbidden paths or unrelated modules stop execution unless explicitly approved.

### Static Gate

The executor runs available static checks such as format, lint, typecheck, compile, schema validation, or docs checks according to `VALIDATION_PROFILE.md`.

### Behavioral Gate

The executor runs targeted behavior validation for the requested change. If no validation surface exists, the executor must report that and stop when acceptance cannot be evidenced.

### Regression Gate

The executor runs relevant regression or integration checks when the change crosses module boundaries, changes shared behavior, alters public interfaces, or has elevated risk.

### Performance / Stability Gate

The executor checks performance, stability, resource use, or long-running behavior when the work can affect those dimensions.

### Review Gate

The executor obtains reviewer or subagent review when required by setup, complexity, risk, or the work package.

### Evidence Gate

The executor cannot claim DONE without evidence that maps validation results to acceptance criteria and scope boundaries.

## Bounded Repair Loop

Default repair policy:

- `max_repair_attempts: 2`
- `same_failure_repeat_limit: 1`

The executor may repair validation failures only when the repair remains inside approved scope and the root cause is understood.

The executor stops on:

- repeated validator failure
- new dependency requirement
- new module boundary
- forbidden area
- missing validation surface
- out-of-scope architecture decision
- public API scope expansion
- tool or credential blockage
- unclear acceptance

Repair evidence must include the failed check, suspected root cause, repair attempt number, changed files, rerun validators, and remaining risk.

## Human-Readable Execution Result

The execution result is human-readable first and should include:

- status: DONE, NEEDS_INPUT, STUCK, FAILED, or PARTIAL when allowed by the active compatibility contract
- target confirmation
- requested work
- summary of completed work
- files changed
- acceptance evidence
- validation evidence
- repair attempts
- forbidden-path confirmation
- risks and residual issues
- setup or context gaps, if any
- next recommended route

For execution-layer final states that require only DONE, NEEDS_INPUT, or STUCK, the result must conform to that active route. Compatibility documents may allow broader repository-maintenance statuses.

## Minimal Future-Compatible Return Fields

The following fields are useful for future machine-readable transport compatibility. They are not a canonical transport template in this pass.

```text
executor_result:
  status:
  target_project_ref:
  work_package_id:
  setup_status:
  planning_mode:
  task_graph_used:
  files_changed:
  validation_level_requested:
  validation_performed:
  acceptance_evidence:
  repair_attempts:
  forbidden_paths_touched:
  blockers:
  next_route:
```

## DONE Rule

There is no DONE without validation and evidence. The executor must not claim DONE based on intention, code changes alone, or unverified assumptions.

END_OF_FILE: workflow/executor/EXECUTOR_VALIDATION_AND_RETURN.md
