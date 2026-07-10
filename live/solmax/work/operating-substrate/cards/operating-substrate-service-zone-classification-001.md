# Operating-substrate architecture card — service-zone and responsibility classification

status: accepted
accepted_at: 2026-07-10
session: s-solmax-operating-substrate-service-zone-classification-architecture-forge-001
call: c-solmax-operating-substrate-service-zone-classification-architecture-forge-001
card_id: operating-substrate-service-zone-classification-001
graph_nodes:
  - q02_service_zone_rule

## Owner approval

diverge_choice: |
  "A"

freeze_words: |
  "Approve v1"

## Question

Какие service zones могут быть reusable structure, и по какому
правилу candidate responsibility becomes substrate-level?

## Frozen answer

### Service zone

Service zone is an architectural analysis boundary: a family of
semantically related responsibilities around a recurring process
concern.

A service zone is not automatically a module, deployable service,
agent, process, file, repository or runtime entity.

It may be centralized, distributed, cross-cutting, embedded in several
components or implemented by several adapters.

One physical component may implement responsibilities from several
zones. One zone may be implemented by several components.

Therefore there is no required one-to-one relationship between
semantic service zones and implementation blocks.

### Unit of classification

The unit of classification is an atomic responsibility claim, not a
whole concern such as persistence, routing, interface or safety.

An atomic responsibility claim states:

- the semantic obligation;
- its required outcome or guarantee;
- its legitimate variation owner;
- its authority and effect boundary;
- its failure and recovery meaning;
- how it can be refuted without depending on one provider, carrier or
  implementation.

If one claim mixes a universal guarantee, local policy and concrete
technology, it must be split before classification.

Each atomic claim has one primary normative owner. Dependencies between
layers are recorded separately and do not create double ownership.

### Architecture classes

1. Invariant kernel semantics

   A semantic guarantee required for every compliant process,
   independent of domain, process pack, owner-specific content, model,
   provider, carrier and implementation.

   A process pack cannot override or disable it.

2. Reusable service semantics

   Repeated cross-process behavior with a stable abstract contract and
   stable failure/recovery meanings.

   It may be useful to several different processes without being
   mandatory for every process.

   Reusable service semantics does not imply a separate deployable
   service.

3. Process-pack declarations

   Values, rules and policies that legitimately vary by process or
   domain while the kernel supplies declaration, validation and
   invocation semantics.

   Examples may include local procedures, routing policy, domain
   vocabulary, local state shape, evidence criteria, effect policy,
   budgets and interaction rhythm.

4. Owner-profile concerns

   Approved owner-wide preferences, policies and shared context that
   apply across several processes and should not be copied into every
   process pack.

   A process-specific fact or safety rule does not become owner-wide
   merely because the same owner uses the process.

5. Adapter/implementation concerns

   Concrete bindings to a provider, model, tool, runtime, store,
   repository, transport, application, UI, validator, deployment or
   physical topology.

   Implementations realize accepted semantics but do not define their
   architectural meaning.

### Classification operations

Candidate:
an unaccepted concern, provisional service zone or atomic
responsibility claim submitted for evaluation.

Classify:
assign an atomic claim to one primary architecture class or to defer or
reject.

Promote:
accept an atomic claim as shared substrate semantics—either invariant
kernel semantics or reusable service semantics—after all evidence and
conformance gates pass and the owner approves the architecture card.

Defer:
keep a claim open when evidence, decomposition, failure semantics,
substitutability or downstream definitions are insufficient.

Reject:
reject the current formulation when it contradicts Q1, leaks one
consumer/provider/carrier/implementation into architecture, hides
authority or mutation, cannot be independently tested or freezes a
physical block list.

Rejection applies to the formulation. The underlying concern may return
after decomposition.

### Classification rule

For each candidate concern:

1. Split it into atomic responsibility claims.
2. Remove provider, carrier, repository, runtime and topology leakage.
3. Identify who legitimately owns variation:
   - universal guarantee: invariant candidate;
   - optional stable cross-process contract: reusable-service candidate;
   - process/domain variation: process-pack declaration;
   - owner-wide variation: owner-profile concern;
   - concrete realization: adapter/implementation.
