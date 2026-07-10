# Operating-substrate architecture card — semantic service-zone relationships and responsibility flow

status: accepted
accepted_at: 2026-07-10
session: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
call: c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
card_id: operating-substrate-service-zone-relationship-001
graph_nodes:
  - q03_service_zone_relationships

## Owner approval

diverge_choice: |
  "A"

freeze_words: |
  "Approve v1"

## Question

Какие implementation-neutral смысловые отношения должны связывать
ответственности end-to-end: кто инициирует, принимает, делегирует,
передаёт active ownership, читает, наблюдает, предлагает, валидирует,
решает, применяет, возвращает результат и сохраняет continuation?

## Preserved parent locks

This card does not revise Q1 or Q2:

- operating-substrate remains a stable, model-neutral and
  carrier-neutral kernel with pluggable process packs;
- process packs and domain policy do not modify kernel semantics;
- service zones are semantic responsibility families, not physical
  modules, services, agents, processes, files or deployments;
- atomic responsibility claims are classified independently;
- every atomic claim has one primary normative owner;
- portable continuation is mandatory while its exact entity model,
  schema and serialization remain open;
- durable mutation crosses a logical validated writer/apply boundary
  while physical topology remains open;
- no final service-zone or service-block list is accepted.

## Frozen answer

### Semantic relationship

A semantic relationship is a typed normative and causal relation between
responsibility-bearing roles over a bounded obligation, state boundary,
claim, decision, effect, result or continuation.

It specifies:

1. what bounded subject the interaction concerns;
2. who owns the next action before and after the transition;
3. what accountability is retained;
4. what authority is exercised, transferred or explicitly not
   transferred;
5. whether authoritative state or the external world may change;
6. what acceptance, response, closure, recovery or continuation is owed.

A semantic relationship is not:

- a message or message type;
- a packet, object or entity schema;
- an API or tool call;
- a queue publication or event-bus delivery;
- a configured graph edge;
- a scheduler transition;
- a transport connection;
- a service, module, agent, process or deployment boundary.

One delivered message or synchronous call may realize several semantic
transitions. One semantic relationship may require several messages or
records. Conformance evaluates responsibility, authority, state effects
and closure rather than counting messages, endpoints or components.

### Required semantic facets

Every relationship instance must make it possible to determine at the
semantic level:

- the bounded obligation, state, claim, proposal or effect concerned;
- the source and target responsibility roles;
- the primary current next-action owner before and after the transition;
- retained accountability and integration responsibility;
- authority exercised, granted, denied, preserved or revoked;
- authoritative state/effect meaning;
- required acceptance or refusal, where applicable;
- required closure;
- failure, cancellation, retry, recovery and continuation disposition.

These are semantic requirements, not mandatory message fields.

## Responsibility loci

### Primary normative owner

The Q2-level owner of an atomic responsibility claim. Q3 does not
reclassify these claims.

### Current next-action owner

The one primary role responsible for the next resolution step for one
open obligation.

This is instance-level ownership. It does not imply a permanent central
orchestrator or one physical manager.

### Integration/accountability owner

The role responsible for integrating child or specialist outcomes into
the parent result, handling child failure and producing owner-facing
closure.

### Authoritative state owner

The primary normative role that establishes each accepted durable version
of one mutable-state boundary.

Other roles may query, derive, propose, validate, observe or produce
evidence without becoming the state owner.

### Human authority owner

The human or explicitly owner-authorized role whose decision is required
for a bounded class of effects or commitments.

Capability, possession of data, receipt of a request, delegation,
handoff, event or evidence does not itself grant human authority.

## Bounded relationship taxonomy

Five families and twelve primary semantic kinds are accepted.

Their semantic non-equivalence is frozen. Their names do not prescribe
message types, packet schemas, endpoints, services or agents.

### Family A — Work commitment

#### A1. Invoke

Meaning:

- request a role to perform or initiate a bounded procedure or action.

Responsibility effect:

- opens a requested obligation;
- does not itself prove the target understood, accepted or began work;
- the initiator/current owner retains resolution responsibility until
  the target takes, refuses or otherwise resolves the request.

