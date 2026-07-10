# Research note — kernel service-zone and responsibility classification

status: research_input_not_architecture_decision
researched_at: 2026-07-10
call: c-solmax-operating-substrate-kernel-service-zone-best-practice-research-001
parent: s-solmax-operating-substrate-core-invariant-architecture-forge-001
question: |
  What universal AI-process kernel responsibilities and boundaries are
  supported by current primary-source practice, and what evidence-backed
  criteria can Q2 use to distinguish invariant kernel semantics, reusable
  service semantics, process-pack declarations, owner-profile concerns and
  adapter/implementation concerns?

## 1. Scope and preserved locks

This note preserves the accepted Q1 answer without extending it:

- operating-substrate remains a stable, model-neutral, carrier-neutral,
  owner-tuned AI-process kernel with pluggable process packs;
- domains and process packs do not modify kernel semantics;
- bounded runs, procedure invocation, routing, delegation, structured
  communication and continuation, state/memory/source discipline,
  authority/effect boundaries, adapters, evidence/recovery, owner
  interface and governed evolution remain accepted responsibility classes;
- every close/checkpoint yields a portable continuation index;
- durable mutation crosses a validated writer/apply boundary;
- exact packet schemas, service zones, writer topology, entity model,
  storage, provider, runtime and application architecture remain open;
- Markdown/chat remain the bootstrap carrier only.

This note does not:

- approve an architecture card;
- define a canonical service-block list;
- assert that every responsibility becomes a separate service, module,
  process, agent or file;
- select a framework, provider, model, storage system, repository,
  transport or application architecture;
- treat Direction OS or any researched system as substrate authority.

## 2. Bounded answer

The compared systems converge on stable semantic boundaries but not on a
stable physical decomposition.

They repeatedly need to answer:

1. What durable unit of work exists, and what is only a chat, transport
   connection or execution attempt?
2. What procedure or routing decision is active?
3. Who or what has been delegated work, under which bounds and authority?
4. What messages, artifacts and state transitions have defined meanings?
5. What must survive interruption and permit legitimate continuation?
6. Which data is current state, history, memory, source, configuration,
   artifact or evidence?
7. Which proposed changes or external effects are authorized, validated
   and actually applied?
8. Which capabilities exist, which are permitted, and which implementation
   supplies them?
9. What evidence permits observation, verification, recovery and
   evolution?
10. How does long-lived work survive model, definition and carrier changes?

No researched source supports the inference that these questions must map
one-to-one to deployable service blocks.

Candidate Q2 orientation:

A service zone may be treated provisionally as a semantically coherent
responsibility family with:

- a stable abstract contract;
- an identifiable authority and state boundary;
- explicit failure and recovery semantics;
- cross-process reuse evidence;
- implementation substitutability.

This is a candidate definition for architecture-forge, not an accepted
definition. A zone may ultimately be centralized, distributed,
cross-cutting, embedded or implemented by several adapters.

## 3. Primary-system comparison

### 3.1 OpenAI Agents SDK

Evidence:

- A Runner performs a bounded agent loop: model output may finish, invoke
  tools or hand off to another agent; turn limits provide an execution
  bound.
- One logical run may contain several model calls and several agents.
- Conversation continuity can be maintained manually, by a Session, by a
  server-side conversation or by a previous-response reference.
- Handoffs expose delegation with a target, optional typed input and input
  filtering.
- Interrupted runs can preserve serializable RunState, collect approval or
  rejection and resume.
- Sessions and tracing are separate concerns: sessions preserve working
  conversation context; traces record workflow, model, tool, guardrail and
  handoff activity.

Supported semantics:

- run is not identical to conversation;
- delegation has a contract;
- execution is bounded;
- approval can suspend and resume work;
- trace and working memory are distinct;
- state can be serialized.

Limitation for Q2:

Conversation IDs, previous-response IDs, RunState classes and Runner APIs
are runtime conveniences. They do not by themselves define a
carrier-neutral continuation contract.

### 3.2 Anthropic agent/workflow guidance

Evidence:

- Anthropic distinguishes workflows, whose paths are predetermined in
  code, from agents, where the model dynamically controls process and tool
  use.
- Its guidance recommends beginning with simple composable patterns and
  adding agentic complexity only where measured value justifies it.
- Common patterns include prompt chaining, routing, parallelization,
  orchestrator-workers and evaluator-optimizer loops.
- Its multi-agent research implementation uses a lead agent and bounded
  subagents with isolated contexts, explicit objectives, output
  expectations, tools, sources and effort budgets.
- Long-horizon work is checkpointed into external memory; fresh agents can
  resume from summaries and persisted artifacts.
- Production lessons emphasize full tracing, checkpointing, deterministic
  retries, evaluation of end state and compatibility while different
  agent versions coexist.

Supported semantics:

- procedure invocation must support both predictable workflows and
  model-directed agents;
- delegation requires bounded objective, context, capabilities and return;
- isolated child contexts can be useful;
- checkpoints and persisted artifacts are needed for long-running work;
- orchestration complexity must earn its cost.

Limitation for Q2:

