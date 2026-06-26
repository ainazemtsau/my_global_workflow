# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta
active_bet:
  status: none
route_status: g-zara-operate-contract_converge_verify_passed_pending_shape
owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived personal operating-manager capability becomes the real Personal Operating System phase of Zaratusta, not a PoC and not a separate LifeReset project.

  The owner approved option A on 2026-06-26: g-zara-operate is split into four child outcomes:
  - g-zara-operate-contract
  - g-zara-operate-state
  - g-zara-operate-runtime
  - g-zara-operate-evolution

  First child to shape: g-zara-operate-contract.
blocked_reason: |
  No implementation resumes until g-zara-operate-contract is shaped into a bounded bet.
  The authority WHAT spec has passed converge-verify; W20/A1-A13 are now shape-binding acceptance rows.
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
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta
next:
  id: c-zara-operate-contract-shape-001
  to: session
  direction: solmax
  play: shape
  node: g-zara-operate-contract
  goal: |
    Shape g-zara-operate-contract into a bounded implementation bet that preserves the verified operating-manager authority WHAT spec without smuggling HOW choices.
  context: |
    Read:
    - live/solmax/CHARTER.md
    - live/solmax/TREE.md
    - live/solmax/NOW.md
    - live/solmax/LOG.md
    - live/solmax/work/converge-g-zara-operate-contract.md
    - live/solmax/history/2026-06-26-s-zara-operate-contract-converge-verify-001.md
    - live/life-reset/CHARTER.md
    - github.com/ainazemtsau/life-reset-manager/SPEC.md

    converge-verify passed:
    - complete=PASS
    - smuggling=PASS
    - row_failures=none

    Copy W20 acceptance rows A1-A13 verbatim into Definition-of-Ready or executor done_when.
    No separate §CONTRACTS section exists in the converge file; W20/A1-A13 are the contract surface to preserve.

    Treat W19 routed choices as PLAN agenda, not as WHAT:
    - exact UI/channel/surface
    - exact storage/schema/file layout/database
    - exact engine/vendor/framework/API/subscription adapter
    - exact horizon durations/cadence/month/12-week model
    - exact non-caving weighing/scoring policy and thresholds
    - exact implementation of state writer and replay
    - exact research procedure mechanics
    - exact automation/scheduler/spend controls

    Preserve child-consumer edges:
    - g-zara-operate-state consumes W8-W10, W16, W18, W20
    - g-zara-operate-runtime consumes W1-W15, W17-W20
    - g-zara-operate-evolution consumes W15, W18-W20
  boundaries: |
    Do not implement or modify the product repository.
    Do not reopen the old W0/kernel-first route.
    Do not copy LifeReset wholesale.
    Do not convert W19 HOW/PLAN choices into WHAT unless shape finds a contradiction that must bounce to converge.
    Do not prescribe medical, psychiatric, nutrition or training actions.
    Do not permit Direction OS writes.
  done_when: |
    An owner-approved bounded bet for g-zara-operate-contract exists with appetite, kill_by, cut list, lens sweep and tasks that include the riskiest assumption.
    Shape copies A1-A13 into the bet's Definition-of-Ready or executor done_when and carries W19 as PLAN agenda.
    If any verified WHAT row becomes inconsistent during shape, the exact row is bounced to converge instead of guessed.
  return: |
    RESULT with approved bet or exact bounce, TREE/NOW/LOG state_changes, evidence, and next ready work/verify route.
  budget: one shape session
END_OF_FILE: live/solmax/NOW.md
