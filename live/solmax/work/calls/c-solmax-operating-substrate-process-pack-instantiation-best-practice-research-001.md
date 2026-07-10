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
