# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_trace_repaired_pending_converge_verify

owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
  personal operating-manager capability becomes the real Personal Operating System phase
  of Zaratusta, not a PoC and not a separate LifeReset project.

  The owner approved option A on 2026-06-26: g-zara-operate is split into four child
  outcomes:
  - g-zara-operate-contract
  - g-zara-operate-state
  - g-zara-operate-runtime
  - g-zara-operate-evolution

  First child remains g-zara-operate-contract. Shape bounced it back to converge, and
  converge repaired the authority WHAT rows that had encoded the wrong forbidden-domain /
  blacklist model.

  Preserved owner clarification:
  - Zaratusta manager should not be defined by broad domain prohibitions.
  - The manager may work on any owner-requested domain/topic through the right process
    and source context.
  - The hard boundary is write ownership and side effects: Zaratusta manager writes only
    to its own Zaratusta workspace/repo by default.
  - Other repos/directions/projects are read-only sources by default.
  - Future write access to another system requires an explicit narrow integration/procedure.
  - First implementation layer should be Markdown/GitHub-readable: source registry,
    process registry, owner-context structure, context-loading procedure and examples/tests;
    no DB/API/engine/scheduler/automation now.
  - Deep research is a first-class process/route for creating or improving processes when
    external evidence is needed.

blocked_reason: |
  No implementation resumes until converge-verify validates the 2026-06-28 trace repair.

  Converge trace repair result:
  - W2 acceptance invalid glossary trace repaired by retargeting to valid G2/G3/G11 properties.
  - W6 answer invalid glossary trace repaired by retargeting to valid G9/G10 properties.
  - W13 answer invalid glossary trace repaired by retargeting to valid G9/G10 properties.
  - W17 answer invalid glossary trace repaired by retargeting to valid G9 properties while
    retaining the already-valid G10[source-backed] trace.

  Preserve:
  - no generic domain/topic blacklist;
  - topic work is allowed through process/source/context;
  - Direction OS and other repos/directions/projects are read-only sources by default;
  - Zaratusta writes only to its own workspace/repo by default;
  - future non-Zaratusta writes require explicit narrow integration/procedure;
  - W19 HOW firewall and GitHub/Markdown-readable first-layer constraint;
  - W20/A1-A13 shape-copyable acceptance surface.

tasks: []
recurring: []
decisions: []
open_calls: []

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/LOG.md
  - live/solmax/work/converge-g-zara-operate-contract.md
  - live/solmax/history/2026-06-25-s-zara-remap-001.md
  - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
  - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-operate-contract-converge-verify-trace-repair-004
  to: session
  direction: solmax
  play: converge-verify
  node: g-zara-operate-contract
  goal: |
    Verify the repaired g-zara-operate-contract WHAT after trace/copyability repair of
    W2/W6/W13/W17. The verification must confirm that active WHAT rows no longer cite
    missing §GLOSSARY properties and that W20/A1-A13 remains shape-copyable, topic-open
    and HOW-clean.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
    - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
    - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md

    Prior owner-boundary verify found complete=PASS and backward_clean=PASS, and found no
    substantive owner-boundary contradiction, no generic domain/topic blacklist and no hidden
    HOW in W20/A1-A13. It failed only because W2/W6/W13/W17 cited missing glossary properties.

    Trace repair performed:
    - W2 acceptance: replaced missing G2[explainable] with valid G2[bounded],
      G3[auditable] and G11[auditable].
    - W6 answer: replaced missing G9[source-backed] with valid G9[read-not-own]
      and G10[source-backed].
    - W13 answer: replaced missing G9[source-backed] with valid G9[context-loaded]
      and G10[source-backed].
    - W17 answer: replaced missing G9[source-backed] with valid G9[read-not-own]
      and G9[context-loaded], retaining valid G10[source-backed].

    Preserve during verification:
    - no generic domain/topic blacklist;
    - topic work is allowed through process/source/context;
    - Direction OS and other repos/directions/projects are read-only sources by default;
    - Zaratusta writes only to its own workspace/repo by default;
    - future non-Zaratusta writes require explicit narrow integration/procedure;
    - W19 HOW firewall and GitHub/Markdown-readable first-layer constraint;
    - W20/A1-A13 substance unless verification finds a new exact defect.
  boundaries: |
    Do not reintroduce a generic domain/topic blacklist.
    Do not change the owner-approved rule that the manager may work on any owner-requested
    topic through the right process and source context.
    Do not weaken the write boundary: Zaratusta writes only to its own workspace/repo by
    default; other repos/directions/projects remain read-only sources by default; future
    writes elsewhere require explicit narrow integration/procedure.
    Do not choose UI, storage engine, database, exact schema, exact cadence, scoring,
    automation, scheduler, vendor, framework or API/subscription adapter.
    Do not implement or modify the product repository.
  done_when: |
    Verification explicitly attacks complete/backward-clean/forward-clean/smuggling after
    the trace repair. Verdict is PASS with no row failures and next routes to shape, or FAIL
    with exact rows reopened / exact owner decision needed. The verifier specifically checks
    that W2/W6/W13/W17 no longer contain invalid glossary property references and that
    W20/A1-A13 can be copied by shape without contradicting owner-boundary clarification.
  return: |
    RESULT with verification verdict, row failures if any, state_changes for work/NOW/LOG/history,
    and next route to shape if PASS or converge/awaiting_decision if FAIL.
  budget: one converge-verify session

END_OF_FILE: live/solmax/NOW.md
