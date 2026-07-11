RESULT s-solmax-operating-substrate-persistence-history-best-practice-research-001 (call: c-solmax-operating-substrate-persistence-history-best-practice-research-001)
direction: solmax   play: research   node/task: g-operating-substrate/Q6-persistence-history
outcome: |
  A bounded, source-backed Q6 persistence/history research note is complete
  and carried verbatim in this packet for writer persistence.

  The note classifies candidate responsibilities across invariant kernel
  semantics, reusable-service candidates, process-pack declarations,
  owner-profile concerns and adapter/implementation concerns.

  The research recommends responsibility-separated continuity with an
  authoritative-state anchor as the first Q6 forge direction. This is a
  semantic architecture direction, not a selection of mutable storage,
  event sourcing, snapshots, hybrid persistence or any backend.

  Q1-Q5 remain unchanged. No architecture card, schema, repository, storage
  system, carrier, provider, runtime, topology, implementation or final
  service-block list has been approved.

  hidden_prerequisite: none
  gap_event: none
  graph_verdict: Q6 architecture-forge is ready.

evidence: |
  # Operating Substrate Q6 Persistence / History Best-Practice Research

  status: research_input_not_architecture_decision
  call: c-solmax-operating-substrate-persistence-history-best-practice-research-001
  direction: solmax
  node: g-operating-substrate
  researched_at: 2026-07-11
  source_observation_cutoff: 2026-07-11

  ## 1. Research question

  Plain question:

  "Какие persistence/history responsibilities are substrate-level, and what
  remains consumer-specific?"

  The research separates:

  - accepted current state;
  - transition or history material;
  - audit;
  - evidence;
  - provenance;
  - source material;
  - memory;
  - artifacts;
  - process-definition and version material;
  - checkpoint and recovery material;
  - retention and status concerns.

  These terms are working semantic distinctions. They are not accepted
  substrate entities, records, field sets, lifecycle enums or service blocks.

  ## 2. Scope and inherited locks

  The following accepted parent conclusions remain unchanged:

  1. The operating substrate is a stable, model-neutral and carrier-neutral
     kernel with pluggable process packs.

  2. Service zones are semantic responsibility families, not physical
     services, repositories or storage blocks.

  3. Every atomic normative responsibility claim has one primary owner.

  4. One primary normative state owner establishes each accepted durable
     version within a mutable-state boundary.

  5. Query, evidence, proposal, validation, authorization, apply, result and
     continuation remain semantically distinguishable.

  6. A result, event, transcript, artifact or observation does not
     automatically establish accepted durable truth.

  7. Accepted durable mutation crosses a validated apply boundary, and only
     an authoritative apply outcome establishes that the mutation occurred.

  8. Unknown external-effect outcome blocks blind retry.

  9. Portable continuation preserves legitimate resume semantics rather than
     one runtime cursor, transcript or serialized framework object.

  10. Process-pack instantiation is staged admission and activation.

  11. Owner-wide sharing eligibility, process-local accepted truth and action
      authority remain separate conclusions.

  12. Correction, dispute, revocation and retirement are non-equivalent and
      require lineage plus active-work treatment.

  13. Pinning may preserve historical interpretation but cannot preserve
      revoked permission or authority.

  14. No final service-block list, storage system, schema, repository,
      topology, carrier or implementation is accepted.

  Parent evidence:

  - [P1] live/solmax/work/operating-substrate-universal-structure-cartography-001.md
  - [P2] live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
  - [P3] live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
  - [P4] live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
  - [P5] live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
  - [P6] live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md
  - [P7] live/solmax/work/operating-substrate/cards/operating-substrate-shared-owner-context-001.md
  - [P8] live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

  ## 3. Bounded research answer

  The substrate-level answer is not "store everything" and not "choose one
  canonical history model."

  Candidate substrate invariants concern the meaning and legitimacy of durable
  continuity:

  - which accepted state is authoritative for the next legitimate action;
  - who may establish a new accepted version;
  - how a durable change remains attributable to its cause, authority,
    evidence and prior version;
  - how current state remains distinct from observation, history, audit,
    evidence, source, memory and artifacts;
  - how correction, dispute, revocation and retirement affect current use
    without silently rewriting history;
  - how uncertainty about an external effect survives interruption;
  - how recovery avoids blind replay, duplicated effects and authority
    expansion;
  - how the governing definition/version remains identifiable and
    historically interpretable;
  - how retention, restriction, disposition and currentness remain explicit
    governed concerns rather than accidental properties of a backend;
  - how portable continuation preserves the next legitimate action without
    copying every transcript or internal trace.

  Consumer-specific concerns include:

  - the domain meaning and content of state;
  - which occurrences deserve history or audit treatment;
  - evidence sufficiency;
  - source acceptance rules;
  - replay-safe and replay-unsafe operations;
  - recovery, compensation and migration policy;
  - retention purposes and constraints;
  - correction, dispute and retirement policy;
  - owner-facing history presentation;
  - exact representation and implementation.

  No universal exhaustive event history, full audit log, snapshot stream,
  transcript archive or memory store is supported by the evidence.

  ## 4. Semantic distinctions

  ### 4.1 Accepted current state

  Meaning:

  - the normative durable conclusion used as the current basis for subsequent
    legitimate reads, validation, decisions and actions within a named
    mutable-state boundary;
  - established by that boundary's primary normative state owner through the
    accepted apply semantics.

  It is not automatically:

  - the last message;
  - the most recent timestamp;
  - the newest event;
  - a transcript summary;
  - a model inference;
  - a restored checkpoint;
  - an artifact;
  - the output of an arbitrary writer.

  The accepted current state may be materialized directly or derived in an
  implementation. Q6 architecture should freeze its normative meaning and
  ownership, not its physical representation.

  ### 4.2 Transition or history material

  Meaning:

  - durable material describing an occurrence, attempted transition,
    authoritative transition, status change or relation between versions.

  It can include successful, rejected, partial, cancelled or uncertain
  attempts when relevant.

  It is not automatically:

  - accepted current state;
  - sufficient evidence;
  - an audit record;
  - a command;
  - proof that an external effect occurred;
  - an authorization to repeat the transition.

  One occurrence may produce several observations or event records, and an
  event producer can differ from the source in whose context the occurrence
  happened. [S3]

  ### 4.3 Audit

  Meaning:

  - selected durable accountability material supporting review of what was
    attempted or decided, by whom or under which authority, against which
    policy or definition, and with what reported outcome;
  - governed by an explicit audit purpose, access boundary and retention
    responsibility.

  It is not automatically:

  - a full domain history;
  - the authoritative current state;
  - a complete evidence ledger;
  - every debug log;
  - every model trace;
  - proof that an observed claim is true.

  NIST treats log management as an enterprise process spanning infrastructure,
  collection and maintenance rather than merely one log format. OpenTelemetry
  separately defines a logical log-record model independent of physical
  encoding. [S4] [S5]

  The substrate therefore has reason to preserve audit semantics and
  responsibility, but not to require an exhaustive universal audit stream for
  every low-consequence process.

  ### 4.4 Evidence

  Meaning:

  - material that supports, refutes or qualifies a claim, proposal,
    validation conclusion, transition, effect outcome or result;
  - material whose sufficiency is judged by the legitimate evaluator or
    authority for the consuming obligation.

  It is not automatically:

  - accepted truth;
  - provenance;
  - an artifact merely because it was attached;
  - an audit record;
  - a result;
  - an authorization.

  Evidence needs provenance appropriate to the consequentiality of the claim.
  The evidence producer owns the accuracy of its stated origin and scope; the
  evaluator owns the sufficiency conclusion.

  ### 4.5 Provenance

  Meaning:

  - lineage information about origin, generation, use, derivation, revision,
    invalidation, responsible actors or activities and relationships among
    materials.

  W3C PROV explicitly separates generation, derivation, revision,
  invalidation, attribution and primary-source relations. It also treats
  provenance as information used to assess quality, reliability or
  trustworthiness rather than as an automatic truth verdict. [S1]

  Provenance is not automatically:

  - proof that the source is correct;
  - permission to use the material;
  - accepted current state;
  - a complete audit;
  - a transition authorization.

  ### 4.6 Source

  Meaning:

  - originating material, system, actor, observation or assertion from which a
    claim, artifact, evidence item or derived material is obtained.

  A source can be:

  - available or unavailable;
  - current or superseded;
  - trusted for one purpose and insufficient for another;
  - disputed, corrected or invalidated;
  - retained, referenced or absent.

  Source identity, source availability, source authenticity, claim truth,
  fitness for purpose and permission to use remain separate conclusions.

  Source disappearance does not prove that the source was false, nor may it
  silently promote a derived summary into authoritative truth.

  ### 4.7 Memory

  Meaning:

  - retrievable material intended to assist later reasoning, recall,
    personalization or continuity;
  - potentially copied from prior interactions or derived through extraction,
    summarization or consolidation.

  It is not automatically:

  - accepted process state;
  - owner-wide truth;
  - evidence;
  - source material;
  - a checkpoint;
  - a transcript archive.

  Google ADK distinguishes session event history, mutable session state and
  longer-term searchable memory. Its documentation also shows that memory may
  ingest a full session or use model-based consolidation. LangGraph similarly
  separates thread-scoped checkpoints from cross-thread stores. [S8] [S9]

  Derived memory therefore requires provenance and cannot launder an inference
  into accepted truth.

  ### 4.8 Artifact

  Meaning:

  - a produced object, document, dataset, media item, code output or other
    deliverable.

  It may be:

  - an output referenced by a result;
  - evidence for a claim;
  - a source for later work;
  - proposed material awaiting acceptance.

  It is not automatically:

  - a complete result;
  - proof of correctness;
  - accepted durable state;
  - authorized for use;
  - current merely because it is newest.

  ### 4.9 Process-definition and version material

  Meaning:

  - accepted semantics, rules, obligations, compatibility expectations and
    authority boundaries governing a process or active obligation;
  - the interpretive basis needed to understand why historical state or work
    had its meaning at the time.

  It is distinct from:

  - runtime state;
  - source-package availability;
  - one code revision identifier;
  - current pack activation;
  - storage schema version.

  Definition identity and lineage must remain interpretable even when the
  original source or runtime is unavailable. The exact method of preserving
  that interpretability is downstream.

  ### 4.10 Checkpoint and recovery material

  Meaning:

  - a bounded durable basis from which legitimate work may be resumed,
    reconciled, restored or branched after interruption.

  It can contain or reference:

  - accepted state;
  - completed and open obligations;
  - authority and pending decisions;
  - effect certainty;
  - definition compatibility;
  - evidence and provenance;
  - the next legitimate action.

  It is not automatically:

  - full history;
  - current accepted truth at resume time;
  - proof that no later effect happened;
  - a new authorization;
  - a safe instruction to replay every post-checkpoint action;
  - long-term memory.

  ### 4.11 Retention and status concerns

  Meaning:

  - governed conclusions about continued availability, permitted use,
    restriction, currentness, correction, suspension, revocation, retirement,
    expiration, disposition or erasure.

  Exact statuses and lifecycle enums remain downstream.

  Important non-equivalences include:

  - unavailable is not false;
  - restricted is not erased;
  - revoked is not historically nonexistent;
  - retired is not necessarily deleted;
  - corrected is not silently overwritten;
  - disputed is not resolved;
  - expired is not necessarily invalid for historical interpretation;
  - retained is not necessarily permitted for every use.

  GDPR provides jurisdiction-specific evidence for separating minimization,
  accuracy, rectification, erasure, restriction, storage limitation and
  notification to recipients. W3C Bitstring Status List separately models
  suspension/revocation-style status and highlights privacy risks caused by
  status checking itself. [S11] [S12]

  ## 5. Primary-source comparison

  ### 5.1 W3C PROV-DM

  Relevant evidence:

  - provenance concerns entities, activities, responsible agents and the
    production of data or things;
  - generation, use, derivation, revision, invalidation and primary-source
    relations are distinguishable;
  - a revision is a qualified derivation relation;
  - invalidation concerns cessation, destruction or expiry;
  - provenance can support assessment but does not itself decide truth.

  Q6 support:

  - origin, lineage, revision and invalidation should not collapse into one
    generic history field;
  - source and derived material remain distinguishable;
  - correction can retain lineage rather than overwrite prior material.

  Limitation:

  - PROV is retrospective provenance, not a model of accepted state,
    authorization, durable workflow recovery or retention authority.

  ### 5.2 OpenLineage 1.50.0

  Relevant evidence:

  - runtime run-state observations, design-time job metadata and dataset
    metadata use distinct event forms;
  - design lineage is not tied to a runtime execution;
  - job source location/version and dataset lifecycle/version can be
    represented separately from run observations;
  - later observations can add information that was unavailable earlier.

  Q6 support:

  - runtime history and definition/design lineage are different concerns;
  - lineage can span heterogeneous underlying architectures;
  - observations can be incomplete and additive.

  Limitation:

  - OpenLineage is designed for data pipelines and does not define state
    authority, human authorization, correction policy or portable
    continuation.

  ### 5.3 CloudEvents 1.0.2

  Relevant evidence:

  - an occurrence is a captured statement about something noteworthy;
  - an event is a data record expressing the occurrence and its context;
  - one occurrence can produce multiple events;
  - source, producer, consumer and intermediary are separate roles.

  Q6 support:

  - event records must not be treated as unique, authoritative state truth;
  - event source and event producer can differ;
  - event transport does not determine evidence, audit or state semantics.

  Limitation:

  - CloudEvents defines interoperable event data, not state ownership,
    validation, authority, audit sufficiency or recovery.

  ### 5.4 OpenTelemetry Logs Data Model 1.59.0

  Relevant evidence:

  - the stable model represents logs from heterogeneous sources;
  - it is a logical model independent of physical format and encoding;
  - occurrence time and observation time can be different;
  - resource, instrumentation scope, trace relation, severity and event body
    are distinguishable.

  Q6 support:

  - a log record is an observation representation, not automatically a domain
    transition or accepted state;
  - logical log semantics can remain separate from storage representation;
  - observation provenance and timing matter for audit interpretation.

  Limitation:

  - OpenTelemetry does not define which records are normatively complete,
    admissible as evidence or authoritative for current state.

  ### 5.5 NIST SP 800-92

  Relevant evidence:

  - sound security-log management requires organization-wide processes for
    collection, infrastructure, maintenance and use;
  - the guidance intentionally remains above one logging technology;
  - audit and accountability are a distinct control concern.

  Q6 support:

  - audit/log responsibility includes governance and lifecycle, not merely
    writing messages;
  - audit purpose and operational history need not be identical.

  Limitation:

  - the publication dates to 2006, is security-log focused and does not define
    a universal operating-substrate state or recovery model.

  ### 5.6 Temporal Event History, Activities, retries and Worker Versioning

  Relevant evidence:

  - workflow event history is durably appended and used for crash recovery,
    debugging and audit-like inspection;
  - history has operational limits and can be continued through a new run;
  - completed workflow-side effects can be represented in history rather than
    re-executed during deterministic replay;
  - activities can execute more than once even when completion is observed
    once;
  - a worker can complete an external effect and fail before reporting it,
    causing retry;
  - idempotence or external reconciliation is required for safe repeated
    execution;
  - pinned and auto-upgrading workflows impose different compatibility
    expectations;
  - deployments can be active, draining or drained, and retained historical
    workflow queries may still depend on old workers.

  Q6 support:

  - effect certainty and execution-attempt history are distinct from one
    reported completion;
  - unknown outcome cannot be treated as known-not-done;
  - deterministic replay is a special contract, not a universal recovery
    primitive;
  - active work needs explicit compatibility, migration or pin/drain behavior.

  Limitation:

  - Temporal is one durable-workflow realization with specific event-history,
    determinism and worker-version semantics.

  ### 5.7 Microsoft Durable Task

  Relevant evidence:

  - orchestration progress is checkpointed across process or machine failure;
  - current local orchestration state is rebuilt by replaying execution
    history;
  - the implementation explicitly uses event sourcing and append-only
    orchestration history;
  - replay correctness requires deterministic orchestration code;
  - consistency characteristics can differ between storage providers;
  - its illustrative history-table representation is not a stable universal
    contract.

  Q6 support:

  - event/history-derived state is a viable implementation;
  - recovery semantics can be coupled to code determinism and runtime history;
  - provider consistency and history representation are adapter concerns.

  Limitation:

  - its event-sourced, deterministic orchestration model must not be elevated
    into the universal substrate architecture.

  ### 5.8 LangGraph persistence and time travel

  Relevant evidence:

  - checkpoints capture thread-scoped state while stores provide cross-thread
    long-term material;
  - retained checkpoints can grow without bound unless pruned;
  - replay resumes from a checkpoint but re-executes later nodes;
  - LLM calls, API calls and interrupts after the selected checkpoint execute
    again and can produce different results;
  - fork creates a new branch and leaves the original history intact.

  Q6 support:

  - checkpoint, memory, replay and fork are different concerns;
  - replay in model-driven work is not deterministic restoration;
  - branching can preserve prior lineage instead of overwriting it;
  - checkpoint retention needs explicit policy.

  Limitation:

  - LangGraph is an evolving framework and does not define universal state
    authority, effect reconciliation or retention policy.

  ### 5.9 Google Agent Development Kit state and memory

  Relevant evidence:

  - session event history and mutable session state are separate;
  - searchable memory is separate from the active session;
  - direct mutation outside the event/update path can bypass tracking and lose
    data;
  - a memory implementation may copy transcript material or derive and
    consolidate it.

  Q6 support:

  - transcript, history, current state and memory should not collapse;
  - hidden mutation breaks lineage;
  - derived memory needs provenance and acceptance boundaries.

  Limitation:

  - ADK objects and services are framework-specific and cannot become
    substrate entities.

  ### 5.10 Kubernetes CustomResourceDefinition versioning

  Relevant evidence:

  - old and new versions can be served concurrently while clients migrate;
  - stored objects can be migrated separately from client adoption;
  - old serving support is disabled after client migration;
  - old stored-version support is removed after persisted material has been
    upgraded;
  - previous storage versions remain tracked during transition.

  Q6 support:

  - definition/version evolution requires compatibility and migration state;
  - pin/drain and migration can be per-consumer or per-obligation rather than
    one global instant;
  - removal requires proof that active and stored dependencies are settled.

  Limitation:

  - this is an API and object-storage versioning workflow, not a universal
    process-definition model.

  ### 5.11 GDPR official text

  Relevant evidence:

  - purpose limitation, minimization, accuracy, storage limitation and
    accountability are separate duties;
  - correction, erasure and restriction are distinct;
  - restriction can preserve storage while limiting use;
  - recipients can need notification of correction, erasure or restriction;
  - erasure has scoped exceptions for legal, public-interest, research and
    claims purposes;
  - retention periods or criteria and source information can be material to
    the data subject.

  Q6 support:

  - retention cannot be one universal TTL;
  - correction, restriction and erasure must not be represented as synonyms;
  - status changes can need propagation to active consumers;
  - retained historical proof and continued permission to use are distinct.

  Limitation:

  - GDPR is jurisdiction-specific law and cannot itself define universal
    substrate policy.

  ### 5.12 W3C Bitstring Status List 1.0

  Relevant evidence:

  - suspension and revocation-style purposes can be distinct;
  - point-in-time status can differ from current status;
  - status retrieval can itself leak sensitive correlation information;
  - verification of status remains separate from trusting the issuer or claim.

  Q6 support:

  - validity/status and provenance/trust are separate;
  - status history and current status are both meaningful;
  - privacy applies to metadata and status access, not only payload content.

  Limitation:

  - the specification concerns verifiable credentials and one status-list
    mechanism, not a universal substrate status model.

  ## 6. Convergent findings

  ### 6.1 Durable continuity is a semantic property

  Durable continuity means that interrupted work can determine:

  - which accepted state still governs;
  - what has definitely happened;
  - what might have happened;
  - what remains open;
  - who owns the next resolution step;
  - which authority remains valid;
  - which definition/version can interpret the work;
  - what next action is legitimate.

  This property can be implemented with mutable records, histories,
  checkpoints, snapshots, event sourcing or combinations. None of those
  techniques is itself the invariant.

  ### 6.2 Current truth and historical observation are different normative roles

  A history event can report that a state change was attempted or observed.
  The primary normative state owner determines whether an accepted durable
  version exists.

  Therefore:

  - event order alone cannot establish accepted current truth;
  - newest timestamp does not imply precedence;
  - audit completeness does not confer state authority;
  - state truth does not guarantee complete audit;
  - a lost history append after successful authoritative apply creates an
    audit/lineage gap to reconcile, not permission to deny the applied state;
  - a history item claiming success cannot override the authoritative state
    owner's contrary outcome.

  ### 6.3 History, audit, evidence and provenance overlap but are not synonyms

  A single physical record may support several responsibilities, but
  conformance still needs to establish separately:

  - what occurrence or transition it reports;
  - whether it is part of normative history;
  - whether it satisfies an audit purpose;
  - which claim it supports as evidence;
  - what provenance it asserts;
  - who owns completeness and interpretation;
  - what retention and access rules apply.

  ### 6.4 No universal exhaustive history is justified

  High-consequence processes may require detailed causal, decision, effect and
  audit histories. Lightweight creative or exploratory work may need only
  sparse accepted-state lineage and bounded checkpoints.

  The kernel should require enough durable material to preserve accepted-state
  legitimacy, effect certainty, unresolved ownership, definition
  interpretability and required evidence. Process packs declare the additional
  history and audit obligations.

  ### 6.5 No universal deterministic replay is justified

  Deterministic workflow systems can reconstruct local state by replaying
  recorded events. Model calls, human decisions, external APIs and
  non-idempotent effects do not generally satisfy that assumption.

  Replay is therefore one possible recovery operation, not the definition of
  recovery.

  ### 6.6 Checkpoint sufficiency is semantic, not byte completeness

  A checkpoint is insufficient for portable recovery when it omits material
  needed to determine:

  - authoritative accepted state;
  - pending owners and obligations;
  - authority and decision scope;
  - partial or unknown effects;
  - governing definition compatibility;
  - relevant provenance;
  - the next legitimate action.

  A compact reference-based continuation can be sufficient if its references
  remain accessible, authorized and interpretable. A large snapshot can still
  be insufficient if it omits those semantics.

  ### 6.7 Correction must create lineage rather than silent replacement

  A correction normally establishes a new accepted conclusion through the
  governed apply path and links it to the material it corrects.

  The prior material can remain:

  - historical but no longer current;
  - restricted;
  - disputed;
  - retained only for a legitimate evidence or audit purpose;
  - removed when required and when removal does not falsify unresolved effect
    certainty or other mandatory obligations.

  The exact retention result is policy-specific.

  ### 6.8 Revocation does not fictionalize history

  Revocation can stop future use, sharing, reliance or action authority.
  It does not prove that prior lawful processing, prior decisions or already
  applied external effects never happened.

  Recovery and continuation must therefore preserve:

  - the fact of prior effects when legitimately necessary;
  - the current prohibition on future use;
  - the need to revalidate affected open work.

  ### 6.9 Definition evolution must not retroactively reinterpret history

  Historical state and decisions need to be understood under the governing
  definition/version effective at the time.

  A new definition can trigger migration or revalidation, but it must not
  silently make an old record mean something different.

  ### 6.10 Retention is a governed responsibility, not a storage default

  Each durable responsibility class can have a different legitimate retention
  purpose:

  - accepted current state;
  - transition history;
  - audit;
  - evidence;
  - provenance;
  - source material;
  - memory;
  - artifacts;
  - checkpoints;
  - definition/version material;
  - continuation material.

  Keeping everything indefinitely and deleting everything after one process
  completes are both unsupported universal defaults.

  ## 7. Candidate responsibility classification

  This classification is research input for Q6 forge. It does not approve an
  architecture card or a final service-zone catalogue.

  ### 7.1 Candidate invariant kernel semantics

  #### K1. Semantic non-collapse

  Accepted state, transition/history, audit, evidence, provenance, source,
  memory, artifact, definition/version, checkpoint/recovery and
  retention/status remain distinguishable even when one representation serves
  several purposes.

  #### K2. Authoritative accepted-state ownership

  Each mutable-state boundary has one primary normative owner that establishes
  each accepted durable version.

  Many roles may observe, propose, validate, derive, checkpoint or audit. They
  do not become the state owner through possession of data or write
  capability.

  #### K3. Validated durable mutation

  Durable mutation occurs only through the accepted validated apply semantics.

  A proposal, validation result, human authorization, event, history append,
  artifact or result does not independently prove that the state transition
  occurred.

  #### K4. Accepted-version lineage

  A newly accepted durable version remains attributable, at the semantic
  level, to:

  - the prior accepted basis or explicitly stated absence of one;
  - the governed transition or correction;
  - relevant authority and validation;
  - material provenance/evidence;
  - the governing process definition;
  - the authoritative effect outcome.

  Exact identifiers and fields remain downstream.

  #### K5. No silent overwrite

  Correction, conflict resolution, migration or replacement cannot erase the
  fact that a prior accepted version governed earlier work.

  This does not require permanent retention of all prior bytes. It requires
  that legitimate history, active dependencies and effect certainty are not
  silently falsified.

  #### K6. Effect certainty preservation

  Interruption, timeout, cancellation and delivery failure preserve the
  distinction among:

  - known not done;
  - applied or authoritatively confirmed;
  - partial;
  - outcome unknown;
  - resolved through a later governed compensating effect.

  These are working distinctions, not a frozen lifecycle enum.

  #### K7. Recovery-action non-equivalence

  Resume, retry, replay, restore, fork, reconcile and compensate have different
  semantic effects and must not be treated as one generic recovery command.

  Recovery cannot expand authority or infer that an uncertain prior effect did
  not occur.

  #### K8. Legitimate portable continuation

  Continuation preserves enough accepted semantics to establish:

  - the current accepted basis or authoritative reference;
  - completed and unresolved obligations;
  - current next-action owners;
  - relevant decisions and authority;
  - effect certainty;
  - evidence/provenance needed for continuation;
  - definition/version compatibility;
  - the next legitimate action and return route.

  It is not required to contain every transcript, event or artifact.

  #### K9. Historical definition interpretability

  Accepted state, results, evidence and transitions remain interpretable under
  the definition/version that governed them.

  Source disappearance, deprecation or runtime replacement cannot silently
  make accepted historical material semantically opaque.

  #### K10. Lifecycle-status non-equivalence

  Correction, dispute, restriction, suspension, revocation, retirement,
  expiration, erasure and source unavailability remain distinct governed
  conclusions where applicable.

  Exact status vocabulary remains downstream.

  #### K11. Explicit retention/disposition responsibility

  Durable material has a legitimate responsible route for deciding continued
  retention, restricted use, archival treatment or disposition.

  The kernel does not define universal purposes, legal bases, intervals or
  deletion mechanics.

  #### K12. Active-work impact propagation

  When relevant state, source, definition, authority or retention status
  changes, affected open obligations receive an explicit compatible-resume,
  revalidation/migration, pin/drain, handoff, block/rejection or
  named-unresolved-owner disposition.

  #### K13. Reference failure is explicit

  A continuation or historical record that depends on external material must
  preserve enough information to detect inaccessible, missing, superseded or
  unauthorized references and route the resulting obligation.

  Missing material cannot silently become accepted from a stale summary.

  #### K14. Proportional owner-facing visibility

  Persistence conformance cannot require the owner to operate raw audit logs,
  event streams or checkpoint machinery.

  The substrate must support useful accountability and correction, while the
  process pack and live interface determine proportional owner-facing
  summaries, inspection and decision requests.

  ### 7.2 Reusable-service candidates

  The following are semantic capability candidates, not final services or
  deployment blocks:

  1. Accepted-state read and controlled apply support.
  2. Transition/history capture and query.
  3. Provenance and lineage maintenance.
  4. Evidence integrity, reference and retrieval.
  5. Audit capture, review and export under bounded policy.
  6. Source-reference integrity and availability observation.
  7. Checkpoint creation, validation, import and restore support.
  8. Recovery and authoritative reconciliation coordination.
  9. Definition/version lineage and compatibility evaluation.
  10. Migration, pin/drain and historical-interpretation support.
  11. Retention, restriction, disposition and downstream-status propagation.
  12. Conflict, correction, dispute, revocation and retirement propagation.

  A realization may:

  - compose several candidates in one component;
  - distribute one candidate across several components;
  - omit optional candidates when a pack does not require them;
  - use consumer-native implementations behind adapters.

  A reusable capability does not automatically become the normative owner of
  the state, evidence, authority or retention decision it handles.

  ### 7.3 Process-pack declarations

  A process pack is the candidate normative owner for domain-specific
  declarations such as:

  1. Which domain conclusions can become accepted process state.
  2. Mutable-state boundaries and required normative owners.
  3. Valid transition and correction conditions.
  4. Required causal and historical material by consequence class.
  5. Which occurrences require audit treatment and for what purpose.
  6. Evidence sufficiency and source-currentness rules.
  7. Which operations are replay-safe, retry-safe, idempotent, reconcilable,
     compensatable or unsafe to repeat.
  8. Checkpoint sufficiency, creation triggers and acceptable recovery loss at
     the semantic level.
  9. Forking, alternative-branch and canonical-promotion behavior.
  10. Definition/version compatibility and migration obligations.
  11. Pin/drain, deprecation and removal conditions.
  12. Correction, dispute, restriction, revocation and retirement effects.
  13. Retention purposes, minimization requirements and mandatory historical
      evidence.
  14. Source capture versus durable-reference requirements.
  15. Owner-facing history, correction and audit presentation.
  16. Domain escalation when retained proof conflicts with privacy, safety or
      legal disposition requirements.

  Actual Health, game, Zaratusta or Direction OS declarations remain outside
  Q6.

  ### 7.4 Owner-profile concerns

  Genuinely owner-wide concerns can include:

  - approved privacy and sharing preferences;
  - preferred audit/history visibility and notification level;
  - owner-wide correction and dispute preferences;
  - approved retention minimization preferences;
  - preferences for destructive-action confirmation;
  - preferred balance between concise summaries and inspectable detail.

  Owner-profile concerns do not:

  - establish process-local truth;
  - override mandatory safety, legal, evidence or retention policy;
  - authorize an external effect;
  - make all process history owner-wide;
  - permit secret or sensitive material to be copied into continuations;
  - turn a personal preference into a universal kernel rule.

  ### 7.5 Adapter and implementation concerns

  The following remain downstream HOW decisions:

  - mutable records, append-only histories, event stores, snapshots or
    physical hybrids;
  - databases, filesystems, Git repositories, object stores, vector stores,
    knowledge graphs or other backends;
  - event, state, audit, evidence, provenance, checkpoint and retention
    schemas;
  - fields, identifiers, version syntax, timestamps and correlation formats;
  - serialization, compression, compaction and garbage collection;
  - replication, backup, encryption and access-control mechanisms;
  - indexing, search and query optimization;
  - snapshot cadence and physical consistency;
  - replay engines and deterministic-execution mechanisms;
  - idempotency-key representation and deduplication technology;
  - tombstones, deletion, redaction and erasure mechanics;
  - provider-specific migration and rollback mechanisms;
  - runtime, framework, model, transport, deployment and topology.

  ## 8. Normative ownership of durable concerns

  The following labels describe temporary responsibility roles. They do not
  prescribe physical components.

  ### 8.1 Accepted-state owner

  Owns:

  - the current normative durable version for its mutable boundary;
  - validation of current-state preconditions at apply;
  - authoritative settlement of whether the mutation occurred;
  - conflict or stale-write rejection.

  Does not automatically own:

  - every source claim;
  - the truth of every evidence item;
  - all audit collection;
  - process integration;
  - owner-wide policy.

  ### 8.2 History responsibility

  Owns:

  - the completeness and integrity of the history it claims to maintain;
  - attribution of observed or accepted transitions to their reported causes;
  - explicit gaps or uncertainty in that history.

  Does not automatically own:

  - current state truth;
  - authority to apply;
  - evidence sufficiency;
  - retention policy outside its scope.

  ### 8.3 Audit responsibility

  Owns:

  - the declared audit purpose and coverage;
  - integrity and access expectations for audit material;
  - explicit disclosure of known audit gaps;
  - routing of required review or accountability obligations.

  Does not automatically own:

  - the domain transition;
  - current state;
  - every debug trace;
  - owner-facing presentation.

  ### 8.4 Evidence producer and evaluator

  The producer owns:

  - stated origin;
  - stated scope;
  - known derivation;
  - known limitations.

  The evaluator or authority owner owns:

  - whether the evidence is sufficient for the consuming claim, decision or
    transition.

  ### 8.5 Provenance responsibility

  Owns:

  - accuracy of asserted lineage relations;
  - distinction among source, derivation, revision and invalidation;
  - preservation or explicit loss of relevant lineage.

  It does not prove the truth of the related content.

  ### 8.6 Checkpoint responsibility

  Owns:

  - what the checkpoint claims to preserve;
  - whether its references and integrity can be validated;
  - its known omissions;
  - compatibility information needed for attempted use.

  It does not unilaterally decide that restore or replay is safe.

  ### 8.7 Recovery owner

  Owns:

  - resolution of the interrupted or uncertain obligation;
  - selection or routing of a legitimate recovery action;
  - reconciliation before unsafe repetition;
  - explicit closure or escalation when recovery remains unresolved.

  Recovery ownership does not transfer durable-state or human-decision
  authority.

  ### 8.8 Definition/version owner

  Owns:

  - accepted definition identity and lineage;
  - compatibility claims;
  - deprecation and removal criteria;
  - historical interpretability expectations.

  It does not automatically migrate consumer state or authorize changed
  effects.

  ### 8.9 Retention/disposition owner

  Owns:

  - applicable retention, restriction or disposition conclusions within its
    normative scope;
  - legitimate purpose and minimization;
  - propagation to affected consumers when required;
  - conflicts or exceptions requiring authority escalation.

  The adapter executing deletion or restriction does not invent the policy.

  ## 9. Validated mutation, lineage and lifecycle changes

  ### 9.1 Normal accepted mutation

  A semantically complete durable transition follows the inherited relation
  distinctions:

  1. A current owner or procedure forms a candidate change.
  2. Relevant current state and sources are queried.
  3. Evidence and provenance are assembled.
  4. The proposal is validated against current preconditions and policy.
  5. Required authority decides the exact proposal.
  6. The authoritative state/effect owner performs apply.
  7. The authoritative outcome establishes applied, rejected, conflicting,
     partial, known-not-done or outcome-unknown treatment.
  8. Relevant history, provenance, evidence and audit responsibilities record
     or reference the transition according to their declared obligations.
  9. The result integrates the outcome.
  10. Continuation preserves unresolved work and the next legitimate action.

  One implementation can combine several steps internally. Conformance still
  has to prove their semantic effects.

  ### 9.2 Correction

  Candidate invariant treatment:

  - correction enters as a proposed new conclusion;
  - it is validated and applied by the relevant normative state owner;
  - the new accepted version identifies the corrected relation at the
    semantic level;
  - active consumers revalidate affected work;
  - prior material ceases to be current;
  - prior material is retained, restricted or disposed according to applicable
    policy;
  - derived memory and summaries do not continue presenting the old material
    as accepted truth.

  Correction is not an in-place edit that makes prior use impossible to
  explain.

  ### 9.3 Dispute

  Candidate invariant treatment:

  - the dispute is preserved as a qualified claim or status;
  - competing claims and provenance remain distinguishable;
  - unresolved material is not silently resolved by newest timestamp or
    last-write-wins;
  - active work receives a use, revalidation, block or escalation
    disposition;
  - an authority or state owner resolves only the claims within its scope.

  A dispute can exist without an immediate replacement state.

  ### 9.4 Revocation

  Candidate invariant treatment:

  - revocation changes future permission, reliance, status or authority for
    its bounded subject;
  - active dependants are notified or revalidated;
  - pending authorization cannot be reused outside its still-valid scope;
  - already applied effects remain historical facts;
  - compensation, when required, is a new governed effect.

  Revocation is not retroactive erasure of reality.

  ### 9.5 Retirement

  Candidate invariant treatment:

  - retired material is no longer eligible for ordinary new use or
    activation;
  - active work receives explicit drain, migration, replacement, rejection or
    unresolved-owner treatment;
  - historical interpretation remains possible where legitimately required;
  - actual retention and access are governed separately.

  Retirement is not synonymous with deletion.

  ### 9.6 Source invalidation or disappearance

  Candidate invariant treatment:

  - source availability and source status change explicitly;
  - historical derivations preserve the fact that the source was used;
  - the absence of the source does not prove or disprove the derived claim;
  - new use is revalidated against current source and evidence requirements;
  - continuations depending on inaccessible material become blocked,
    substitutable or unresolved rather than silently resumable;
  - the process pack decides whether accepted source capture, stable reference,
    replacement or owner escalation is sufficient.

  ## 10. Recovery and effect certainty

  The following are working semantic recovery actions, not a final protocol or
  enum.

  ### 10.1 Resume

  Continue from a preserved legitimate state without intentionally repeating
  already completed work.

  Resume requires:

  - accepted state or an authoritative reference;
  - compatible definition;
  - current owners;
  - valid authority;
  - known effect status;
  - the next legitimate action.

  ### 10.2 Retry

  Start another execution attempt for the same logical obligation.

  Retry is safe only when:

  - prior outcome is known not done;
  - the operation is idempotent or deduplicated;
  - authoritative reconciliation established that repetition is safe;
  - or an authority explicitly accepts the bounded duplicate-effect risk.

  A timeout alone is insufficient.

  ### 10.3 Replay

  Re-execute prior procedural steps using retained history or inputs.

  Replay can be:

  - deterministic reconstruction in a constrained workflow runtime;
  - a new nondeterministic attempt in model-, human- or API-driven work.

  Q6 must not assume the first meaning universally.

  ### 10.4 Restore

  Re-establish state from a prior checkpoint or snapshot.

  Restore does not prove:

  - that no later external effect occurred;
  - that the restored definition is still compatible;
  - that prior authorization is still valid;
  - that the checkpoint is the current accepted state.

  ### 10.5 Fork

  Create a new branch from a prior accepted basis or checkpoint while
  preserving the original branch.

  Fork is not rollback and does not change canonical accepted state until a
  separate governed apply or promotion occurs.

  ### 10.6 Reconcile

  Query the authoritative state or effect owner to determine what actually
  happened and settle uncertainty.

  Reconcile is the preferred first response when an external effect may have
  occurred and retry safety is not independently proven.

  ### 10.7 Compensate

  Perform a new governed effect intended to offset or mitigate a prior effect.

  Compensation:

  - requires current validation and authority;
  - has its own outcome and evidence;
  - does not erase the prior effect or its history.

  ### 10.8 Checkpoint sufficiency test

  A candidate checkpoint fails semantic sufficiency when a fresh legitimate
  carrier cannot determine:

  - whether the state is accepted or merely proposed;
  - whether an external effect may already have happened;
  - which authorization remains applicable;
  - which obligations are still open;
  - who owns the next resolution step;
  - which definition can interpret the material;
  - whether required sources or evidence remain usable;
  - what next action is permitted.

  ## 11. Result and portable continuation

  ### 11.1 Result

  A result settles or checkpoints a bounded obligation and returns integration
  responsibility.

  It can report:

  - achieved or not achieved;
  - authoritative apply outcome;
  - effect certainty;
  - outputs and artifacts;
  - evidence and provenance;
  - unresolved obligations and owners;
  - continuation disposition.

  A result does not by itself:

  - mutate non-authoritative state;
  - make its narrative accepted truth;
  - turn every artifact into evidence;
  - become the complete process history;
  - authorize further effects.

  When a result contains an authoritative apply receipt, the receipt reports
  the state owner's outcome. The result wrapper is not the source of state
  authority.

  ### 11.2 Portable continuation

  Portable continuation is a semantic recovery contract.

  It can carry or reference:

  - accepted state;
  - relevant history;
  - a checkpoint;
  - governing definition/version material;
  - decisions and authority;
  - evidence and provenance;
  - unresolved obligations;
  - effect certainty;
  - the next legitimate action.

  It is not:

  - a transcript dump;
  - one framework's serialized run;
  - a complete audit trail;
  - a storage snapshot by definition;
  - a reusable authorization;
  - proof that every referenced source remains available.

  On resume, the receiving carrier may need to:

  - validate integrity;
  - resolve references;
  - re-check sharing or privacy status;
  - assess definition compatibility;
  - reconcile uncertain effects;
  - revalidate stale authority or current-state preconditions.

  ### 11.3 Relation between result, continuation and history

  Candidate semantic relation:

  - result explains closure or non-closure of the current obligation;
  - continuation preserves legitimate future ownership and action;
  - history records relevant occurrences or transitions;
  - audit supports accountability;
  - evidence supports claims;
  - provenance explains lineage;
  - accepted state remains owned by the normative state owner.

  One physical artifact can carry several of these facets. Their normative
  meanings remain separately testable.

  This conclusion does not copy Direction OS RESULT fields or establish a
  universal packet schema.

  ## 12. Persistence approach comparison

  All four approaches can conform if they preserve the candidate invariants.
  None is selected as the universal implementation.

  ### 12.1 Mutable-current-state approach

  Concept:

  - the implementation stores or exposes an authoritative current state and
    mutates it under controlled apply;
  - history and audit are supplementary.

  Strengths:

  - direct current-state reads;
  - simple owner and conflict semantics;
  - straightforward correction and restriction of current material;
  - potentially bounded storage.

  Risks:

  - hidden overwrite;
  - weak causal lineage;
  - incomplete audit;
  - difficult reconstruction;
  - inability to explain prior decisions;
  - direct mutation bypassing accepted apply.

  Conformance conditions:

  - accepted-version lineage is preserved;
  - material corrections are attributable;
  - effect certainty survives crashes;
  - history/audit obligations declared by the pack are not lost;
  - definition/version interpretation remains available.

  Q6 conclusion:

  - viable implementation family;
  - not sufficient as architecture merely because a "current row" exists.

  ### 12.2 Event/history-derived approach

  Concept:

  - current state is reconstructed or projected from a transition/event
    history.

  Strengths:

  - rich causal trace;
  - reconstruction and branching;
  - strong historical inspection;
  - natural representation of attempts and temporal evolution.

  Risks:

  - deterministic-replay assumptions;
  - duplicate or unsafe external effects;
  - unbounded history;
  - privacy and erasure conflicts;
  - definition drift changing replay meaning;
  - event ordering or delivery being mistaken for authority;
  - projection bugs;
  - inability to remove sensitive material without breaking reconstruction.

  Conformance conditions:

  - one normative state owner still accepts the current projection;
  - events and observations do not self-authorize;
  - nondeterministic and external effects are recorded or reconciled safely;
  - historical definitions remain interpretable;
  - retention/disposition can be governed without fictionalizing history.

  Q6 conclusion:

  - viable for suitable processes;
  - unsupported as a universal substrate mandate.

  ### 12.3 Checkpoint/snapshot approach

  Concept:

  - bounded snapshots preserve resumable state at selected boundaries;
  - intervening detail can be absent, external or separately retained.

  Strengths:

  - efficient restart;
  - bounded recovery material;
  - practical carrier transfer;
  - useful creative branching;
  - reduced dependence on full replay.

  Risks:

  - stale or incomplete state;
  - omitted pending authority or obligations;
  - loss of causal history;
  - external effects after the checkpoint;
  - snapshot treated as automatically accepted;
  - incompatible definitions;
  - excessive retention of sensitive payloads.

  Conformance conditions:

  - checkpoint acceptance and integrity are explicit;
  - effect certainty is reconciled;
  - current authoritative state is revalidated;
  - pending ownership and authority are preserved;
  - omitted history is acceptable under the pack's evidence and audit policy.

  Q6 conclusion:

  - viable recovery mechanism;
  - not a universal replacement for current state, history or provenance.

  ### 12.4 Physical hybrid approach

  Concept:

  - combine current-state materialization, selected transition history,
    checkpoints and separate audit/evidence stores.

  Strengths:

  - can optimize current reads, recovery, historical explanation and
    retention independently;
  - can use different retention policies for different concerns;
  - reduces dependence on one reconstruction mechanism.

  Risks:

  - consistency and reconciliation complexity;
  - multiple apparent sources of truth;
  - duplicated sensitive material;
  - taxonomy and operational bureaucracy;
  - accidental coupling among service blocks.

  Conformance conditions:

  - one normative owner remains clear for each atomic claim;
  - duplicate material does not create duplicate authority;
  - discrepancies have an explicit reconciliation owner;
  - retention and correction propagate appropriately;
  - owner-facing operation remains useful.

  Q6 conclusion:

  - viable implementation family;
  - this research does not select it.

  ### 12.5 Cross-approach verdict

  Architecture should specify responsibility semantics and conformance
  conditions that all four families can satisfy.

  It should not infer:

  - an event store from history semantics;
  - append-only storage from lineage;
  - mutable storage from current-state authority;
  - snapshots from continuation;
  - one physical hybrid because several concerns exist.

  ## 13. Definition/version compatibility and historical interpretation

  ### 13.1 Required semantic preservation

  Historical or active material needs enough governing-definition information
  to determine:

  - which semantics and obligations applied;
  - which authority rules applied;
  - which evidence requirements applied;
  - which state transitions were valid;
  - how status and results should be interpreted;
  - whether current continuation is compatible.

  Exact version syntax and representation remain downstream.

  ### 13.2 Coexistence

  Old and new definitions can coexist when:

  - their applicable obligations are distinguishable;
  - each active obligation has an explicit compatibility disposition;
  - state owners can interpret the version governing each mutation;
  - authority and privacy remain current;
  - cross-version conversion is validated where required.

  ### 13.3 Migration

  Migration is a governed mutation, not silent reinterpretation.

  Candidate requirements:

  - known source definition;
  - known target definition;
  - compatibility or transformation assessment;
  - validation against current accepted state and policy;
  - authority where the migration changes consequences;
  - authoritative apply;
  - lineage from pre-migration to post-migration material;
  - explicit handling of lossy, conflicting or untranslatable material.

  ### 13.4 Pin and drain

  Pinning can preserve interpretation for active work under an older
  definition.

  It cannot preserve:

  - revoked disclosure permission;
  - expired action authority;
  - a mandatory safety rule that now blocks use;
  - inaccessible required sources;
  - an unsafe external-effect assumption.

  Draining closes or migrates remaining obligations before old support is
  removed.

  ### 13.5 Removal

  Definition support is removable only when:

  - no active obligation depends on it without an explicit disposition;
  - persisted accepted material remains interpretable;
  - required migration is complete;
  - required historical queries or evidence no longer depend on unavailable
    execution support, or an explicit unresolved owner remains;
  - retention and privacy policy permit the retained interpretive material.

  ### 13.6 Source disappearance

  An accepted definition cannot depend solely on an ephemeral source that can
  vanish without a failure route.

  Viable strategies can include durable accepted copies, stable immutable
  references, signed artifacts, normalized interpretation or other means.
  Q6 does not choose among them.

  The invariant candidate is:

  - accepted historical meaning and current compatibility must remain
    determinable, or the dependency must be explicitly blocked and owned.

  ## 14. Retention, restriction and privacy governance

  ### 14.1 No universal retention interval

  Retention depends on:

  - purpose;
  - consequence and safety;
  - active obligations;
  - evidence and audit requirements;
  - privacy and sharing limits;
  - legal or regulatory duties;
  - definition interpretability;
  - source availability;
  - correction and dispute status;
  - owner-wide minimization preferences;
  - recovery requirements.

  Exact intervals remain process-, jurisdiction- and implementation-specific.

  ### 14.2 Different material can have different retention treatment

  Examples:

  - current accepted state can remain while an obsolete checkpoint is pruned;
  - minimal effect evidence can remain after sensitive payload deletion;
  - audit can outlive mutable operational state where legitimate;
  - source material can be removed while a provenance relation and qualified
    conclusion remain;
  - a disputed source can be retained under restricted access;
  - derived memory can be deleted while accepted process state remains;
  - a retired definition can remain interpretable without remaining eligible
    for new activation.

  These are examples, not universal retention prescriptions.

  ### 14.3 Restriction versus erasure

  Restriction can preserve material for limited purposes while blocking
  ordinary use.

  Erasure removes applicable material, subject to legitimate exceptions and
  implementation mechanics.

  Neither operation automatically:

  - undoes external effects;
  - resolves a dispute;
  - changes historical truth;
  - authorizes retention of unrelated copies;
  - determines every downstream consumer's legal obligations.

  ### 14.4 Propagation

  When a relevant correction, restriction, revocation or erasure conclusion
  changes, known active consumers and continuations need appropriate
  propagation or revalidation.

  The exact propagation mechanism is downstream.

  ### 14.5 Minimal proof

  A process can need to preserve minimal material proving:

  - whether a consequential effect occurred;
  - which authority applied;
  - why a current state is accepted;
  - that required correction or disposition occurred;
  - which unresolved owner remains.

  The retained proof should be purpose-bound and minimized. It must not become
  a pretext for retaining complete sensitive transcripts or payloads.

  ### 14.6 Status-access privacy

  Access to status and history can itself reveal:

  - which process is active;
  - which credential or source is being checked;
  - when a person is interacting with a service;
  - which correction or dispute exists;
  - which health or personal concern is relevant.

  Retention, indexing, query and notification policy therefore apply to
  metadata as well as content.

  ## 15. Pressure tests

  ### 15.1 Health-like privacy and safety pressure

  Scenario:

  - a process previously accepted a health-related source claim;
  - a corrected source arrives;
  - some disclosure permission is revoked;
  - an external consequential action has an uncertain outcome;
  - an active continuation still refers to the prior material.

  Required behavior:

  1. The corrected claim enters validation rather than overwriting current
     state directly.
  2. The normative state owner applies a corrected accepted version when
     justified.
  3. Prior material remains identifiable as prior rather than current, subject
     to legitimate retention and restriction.
  4. Derived memories and summaries do not continue laundering the old claim.
  5. Open obligations revalidate their dependency.
  6. Revoked disclosure or use permission blocks future prohibited use,
     including use from a pinned continuation.
  7. Already applied effects remain historical facts.
  8. The uncertain external action is reconciled before retry or compensation.
  9. The portable continuation preserves only the minimum sensitive material
     needed for legitimate resume.
  10. The owner sees the material change, consequence and required decision,
      not raw audit bureaucracy.

  Verdict:

  - PASS for responsibility-separated semantics;
  - FAIL for transcript-as-state, silent overwrite, full-profile replication,
    blind replay and permanent full-history retention.

  ### 15.2 Game / productive-play creative pressure

  Scenario:

  - a creative process checkpoints an accepted canon state;
  - the owner explores an alternative branch;
  - model-generated material after the checkpoint is nondeterministic;
  - a source asset later disappears;
  - only one branch should become accepted canon.

  Required behavior:

  1. Fork creates an alternative branch without rolling back or rewriting the
     accepted branch.
  2. Post-checkpoint model or API execution is a new attempt, not guaranteed
     deterministic replay.
  3. Generated artifacts and playtest transcripts remain proposals or evidence
     until accepted through the canon/state owner.
  4. Promotion of one branch is a governed apply with lineage to its basis.
  5. Unselected drafts and checkpoints can receive lightweight retention or
     pruning treatment declared by the pack.
  6. Accepted canon decisions and consequential source provenance remain
     interpretable.
  7. Source disappearance is explicit and routes substitution, relicensing,
     blocking or owner decision.
  8. Owner-facing history is summarized around creative decisions and branch
     consequences, with deeper lineage available when useful.

  Verdict:

  - PASS for sparse, branch-aware and pack-governed persistence;
  - FAIL for every-token audit, artifact-as-canon, replay-equals-restoration
    and owner-facing state machinery.

  ## 16. Failure modes

  ### F1. Transcript as state

  Treating conversational occurrence or the latest message as accepted truth.

  Failure:

  - bypasses validation, ownership and correction;
  - carries stale or speculative material forward.

  ### F2. Artifact as proof

  Treating the existence of a file, report, screenshot or generated output as
  evidence of correctness or completed apply.

  ### F3. Event as accepted truth

  Treating an emitted or delivered event as proof that the authoritative state
  changed.

  ### F4. History, source, evidence and provenance collapse

  Using one generic "history" field without identifying what was observed,
  where it came from, which claim it supports or who accepted it.

  ### F5. Audit log as authority

  Allowing the audit collector or newest log entry to override the normative
  state owner.

  ### F6. Hidden mutation

  Directly changing durable material outside validated apply and then
  backfilling history.

  ### F7. Silent overwrite

  Replacing corrected, migrated or conflicting state without preserving
  sufficient lineage and active-work impact.

  ### F8. Lost provenance

  Copying claims, summaries or artifacts until origin, derivation and limits
  are no longer knowable.

  ### F9. Derived-memory laundering

  Promoting a model-derived summary or repeated transcript pattern into
  accepted truth without evidence and governed admission.

  ### F10. Success-only history

  Retaining only successful outcomes and losing rejected, partial, cancelled
  or uncertain attempts needed for effect reconciliation.

  ### F11. Blind retry after uncertain effect

  Repeating an external action because an acknowledgement was lost or a
  timeout occurred.

  ### F12. Universal deterministic replay

  Assuming model calls, human decisions and external APIs will reproduce the
  same result when re-executed.

  ### F13. Checkpoint as complete truth

  Restoring a snapshot without validating current authority, definition,
  external effects or later accepted mutations.

  ### F14. Restore as rollback

  Treating a prior snapshot as if later external effects and obligations never
  existed.

  ### F15. Fork as mutation

  Changing the accepted main branch merely because an exploratory branch was
  created.

  ### F16. Source disappearance breaks interpretation

  Depending on an ephemeral source so that accepted state or historical
  decisions become semantically unreadable when it vanishes.

  ### F17. Latest-definition reinterpretation

  Reading historical state under current semantics without preserving the
  definition that governed it.

  ### F18. Unsafe definition removal

  Removing old support while active obligations or stored historical material
  still depend on it.

  ### F19. Revocation as fictional rollback

  Pretending prior lawful processing or already applied effects did not occur.

  ### F20. Append-only ideology

  Refusing legitimate correction, restriction or erasure because the chosen
  history technology is treated as architecture authority.

  ### F21. Generic deletion ideology

  Erasing lineage or effect evidence needed to resolve open safety,
  accountability or compensation obligations.

  ### F22. Over-retention

  Keeping transcripts, prompts, sources, checkpoints and sensitive payloads
  indefinitely because storage is available.

  ### F23. Retention-policy flattening

  Applying one TTL or disposition rule to current state, evidence, audit,
  memory, artifacts and checkpoints despite different purposes.

  ### F24. Status metadata leakage

  Allowing history or status queries to reveal sensitive owner activity,
  disputes or health-related dependencies.

  ### F25. Owner-facing audit bureaucracy

  Exposing internal event, intake, checkpoint and handback machinery instead
  of useful progress, decisions, effects and correction routes.

  ### F26. Final service-list leakage

  Turning every semantic distinction into a mandatory repository, service or
  network hop.

  ## 17. Viable Q6 forge directions

  These are research directions. None is accepted architecture.

  ### Direction A — authoritative-current-state minimalism

  Core idea:

  - freeze one authoritative current-state owner, validated apply, minimal
    accepted-version lineage and portable continuation;
  - leave most detailed history, audit, evidence and checkpoint obligations to
    process packs.

  Useful because:

  - small invariant surface;
  - direct state authority;
  - low risk of universal audit bureaucracy;
  - broad implementation freedom.

  Bad, because:

  - weak pack declarations could leave recovery, historical interpretation and
    consequential evidence materially underspecified.

  ### Direction B — transition/history-derived continuity

  Core idea:

  - treat durable transition history as the conceptual primary basis from
    which current state and recovery are reconstructed.

  Useful because:

  - strong causality, reconstruction, branching and historical inspection.

  Bad, because:

  - it overfits event sourcing and deterministic replay, and creates
    cross-domain privacy, retention, definition-drift and external-effect
    hazards.

  ### Direction C — responsibility-separated continuity with an authoritative-state anchor

  Core idea:

  - preserve one authoritative current-state owner and validated apply;
  - separately freeze the semantic responsibilities and relationships for
    history, provenance/evidence/audit, checkpoint/recovery,
    definition/version and retention/status;
  - let packs declare consequence-specific requirements and adapters choose
    materialization.

  Useful because:

  - it preserves all supported non-equivalences;
  - effect uncertainty and recovery remain safe;
  - versioning and retention remain explicit;
  - current-state, event-derived, checkpoint and physical hybrid
    implementations can conform;
  - low-risk processes can remain lightweight.

  Bad, because:

  - without strict proportionality and atomic ownership, the distinctions can
    become a sprawling taxonomy or owner-facing ceremony.

  ### Research recommendation

  Evaluate Direction C first, with Direction A's single authoritative
  current-state owner and anti-bureaucracy discipline as mandatory internal
  constraints.

  Do not adopt Direction B as the universal answer.

  This recommendation selects a semantic responsibility arrangement, not a
  storage hybrid or final service-block list.

  ## 18. Evidence confidence

  ### High confidence

  Cross-source and parent-architecture support is strong for:

  - accepted current state versus event/history separation;
  - state authority versus observation/logging separation;
  - validated apply as the durable mutation boundary;
  - result and artifact not automatically establishing state;
  - source, evidence and provenance non-equivalence;
  - correction through lineage rather than silent overwrite;
  - external-effect uncertainty blocking blind retry;
  - deterministic replay being a specialized runtime constraint;
  - checkpoint, memory and full history non-equivalence;
  - definition coexistence, migration and drain before removal;
  - correction, restriction, revocation, retirement and erasure
    non-equivalence;
  - no universal retention interval;
  - no physical service or storage inference from semantic responsibilities.

  ### Medium-high confidence

  Research synthesis supports:

  - responsibility-separated continuity as the preferred forge direction;
  - preserving enough accepted-version lineage to explain current state;
  - explicit recovery-action distinctions;
  - historical definition interpretability as a substrate invariant;
  - active-work propagation for relevant correction, status and definition
    changes;
  - purpose-bound audit rather than exhaustive universal logging.

  ### Medium or still open

  Primary sources do not settle:

  - the exact minimum lineage needed for every accepted version;
  - the minimum universal effect evidence for low-consequence processes;
  - when audit is mandatory rather than pack-declared;
  - whether accepted current state must always be physically materialized;
  - the minimum portable-continuation content;
  - retention conflict arbitration among privacy, safety, legal, audit and
    recovery duties;
  - when a source must be copied versus stably referenced;
  - the exact historical-query compatibility contract;
  - identity and correlation semantics;
  - the final service-zone list.

  ## 19. Evidence limits

  1. No reviewed source defines the full desired operating substrate.

  2. W3C PROV is strong for provenance but does not define accepted truth,
     authority or recovery.

  3. OpenLineage is data-pipeline specific and observation-oriented.

  4. CloudEvents and OpenTelemetry define event/log representation, not
     normative state ownership or evidence sufficiency.

  5. NIST SP 800-92 is a 2006 security-log-management publication and is used
     only for high-level audit/log-governance evidence.

  6. Temporal and Durable Task are durable-workflow implementations with
     specific deterministic-history assumptions.

  7. LangGraph and Google ADK are evolving agent-framework documentation, not
     standards.

  8. Kubernetes versioning is API/storage-specific evidence rather than a
     universal process-definition model.

  9. GDPR is jurisdiction-specific law. It demonstrates governance pressure
     but cannot become universal substrate policy.

  10. W3C Bitstring Status List is credential-specific and does not provide a
      general lifecycle enum.

  11. No source proves that one physical data model is optimal across Health,
      creative work, games and general owner processes.

  12. No source proves one exact semantic category count.

  13. No live Health or game process implementation was tested.

  14. The pressure tests are architecture reasoning tests, not legal,
      security, performance or distributed-systems proofs.

  15. The research does not establish exact retention periods, deletion
      guarantees, recovery-point objectives or availability requirements.

  16. Owner-facing usefulness remains a future proof obligation; protocol or
      history completeness alone does not establish it.

  Evidence that would materially change the recommendation includes:

  - a cross-domain proof that event observations can safely establish accepted
    state without a normative state owner;
  - a universal recovery model that eliminates nondeterminism and uncertain
    external effects;
  - evidence that historical interpretation never depends on the governing
    definition/version;
  - a universal retention policy satisfying privacy, safety, audit, creative
    and legal pressures;
  - live evidence that exposing complete internal audit/history machinery is
    necessary for useful owner operation.

  ## 20. Child and downstream questions

  ### 20.1 Q6 architecture-forge must decide

  1. The accepted semantic definition of substrate-level durable continuity.
  2. Which candidate responsibilities are kernel invariants.
  3. Which concerns remain reusable-service candidates, pack declarations,
     owner-profile concerns or adapter concerns.
  4. Whether one authoritative current-state anchor is explicitly required
     even when an implementation derives state from history.
  5. The minimum accepted-version lineage obligation.
  6. The minimum effect-certainty and recovery constraints.
  7. The correction, dispute, revocation and retirement active-use rule.
  8. The definition/version historical-interpretability rule.
  9. The retention/status responsibility boundary without a universal TTL.
  10. The relation of result and continuation to durable state and history.
  11. Which forge direction the owner selects, mixes or rejects.
  12. The exact rejected alternatives and proof anchors.

  ### 20.2 Existing downstream routes

  Q8 live interface:

  - how history, correction, effect uncertainty and audit are summarized to
    the owner;
  - when deeper lineage becomes inspectable.

  Q9 result/handback:

  - exact minimum result and continuation semantics;
  - exact closure and unresolved-obligation representation.

  Q10 authority/effects:

  - authority for retry, replay, restore, compensation, disposition and
    destructive changes;
  - effect-class-specific reconciliation.

  Q11 evolution:

  - exact compatibility evidence;
  - migration and conversion semantics;
  - deprecation/removal proof;
  - historical query interpretation.

  Q12 structured communication:

  - identities, correlation, representations and protocol contracts among
    state versions, transitions, evidence, decisions, checkpoints and
    continuations.

  Q13 proof:

  - conformance scenarios for hidden mutation, duplicate effect, unknown
    outcome, replay, fork, correction, restriction, source disappearance,
    definition migration and retention.

  Q14 carrier:

  - mappings to chat, files, applications and automated transports.

  Q15 graph growth:

  - classification of any new architectural entities discovered by forge.

  ### 20.3 Additional downstream questions

  - What minimum retained proof can establish effect certainty without
    over-retaining sensitive payloads?
  - How are conflicting retention authorities ordered or escalated?
  - When is stable reference sufficient after source disappearance, and when
    must interpretive material be retained?
  - How is a lossy migration represented without freezing a schema?
  - Which audit obligations are consequence-triggered versus optional?
  - How does a process prove that no active continuation depends on a retired
    definition?
  - How are checkpoint integrity and reference accessibility validated across
    carriers?
  - How are owner correction requests propagated to derived memory and
    downstream active processes?

  ## 21. Graph, gap and forge verdict

  hidden_prerequisite: none

  Rationale:

  - Q1 defines the kernel, durable mutation and portable-continuation locks;
  - Q2 supplies the five-layer responsibility classification;
  - Q3 supplies state ownership, apply, result, effect-certainty and recovery
    distinctions;
  - Q4 supplies definition admission, compatibility, migration and pin/drain
    semantics;
  - Q5 supplies owner-context, correction, dispute, revocation, retirement and
    privacy boundaries;
  - primary sources provide sufficient cross-domain evidence to compare
    bounded Q6 directions;
  - unresolved identity, schema, implementation and proof questions already
    have downstream routes.

  gap_event: none

  graph_verdict:

  - return to the existing Q6 node;
  - no top-level cartography rebalance;
  - no Q1-Q5 revision;
  - no implementation activation;
  - next session is one bounded Q6 architecture-forge.

  ## 22. Primary-source register

  [S1] W3C, PROV-DM: The PROV Data Model,
  W3C Recommendation, 30 April 2013.
  https://www.w3.org/TR/prov-dm/

  [S2] OpenLineage Core Specification 1.50.0,
  Object Model and Run Cycle, observed 2026-07-11.
  https://openlineage.io/docs/spec/object-model/
  https://openlineage.io/docs/spec/run-cycle/

  [S3] CloudEvents Specification 1.0.2.
  https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md

  [S4] OpenTelemetry Specification 1.59.0,
  Logs Data Model, stable, observed 2026-07-11.
  https://opentelemetry.io/docs/specs/otel/logs/data-model/

  [S5] NIST SP 800-92,
  Guide to Computer Security Log Management, September 2006.
  https://csrc.nist.gov/pubs/sp/800/92/final

  [S6] Temporal Platform documentation, observed 2026-07-11:
  Event History.
  https://docs.temporal.io/workflow-execution/event
  Activity Definition and idempotency.
  https://docs.temporal.io/activity-definition
  Retry Policies.
  https://docs.temporal.io/encyclopedia/retry-policies
  Worker Versioning.
  https://docs.temporal.io/worker-versioning

  [S7] Microsoft Durable Task,
  Durable orchestrations, observed 2026-07-11.
  https://learn.microsoft.com/en-us/azure/durable-task/common/durable-task-orchestrations

  [S8] LangGraph documentation, observed 2026-07-11:
  Persistence.
  https://docs.langchain.com/oss/python/langgraph/persistence
  Time travel, replay and fork.
  https://docs.langchain.com/oss/python/langgraph/use-time-travel

  [S9] Google Agent Development Kit documentation,
  observed 2026-07-11:
  Session state.
  https://adk.dev/sessions/state/
  Memory.
  https://adk.dev/sessions/memory/

  [S10] Kubernetes documentation,
  Versions in CustomResourceDefinitions,
  page last modified 4 June 2026.
  https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/

  [S11] Regulation (EU) 2016/679, official EUR-Lex text.
  https://eur-lex.europa.eu/eli/reg/2016/679/oj

  [S12] W3C Bitstring Status List v1.0,
  W3C Recommendation, 15 May 2025.
  https://www.w3.org/TR/vc-bitstring-status-list/

  END_OF_FILE: live/solmax/work/operating-substrate-persistence-history-best-practice-research-001.md