Authority and state effect:

- grants no authority beyond the already authorized bounded scope;
- does not itself mutate durable state.

Owed closure:

- taken or acknowledged;
- refused;
- rejected as invalid or unauthorized;
- input-required;
- not-understood;
- after acceptance: result, failure, cancellation or continuation.

Invoke is not equivalent to an API call, tool call, queue publication,
model prompt or completed work.

#### A2. Delegate

Meaning:

- assign bounded child execution to a role acting under a parent
  obligation.

Responsibility effect:

- after acceptance, the delegate owns the bounded child execution;
- the delegator retains parent integration, outcome accountability and
  owner-facing closure;
- the delegate owes result, failure or explicit unresolved return.

Authority and state effect:

- may convey explicitly bounded operational authority;
- does not transfer unrelated human authority, parent accountability or
  authoritative state ownership.

Owed closure:

- result or unresolved return to the parent/current integration owner;
- explicit cancellation and failure propagation meaning;
- explicit disposition when the child cannot resolve the work.

Delegate is not equivalent to unrestricted autonomy, complete handoff,
copying all context or spawning a physical agent.

#### A3. Handoff

Meaning:

- transfer active next-step ownership for a named bounded work or
  interaction scope to a successor.

Responsibility effect:

- the predecessor remains current owner until the successor accepts;
- after acceptance, the successor becomes primary current owner of the
  transferred scope;
- retained supervision, accountability and return expectation must be
  explicit rather than assumed;
- refusal, ambiguity or lost acknowledgement leads to reconciliation,
  not silent abandonment.

Authority and state effect:

- transfers only the stated active ownership;
- does not automatically transfer human authority, state ownership or
  permission for external effects.

Owed closure:

- successor acceptance or refusal;
- unambiguous transfer scope;
- no interval without a primary owner;
- continuation or route-back when the successor cannot proceed.

Handoff is not equivalent to routing a message, invoking a helper or
changing physical agent topology.

### Family B — Knowledge and observation

#### B1. Query

Meaning:

- request an authoritative read, observation or derivation.

Responsibility effect:

- the queried role owes an answer, unknown, refusal or input-required
  resolution;
- work ownership and state ownership do not transfer.

Authority and state effect:

- read-only with respect to the queried durable boundary;
- does not authorize later mutation;
- does not create a lock or reservation unless defined separately
  downstream.

Owed closure:

- scoped answer with relevant provenance, version and uncertainty;
- explicit unknown or refusal rather than fabricated certainty.

Query is not equivalent to proposal, mutation, subscription or durable
continuation.

#### B2. Observe / Event

Meaning:

- report an occurrence, status change or observation.

Responsibility effect:

- informs interested roles;
- does not itself assign next-step ownership;
- a policy may cause a receiver to open a new obligation, which must
  receive its own explicit owner and lifecycle.

Authority and state effect:

- reports rather than commands;
- does not authorize or apply a change;
- the authoritative state owner determines whether the occurrence
  establishes accepted state.

Owed closure:

- none merely because an event was emitted;
- any triggered work must have its own explicit obligation and owner.

Event is not equivalent to invocation, result, accepted truth, an event
bus or publish-subscribe topology.

#### B3. Evidence / Provenance

Meaning:

- provide material and lineage supporting, refuting or qualifying a
  claim, event, proposal, validation or result.

Responsibility effect:

- the evidence producer is responsible for declared provenance,
  derivation and scope;
- the evaluator, authority holder or state owner retains responsibility
  for judging sufficiency.

Authority and state effect:

- evidence alone neither authorizes nor applies;
- receipt does not make a claim accepted truth.

Owed closure:

- attribution and relevant derivation/use information;
- known limitations;
- association with the claim or obligation it supports.

Evidence is not equivalent to result completion, state truth, trace
volume or an arbitrary artifact attachment.

### Family C — Governance and mutation

#### C1. Propose

Meaning:

- offer a candidate decision, durable mutation or external effect with
  rationale, preconditions and evidence.

Responsibility effect:

