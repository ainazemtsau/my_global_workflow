# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_owner-boundary-repaired_pending_converge-verify

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
  No implementation resumes until converge-verify checks the repaired WHAT surface.
  The previous converge-verify PASS is stale because G10/W8/W17/W20-A12 and dependent
  acceptance semantics changed after owner clarification.

  Repaired model:
  - no generic domain/topic blacklist;
  - topic work is allowed through the right process and loaded source context;
  - hard boundaries are source integrity, owner approval, state ownership and side-effect
    safety;
  - Direction OS and other repos/directions/projects remain read-only sources by default;
  - Zaratusta writes only to its own workspace/repo by default;
  - W19 HOW firewall remains intact except for the owner-clarified first-layer constraint:
    Markdown/GitHub-readable source/process/owner-context/context-loading/examples/tests,
    with no DB/API/engine/scheduler/automation now.

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
  id: c-zara-operate-contract-converge-verify-owner-boundary-002
  to: session
  direction: solmax
  play: converge-verify
  node: g-zara-operate-contract
  goal: |
    Verify the repaired operating-manager authority WHAT after owner-boundary repair.
    The verification must attack whether the repaired G10/W8/W17/W20-A12 and dependent
    rows are forward-clean, backward-clean and shape-copyable without reintroducing a
    domain blacklist or smuggling implementation HOW.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-owner-boundary-002.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-shape-001.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    Prior converge-verify passed before owner clarification, but shape then exposed a
    contradiction. The repaired WHAT must now be verified against the owner-approved model:
    the manager is topic-open and works through process/source/context; writes default only
    to Zaratusta workspace/repo; other repos/directions/projects are read-only sources;
    any future non-Zaratusta write requires explicit narrow integration/procedure.

    Specific repair surface to attack:
    - G10 now means process/source/workspace model, not forbidden prescription zone.
    - W8 ET3 now blocks effects that lack source/approval/integration/side-effect safety;
      it is not a domain-forbidden list.
    - W17 now handles high-stakes/source-owned topics by process/source/context routing,
      not topic refusal.
    - W20/A1-A13 is replaced with a shape-copyable acceptance surface for source registry,
      process registry, context loading, owner-context structure, examples/tests,
      review/mutation route and write-boundary semantics.
    - W2/W5/W6/W7/W10/W12/W13/W15/W16/W19 were adjusted only where dependent on the old model.
  boundaries: |
    Do not implement or modify the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not copy LifeReset wholesale.
    Do not treat the previous converge-verify PASS as still valid for repaired rows.
    Do not reintroduce a broad domain blacklist under a different name.
    Do not remove the Direction OS / other-repo read-only boundary unless owner explicitly
    changes it.
    Do not choose UI, storage engine, database, exact schema, exact cadence, scoring,
    automation or scheduler.
  done_when: |
    Verification explicitly attacks complete/backward-clean/forward-clean/smuggling for
    the repaired G10/W8/W17/W20-A12 and dependent rows.
    Verdict is PASS with no row failures and next routes to shape, or FAIL with exact rows
    reopened / exact owner decision needed.
    The verifier specifically checks that W20/A1-A13 can be copied by shape without
    contradicting the owner clarification.
  return: |
    RESULT with verification verdict, row failures if any, state_changes for work/NOW/LOG/history,
    and next route to shape if PASS or converge/awaiting_decision if FAIL.
  budget: one converge-verify session

END_OF_FILE: live/solmax/NOW.md
