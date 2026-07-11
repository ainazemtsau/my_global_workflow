# Operating-substrate architecture card — persistence and history

status: accepted
accepted_at: 2026-07-11
session: s-solmax-operating-substrate-persistence-history-architecture-forge-001
call: c-solmax-operating-substrate-persistence-history-architecture-forge-001
card_id: operating-substrate-persistence-history-001
graph_nodes:
  - q06_persistence_history

## Owner approval

diverge_choice_words: |
  "беру твою рекумендацию"

selected_direction: |
  Direction C — responsibility-separated continuity with an
  authoritative-state anchor — is the architecture backbone.

  Direction A contributes mandatory internal constraints:
  - one primary normative owner for each accepted durable-state version;
  - minimum proportional universal persistence burden;
  - no exhaustive universal history or audit requirement;
  - no owner-facing persistence bureaucracy.

  Direction B — transition/history-derived continuity — is rejected as
  the universal backbone. Event/history-derived persistence remains a
  possible conforming implementation family.

freeze_words: |
  "Approve v1"

## Question

Какие persistence/history responsibilities являются substrate-level,
а какие остаются consumer-specific?

## Preserved parent locks

This card does not revise Q1, Q2, Q3, Q4 or Q5.

The following accepted positions remain unchanged:

1. Operating-substrate is a stable, model-neutral and carrier-neutral
   kernel with pluggable process packs.

2. Service zones are semantic responsibility families, not physical
   services, repositories, stores, agents, files or deployment blocks.

3. Atomic responsibility claims have one primary normative owner.

4. One primary normative state owner establishes each accepted durable
   version inside a bounded mutable-state boundary.

5. Query, evidence, propose, validate, decide/authorize, apply/effect,
   return/result and continue remain semantically distinguishable.

6. A result, event, observation, artifact, evidence item, audit record,
   timestamp or transcript statement does not automatically establish
   accepted durable truth.

7. Durable mutation crosses a logical validated apply boundary.

8. Only an authoritative apply outcome establishes whether an accepted
   durable mutation or external effect occurred.

9. Unknown external-effect outcome blocks blind retry.

10. Portable continuation preserves legitimate resume semantics rather
    than relying only on a transcript or opaque runtime cursor.

11. Process-pack instantiation uses staged semantic admission and
    activation.

12. Owner-wide sharing eligibility, process-local accepted truth,
    permission to use and action authority remain separate conclusions.

13. Correction, dispute, restriction, revocation and retirement are
    non-equivalent.

14. Pinning may preserve interpretation and evidence but cannot preserve
    revoked permission, use permission or action authority.

15. No final service-block list, persistence representation, schema,
    repository, carrier, provider, topology or implementation has been
    accepted.

## Frozen answer

Durable continuity is a responsibility-separated semantic capability
through which interrupted, changed or long-lived work can determine:

- which accepted state currently governs;
- who may establish a successor accepted state;
- what definitely happened;
- what may have happened;
- which obligations remain open;
- who owns the next resolution step;
- which authority remains applicable;
- which definition/version can interpret the work;
- which evidence and provenance remain relevant;
- which next action is legitimate.

Durable continuity is anchored in authoritative accepted state.

For each mutable-state boundary, one primary normative state owner
establishes each accepted durable version through the validated apply
semantics inherited from Q1-Q5.

Accepted current state, transition/history, audit, evidence, provenance,
source, memory, artifact, process-definition/version,
checkpoint/recovery and retention/status remain distinct semantic
responsibility classes even when one physical representation implements
several of them.

The kernel freezes the minimum guarantees required for legitimate
continuity.

Process packs own domain-, purpose- and consequence-specific persistence,
history, evidence, recovery and retention policy.

Reusable services may supply stable semantic capabilities without
acquiring state, authority, evidence-sufficiency or retention ownership.

Adapters and implementations choose materialization.

This card does not select mutable-current-state storage, event sourcing,
append-only history, deterministic replay, snapshots, files, Git,
databases or a physical hybrid as the universal answer.

## Semantic concern classes

These are responsibility distinctions, not mandatory entities, records,
fields, tables, files or service blocks.

### 1. Accepted current state

The normative durable conclusion used as the current basis for
subsequent legitimate reads, validation, decisions and actions inside a
named mutable-state boundary.

It is established by that boundary's primary normative state owner
through authoritative apply.

It is not automatically:

- the last message;
- the newest timestamp;
- the newest event;
- a transcript summary;
- a model inference;
- a restored checkpoint;
- an artifact;
- an audit record;
- an arbitrary writer's output.

Accepted current state may be directly materialized or derived by an
implementation. Its normative meaning and ownership do not depend on
that representation.

### 2. Transition or history material

Durable material describing an occurrence, attempted transition,
authoritative transition, status change or relation between versions.

It may include rejected, cancelled, failed, partial or uncertain attempts
where those are relevant.

It is not automatically:

- accepted current state;
- sufficient evidence;
- audit material;
- proof that an external effect occurred;
- authorization to repeat the transition;
- a command.

Observation order, arrival order and timestamp order do not establish
normative state precedence.

### 3. Audit

