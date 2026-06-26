# NOW — solmax

project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none

route_status: operate_first_node_split_approved_pending_converge

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
  id: c-zara-operate-contract-converge-001
  to: session
  direction: solmax
  play: converge
  node: g-zara-operate-contract
  goal: |
    Close the WHAT spec for the operating-manager authority contract so the
    first g-zara-operate child can later be shaped into a bounded
    implementation bet without hidden assumptions.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - relevant solmax and life-reset history/work evidence as needed

    g-zara-operate is the first Zaratusta node: the real Personal Operating
    System / operating-manager outcome, not a PoC. The owner approved the
    4-child split on 2026-06-26 by answering "A".

    Approved children:
    1. g-zara-operate-contract
    2. g-zara-operate-state
    3. g-zara-operate-runtime
    4. g-zara-operate-evolution

    This CALL is only for the first child, g-zara-operate-contract.

    Load-bearing terms likely include manager authority, effect tier,
    entity model, horizon model, intake, escalation, owner approval,
    forbidden prescription zone, read-only OS boundary and implementation
    acceptance properties.
  boundaries: |
    No implementation or product-repository changes.
    No old W0 restart.
    No wholesale LifeReset copy.
    No monolithic prompt.
    No hidden assumptions.
    Markdown-first; code only after demonstrated need.
    No medical, psychiatric, nutrition or training prescriptions.
    No OS writes; the workflow OS is read-only evidence only.
    Do not decide vendor, framework, UI or storage implementation.
  done_when: |
    A signed WHAT spec exists for g-zara-operate-contract. It is sufficient
    for a later shape session to create a bounded implementation bet without
    guessing manager powers, effect tiers, entity/horizon model, escalation
    rules, owner-approval boundaries or forbidden prescription zones.

    Any still-load-bearing unknown is explicitly routed to owner decision,
    research or a later child node, not silently defaulted.
  return: |
    RESULT with the signed WHAT spec, glossary/decision evidence, unresolved
    routes if any, coverage against the node done_when, and next =
    converge-verify.
  budget: one converge session

END_OF_FILE: live/solmax/NOW.md