state_changes: |
  1. CREATE
     live/solmax/work/operating-substrate-persistence-history-best-practice-research-001.md

     Content postcondition:
     - persist verbatim the research note contained in RESULT.evidence from
       "# Operating Substrate Q6 Persistence / History Best-Practice Research"
       through its END_OF_FILE marker;
     - retain status `research_input_not_architecture_decision`;
     - do not convert candidate findings into accepted architecture.

  2. UPDATE
     live/solmax/NOW.md

     Stable-target intent under `g-operating-substrate`:
     - append a `Q6 persistence/history research checkpoint` after the existing
       accepted Q5 shared-owner-context architecture checkpoint;
     - record that primary-source comparison is complete;
     - record the recommended Direction C with Direction A's authoritative
       state-owner and anti-bureaucracy constraints;
     - record that accepted current state, history, audit, evidence,
       provenance, source, memory, artifact, definition/version,
       checkpoint/recovery and retention/status remain distinct;
     - record that no universal event sourcing, replay, snapshot, mutable
       storage, schema, repository, provider, topology or final service-block
       list was selected;
     - record `hidden_prerequisite: none`;
     - record `gap_event: none`;
     - record `top-level graph rebalance: not needed`;
     - set the next route to one bounded Q6 persistence/history
       architecture-forge;
     - add the research note and next CALL path to `preserved_evidence`;
     - add the next CALL to `open_calls`.

     Preserve all Q1-Q5 checkpoints and concurrent state unchanged.

  3. CREATE
     live/solmax/work/calls/c-solmax-operating-substrate-persistence-history-architecture-forge-001.md

     Content postcondition:
     - persist verbatim the CALL carried in RESULT.next after the required
       return-to-parent marker;
     - include its END_OF_FILE marker.

  4. APPEND
     live/solmax/LOG.md

     Log intent:
     - record that bounded Q6 persistence/history primary-source research
       completed;
     - record Direction C as the research recommendation;
     - record Q6 forge readiness, no gap and no implementation selection.

  5. CREATE history closure using the repository's current history convention:
     live/solmax/history/2026-07-11-s-solmax-operating-substrate-persistence-history-best-practice-research-001.md

     Content postcondition:
     - persist this complete RESULT packet;
     - preserve source register, return-to-parent marker and next CALL.

  6. TREE.md:
     - no semantic change;
     - no top-level graph rebalance.

  7. CHARTER.md and Direction OS:
     - no change.