This is architecture guidance and an implementation report, not a durable
state or interoperability protocol.

### 3.3 Google Agent Development Kit

Evidence:

- ADK distinguishes Session, Session State, Events, Memory and Artifacts.
- A Session represents one conversation thread; State carries small
  serializable working data; Events record interactions and state deltas;
  Memory supports retrieval beyond one session; Artifacts hold larger or
  binary outputs.
- Resumability records completed workflow steps and tool results through
  Events and Event Actions, then resumes incomplete work.
- Resume uses app, user, session and invocation identifiers.
- Documentation warns that resumable tools may execute more than once and
  should prevent harmful duplicate effects.
- Durable state changes are made through managed context/event paths;
  directly editing a retrieved Session object bypasses event tracking and
  can lose updates.
- Tool confirmations suspend action until structured confirmation returns.
- Tracing propagates hierarchical causal context.

Supported semantics:

- conversation, invocation and workflow step are distinct;
- current state, event history, long-term memory and artifacts are
  separate concerns;
- mutation must pass through a tracked apply path;
- resumability requires discrete durable checkpoints;
- effects must tolerate at-least-once execution;
- approval must correlate to the suspended invocation.

Limitation for Q2:

ADK object names, workflow classes and identifier tuple are implementation
choices, not universal entities.

### 3.4 LangGraph

Evidence:

- Checkpointers preserve graph state by thread and checkpoint.
- Checkpoints include current values, next work, metadata, parentage,
  pending tasks, writes and interrupts.
- Pending writes avoid repeating already completed sibling work after
  failure.
- Interrupts suspend execution and resume through a persistent thread
  cursor.
- Nodes restart from their beginning after an interrupt; effects before an
  interrupt therefore require idempotency or isolation in a separate node.
- Time travel can replay or fork from a checkpoint while retaining prior
  history.
- Subgraphs permit isolated reusable or multi-agent work and can use
  per-invocation, per-thread or stateless persistence.
- Graph definitions can evolve, but compatibility with old checkpoints is
  an explicit concern.

Supported semantics:

- execution attempt and durable thread are distinct;
- checkpoints need lineage, pending work and interrupt state;
- resume/replay has explicit effect-safety consequences;
- child work can have isolated state;
- recovery and forking are different operations;
- durable definition evolution needs compatibility handling.

Limitation for Q2:

Graph nodes, thread IDs, checkpoint objects and replay mechanics are one
orchestration realization. Exact deterministic replay is not universal to
LLM-led processes.

### 3.5 Model Context Protocol, specification 2025-11-25

Evidence:

- MCP separates host, client and server responsibilities.
- The host controls lifecycle, permission, security policy, consent,
  authorization and context aggregation.
- Each client maintains an isolated stateful session with one server.
- Clients and servers negotiate protocol version and supported
  capabilities before use.
- Servers expose focused resources, prompts and tools rather than receiving
  all host context.
- Tool declarations include names, descriptions and input/output schemas.
- Tool use remains model-controlled but the specification recommends
  visible human review and confirmation for sensitive operations.
- Authorization guidance uses least privilege and rejects token
  passthrough.
- Task support distinguishes asynchronous task lifecycle, status,
  input-required, result retrieval, cancellation, TTL and audit.
- Requests have timeout, progress and cancellation semantics.

Supported semantics:

- capability availability must be declared and negotiated;
- capability does not imply authority;
- context must be minimized across trust boundaries;
- host/user authority remains outside an individual tool server;
- asynchronous work needs identity, lifecycle, progress and cancellation;
- permission and sensitive-input handling are explicit responsibilities.

Limitation for Q2:

MCP is a capability/context protocol. It does not define the full process
state, procedure, evidence, continuation or governed-evolution contract.

### 3.6 Microsoft AutoGen

Evidence:

- Agents and teams can save and load serializable state, including model
  context and component versions.
- Teams coordinate a shared goal and return a task result plus stop reason.
- Handoff messages can transfer active control.
- Internal events such as tool requests and executions are distinguished
  from chat messages.
- Termination can depend on maximum messages, tokens, timeout, handoff,
  external signal or custom conditions.
- GraphFlow provides structured sequential, parallel, conditional and loop
  execution.
- OpenTelemetry-based tracing records agent and runtime behavior.

Supported semantics:

- bounded team run and persistent team state are separate;
- chat messages and internal control events differ;
- orchestration may be conversational or graph-defined;
- state serialization and stop reason support continuation;
- tracing is backend-neutral.

Limitation for Q2:

AgentChat classes, team types and GraphFlow APIs are framework-specific;
some graph functionality is explicitly experimental and must not be
promoted into substrate architecture.

### 3.7 Temporal durable workflows

Evidence:

- Workflow Definition and Workflow Execution are distinct.
- Workflow ID is a durable application/business identity; Run ID identifies
  one runtime execution and may change across retries or continuation.
- Event History is the durable lifecycle record from which workflow state
  is reconstructed by replay.
- Workflow code coordinates; non-deterministic or external effects execute
  as Activities whose results are recorded.
- Activities are expected to be idempotent because retries can repeat
  execution.
