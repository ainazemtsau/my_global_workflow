outcome:
  status: completed
  session: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
  call: c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
  direction: solmax
  node: g-operating-substrate
  play: local/architecture-forge

  accepted_card:
    card_id: operating-substrate-service-zone-relationship-001
    path: live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
    graph_nodes:
      - q03_service_zone_relationships
    status: accepted
    accepted_at: 2026-07-10
    owner_choice: "A"
    owner_approval_words: "Approve v1"

    frozen_answer_summary: |
      Operating-substrate uses a bounded implementation-neutral semantic
      relationship algebra between responsibility-bearing roles.

      The accepted model has five relationship families and twelve primary
      semantic kinds:

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

      Acceptance, refusal, input-required, progress, waiting, failure,
      cancellation, retry and recovery are shared lifecycle semantics attached
      to an underlying open obligation. They are not a required flat catalogue
      of top-level messages.

      Every open obligation has one primary current next-action owner. Delegation
      gives a delegate bounded child execution ownership while the delegator
      retains parent integration, outcome accountability and owner-facing
      closure. Handoff changes active next-step ownership only after the
      successor accepts the bounded transfer.

      Query, proposal, validation, authorization, apply and event remain
      semantically non-equivalent even when one implementation combines their
      execution. Capability does not imply authority. Human effect authority
      and authoritative mutable-state ownership do not transfer implicitly
      through invoke, delegate, handoff, event or evidence.

      Cancellation request is not proof of cessation. Timeout is not proof that
      an effect did not occur. Unknown effect outcome blocks blind retry until
      authoritative reconciliation or independent retry-safety evidence exists.

      Result settles or checkpoints an obligation and identifies unresolved
      work and its owners. Portable continuation preserves accepted state,
      ownership, authority, effect certainty, evidence and the next legitimate
      route without requiring one runtime identifier or carrier.

      Logical adjacency is sparse: relationships are required where obligation,
      authority, state access, evidence or closure requires them. All-to-all
      communication and a permanent central physical orchestrator are not
      required.

  stress_test:
    status: PASS
    scenario: |
      Human intake was carried through owner-facing work ownership, procedure
      invocation, authoritative query, bounded child delegation, proposal,
      validation, owner decision, authoritative apply, result integration and
      portable continuation.

      Failure branches covered child timeout, cancellation before apply,
      uncertain apply outcome, duplicate apply delivery and carrier switch
      after authorization but before effect.
    verdict: |
      Ownership, authority and effect status remain coherent without requiring
      every candidate zone to communicate with every other zone and without
      choosing a central physical orchestrator, transport or final zone list.

  graph_verdict:
    hidden_prerequisite: none
    gap_event: none
    top_level_rebalance: not_needed
    return_to_cartography: not_required
    implementation_activation: prohibited
    next_graph_node: q04_process_pack_instantiation
    next_route: bounded best-practice/comparable-system research before Q4 forge

evidence:
  - done_when: 1
    proof: |
      The accepted card defines semantic relationship as a typed normative and
      causal relation over bounded obligations, state, effects, claims, results
      or continuation, explicitly separate from message, API, transport,
      graph edge and physical topology.

  - done_when: 2
    proof: |
      Five bounded families and twelve primary semantic kinds are frozen.
      Their names do not prescribe packet types, endpoints, agents, services
      or deployment blocks.

  - done_when: 3
    proof: |
      Invoke opens a requested obligation; delegate transfers bounded child
      execution while parent integration/accountability remains; handoff
      transfers active next-step ownership only after successor acceptance.

  - done_when: 4
    proof: |
      Query, proposal, validation, owner decision/authorization, apply/effect
      and event have separate ownership, authority, state-effect and closure
      meanings.

  - done_when: 5
    proof: |
      Event reports an occurrence; evidence supports or refutes a claim;
      artifact is addressable output; result settles/checkpoints an obligation;
      continuation preserves legitimate resumability.

  - done_when: 6
    proof: |
      One primary current next-action owner is required for each open
      obligation. Waiting retains a containing work owner; awaited input or
      decision has a named bounded owner. Handoff has no ownerless interval.

  - done_when: 7
    proof: |
      One primary normative state owner establishes each accepted durable
      version of a mutable boundary. Human effect authority does not transfer
      implicitly through capability, delegation, handoff, event or evidence.

  - done_when: 8
    proof: |
      The card distinguishes refusal, input-required, known-not-done, partial
      effect, completed effect with lost acknowledgement, unknown outcome,
      cancellation request, effective cancellation, retryability, recovery,
      compensation and unresolved ownership.

  - done_when: 9
    proof: |
      Result and portable-continuation obligations are frozen semantically while
      exact entities, fields, identifiers, encoding and serialization remain
      downstream.

  - done_when: 10
    proof: |
      The owner-facing intake-through-procedure/effect/result/continuation
      stress test passes with sparse responsibility adjacency.

  - done_when: 11
    proof: |
      Rejected alternatives, evidence limits, downstream and child questions,
      stress-test branches and explicit graph/gap verdict are recorded.

  - done_when: 12
    proof: |
      Q1/Q2 remain unchanged. No framework, message schema, transport,
      orchestration topology, physical writer or final service-block list is
      selected.

  source_anchors:
    - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
    - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
    - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
    - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
    - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
    - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
    - 'owner diverge choice in chat: "A"'
    - 'owner freeze approval in chat: "Approve v1"'