Purpose-bound durable accountability material supporting review of:

- what was proposed, attempted, decided or applied;
- by whom or under which responsibility;
- under which authority and process definition;
- against which policy or preconditions;
- with which reported outcome and known gaps.

Audit has a declared purpose, coverage, access boundary and retention
responsibility.

It is not automatically:

- complete domain history;
- current state;
- all debug logs or model traces;
- a complete evidence ledger;
- proof that an observed claim is true.

### 4. Evidence

Material supporting, refuting or qualifying a claim, proposal,
validation conclusion, transition, effect outcome or result.

The evidence producer owns the accuracy of its stated origin, scope,
derivation and known limitations.

The legitimate evaluator or authority owner owns the conclusion that
evidence is sufficient for a consuming obligation.

Evidence is not automatically:

- accepted truth;
- provenance;
- authorization;
- audit;
- result;
- correct merely because it is an artifact.

### 5. Provenance

Lineage concerning origin, generation, use, derivation, revision,
invalidation, responsible actors or activities and relationships among
materials.

Provenance supports evaluation and interpretation.

It does not automatically establish:

- truth;
- permission;
- evidence sufficiency;
- state authority;
- complete audit.

### 6. Source

An originating material, system, actor, observation or assertion from
which a claim, artifact, evidence item or derived material is obtained.

Source identity, availability, authenticity, claim truth, fitness for
purpose and permission to use remain separate conclusions.

Source disappearance does not prove that the source was false and does
not promote a derived summary into authoritative truth.

### 7. Memory

Retrievable material intended to aid future reasoning, recall,
personalization or continuity.

Memory may be copied or derived from interactions, sources, state or
history.

It is not automatically:

- accepted process state;
- owner-wide truth;
- source;
- evidence;
- checkpoint;
- complete transcript archive.

Derived memory retains provenance, derivation and uncertainty and cannot
launder inference into accepted fact.

### 8. Artifact

A separately addressable produced output such as a document, dataset,
media item, code output or other deliverable.

An artifact may be result material, evidence, a source for later work or
a proposal awaiting acceptance.

Artifact existence does not automatically prove:

- correctness;
- completion;
- accepted durable mutation;
- currentness;
- authorization for use.

### 9. Process-definition and version material

Accepted semantics, rules, obligations, compatibility expectations and
authority boundaries governing a process or active obligation.

This material provides the interpretive basis needed to understand why
historical state, decisions, results and transitions had their meaning
at the relevant time.

It is distinct from:

- runtime state;
- source-package availability;
- one code commit identifier;
- current pack activation;
- storage-schema version.

### 10. Checkpoint and recovery material

A bounded durable basis from which legitimate work may be resumed,
reconciled, restored or branched after interruption.

It may contain or reference:

- accepted state;
- completed and open obligations;
- current owners;
- decisions and authority;
- effect certainty;
- definition compatibility;
- evidence and provenance;
- the next legitimate action.

It is not automatically:

- complete history;
- accepted current truth at resume time;
- proof that no later effect occurred;
- renewed authorization;
- a safe instruction to replay all later actions;
- long-term memory.

### 11. Retention and status

Governed conclusions concerning continued availability, permitted use,
restriction, currentness, correction, dispute, suspension, revocation,
retirement, expiration, disposition or erasure.

Important non-equivalences include:

- unavailable is not false;
- restricted is not erased;
- revoked is not historically nonexistent;
- retired is not necessarily deleted;
- corrected is not silently overwritten;
- disputed is not resolved;
- expired is not necessarily uninterpretable historically;
- retained is not necessarily permitted for every future purpose.

Exact status names and lifecycle enums remain downstream.

## Invariant kernel semantics

### K1. Semantic non-collapse

Accepted state, transition/history, audit, evidence, provenance, source,
memory, artifact, definition/version, checkpoint/recovery and
retention/status remain distinguishable.

A physical representation may implement several responsibilities.
Conformance still establishes their normative meanings independently.

### K2. Authoritative accepted-state ownership

Each mutable-state boundary has one primary normative state owner that
establishes every accepted durable version.

Other roles may query, observe, propose, validate, derive, checkpoint,
audit, store or replicate material.

Data possession, technical write capability, event production or
timestamp recency does not make those roles normative state owners.

### K3. Validated durable mutation

Durable mutation occurs only through the accepted semantic distinctions:

1. propose a bounded candidate change;
2. validate it against current state, invariants, policy and evidence;
3. obtain applicable bounded authority where required;
4. apply through the authoritative state/effect owner;
5. return an authoritative outcome and evidence.

Proposal does not mutate state.

Validation does not grant authority.

Authorization does not prove apply.

Result narrative, artifact existence, history append and event emission
do not independently establish the transition.

### K4. Minimum accepted-version lineage

For each accepted durable version, it must be semantically determinable:

1. which prior accepted basis governed, or that no prior basis existed;
2. which proposed transition, correction or migration was considered;
3. which validation conclusion and applicable authority supported it;
4. which authoritative apply outcome established the version;
5. which material evidence and provenance are relevant;
6. which process definition/version governed the transition;
7. how the version relates to superseded, corrected, disputed or
   migrated material;
