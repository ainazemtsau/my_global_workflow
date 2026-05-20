# Executor Project Execution Core Concept

status: accepted_concept_for_wave_a_b

Source note: this concept is derived from the reviewed Executor Project Execution Core concept and approved user deltas for Wave A-B, then aligned with the X0/X1 executor-stage migration.

## Purpose

This document records the accepted design baseline for the new Executor Project Execution Core. The core defines how ChatGPT Direction Projects delegate software/product implementation to an external coding executor while preserving clear ownership of intent, scope, acceptance, and evidence.

The first/default adapter is Codex. The architecture remains executor-generic so future adapters can be added without making Codex the permanent execution model.

## Architecture Roles

ChatGPT Direction Project is the Orchestrator, Planner, and Reviewer. It owns WHY, WHAT, DONE, target selection, acceptance criteria, scope boundaries, risk framing, and evidence expectations.

Executor is an external coding agent operating inside a concrete project workspace. It owns HOW, codebase discovery, implementation planning, local tool use, validation, bounded repair, and evidence return.

Codex is the first executor adapter. It provides the initial concrete commands, setup checks, Task Master integration, subagent/reviewer role expectations, and return evidence format. Codex-specific behavior belongs in adapter documentation, not in the generic core.

Project means the concrete software or product workspace with local technical artifacts, source code, validators, build configuration, module boundaries, and project-specific operating instructions.

## Repository Maintenance vs Product Execution

Workflow repository maintenance remains separate from product/project execution.

Repository maintenance applies approved changes to this workflow repository and returns read-back, diff, validation, commit, and push evidence. It may create or update workflow documentation when explicitly allowed.

Product/project execution requires a completed Executor Project Setup in the target project workspace. It must not be inferred from workflow documentation alone and must not modify sibling Directions or product repositories unless the handoff explicitly targets them.

## Setup Gate

Product/project execution is gated by Executor Project Setup. Normal execution assumes setup is complete and target-bound. If setup is missing, incomplete, blocked, or points at the wrong workspace, execution must stop before material work.

Required target binding fields:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Wrong target or workspace blocks execution. The executor must confirm the target binding before reading project-local context or changing files.

## Two-Layer Setup Model

Executor Project Setup has two layers.

Layer 1, Required Core Bootstrap, creates or verifies the minimum executor-ready project layer: project-local instructions, executor profile, validation profile, module map, required tools, doctor checks, and target binding.

Layer 2, Optional Stack-Specific Setup Tuning Pass, investigates whether stack-specific validators, MCP servers, tools, skills, conventions, or docs should be enabled for that project. Core-only setup is valid complete setup. Optional tuning is not required for execution readiness.

The tuning pass may produce a Setup Recommendation Brief with explicit decisions:

- enable now
- use core-only
- park for later
- research more
- reject

Current external facts or tool behavior must not be guessed. If they matter, setup may request `D1_DEEP_RESEARCH` or return a research-needed note. If external UI or local guided action is required, setup may route to `U1_USER_GUIDED_EXECUTION`.

## Task Master and Subagent Setup Decisions

The Codex adapter setup must install, configure, and verify baseline tools for Codex projects:

- Task Master
- subagents and reviewer roles
- validation profile
- module map
- `AGENTS.md`
- project and executor profiles
- doctor checks

Task Master is required and verified during setup. P2/P3 execution tasks must use a Task Master graph. P0/P1 work may not require graph creation, but Task Master remains available.

Subagents and reviewer roles are setup-time requirements. If true subagents cannot be configured, setup must stop and ask for a setup-time fallback decision. Normal execution does not renegotiate fallback.

## Full-Trust Target-Bound Execution

After user authorization and successful setup, execution mode is full-trust inside the target project workspace. Full trust is target-bound only. It does not grant permission to operate in sibling Directions, unrelated repositories, workflow repository maintenance paths, or external systems outside the approved target.

No recurring permission or policing ceremony is required during normal execution. Instead, the target binding and approved plan define the execution envelope.

## Planning and Execution

Executor receives an Execution Work Package. It confirms target binding, reads project-local technical context, produces a human-readable Plan Preview, and waits for plan approval before nontrivial autonomous execution.

Complex work requires a Task Master graph. The Plan Quality Compiler blocks weak plans before execution. Plans must identify reuse opportunities, module boundaries, validation surfaces, forbidden areas, repair limits, and evidence expectations.

The executor executes autonomously within the approved plan and bounded repair loop:

- `max_repair_attempts: 2` by default
- `same_failure_repeat_limit: 1`
- stop on repeated validator failure
- stop on new dependency
- stop on new module boundary
- stop on forbidden area
- stop on missing validation surface
- stop on out-of-scope architecture decision
- stop on public API scope expansion

There is no DONE without validation and evidence.

## Validation and Return

The validation ladder is:

- V0_READINESS
- V1_PATCH_SANITY
- V2_TARGETED_BEHAVIOR
- V3_INTEGRATION_BUILD
- V4_RELEASE_CONFIDENCE

Executor results are human-readable first. Machine-readable packets use canonical transport templates where applicable.

## X0/X1 Runtime Mapping

E1 prepares a setup request or execution work package.

`X0_EXECUTOR_PROJECT_SETUP` runs the Executor Project Setup Wizard and returns `executor_setup_result.v1`.

`X1_EXECUTOR_RUN` executes approved `execution_work_package.v1` work and returns `executor_return_packet.v1`.

## Non-Goals

This concept does not by itself:

- install project tooling
- create product/project setup artifacts
- implement Unity-specific or other stack-specific rules
- run product/project execution
- create a Task Master graph

Unity may be considered later as one example of stack-specific tuning. No Unity-specific rule is implemented by this document.

## Implementation Waves Summary

Wave A-B creates the accepted design and contract documentation layer under `workflow/executor/`.

Later waves may add adapter commands and project setup artifacts only when explicitly approved.

## Acceptance Criteria

This baseline is accepted when:

- executor-generic core roles are documented
- Codex is described as the first/default adapter only
- repository maintenance and product execution are separated
- Executor Project Setup is a product execution gate
- core-only setup is valid complete setup
- optional stack-specific tuning is not blind installation
- Task Master and subagent setup decisions are recorded for Codex
- full-trust execution is target-bound
- project-local technical context boundaries are documented
- X0/X1 executor stage routing is clean and registry-owned
- no runtime, registry, prompt, transport, Direction, or product repository files are changed

END_OF_FILE: workflow/executor/EXECUTOR_PROJECT_EXECUTION_CORE_CONCEPT.md
