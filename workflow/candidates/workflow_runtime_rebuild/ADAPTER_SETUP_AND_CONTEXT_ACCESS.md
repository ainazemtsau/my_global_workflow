# Adapter Setup and Context Access

status: candidate_draft

## Purpose

Этот файл описывает минимальные setup rules для adapters и context access.

Adapters allow different tools and humans to participate in the workflow without becoming core runtime primitives.

Adapters include:

- ChatGPT;
- Codex;
- Claude Code;
- Deep Research;
- GitHub;
- future AI providers;
- human actions.

## Core adapter rule

Adapter can perform a Run or return candidate evidence.

Adapter cannot create Accepted State by itself.

Adapter output is candidate until explicit Acceptance Decision / acceptance-update path.

## Context authority rule

Before material work, context must be classified.

Common context classes:

- canonical storage / GitHub verified source;
- accepted record;
- current human input;
- verified excerpt;
- Project Files cache/context;
- candidate context;
- legacy evidence;
- unknown/unverified.

Project Files are useful context, but they are not truth.

If Project Files conflict with verified canonical source, canonical source wins.

If no canonical source can be read, the adapter must state this limitation.

## Minimum context access check before material work

Before material work, every adapter should answer:

```text
Do I have the Launch Packet?
Do I know the target?
Do I know the source authority?
Do I know what context is verified?
Do I know what context is cache/candidate?
Do I know allowed and forbidden scope?
Do I know expected output?
Do I know evidence requirements?
Do I know where to return the result?
Do I know what I must not decide?
```

If not, adapter must stop or return blocked Result Packet.

## ChatGPT adapter setup concept

ChatGPT is usually used for:

- work planning;
- design drafts;
- parent/integration synthesis;
- child bounded analysis;
- Codex Work Package creation;
- Codex result verification;
- human-readable closure.

ChatGPT setup should provide:

- Project Instructions UI for behavioral rules;
- Project Files/Sources as cache/context;
- Launch Packet for every material chat;
- exact repository refs when source state matters;
- expected Result Packet format;
- exact Next Move requirement.

ChatGPT must not rely on:

- unstated memory;
- old chat continuation;
- stale Project Files as truth;
- hidden accepted state.

If ChatGPT lacks GitHub read, it may work from verified excerpts, but it must mark source limitations.

## Codex adapter setup concept

Codex is used for bounded repository work.

Codex setup requires:

- repository;
- base ref;
- target branch or branch policy;
- allowed paths;
- forbidden paths;
- required changes;
- validation commands/checks;
- commit/push instructions if persistence is authorized;
- return fields.

Codex must stop if repository state makes the package unsafe or ambiguous.

Codex result returns to ChatGPT for verification.

Codex must not be asked to decide acceptance.

## Claude Code / future code assistant setup concept

Claude Code or another code assistant can participate like Codex if it receives equivalent boundaries.

Minimum setup:

- repository/context access method;
- allowed paths;
- forbidden paths;
- task;
- validation;
- stop conditions;
- return packet.

The provider does not become a core runtime primitive.

If it cannot commit/push, it can still return a patch, diff summary or implementation notes as candidate evidence.

If it cannot verify, it must not claim done.

## Deep Research / research agent setup concept

Deep Research or another research agent is used for bounded evidence gathering.

Minimum setup:

- research question;
- why the evidence is needed;
- source requirements;
- allowed/forbidden source types;
- recency/freshness needs;
- expected output format;
- confidence/limitations reporting;
- return destination.

Research agent must not:

- decide route;
- create accepted project facts;
- create implementation scope;
- convert findings into roadmap automatically;
- hide uncertainty.

Research output returns as candidate evidence.

## GitHub / context access expectations

GitHub or canonical repository access is preferred when exact state matters.

A material GitHub read should specify:

- repo;
- ref/branch/commit;
- path;
- whether read was complete;
- whether EOF marker was observed when relevant;
- read limitations.

If a read is truncated, missing, or unverified, do not treat it as authority.

Use exact files, not vague repository memory.

## Project Files as cache/context, not truth

Project Files/Sources help reduce friction, but they may be stale.

They can support:

- orientation;
- setup context;
- repeated rules;
- cached pack content;
- examples.

They cannot by themselves prove:

- accepted Direction state;
- latest repository content;
- active runtime authority;
- successful implementation;
- acceptance.

When Project Files are used materially, Result Packet should say whether exact canonical read was verified or not.

## Fallback if GitHub read is unavailable

If provider cannot read GitHub:

1. Use supplied Launch Packet.
2. Use exact excerpts pasted by user.
3. Use uploaded files only as cache/context.
4. State that GitHub read was unavailable.
5. Avoid claims about files not supplied.
6. Return blocked Result Packet if missing state is material.
7. Ask for exact path/ref/content needed.

Fallback wording:

```text
source_read:
  github_read: unavailable
  fallback_used:
    - Launch Packet
    - user-provided verified excerpt
  limitation:
    repository state outside supplied excerpts was not verified
```

## Human action setup concept

Human action is used when work is external, manual, sensitive, permissioned, account-based, local-device-based or requires human judgment.

Human action setup should include:

- action to perform;
- why it is needed;
- safety/permission boundary;
- expected confirmation;
- evidence to report;
- return destination.

Human confirmation is evidence, but it is not automatically Accepted State unless the acceptance/update path accepts it.

## How another AI provider can participate

A future provider can participate if it can obey packet boundaries.

Minimum requirement:

- receives Launch Packet;
- performs bounded Run;
- returns Result Packet;
- marks source limitations;
- does not mutate Accepted State;
- does not make acceptance decisions;
- provides evidence sufficient for parent verification.

Provider-specific features are adapters. They should not change the runtime model.

## Portability between devices and chats

To keep workflow portable:

- use repo/path/ref source references;
- keep Launch Packet and Result Packet copy-pasteable;
- put results in canonical storage after acceptance;
- do not require one chat's hidden memory;
- summarize evidence in return packets;
- always provide exact Next Move;
- record limitations and unresolved decisions.

## Minimum setup checklist before material work

```text
[ ] Launch Packet present.
[ ] Target is bounded.
[ ] Source authority identified.
[ ] Context access verified or limitation stated.
[ ] Project Files classified as cache/context if used.
[ ] In-scope and out-of-scope boundaries present.
[ ] Expected result present.
[ ] Evidence requirement present.
[ ] Return destination present.
[ ] Adapter forbidden decisions stated.
[ ] Exact Next Move required on closure.
```

If this checklist fails, the adapter should not proceed as if the work is safe.

END_OF_FILE: workflow/candidates/workflow_runtime_rebuild/ADAPTER_SETUP_AND_CONTEXT_ACCESS.md
