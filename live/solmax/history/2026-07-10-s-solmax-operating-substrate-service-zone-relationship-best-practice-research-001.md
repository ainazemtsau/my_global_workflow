RESULT s-solmax-operating-substrate-service-zone-relationship-best-practice-research-001 (call: c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001)
direction: solmax
play: research
node/task: g-operating-substrate/c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001
parent: s-solmax-operating-substrate-service-zone-classification-architecture-forge-001

outcome: |
  Research status: COMPLETE.
  Architecture status: RESEARCH INPUT ONLY — this session does not approve the
  Q3 relationship architecture.
  gap_event: none.
  top_level_graph_rebalance: not_required.
  q3_forge_readiness: READY.

  Proposed artifact path:
  live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md

  # Research note — implementation-neutral service-zone relationships and responsibility flow

  status: research_input_not_architecture_decision
  researched_at: 2026-07-10
  call: c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001
  parent: s-solmax-operating-substrate-service-zone-classification-architecture-forge-001

  question: |
    Which implementation-neutral relationship and responsibility-flow semantics
    can connect candidate service zones end-to-end while preserving accepted Q1
    and Q2, without choosing transport, message schema, orchestration topology
    or a final service-block list?

  ## 1. Scope and preserved locks

  This note preserves the accepted Q1 and Q2 answers without extending or
  revising them:

  - operating-substrate remains a stable, model-neutral and carrier-neutral
    kernel with pluggable process packs;
  - process and domain declarations do not modify kernel semantics;
  - service zones are semantic responsibility families, not physical modules,
    services, agents, processes, files or deployment units;
  - atomic responsibility claims are classified independently;
  - each atomic responsibility has one primary normative owner even when many
    actors contribute;
  - portable continuation is mandatory, while its exact entity and schema
    remain open;
  - durable mutation crosses a logical validated writer/apply boundary, while
    physical writer topology remains open;
  - no final service-zone or service-block list is accepted.

  This note does not:

  - approve a Q3 architecture card;
  - freeze the number or names of future service zones;
  - define entities, identifiers, packets, message fields or schemas;
  - define APIs, queues, event buses, graph edges, schedulers, transports,
    delivery guarantees or orchestration topology;
  - select a framework, model, provider, repository, carrier, storage engine,
    backend, deployment or application;
  - assert that each relationship kind needs a separate message, endpoint,
    agent, service or process;
  - copy Direction OS CALL/RESULT objects as a universal substrate protocol;
  - treat any source implementation as substrate authority.

  ## 2. Bounded answer

  The compared sources support a stable distinction between:

  1. the semantic relationship between responsibility-bearing roles;
  2. the lifecycle of the obligation created or modified by that relationship;
  3. the representation used to record the relationship;
  4. the delivery mechanism carrying that representation;
  5. the physical or agent topology in which the roles are implemented.

  An implementation-neutral relationship is provisionally:

  > A typed normative and causal relation between responsibility-bearing roles
  > over a bounded work obligation, state, effect, claim, result or
  > continuation, specifying what responsibility, authority or state meaning
  > changes and what closure is owed.

  The candidate Q3 model is not a universal message catalogue. It is a small
  semantic algebra:

  - five relationship families;
  - twelve candidate primary relation kinds;
  - shared lifecycle distinctions for acceptance, progress, failure,
    cancellation, retry, recovery and continuation;
  - cross-cutting ownership and authority invariants.

  Recommended evaluation orientation for architecture-forge:

  1. Work commitment:
     invoke, delegate, handoff.
  2. Knowledge and observation:
     query, observe/event, evidence/provenance.
  3. Governance and mutation:
     propose, validate, decide/authorize, apply/effect.
  4. Closure:
     return/result.
  5. Continuity:
     continue.

  Acceptance, refusal, progress, input-required, suspension, cancellation,
  failure, retry and recovery are normally lifecycle transitions of one of
  those primary relationships. Treating all of them as unrelated top-level
  message types would obscure which underlying obligation remains open.

  ## 3. Working terms

  These are research terms for evaluating Q3, not accepted substrate entities.

  ### 3.1 Responsibility

  An obligation to perform, decide, preserve, report or close something under
  defined bounds.

  ### 3.2 Accountability

  Retained answerability for integration and outcome. Delegating execution does
  not necessarily remove the delegator's accountability.

  ### 3.3 Capability

  The practical ability to perform an operation. Capability does not itself
  grant permission.

  ### 3.4 Authority

  The legitimate right to decide, permit, deny, revoke or apply within a
  defined scope. Authority cannot be inferred merely from capability,
  possession of data, receipt of a request or production of an event.

  ### 3.5 Current work owner

  The one primary role responsible for the next resolution step and eventual
  closure of one open obligation.

  This is not a permanent central manager or a physical service. Different
  child obligations can have different owners in parallel, and ownership can
  move through an accepted handoff.

  ### 3.6 State owner

  The primary normative role that establishes the authoritative durable version
  of one mutable state boundary. Other roles may read, derive, propose,
  validate or observe without becoming its state owner.

  ### 3.7 Human authority owner

  The human or owner-authorized role whose decision is required for a bounded
  class of effects or commitments.

  ### 3.8 Result

  The semantic settlement of an obligation: what was achieved, not achieved,
  rejected, cancelled, left partial or left unresolved, together with the
  material needed for the next legitimate step.

  An artifact is possible result material; it is not by itself proof that the
  obligation is complete.

  ### 3.9 Continuation

  A carrier-independent preservation of enough accepted semantic state,
  ownership, authority, effect status and pending work to resume legitimately.
  A runtime cursor, thread ID, task ID or previous-response ID may be a useful
  reference but is not sufficient portable continuation.

  ## 4. Primary-source comparison

  ### 4.1 FIPA Communicative Act Library, version J

  Primary evidence:

  - Request asks another agent to perform an action.
  - Agree and Refuse distinguish taking a requested commitment from declining
    it.
  - Propose, Accept Proposal and Reject Proposal distinguish a candidate
    agreement from acceptance or rejection.
  - Query and Inform distinguish asking for knowledge from reporting a claim.
  - Failure reports that an action was attempted but not completed.
  - Not Understood reports that nothing was done as a consequence of an
    uninterpretable act.
  - Cancel withdraws the requester's intention but does not guarantee that the
    performer has actually stopped.

  Q3 support:

  - communicative meaning is distinct from message transport;
  - request, acceptance, refusal, proposal, query, information, failure and
    cancellation are not interchangeable;
  - an open commitment needs a correlated response or closure;
  - cancellation request and effective cancellation must be distinguished.

  Q3 limitation:

  - FIPA's formal semantics depend heavily on beliefs, intentions and
    sincerity assumptions;
  - those mental-state assumptions cannot be promoted directly to arbitrary
    LLMs, software services or humans;
  - it provides neither a durable state-ownership model nor a portable
    continuation contract;
  - its act names are evidence for distinctions, not a required substrate
    vocabulary.

  ### 4.2 W3C PROV-DM

  Primary evidence:

  - provenance describes entities, activities and agents bearing
    responsibility;
  - association assigns responsibility for an activity;
  - delegation assigns authority and responsibility to a delegate while the
    principal retains some responsibility for the outcome;
  - usage, generation, communication, derivation, attribution, association and
    delegation are distinct provenance relations;
  - provenance is domain-agnostic and extensible.

  Q3 support:

  - responsibility and authority can be represented separately from physical
    execution;
  - delegation is not equivalent to complete disappearance of the principal;
  - evidence should preserve activity, agent, usage, generation and derivation
    lineage;
  - an artifact or claim should retain provenance rather than being accepted
    solely because it was delivered.

  Q3 limitation:

  - PROV primarily records what happened in the past;
  - it does not define prospective invocation, cancellation, owner decisions,
    retries, recovery or continuation;
  - provenance can support trust decisions but cannot itself make an effect
    authorized or a result accepted.

  ### 4.3 CloudEvents 1.0.2

  Primary evidence:

  - an occurrence is a captured statement of fact during system operation;
  - an event is a data record expressing an occurrence and its context;
  - events are transported through messages;
  - messages may use different protocols and protocol bindings;
  - one occurrence may produce more than one event;
  - duplicate events may be recognized by source and event identity.

  Q3 support:

  - event meaning is distinct from message and transport;
  - an event reports an occurrence; it is not inherently a command, proposal,
    authorization or result;
  - event consumers do not become state owners merely by observing an event;
  - duplicate observation and source identity are relevant to evidence and
    retry safety.

  Q3 limitation:

  - CloudEvents defines interoperable event data, not process responsibility;
  - it does not determine whether an occurrence claim is true, authorized or
    sufficient evidence;
  - it does not define work ownership, result closure, cancellation,
    continuation or apply authority.

  ### 4.4 Temporal durable-workflow documentation

  Primary evidence:

  - Queries read workflow state without writing it.
  - Signals are asynchronous write requests without an awaited result.
  - Updates are tracked synchronous write requests and can be validated before
    acceptance into durable history.
  - Parent and Child Workflows have distinct state and lifecycle relations.
  - parent closure can propagate cancellation or termination under a defined
    close policy;
  - child execution and external-world Activity execution have different state
    and cancellation properties;
  - retried external Activities should be idempotent because execution may
    occur more than once;
  - transient and permanent failures require different retry treatment;
  - a completed external action can be retried when its completion
    acknowledgement is lost.

  Q3 support:

  - read, asynchronous change request and validated tracked mutation have
    different meanings;
  - parent-child work needs explicit lifecycle and result relations;
  - external effects must be isolated from reasoning and made retry-safe;
  - timeout or missing acknowledgement does not prove that an effect did not
    happen;
  - retry requires attempt bounds and permanent-failure classification;
  - state ownership can remain explicit even with separate execution units.

  Q3 limitation:

  - Query, Signal, Update, Workflow and Activity are Temporal abstractions;
  - deterministic replay is not a universal assumption for LLM-led reasoning;
  - parent-close policies, histories and retry settings are implementation
    mechanisms, not substrate protocol fields;
  - the evidence supports semantic distinctions, not adoption of Temporal.

  ### 4.5 Agent2Agent Protocol 1.0.0

  Primary evidence:

  - Task is a stateful unit of action with working, completed, failed,
    cancelled, rejected and interrupted states;
  - input-required and authorization-required are interrupted rather than
    terminal states;
  - Message is communication, while Artifact is task output;
  - task lifecycle is independent from any one polling, streaming or push
    delivery channel;
  - cancellation is a distinct operation and can be rejected when the task is
    no longer cancellable;
  - errors distinguish authorization, validation, resource and temporary
    system failures;
  - messages can initiate or continue tasks, while critical state must not
    depend solely on transient status messages;
  - protocol bindings preserve operation meaning across different transports.

  Q3 support:

  - logical work identity, conversation context, message, status and output are
    distinct;
  - interrupted work can request input without falsely claiming failure;
  - task state must outlive an individual transport connection;
  - cancellation needs an authoritative terminal outcome;
  - result material should be distinguishable from conversational traffic;
  - transport bindings can vary while operation semantics remain stable.

  Q3 limitation:

  - A2A is an inter-agent protocol rather than a complete process kernel;
  - task and context identifiers are opaque runtime references, not sufficient
    portable continuation;
  - it does not settle internal state ownership, proposal/validation/apply,
    human decision authority or evidence acceptance;
  - its exact objects and states must not be copied as universal entities.

  ### 4.6 OpenJDK JEP 525 Structured Concurrency

  Primary evidence:

  - related concurrent subtasks are treated as one unit of work;
  - unstructured futures can leak work, lose parent-child relationships and
    leave no clear return owner;
  - task and subtask lifetimes form a hierarchy;
  - parent interruption and child failure can propagate cancellation;
  - child results return to the parent scope;
  - structured task relations improve observability and error handling.

  Q3 support:

  - child work needs a parent, bounded lifetime and return path;
  - the parent remains responsible for integrating child outcomes;
  - cancellation propagation follows responsibility structure rather than
    arbitrary connectivity;
  - unowned or detached work is an explicit failure risk;
  - a sparse task/subtask structure can remain coherent without all-to-all
    communication.

  Q3 limitation:

  - JEP 525 is a preview Java in-process concurrency API;
  - thread lifetime and lexical scope cannot be universalized to durable,
    distributed, human-interrupted or multi-carrier work;
  - it supports structured ownership principles, not a substrate topology.

  ### 4.7 OpenAI Agents SDK documentation

  Primary evidence:

  - manager-style agents-as-tools retain control of the conversation and final
    answer while specialists perform bounded subtasks;
  - handoffs make a specialist the active agent for the next part of the
    interaction;
  - handoff inputs can be bounded or filtered;
  - human approval can interrupt an outer run even when the pending effect is
    inside a delegated or handed-off agent;
  - approval and rejection are stored against the paused work and the run can
    resume;
  - final output, rich run items, last active agent and resumable state are
    separate result surfaces;
  - cancellation of streaming execution requires continued cleanup handling.

  Q3 support:

  - bounded delegation with retained integration is distinct from active-control
    handoff;
  - authority gates can remain outside the delegated performer;
  - approval pauses rather than silently completing work;
  - result, trace material, current agent and continuation state are distinct;
  - one implementation can realize different ownership patterns.

  Q3 limitation:

  - the term handoff is framework-specific and may combine routing,
    conversation ownership and delegation;
  - SDK RunState, agent classes, call IDs and previous-response IDs are not
    portable substrate entities;
  - approval implementation details do not establish a universal owner-decision
    protocol;
  - the current APIs are live vendor documentation and may evolve.

  ### 4.8 Anthropic multi-agent research-system engineering report

  Primary evidence:

  - a lead agent decomposes a request into bounded specialist tasks;
  - each subagent needs an objective, output form, tools/sources and clear task
    boundary;
  - subagents return findings to the lead for integration;
  - vague delegation produces duplication and gaps;
  - direct persistent artifacts can reduce information loss while lightweight
    references return to the coordinator;
  - synchronous child execution simplifies coordination but creates blocking;
  - asynchronous execution introduces result coordination, state consistency
    and error-propagation problems.

  Q3 support:

  - delegation quality depends on bounded responsibility and explicit return;
  - the parent integrator need not expose every child interaction to the owner;
  - persistent artifacts can be shared without transferring process ownership;
  - sparse lead-child relations are operationally useful;
  - state and error semantics become more important, not less, when execution
    becomes asynchronous.

  Q3 limitation:

  - this is one production implementation and engineering report, not a
    standard;
  - the orchestrator-worker topology must not be frozen as the substrate
    architecture;
  - direct artifact sharing does not remove the need for result ownership,
    provenance and closure.

  ## 5. Convergent semantic patterns

  ### 5.1 Request is not completion

  Across FIPA, Temporal, A2A and agent frameworks, asking for work does not
  establish that:

  - the target understood it;
  - the target took responsibility;
  - execution began;
  - an effect occurred;
  - the requested outcome succeeded;
  - a returned artifact is accepted.

  Q3 therefore needs semantic closure beyond a bare invocation.

  ### 5.2 Taking responsibility is a distinct transition

  A target may:

  - take the work;
  - refuse it;
  - reject it as unauthorized or invalid;
  - request missing input;
  - report that it is not understood.

  An authoritative instruction may make refusal impermissible under policy, but
  the semantic distinction between instruction, acknowledgement and execution
  still remains.

  ### 5.3 Delegation retains a parent relation

  Delegation repeatedly implies:

  - a parent objective;
  - bounded child responsibility;
  - authority and context bounds;
  - a return path;
  - parent integration;
  - retained principal accountability.

  Delegation is therefore not equivalent to sending context to an independent
  actor and forgetting the work.

  ### 5.4 Handoff is not merely delegation

  Sources expose two materially different patterns:

  - retained-control delegation: a parent or manager remains the active
    integrator and owner-facing responder;
  - active-ownership handoff: a successor becomes responsible for the next
    interaction or continuation.

  Q3 must either define handoff narrowly as accepted active-ownership transfer
  or explicitly separate multiple handoff subtypes. Leaving the term
  unspecified would preserve a high-risk ambiguity.

  ### 5.5 Read, proposal, permission and mutation differ

  Stable distinctions are:

  - query/read observes authoritative state without changing it;
  - proposal offers a candidate change or effect;
  - validation assesses that candidate;
  - owner decision or authorization grants or denies bounded permission;
  - apply/effect establishes the authoritative durable transition or external
    effect;
  - an event reports what occurred.

  A single implementation may perform several of these responsibilities in one
  component or call, but their meanings remain separately testable.

  ### 5.6 Event, evidence and result differ

  - Event reports an occurrence or status transition.
  - Evidence supports or refutes a claim and preserves provenance.
  - Result settles an obligation and returns ownership for integration.

  An event is not automatically reliable evidence. Evidence is not automatically
  accepted truth. An artifact is not automatically a complete result.

  ### 5.7 Work lifecycle outlives delivery lifecycle

  A task or obligation can continue after:

  - an API call returns;
  - a stream disconnects;
  - a chat ends;
  - a model invocation stops;
  - a worker crashes.

  Transport connection state therefore cannot be the authoritative work state.

  ### 5.8 Failure and cancellation require explicit ownership

  Failure, timeout and cancellation are not safe terminal catch-all states:

  - timeout can leave the effect outcome unknown;
  - cancellation request may arrive too late or be refused;
  - child failure returns a resolution obligation to the parent;
  - partial effects require recovery or compensation;
  - retry may duplicate an effect.

  ### 5.9 Sparse responsibility flow can be coherent

  Parent-child task structure, authoritative state owners, bounded
  request/return relations and owner-facing integration repeatedly work without
  every participant communicating with every other participant.

  What must be connected is the chain of responsibility and authority, not an
  all-to-all physical graph.

  ## 6. Material conflicts and unresolved choices

  ### 6.1 Retained control versus transferred active ownership

  Some systems keep a manager responsible for final synthesis. Others transfer
  the active user interaction to a specialist.

  This is a semantic conflict, not merely a transport difference.

  Q3 must distinguish:

  - who owns the child execution;
  - who owns integration;
  - who owns the next owner-facing turn;
  - who retains accountability;
  - what, if any, authority moves.

  ### 6.2 Implicit versus explicit acceptance

  In-process calls often appear to accept work implicitly. Agent and
  cross-boundary protocols expose agree, refuse, reject, input-required and
  not-understood explicitly.

  A universal relation model should preserve the semantic distinction while
  leaving representation and optimization open.

  ### 6.3 Cooperative versus enforced cancellation

  FIPA cancellation withdraws intention but cannot force the target to stop.
  Structured concurrency can propagate interruption within one controlled
  runtime. A2A defines a cancellation operation and terminal task state.

  No universal source supports treating a cancel request as immediate proof of
  cessation or rollback.

  ### 6.4 Parent-mediated versus direct result sharing

  Anthropic reports value from persistent artifacts that can bypass the main
  coordinator for data delivery, while manager patterns return child results
  through a parent.

  Q3 should not require all bytes to traverse the parent. It should require the
  parent/current owner to receive enough semantic result and provenance to
  integrate and close its obligation.

  ### 6.5 Shared versus isolated state

  Some frameworks provide shared conversational context; durable workflow
  systems often isolate child state; multi-agent systems commonly filter or
  minimize context.

  Q3 should freeze authority and ownership semantics, not a shared-memory or
  context propagation topology.

  ### 6.6 Retry defaults

  Some runtimes retry transient failures automatically. Other agent systems
  expose failure for re-planning. External effects may be unsafe to retry.

  Retry therefore cannot be a universal default independent of failure class,
  operation identity and effect-safety evidence.

  ### 6.7 Exact relationship granularity

  Sources support the distinctions but do not agree on whether validation,
  authorization, apply, status, evidence and result should be separate
  protocol verbs, phases, facets or records.

  Q3 can freeze their semantic non-equivalence without freezing one message
  taxonomy.

  ## 7. Candidate Q3 relationship taxonomy

  This taxonomy is proposed for architecture evaluation. It is not accepted
  architecture and does not imply twelve messages or twelve services.

  ### Family A — work commitment

  #### A1. Invoke

  Meaning:

  - request a role to perform or initiate a bounded procedure or action.

  Responsibility effect:

  - opens a requested obligation;
  - does not itself prove that the target took execution responsibility;
  - the initiating/current owner retains resolution responsibility until the
    target takes, refuses or otherwise resolves the request.

  Authority/state effect:

  - does not grant authority beyond the invocation's authorized scope;
  - does not itself mutate durable state.

  Required closure:

  - taken/acknowledged, refused, rejected, input-required, not-understood or
    equivalent resolution;
  - after taking: result, failure, cancellation or continuation.

  Not equivalent to:

  - API call;
  - tool call;
  - queue publication;
  - model prompt;
  - completed work.

  #### A2. Delegate

  Meaning:

  - assign bounded child execution to a role acting on behalf of a parent
    obligation.

  Responsibility effect:

  - after taking, the delegate owns the bounded child execution;
  - the delegator retains parent integration and outcome accountability;
  - the delegate owes a result, failure or explicit unresolved return.

  Authority/state effect:

  - may convey bounded operational authority;
  - does not transfer unrelated human authority, parent accountability or state
    ownership.

  Required closure:

  - result/return to the parent;
  - explicit cancellation propagation policy;
  - explicit handling when the child cannot resolve the work.

  Not equivalent to:

  - complete handoff;
  - unrestricted autonomy;
  - copying all context;
  - spawning a physical agent.

  #### A3. Handoff

  Meaning:

  - transfer active next-step ownership for a named work or interaction scope
    to a successor.

  Responsibility effect:

  - predecessor remains the current owner until the successor takes the
    handoff;
  - on taking, successor becomes the primary active owner for the transferred
    scope;
  - predecessor's retained accountability, supervision or return expectation
    must be explicit rather than assumed.

  Authority/state effect:

  - transfers only the stated active ownership;
  - does not automatically transfer human decision authority, durable state
    ownership or permission to create external effects.

  Required closure:

  - successor acceptance or refusal;
  - unambiguous transfer scope;
  - no interval with no primary owner;
  - continuation or return path if the successor cannot proceed.

  Not equivalent to:

  - routing a message;
  - invoking a helper;
  - changing physical agent topology;
  - silently abandoning the work.

  ### Family B — knowledge and observation

  #### B1. Query

  Meaning:

  - request an observation, derivation or authoritative read.

  Responsibility effect:

  - the queried owner owes an answer, unknown, refusal or input-required
    resolution;
  - no work or state ownership transfer is implied.

  Authority/state effect:

  - read-only with respect to the queried durable boundary;
  - does not authorize later mutation;
  - does not imply a lock unless separately specified downstream.

  Required closure:

  - answer qualified by relevant provenance, version or uncertainty;
  - explicit unknown/refusal rather than fabricated certainty.

  Not equivalent to:

  - proposal;
  - mutation;
  - subscription;
  - durable continuation.

  #### B2. Observe/Event

  Meaning:

  - report an occurrence, status change or observation.

  Responsibility effect:

  - informs interested roles;
  - does not by itself assign next-step ownership;
  - a policy may cause a receiving role to open a new obligation.

  Authority/state effect:

  - reports rather than commands;
  - does not itself authorize or apply a change;
  - the authoritative state owner determines whether the occurrence establishes
    accepted state.

  Required closure:

  - none merely because an event was emitted;
  - any triggered work must have its own explicit owner and lifecycle.

  Not equivalent to:

  - invocation;
  - result;
  - accepted truth;
  - event bus or publish-subscribe topology.

  #### B3. Evidence/Provenance

  Meaning:

  - provide material and lineage supporting, refuting or qualifying a claim,
    event, proposal, validation or result.

  Responsibility effect:

  - evidence producer bears responsibility for the stated provenance and scope;
  - evaluator or authority holder retains responsibility for deciding its
    sufficiency.

  Authority/state effect:

  - evidence alone neither authorizes nor applies;
  - receipt does not make a claim accepted.

  Required closure:

  - attribution, relevant derivation/use information and known limitations;
  - association with the claim or obligation it supports.

  Not equivalent to:

  - result completion;
  - state truth;
  - trace volume;
  - an arbitrary artifact attachment.

  ### Family C — governance and mutation

  #### C1. Propose

  Meaning:

  - offer a candidate decision, durable mutation or external effect with
    rationale, preconditions and evidence.

  Responsibility effect:

  - proposer owns the proposal's coherence and support;
  - target authority or state owner retains decision and apply responsibility.

  Authority/state effect:

  - changes neither permission nor durable state;
  - capability to propose does not imply capability or authority to apply.

  Required closure:

  - validation, rejection, request for evidence or decision routing.

  Not equivalent to:

  - command;
  - authorization;
  - apply;
  - event saying the change happened.

  #### C2. Validate

  Meaning:

  - assess a proposal, input or intended transition against declared
    invariants, policy, evidence and current-state preconditions.

  Responsibility effect:

  - validator owns the correctness and limits of the validation conclusion;
  - proposer/current work owner retains responsibility for the next action.

  Authority/state effect:

  - validation alone does not grant human authority;
  - validation alone does not apply the mutation;
  - one implementation may combine roles, but conformance must preserve the
    semantic distinctions.

  Required closure:

  - valid, invalid, stale, conflicting, evidence-required or equivalent
    resolution with reasons.

  Not equivalent to:

  - owner approval;
  - execution success;
  - writer topology.

  #### C3. Decide/Authorize

  Meaning:

  - an authority holder approves, denies, conditions or revokes permission for
    a specific proposal or effect.

  Responsibility effect:

  - authority holder owns the decision;
  - current work owner owns routing and responding to the decision;
  - effect performer still owns correct execution after authorization.

  Authority/state effect:

  - changes permission status for the exact bounded subject;
  - does not itself prove execution or durable mutation;
  - authorization may become stale if the proposal, evidence or relevant state
    changes.

  Required closure:

  - recorded approval, denial, condition, revocation or unresolved decision;
  - binding to the proposal scope/version sufficiently to prevent substitution.

  Not equivalent to:

  - generic consent;
  - capability;
  - validation;
  - apply.

  #### C4. Apply/Effect

  Meaning:

  - exercise authorized capability to establish an authoritative durable
    transition or external effect.

  Responsibility effect:

  - state/effect owner owns validation of current applicability, execution and
    authoritative outcome reporting;
  - caller/current work owner owns integration and owner-facing closure.

  Authority/state effect:

  - this is the relation through which accepted durable mutation or external
    effect can occur;
  - it may reject stale, invalid, unauthorized or conflicting requests;
  - only authoritative applied outcome, not the earlier proposal or command,
    establishes that the change happened.

  Required closure:

  - applied, rejected, conflict, failed-known-not-done, partial or
    outcome-unknown;
  - evidence sufficient for reconciliation and safe continuation.

  Not equivalent to:

  - proposal;
  - owner approval;
  - arbitrary write access;
  - one physical writer service.

  ### Family D — closure

  #### D1. Return/Result

  Meaning:

  - settle or checkpoint an invocation, delegation, apply operation or other
    obligation and return responsibility for integration.

  Responsibility effect:

  - performer closes its bounded obligation or explicitly identifies what
    remains open;
  - parent/current owner retakes integration responsibility;
  - unresolved work must name its current next-action owner.

  Authority/state effect:

  - reports outcome;
  - does not by itself make non-authoritative state durable;
  - may include authoritative apply receipt when produced by the state/effect
    owner.

  Required closure content at the semantic level:

  - achieved/not achieved status;
  - stop or interruption reason;
  - relevant outputs;
  - evidence/provenance;
  - effect certainty;
  - unresolved obligations and their owners;
  - continuation disposition.

  Exact fields and serialization remain downstream.

  Not equivalent to:

  - last chat message;
  - raw model output;
  - artifact alone;
  - trace alone.

  ### Family E — continuity

  #### E1. Continue

  Meaning:

  - preserve and rebind legitimate work across interruption, checkpoint,
    carrier change, run change or definition evolution.

  Responsibility effect:

  - preserves current and pending owners;
  - does not silently close open work;
  - establishes who owns the next legitimate step after resume.

  Authority/state effect:

  - preserves accepted decisions and effect status without re-authorizing
    unrelated actions;
  - pending authorization remains bound to its original scope and must be
    revalidated when stale;
  - opaque runtime references may assist but cannot be the sole basis.

  Required semantic preservation:

  - work identity and objective;
  - accepted current state or authoritative references;
  - completed and open obligations;
  - current next-action owners;
  - decisions, authority bounds and pending approvals;
  - proposed, applied, failed, partial or unknown effect status;
  - evidence and provenance;
  - procedure/definition compatibility information;
  - next legitimate action and return route.

  Exact continuation entities and schema remain downstream.

  Not equivalent to:

  - transcript copy;
  - one framework's serialized run object;
  - task ID;
  - thread cursor;
  - transport reconnection.

  ## 8. Shared lifecycle distinctions

  The following distinctions should be evaluated as lifecycle semantics attached
  to primary relationships. This note does not freeze exact labels or an enum.

  ### 8.1 Offer and take

  - requested/offered;
  - taken/acknowledged;
  - refused;
  - rejected as invalid or unauthorized;
  - not understood;
  - missing input or authority.

  ### 8.2 Active work

  - working;
  - progress observed;
  - suspended;
  - waiting for named input or decision;
  - checkpointed.

  Waiting is not ownerless. The awaited input or decision has an owner, while
  the containing work owner retains monitoring, escalation and continuation
  responsibility.

  ### 8.3 Cancellation

  - cancellation requested;
  - cancellation accepted/in progress;
  - cancelled with no effect;
  - cancellation refused or not possible;
  - completed before cancellation;
  - applied effect requiring recovery or compensation.

  A cancellation request is not a terminal result.

  ### 8.4 Failure and uncertainty

  At minimum, distinguish:

  1. refusal/rejection before execution;
  2. known not done;
  3. partial outcome;
  4. completed effect with lost acknowledgement;
  5. outcome unknown;
  6. permanent/non-retryable failure;
  7. transient/retryable failure;
  8. unresolved responsibility or ownership.

  A generic "failed" state is insufficient for safe effect handling.

  ### 8.5 Retry

  Retry is a new execution attempt under the same logical obligation or
  operation, not evidence that the previous attempt did nothing.

  A safe retry disposition requires:

  - causal linkage to the prior attempt;
  - a bounded retry policy or decision owner;
  - classification of transient versus permanent failure;
  - effect idempotence, deduplication or prior reconciliation;
  - preservation of prior evidence;
  - no silent expansion of authority.

  ### 8.6 Recovery

  Recovery is not universally equivalent to rollback. Depending on the failure,
  it can mean:

  - resume from continuation;
  - retry a known-safe operation;
  - query/reconcile authoritative state;
  - re-plan and delegate an alternative;
  - repair incomplete durable state;
  - propose and authorize a compensating effect;
  - escalate an owner decision;
  - close as unresolved with an explicit owner.

  Compensation is a new governed effect, not erasure of history.

  ## 9. Cross-cutting responsibility and authority invariants

  These are candidate Q3 evaluation invariants, not approved architecture.

  ### I1. One primary current owner per open obligation

  Every open obligation has exactly one primary current next-action owner.

  Parallel child obligations are permitted, each with its own owner. Their
  parent has one integration owner.

  ### I2. No ownership gap during handoff

  The predecessor retains ownership until the successor takes the bounded
  handoff. Refusal or lost acknowledgement returns to reconciliation rather
  than producing silent abandonment.

  ### I3. Delegation retains parent accountability

  The delegate owns bounded execution. The delegator retains responsibility for
  integration, owner-facing closure and handling child failure unless an
  explicit accepted handoff changes that relation.

  ### I4. One authoritative owner per mutable state boundary

  Many roles may query, derive, propose or validate. One primary normative
  state owner establishes each accepted durable version.

  This does not require one global store, process or physical writer.

  ### I5. Capability does not imply authority

  A role capable of an effect cannot self-grant permission. Receipt of a
  proposal, event or delegated task does not create authority beyond the
  bounded relation.

  ### I6. Validation, authorization and apply remain distinguishable

  One implementation may compose them, but conformance must still prove:

  - what was validated;
  - who had authority;
  - what was actually applied;
  - what evidence supports the outcome.

  ### I7. Every accepted child obligation owes closure

  Completion, failure, cancellation, unresolved return or continuation must
  return to the parent/current owner. Silent child disappearance is invalid.

  ### I8. Result and artifact are separate

  An artifact can be referenced or delivered directly. The result relation
  still declares whether the obligation closed and who owns what remains.

  ### I9. Observation does not create authority

  Event consumers and evidence collectors do not become state, process or
  effect owners merely by receiving information.

  ### I10. Cancellation requires authoritative settlement

  The requester may revoke interest or permission, but only an authoritative
  outcome establishes whether work stopped, completed, remained partial or
  requires compensation.

  ### I11. Unknown effect outcome blocks blind retry

  When an effect might have occurred, the current owner first queries or
  reconciles with the authoritative state/effect owner unless retry safety is
  independently established.

  ### I12. Continuation preserves unresolved ownership

  A checkpoint that omits pending obligations, authority decisions or current
  owners is not sufficient portable continuation.

  ### I13. Owner-facing integration remains explicit

  Internal delegation must ultimately produce:

  - a useful result;
  - a bounded owner decision request;
  - a clear failure;
  - or a portable continuation.

  Internal state/intake/handback bureaucracy is not evidence of live
  owner-facing usefulness.

  ### I14. Semantic adjacency follows obligations

  A role needs a relationship only with:

  - its caller or parent;
  - its accepted child or successor;
  - authoritative state/effect owners it must query or invoke;
  - authority holders from whom a bounded decision is required;
  - evidence/result consumers to whom it owes closure.

  No all-to-all zone communication is required.

  ## 10. Responsibility flow versus transport and topology

  ### 10.1 Semantic relationship

  Specifies:

  - why interaction occurs;
  - which obligation or state it concerns;
  - who owns the next step;
  - what authority is exercised or preserved;
  - whether durable state may change;
  - what response or closure is owed;
  - how failure and continuation behave.

  ### 10.2 Representation

  A packet, object, document, record or message may represent one or more
  relationship transitions.

  Exact representation is downstream.

  ### 10.3 API call

  An API call can realize invoke, query, propose, validate, decide, apply,
  result or several of them together.

  Therefore "API call" is not a semantic relationship kind.

  ### 10.4 Queue or event bus

  A queue or bus controls delivery and fan-out. It does not determine whether
  a payload is a request, event, proposal, result or evidence, nor who owns the
  next action.

  ### 10.5 Graph edge

  A configured graph edge describes possible reachability or control flow in
  one implementation. A responsibility relation is an actual semantic
  obligation or transition.

  Neither implies the other one-to-one.

  ### 10.6 Agent topology

  Manager-worker, peer, swarm, graph, pipeline and single-agent designs can
  realize the same semantic relationships.

  Q3 should not choose among them.

  ### 10.7 Cardinality is not fixed

  - one semantic invocation may require several delivered messages;
  - one synchronous call may collapse invocation, taking, execution and result;
  - one event may be delivered to many observers;
  - one service-zone responsibility may be implemented by several components;
  - one component may implement several responsibility roles.

  Conformance must therefore inspect semantic effects, not count endpoints or
  messages.

  ## 11. Sparse end-to-end stress test

  The labels below are temporary responsibility roles used only to test the
  taxonomy. They are not proposed service zones or deployment blocks.

  - H: human authority owner;
  - W: current owner-facing work owner;
  - P: procedure responsibility;
  - S: authoritative state/source responsibility;
  - D: bounded delegated performer;
  - V: validation responsibility;
  - A: durable apply/external-effect responsibility.

  One implementation could combine several roles. Another could distribute one
  role. The trace tests logical responsibility only.

  ### 11.1 Normal path

  Step 1 — intake and ownership

  - H invokes W with an owner goal.
  - W takes the bounded work and becomes current work owner.
  - If the goal is invalid, unauthorized or unclear, W refuses or requests
    input rather than fabricating progress.

  Step 2 — procedure invocation

  - W invokes P for an applicable bounded procedure.
  - W retains owner-facing integration responsibility.
  - P takes execution responsibility for that procedure scope.

  Step 3 — authoritative reads

  - P queries S for relevant accepted state and source material.
  - S returns scoped observations and provenance.
  - Neither the query nor response mutates state.

  Step 4 — bounded child work

  - P delegates a bounded evidence or execution subtask to D.
  - The delegation states objective, authority bounds, expected output,
    evidence requirement and return obligation at the semantic level.
  - P remains the parent integrator.

  Step 5 — child return

  - D returns evidence and a result to P.
  - Direct persistent artifact references are permitted.
  - P, not the artifact store, owns integration and determines whether the
    delegated obligation is sufficiently resolved.

  Step 6 — proposal

  - P forms a candidate durable change or external effect.
  - P proposes it with rationale and evidence.
  - No durable state has changed.

  Step 7 — validation

  - V validates the exact proposal against current state, policy,
    preconditions, evidence and authority requirements.
  - A valid conclusion is not yet owner authorization or applied state.

  Step 8 — owner decision

  - W presents H with a bounded decision: proposed effect, relevant evidence,
    consequences, reversibility and alternatives.
  - H decides/authorizes, denies or conditions the exact proposal.
  - Internal delegation details need not be exposed unless relevant to the
    decision.

  Step 9 — apply

  - W invokes A with the validated, authorized proposal.
  - A verifies that the authorization and current-state preconditions still
    apply.
  - A applies once or returns rejection/conflict/unknown outcome.

  Step 10 — authoritative outcome

  - A returns the apply result and evidence.
  - A may emit an event describing the occurrence.
  - The event is observation; the authoritative apply result establishes
    whether the durable effect occurred.

  Step 11 — owner-facing result

  - W integrates procedure, evidence, decision and apply outcomes.
  - W returns H a useful result:
    what was done, what was not done, relevant evidence, remaining risk and
    any next decision.

  Step 12 — continuation

  - W emits a portable continuation for any future work.
  - It preserves accepted state, effect status, unresolved obligations,
    current owners and the next legitimate action.
  - A new model, chat or carrier can resume without treating an old runtime
    cursor as authority.

  ### 11.2 Sparse-connectivity observation

  The normal path does not require every role to communicate with every other
  role:

  - H interacts with W for intake, decision and result;
  - W invokes P and A and integrates their returns;
  - P queries S, delegates D and uses V;
  - D returns to P;
  - A owns the authoritative effect outcome;
  - events/evidence may be observed cross-cuttingly without transferring
    process ownership.

  Logical reachability exists where responsibility, authority or state
  ownership requires it. This is enough for end-to-end coherence.

  It does not freeze W as one physical central orchestrator. W is a per-work
  ownership role and may move through handoff.

  ### 11.3 Failure branch — delegated child times out

  - D stops responding.
  - Timeout is not treated as proof that D performed nothing.
  - P remains accountable for the child obligation and records it as
    unresolved.
  - P may query status, request cancellation, safely retry, choose another
    delegate or return a gap.
  - H is not made the accidental owner of internal recovery unless a real
    owner decision is required.

  Verdict: ownership remains coherent.

  ### 11.4 Cancellation branch — before apply

  - H cancels after proposal but before apply.
  - W issues cancellation/revocation against the open work and any pending
    effect authority.
  - A authoritatively confirms that no effect was applied, or reports a race.
  - W returns a cancelled result and continuation.

  Verdict: no effect is inferred merely from proposal or approval.

  ### 11.5 Cancellation branch — apply outcome uncertain

  - A may have completed the effect, but its acknowledgement is lost.
  - H requests cancellation.
  - W does not report "cancelled" and does not blindly invoke A again.
  - W queries/reconciles with A or authoritative state.
  - If applied, W reports applied state and routes any compensating proposal
    through validation and authority.
  - If not applied, cancellation can settle as effective.
  - If still unknown, W preserves `outcome_unknown`, a named resolution owner
    and a continuation.

  Verdict: cancellation and failure semantics protect against false reporting
  and duplicate effects.

  ### 11.6 Retry branch — duplicate apply delivery

  - The same logical apply operation is delivered again.
  - A uses operation identity or equivalent semantic deduplication/idempotence
    evidence to return the existing authoritative result.
  - If A cannot establish retry safety, it rejects or requires reconciliation
    rather than applying blindly.

  Verdict: retry is an attempt relation, not permission to repeat effects.

  ### 11.7 Carrier-switch branch

  - Work checkpoints after H authorizes but before A applies.
  - A fresh carrier reads the continuation.
  - It reconstructs the pending apply obligation, exact authorization scope,
    current owner and state preconditions.
  - It revalidates staleness where required, then resumes.
  - It does not request broad re-approval solely because the runtime changed,
    and it does not apply if the preserved authorization is no longer valid.

  Verdict: portable continuation can preserve semantic legitimacy without a
  fixed runtime identifier or transport.

  ### 11.8 Stress-test verdict

  PASS, as research evidence for Q3 forge.

  The candidate semantics can support an end-to-end owner-facing process
  without all-to-all zone communication, provided the architecture preserves:

  - one primary current owner per open obligation;
  - explicit delegation and handoff effects;
  - authoritative state/effect ownership;
  - proposal/validation/decision/apply separation;
  - explicit result return;
  - failure, cancellation and unknown-outcome distinctions;
  - portable continuation.

  This is not proof that one particular physical graph, manager or transport is
  universally optimal.

  ## 12. Candidate architecture directions for forge evaluation

  These are research directions, not owner-approved choices.

  ### Direction A — flat communicative-act catalogue

  Define a large list of top-level acts and lifecycle messages.

  Useful because:

  - individual meanings are explicit.

  Bad, because:

  - it risks turning semantics into a packet schema;
  - lifecycle variants multiply rapidly;
  - responsibility ownership can disappear behind message names;
  - it encourages one-to-one mapping to endpoints or services.

  ### Direction B — relationship families plus lifecycle and ownership invariants

  Define a bounded set of primary relations, shared lifecycle distinctions and
  cross-cutting ownership/authority rules.

  Useful because:

  - semantic non-equivalence remains visible;
  - failure and cancellation remain attached to their open obligation;
  - representation and topology remain open;
  - conformance can test responsibility effects rather than message syntax.

  Bad, because:

  - forge must set clear boundaries so relation families do not become vague
    generic labels.

  Research recommendation: evaluate this direction first.

  ### Direction C — one generic relation with arbitrary attributes

  Represent every interaction as one generic record with intent, status and
  metadata.

  Useful because:

  - minimal primitive count and maximum extensibility.

  Bad, because:

  - critical distinctions can become optional metadata;
  - interoperability and conformance become weak;
  - proposal may be confused with apply, event with command and delegation
    with handoff.

  ## 13. Evidence confidence

  ### High confidence

  Cross-source support is strong for:

  - semantic relationship versus transport separation;
  - request versus execution/result separation;
  - read versus mutation separation;
  - proposal versus accepted/applied change separation;
  - event versus command separation;
  - delegation retaining a parent/accountability relation;
  - explicit task lifecycle and terminal/interrupted distinctions;
  - cancellation request versus effective cancellation;
  - retry risk for external effects;
  - result/artifact/status distinctions;
  - sparse parent-child and authoritative-owner flow.

  ### Moderate confidence

  This note synthesizes, rather than directly inherits, support for:

  - exactly five relationship families;
  - the twelve candidate relation kinds;
  - one primary current next-action owner as a universal process invariant;
  - accepted handoff as the point of active-ownership transfer;
  - treating failure, cancellation, retry and recovery primarily as lifecycle
    semantics rather than independent relation families;
  - requiring effect-certainty status in every effect result.

  These are suitable for architecture-forge evaluation, not automatic
  acceptance.

  ### Lower confidence or still open

  Primary sources do not settle:

  - the exact entity model for obligation, work, run, procedure, proposal,
    decision, effect and continuation;
  - exact correlation or identity semantics;
  - whether validation and authorization need separate externally visible
    relations in every realization;
  - whether event and evidence require separate protocol representations;
  - the exact transfer atomicity and acknowledgement model for handoff;
  - shared-state conflict resolution;
  - compensation policy for every effect class;
  - exact continuation minimum or compatibility model;
  - whether one source of state truth can be distributed across several
    physical writers;
  - the final service-zone list.

  ## 14. Evidence limits

  1. No reviewed source defines the whole desired operating-substrate.
  2. FIPA is semantically rich but old and mentalistic.
  3. PROV is retrospective provenance, not prospective control flow.
  4. CloudEvents defines event data and bindings, not authority or process
     ownership.
  5. Temporal provides strong durability evidence but assumes one durable
     workflow realization and deterministic replay constraints.
  6. A2A defines inter-agent task exchange, not internal substrate state or
     owner authority.
  7. JEP 525 concerns in-process Java concurrency and remains a preview API.
  8. OpenAI and Anthropic material documents evolving vendor implementations,
     not standards.
  9. No source provides a universal carrier-neutral continuation contract.
  10. No source proves owner-facing live usefulness merely from protocol
      completeness.
  11. The sparse-flow verdict is a semantic stress-test result, not a
      performance or distributed-systems proof.
  12. Exact taxonomy cardinality is a research synthesis.

  Evidence that would materially change the candidate answer includes:

  - primary cross-domain evidence that safe handoff needs no acceptance or
    reconciliation;
  - a universal effect model that removes uncertain outcomes and duplicate
    execution;
  - a proven responsibility model with no primary owner for open obligations;
  - evidence that durable state can safely be accepted from arbitrary event
    observers without a normative state owner;
  - live owner-facing evidence showing all-to-all responsibility communication
    is necessary rather than merely one implementation choice.

  ## 15. Premature-freeze risks

  Q3 forge should explicitly reject these leaks:

  1. Treating relation names as a mandatory message schema.
  2. Turning each relation family into a service block.
  3. Turning current work ownership into one permanent central orchestrator.
  4. Requiring every zone to communicate directly with every other zone.
  5. Inferring an event bus because event semantics exist.
  6. Inferring synchronous APIs because request/result semantics exist.
  7. Inferring a single physical writer from one normative state owner.
  8. Treating a model or agent as the responsibility owner by default.
  9. Treating capability possession as authority.
  10. Treating proposal, validation, authorization and apply as synonyms.
  11. Treating a cancellation request as rollback or confirmed stop.
  12. Retrying every failure automatically.
  13. Treating timeout as known failure.
  14. Treating raw output or artifact as a complete result.
  15. Treating traces as accepted evidence without provenance and evaluation.
  16. Treating runtime task/thread/conversation IDs as portable continuation.
  17. Copying one framework's handoff meaning without defining ownership
      transfer.
  18. Exposing internal intake/state/handback bureaucracy as the owner-facing
      process.

  ## 16. Downstream questions

  These remain downstream and do not block bounded Q3 forge.

  ### Q3 forge must decide

  - the accepted definition of a semantic relationship;
  - the bounded relationship taxonomy or grouping rule;
  - the exact responsibility difference between invoke, delegate and handoff;
  - whether one primary current owner per open obligation is invariant;
  - the state-ownership and authority effects of query, proposal, validation,
    decision and apply;
  - required distinctions among event, evidence, artifact and result;
  - minimum failure, cancellation, retry, recovery and unresolved-ownership
    semantics;
  - the sparse semantic-adjacency rule.

  ### Existing downstream graph routes

  - Q7 routing/procedure:
    how a suitable responsibility target is selected.
  - Q8 live interface:
    how owner decisions, interruption, progress and correction are presented.
  - Q9 result/handback:
    exact result and continuation semantics.
  - Q10 authority/effects:
    effect classes, authority policy and gate criteria.
  - Q11 evolution:
    compatibility when definitions and policies change.
  - Q12 structured communication:
    entity, correlation, representation and protocol contract.
  - Q13 proof:
    conformance scenarios for ownership, cancellation, retry, unknown outcome,
    cross-carrier continuation and owner usefulness.
  - Q14 carrier:
    mappings to chat, files, applications and automated transports.
  - Q15 graph growth:
    classification of any newly discovered architectural entities.

  No new top-level graph node is required by this research.

  ## 17. Graph, gap and forge verdict

  Hidden prerequisite: none found.

  Why Q3 is ready:

  - Q1 provides the stable kernel, continuation and validated-apply locks;
  - Q2 provides responsibility-family classification, atomic ownership and the
    no-physical-block rule;
  - primary sources provide enough convergent distinctions to compare bounded
    Q3 answer directions;
  - the candidate semantics pass an end-to-end owner-facing flow without
    selecting a topology or final service-zone list;
  - unresolved entity/schema questions can remain downstream.

  graph_verdict:

  - return to the existing Q3 node;
  - no top-level cartography rebalance;
  - no implementation activation;
  - next session is one bounded Q3 architecture-forge.

  gap_event: none.

  ## 18. Primary-source register

  1. FIPA Communicative Act Library Specification, version J,
     2002-12-03.
     https://www.fipa.org/specs/fipa00037/SC00037J.html

  2. W3C PROV-DM, W3C Recommendation, 2013-04-30.
     https://www.w3.org/TR/prov-dm/

  3. CloudEvents Specification 1.0.2.
     https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md

  4. Temporal Workflow message passing.
     https://docs.temporal.io/encyclopedia/workflow-message-passing

     Temporal Child Workflows.
     https://docs.temporal.io/child-workflows

     Temporal Activity Definition and idempotency.
     https://docs.temporal.io/activity-definition

     Temporal Retry Policies.
     https://docs.temporal.io/encyclopedia/retry-policies

  5. Agent2Agent Protocol Specification, latest released version 1.0.0
     observed 2026-07-10.
     https://a2a-protocol.org/latest/specification/

  6. OpenJDK JEP 525: Structured Concurrency, Sixth Preview,
     JDK 26, updated 2026-01-21.
     https://openjdk.org/jeps/525

  7. OpenAI Agents SDK live documentation observed 2026-07-10.

     Agent orchestration:
     https://openai.github.io/openai-agents-python/multi_agent/

     Handoffs:
     https://openai.github.io/openai-agents-python/handoffs/

     Human in the loop:
     https://openai.github.io/openai-agents-python/human_in_the_loop/

     Results:
     https://openai.github.io/openai-agents-python/results/

  8. Anthropic, How we built our multi-agent research system,
     published 2025-06-13.
     https://www.anthropic.com/engineering/multi-agent-research-system

  END_OF_FILE: live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md