state_changes:
  - operation: create
    path: live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
    content: |
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

  - operation: update
    path: live/solmax/NOW.md
    exact_changes:
      - replace:
          from: "route_status: operating_substrate_q3_relationship_research_ready_for_forge"
          to: "route_status: operating_substrate_q3_relationship_card_accepted_q4_instantiation_research_ready"

      - append_under: owner_directive
        after_current_q3_research_checkpoint: |
          Q3 service-zone relationship architecture card:
          - Owner selected direction A.
          - Owner approved operating-substrate-service-zone-relationship-001.
          - Owner words: "Approve v1".
          - Frozen semantic model has five families and twelve primary kinds:
            invoke, delegate, handoff; query, observe/event,
            evidence/provenance; propose, validate, decide/authorize,
            apply/effect; return/result; continue.
          - Acceptance, refusal, input-required, progress, waiting, failure,
            cancellation, retry and recovery are shared lifecycle semantics of
            open obligations rather than a mandatory flat message catalogue.
          - Every open obligation has one primary current next-action owner.
            Waiting is not ownerless; predecessor retains ownership until an
            accepted handoff; delegation retains parent integration and
            accountability.
          - One primary normative state owner establishes each accepted durable
            version. Capability, delegation, handoff, event and evidence do not
            implicitly transfer human authority or state ownership.
          - Cancellation request is not proof of stop. Timeout is not proof
            that an effect did not occur. Unknown effect outcome blocks blind
            retry pending reconciliation or independent retry-safety evidence.
          - Event, evidence, artifact, result and continuation are distinct.
          - Sparse logical responsibility flow passed the intake-through-
            procedure/effect/result/continuation stress test without requiring
            all-to-all communication or a central physical orchestrator.
          - No entity/message schema, transport, orchestration topology,
            physical writer or final service-block list was selected.
          - gap_event: none. Top-level graph rebalance: not needed.
          - Next route is bounded Q4 best-practice/comparable-system research
            on process-pack instantiation and adaptation.

      - append_to: preserved_evidence
        values:
          - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
          - live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md
          - 'owner choice in chat: "A"'
          - 'owner approval in chat: "Approve v1"'
          - live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md

      - replace:
          from: "next: work/calls/c-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md"
          to: "next: work/calls/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md"

  - operation: create
    path: live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md
    content: |
      CALL c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001
      to: session
      direction: solmax
      play: research
      node: g-operating-substrate
      goal: |
        A bounded implementation-neutral research note gives Q4 architecture
        forge enough evidence to decide how a new domain/process instantiates
        the accepted universal kernel and reusable service semantics through a
        process pack, without reinventing common mechanisms or freezing a
        configuration schema, implementation, carrier or consumer template.
      context: |
        Read:
        - live/solmax/CHARTER.md
        - live/solmax/TREE.md
        - live/solmax/NOW.md
        - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
        - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
        - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-classification-001.md
        - live/solmax/work/operating-substrate/cards/operating-substrate-service-zone-relationship-001.md
        - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
        - live/solmax/work/operating-substrate-kernel-service-zone-best-practice-research-001.md
        - live/solmax/work/operating-substrate-service-zone-relationship-best-practice-research-001.md
        - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

        Accepted locks:
        - operating-substrate is a stable, model-neutral and carrier-neutral
          kernel with pluggable process packs;
        - a process/domain does not modify kernel semantics;
        - service zones are semantic responsibility families, not physical
          deployment blocks;
        - atomic responsibility claims have one primary normative owner;
        - Q3 freezes five semantic relationship families and twelve primary
          kinds plus shared lifecycle and ownership invariants;
        - portable continuation is mandatory while exact schema remains open;
        - durable mutation crosses a logical validated writer/apply boundary;
        - no final service-block list, implementation or physical topology is
          accepted.

        Q4 cartography handoff:
        - plain_question: "Как новый domain/process instantiates the universal
          structure without reinventing common service layers?"
        - why_it_matters: "If every process rewrites the structure, substrate
          fails; if substrate dictates local policy, it overreaches."
        - answer_shape: scenario_grammar
        - must_eventually_decide: "What is inherited, declared, locally owned,
          bound, validated, versioned and checked at process-pack
          instantiation."
        - must_not_decide: "Actual Health/Zaratusta/game configurations,
          config/entity schema, UI, repository, storage, runtime, framework,
          provider or deployment."
        - return_to_graph_if: "A process-pack boundary cannot support at least
          two materially different process pressures without copying one
          consumer into another or modifying kernel semantics."

        Research orientation:
        - compare primary-source approaches to extension packages, workflows,
          capability declarations, policy/config overlays, compatibility and
          validation;
        - include materially different process pressures, not only agent
          frameworks;
        - distinguish inherited kernel guarantees from required pack
          declarations, optional reusable services, owner-profile inputs and
          adapter bindings;
        - investigate failure, compatibility, missing-capability and
          invalid-pack behavior;
        - preserve semantic relationships accepted in Q3;
        - treat current Zaratusta and Direction OS artifacts as evidence, not
          authority.
      boundaries: |
        Do not approve or draft the Q4 architecture card.
        Do not revise Q1, Q2 or Q3.
        Do not freeze a final service-zone or service-block list.
        Do not define a configuration, entity, message or continuation schema.
        Do not select a repository, storage system, runtime, framework,
        provider, transport, orchestration topology or deployment.
        Do not define actual Health, Zaratusta, game or Direction OS process
        packs.
        Do not turn current framework package/plugin names into universal
        substrate entities.
        Do not implement.
        Do not change Direction OS.
      done_when: |
        The research note:

        1. compares relevant primary-source architecture approaches for process
           definition, extension/pack installation, inherited guarantees,
           configuration, capability declaration, validation and
           compatibility;
        2. distinguishes kernel-inherited semantics, reusable-service bindings,
           required process-pack declarations, owner-profile inputs and
           adapter/implementation bindings;
        3. identifies what an instantiation must establish semantically without
           defining packet/config fields;
        4. covers missing capabilities, invalid or conflicting declarations,
           incompatible versions, partial installation, failed validation,
           migration/recovery and pack removal/replacement;
        5. tests the candidate boundary against at least two materially
           different process pressures;
        6. offers 2-3 bounded Q4 architecture directions with tradeoffs and a
           recommendation;
        7. records evidence limits, downstream questions, hidden prerequisites,
           graph verdict and gap_event;
        8. selects no implementation, schema, carrier, topology or final block
           list.
      return: |
        RESULT with the research note, primary-source register, comparative
        findings, candidate Q4 answer directions, process-pressure stress test,
        evidence limits, forge handoff, graph/gap verdict, exact state_changes
        and next route.
      budget: one focused session
      parent: s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001
      surface: chatgpt

      END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md

  - operation: append
    path: live/solmax/LOG.md
    line: |
      2026-07-10 — Q3 semantic service-zone relationship architecture accepted:
      owner chose A and approved v1; five-family/twelve-kind responsibility
      model and lifecycle/ownership invariants frozen; sparse flow PASS;
      gap none; routed to Q4 process-pack instantiation research.

  - operation: create
    path: live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md
    content_rule: |
      Store this final session packet verbatim as the append-only history
      record, including owner choice "A", owner approval "Approve v1", accepted
      card, evidence, exact state changes, play check and next route.

  - operation: no_change
    path: live/solmax/TREE.md
    reason: |
      Q3 closes an architecture card inside the existing
      g-operating-substrate route. No TREE outcome, status or structure change
      is required.