- the proposer owns proposal coherence and support;
- the target authority holder or state/effect owner retains decision and
  apply responsibility.

Authority and state effect:

- changes neither permission nor durable state;
- capability to propose does not imply authority to apply.

Owed closure:

- validation;
- rejection;
- request for evidence;
- routing to an appropriate decision owner.

Proposal is not equivalent to command, authorization, apply or an event
stating that the change occurred.

#### C2. Validate

Meaning:

- assess a proposal, input or intended transition against declared
  invariants, policy, evidence and current-state preconditions.

Responsibility effect:

- the validator owns the correctness and declared limits of its
  conclusion;
- the current work owner retains responsibility for the next route.

Authority and state effect:

- validation alone does not grant human authority;
- validation alone does not apply mutation;
- one implementation may combine roles, but conformance must preserve the
  semantic distinctions.

Owed closure:

- valid;
- invalid;
- stale;
- conflicting;
- evidence-required;
- another explicit verdict with reasons.

Validation is not equivalent to owner approval, execution success or
writer topology.

#### C3. Decide / Authorize

Meaning:

- an authority holder approves, denies, conditions or revokes permission
  for a specific proposal or effect.

Responsibility effect:

- the authority holder owns the decision;
- the current work owner owns routing and responding to it;
- the effect performer still owns correct execution after authorization.

Authority and state effect:

- changes permission status only for the bounded subject;
- does not prove execution or durable mutation;
- may become stale when the proposal, evidence or relevant state changes.

Owed closure:

- recorded approval, denial, condition, revocation or unresolved
  decision;
- sufficient binding to the proposal scope/version to prevent
  substitution.

Authorization is not equivalent to generic consent, capability,
validation or apply.

#### C4. Apply / Effect

Meaning:

- exercise authorized capability to establish an authoritative durable
  transition or external effect.

Responsibility effect:

- the state/effect owner owns validation of current applicability,
  execution and authoritative outcome reporting;
- the caller/current work owner owns integration and owner-facing
  closure.

Authority and state effect:

- this is the relation through which an accepted durable mutation or
  external effect may occur;
- stale, invalid, unauthorized or conflicting requests may be rejected;
- only the authoritative applied outcome establishes that the change
  occurred.

Owed closure:

- applied;
- rejected;
- conflict;
- failed-known-not-done;
- partial effect;
- outcome unknown;
- evidence sufficient for reconciliation and safe continuation.

Apply/effect is not equivalent to proposal, approval, arbitrary write
access or one physical writer service.

### Family D — Closure

#### D1. Return / Result

Meaning:

- settle or checkpoint an invocation, delegation, apply operation or
  another bounded obligation and return responsibility for integration.

Responsibility effect:

- the performer closes its bounded obligation or explicitly identifies
  what remains open;
- the parent/current owner retakes integration responsibility;
- every unresolved obligation names its current next-action owner.

Authority and state effect:

- reports outcome;
- does not make non-authoritative information durable truth;
- may include an authoritative apply receipt when produced by the
  state/effect owner.

Required semantic content:

- achieved, not achieved or checkpoint disposition;
- stop, interruption or failure reason;
- relevant outputs;
- evidence and provenance;
- effect certainty;
- unresolved obligations and their owners;
- continuation disposition.

Exact fields and serialization remain downstream.

Result is not equivalent to the last chat message, raw model output,
artifact alone or trace alone.

### Family E — Continuity

#### E1. Continue

Meaning:

- preserve and rebind legitimate work across interruption, checkpoint,
  carrier change, run change, model change or definition evolution.

Responsibility effect:

- preserves current and pending owners;
- does not silently close open work;
- establishes who owns the next legitimate step after resume.

Authority and state effect:

- preserves accepted decisions and effect status;
- does not re-authorize unrelated actions;
- pending authorization remains bound to its original scope and must be
  revalidated when stale;
- opaque runtime identifiers may assist but cannot be the sole basis.

Required semantic preservation:

- work identity and objective;
- accepted current state or authoritative references;
- completed and open obligations;
- current next-action owners;
- decisions, authority bounds and pending approvals;
- proposed, applied, failed, partial or unknown effect status;
- evidence and provenance;
- procedure/process-definition compatibility information;
- next legitimate action and return route.

