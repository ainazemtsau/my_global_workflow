# NOW — solmax

project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: g-zara-operate-contract_converged_pending_verify

owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the
  LifeReset-derived personal operating-manager capability becomes the
  real Personal Operating System phase of Zaratusta, not a PoC and not a
  separate LifeReset project.

  The owner approved option A on 2026-06-26: g-zara-operate is split into
  four child outcomes:
  - g-zara-operate-contract
  - g-zara-operate-state
  - g-zara-operate-runtime
  - g-zara-operate-evolution

  First child to converge: g-zara-operate-contract.

blocked_reason: |
  No implementation resumes until the first child has cleared converge
  and converge-verify. Manager authority, entity model, horizon model,
  escalation/effect-tier boundaries and forbidden prescription zones are
  load-bearing unknowns and must not be guessed during implementation.

tasks: []
recurring: []
decisions: []
open_calls: []

preserved_evidence:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/LOG.md
  - live/solmax/history/s-map-001.md
  - live/solmax/history/s-shape-001.md
  - live/life-reset/CHARTER.md
  - live/life-reset/LOG.md
  - live/life-reset/history/
  - live/life-reset/work/
  - github.com/ainazemtsau/life-reset-manager
  - github.com/ainazemtsau/zaratusta

next:
  id: c-zara-operate-contract-converge-verify-001
  to: session
  direction: solmax
  play: converge-verify
  node: g-zara-operate-contract
  goal: |
    Refute the closed WHAT spec for g-zara-operate-contract before shape.
    Verify that manager authority, effect tiers, entity model, horizon
    model, escalation rules, owner-approval boundaries, read-only OS
    boundary and forbidden prescription zones are complete enough for
    later shape without hidden assumptions.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-25-s-zara-remap-001.md
    - live/solmax/history/2026-06-26-s-zara-shape-operate-001b.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    The converge session closed the WHAT spec without deciding HOW:
    no vendor/framework/UI/storage/cadence/scoring implementation choices.
    Later children consume the spec as input evidence:
    state consumes W8-W10/W16/W18/W20;
    runtime consumes W1-W15/W17-W20;
    evolution consumes W15/W18-W20.
  boundaries: |
    Refute; do not implement.
    Do not write the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not convert routed HOW/PLAN choices into WHAT unless the spec
    is inconsistent without them.
    Do not prescribe medical, psychiatric, nutrition or training actions.
    Do not permit Direction OS writes.
  done_when: |
    The WHAT spec is either verified as forward-clean/backward-clean and
    ready for shape, or rejected with exact rows that must be reopened.
    Coverage must check every node done_when noun, every acceptance row
    A1-A13, every glossary property, and every child-consumer edge.
  return: |
    RESULT with verification verdict, refutation attempts, row-level
    failures if any, and next route.
  budget: one verify session

END_OF_FILE: live/solmax/NOW.md