8. which active obligations require compatible resume, revalidation,
   migration, pin/drain, handoff, block or named unresolved treatment.

These are semantic requirements, not mandatory fields or records.

### K5. No silent overwrite

Correction, migration, conflict resolution or replacement must not make
it impossible to explain which prior accepted version governed earlier
work.

This does not require permanent retention of every prior byte or
append-only physical storage.

It requires that legitimate history, active dependencies, accepted
decisions, effect certainty and historical interpretation are not
silently falsified.

### K6. Effect-certainty preservation

Interruption, timeout, cancellation, checkpoint and carrier change
preserve distinctions among:

- known not done;
- authoritatively applied;
- partial effect;
- outcome unknown;
- later reconciled;
- mitigated through a separately governed compensating effect.

These are semantic distinctions, not a frozen status enum.

### K7. Recovery-action non-equivalence

Resume, retry, replay, restore, fork, reconcile and compensate have
different semantic effects.

They must not collapse into one generic recovery command.

Recovery cannot expand authority, erase evidence or infer that an
uncertain prior effect did not occur.

### K8. Legitimate portable continuation

Portable continuation preserves enough accepted semantics to determine:

- the current accepted basis or authoritative reference;
- completed and unresolved obligations;
- current next-action owners;
- relevant decisions and authority;
- effect certainty;
- evidence and provenance needed for continuation;
- governing definition/version and compatibility;
- next legitimate action and return route.

Continuation is not required to contain every transcript, event,
artifact or audit item.

### K9. Historical-definition interpretability

Accepted state, decisions, results, evidence and transitions remain
interpretable under the process definition/version that governed them.

A successor definition may require migration or revalidation.

It must not silently reinterpret historical material as though the
successor semantics had always governed.

Source disappearance, deprecation or runtime replacement must not
silently make accepted historical meaning opaque.

### K10. Lifecycle-status non-equivalence

Correction, dispute, restriction, suspension, revocation, retirement,
expiration, erasure and source unavailability remain distinct governed
conclusions where applicable.

Their exact representation remains downstream.

### K11. Explicit retention/disposition responsibility

Durable material has a legitimate normative owner responsible for
deciding continued retention, restricted use, archival treatment or
disposition inside the applicable scope.

The kernel does not define:

- universal retention purposes;
- one legal basis;
- one TTL;
- one deletion mechanism;
- one retention hierarchy for every process.

### K12. Active-work impact propagation

When relevant accepted state, source, definition, authority or
retention/status changes, affected open obligations receive an explicit
disposition:

- compatible resume;
- revalidation or migration;
- pin and drain;
- accepted handoff;
- block or rejection;
- unresolved with a named current owner.

New material does not silently rewrite active work.

### K13. External-reference failure is explicit

A continuation or historical record depending on external material must
preserve enough semantics to detect:

- inaccessible;
- missing;
- superseded;
- incompatible;
- unauthorized;
- invalidated references.

Missing authoritative material cannot silently be replaced by a stale
summary or model inference.

### K14. Proportional owner-facing visibility

Persistence conformance must not require the owner to operate raw event
streams, audit logs, checkpoint objects or lineage graphs.

The owner-facing process must expose useful consequences:

- what became accepted;
- what changed;
- what remains uncertain;
- which effect occurred or may have occurred;
- which correction or decision is required;
- what blocks the next step.

Deeper history and lineage remain inspectable when needed.

Internal surface completeness is not proof of owner-facing usefulness.

## Responsibility classification

### Invariant kernel semantics

K1-K14 are accepted invariant kernel semantics:

- semantic non-collapse;
- authoritative accepted-state ownership;
- validated durable mutation;
- minimum accepted-version lineage;
- no silent overwrite;
- effect-certainty preservation;
- recovery-action non-equivalence;
- legitimate portable continuation;
- historical-definition interpretability;
- lifecycle-status non-equivalence;
- explicit retention/disposition responsibility;
- active-work impact propagation;
- explicit external-reference failure;
- proportional owner-facing visibility.

### Reusable-service candidates

The following are semantic capability candidates, not an accepted final
service catalogue or physical decomposition:

1. Accepted-state read and controlled-apply support.
2. Transition/history capture and query.
3. Provenance and lineage maintenance.
4. Evidence integrity, reference and retrieval.
5. Audit capture, review and export under bounded policy.
6. Source-reference integrity and availability observation.
7. Checkpoint creation, validation, import and restore support.
8. Recovery and authoritative reconciliation coordination.
9. Definition/version lineage and compatibility evaluation.
10. Migration, pin/drain and historical-interpretation support.
11. Retention, restriction, disposition and status propagation.
12. Correction, dispute, revocation and retirement propagation.

A realization may combine several candidates in one component,
distribute one candidate across components, omit optional candidates or
bind consumer-native implementations through adapters.

Providing capability does not give the reusable service normative
ownership of:

- accepted state;
- evidence sufficiency;
- human authority;
- domain policy;
- retention decisions.

### Process-pack declarations

Process packs own domain-, purpose- and consequence-specific declarations
such as:

1. Which domain conclusions may become accepted process state.
2. Mutable-state boundaries and their normative owners.
3. Valid transition and correction conditions.
4. Required causal and historical material by consequence class.
5. Which occurrences require audit treatment and for which purpose.
6. Evidence sufficiency and source-currentness rules.
7. Which operations are retry-safe, replay-safe, idempotent,
   reconcilable, compensatable or unsafe to repeat.
8. Checkpoint sufficiency, creation triggers and acceptable recovery
   loss at the semantic level.
9. Forking, alternative-branch and canonical-promotion behavior.
10. Definition/version compatibility and migration obligations.
11. Pin/drain, deprecation, replacement and removal conditions.
12. Correction, dispute, restriction, revocation and retirement effects.
13. Retention purposes, minimization and mandatory historical evidence.
14. Source capture versus durable-reference requirements.
15. Owner-facing history, correction and audit presentation.
16. Domain escalation where privacy, safety, evidence, legal,
    accountability or recovery obligations conflict.

This card does not define actual Health, game, Zaratusta or Direction OS
declarations.

### Owner-profile concerns

Genuinely owner-wide concerns may include:

- approved privacy and sharing preferences;
- preferred audit/history visibility and notification level;
- owner-wide correction and dispute preferences;
- approved retention-minimization preferences;
- destructive-action confirmation preferences;
- preferred balance between concise summaries and inspectable detail.

Owner-profile concerns do not:

- establish process-local truth;
- override mandatory process safety, evidence, legal or retention policy;
- authorize a concrete external effect;
- make all process history owner-wide;
- permit raw secrets or sensitive material in continuations;
- turn a personal preference into a kernel invariant.

### Adapter and implementation concerns

The following remain downstream HOW decisions:

- mutable records, append-only histories, event stores, snapshots or
  physical hybrids;
- databases, filesystems, Git repositories, object stores, vector stores,
  knowledge graphs or other backends;
- event, state, audit, evidence, provenance, checkpoint and retention
  schemas;
- fields, identifiers, version syntax, timestamps and correlation
  formats;
- serialization, compression, compaction and garbage collection;
- replication, backup, encryption and access-control mechanisms;
- indexing, search and query optimization;
- snapshot cadence and physical consistency;
- replay engines and deterministic-execution mechanisms;
- idempotency-key representation and deduplication technology;
- tombstones, deletion, redaction and erasure mechanics;
- provider-specific migration and rollback mechanisms;
- runtime, framework, model, transport, deployment and topology.

## Normative durable-responsibility roles

These roles describe semantic responsibility. They do not prescribe
physical components.

### Accepted-state owner

Owns:

- current normative durable version for its mutable boundary;
- current-state precondition validation at apply;
- authoritative settlement of whether mutation occurred;
- stale or conflicting transition rejection.

Does not automatically own all sources, evidence, audit collection,
process integration or owner-wide policy.

### History responsibility

Owns:

- completeness and integrity of the history it claims to maintain;
- attribution of observed or accepted transitions to reported causes;
- explicit gaps and uncertainty.

Does not own current state truth or authority to apply.

### Audit responsibility

Owns:

- declared audit purpose and coverage;
- integrity and access expectations;
- disclosure of known audit gaps;
- routing of required accountability review.

Does not own domain state, every debug trace or owner-facing
presentation.

### Evidence producer and evaluator

The producer owns stated origin, scope, derivation and limitations.

The evaluator or applicable authority owns evidence-sufficiency
conclusions for the consuming claim, decision or transition.

### Provenance responsibility

Owns the accuracy of asserted lineage relations and explicit loss of
lineage.

It does not prove content truth.

### Checkpoint responsibility

Owns what a checkpoint claims to preserve, reference integrity,
compatibility information and known omissions.

It does not decide unilaterally that restore or replay is safe.

### Recovery owner

Owns resolution of interrupted or uncertain obligations, selection or
routing of legitimate recovery action, reconciliation before unsafe
repetition and explicit unresolved closure.

Recovery ownership does not transfer state or human authority.

### Definition/version owner

Owns accepted definition identity, lineage, compatibility claims,
deprecation/removal criteria and historical interpretability
expectations.

It does not automatically migrate consumer state or authorize changed
effects.

### Retention/disposition owner

Owns applicable retention, restriction or disposition conclusions,
legitimate purpose and minimization, required propagation and escalation
of conflicts inside its normative scope.

The adapter executing deletion or restriction does not invent policy.

## Mutation, lineage and lifecycle changes

### Normal accepted mutation

A semantically complete transition follows the inherited distinctions:

1. A current owner or procedure forms a candidate change.
2. Relevant accepted state and sources are queried.
3. Evidence and provenance are assembled.
4. The proposal is validated against current preconditions and policy.
5. Required bounded authority decides the exact proposal.
6. The authoritative state/effect owner performs apply.
7. The authoritative outcome establishes applied, rejected, conflicting,
   partial, known-not-done or outcome-unknown treatment.
8. Applicable history, provenance, evidence and audit responsibilities
   record or reference the transition.
9. Result integrates the outcome.
10. Continuation preserves unresolved work and the next legitimate
    action.