- Queries read state without writing; Signals request asynchronous changes;
  Updates are tracked synchronous changes and may be validated before
  acceptance into history.
- Child Workflows have explicit parentage, lifecycle and close policies.
- Long-lived definitions require versioning/patch markers so old histories
  remain replay-compatible.

Supported semantics:

- stable work identity must not depend on mutable run identity;
- durable mutation is command/event mediated;
- read, proposed write and accepted write have different semantics;
- external effects are isolated from orchestration;
- retries require idempotency;
- child work has explicit ownership;
- long-running work requires definition/version compatibility.

Limitation for Q2:

Temporal's deterministic replay model is highly valuable evidence for
durability and effects, but arbitrary LLM reasoning cannot be assumed to
replay deterministically. The kernel should preserve recovery semantics,
not freeze Temporal's execution constraints.

### 3.8 Agent2Agent Protocol

Evidence:

- A2A separates Task, Message, Artifact and conversational context.
- Context ID groups related tasks and messages; Task ID identifies a
  particular durable piece of work within that context.
- A task has lifecycle states such as submitted, working, input-required,
  completed, failed, cancelled and rejected.
- Artifacts carry task outputs; status and artifact updates can stream.
- Agent Cards advertise interfaces, capabilities, security schemes and
  extensions.
- Task access and operations are authorization-scoped.
- Asynchronous work supports polling, streaming or push notification.

Supported semantics:

- conversation and task are distinct;
- message and result artifact are distinct;
- input-required is a continuation state rather than a new ad hoc chat;
- capabilities and security are declared;
- asynchronous inter-agent work needs lifecycle and return semantics.

Limitation for Q2:

A2A defines inter-agent interoperability, not the agent's internal
procedure, memory, durable state, evidence ledger or cross-runtime
continuation export.

## 4. Convergent kernel-level responsibility claims

These are evidence-backed responsibility claims. They are not a proposed
final block list.

### 4.1 Stable work identity and boundary

A process needs a durable goal-bearing work identity distinct from:

- the chat or visible thread carrying interaction;
- the conversation context used as working memory;
- one execution attempt;
- one provider's response/run identifier;
- one transport connection.

The work identity may own lifecycle, parentage, accepted outcomes and
continuation across multiple runs or chats.

### 4.2 Bounded execution lifecycle

Every invocation needs explicit start, active status and terminal or
checkpoint outcome.

Recurrent lifecycle concerns include:

- completion;
- input or approval required;
- failure;
- cancellation;
- timeout;
- resource or turn budget;
- interruption;
- retry;
- checkpoint.

Exact state names remain open.

### 4.3 Procedure and routing invocation

Practice supports both:

- predetermined workflow/graph/code control for predictable work;
- model-directed routing and tool choice for open-ended work.

The invariant candidate is not one routing algorithm. It is that an
invocation exposes:

- the active procedure or routing basis;
- required context;
- allowed authority and effects;
- success/stop/failure conditions;
- uncertainty and escalation path;
- expected result.

The actual procedure catalogue, route policy and domain vocabulary belong
to process packs.

### 4.4 Controlled delegation and child work

Universal delegation semantics concern the invocation contract, not role
names.

A delegated unit may be an agent, workflow, tool-backed executor, research
run, verifier, human or external service. It needs:

- parent work identity;
- objective and scope;
- supplied context and sources;
- available capabilities and authority;
- effort/turn/time boundaries;
- expected output or artifact;
- status, cancellation and failure semantics;
- return route and ownership of unresolved work;
- provenance.

`research`, `executor` and `verifier` are plausible reusable role
templates or process-pack declarations. The evidence does not show that
every process requires those exact agent classes.

### 4.5 Structured communication and artifact semantics

Conversation text alone is insufficient for reliable process boundaries.

Current systems repeatedly distinguish meanings such as:

- invocation/request;
- progress/status;
- input or approval required;
- cancellation/error;
- handoff/delegation;
- result;
- artifact;
- proposed mutation;
- applied mutation outcome;
- evidence/provenance;
- continuation.

Q2 may classify these semantic meanings. It must not freeze exact packet
names, fields or serialization.

### 4.6 Portable continuation

Every checkpoint/close needs a semantic continuation artifact that can be
interpreted without the original chat remaining open.

Runtime-local identifiers may be included as references, but cannot be
the sole continuation mechanism.

### 4.7 Explicit state-plane discipline

Sources converge on separating concerns that fail differently:

- active execution context;
- accepted durable process state;
- append-only or lineage-preserving history;
- longer-term retrievable memory;
- source material and provenance;
- output artifacts;
- procedure/configuration definitions and versions;
- trace/evidence;
- owner-specific policy/context;
- protected credentials and secrets.

No single storage layout follows from this convergence.

### 4.8 Authority, validation and effect boundary

Reasoning, proposed mutation and applied mutation are distinct events.

Capability availability does not imply current permission, and permission
does not imply that a particular action has been approved.

Durable writes and external effects require a validated apply path.

### 4.9 Capability, permission and adapter boundary

Models, tools, stores, transports and applications expose capabilities.
Current protocol practice supports explicit declarations, versions,
schemas, negotiated support and least privilege.