captures:
  - Q13 proof should include a checkpoint-before-external-effect scenario in which acknowledgement is lost and replay would duplicate the effect.
  - Q8 should test concise owner-facing correction/effect summaries against on-demand deep lineage, rather than exposing raw audit machinery.

decisions_needed: []

play_check:
  - 1 Recite: done — research play, Q6 question, bounded goal and done_when were restated before investigation.
  - 2 Investigate: done — all named parent artifacts were read to END_OF_FILE where applicable; current primary sources covered provenance, lineage, events/logs, durable recovery, version compatibility and privacy/retention.
  - 3 Confidence: done — findings were checked against all 12 CALL criteria; high-, medium- and open-confidence conclusions plus evidence limits are explicit.
  - 4 Close: done — RESULT.next begins with the required return-to-parent marker, followed by the prepared Q6 architecture-forge CALL.

log: Q6 persistence/history research complete: responsibility-separated continuity with authoritative-state anchor recommended; forge ready; no gap or implementation selected.

next: |
  return-to-parent s-solmax-operating-substrate-shared-owner-context-architecture-forge-001

  CALL c-solmax-operating-substrate-persistence-history-architecture-forge-001
  to: session
  direction: solmax
  play: local/architecture-forge
  node: g-operating-substrate
  goal: |
    One owner-approved Q6 architecture card exists for the
    persistence/history boundary: which continuity, accepted-state, lineage,
    history, audit, evidence, recovery, definition/version and retention
    responsibilities are invariant kernel semantics, reusable-service
    candidates, process-pack declarations, owner-profile concerns or
    adapter/implementation concerns, without selecting storage, schema,
    repository, carrier, runtime or implementation.

  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/plays/architecture-forge.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-process-pack-instantiation-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-shared-owner-context-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
    - live/solmax/work/operating-substrate-process-pack-instantiation-best-practice-research-001.md
    - live/solmax/work/operating-substrate-shared-owner-context-best-practice-research-001.md
    - live/solmax/work/operating-substrate-persistence-history-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

    Q6 plain question:
    "Какие persistence/history responsibilities are substrate-level, and
    what remains consumer-specific?"

    Accepted parent locks:
    - Q1-Q5 remain unchanged.
    - Operating-substrate is a stable, model-neutral and carrier-neutral
      kernel with pluggable process packs.
    - Service zones are semantic responsibility families, not physical
      services or storage blocks.
    - Atomic claims have one primary normative owner.
    - One primary normative state owner establishes each accepted durable
      version within a mutable-state boundary.
    - Query, evidence, proposal, validation, authorization, apply, result
      and continuation remain distinct.
    - Only authoritative applied outcome establishes accepted durable
      mutation.
    - Result, event, artifact, evidence and continuation do not automatically
      establish accepted truth.
    - Unknown effect outcome blocks blind retry.
    - Portable continuation preserves legitimate resume semantics.
    - Process-pack instantiation uses staged admission and activation.
    - Owner-wide admission, sharing eligibility, process-local truth and
      action authority remain distinct.
    - Correction, dispute, revocation and retirement are non-equivalent.
    - Pinning preserves interpretation but cannot preserve revoked permission
      or authority.
    - No final service-block list, storage system, schema, repository,
      carrier, provider, topology or implementation is accepted.

    Q6 research findings:
    - Durable continuity is a semantic property, not a storage model.
    - Accepted current state, transition/history, audit, evidence,
      provenance, source, memory, artifact, definition/version,
      checkpoint/recovery and retention/status need semantic separation
      without freezing exact entities.
    - Current state remains anchored in one normative state owner even when an
      implementation derives it from history.
    - History observations and audit records do not acquire state authority.
    - Correction is a governed new accepted version with lineage rather than
      silent overwrite.
    - Dispute, restriction, revocation, retirement, expiration and erasure
      have different effects on current use and history.
    - Resume, retry, replay, restore, fork, reconcile and compensation are
      non-equivalent recovery actions.
    - External-effect certainty survives timeout, cancellation, checkpoint
      and carrier change.
    - A checkpoint is insufficient when it loses accepted state, pending
      ownership, authority, effect certainty, provenance, definition
      compatibility or the next legitimate action.
    - Result closes or checkpoints an obligation; portable continuation
      preserves legitimate future ownership. Neither is automatically
      accepted state or complete history.
    - Definition evolution requires historical interpretation, compatibility,
      migration or pin/drain, and governed removal.
    - Source disappearance is an availability/status change, not proof that
      the source was false or that a derived summary became authoritative.
    - Retention requires explicit purpose, minimization, restriction and
      disposition ownership; there is no universal TTL.
    - Full event sourcing, deterministic replay, snapshots, append-only
      histories and mutable-current-state storage are viable implementation
      families in some contexts but none is universal.
    - Health-like and game/productive-play pressure tests pass under
      responsibility-separated semantics.
    - Failure modes include transcript-as-state, artifact-as-proof,
      event-as-truth, history/source/evidence collapse, hidden mutation,
      lost provenance, derived-memory laundering, unsafe replay,
      checkpoint-as-truth, definition drift, over-retention and owner-facing
      audit bureaucracy.
    - Candidate directions:
      A. authoritative-current-state minimalism;
      B. transition/history-derived continuity;
      C. responsibility-separated continuity with an authoritative-state
         anchor.
    - Research recommendation: evaluate C first while retaining A's
      single-state-owner and anti-bureaucracy constraints.
    - hidden_prerequisite: none.
    - gap_event: none.
    - top-level graph rebalance: not needed.

  boundaries: |
    Do not revise or reopen Q1, Q2, Q3, Q4 or Q5.
    Do not copy Direction OS NOW, LOG, history or RESULT surfaces into the
    substrate architecture.
    Do not copy Zaratusta workspace surfaces into substrate architecture.
    Do not define a database, event store, Git repository, filesystem,
    vector store, knowledge graph, object store or backend.
    Do not define exact state, event, history, audit, evidence, provenance,
    source, checkpoint, continuation, retention or definition schemas.
    Do not define fields, identifiers, version syntax, timestamps, retention
    intervals or exact lifecycle enums.
    Do not select event sourcing, deterministic replay, snapshots,
    append-only logs, mutable state or a physical hybrid as the universal
    implementation.
    Do not turn semantic responsibility distinctions into a final service
    block list.
    Do not define actual Health, Zaratusta, game or Direction OS state,
    history, retention or recovery policy.
    Do not define actual owner context or personal content.
    Do not select provider, model, framework, runtime, transport,
    application, topology or deployment.
    Do not implement.
    Do not change Direction OS.
    Keep Q7-Q14 downstream unless a genuine hidden prerequisite appears.

  done_when: |
    One atomic Q6 architecture card is explicitly owner-approved and:

    1. defines substrate-level durable continuity semantically without
       selecting a persistence representation;

    2. distinguishes accepted current state, transition/history, audit,
       evidence, provenance, source, memory, artifact,
       process-definition/version, checkpoint/recovery and retention/status
       without freezing exact entities;

    3. classifies responsibilities across invariant kernel semantics,
       reusable-service candidates, process-pack declarations, owner-profile
       concerns and adapter/implementation concerns;

    4. preserves one primary normative owner for each accepted durable state
       version and rejects event, audit, timestamp or last-write-wins
       authority;

    5. preserves proposal, validation, authorization, apply, result and
       continuation non-equivalence;

    6. defines the minimum candidate lineage and no-silent-overwrite rule for
       correction, dispute, revocation, retirement and migration;

    7. defines effect-certainty and recovery constraints across resume, retry,
       replay, restore, fork, reconcile and compensation without freezing a
       protocol enum;

    8. defines how result and portable continuation relate to durable state,
       history, evidence and recovery without copying Direction OS RESULT;

    9. remains neutral among mutable-current-state, event/history-derived,
       checkpoint/snapshot and physical hybrid implementations;

    10. covers definition/version compatibility, coexistence, migration,
        pin/drain, removal, source disappearance and historical
        interpretability;

    11. defines the retention/status responsibility boundary without a
        universal TTL, legal regime, schema or deletion technology;

    12. passes at least one Health-like privacy/safety pressure and one
        game/productive-play creative pressure;

    13. records rejected alternatives and failure modes including
        transcript-as-state, artifact-as-proof, hidden mutation, unsafe
        replay, over-retention and owner-facing audit bureaucracy;

    14. records the owner's direction choice and final approval words;

    15. records evidence limits, child/downstream questions, hidden
        prerequisites, graph verdict and gap_event;

    16. selects no implementation, schema, repository, carrier, provider,
        topology, consumer template or final service-block list.

  return: |
    RESULT with the owner-approved Q6 architecture card, owner direction
    choice and approval words, accepted responsibility classification,
    state/history/provenance/recovery/version/retention semantics, rejected
    alternatives, Health/game stress test, evidence limits,
    child/downstream questions, graph/gap verdict, exact state_changes and
    next graph route.

  budget: one focused session
  parent: s-solmax-operating-substrate-persistence-history-best-practice-research-001
  surface: chatgpt

  END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-persistence-history-architecture-forge-001.md

END_OF_FILE: live/solmax/history/2026-07-11-s-solmax-operating-substrate-persistence-history-best-practice-research-001.md