One implementation may physically combine several responsibilities.
Conformance must still prove their semantic effects.

### Correction

Correction:

- enters as a proposed new conclusion;
- is validated and applied by the relevant normative state owner;
- establishes a successor accepted version when justified;
- preserves a semantic relation to the corrected material;
- triggers revalidation of affected active work;
- makes prior material non-current;
- subjects prior material to separate retention, restriction or
  disposition policy;
- prevents derived memories and summaries from continuing to represent
  the old material as accepted truth.

Correction is not an in-place edit that makes earlier use impossible to
explain.

### Dispute

Dispute:

- preserves competing claims and provenance;
- is not resolved through newest timestamp or last-write-wins;
- gives active work an explicit use, revalidation, provisional/degraded,
  block or escalation disposition;
- names a current resolution owner where unresolved;
- may exist without immediate replacement accepted state.

### Revocation

Revocation:

- changes future permission, reliance, sharing, status or authority for
  a bounded subject;
- causes active dependants and pending authority to be revalidated;
- blocks prohibited future use;
- does not make prior lawful processing or already-applied effects
  historically nonexistent;
- routes any mitigation through a new governed compensation effect.

Revocation is not rollback.

### Retirement

Retirement:

- makes material ineligible for ordinary new use or activation;
- gives active dependants drain, migration, replacement, rejection or
  named-unresolved treatment;
- preserves historical interpretation where legitimately required;
- leaves physical retention and access to applicable policy.

Retirement is not synonymous with deletion.

### Migration

Migration is governed mutation, not silent reinterpretation.

It requires:

- known source and target definitions;
- compatibility or transformation assessment;
- validation against current accepted state and policy;
- applicable authority where consequences change;
- authoritative apply;
- lineage between pre- and post-migration material;
- explicit treatment of lossy, conflicting or untranslatable material;
- disposition for open obligations and continuations.

## Recovery and effect certainty

These are semantic recovery actions, not a mandatory protocol enum.

### Resume

Continue from a preserved legitimate state without intentionally
repeating completed work.

Resume requires:

- accepted state or an authoritative reference;
- compatible definition;
- current owners;
- valid authority;
- known effect status;
- next legitimate action.

### Retry

Start a new execution attempt for the same logical obligation.

Retry is safe only when at least one holds:

- prior outcome is known not done;
- the operation is idempotent or deduplicated;
- authoritative reconciliation establishes repetition is safe;
- an applicable authority explicitly accepts the bounded
  duplicate-effect risk.

Timeout alone is insufficient.

### Replay

Re-execute prior procedural steps from retained history or inputs.

Replay may mean deterministic reconstruction in a constrained runtime or
a new nondeterministic attempt in model-, human- or API-driven work.

Deterministic replay is not assumed universally.

### Restore

Re-establish material from a prior checkpoint or snapshot.

Restore does not prove:

- no later external effect occurred;
- restored definition remains compatible;
- prior authorization remains current;
- restored material is current accepted state.

### Fork

Create a new branch from a prior accepted basis or checkpoint while
preserving the original branch.

Fork is not rollback and does not change canonical accepted state until
a separate governed promotion/apply occurs.

### Reconcile

Query the authoritative state or effect owner to determine what actually
happened and settle uncertainty.

Reconciliation is the preferred first route when an effect may have
occurred and retry safety is not independently proven.

### Compensate

Perform a new governed effect intended to offset or mitigate a prior
effect.

Compensation:

- requires current validation and authority;
- has its own outcome and evidence;
- does not erase the prior effect or history.

### Checkpoint sufficiency

A checkpoint is semantically insufficient when a fresh legitimate
carrier cannot determine:

- whether state is accepted or merely proposed;
- whether an effect may already have happened;
- which authorization remains applicable;
- which obligations remain open;
- who owns the next resolution step;
- which definition can interpret the material;
- whether required sources and evidence remain usable;
- which next action is permitted.

## Result and portable continuation

### Result

A result settles or checkpoints a bounded obligation and returns
integration responsibility.

It may report:

- achieved or not achieved;
- authoritative apply outcome;
- effect certainty;
- outputs and artifacts;
- evidence and provenance;
- unresolved obligations and owners;
- continuation disposition.

Result narrative does not mutate non-authoritative state or make itself
accepted truth.

When a result includes an authoritative apply receipt, state authority
comes from the state/effect owner's outcome, not from the result wrapper.

### Portable continuation

Portable continuation is a semantic recovery contract.

It may carry or reference:

- accepted state;
- relevant history;
- checkpoint material;
- governing definition/version;
- decisions and authority;
- evidence and provenance;
- unresolved obligations;
- effect certainty;
- next legitimate action.

It is not:

- a transcript dump;
- one framework's serialized run;
- complete history or audit;
- a storage snapshot by definition;
- reusable authorization;
- proof that every referenced source remains available.

On resume, a receiving carrier may need to:

- validate integrity;
- resolve references;
- recheck permission and sharing status;
- assess definition compatibility;
- reconcile uncertain effects;
- revalidate stale authority and current-state preconditions.

