# Workflow v3 Generic AI Provider Setup

status: active_skeleton_namespace_corrected

## Purpose

This file defines setup expectations for ChatGPT, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub context access, human actions, and generic future AI providers.

Providers are adapters. They do not become runtime authority or acceptance authority.

## Minimum provider contract

Every provider must:

- receive a Launch Packet or bounded equivalent;
- perform a bounded Run;
- return evidence, output, and limitations in the expected return shape;
- state source limitations;
- not create Accepted State;
- not decide acceptance, route, product meaning, or scope expansion.

## Shared setup fields

```text
provider:
role:
repository_or_context_access:
source_refs:
context_included:
in_scope:
out_of_scope:
expected_result:
evidence_required:
return_to:
blocked_if:
forbidden_decisions:
```

## ChatGPT

ChatGPT is used for planning, synthesis, bounded work chats, child/parent coordination, code-assistant work package creation, returned evidence verification, and human-readable closure.

ChatGPT setup requires compact Project Instructions UI, exact source refs when state matters, Project Files/Sources classified as cache/context, and explicit Operator Brief, START_CONTRACT, STAGE_RESULT, CHILD_PROCEDURE_CALL / CHILD_PROCEDURE_RETURN, RUN_WAITING_FOR_CHILD_RETURN, CHILD_RETURN_VERIFICATION, CLOSURE_CHECK, FINISH_PACKET, and post-closed NEXT_CHAT_CARD or no_next_chat_needed boundaries. Legacy UTILITY_CALL / UTILITY_RETURN labels are compatibility aliases only for child/adaptor packets.

## Codex

Codex is used for bounded repository work.

Codex setup requires repository, base ref, target branch or branch policy, allowed paths, forbidden paths, required changes, validation, stop conditions, commit/push instructions when authorized, requested return fields, expected `CHILD_PROCEDURE_RETURN`, and parent verification contract.

Codex must stop when repository state, source access, branch state, or validation makes the package unsafe.

## Claude Code / future code assistants

Claude Code or a future code assistant may participate if it receives equivalent code-assistant boundaries.

If it cannot commit or push, it may return a patch, diff summary, implementation notes, or validation evidence as candidate output.

It must not claim done without validation.

## Deep Research / research agents

Research agents perform bounded evidence or freshness checks.

Setup requires a research question, source requirements, allowed/forbidden sources, recency needs, expected finding format, confidence/limitations reporting, and return destination.

Research output is candidate evidence, not accepted state.

## GitHub context access

GitHub or exact repository access is preferred when source state matters.

A material read should name repository, ref/branch/commit, path, read completeness, EOF marker status when relevant, and limitations.

If GitHub access is unavailable, use verified excerpts and mark limitations. Do not claim state outside supplied evidence.

## Human actions

Human actions cover external, manual, sensitive, permissioned, account-based, local-device, or judgment-dependent work.

Setup requires the action, reason, safety/permission boundary, expected confirmation, evidence to report, and return destination.

Human confirmation is evidence, not automatic accepted state.

## Generic future AI provider

A future provider may participate if it can obey packet boundaries, source limitations, and acceptance boundaries.

Provider-specific features are adapter features only. They do not change Workflow v3 authority, accepted-state rules, or Project setup boundaries.

END_OF_FILE: workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md