Process packs may declare required capabilities. Adapters supply concrete
implementations. Kernel semantics remain independent of either.

### 4.10 Evidence, observability, replay and recovery

A trustworthy process needs enough durable evidence to establish:

- what was attempted;
- what inputs/sources were used;
- what became accepted or applied;
- which tools/children participated;
- what failed or remains unresolved;
- where continuation can safely begin.

Systems disagree on exact replay technology. The universal claim is
recoverability and causal evidence, not deterministic re-execution of
every model token.

### 4.11 Owner/human interface

The sources strongly support a host/user authority layer for:

- consent;
- sensitive input;
- high-impact tool use;
- approval/rejection;
- interruption;
- cancellation;
- visibility of proposed effects.

They do not converge on a first-class owner-profile object.

Therefore the accepted Q1 owner-profile layer remains valid, while its
concrete schema, facts, preferences and interaction style must not be
promoted to universal kernel structure from this research alone.

### 4.12 Governed evolution and version compatibility

Long-running work may outlive:

- a model version;
- a prompt or procedure definition;
- an agent graph;
- a capability version;
- a deployment.

Current practice therefore supports explicit version identity,
compatibility checks, migration/patch policy and rejection of hidden
definition drift.

## 5. Meaningful disagreements

### 5.1 Conversation-centric vs task/workflow-centric identity

OpenAI and AutoGen commonly begin from conversation and agent-run
abstractions. Temporal begins from durable workflow identity. A2A and MCP
Tasks distinguish conversation/context from asynchronous task identity.

Q2 implication:
do not make chat the universal unit and do not require a full durable
workflow engine for every interaction.

### 5.2 Model-directed vs predefined control

Anthropic, OpenAI, ADK and AutoGen support both model-directed routing and
more deterministic workflow structures.

Q2 implication:
kernel semantics should permit both; process packs declare which control
mode is appropriate.

### 5.3 Manager-retained control vs control-transfer handoff

Some systems call specialists as tools while a manager retains control.
Others hand off the active conversation or task.

Q2 implication:
preserve delegation ownership and return semantics without selecting one
topology.

### 5.4 Shared transcript vs isolated child context

Team systems may share a message context. Anthropic's research system and
MCP security boundaries favor filtered or isolated context.

Q2 implication:
context projection is part of delegation semantics; full-history sharing
must not be assumed.

### 5.5 Mutable state vs event/checkpoint-derived state

Agent frameworks often serialize current state. ADK, LangGraph and
Temporal place more weight on events, deltas, checkpoints or histories.

Q2 implication:
require controlled durable mutation and provenance, but do not yet choose
event sourcing, snapshots or another storage model.

### 5.6 Runtime cursor vs semantic continuation

Most products expose a local session/thread/run/task identifier. No
compared standard provides a complete cross-provider process continuation
export.

Q2 implication:
preserve Q1's stronger portable-continuation requirement.

### 5.7 Deterministic replay vs checkpoint recovery

Temporal reconstructs deterministic workflow state from history.
LangGraph resumes or re-executes from checkpoints. ADK restores completed
steps. Agent runtimes may only serialize current state.

Q2 implication:
distinguish record, reconstruct, resume, replay, fork and compensate;
do not use one word to freeze one technology.

### 5.8 Framework-provided HITL vs host/application policy

Some frameworks expose approval primitives. MCP places authorization and
consent primarily with the host. Domain-specific policy remains external
to both.

Q2 implication:
approval categories may be invariant; concrete thresholds and policies
belong to process packs and owner profile.

### 5.9 Automatic memory vs explicit ingestion

Systems vary on whether conversation history automatically becomes memory
or must be explicitly archived and searched.

Q2 implication:
do not treat all transcript content as durable memory or accepted truth.

### 5.10 Physical writer topology

Temporal uses workflow-service and Activity boundaries; ADK uses managed
event/state services; LangGraph uses checkpointed updates; agent systems
may use approval-wrapped tools.

Q2 implication:
freeze only the logical validated apply boundary. A separate writer chat
or agent remains one implementation pattern.

## 6. Candidate five-layer classification for Q2

### A. Invariant kernel semantics

Candidate definition:

A semantic guarantee required for every compliant process, regardless of
model, provider, carrier or implementation.

Promotion signals:

- its absence breaks durable work identity, authority/effect safety,
  legitimate continuation, evidence or governed evolution;
- it can be expressed without a provider API or one consumer's policy;
- it has implementation-independent conformance scenarios;
- process packs cannot safely override it.

Examples for evaluation only:

- distinction between proposed and applied durable mutation;
- parentage and return ownership for delegated work;
- every checkpoint yields a continuation contract;
- capability does not equal authority.

### B. Reusable service semantics

Candidate definition:

Repeated cross-process behavior with a stable abstract contract and
reusable failure/recovery semantics, but not necessarily required by every
process.

Promotion signals:

- at least several materially different process packs need it;
- implementations can be replaced without changing pack meaning;
- central reuse prevents repeated high-cost failure;
- the kernel can remain semantically valid when the service is absent or
  substituted.