### Result, continuation and history relation

- Result explains closure or non-closure of the current obligation.
- Continuation preserves legitimate future ownership and action.
- History records relevant occurrences or transitions.
- Audit supports accountability.
- Evidence supports or refutes claims.
- Provenance explains lineage.
- Accepted state remains owned by the normative state owner.

One physical artifact may carry several facets. Their normative meanings
remain separately testable.

This card does not copy Direction OS RESULT fields or define a packet
schema.

## Implementation-neutrality verdict

Four implementation families can conform. None is selected universally.

### Mutable-current-state

Viable when:

- accepted-version lineage is preserved;
- mutation crosses governed apply;
- effect certainty survives interruption;
- pack-required history and audit are retained;
- governing definitions remain interpretable.

A current row or file does not by itself satisfy Q6.

### Event/history-derived

Viable when:

- one normative state owner still accepts the current projection;
- events and observations do not self-authorize;
- nondeterministic and external effects are safely recorded or
  reconciled;
- historical definitions remain interpretable;
- retention and disposition remain governable.

Event sourcing and deterministic replay are not universal substrate
mandates.

### Checkpoint/snapshot

Viable when:

- checkpoint acceptance and integrity are explicit;
- effect certainty is reconciled;
- current authoritative state is revalidated;
- pending ownership and authority are preserved;
- omitted history is legitimate under pack evidence/audit policy.

A checkpoint is not a replacement for all current state, history or
provenance responsibilities.

### Physical hybrid

Viable when:

- each atomic claim retains one normative owner;
- duplicated material does not create duplicated authority;
- discrepancies have a named reconciliation owner;
- retention and correction propagate appropriately;
- owner-facing operation remains useful.

The existence of several semantic concerns does not require one physical
hybrid architecture.

## Definition/version compatibility and historical interpretation

Historical and active material retains enough governing-definition
information to determine:

- which semantics and obligations applied;
- which authority rules applied;
- which evidence requirements applied;
- which state transitions were valid;
- how results and statuses should be interpreted;
- whether current continuation is compatible.

Exact identifiers and version syntax remain downstream.

### Coexistence

Old and new definitions may coexist when:

- applicable obligations are distinguishable;
- every active obligation has an explicit compatibility disposition;
- state owners can interpret the definition governing each mutation;
- authority and privacy remain current;
- required conversions are validated.

### Pin and drain

Pinning may preserve interpretation for active work under an older
definition.

Pinning cannot preserve:

- revoked disclosure or use permission;
- expired action authority;
- a mandatory policy that now blocks use;
- inaccessible mandatory sources;
- unsafe effect assumptions.

Drain completes when remaining obligations are completed, migrated,
handed off, rejected or explicitly closed with a named owner.

### Removal

Definition support may be removed only when:

- no active obligation depends on it without an explicit disposition;
- persisted accepted material remains interpretable;
- required migration is complete;
- required evidence and historical queries have a legitimate route;
- retention and privacy policy permit the remaining interpretive
  material.

### Source disappearance

Accepted historical meaning cannot depend solely on an ephemeral source
that may vanish without a failure route.

Viable implementations may use accepted copies, stable references,
signed artifacts, normalized interpretation or another mechanism.

This card does not select one.

The invariant is:

- accepted historical meaning and current compatibility remain
  determinable;
- otherwise the dependency becomes an explicit blocked or unresolved
  obligation with a current owner.

## Retention, restriction and privacy boundary

There is no universal retention interval.

Retention depends on:

- purpose;
- consequence and safety;
- active obligations;
- evidence and audit requirements;
- privacy and sharing limits;
- applicable domain or legal duties;
- definition interpretability;
- source availability;
- correction and dispute status;
- owner-wide minimization preferences;
- recovery requirements.

Different material may receive different treatment.

Examples, not universal prescriptions:

- current accepted state may remain while an obsolete checkpoint is
  pruned;
- minimal effect evidence may remain after sensitive payload deletion;
- audit may outlive mutable operational state where legitimate;
- source material may be removed while qualified provenance remains;
- disputed material may be retained under restricted access;
- derived memory may be deleted while accepted state remains;
- a retired definition may remain historically interpretable while being
  unavailable for new activation.

Restriction preserves material for bounded purposes while limiting
ordinary use.

Erasure removes applicable material subject to legitimate constraints
and implementation mechanics.

Neither restriction nor erasure automatically:

- undoes external effects;
- resolves a dispute;
- changes historical reality;
- authorizes unrelated retained copies;
- determines every downstream consumer's obligations.

### Propagation

Relevant correction, restriction, revocation, retirement or erasure
conclusions propagate to known active consumers and continuations
through revalidation or another explicit disposition.

Exact propagation mechanisms remain downstream.

### Minimal retained proof

A process may need purpose-bound minimized material proving:

- whether a consequential effect occurred;
- which authority applied;
- why current state is accepted;
- that required correction or disposition occurred;
- which unresolved owner remains.

This is not a reason to retain complete sensitive transcripts or
payloads.

### Status-access privacy

Status and history access can itself reveal:

