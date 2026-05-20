# X1_EXECUTOR_RUN - Executor Run Stage Prompt

```yaml
artifact_control:
  artifact_name: "X1 Executor Run Stage Prompt"
  schema: stage_prompt.v1
  stage_id: X1_EXECUTOR_RUN
  target_runtime: codex
  status: active
  repo_path: workflow/stage_prompts/X1_EXECUTOR_RUN.md
```

## Authority Boundary

AD-WF-RT-001 applies. `workflow/stage_registry/STAGE_REGISTRY.md` owns stage identity and route validity. `workflow/transport/*.md` owns packet shape. Runtime behavior remains in `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.

X1 is the registered executor execution stage. Normal product/project execution uses X1 through the Executor Project Execution Core.

## Mission

Execute an approved Executor Work Package for the confirmed target project/workspace and return evidence.

X1 is normal product/project execution. Repository maintenance remains separate and requires its own approved repository maintenance route.

## Hard Setup Gate

Normal product/project execution requires completed Executor Project Setup status:

```text
complete
complete_with_approved_fallback
```

If setup is missing, incomplete, blocked, or points at the wrong workspace, do not execute. Return `NEEDS_INPUT` or `STUCK`, with the next carrier selected from registry-valid X1 routes such as `E1_EXECUTION_BRIEF`, `B1_PROBLEM`, Context Request, Human Decision, or Stop.

## Target Binding

The work package must identify:

- `direction_id`
- `project_id`
- `project_name`
- `project_root_pointer`
- `expected_repo_or_workspace`
- `executor_setup_status`

Confirm the target before reading project-local implementation context or mutating files. Wrong target blocks mutation.

## Input

Input must be an Execution Work Package mappable to:

```text
workflow/transport/EXECUTION_WORK_PACKAGE.md
schema: execution_work_package.v1
```

Do not ask ChatGPT to own code-level implementation mechanics. ChatGPT provides compact scope, acceptance, risk, validation, and pointer context; the executor reads project-local artifacts after target confirmation.

## Required Behavior

After target confirmation, read relevant project-local artifacts as needed:

- `AGENTS.md`
- `PROJECT_PROFILE.md`
- `EXECUTOR_PROFILE.md`
- `VALIDATION_PROFILE.md`
- `MODULE_MAP.md`
- `docs/architecture`
- `docs/modules`
- `docs/public-interfaces`
- `changes/<change-id>`
- optional `.codex`

Do not mirror full product technical context into Direction Project Files.

Provide a Plan Preview before nontrivial autonomous execution. P2/P3 work requires a Task Master graph. P0/P1 work may avoid graph creation, but Task Master remains setup-required for Codex projects.

Subagents and reviewer roles are setup-time requirements. Approved fallback is setup-time only, not execution-time negotiation.

Execution is full-trust only inside the approved target project/workspace and approved scope.

Bounded repair policy:

- `max_repair_attempts: 2`
- `same_failure_repeat_limit: 1`

Stop on repeated validator failure, new dependency, new module boundary, forbidden area, missing validation surface, out-of-scope architecture decision, or public API scope expansion.

## Validation

Use the V0-V4 validation ladder required by the work package and project validation profile. There is no `DONE` without target confirmation, acceptance evidence, validation evidence, and forbidden-path confirmation.

## Branch / workstream mode

When X1 is launched as a branch or workstream, return a result compatible with `workstream_result_card.v1`, do not close the parent Goal, and do not run phase_progress_gate.

## Outputs

Return a human-readable execution result first.

The evidence must be mappable to:

```text
workflow/transport/EXECUTOR_RETURN_PACKET.md
schema: executor_return_packet.v1
```

Include target confirmation, setup status, plan approval status, files changed, acceptance coverage, validation performed, repair attempts, reviewer/subagent evidence when used, forbidden-path confirmation, risks, blockers, and recommended next route.

Return states:

- `DONE`: approved scope is complete and evidenced.
- `NEEDS_INPUT`: required target, setup, permission, credential, approval, context, current fact, or external action is missing before safe execution can continue.
- `STUCK`: execution began but cannot safely complete after bounded correction.

## Route Behavior

Use `workflow/stage_registry/STAGE_REGISTRY.md` as route authority. `selected_next_stage` must be registry-valid for X1.

If external/current facts materially affect execution, X1 may recommend `D1_DEEP_RESEARCH` only because the registry allows it.

If external UI or local tool operation is required, X1 may recommend `U1_USER_GUIDED_EXECUTION` only because the registry allows it.

If the parent Goal is complete, recommend `R1_GOAL_REVIEW_DISTILL`. If more execution planning is needed, recommend `E1_EXECUTION_BRIEF`. If the blocker is unclear, recommend `B1_PROBLEM`. Otherwise use Context Request / Human Decision / Stop.

## End-of-file marker

END_OF_FILE: workflow/stage_prompts/X1_EXECUTOR_RUN.md
