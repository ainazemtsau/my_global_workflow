# Adapter, Codex, and Provider Interface

status: active_interface_layer

## Purpose

This file defines Workflow v3 boundaries for AI, human, tool, repository, and future-provider adapters.

## Owner/surface

Owner/surface: ChatGPT, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub access, human actions, and future provider boundaries.

## Persistence target

Persistence target: `workflow_v3/interfaces/07_ADAPTER_CODEX_PROVIDER_INTERFACE.md` for shared rules; future adopted Direction adapter config belongs under `directions_v3/<direction-id>/runtime/config/**` after explicit adoption and acceptance.

## Adapter contract

A provider receives bounded launch/context and returns evidence, result, and limitations.

An adapter cannot accept state, decide route, expand scope, decide product meaning, import legacy state, adopt a Direction, update Project UI, refresh Project Files/Sources, or become runtime authority.

## Provider surfaces

ChatGPT may plan, synthesize, coordinate parent/child work, create Codex work packages, verify Codex results, and close work with Result Packet plus Event Loop Closure.

Codex performs bounded repository work.

Claude Code/future code assistants may perform bounded code or repository work when given equivalent boundaries.

Deep Research/research agents perform bounded evidence or freshness checks.

GitHub access is used for exact repository, PR, issue, commit, branch, and CI context when needed.

Human actions cover external, manual, sensitive, permissioned, account-based, local-device, or judgment-dependent work.

Future providers may participate only when they obey the packet, source, evidence, and acceptance boundaries.

## Codex branch policy

Codex repository work must state:

- repository;
- base ref or SHA;
- branch name or branch policy;
- allowed paths;
- forbidden paths;
- required reads;
- required changes;
- validation;
- stop conditions;
- commit and push instructions when authorized;
- requested return fields.

Codex must not push to `main` directly unless a package explicitly authorizes that. Review branch work must use the requested review branch.

No parallel Codex commits may target overlapping paths without integration ownership.

## Codex stop conditions

Codex must stop when:

- required source cannot be read completely;
- repository state contradicts the package;
- branch state is unsafe;
- validation cannot verify changed files or EOF markers;
- forbidden paths would be needed;
- a real Direction adoption target must be chosen without authority;
- actual Project UI update or Project Files/Sources refresh would be required;
- old Workflow OS decommission, legacy import, or migration would be implied.

## Codex result verification return path

Codex results return as candidate evidence to the current chat or named verification destination.

Verification must check branch, base SHA, commit SHA, changed files, allowed paths, forbidden paths unchanged, validation results, EOF markers, Project setup refresh categories, push status, contradictions, unresolved questions, and residual risks.

Codex does not accept its own result.

## Inputs

Inputs are Launch Packets, Transition Packets, bounded context, exact source refs, adapter setup fields, credentials/permissions when applicable, and return requirements.

## Outputs

Outputs are Result Packets, evidence, limitations, diffs, commits, validation logs, research findings, human confirmations, blocked results, and return packets.

## State mutation rights

Adapters may mutate repository files only when explicitly authorized by scope and path.

Adapters do not mutate accepted state by outputting a result. Accepted state changes require explicit acceptance/update after verification.

Adapters do not update actual ChatGPT Projects unless a separate authorized human or tool action explicitly performs that external update.

## Allowed producers

Allowed producers are ChatGPT, Codex, Claude Code/future code assistants, Deep Research/research agents, GitHub tools, humans, and future providers operating under a bounded packet.

## Allowed consumers

Allowed consumers are parent chats, Codex result verification, Acceptance review, Event Loop Closure, Progression Router, Project setup, quality gates, and future adapter config.

## Validation/evidence requirement

Each adapter result must state source limitations, evidence, validation performed or not performed, what changed, what did not change, and where the result returns.

## Forbidden behaviors

- Black-box adapter output.
- Provider deciding acceptance or route.
- Provider expanding scope silently.
- Provider adopting a Direction or importing legacy state.
- Provider updating Project UI or Project Files/Sources by implication.
- Codex claiming done after failed validation.
- Codex continuing after a stop condition.
- Human action treated as complete without confirmation.

## Failure/recovery path

If adapter limitations block the work, return a blocked result with exact missing source, permission, credential, or validation.

If output is incomplete, return for repair or Codex result verification.

If acceptance is unclear, request human/parent decision.

If scope expands across surfaces, split into an integration package.

## Dependencies

- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`
- `workflow_v3/templates/TRANSITION_PACKET_TEMPLATE.md`

END_OF_FILE: workflow_v3/interfaces/07_ADAPTER_CODEX_PROVIDER_INTERFACE.md
