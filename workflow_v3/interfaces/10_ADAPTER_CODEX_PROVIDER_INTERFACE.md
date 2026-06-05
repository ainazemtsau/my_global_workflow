# Adapter, Codex, and Provider Interface

status: active_interface_layer

## Purpose

This interface defines provider/adapter boundaries.

Embedded adapter use is governed by `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`.

## Adapter classes

Adapters include:

- ChatGPT;
- Codex;
- Claude/future code assistants;
- research agents;
- GitHub access;
- human actions;
- future providers.

## Adapter contract

Adapters receive bounded context in and return evidence/result/limitations out.

Every adapter run must define:

- target;
- source authority;
- bounded context in;
- in scope;
- out of scope;
- expected result;
- evidence required;
- return destination;
- blocked conditions;
- forbidden decisions.

## Adapter limits

Adapters cannot:

- accept state;
- route product meaning;
- expand scope;
- adopt a Direction;
- mutate Direction Map or Active Front by implication;
- silently launch children;
- treat Project Files/Sources as authority over exact repository source.

## Codex

Codex is a bounded repository-work adapter.

Codex handoff must include repository, base ref, target branch/branch policy, allowed paths, forbidden paths, required reads, required changes, validation, stop conditions, commit/push instruction, and requested return fields.

Codex handoff may be embedded as RUN_EXTERNAL_HANDOFF when Codex evidence is needed before completion and the Utility Use Gate passes.

When Codex/storage utility is used for persistence, the handoff must also include explicit approval/update authority, write gate, exact path boundaries, validation, and expected return evidence.

Codex result returns as adapter evidence to the requesting/current chat. When embedded, it returns through RUN_EXTERNAL_RETURN to the same selected owner procedure before FINISH_REQUEST.

Codex result verification must check branch, commit/diff, changed files, allowed paths, forbidden paths, validation output, EOF markers where relevant, project refresh requirements, and residual risks.

Codex must not perform ChatGPT lifecycle FINISH, decide acceptance, or make its output accepted state by itself.

END_OF_FILE: workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md
