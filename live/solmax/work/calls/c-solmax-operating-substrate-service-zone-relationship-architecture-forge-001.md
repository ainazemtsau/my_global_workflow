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