Exact continuation entities and schema remain downstream.

Continue is not equivalent to transcript copy, one framework's serialized
run object, task ID, thread cursor or transport reconnection.

## Event, evidence, artifact, result and continuation

These concepts are non-equivalent:

- Event reports an occurrence or status transition.
- Evidence supports, refutes or qualifies a claim and retains provenance.
- Artifact is separately addressable produced output.
- Result settles or checkpoints an obligation and returns integration
  responsibility.
- Continuation preserves enough accepted semantics to resume
  legitimately.

Therefore:

- event is not command or accepted truth;
- evidence is not authorization;
- artifact existence is not proof of completion;
- result is not the last conversational output;
- continuation is not transcript copy or a runtime cursor.

## Cross-cutting ownership and authority invariants

### R1. One primary current owner per open obligation

Every open obligation has exactly one primary current next-action owner.

Parallel child obligations are permitted, each with its own owner.
Their parent obligation has one integration owner.

### R2. Waiting is not ownerless

When work waits for input or decision:

- the containing work owner retains monitoring, escalation,
  continuation and closure responsibility;
- the awaited input or decision is a bounded obligation with a named
  owner.

### R3. No ownership gap during handoff

The predecessor retains ownership until successor acceptance.

Lost, unknown or ambiguous acceptance returns to reconciliation rather
than creating silent abandonment.

### R4. Delegation retains parent accountability

The delegate owns bounded execution.

The delegator retains integration, handling of child failure,
owner-facing closure and outcome accountability unless a separate
accepted handoff explicitly changes that relation.

### R5. One authoritative owner per mutable-state boundary

Many roles may query, derive, propose, validate or observe.

One primary normative state owner establishes each accepted durable
version.

This does not require one global store, process or physical writer.

### R6. Capability does not imply authority

A technically capable role cannot self-grant permission.

Credentials, data access, events or delegated work do not create authority
beyond the bounded relation and applicable policy.

### R7. Human effect authority does not transfer implicitly

Invoke, delegate and handoff do not themselves transfer owner/human
authority.

Bounded permission changes only through explicit decide/authorize
semantics or previously established explicit authority.

### R8. Validation, authorization and apply remain distinguishable

Even when one implementation combines them, conformance must establish:

- what was validated;
- who possessed authority;
- what was actually applied;
- what evidence supports the outcome.

### R9. Every accepted child obligation owes closure

Completion, failure, cancellation, unresolved return or continuation
must return to the parent/current owner.

Silent child disappearance is invalid.

### R10. Result and artifact remain separate

An artifact may be shared directly.

A result relation must still declare whether the obligation closed and
who owns what remains.

### R11. Cancellation request does not prove stop

Only an authoritative settlement establishes whether work stopped,
completed, remained partial or requires compensation.

### R12. Unknown effect outcome blocks blind retry

When an effect may have occurred, the current owner first reconciles with
the authoritative state/effect owner unless retry safety is independently
established.

### R13. Continuation preserves unresolved ownership

A checkpoint omitting pending obligations, authority decisions,
effect certainty or current owners is not sufficient portable
continuation.

### R14. Owner-facing integration remains explicit

Internal delegation must ultimately produce:

- a useful result;
- a bounded owner decision request;
- a clear failure;
- or portable continuation.

Internal state, intake, trace and handback bureaucracy is not evidence of
owner-facing usefulness.

## Shared lifecycle semantics

Lifecycle semantics attach to the primary relationship and its underlying
obligation. They are not a mandatory flat message catalogue.

### Offer and take

At minimum distinguish:

- requested or offered;
- taken or acknowledged;
- refused;
- rejected as invalid or unauthorized;
- not understood;
- input-required;
- authority-required.

Delivery of invoke or handoff does not prove acceptance.

### Active and waiting

At minimum distinguish:

- working;
- progress observed;
- suspended;
- waiting for named input;
- waiting for named decision;
- checkpointed.

A progress event does not change ownership or close the obligation.

### Failure and effect certainty