evidence:
  internal_sources_read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
    - live/solmax/plays/architecture-forge.md
    - os/KERNEL.md
    - os/plays/research.md
    - os/schema/packets.md

  primary_source_families_compared:
    - FIPA Communicative Act Library
    - W3C PROV-DM
    - CloudEvents 1.0.2
    - Temporal durable-workflow documentation
    - Agent2Agent Protocol 1.0.0
    - OpenJDK JEP 525 Structured Concurrency
    - OpenAI Agents SDK documentation
    - Anthropic multi-agent research-system engineering report

  load_bearing_evidence:
    - FIPA separates request, agreement/refusal, proposal, query, failure,
      cancellation and not-understood.
    - PROV assigns responsibility to agents and retains principal
      responsibility under delegation.
    - CloudEvents separates occurrence, event, message and protocol binding.
    - Temporal separates query, asynchronous change request, tracked validated
      update, child work, external effect, retry and authoritative history.
    - A2A separates task, message, status, artifact and transport lifecycle.
    - Structured concurrency demonstrates parent-child lifetime, return and
      cancellation obligations.
    - OpenAI distinguishes manager-retained delegation from active-agent
      handoff and preserves approval interruptions.
    - Anthropic demonstrates bounded child tasks, parent integration, sparse
      coordination and asynchronous state/error risks.

  confidence:
    established:
      - relationship meaning is not transport or topology;
      - request, result, event, evidence and mutation are semantically distinct;
      - delegation needs bounded ownership and return;
      - cancellation and failure need explicit lifecycle resolution;
      - sparse responsibility flow can remain coherent.
    candidate_inference:
      - five families and twelve primary relation kinds;
      - one primary current next-action owner per open obligation;
      - accepted handoff as the active-ownership transfer point;
      - failure/cancel/retry/recovery as lifecycle semantics.
    open:
      - exact entity and correlation model;
      - exact representation/schema;
      - final relationship names and granularity;
      - physical state/writer/orchestration topology;
      - final service-zone list.

