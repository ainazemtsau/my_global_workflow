# Codex Adapter

status: adapter_first

## Purpose

This document defines Codex as the first/default executor adapter for the Executor Project Execution Core. Codex is not the permanent architecture lock-in. Generic executor rules live in the core documents; Codex-specific setup and execution requirements live here.

This file is a documentation contract for the Codex adapter under the generic Executor stages. It does not register adapter-specific stages.

## Adapter Command Concepts

Codex setup and maintenance command concepts:

- `/executor:init-project`
- `/executor:doctor`
- `/executor:update-project-profile`
- `/executor:add-validator`
- `/executor:add-tool`
- `/executor:research-tools`
- `/executor:promote-learning`

These are command concepts for adapter implementation. They are not registered stages.

## Required Setup

Codex project setup must install, configure, and verify:

- Task Master installed, configured, and project-bound
- subagents and reviewer roles configured and verified
- validation profile verified
- module map verified
- `AGENTS.md` verified
- project profile verified
- executor profile verified
- doctor checks passing

Task Master is required and verified during setup. Subagents and reviewer roles are setup-time requirements.

If true subagents or required baseline tools cannot be configured, setup must stop and request a setup-time fallback decision. Normal execution assumes setup is complete and does not renegotiate fallback.

Codex setup runs through `X0_EXECUTOR_PROJECT_SETUP`. Normal Codex product/project execution runs through `X1_EXECUTOR_RUN`.

## Full-Trust Target-Bound Execution

After user authorization and completed setup, Codex runs in full-trust mode inside the target project workspace only. Full trust does not apply to sibling Directions, unrelated repositories, workflow repository maintenance paths, or external systems outside the approved target.

Required target binding fields:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Wrong target or workspace blocks execution.

## Target Check Before Work

Before material work, Codex must:

- confirm the current directory or workspace matches `project_root_pointer`
- confirm repository/workspace identity matches `expected_repo_or_workspace`
- confirm setup status is acceptable
- read project-local `AGENTS.md`
- read project and executor profiles
- read validation profile and module map
- stop on mismatch or missing required setup

## Plan Preview

Codex must provide a human-readable Plan Preview before nontrivial autonomous work. The preview includes:

- target confirmation
- planning mode
- files or modules likely to be touched
- existing-code/reuse discovery plan
- Task Master graph requirement, if any
- validation ladder level
- repair limits
- stop conditions
- evidence expected on return

User approval of the readable plan is required before nontrivial autonomous execution.

## Task Master Graph Requirement

P2 and P3 Codex tasks must use a Task Master graph.

P0 and P1 tasks may not require graph creation, but Task Master remains installed, configured, verified, and available after setup.

Task Master is a graph substrate. It is not execution authority, DONE authority, process authority, or the control plane.

## Bounded Repair Loop

Default Codex repair policy:

- `max_repair_attempts: 2`
- `same_failure_repeat_limit: 1`

Codex stops when repair would introduce a new dependency, cross a new module boundary, touch a forbidden area, expand public API scope, require an out-of-scope architecture decision, hide a missing validation surface, or repeat the same validator failure.

## Evidence and DONE

Codex cannot claim DONE without validation and evidence.

Return evidence should include:

- target confirmation
- setup status
- planning mode
- Task Master graph summary for P2/P3
- files changed
- acceptance mapping
- validators run
- command output summaries
- repair attempts, if any
- reviewer/subagent evidence when required
- forbidden-path confirmation
- remaining risks
- next route

## Return Evidence Format

Codex returns human-readable evidence first. Normal execution return evidence should be mappable to `workflow/transport/EXECUTOR_RETURN_PACKET.md`.

```text
codex_executor_result:
  status:
  target_project_ref:
  setup_status:
  planning_mode:
  task_master_graph_used:
  files_changed:
  validation_performed:
  acceptance_evidence:
  repair_attempts:
  blockers:
  next_route:
```

## Separation From Codex Repository Maintenance

Codex repository maintenance is separate from Codex product/project execution.

Repository maintenance applies approved workflow repository changes and returns read-back, diff, validation, commit, and push evidence. It does not require product Executor Project Setup and must not mutate product repositories.

Product/project execution requires completed Executor Project Setup in the target project workspace and remains target-bound to that workspace.

END_OF_FILE: workflow/executor/adapters/CODEX_ADAPTER.md