Possible examples for evaluation only:

- memory retrieval;
- checkpoint materialization;
- tracing export;
- capability discovery;
- validation service;
- routing assistance.

### C. Process-pack declarations

Candidate definition:

Values or policies that legitimately vary by process while the kernel
provides declaration, validation and invocation semantics.

Likely contents:

- procedures and route policy;
- domain vocabulary;
- local role taxonomy;
- required capabilities;
- local state/memory shape;
- evidence and result criteria;
- effect policy;
- budgets and termination conditions;
- process-specific proof scenarios.

### D. Owner-profile concerns

Candidate definition:

Cross-process owner-specific policy, preference or approved shared context
that should not be duplicated in every process pack.

Likely contents:

- language and presentation preference;
- initiative/ask/proceed preference;
- privacy and sharing defaults;
- approval thresholds;
- preferred explanation and decision style;
- owner-wide constraints and approved context.

Boundary:

A process-specific safety rule or domain fact does not become owner-wide
merely because the same owner uses the process.

### E. Adapter/implementation concerns

Candidate definition:

Concrete bindings that implement a semantic contract for a provider,
runtime, tool, store, transport, application or deployment.

Examples:

- OpenAI Runner or conversation ID;
- ADK SessionService or Event object;
- LangGraph checkpoint backend;
- Temporal Workflow/Activity implementation;
- MCP client/server transport;
- A2A endpoint;
- AutoGen team class;
- database, queue, repository or telemetry backend.

These may require compatibility declarations, but do not define kernel
meaning.

## 7. Candidate Q2 classification criteria

For each candidate responsibility, Q2 should ask:

1. Universal necessity
   Is it required for every admissible custom AI-process, or merely common?

2. Failure consequence
   If absent, does a universal guarantee fail—identity, authority,
   continuation, evidence, recovery or governed evolution?

3. Cross-domain recurrence
   Does the same semantic problem appear in materially different processes,
   not only in Direction OS or Zaratusta?

4. Model/carrier stability
   Does the meaning survive a change of model, provider, chat surface,
   storage system and orchestration framework?

5. Semantic expressibility
   Can inputs, outcomes, failures, authority and recovery be defined
   without current API/class names?

6. Variation owner
   Who legitimately chooses the values: kernel, process pack, owner
   profile or adapter?

7. Authority locus
   Who may propose, validate, approve, apply, observe, cancel or revoke the
   responsibility's effects?

8. State locus
   What durable data, provenance, version and retention boundary does the
   responsibility own?

9. Substitutability
   Can one implementation be replaced while preserving process-pack
   semantics?

10. Conformance testability
    Can the claim be refuted through carrier/provider-neutral scenarios?

11. Evidence breadth
    Is support drawn from at least two independent agent approaches and,
    for durability/effect claims, at least one protocol or durable-workflow
    source?

12. Kernel-cost justification
    Does promotion prevent repeated serious failure strongly enough to
    justify increasing universal kernel burden?

13. Leakage check
    Does the candidate encode one consumer, owner fact, current repository,
    provider feature or bootstrap carrier?

14. Live-use friction
    Would universalizing it create bureaucracy that obstructs the useful
    owner-facing process?

Candidate disposition rule:

- INVARIANT when universal necessity, universal failure consequence,
  implementation neutrality and conformance testability all hold.
- REUSABLE SERVICE SEMANTICS when recurrence and stable substitutable
  contract hold, but universal necessity does not.
- PROCESS-PACK DECLARATION when legitimate variation is process/domain
  owned.
- OWNER-PROFILE CONCERN when legitimate variation is owner-wide rather
  than process-wide.
- ADAPTER/IMPLEMENTATION when the concern binds a concrete capability,
  provider, runtime, store, transport or topology.
- DEFER when evidence is only repetition, one current API, one consumer
  example or a rough block sketch.

No numeric score is recommended at this stage. A single hard failure on
implementation neutrality, consumer leakage or owner authority is enough
to reject invariant promotion.

## 8. Explicit boundary analysis

### 8.1 Working chat/run/task vocabulary

This vocabulary is sufficient for Q2 classification but is not the final
entity model:

- Chat/interaction:
  a carrier-level exchange or visible transcript container. It may be
  disposable.

- Conversation/session context:
  related interaction history and working context. It may span several
  runs and may contain several tasks.

- Run/invocation:
  one bounded execution attempt under a procedure or routing decision.

- Task/work item:
  a durable goal-bearing unit with lifecycle and ownership. It may span
  multiple runs, chats or conversations and may have children.

- Procedure:
  a declared execution contract invoked for a class of work.

- Checkpoint:
  a durable point from which a legitimate next execution can be
  reconstructed.

- Continuation:
  the portable semantic index used to start that next execution.

Consequence:

`one chat = one task` remains a useful bootstrap discipline, but the
universal invariant is not identity equality. Future carriers may execute
one task over several runs or several tasks within one long-lived
conversation.

Exact entity relationships remain the existing downstream kernel
entity-model child question. This does not block Q2.

### 8.2 Portable continuation levels

