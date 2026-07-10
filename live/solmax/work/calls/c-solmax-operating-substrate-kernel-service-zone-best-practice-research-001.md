CALL c-solmax-operating-substrate-kernel-service-zone-best-practice-research-001
to: session
direction: solmax
play: research
node: g-operating-substrate
goal: |
  An evidence-backed research note exists for Q2 service-zone and
  responsibility-classification design: what universal AI-process kernel
  responsibilities and boundaries are supported by current best
  practices, without freezing a final block list or choosing an
  implementation.

context: |
  Read:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-scope-boundary-001.md
  - live/solmax/work/operating-substrate/cards/operating-substrate-core-invariant-001.md
  - live/solmax/work/operating-substrate-universal-structure-cartography-001.md
  - live/solmax/knowledge/zaratusta-live-use-failure-and-operating-substrate-route.md
  - os/KERNEL.md
  - os/schema/packets.md

  Accepted Q1 locks:
  - operating-substrate is a stable, model-neutral, carrier-neutral,
    owner-tuned AI-process kernel with pluggable process packs;
  - process/domain does not modify the kernel;
  - kernel semantics include bounded runs, procedure invocation, routing,
    child/delegated work, structured communication and continuation,
    state/memory/source discipline, authority/effect boundaries,
    adapters, evidence/replay, owner interface and governed evolution;
  - every close/checkpoint must yield a portable continuation index;
  - durable mutation crosses a validated writer/apply boundary;
  - exact message schemas and writer topology remain open;
  - Markdown/chat are the current bootstrap carrier;
  - future automation must implement the semantics rather than redefine
    them.

  Research emphasis:
  - session/run/chat boundaries;
  - message and handoff semantics;
  - procedure/workflow invocation;
  - child-agent, research, executor and verifier delegation;
  - portable continuation and resumability;
  - state, memory, source, history and configuration separation;
  - durable mutation, writer/apply and validation boundaries;
  - authority and human approval;
  - tool/capability declarations and permissions;
  - observability, evidence, replay and recovery;
  - portability across newer LLMs and future application carriers.

  Compare primary-source material from multiple current approaches, such
  as OpenAI agent tooling, Anthropic agent/workflow guidance, Google ADK,
  LangGraph, MCP, Microsoft AutoGen, durable-workflow systems and other
  relevant primary architecture sources.

  Direction OS and current Solmax/Zaratusta artifacts are evidence, not
  authority.

boundaries: |
  Do not create or approve an architecture card.
  Do not freeze a final service-block list.
  Do not select a framework, provider, model, repo, backend, carrier,
  storage engine or application architecture.
  Do not implement.
  Do not copy Direction OS, OpenAI, Anthropic, LangGraph, ADK, MCP,
  AutoGen or another system as authority.
  Do not turn current product APIs or class names into substrate
  architecture.
  Do not change Direction OS kernel.
  Use current web research and primary sources.
  Separate semantic guarantees from implementation conveniences.

done_when: |
  A research artifact:
  1. compares at least five relevant current primary-source systems or
     architecture guides;
  2. identifies convergent kernel-level responsibilities and meaningful
     disagreements;
  3. distinguishes invariant kernel semantics, reusable service
     semantics, process-pack declarations, owner-profile concerns and
     adapter/implementation concerns;
  4. examines portable continuation, chat/run boundaries and
     writer/apply validation explicitly;
  5. records failure modes and premature-freeze risks;
  6. derives evidence-backed candidate classification criteria for Q2;
  7. identifies any hidden prerequisite or gap_event;
  8. preserves the accepted Q1 card and does not select implementation;
  9. returns a ready Q2 architecture-forge CALL.

return: |
  RESULT with the research artifact, primary-source evidence,
  convergent findings, disagreements, candidate Q2 classification
  criteria, gap_event if needed, exact state_changes and a ready
  service-zone/classification architecture-forge CALL.

budget: one focused session
parent: s-solmax-operating-substrate-core-invariant-architecture-forge-001
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-solmax-operating-substrate-kernel-service-zone-best-practice-research-001.md
