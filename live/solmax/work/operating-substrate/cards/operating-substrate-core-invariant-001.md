# Operating-substrate architecture card — core invariant

status: accepted
accepted_at: 2026-07-10
session: s-solmax-operating-substrate-core-invariant-architecture-forge-001
call: c-solmax-operating-substrate-core-invariant-architecture-forge-001
card_id: operating-substrate-core-invariant-001
graph_nodes:
  - q01_core_invariant

## Owner approval

words: |
  "я approve версию 1, вариант А"

preceding_alignment_words: |
  "то, что ты расписала, я со всем согласен"

clarification_words: |
  "для сообщения должен быть какой-то формат, для чата, возможно,
  какой-то формат"
  "writer — это отдельная задача"
  "своя валидация должна быть"
  "что точно должно быть в каком-то виде, я должен получить индекс,
  который могу скопировать и вставить в новый чат"
  "я могу легко получить следующий шаг при завершении чата"

carrier_and_automation_words: |
  "сейчас это как просто Markdown-файл"
  "в будущем есть планы делать это более автоматизировано"
  "либо засунуть в какое-нибудь приложение"
  "может какие-то автоматические проверки, чтобы тулзы вызывались правильно"

## Question

Какая core invariant делает operating-substrate универсальной основой,
на базе которой можно создавать разные кастомные AI-процессы?

## Frozen answer

Operating-substrate is a stable, model-neutral, carrier-neutral and
owner-tuned AI-process kernel with pluggable process packs.

It is the common operating layer on which Health-like, Zaratusta-like,
game-like, architecture-like and future custom AI-processes can be built.

A concrete process is created by installing a process pack into the
kernel, not by modifying or forking the kernel for that domain.

The kernel's invariant is an explicit process-execution contract:
regardless of domain, model or carrier, the process follows the same
semantics for bounded work, procedure invocation, routing, delegation,
communication, continuity, authority, evidence and governed change.

These are architectural responsibility classes, not a frozen list of
implementation modules, files, services or APIs.

## Kernel responsibility classes

### 1. Bounded run/session semantics

Every working unit has an explicit identity, goal, context, boundaries,
active procedure or routing decision, available authority, expected
return and close/checkpoint condition.

"One chat = one task" is a strong current pattern and evidence anchor.
The carrier-neutral invariant is one bounded run = one explicit unit of
work. The exact relationship between chat, thread, run and task remains
a downstream entity-model question.

### 2. Procedure invocation and routing

Procedures are first-class process definitions rather than informal
prompt suggestions.

The kernel defines that the active procedure, its invocation reason,
required context, allowed effects, completion contract, uncertainty path
and delegation behavior must be explicit.

Concrete procedure catalogues and domain routing rules live in process
packs.

### 3. Controlled delegation and child work

Child chat, research, executor, verifier and other delegated work are
bounded invocations with an explicit parent, goal, context, boundaries,
return contract and route-back.

The exact taxonomy of child roles and the mechanism that creates them are
not frozen here.

### 4. Structured communication and continuation

Runs, processes and agents do not rely only on unstructured conversation
history. The kernel defines stable communication meanings such as:

- invocation/request;
- completion/result;
- owner decision;
- gap or unresolved prerequisite;
- evidence;
- proposed durable change;
- continuation/next route.

Exact message schemas, field names and serialization are downstream.

Every completed or checkpointed run must produce a portable continuation
index: a self-contained handoff containing enough outcome, evidence,
unresolved state and next-invocation information to continue in another
chat/run/model or through future automation.

In the current Markdown/chat carrier, this index must be copyable by the
owner into a new chat without reconstructing the previous conversation
from memory.

### 5. State, memory, source and history discipline

The kernel requires explicit separation between at least these concerns:

- current run context and trace;
- durable process state;
- longer-term memory;
- sources and artifacts;
- accepted configuration and procedure definitions;
- audit/history/evidence.

The exact state planes, schemas, storage and process-specific memory
shape remain downstream.

### 6. Authority, effects and durable-mutation boundary

Reasoning does not silently become durable truth or an external effect.

The kernel requires explicit boundaries for:

- owner decisions;
- accepted architecture/process changes;
- durable state mutation;
- external, irreversible or spend-incurring effects;
- validation and evidence before applying a change.

A run may propose a change, but application of durable changes must cross
a validated writer/apply boundary.

A separate writer chat, agent or procedure is a strong current pattern:
writing is its own bounded task with its own rules and validation.
This card does not freeze that the physical implementation must always be
a separate agent or chat. It freezes the mutation boundary and validation
responsibility.

