# Workflow v3 Execution Surface Setup

status: active_skeleton_namespace_corrected

## Purpose

This file defines setup expectations for ChatGPT, the Code Assistant Development Runtime, research agents, GitHub context access, human actions, and future execution surfaces.

Execution surfaces do not become Workflow runtime authority or acceptance authority.

## Minimum Execution-Surface Contract

Every execution surface must:

- receive a bounded packet or explicit task frame;
- perform a bounded Run;
- return evidence, output, and limitations in the expected return shape;
- state source limitations;
- not create Accepted State;
- not decide acceptance, route, product meaning, or scope expansion.

## Shared setup fields

```text
execution_surface:
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

ChatGPT is used for planning, synthesis, bounded work chats, dependency/parent coordination, code repository dependency call creation, returned evidence verification, and human-readable closure.

ChatGPT setup requires compact Project Instructions UI, exact source refs when state matters, Project Files/Sources classified as cache/context, and explicit Operator Brief, START_CONTRACT, STAGE_RESULT, DEPENDENCY_CALL / DEPENDENCY_RETURN, RUN_WAITING_FOR_DEPENDENCY_RETURN, DEPENDENCY_RETURN_VERIFICATION, CLOSURE_CHECK, FINISH_PACKET, and post-closed NEXT_CHAT_CARD or no_next_chat_needed boundaries. Prior packet labels are unsupported.

## Code Assistant Development Runtime

The Code Assistant Development Runtime is used for bounded repository work. Codex is the current code assistant execution surface instance.

Code repository dependency setup requires repository, repository role, target integration ref, expected base commit SHA, workspace policy id, integration policy id, allowed paths, forbidden paths, required changes, validation, stop conditions, expected `DEPENDENCY_RETURN`, project refresh requirements, and parent verification contract.

The dependency call sends intent, source authority, path boundaries, validation, target integration evidence requirements, and acceptance boundary. The Code Assistant Development Runtime owns internal workspace/ref/branch/commit/rebase/merge/push mechanics and reports those details only as return evidence.

Required return evidence includes observed base commit SHA, base match, workspace binding used, internal work ref, internal branch if any, changed files, forbidden and unlisted paths, validation output, result commit SHA, integration requirement, integration status, final target commit SHA, target containment proof, remote verification, push status, pending integration reason when applicable, exact next action when not integrated, project refresh requirements, and residual risks.

The Code Assistant Development Runtime must stop or return blocked when repository state, source access, workspace binding, target integration evidence, or validation makes the package unsafe. It must not claim acceptance, CHECK, FINISH, or CLOSED.

## Claude Code / future code assistants

Claude Code or a future code assistant may participate if it receives equivalent code repository dependency boundaries.

If it cannot integrate to the target ref, it must return `integration_status: not_integrated_blocked` or another exact non-integrated status, with the reason and exact next action.

It must not claim done without validation.

## Deep Research / research agents

Research agents perform bounded evidence or freshness checks.

Setup requires a research question, source requirements, allowed/forbidden sources, recency needs, expected finding format, confidence/limitations reporting, and return destination.

Research output is candidate evidence, not accepted state.

## GitHub context access

GitHub or exact repository access is preferred when source state matters.

A material read should name repository, ref/commit, path, read completeness, EOF marker status when relevant, and limitations.

If GitHub access is unavailable, use verified excerpts and mark limitations. Do not claim state outside supplied evidence.

## Human actions

Human actions cover external, manual, sensitive, permissioned, account-based, local-device, or judgment-dependent work.

Setup requires the action, reason, safety/permission boundary, expected confirmation, evidence to report, and return destination.

Human confirmation is evidence, not automatic accepted state.

## Future Execution Surfaces

A future execution surface may participate if it can obey packet boundaries, source limitations, dependency return evidence requirements, and acceptance boundaries.

Surface-specific features do not change Workflow v3 authority, accepted-state rules, or Project setup boundaries.

END_OF_FILE: workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md
