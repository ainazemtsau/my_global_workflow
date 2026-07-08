CALL c-solmax-operating-substrate-structure-discovery-architecture-forge-001
to: session
direction: solmax
play: local/architecture-forge
node: g-operating-substrate
goal: |
  One owner-approved architecture/spec card defines how the operating
  substrate discovers/designs the needed structure of a custom AI-process
  without pre-freezing generic components as authority.
context: |
  Parent approved card:
  - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md

  Owner approval words:
  - "Approve v2"

  Owner correction preserved:
  - "не факт, что такая структура будет"
  - "мы должны определить эту структуру саму ещё, что надо, что не надо"
  - "Нам нужна абстрактная вещь"
  - "Я не хочу, чтобы он становился авторитетным в какую-то структуру"
  - "Должно всё быть рассмотрено, должна структура быть построена, как она будет работать, почему она будет работать, какие доказательства, что это работает"
  - "какая-то тестовую среду нам сделать так, чтобы понемногу понимать, что мы структуру, которую делаем, она работает"

  Frozen parent scope:
  - Operating-substrate is for abstract customizable AI-process construction.
  - It is not only owner/project processes.
  - It is not only Zaratusta-like systems.
  - It is not a generic all-AI framework.
  - It is not a pre-frozen component list.

  Frozen parent boundary:
  - Substrate may define reusable ways to discover, reason about, test and
    evolve process structures across domains.
  - Concrete process structure remains consumer-specific unless later
    promoted by an owner-approved card with proof/research anchors.
  - Candidate elements such as state, history, procedures, source/evidence
    and tests are investigation areas, not accepted substrate structure.

  Sources:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
  - live/solmax/work/operating-substrate-scope-boundary-cartography-001.md
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
  - any owner-provided Health-like process context if available in-session
boundaries: |
  Do not design the full operating substrate.
  Do not freeze a final state/history/procedure/source/evidence schema.
  Do not create implementation code.
  Do not create a detailed test harness.
  Do not select or create a substrate product repo.
  Do not change Direction OS kernel.
  Do not copy Health, Zaratusta or Direction OS artifacts as authority.
  Use examples only to compare repeated problems and candidate structure needs.
done_when: |
  One owner-approved architecture/spec card exists for structure-discovery
  only: it defines how to determine what structure a custom AI-process
  needs, what evidence is sufficient to promote candidate components, and
  what remains consumer-specific. No final process structure, schema,
  procedure catalogue, proof harness, carrier/backend or repo is frozen.
return: |
  RESULT with the accepted structure-discovery architecture card, owner
  approval evidence, exact state_changes, rejected alternatives,
  downstream questions, gap_event if blocked, and next CALL.
budget: one focused session
parent: s-solmax-operating-substrate-scope-boundary-architecture-forge-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-structure-discovery-architecture-forge-001.md
