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
