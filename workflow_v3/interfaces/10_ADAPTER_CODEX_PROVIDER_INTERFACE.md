# Adapter, Codex, and Provider Interface

status: active_interface_layer

## Purpose

This interface defines provider/adapter boundaries.

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

Codex result returns to the requesting/current chat for verification and FINISH closure.

Codex result verification must check branch, commit/diff, changed files, allowed paths, forbidden paths, validation output, EOF markers where relevant, project refresh requirements, and residual risks.

END_OF_FILE: workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md