captures: []

decisions_needed: []

rejected_alternatives:
  - option: B — facets-only normative grammar
    verdict: rejected_as_primary
    reason: |
      It preserves flexibility but leaves canonical conformance and
      interoperability too ambiguous. Its semantic facets are retained inside
      option A.

  - option: C — expanded communicative-act catalogue
    verdict: rejected
    reason: |
      It turns lifecycle transitions into packet-like top-level acts, causes
      taxonomy proliferation and obscures the underlying open obligation.

  - option: one_generic_relation_with_attributes
    verdict: rejected
    reason: |
      Critical distinctions such as delegation/handoff,
      proposal/apply and event/command could become optional metadata.

  - option: relationship_equals_message_api_or_graph_edge
    verdict: rejected
    reason: |
      Representation, delivery and configured reachability do not establish
      normative responsibility, authority, state effect or closure.

  - option: permanent_central_orchestrator_or_all_to_all_graph
    verdict: rejected
    reason: |
      Per-obligation integration ownership and sparse semantic adjacency are
      sufficient; physical topology remains open.

downstream_questions:
  - q04_process_pack_instantiation_and_adaptation
  - q06_state_history_ownership_and_conflict
  - q07_routing_and_relationship_target_selection
  - q08_owner_facing_progress_decision_and_interruption
  - q09_result_and_portable_continuation_minimum
  - q10_authority_effect_classes_and_gates
  - q11_definition_evolution_compatibility_and_recovery
  - q12_entity_identity_correlation_and_protocol_representation
  - q13_relationship_conformance_and_live_use_proof
  - q14_carrier_mapping