- which process is active;
- which source or credential is being checked;
- when an owner interacts with a process;
- which correction or dispute exists;
- which sensitive domain is relevant.

Privacy and minimization therefore apply to metadata, indexing, queries
and notifications as well as payload content.

## Pressure tests

### Health-like privacy and safety pressure

Scenario:

- a process previously accepted a sensitive source claim;
- a corrected source arrives;
- some disclosure or use permission is revoked;
- a consequential external action has an uncertain outcome;
- active continuation still refers to prior material.

Required behavior:

1. Correction enters validation rather than overwriting accepted state.
2. The normative state owner applies a corrected accepted version when
   justified.
3. Prior material remains identifiable as prior rather than current,
   subject to legitimate restriction and retention.
4. Derived memories and summaries stop presenting the old claim as
   accepted truth.
5. Open obligations revalidate their dependency.
6. Revoked permission blocks future prohibited use, including use from a
   pinned continuation.
7. Already-applied effects remain historical facts.
8. The uncertain effect is reconciled before retry or compensation.
9. Portable continuation preserves only minimum sensitive material
   needed for legitimate resume.
10. The owner sees the material change, consequence and required
    decision rather than raw audit machinery.

Verdict: PASS.

The boundary supports strict privacy, correction, effect certainty and
fail-closed behavior without making Health policy universal.

### Game/productive-play creative pressure

Scenario:

- a creative process checkpoints accepted canon;
- the owner explores an alternative branch;
- model-generated work after the checkpoint is nondeterministic;
- a source asset later disappears;
- only one branch should become accepted canon.

Required behavior:

1. Fork creates an alternative branch without rewriting accepted canon.
2. Post-checkpoint model/API execution is a new attempt, not guaranteed
   deterministic replay.
3. Generated artifacts and transcripts remain proposals or evidence
   until accepted by the canon/state owner.
4. Promotion of one branch is governed apply with lineage.
5. Unselected drafts and checkpoints may receive lightweight
   pack-declared retention or pruning.
6. Accepted canon decisions and consequential source provenance remain
   interpretable.
7. Source disappearance routes substitution, relicensing, blocking or an
   owner decision.
8. Owner-facing history summarizes creative decisions and branch
   consequences, with deeper lineage inspectable when useful.

Verdict: PASS.

The boundary supports sparse, branch-aware creative persistence without
every-token audit or artifact-as-canon behavior.

## Rejected alternatives

1. Authoritative-current-state minimalism as the complete Q6 answer.

   Rejected because, by itself, it can leave lineage, recovery,
   historical interpretation, source disappearance and
   consequence-specific evidence materially underspecified.

   Retained:
   - single normative state owner;
   - minimal universal burden;
   - anti-bureaucracy discipline.

2. Transition/history-derived continuity as the universal backbone.

   Rejected because it privileges event sourcing and replay, risks
   event-as-truth, nondeterministic re-execution, duplicated external
   effects, unbounded retention, privacy conflict and definition drift.

3. Universal exhaustive event or history stream.

   Rejected because materially different processes require different
   history and audit depth.

4. Universal deterministic replay.

   Rejected because arbitrary model calls, human decisions and external
   APIs do not satisfy deterministic-replay assumptions.

5. Transcript, last message or checkpoint as accepted state.

   Rejected because it bypasses normative ownership, validation,
   correction, current authority and effect reconciliation.

6. Artifact existence as proof.

   Rejected because an artifact does not establish correctness,
   completion or authoritative apply.

7. Newest timestamp, newest event or last-write-wins as authority.

   Rejected because arrival and storage order do not establish normative
   ownership or truth.

8. Append-only history as universal architecture law.

   Rejected because it can block legitimate correction, restriction,
   minimization and erasure.

9. Generic deletion as universal disposition.

   Rejected because it can destroy lineage or effect evidence needed for
   unresolved safety, accountability or compensation obligations.

10. One semantic concern equals one service, store or network hop.

    Rejected because it violates Q2 and prematurely freezes physical
    decomposition.

11. Owner-facing raw audit and history machinery.

    Rejected because internal completeness does not prove useful live
    process behavior.

## Required failure defenses

The architecture explicitly rejects:

- transcript-as-state;
- artifact-as-proof;
- event-as-accepted-truth;
- history, source, evidence and provenance collapse;
- audit-log authority;
- hidden mutation followed by backfilled history;
- silent overwrite;
- lost provenance;
- derived-memory laundering;
- success-only history where uncertain effects disappear;
- blind retry after uncertain effect;
- universal deterministic replay;
- checkpoint-as-complete-truth;
- restore-as-rollback;
- fork-as-canonical-mutation;
- source disappearance making accepted history unintelligible;
- latest-definition reinterpretation;
- unsafe definition removal;
- revocation as fictional rollback;
- append-only ideology;
- generic deletion ideology;
- over-retention;
- one flattened TTL for all durable concerns;
- status-metadata leakage;
- owner-facing audit bureaucracy;
- semantic concerns converted into a final physical service list.

## Evidence limits

The card does not establish:

1. Exact minimum bytes, identifiers or fields for accepted-version
   lineage.
2. One universal evidence threshold for low- and high-consequence
   processes.