Candidate levels:

- C0 — narrative/transcript only:
  context may be readable but unresolved authority, state and next route
  are implicit. Not sufficient for Q1.

- C1 — opaque runtime cursor:
  provider conversation, invocation, thread, task or run ID. It may resume
  in the same runtime but is not carrier-neutral.

- C2 — semantic continuation index plus validated references:
  enough explicit meaning to continue in a fresh chat/model/carrier while
  retaining optional runtime-local references. Candidate minimum Q1
  guarantee.

- C3 — fully materialized portable export:
  all required state and artifacts copied into an interoperable package.
  Potentially useful but too costly to require universally without further
  evidence.

Candidate C2 semantic contents:

1. kernel and process-pack identity, version and compatibility claim;
2. durable work identity and parent/child relationships;
3. goal, boundaries, expected return and current authority/effect class;
4. active or last procedure position, lifecycle state and stop reason;
5. accepted outcomes, decisions and durable mutations already applied;
6. unresolved gaps, obligations, rejected paths and pending owner
   decisions;
7. pending tool/effect requests, approvals, preconditions and idempotency
   information;
8. child-work status, returned artifacts and route-back ownership;
9. durable state, source, memory, artifact and evidence references with
   provenance and access requirements;
10. next permitted invocation and required capabilities;
11. integrity/validation marker;
12. explicit distinction between embedded material and external
    runtime-specific references.

These are candidate semantic contents, not an exact message schema.

### 8.3 State, memory, source, history and configuration

Candidate semantic distinctions:

- Active execution context:
  temporary inputs, current model context, in-flight control state.

- Durable process state:
  accepted current facts and commitments required for future operation.

- History/audit:
  lineage of requests, transitions, decisions, proposals and apply
  outcomes.

- Long-term memory:
  retrievable material that may aid future reasoning but is not
  automatically authoritative truth.

- Source:
  externally or internally produced material whose provenance supports a
  claim or decision.

- Artifact:
  a produced output that may be referenced independently from the
  conversation.

- Evidence:
  material used to verify or refute an outcome or transition.

- Configuration/process definition:
  accepted procedures, policies, capabilities, schemas and versions that
  govern execution.

- Owner profile:
  owner-wide preference, policy and approved shared context.

- Secret/credential:
  protected capability material that should not be copied into ordinary
  context, memory or continuation packets.

Promotion and mutation between these concerns must be explicit. For
example:

- transcript text does not automatically become durable process state;
- retrieved memory does not automatically become accepted fact;
- one process's assumption does not automatically become owner-wide
  profile;
- an artifact does not prove its own correctness;
- trace data does not automatically constitute sufficient evidence.

### 8.4 Writer/apply and validation boundary

Strong cross-system convergence supports the following logical stages:

1. Propose/command intent
   State what mutation or external effect is requested.

2. Validate
   Check syntax/schema, target, preconditions, current version, applicable
   policy, capability availability and evidence requirements.

3. Authorize
   Establish whether the invoking role may act and obtain owner/human
   approval where required.

4. Apply
   Execute through the authorized state/effect capability.

5. Verify and record
   Record result, new version/state, external receipt or error, evidence
   and causal linkage to the proposal/approval.

6. Recover
   Permit safe retry, rejection, compensation or escalation.

Candidate mutation-envelope semantics, not schema:

- operation identity/idempotency key;
- target identity;
- expected version or precondition;
- proposed change/effect;
- authority/effect class;
- validation result;
- approval reference when required;
- apply outcome and new version;
- evidence/trace reference;
- rollback or compensation status.

Universal guarantee:

A reasoning run cannot make an untracked durable mutation merely by
asserting that something is now true.

Not universal:

- separate writer chat;
- separate writer agent;
- event-sourced service;
- transactional database service;
- repository commit;
- one specific validator topology.

Any physical topology is acceptable only if it enforces the same logical
boundary.

### 8.5 Authority, approval, tools and capabilities

Candidate distinctions:

- Capability:
  what an adapter can technically do.

- Permission:
  what a role/process is generally allowed to request.

- Authorization:
  whether the current identity may perform a concrete action on a concrete
  target.

- Approval:
  an owner/human decision bound to a sufficiently specific proposed
  action.

- Policy:
  rules determining validation, authorization and approval needs.

Process-pack responsibility candidates:

- required capabilities;
- domain effect policy;
- allowed delegation roles;
- evidence thresholds;
- local escalation rules.

Owner-profile candidates:

- owner-wide approval thresholds;
- privacy defaults;
- preferred initiative level;
- approved shared context.

Adapter responsibility candidates:

- capability discovery;
- authentication;
- tool schemas;
- token/credential handling;
- concrete enforcement and receipts.

Approval must remain correlated with the exact pending action after resume.
General consent should not silently authorize a changed target, payload or
effect.

### 8.6 Observability, evidence, replay and recovery

Candidate semantic separation:

- Trace:
  causal execution record across model, agent, procedure, tool and
  handoff.

- Audit/history:
  durable record of accepted transitions and authority decisions.

- Evidence:
  proof supporting or refuting an outcome.