At minimum distinguish:

1. refusal or rejection before execution;
2. failure-known-not-done;
3. partial outcome or effect;
4. completed effect with lost acknowledgement;
5. outcome unknown;
6. transient/retryable failure;
7. permanent/non-retryable failure;
8. unresolved responsibility or ownership.

Generic failed status is insufficient for effect-safe recovery.

### Cancellation

At minimum distinguish:

- cancellation requested;
- cancellation accepted or in progress;
- effectively cancelled with no effect;
- cancellation refused or no longer possible;
- completed before cancellation;
- effect already applied and requiring recovery or compensation;
- effect outcome unknown.

Cancellation request is neither a terminal result nor rollback.

### Retry

Retry is a new execution attempt under the same logical obligation, not
evidence that the prior attempt did nothing.

Safe retry requires:

- causal linkage to the prior attempt;
- bounded retry policy or decision owner;
- transient/permanent classification;
- effect idempotence, deduplication or authoritative reconciliation;
- preservation of prior evidence;
- no silent expansion of authority.

Blind retry is prohibited while effect outcome remains unknown.

### Recovery

Recovery may mean:

- resume from continuation;
- query or reconcile authoritative state;
- retry a known-safe operation;
- re-plan and delegate an alternative;
- repair incomplete durable state;
- escalate an owner decision;
- propose and authorize a compensating effect;
- close unresolved with an explicit resolution owner.

Compensation is a new governed effect. It does not erase history and
requires its own validation, authority and apply semantics.

### Unresolved ownership

Unresolved ownership is an explicit exception condition, not an accepted
empty state.

A resolution owner must be named for reconciliation, escalation or safe
closure.

## Sparse semantic adjacency

A responsibility role requires direct semantic relationship only with:

- its caller or parent;
- its accepted child or handoff successor;
- authoritative state/effect owners it must query or invoke;
- authority holders from whom it needs a bounded decision;
- evidence/result consumers to whom it owes closure.

All-to-all communication is not required.

Sparse adjacency concerns logical responsibility and authority flow, not
physical topology.

Event or artifact delivery may bypass a parent for data movement, but the
integration owner must still receive enough semantic result and
provenance to close the parent obligation.

## End-to-end stress test

The following labels are temporary responsibility roles for testing and
are not accepted service zones or deployment blocks:

- H: human authority owner;
- W: current owner-facing work owner;
- P: procedure responsibility;
- S: authoritative state/source responsibility;
- D: bounded delegated performer;
- V: validation responsibility;
- A: authoritative apply/effect responsibility.

One implementation may combine several roles. Another may distribute one
role.

### Normal path

1. H invokes W with an owner goal.
   W accepts the bounded work and becomes current work owner.

2. W invokes P for an applicable bounded procedure.
   P accepts procedure execution while W retains owner-facing
   integration.

3. P queries S for relevant accepted state and source material.
   S returns scoped observations and provenance. No mutation occurs.

4. P delegates a bounded evidence or execution subtask to D.
   D owns child execution; P remains parent integrator.

5. D returns evidence and result to P.
   Persistent artifacts may be referenced directly, but P determines
   whether the child obligation is sufficiently resolved.

6. P proposes a durable change or external effect.
   No durable state changes.

7. V validates the exact proposal against current state, policy,
   preconditions and evidence.
   Validation is not authorization or apply.

8. W presents H with a bounded decision.
   H authorizes, denies or conditions the exact proposal.

9. W invokes A with the validated and authorized proposal.
   A rechecks current applicability and applies or returns an explicit
   non-success disposition.

10. A returns authoritative apply result and evidence.
    A may emit an event, but the event does not replace the authoritative
    effect outcome.

11. W integrates procedure, evidence, decision and effect outcomes and
    returns H a useful result.

12. W produces portable continuation preserving accepted state, effect
    status, open obligations, current owners and next legitimate action.

### Sparse-connectivity verdict

Required logical relations are:

- H with W;
- W with P and A;
- P with S, D and V;
- D returns to P;
- A owns authoritative effect outcome.

S, D, V and A need not communicate with every other role.