state_changes: |
  No repository files were created or modified by this session.

  Mechanical writer should apply exactly:

  1. Create the Q3 research work artifact.

     Path:
     live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md

     Content:
     Copy the complete research note from RESULT.outcome beginning with:

     "# Research note — implementation-neutral service-zone relationships and responsibility flow"

     and ending with:

     "END_OF_FILE: live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md"

  2. Create the ready Q3 architecture-forge CALL.

     Path:
     live/solmax/work/calls/c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md

     Content:
     Copy the complete CALL from RESULT.next beginning with:

     "CALL c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001"

     and ending with its matching END_OF_FILE marker.

  3. Update live/solmax/NOW.md.

     Change:

     route_status: operating_substrate_q2_service_zone_classification_accepted_q3_relationship_research_next

     To:

     route_status: operating_substrate_q3_relationship_research_ready_for_forge

     In owner_directive, append this exact checkpoint:

     Q3 service-zone relationship research checkpoint:
     - Primary-source comparison across FIPA ACL, W3C PROV-DM, CloudEvents,
       Temporal, A2A, Structured Concurrency, OpenAI Agents SDK and Anthropic
       multi-agent engineering is complete.
     - This is research input, not an approved Q3 architecture answer.
     - Research supports typed semantic relationships between responsibility
       instances, not API calls, queues, event buses, graph edges or physical
       service topology.
     - Candidate evaluation taxonomy groups invoke/delegate/handoff;
       query/event/evidence; propose/validate/decide/apply; result; and
       continuation, with shared lifecycle semantics for acceptance, failure,
       cancellation, retry and recovery.
     - One primary current next-action owner per open obligation, one
       authoritative owner per mutable state boundary and explicit unresolved
       ownership are candidate Q3 invariants.
     - Cancellation request is not proof of stop; timeout is not proof of
       failure; unknown effect outcome requires reconciliation before unsafe
       retry.
     - A sparse logical responsibility flow passed the intake-through-
       procedure/effect/result/continuation stress test without requiring
       all-to-all zone communication or a central physical orchestrator.
     - gap_event: none. Exact entities, correlation, schema, transport,
       topology and final service-block list remain downstream.
     - Next route is the Q3 service-zone relationship architecture-forge.

     Keep:

     open_calls: []

     Do not add the ready architecture-forge CALL to open_calls until that
     session actually starts.

     Replace NOW.next with:

     work/calls/c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md

     Append to preserved_evidence:

     - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
     - live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-best-practice-research-001.md
     - live/solmax/work/calls/c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md

     Keep tasks, recurring, decisions and active_bet unchanged.

  4. Append live/solmax/LOG.md:

     2026-07-10 — solmax/g-operating-substrate research: Q3 implementation-
     neutral relationship and responsibility-flow primary-source note completed
     across FIPA, PROV, CloudEvents, Temporal, A2A, Structured Concurrency,
     OpenAI and Anthropic; five-family/twelve-relation candidate taxonomy,
     ownership/authority/failure semantics and sparse end-to-end stress test
     derived; gap_event none; next Q3 architecture-forge. →
     history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-best-practice-research-001.md

  5. Create the history record.

     Path:
     live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-best-practice-research-001.md

     Content:
     This complete RESULT, including its final history END_OF_FILE marker.

  6. Do not modify:

     - live/solmax/CHARTER.md
     - live/solmax/TREE.md
     - either accepted architecture card
     - the Q2 classification card
     - the accepted cartography graph
     - any Direction OS play/schema
     - any implementation or product repository