- Checkpoint:
  durable restart position.

- Resume:
  continue pending work.

- Replay:
  reconstruct or re-execute prior work under defined rules.

- Fork:
  create a new branch from a past state without rewriting original
  history.

- Retry:
  repeat failed work, potentially at least once.

- Compensation:
  counteract an already-applied external effect where reversal is
  possible.

Kernel-level candidate guarantees:

- causal linkage and stable work identity;
- enough evidence to understand what became true;
- explicit pending and unresolved work;
- safe recovery rules;
- privacy/redaction obligations;
- version compatibility information.

Reusable service candidates:

- trace collection/export;
- checkpoint persistence;
- evaluation;
- replay/fork tooling;
- recovery coordination.

Adapter concerns:

- OpenTelemetry backend;
- checkpoint database;
- provider trace API;
- event store;
- application visualization.

### 8.7 Portability across models and carriers

Portability pressure produces these candidate guarantees:

- durable work identity is not a provider Run ID;
- process semantics are versioned independently of model/provider;
- continuation is semantically exportable;
- required capabilities are declared rather than assumed;
- adapters advertise compatibility;
- old work is either resumable under compatible definitions, migrated
  explicitly or rejected with a clear gap;
- a stronger model improves execution without redefining authority,
  continuation or durable mutation semantics.

## 9. Evaluation-only classification stress test

The following is not a final service-zone list. It tests whether the
five-layer taxonomy can separate one concern across several ownership
levels.

### Work lifecycle

- invariant candidate:
  durable identity, lifecycle and terminal/checkpoint semantics;
- pack:
  local budgets and success conditions;
- adapter:
  provider run/thread IDs and scheduler implementation.

### Procedure/routing

- invariant candidate:
  explicit invocation, stop, uncertainty, authority and result semantics;
- reusable service candidate:
  optional router/workflow execution assistance;
- pack:
  concrete procedures and route policy;
- adapter:
  graph engine, classifier or Runner API.

### Delegation

- invariant candidate:
  parentage, bounds, authority, return and unresolved ownership;
- reusable service candidate:
  common research/executor/verifier templates;
- pack:
  role catalogue and when to delegate;
- adapter:
  child-agent runtime or remote-agent protocol.

### Communication/handoff

- invariant candidate:
  stable meanings for request, result, gap, approval, effect and
  continuation;
- reusable service candidate:
  validation and routing of typed messages;
- pack:
  process-specific result/evidence expectations;
- adapter:
  JSON, Markdown, A2A, MCP, queue or chat transport.

### Continuation

- invariant candidate:
  C2 semantic continuation obligation;
- reusable service candidate:
  materialization, validation and import/export;
- pack:
  local state and evidence that must be included;
- adapter:
  conversation/checkpoint/task identifiers.

### State/history

- invariant candidate:
  controlled mutation, provenance and concern separation;
- reusable service candidate:
  persistence/checkpoint/audit services;
- pack:
  local state schema and retention policy;
- adapter:
  file, repository, database or event store.

### Memory

- invariant candidate:
  memory is distinct from accepted state/source authority;
- reusable service candidate:
  retrieval, ingestion and retirement;
- pack:
  what may be remembered and how it is used;
- owner profile:
  sharing/privacy defaults;
- adapter:
  index/vector/store implementation.

### Authority/effects

- invariant candidate:
  capability/permission/authorization distinction and validated apply;
- reusable service candidate:
  policy evaluation and approval coordination;
- pack:
  domain-specific rules/effect classes;
- owner profile:
  owner-wide approval preferences;
- adapter:
  credentials and effect execution.

### Observability/recovery

- invariant candidate:
  causal evidence, unresolved status and recoverability;
- reusable service candidate:
  tracing/checkpoint/replay/evaluation;
- pack:
  proof requirements and retention;
- adapter:
  telemetry/checkpoint backend.

### Owner interface

- invariant candidate:
  route for consent, approval, correction, cancellation and decision;
- owner profile:
  language, initiative, explanation and presentation preferences;
- pack:
  process-specific interaction rhythm;
- adapter:
  chat, voice, application or notification UI.

### Evolution/versioning

- invariant candidate:
  explicit versioned evidence-gated change; no hidden prompt drift;
- reusable service candidate:
  compatibility/migration validation;
- pack:
  local definition versions;
- adapter:
  deployment and migration mechanism.

The stress test produces no contradiction across persistence, live
interface and domain-specific safety policy. Therefore Q2 is ready.

## 10. Failure modes and premature-freeze risks

### Boundary-collapse failures

- chat, conversation, run and durable task are treated as one entity;
- provider runtime ID is treated as process identity;
- full transcript is treated as authoritative state;
- status updates are confused with durable outcomes;
- artifact existence is confused with proof of live usefulness.

### Continuation failures

- handoff omits goal, authority, pending approval or unresolved obligation;
- new chat depends on owner's memory of the prior transcript;
- continuation contains inaccessible references without declaring them;
- resumption uses incompatible process definitions without detection;
- child work returns findings but no ownership of remaining gaps.

### Mutation/effect failures

