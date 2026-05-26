---
artifact_control:
  namespace: workflow
  artifact_type: transport_protocol
  status: project_instruction_budget_residual_sweep
  owner: workflow_os
---

# Transport Protocol

## Transport Boundary

Transport is serialization, not semantic authority.

Transport artifacts carry instructions, context, missing-context requests, decisions, receipts, and commit proposals. They do not create accepted state unless Verify and Commit produce a committed Ledger delta.

Transport may carry accepted state, candidate context, projections, or legacy evidence.

Transport must label authority status when material.

## Transport Flow

Chat A does not communicate by memory with Chat B.

Chat A emits transport artifact.

Chat B consumes transport artifact.

Durable state changes only through committed Ledger delta.

## Launch Card

Launch Card serializes Operator invocation over one Obligation.

It binds:

- target Obligation
- selected Operator
- Ledger snapshot reference
- Commit Scope reference
- accepted state references
- candidate context references
- projection context references
- legacy context references
- verification policy
- human and tool gates
- stop conditions
- return target

Launch Card should separate `accepted_state_refs` from `candidate_context_refs` and `legacy_context_refs`.

Launch Card is not a legacy stage launch and does not authorize work outside its target Obligation.

## Receipt Card

Receipt Card serializes a Receipt.

It records the outcome of one Operator invocation and includes produced claims, evidence, assumptions, residual Obligations, invariant checks, verification policy result, and commit recommendation.

Receipt Card is candidate state until committed.

Receipt Card = proof result.

If a Receipt needs persistence, it should be accompanied by a Codex Commit Handoff Card unless commit is intentionally deferred.

## Context Request Card

Context Request Card serializes missing blocking context.

It must name the smallest sufficient context needed to continue and explain why continuing without it is unsafe.

## Child Obligation Request Card

Child Obligation Request Card serializes one copy-paste runnable child request from a parent Operator invocation.

It names the parent Obligation, child Obligation, launch order, child prompt, forbidden actions, expected result, return instruction, and recovery reference.

## Child Result Return Card

Child Result Return Card serializes compact child output for parent synthesis.

It is candidate parent input, not Ledger state.

## Parent Recovery Block

Parent Recovery Block serializes enough parent state to recover if the parent chat is lost.

It lists child requests, received results, missing required results, synthesis rules, conflict policy, and copy-paste recovery prompt.

## Human Decision Card

Human Decision Card serializes a human-owned decision request.

It may present options, consequences, and recommendation if any. It must not write the user's decision for them.

## Commit Packet

Commit Packet serializes proposed commit and verification state.

It connects Receipt IDs, target Commit Scope, proposed Ledger delta, verification results, invariant results, verification policy result, human gate result, and storage or projection updates required after commit.

## Codex Commit Handoff Card

Codex Commit Handoff Card serializes a copy-paste repository maintenance request for Codex.

Commit Handoff Card = copy-paste repository maintenance instruction for Codex.

It is a transport adapter, not semantic authority.

It must be self-contained.

It must include repository, worktree, branch, mode, allowed paths, forbidden paths, protected paths, git behavior, commit behavior, push behavior, and no-main-merge behavior.

It is distinct from product/project execution and must not ask the user to infer repository paths, execution boundaries, or validation steps from the Receipt.

It must include separated project refresh requirements when changed files affect ChatGPT Projects.

Separated project refresh requirements must distinguish:

- `project_instruction_ui_update_required`
- `project_instruction_ui_payload_char_counts` when Project Instructions UI sources change
- `project_sources_files_refresh_required`
- `request_only_sources_refresh_required`
- `do_not_upload_as_project_file`

## Codex Execution Launch Card

Codex Execution Launch Card serializes one CodexRun over one execution Obligation.

It is for product/project execution and is distinct from Codex Commit Handoff Card, which is repository maintenance after a Receipt.

## Execution Receipt Card

Execution Receipt Card serializes the return from one execution Operator invocation.

It records changed surfaces, commands, validation receipts, reviewer/subagent receipts, technical memory delta, unresolved risks, rollback notes, ledger delta proposal, and commit recommendation.

## Project Setup Receipt Card

Project Setup Receipt Card serializes target binding, setup status, setup gaps, validation profile status, module map status, and next allowed execution.

## Validation Receipt Card

Validation Receipt Card serializes validation matrix, required and omitted levels, commands or checks run, evidence, failures, validation gaps, and commit allowance.

## Human Action Card

Human Action Card serializes human-guided execution steps, stop conditions, expected visible result, evidence to return, and human confirmation receipt.

## Proof Relationship

Transport artifacts are not proof unless they contain or point to a valid Receipt.

A transport artifact may support verification, but accepted state requires a committed Ledger delta.

END_OF_FILE: workflow/policies/04_TRANSPORT_PROTOCOL.md
