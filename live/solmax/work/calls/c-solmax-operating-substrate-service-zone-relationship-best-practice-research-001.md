CALL c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001
to: session
direction: solmax
play: research
node: g-operating-substrate
goal: |
  One bounded primary-source research note exists for Q3: which
  implementation-neutral relationship and responsibility-flow
  semantics can connect candidate service zones end-to-end while
  preserving accepted Q1/Q2 and without choosing transport, message
  schema, orchestration topology or a final service-block list.
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
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md

  Accepted locks:
  - operating-substrate is a stable, model-neutral, carrier-neutral
    kernel with pluggable process packs;
  - process/domain does not modify kernel semantics;
  - service zones are semantic responsibility families, not physical
    deployment blocks;
  - atomic responsibilities are classified independently;
  - portable continuation is mandatory but its schema is open;
  - durable mutation crosses a logical validated writer/apply boundary
    while physical topology remains open;
  - no final service-block list is accepted.

  Q3 research orientation:
  - investigate stable relationship meanings such as invocation,
    delegation, read/query, proposal, validation/apply, event/evidence,
    result, handoff, continuation and owner decision;
  - investigate responsibility, authority and state ownership across
    boundaries;
  - investigate failure, retry, cancellation, unresolved ownership and
    recovery;
  - distinguish semantic relationship types from API calls, queues,
    event buses, graphs and agent topology;
  - test whether an end-to-end owner-facing process flow can remain
    coherent without every zone communicating with every other zone.
boundaries: |
  Do not forge or approve the Q3 architecture answer.
  Do not freeze a final service-zone or service-block list.
  Do not design message schemas, APIs, event buses, queues, graph
  runtimes, schedulers or orchestration topology.
  Do not select a framework, provider, model, repository, backend,
  carrier, storage engine, transport, deployment or application.
  Do not implement.
  Do not revise Q1 or Q2.
  Do not copy Direction OS CALL/RESULT or current framework objects as
  universal protocol.
done_when: |
  A bounded research note:

  1. compares relevant primary sources;
  2. identifies convergent and conflicting semantic relationship
     patterns;
  3. proposes an implementation-neutral candidate relationship
     taxonomy for Q3 evaluation;
  4. distinguishes responsibility flow from transport and topology;
  5. covers authority, state ownership, failure, cancellation,
     unresolved ownership, recovery and continuation;
  6. stress-tests at least one end-to-end flow from intake through
     procedure/effect/result/continuation;
  7. records evidence limits, premature-freeze risks, downstream
     questions and gap_event;
  8. returns a bounded Q3 forge handoff if Q3 is ready.
return: |
  RESULT with the research note, primary-source comparison, candidate
  Q3 taxonomy, stress-test verdict, graph/gap verdict, exact
  state_changes and the next architecture-forge CALL if ready.
budget: one focused session
parent: s-solmax-operating-substrate-service-zone-classification-architecture-forge-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-service-zone-relationship-best-practice-research-001.md