captures:
  - Q13 proof should include a lost apply-acknowledgement scenario where the
    effect may have happened and blind retry must be rejected.
  - Q13 proof should attempt a handoff whose successor never acknowledges
    ownership; the predecessor must remain responsible or enter explicit
    reconciliation.
  - Q13 proof should attempt child timeout, cancellation race, duplicate apply,
    stale owner approval and cross-carrier resume.
  - Q8/Q9 proof should measure owner usefulness and reject a technically
    complete flow that exposes state/intake/handback bureaucracy instead of a
    useful decision or result.
  - Q12 should preserve the semantic distinction between event, evidence,
    artifact and result even if one transport envelope carries several of them.
  - Q12/Q14 should allow direct artifact delivery without treating the artifact
    store or recipient as the process owner.
  - Q10 should define which human authorities may be delegated, if any; agent
    capability must not silently become owner authority.
  - Q9/Q14 should treat runtime identifiers only as optional references inside
    portable continuation.
  - A future formal relation-instance state machine may be useful, but designing
    it now would prematurely freeze entities and schema.
  - Privacy/minimum-context behavior at delegation and handoff boundaries is
    downstream and should be tested before production readiness.

decisions_needed: []

play_check:
  - 1 Recite: done — the bounded Q3 question, accepted Q1/Q2 locks,
    prohibited implementation choices, requested RESULT shape and focused
    session budget were restated.
  - 2 Investigate: done — all named internal inputs were read through their
    END_OF_FILE markers, and eight relevant primary-source families were
    compared.
  - 3 Confidence: done — cross-source convergence was separated from candidate
    synthesis; material conflicts, source limits, confidence levels,
    premature-freeze risks and answer-change conditions were recorded.
  - 4 Close: done — the bounded research note, candidate taxonomy,
    responsibility/authority/failure model, sparse end-to-end stress-test
    verdict, graph/gap verdict, exact writer state_changes and ready Q3
    architecture-forge CALL are returned.

