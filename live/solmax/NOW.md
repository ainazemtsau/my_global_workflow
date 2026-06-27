# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_converge_verify_failed_trace_repair_needed

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
  No implementation resumes until converge repairs the trace/copyability failures found by
  converge-verify after the owner-boundary repair.

  Verification result:
  - complete=PASS
  - backward_clean=PASS
  - forward_clean=FAIL
  - smuggling=FAIL

  Rows to reopen for trace repair only:
  - W2 acceptance: invalid `→GLOSSARY:G2[explainable]`
  - W6 answer: invalid `→GLOSSARY:G9[source-backed]`
  - W13 answer: invalid `→GLOSSARY:G9[source-backed]`
  - W17 answer: invalid `→GLOSSARY:G9[source-backed]`

  Preserve:
  - no generic domain/topic blacklist;
  - topic work is allowed through process/source/context;
  - Direction OS and other repos/directions/projects are read-only sources by default;
  - Zaratusta writes only to its own workspace/repo by default;
  - future non-Zaratusta writes require explicit narrow integration/procedure;
  - W19 HOW firewall and GitHub/Markdown-readable first-layer constraint.

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
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-operate-contract-converge-trace-repair-003
  to: session
  direction: solmax
  play: converge
  node: g-zara-operate-contract
  goal: |
    Repair the trace/copyability failures found by converge-verify after the owner-boundary
    repair, without changing the owner-approved process/source/workspace authority model.
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

    Converge-verify found no substantive owner-boundary contradiction, no domain blacklist
    reintroduced, and no hidden HOW in W20/A1-A13. It failed only because four rows cite
    glossary properties that do not exist in the current §GLOSSARY:

    - W2 acceptance: `→GLOSSARY:G2[explainable]`; current G2 has `[bounded]`,
      `[process-routed]`, `[source-backed]`, `[override-safe]`, `[no-hidden-power]`.
    - W6 answer: `→GLOSSARY:G9[source-backed]`; current G9 has `[read-not-own]`,
      `[no-scope-capture]`, `[context-loaded]`, `[integration-explicit]`.
    - W13 answer: `→GLOSSARY:G9[source-backed]`; same invalid property.
    - W17 answer: `→GLOSSARY:G9[source-backed]`; same invalid property, though W17 also
      cites valid `→GLOSSARY:G10[source-backed]`.

    Repair should make the traces valid by retargeting to existing resolved glossary
    properties or by adding explicit resolved properties if converge determines they are
    load-bearing. Then route back to converge-verify.
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
    W2/W6/W13/W17 no longer contain invalid glossary property references; every
    load-bearing value traces to a valid §GLOSSARY property, §WHAT row, source or frozen
    canon id. W20/A1-A13 remains shape-copyable, topic-open and HOW-clean. The repaired
    WHAT routes back to converge-verify.
  return: |
    RESULT with exact row repairs, evidence that all invalid traces are fixed, state_changes
    for work/NOW/LOG/history, and next route back to converge-verify.
  budget: one converge session

END_OF_FILE: live/solmax/NOW.md