4. Apply promotion evidence and conformance gates.
5. Return exactly one primary disposition:
   - PROMOTE: INVARIANT;
   - PROMOTE: REUSABLE SERVICE SEMANTICS;
   - CLASSIFY: PROCESS PACK;
   - CLASSIFY: OWNER PROFILE;
   - CLASSIFY: ADAPTER/IMPLEMENTATION;
   - DEFER;
   - REJECT.

### Invariant promotion criteria

All must hold:

1. The claim is necessary for every compliant process.
2. Its absence breaks an accepted Q1 guarantee such as legitimate
   continuation, authority/effect safety, durable-state integrity,
   bounded work ownership, evidence/recovery or governed evolution.
3. There is no legitimate process-level variation in the guarantee
   itself.
4. The claim survives changes of provider, model, carrier, storage and
   orchestration implementation.
5. A provider- and carrier-neutral conformance scenario can refute it.
6. A process pack cannot safely override it.

### Reusable-service promotion criteria

All must hold:

1. The same semantic problem occurs in materially different processes.
2. The stable contract includes inputs, outcomes, authority,
   failure and recovery meanings.
3. Implementations can be replaced without changing process-pack
   semantics.
4. The kernel remains valid if the service is absent, unnecessary or
   substituted.
5. Reuse prevents repeated serious failure or reconstruction cost.
6. Reuse does not impose unjustified owner-facing bureaucracy.

### Evidence threshold

Promotion requires:

- support from at least two independent primary-source architecture
  approaches;
- evidence from at least two materially different process pressures or
  consumer classes;
- for durability, mutation, external-effect and recovery claims, at
  least one protocol or durable-workflow source in addition to agent
  framework evidence;
- an explicit search for counterexamples.

No numeric score is used.

One hard failure on implementation neutrality, consumer leakage,
owner authority, refutability or no-topology-freeze is enough to stop
promotion.

### Implementation-neutral conformance pressure

Every promoted claim must admit:

- a positive compliance scenario;
- a negative/refutation scenario;
- provider/carrier/implementation substitution;
- failure and recovery behavior;
- authority/effect rejection where applicable;
- a live-use friction check showing that internal structure does not
  force the owner to operate audit bureaucracy instead of receiving a
  useful process result.

This card does not select a test harness, dataset, repository or
implementation.

## Explicit classification

### Portable continuation

Invariant kernel semantics:

Every close or checkpoint must yield a portable semantic continuation
sufficient to begin a legitimate next invocation in another chat, run,
model or carrier without reconstructing the previous conversation from
the owner's memory.

A runtime-local thread, conversation, checkpoint, task or run ID may be
included as an optional validated reference but is not sufficient by
itself.

Reusable service candidate:

Continuation materialization, validation, import/export and compatibility
checking may be reusable service semantics if separately promoted.

Process pack:

The pack declares which local state, evidence, obligations and
procedure-specific information must supplement the universal
continuation obligation.

Adapter/implementation:

Serialization, Markdown, JSON, transport, storage and runtime
identifiers are implementation concerns.

The exact continuation schema and field set remain open.

### Writer/apply validation

Invariant kernel semantics:

A reasoning statement or proposed mutation does not become durable truth
merely because it was produced.

Durable mutation must cross a logical boundary that provides:

- explicit proposed change or effect;
- validation of applicable preconditions and policy;
- authorization and owner approval where required;
- controlled application;
- recorded outcome and evidence;
- explicit failure and recovery behavior.

These are semantic obligations, not required packet fields or required
physical stages.

Reusable service candidates:

Validation, policy evaluation, approval coordination and apply
coordination may become reusable service semantics.

Process pack:

The pack owns domain effect policy, local validation rules, local
evidence thresholds, preconditions, escalation and compensation policy.

Owner profile:

Owner-wide approval, privacy or sharing defaults may live here when
genuinely shared across processes.

Adapter/implementation:

A separate writer chat, writer agent, repository commit, database
transaction, event-mediated workflow or application service are
alternative implementations.

No physical writer topology is frozen.

### Persistence

Persistence is not accepted as one universal service block.

Its responsibilities classify separately:

- invariant: controlled durable mutation, provenance and explicit
  separation of accepted state, history, memory, sources, artifacts and
  evidence;