- reasoning output directly mutates durable state;
- proposal, approval and apply collapse into one unvalidated action;
- stale writes have no expected-version/precondition check;
- retries duplicate purchase/send/delete/write effects;
- system claims exactly-once behavior without idempotency or evidence;
- approval is reused after the action payload or target changes;
- failed apply leaves no durable failure record or recovery route.

### State-discipline failures

- retrieved memory becomes truth without provenance;
- one process's local fact becomes owner-wide profile;
- source, evidence, artifact, state and history are merged;
- all context is persisted indefinitely;
- credentials enter ordinary memory, trace or continuation packets;
- direct state mutation bypasses event/audit/version tracking.

### Delegation failures

- child receives an unbounded objective;
- full context is shared despite least-privilege needs;
- child has more tool/effect authority than its task requires;
- parent cannot cancel or determine child status;
- manager and child both assume the other owns the next step;
- multi-agent scaffolding is used where one bounded workflow would work.

### Observability/recovery failures

- trace exists but accepted state transitions are not auditable;
- logs expose sensitive content without redaction;
- deterministic replay is promised for non-deterministic model behavior;
- checkpoint recovery repeats non-idempotent effects;
- new procedure version cannot interpret old continuation state;
- evaluation checks artifact completeness but not owner-facing behavior.

### Architecture-freeze failures

- framework class or API becomes a substrate entity;
- service zone is assumed to equal deployable service/module/agent;
- every repeated concern is promoted to the kernel;
- every optional concern is dismissed as consumer-specific;
- one consumer's state layout becomes universal;
- current experimental functionality becomes a permanent invariant;
- exact writer-agent topology is frozen before the logical contract;
- event sourcing, graph execution or Markdown is selected while asking a
  responsibility question.

### Live-use failure

A semantically complete internal structure can still create owner-facing
bureaucracy. The Zaratusta trial shows that state, intake and handback
surfaces are not sufficient evidence of useful process behavior.

Therefore Q2 criteria need the live-use friction check: reusable structure
must reduce reconstruction and failure without forcing the owner to
operate internal audit machinery.

## 11. Hidden prerequisite and graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed

Working prerequisite:

Q2 needs the provisional chat/conversation/run/task vocabulary in section
8.1 to avoid category errors.

Classification:

- inline minimal definition for Q2;
- link to the existing Q1 child question, "kernel entity model";
- exact entity model remains downstream;
- it does not block the service-zone/classification rule.

Spawned downstream proof questions:

1. Can a C2 continuation index move one real task to a fresh chat/model
   without reconstructing the prior transcript?
2. Can two carriers execute the same process-pack semantics while using
   different runtime identifiers and persistence mechanisms?
3. Are unauthorized, stale and duplicate durable mutations rejected while
   valid changes return evidence?
4. Can research, executor and verifier delegation share one parent/return
   contract without forcing them into universal agent classes?
5. Can observability prove live owner-facing behavior rather than only
   artifact completeness?

These fit existing Q3, Q9, Q10, Q12, Q13 and Q14 work. No new top-level
graph node is required.

## 12. Confidence and limits

High confidence:

- current primary sources converge on separating conversation/run/task,
  state/evidence, capability/authority and proposal/apply;
- bounded execution, explicit delegation, checkpoint/resume and causal
  evidence are recurring cross-system responsibilities;
- logical writer/apply validation is more universal than a separate
  writer-agent topology;
- a final physical service-block list is not supported by the evidence.

Medium-high confidence:

- the five-layer Q2 taxonomy can classify current candidate concerns
  without contradiction;
- service zone is best investigated as a semantic responsibility family
  rather than a deployment unit.

Medium confidence:

- the candidate minimum contents of C2 portable continuation;
- the proposed evidence threshold of two independent agent sources plus a
  protocol/durable-workflow source for durability/effect claims;
- a distinct owner-profile layer as a universal architectural object.
  External sources strongly support host/user authority, but do not
  converge on an owner-profile schema.

What would change the answer:

- a broadly adopted interoperable standard that exports full process
  state, authority, provenance and continuation across providers;
- live cross-carrier experiments showing that a materially smaller
  continuation contract is sufficient;
- two materially different process packs that cannot share the proposed
  service semantics;
- evaluation showing that a currently optional service is universally
  necessary;
- safety evidence showing that a proposed invariant belongs instead to
  domain policy or owner profile;
- owner correction to the accepted Q1 object or responsibility classes.

## 13. Q2 forge input

Plain question:

Какие service zones могут быть reusable structure, и по какому правилу
candidate responsibility becomes substrate-level?

Evidence-backed forge pressure:

- decide a classification rule, not a final block list;
- define service zone without equating it to module/service/agent;
- distinguish invariant semantics, reusable service semantics,
  process-pack declarations, owner-profile concerns and adapters;
- classify portable continuation as semantic obligation while leaving
  exact schema open;
- classify writer/apply as logical validated boundary while leaving
  physical topology open;
- require cross-domain, substitution and conformance evidence;
- reject current API/class/repository/carrier leakage;
- preserve anti-bureaucracy/live-use pressure.

END_OF_FILE: live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