W is a per-obligation ownership role, not a frozen physical central
orchestrator. Its active ownership may move through handoff.

### Child timeout branch

- timeout does not prove D performed nothing;
- P retains parent accountability;
- P may query status, request cancellation, reconcile, safely retry,
  choose an alternative or return unresolved result;
- H does not accidentally become owner of internal recovery.

Verdict: ownership remains coherent.

### Cancellation before apply

- H cancels after proposal but before effect;
- W revokes the pending work/authority as applicable;
- A authoritatively confirms no effect or reports a race/unknown state;
- W returns a cancelled result only after authoritative settlement.

Verdict: proposal or approval is not mistaken for an effect.

### Uncertain apply outcome

- A may have completed the effect while acknowledgement was lost;
- W preserves outcome-unknown;
- W neither reports cancelled nor blindly invokes A again;
- W reconciles with A or authoritative state;
- an applied effect requiring compensation follows a new governed
  propose/validate/authorize/apply path;
- unresolved outcome retains a named resolution owner and continuation.

Verdict: false reporting and duplicate effects are avoided.

### Duplicate apply delivery

- repeated delivery is treated as a new attempt under the same logical
  operation;
- A returns the existing authoritative outcome when retry safety can be
  established;
- otherwise A rejects or requires reconciliation.

Verdict: retry is not permission to repeat an uncertain effect.

### Carrier-switch branch

Work checkpoints after authorization and before apply:

- continuation preserves exact authorization scope, current owner and
  state preconditions;
- the fresh carrier revalidates staleness and compatibility;
- runtime change alone does not require broad re-approval;
- stale or incompatible authorization is not used.

Verdict: semantic legitimacy survives carrier change.

### Stress-test verdict

PASS.

The semantic model supports coherent owner-facing intake through
procedure, effect, result and continuation without all-to-all
communication, a permanent central physical orchestrator or a fixed
service-zone list.

## Rejected alternatives

1. Facets-only grammar as the primary architecture answer.

   Rejected because conformance and interoperability would remain too
   ambiguous without bounded canonical semantic kinds.

   Its useful part is retained: every accepted relationship kind carries
   mandatory ownership, authority, state-effect, closure and lifecycle
   facets.

2. Expanded communicative-act catalogue.

   Rejected because acceptance, progress, failure, cancellation and retry
   would proliferate into packet-like top-level types and obscure the
   underlying open obligation.

3. One generic relation with arbitrary attributes.

   Rejected because critical distinctions could become optional metadata:
   delegation could collapse into handoff, proposal into apply and event
   into command.

4. Message, API call or graph edge as relationship.

   Rejected because these are representation, delivery or implementation
   reachability rather than normative responsibility effects.

5. One service/module/agent for every relationship kind.

   Rejected because it violates Q2 and prematurely freezes physical
   decomposition.

6. Permanent central manager.

   Rejected because a bounded obligation requires a current integration
   owner, not one universal physical orchestrator.

7. All-to-all service-zone communication.

   Rejected because end-to-end coherence requires connected
   responsibility and authority chains rather than a complete physical
   graph.

8. Delegation as complete transfer of accountability.

   Rejected because the parent retains integration and owner-facing
   closure.

9. Handoff as message routing.

   Rejected because handoff changes current next-action ownership only
   after accepted transfer.

10. Query, proposal, validation, authorization and apply as one write act.

    Rejected because it hides authority, stale decisions and unvalidated
    mutation.

11. Cancellation request as immediate stop or rollback.

    Rejected because request and authoritative outcome are different.

12. Artifact or final model output as complete result.

    Rejected because result must settle ownership and identify unresolved
    work.

13. Runtime task/thread/conversation ID as portable continuation.

    Rejected because runtime identity alone does not preserve enough
    semantic state, authority, ownership or evidence.

## Evidence confidence and limits

Strong cross-source convergence supports:

- semantic meaning separate from transport;
- request separate from execution and result;
- query/read separate from mutation;
- proposal separate from accepted/applied change;
- event separate from command;
- delegation retaining parent/accountability relation;
- cancellation request separate from effective cancellation;
- timeout not proving absence of effect;
- artifact/status separate from result;
- sparse responsibility flow.

