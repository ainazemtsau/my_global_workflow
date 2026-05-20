# Executor Runtime Model

## Purpose

This document defines the generic executor runtime behavior model for product/project execution. Runtime behavior, stage identity, and packet shapes remain owned by the runtime core, stage registry, and transport templates respectively.

## Role Model

ChatGPT Direction Project acts as Orchestrator, Planner, and Reviewer. It owns WHY, WHAT, DONE, target selection, acceptance criteria, scope boundaries, forbidden changes, risk posture, and evidence expectations.

Executor acts as the implementation agent inside a target project workspace. It owns HOW, local discovery, implementation planning, tool use, validation, bounded repair, and evidence return.

Project is the concrete local software/product workspace. Its technical context is stored in project-local files, not in ChatGPT history.

Adapter is the executor-specific binding. Codex is the first/default adapter and is documented separately.

## Lifecycle

1. E1 prepares an Executor Setup Request for setup or an Execution Work Package for normal execution.
2. `X0_EXECUTOR_PROJECT_SETUP` runs setup when setup is missing, incomplete, or the current action is setup.
3. `X1_EXECUTOR_RUN` handles normal execution when setup is complete.
4. Executor confirms target binding.
5. Executor checks setup status and readiness.
6. Executor reads project-local technical context.
7. Executor prepares a human-readable Plan Preview for nontrivial execution.
8. User approves the readable plan when required.
9. Executor executes within the approved plan.
10. Executor validates using the requested validation ladder level.
11. Executor runs bounded repair if validation fails and repair remains in scope.
12. Executor returns human-readable evidence for review.
13. ChatGPT reviews against DONE, acceptance, scope, and evidence expectations.

## ChatGPT / Executor Boundary

ChatGPT provides:

- objective and reason for the work
- target project reference
- acceptance criteria
- scope and forbidden changes
- validation expectations
- evidence requirements
- plan approval for nontrivial autonomous work
- final review against DONE

Executor provides:

- target confirmation
- local technical discovery
- implementation plan
- Task Master graph when required by complexity
- code changes inside the target project
- validation and repair
- final evidence
- blockers or setup gaps when execution cannot proceed safely

The executor must not ask ChatGPT to own implementation mechanics that belong in local project discovery and planning. ChatGPT must not mirror full technical context into Direction Project Files.

## Project-Local Technical Context Boundary

Technical context lives in the project workspace. Typical project-local artifacts include:

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

`AGENTS.md` must not contain Direction state, raw chats, secrets, or a full workflow state mirror.

Direction Project Files store compact outcome summaries, approval-relevant decisions, risk notes, and pointers to project-local artifacts.

## Target Binding

The executor must confirm target binding before material work. Required fields:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Wrong target, missing setup, or ambiguous workspace blocks execution.

## Planning Modes

P0 means trivial inspection or answer-only work. It may not require a graph.

P1 means small bounded edits or validation work with low blast radius. It may not require graph creation, but setup and target binding still apply.

P2 means moderate implementation with multiple steps, validators, or module impact. It requires a Task Master graph for Codex adapter execution.

P3 means complex, cross-module, risky, or long-running implementation. It requires a Task Master graph for Codex adapter execution and stronger validation evidence.

P0/P1 work can proceed without creating a graph when setup, target binding, and plan requirements are satisfied. Task Master remains available after setup.

## Plan Preview Requirement

Before nontrivial autonomous execution, the executor produces a human-readable Plan Preview that includes:

- target confirmation
- setup status
- intended files or modules
- reuse and existing-code discovery plan
- implementation steps
- validation ladder level
- repair limits
- forbidden changes and stop conditions
- expected evidence

The readable plan is approved before nontrivial autonomous execution begins.

## Plan Quality Compiler Summary

The Plan Quality Compiler blocks weak plans. A plan is weak when it lacks a confirmed target, acceptance mapping, scope boundary, validation surface, reuse check, module boundary analysis, repair limits, or evidence expectations.

The compiler does not replace executor judgment. It prevents execution from starting when the plan cannot support safe validation and review.

## Bounded Repair Loop Summary

Default repair policy:

- `max_repair_attempts: 2`
- `same_failure_repeat_limit: 1`

The executor stops when repair would introduce a new dependency, cross a new module boundary, touch a forbidden area, expand a public API, make an out-of-scope architecture decision, hide a missing validation surface, or repeat the same validator failure.

## Evidence-First DONE Rule

DONE requires evidence. The executor cannot claim DONE based on intent, partial implementation, or unverified assumptions.

Required evidence normally includes:

- target binding confirmation
- files changed
- validation run and output summary
- acceptance mapping
- repair attempts, if any
- remaining risks or explicit none
- forbidden-path confirmation

## Registry and Transport Boundary

Project Setup Wizard is a capability/action executed through `X0_EXECUTOR_PROJECT_SETUP`. Normal executor product/project execution uses `X1_EXECUTOR_RUN`.

Setup action does not require prior completed setup. Normal execution requires setup status `complete` or `complete_with_approved_fallback`.

Core-only setup is valid complete setup. Stack-specific tuning is optional and decision-gated.

This document does not duplicate the stage registry allowed-next table and does not duplicate transport schemas.

END_OF_FILE: workflow/executor/EXECUTOR_RUNTIME_MODEL.md