child_questions:
  - |
    What are the exact relationships among logical obligation, durable work
    item, invocation and execution attempt?
  - |
    How is successor acceptance established and ambiguous handoff reconciled
    without freezing transport?
  - |
    What semantic operation identity is sufficient for retry reconciliation
    and deduplication?
  - |
    How does one normative state owner relate to several physical writers or
    replicas?
  - |
    Which effect classes require compensation and which support genuine
    reversal?
  - |
    How does continuation establish compatibility with changed procedure or
    process-pack definitions?

play_check:
  - step: 1. Frame
    status: done
    evidence: |
      Exact Q3 question, Q1/Q2 parent locks, must-decide, must-not-decide and
      readiness were presented before divergence.

  - step: 2. Diverge (owner)
    status: done
    owner_words: "A"
    evidence: |
      Three viable directions were presented with bad-because tradeoffs and a
      recommendation. The owner selected option A.

  - step: 3. Draft
    status: done
    evidence: |
      One atomic Q3 architecture card v1 was drafted with invariant answer,
      boundaries, rejected alternatives, evidence limits, downstream questions
      and proof anchors.

  - step: 4. Gate
    status: done
    evidence: |
      Draft passed parent-lock, no-HOW, no-schema, no-transport,
      no-topology, no-final-block-list and owner-facing sparse-flow checks.

  - step: 5. Freeze & grow (owner)
    status: done
    owner_words: "Approve v1"
    evidence: |
      Owner explicitly approved the final card. Rejected alternatives, child
      questions and graph/gap verdict are recorded.

  - step: 6. Close & route
    status: done
    evidence: |
      No implementation was activated. The next route is a bounded Q4
      process-pack instantiation/adaptation research call before architecture
      forge.

log: |
  Q3 semantic relationship architecture accepted under owner choice A and
  approval "Approve v1"; sparse responsibility flow passed; no gap or graph
  rebalance; next Q4 instantiation research.

next:
  status: ready
  call_id: c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001
  path: live/solmax/work/calls/c-solmax-operating-substrate-process-pack-instantiation-best-practice-research-001.md
  route: |
    Research implementation-neutral process-pack instantiation and adaptation
    semantics, then return to local/architecture-forge for one Q4 card.

END_OF_FILE: live/solmax/history/2026-07-10-s-solmax-operating-substrate-service-zone-relationship-architecture-forge-001.md