The following are Q3 architecture synthesis rather than one universal
external standard:

- exactly five relationship families;
- exactly twelve primary kinds;
- one primary current next-action owner as a universal invariant;
- successor acceptance as the ownership-transfer point for handoff;
- lifecycle semantics attached primarily to obligations rather than
  expanded into independent relation families.

Sources do not settle:

- exact entity model;
- exact identity and correlation semantics;
- handoff acknowledgement mechanism or transfer atomicity;
- exact continuation minimum;
- shared-state conflict resolution;
- compensation policy for every effect class;
- physical writer topology;
- final service-zone list.

Protocol completeness does not prove owner-facing live usefulness.

The sparse-flow verdict is a semantic stress test, not a performance or
distributed-systems proof.

## Spawned and downstream questions

### Inline minimal definitions accepted here

- semantic relationship;
- open obligation;
- current next-action owner;
- integration/accountability owner;
- authoritative state owner;
- human authority owner;
- result;
- continuation;
- compensation.

### Existing downstream routes

- Q4: process-pack declarations, inheritance and instantiation;
- Q6: exact state/history ownership and conflict model;
- Q7: target selection for invoke, delegate and handoff;
- Q8: owner-facing progress, decisions, interruption and correction;
- Q9: exact semantic minimum for result and portable continuation;
- Q10: effect classes, authority policy and gate criteria;
- Q11: compatibility and recovery across definition evolution;
- Q12: entities, identity, correlation, representation and communication
  protocol;
- Q13: conformance scenarios for ownership, cancellation, retry, unknown
  outcome and cross-carrier continuation;
- Q14: mapping semantics to Markdown, chat, applications and transports.

### Child questions

1. How are logical obligation, durable work item, invocation and
   execution attempt related?
2. How is successor acceptance established and ambiguous handoff resolved
   without freezing transport?
3. What semantic operation identity is sufficient for retry
   reconciliation and deduplication?
4. How does normative state ownership work with several physical writers
   or replicas?
5. Which effect classes require compensation and which support genuine
   reversal?
6. How does continuation establish compatibility with changed procedure
   or process-pack definitions?

None is a hidden prerequisite for this card.

## Graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed
return_to_cartography: not_required
implementation_activation: prohibited

Next graph route:

- Q4 process-pack instantiation/adaptation;
- first run bounded best-practice/comparable-system research;
- then forge one Q4 architecture card.

## Not frozen

This card does not freeze:

- final service-zone or service-block list;
- physical module, process, service or agent boundaries;
- entity or message schemas;
- identifiers or correlation fields;
- packet formats;
- APIs or tool contracts;
- queue, event bus or publish-subscribe topology;
- scheduler;
- graph runtime;
- orchestration topology;
- permanent central manager;
- physical writer;
- transport or delivery guarantee;
- repository, backend or storage engine;
- framework, provider or model;
- exact lifecycle enum;
- exact continuation serialization;
- concrete process packs;
- UI or owner-facing templates.

## Gate

status: PASS

Checks:

- Q1 and Q2 are unchanged.
- Semantic relationship is separate from message, API, transport,
  graph edge and topology.
- Taxonomy is bounded without becoming a message schema.
- Invoke, delegation and handoff have distinct ownership effects.
- Query, proposal, validation, authorization, apply and event remain
  distinguishable.
- Event, evidence, artifact, result and continuation remain
  distinguishable.
- Every open obligation retains one primary current owner.
- Waiting and pending handoff do not become ownerless.
- State ownership and human authority do not transfer implicitly.
- Refusal, input-required, known-not-done, partial effect, unknown
  outcome, cancellation, retry, recovery and compensation are covered.
- Unknown effect blocks blind retry.
- Result and continuation are specified without exact schema.
- Sparse end-to-end flow passes without all-to-all communication or a
  physical central orchestrator.
- No implementation, transport, carrier, topology or final service-block
  list is selected.
- Evidence limits and downstream questions are recorded.
- No gap event is required.

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
