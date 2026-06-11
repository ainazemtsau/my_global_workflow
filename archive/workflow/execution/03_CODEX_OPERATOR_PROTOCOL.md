---
artifact_control:
  namespace: workflow
  artifact_type: codex_operator_protocol
  status: gate_2_initial
  owner: workflow_os
---

# Codex Operator Protocol

## Boundary

CodexRun is one Operator invocation over one execution Obligation.

CodexRun is not the execution system.

CodexRun must return an Execution Receipt or a blocking transport card.

## Modes

Codex operator modes:

- `plan_only`
- `read_only_discovery`
- `workspace_write`
- `validate_only`
- `repair`
- `review_only`
- `project_setup`

Mode does not override the Obligation, Launch Card, verification policy, or allowed/forbidden surfaces.

## Preconditions

No CodexRun without:

- target binding receipt
- setup or setup-gap receipt
- execution readiness receipt
- validation plan receipt
- Codex Execution Launch Card

The launch card must include the task statement, acceptance predicate, validation plan, non-goals, allowed changes, forbidden changes, stop conditions, and return schema.

## Return Contract

Codex must return an Execution Receipt that records:

- status
- changed surfaces/files
- commands run
- validation receipt references
- subagent/reviewer receipt references
- unresolved risks
- rollback notes
- technical memory delta
- ledger delta proposal
- commit recommendation

No validation receipt -> no done.

## Subagent And Reviewer Protocol

Required reviewers or subagents must be listed in the launch card.

If required reviewers or subagents are listed in launch and missing from return, the Execution Receipt is invalid.

Read/review subagents are the safer default.

Parallel write is denied unless disjoint paths or worktrees and an integration plan are proven before launch.

Product/project mutation uses one writer by default.

END_OF_FILE: workflow/execution/03_CODEX_OPERATOR_PROTOCOL.md