3. That audit is mandatory for every process or occurrence.
4. That accepted current state must always be physically materialized.
5. An exact portable-continuation content schema.
6. A universal precedence rule among privacy, safety, legal, audit and
   recovery retention authorities.
7. When a source must be copied versus stably referenced.
8. Exact historical-query compatibility mechanics.
9. Exact identity and correlation semantics.
10. Exact retention periods or deletion guarantees.
11. Legal compliance for a specific process or jurisdiction.
12. Performance, availability, consistency or distributed-systems
    guarantees.
13. A final semantic category count or service-zone catalogue.
14. Live owner-facing usefulness from protocol or history completeness.

These limits do not form a hidden prerequisite for the bounded Q6
decision.

## Child and downstream questions

The following remain open and do not block Q6:

1. What minimum lineage is required for each consequence class?
2. What minimum retained proof establishes effect certainty without
   over-retaining sensitive payloads?
3. Which audit obligations are consequence-triggered and which are
   optional?
4. How are conflicting retention authorities ordered or escalated?
5. When is stable reference sufficient after source disappearance?
6. How is lossy migration represented without freezing a schema?
7. How does a process prove no active continuation depends on a retired
   definition?
8. How are checkpoint integrity and reference accessibility validated
   across carriers?
9. How do correction and revocation propagate into derived memory and
   active consumers?

Existing downstream routes:

- Q7 routing/procedure:
  how intake, accepted state, source requirements and recovery state route
  into reusable procedure invocation versus process-pack-owned procedure
  policy.

- Q8 live interface:
  how history, correction, effect uncertainty and audit are summarized to
  the owner and when deeper lineage becomes inspectable.

- Q9 result/handback:
  exact minimum result and portable-continuation semantics.

- Q10 authority/effects:
  authority for retry, replay, restore, compensation, disposition and
  destructive changes.

- Q11 evidence/evolution:
  exact compatibility evidence, migration, conversion,
  deprecation/removal proof and historical interpretation.

- Q12 communication:
  identities, correlation and representation among state versions,
  transitions, evidence, decisions, checkpoints and continuations.

- Q13 proof:
  conformance scenarios for hidden mutation, duplicate effect,
  outcome-unknown, replay, fork, correction, source disappearance,
  definition migration, retention and owner-facing usefulness.

- Q14 carrier:
  mappings to chat, files, applications, stores and automated transports.

- Q15 graph growth:
  classification of any new architectural entities.

## Graph verdict

hidden_prerequisite: none
gap_event: none
top_level_rebalance: not_needed
return_to_cartography: not_required
implementation_activation: prohibited

Next graph route:

1. bounded Q7 routing/procedure best-practice research;
2. one separate Q7 routing/procedure architecture-forge if research finds
   Q7 ready;
3. no implementation, procedure syntax, router algorithm, provider,
   carrier or final service-block work.

## Not frozen

This card does not freeze:

- actual Health, Zaratusta, game or Direction OS state/history policy;
- actual process-pack declarations;
- a final semantic category catalogue;
- a final reusable-service or service-block list;
- entity, state, event, history, evidence, provenance, source, memory,
  audit, checkpoint, definition, retention or continuation schema;
- field names, identifiers, correlation or version syntax;
- exact lifecycle enums;
- retention intervals;
- legal policy;
- database, event store, filesystem, Git repository, object store,
  vector store or knowledge graph;
- mutable, append-only, event-sourced, snapshot or hybrid storage;
- replay or deduplication implementation;
- provider, model, framework, runtime, transport or topology;
- application, UI or deployment;
- physical writer or state-owner topology;
- proof harness;
- implementation;
- Direction OS changes.

## Gate

status: PASS

Checks:

- Q1-Q5 remain unchanged.
- The card answers only Q6.
- Durable continuity is defined semantically rather than as storage.
- All required concern classes remain distinguishable without exact
  entities.
- One normative state owner establishes each accepted durable version.
- Event, audit, timestamp and last-write-wins authority are rejected.
- Proposal, validation, authorization, apply, result and continuation
  remain distinct.
- Minimum lineage and no-silent-overwrite are defined.
- Correction, dispute, revocation, retirement and migration are covered.
- Effect certainty survives interruption and carrier change.
- Resume, retry, replay, restore, fork, reconcile and compensation remain
  non-equivalent.
- Result and continuation are related to state/history without copying
  Direction OS RESULT.
- Mutable-current-state, event/history-derived, checkpoint and hybrid
  implementation families remain available.
- Definition compatibility, coexistence, migration, pin/drain, removal,
  source disappearance and historical interpretation are covered.
- Retention/status is governed without a universal TTL or deletion
  technology.
- Health-like and game/productive-play pressure tests pass.
- Rejected alternatives and required failure defenses are recorded.
- Owner choice and approval words are recorded.
- Evidence limits and downstream questions are recorded.
- No hidden prerequisite or gap exists.
- No implementation, schema, repository, carrier, provider, topology,
  consumer template or final service-block list is selected.

END_OF_FILE: live/solmax/work/operating-substrate/cards/operating-substrate-persistence-history-001.md