- reusable-service candidates: persistence, checkpoint materialization,
  audit/history maintenance and recovery coordination;
- process pack: local state shape, retention, promotion-to-state and
  domain recovery rules;
- owner profile: genuinely owner-wide privacy, sharing or retention
  defaults;
- adapter: files, Git repository, database, event store or another
  storage mechanism.

### Live interface

Live interface is not accepted as one universal UI service.

Its responsibilities classify separately:

- invariant: an authorized human route for consent, correction,
  decision, approval/rejection, interruption/cancellation and visibility
  of proposed effects; useful operation must not require reading
  internal audit machinery;
- reusable-service candidates: decision, approval, notification or
  continuation mediation;
- process pack: local interaction rhythm, domain language, intake and
  result expectations;
- owner profile: language, presentation, explanation and
  ask/proceed/initiative preferences;
- adapter: chat, voice, web application, notifications or another UI.

### Domain-specific safety policy

Concrete domain safety policy is not invariant kernel semantics.

Its responsibilities classify separately:

- invariant: capability is not permission or authorization; a
  high-impact effect crosses an explicit authority and validation path;
- reusable-service candidates: policy evaluation, approval coordination
  and evidence collection;
- process pack: medical, legal, financial, product, security or other
  domain-specific safety policy, local effect classes, escalation and
  refusal rules;
- owner profile: owner-wide approval and privacy defaults, not domain
  expertise or process-local safety rules;
- adapter: credentials, concrete enforcement, tool permissions, receipts
  and effect execution.

## Rejected alternatives

1. Give one class to a whole service zone.
   Rejected because most concerns mix universal semantics, local policy
   and implementation.

2. Promote every repeated concern to kernel invariant.
   Rejected because recurrence does not prove universal necessity.

3. Treat every optional concern as consumer-specific.
   Rejected because optional concerns may still have reusable
   cross-process semantics.

4. Equate service zone with deployable service, module or agent.
   Rejected because it prematurely freezes physical topology.

5. Accept persistence, history, routing, procedures, context, results,
   gates and communication as a canonical block list.
   Rejected because this is an evaluation set, not accepted
   decomposition.

6. Use a numeric architecture score.
   Rejected because critical failures must not be compensated by weak
   positive signals.

7. Promote framework classes or runtime identifiers into substrate
   entities.
   Rejected because they are implementation-specific.

8. Require a separate writer agent or writer chat.
   Rejected because only the logical validated apply boundary is
   invariant.

9. Treat artifact completeness as proof of live process usefulness.
   Rejected because complete internal surfaces can still produce a
   failed owner-facing process.

## Child and downstream questions

Inline minimal definition:

- atomic responsibility claim is defined semantically in this card;
  no exact template or schema is frozen.

Existing child question:

- exact entity relationships among task, work item, run, invocation,
  chat, session, procedure, checkpoint and continuation.

Downstream:

- Q3: responsibility and service-zone relationship model;
- Q4: process-pack declarations and instantiation;
- Q5: owner-profile boundary;
- Q6-Q12: persistence, routing, live interface, handback, authority,
  evolution and communication cards;
- portable-continuation semantic minimum and compatibility contract;
- mutation/writer validation and evidence contract;
- Q13: proof and evaluation;
- Q14: carrier boundary.

## Graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed

The rule classifies portable continuation, writer/apply, persistence,
live interface and domain-specific safety policy without contradiction
and without choosing an implementation or final block list.

## Not frozen

This card does not freeze:

- a final service-zone or service-block list;
- physical module or service boundaries;
- entity or message schemas;
- continuation fields or serialization;
- writer topology;
- API, framework, provider or model;
- repository, backend, storage or transport;
- application or deployment architecture;
- concrete process packs;
- concrete owner-profile content;
- detailed proof harness.

## Gate

status: PASS

Q1 remains unchanged.

Portable continuation is classified as semantic obligation while its
exact schema remains open.

Writer/apply is classified as a logical validated boundary while its
physical topology remains open.

Persistence, live interface and domain-specific safety policy classify
without contradiction.

No implementation, consumer policy, final service-block list or
Direction OS change is selected.

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