### 7. Capability, tool, model and carrier boundary

Models, tools, research, code agents, repositories, applications and
storage are capabilities/adapters used by the kernel.

They may improve execution but cannot redefine kernel semantics.

Tool declarations, permission models, exact adapter contracts and
provider selection remain downstream.

### 8. Evidence, trace, replay and recovery

A run must leave enough structured evidence to understand what became
true, what was attempted, what remains unresolved and how work can be
verified, resumed or refuted.

Exact tracing technology and proof harness are not frozen.

### 9. Owner-interface discipline

The kernel supports stable cross-process owner-facing rules, including:

- owner language;
- decision presentation;
- when to ask and when to proceed;
- preferred level of initiative;
- explanation and handoff style;
- authority and approval expectations.

The universal kernel supports this owner-profile layer. The owner's
concrete facts, preferences and policies are not universal substrate
architecture.

### 10. Governed evolution

Failures, contradictions and missing capabilities produce explicit gaps,
research questions or proposed process/kernel changes.

Process packs and the kernel do not mutate through hidden prompt drift.

Kernel evolution remains possible, but only as explicit, versioned and
evidence-gated architecture work.

## Architectural roles

### Kernel

Stable process-execution semantics shared by all custom AI-processes.

### Process pack

A pluggable description of a concrete process, potentially including:

- procedures;
- process-specific routing declarations;
- domain vocabulary;
- local policies;
- local state/memory shape;
- source and capability bindings;
- proof scenarios;
- optional style overlays.

A process pack fills declared extension points. It does not redefine
kernel semantics.

### Owner profile

Cross-process owner-specific interaction rules, preferences, authority
expectations and approved shared context.

The kernel supports this layer; its concrete content is not universal.

### Capability/carrier adapter

Connection to a concrete LLM, tool, research system, coding agent,
repository, storage medium, chat surface, application or service.

Adapters implement capabilities without becoming architectural authority.

### Bootstrap carrier

The current simple representation of kernel contracts in Markdown,
documents and chat.

Markdown is a starting medium for testing and refining processes. It is
not frozen as the permanent carrier.

### Portable continuation index

A copyable or machine-routable close/checkpoint artifact that allows the
next run to begin without depending on the previous chat remaining open
or on the owner's memory.

Its exact schema remains downstream.

## Model-strength amplification

A new and more capable LLM strengthens the kernel's execution rather than
replacing the kernel.

It may improve:

- understanding of owner intent;
- procedure adherence;
- routing and uncertainty detection;
- research depth;
- tool use;
- handback quality;
- contradiction and gap detection.

It does not require redefining:

- work-unit semantics;
- procedure invocation;
- delegation contracts;
- authority boundaries;
- durable-change rules;
- evidence and continuation responsibilities.

The model supplies stronger intelligence. The kernel supplies the stable
form in which that intelligence operates.

## Current carrier and future automation

Current mode:

- Markdown and chat hold rules, procedures and handoffs;
- the owner can inspect and copy continuation packets;
- validation is partly procedural and partly performed by LLM/owner;
- processes can be tested before automating them.

Possible future mode:

- application or service;
- machine-readable process packs;
- automated procedure selection;
- schema and conformance validation;
- permission enforcement;
- tool routing;
- memory retrieval;
- automatic writer/apply execution;
- trace/replay and process checks.

Future automation must implement accepted kernel semantics. It must not
silently redefine them.

## Not frozen

This card does not freeze:

- final service-block list;
- whether every responsibility class becomes a separate service zone;
- exact entity model;
- message or packet schemas;
- chat/thread/run representation;
- procedure syntax;
- child-process taxonomy;
- state or memory schemas;
- storage or repository;
- Markdown layout;
- writer implementation topology;
- application/backend architecture;
- provider or model;
- tool framework;
- routing implementation;
- proof harness;
- concrete owner-profile contents;
- concrete process packs.

## Rejected alternatives

1. Domain-adaptive kernel

   Rejected because different processes would gradually fork the common
   rules and cease to share one operating substrate.

2. Universal lifecycle as the core invariant

   Rejected because a lifecycle does not define the full semantics of
   procedure invocation, delegation, state, authority, evidence and
   governed evolution.

3. Discovery loop as the primary substrate answer

   Rejected because every process would repeatedly reinvent common
   operating mechanisms.