log: |
  solmax research
  c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001:
  Q3 primary-source relationship semantics complete; five-family,
  twelve-relation candidate taxonomy and lifecycle/ownership invariants
  derived; sparse owner-facing flow passes; gap_event none; return to parent
  with ready Q3 architecture-forge CALL.

next: |
  return-to-parent s-solmax-operating-substrate-service-zone-classification-architecture-forge-001

  CALL c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
  to: session
  direction: solmax
  play: local/architecture-forge
  node: g-operating-substrate
  goal: |
    One owner-approved Q3 architecture card exists for implementation-neutral
    semantic relationships and responsibility flow between candidate service
    zones, preserving Q1/Q2 while selecting no transport, message schema,
    orchestration topology or final service-block list.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
    - live/solmax/plays/architecture-forge.md

    Accepted parent locks:
    - operating-substrate is a stable, model-neutral and carrier-neutral kernel
      with pluggable process packs;
    - process/domain does not modify kernel semantics;
    - service zones are semantic responsibility families, not physical
      deployment blocks;
    - atomic responsibility claims are classified independently and have one
      primary normative owner;
    - portable continuation is mandatory while its exact schema remains open;
    - durable mutation crosses a logical validated writer/apply boundary while
      physical topology remains open;
    - no final service-block list is accepted;
    - Q1 and Q2 are accepted and must not be revised by Q3.

    Q3 forge handoff:
    - plain_question: "Какие смысловые отношения должны связывать
      ответственности end-to-end: кто вызывает, делегирует, передаёт
      ownership, читает, предлагает, валидирует, решает, применяет, возвращает
      результат и сохраняет continuation?"
    - why_it_matters: "Без общей семантики pile of zones не образует связный
      процесс: ownership может потеряться, proposal смешаться с apply,
      cancellation — с rollback, а artifact — с result."
    - must_decide: "Определение semantic relationship; bounded taxonomy или
      grouping rule; responsibility/authority/state effects; delegation versus
      handoff; lifecycle obligations for failure, cancellation, retry,
      unresolved ownership, recovery and continuation; sparse adjacency rule."
    - must_not_decide: "Message/entity schema, API, queue, event bus, graph
      runtime, scheduler, transport, orchestration topology, physical writer,
      framework or final service-zone list."
    - expected_answer_shape: call_protocol
    - return_to_graph_if: "The answer cannot assign unambiguous current
      ownership and state/authority effects through the tested end-to-end flow
      without choosing a transport, topology or final zone list."

    Research orientation:
    - Relationship meaning is distinct from representation, delivery and
      physical topology.
    - Candidate evaluation model has five families:
      work commitment; knowledge/observation; governance/mutation; closure;
      continuity.
    - Candidate primary kinds are invoke, delegate, handoff, query,
      observe/event, evidence/provenance, propose, validate, decide/authorize,
      apply/effect, return/result and continue.
    - Acceptance, progress, input-required, failure, cancellation, retry and
      recovery are candidate lifecycle semantics attached to open obligations,
      not necessarily independent top-level relation types.
    - Delegation gives a child bounded execution ownership while the parent
      retains integration/accountability.
    - Handoff is candidate accepted transfer of active next-step ownership;
      it must not automatically transfer human authority or state ownership.
    - Query, proposal, validation, authorization, apply and event are
      semantically non-equivalent even when one implementation collapses them.
    - Every open obligation should be evaluated for one primary current
      next-action owner; every mutable boundary for one primary normative state
      owner.
    - Cancellation request is not proof of stop. Timeout is not proof that an
      effect did not occur. Unknown outcome blocks blind retry.
    - Sparse logical responsibility flow passed the owner-facing stress test;
      no all-to-all communication or central physical orchestrator is required.
    - Research recommendation is relationship families plus shared lifecycle
      and ownership invariants, not a flat message catalogue or one untyped
      generic relation.
    - gap_event from research: none.
  boundaries: |
    Do not revise or reopen Q1 or Q2.
    Do not freeze a final service-zone or service-block list.
    Do not turn relationship kinds into required services, modules, agents,
    processes, files or deployment units.
    Do not define message/entity schemas, identifiers, correlation fields,
    packet formats, APIs, queues, event buses, graph runtimes, schedulers,
    orchestration topology or transport.
    Do not select a framework, provider, model, repository, backend, carrier,
    storage engine, deployment or application.
    Do not freeze one central manager, one physical writer or all-to-all
    communication.
    Do not universalize FIPA, PROV, CloudEvents, Temporal, A2A, Structured
    Concurrency, OpenAI, Anthropic or Direction OS object names.
    Do not implement.
    Do not change Direction OS.
  done_when: |
    One atomic Q3 architecture card is explicitly owner-approved and:

    1. defines semantic relationship independently from message, API,
       transport, graph edge and physical topology;
    2. freezes a bounded relationship taxonomy or principled grouping rule
       without defining a message schema;
    3. distinguishes invocation, bounded delegation and active-ownership
       handoff, including what responsibility/accountability remains;
    4. distinguishes query, proposal, validation, owner decision/authorization,
       apply/effect and event;
    5. distinguishes event, evidence, artifact, result and continuation;
    6. states how one primary current next-action owner is maintained for every
       open obligation, including handoff and waiting states;
    7. states how authoritative mutable-state ownership and human effect
       authority behave across relationships;
    8. covers refusal, input-required, failure-known-not-done, partial effect,
       unknown outcome, cancellation request/effective cancellation,
       retryability, recovery, compensation and unresolved ownership at the
       semantic level;
    9. states the result/return and portable-continuation obligations while
       leaving exact schema open;
    10. demonstrates a coherent owner-facing intake-through-procedure/effect/
        result/continuation flow without requiring every zone to communicate
        with every other zone;
    11. records rejected alternatives, evidence limits, child/downstream
        questions and any gap_event;
    12. preserves Q1/Q2 and selects no implementation, topology, transport or
        final service-block list.
  return: |
    RESULT with the accepted Q3 architecture card, owner choice and approval
    words, rejected alternatives, downstream questions, stress-test and
    graph/gap verdict, exact state_changes and the next graph route.
  budget: one focused session
  parent: s-solmax-operating-substrate-service-zone-classification-architecture-forge-001
  surface: chatgpt

  END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md

END_OF_FILE: live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-best-practice-research-001.md