4. Literal copy of Direction OS

   Rejected because Direction OS is evidence and a working prototype of
   useful patterns, not universal authority. Its file names, play names,
   packet schemas, writer mechanics and policies remain open to
   abstraction and improvement.

5. Prompt file for one current model

   Rejected because the kernel must survive model changes and become
   stronger when models improve.

6. Markdown/GitHub as permanent architecture

   Rejected because they are current carriers, not substrate truth.

7. Application or automation first

   Rejected because implementation would prematurely freeze contracts
   that are still being architecturally developed.

8. Unstructured chat history as handoff

   Rejected because the next run would depend on the previous chat,
   model context window and owner's memory rather than a portable
   continuation contract.

9. Silent state writing by the reasoning run

   Rejected because durable mutation requires explicit authority,
   validation, evidence and recoverability.

## Spawned entities and questions

### Inline minimal definitions

- Kernel: stable shared process-execution semantics.
- Process pack: pluggable concrete-process definition.
- Owner profile: cross-process owner-specific rules and approved context.
- Adapter: connection to model, tool or carrier.
- Bounded run: explicit unit of work.
- Portable continuation index: self-contained next-run handoff.
- Mutation boundary: separation between proposing and applying durable
  effects.
- Writer/apply role: the validated responsibility that applies durable
  changes; exact physical topology remains open.
- Bootstrap carrier: current simple Markdown/chat realization.

### Child questions

1. Kernel entity model:
   What exactly are run, session, chat, task, procedure, invocation,
   child work, result, gap, capability and state transition?

2. Process-pack contract:
   What must every pack declare, and what kernel semantics may it never
   override?

3. Owner-profile boundary:
   What is stable cross-process owner context/policy, and what remains
   local to a process?

4. Message/chat/continuation contract:
   What semantic message types and close/checkpoint information are
   required, independent of exact serialization?

5. Mutation/writer contract:
   What must be validated before a durable change is applied, and what
   evidence must the apply role return?

### Downstream elaborations

- Q2: classify kernel responsibilities, reusable service semantics,
  process-pack declarations, owner-profile concerns and adapters.
- Q3: responsibility relationships.
- Q4: process-pack instantiation.
- Q5: shared owner context.
- Q6: state, memory and history.
- Q7: procedure invocation and routing.
- Q9: result, close, handback and portable continuation.
- Q10: authority and effect gates.
- Q11: process/kernel evolution and mutation.
- Q12: communication, child runs, models, tools and adapters.
- Q13: proof and evaluation.
- Q14: Markdown, application and carrier boundary.

### Proof questions

- Does one process pack preserve its semantics when the model changes?
- Can a process move from Markdown/chat to an application without
  redefining the kernel?
- Does every close/checkpoint return a continuation index sufficient for
  another run?
- Are implicit durable mutations detected and rejected?
- Can writer/apply validation detect invalid or unauthorized changes?
- Does a stronger model improve execution without requiring kernel or
  process-pack rewrite?

### Consumer-specific details

- Health policies and memory.
- Zaratusta operating rhythm.
- Game/canon procedures.
- Concrete owner facts and preferences.
- Concrete tool permissions and proof scenarios.

### Rejected premature freezes

- exact message format;
- exact CALL/RESULT analogue;
- exact writer agent;
- exact state files;
- exact service list;
- exact application architecture;
- exact automated validator;
- exact tool-routing framework.

## Graph verdict

top_level_rebalance: not_needed

reason: |
  Q1 introduced useful entities and child questions, but none is a hidden
  prerequisite that prevents the core invariant from being frozen.

  The spawned concerns fit existing Q2-Q14 nodes, especially Q9
  result/handback, Q10 authority, Q11 evolution, Q12 communication and
  Q14 carrier.

  Q2 should now classify candidate responsibilities among:
  - invariant kernel semantics;
  - reusable service semantics;
  - required process-pack declarations;
  - owner-profile concerns;
  - adapter/implementation concerns.

gap_event: none

## Gate

status: PASS

checks:
  - Frozen only Q1 core invariant and kind of object.
  - No final service-block list frozen.
  - No exact packet or chat format frozen.
  - No writer implementation topology frozen.
  - No implementation, repo, backend or application selected.
  - Markdown retained only as bootstrap carrier.
  - Current artifacts treated as evidence, not authority.
  - Consumer-specific policy remains outside the kernel.
  - Portable continuation and durable-mutation boundaries are expressed
    as semantics, not current tooling.
  - Child/downstream questions preserved.
  - Owner approval and clarification recorded.

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
