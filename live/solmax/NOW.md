# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none
  note: |
    No active bet after repair applied the reviewed closure of
    b-zara-operate-contract-002 on 2026-07-02.

    Review verdict: met/done. g-zara-operate-contract is done at the
    Markdown/GitHub-readable authority-contract substrate level.

    Product evidence:
    - Zaratusta commit:
      79578ac87c73591000409f9f82a3bb4d0e33aa5b
      (`Correct W20 A1-A13 acceptance map boundary`).

    Closed task evidence:
    - t-1 done: product repo evidence maps W20/A1-A13 to Markdown-readable
      artifacts/checks without choosing W19 HOW.
    - t-2 done: smallest Markdown/GitHub-readable operating-manager
      authority contract pack materialized.
    - t-3 done: clean independent verification PASS against commit
      79578ac87c73591000409f9f82a3bb4d0e33aa5b.

    Verified t-3 dimensions:
    - complete: PASS
    - backward_clean: PASS
    - forward_clean: PASS
    - smuggling: PASS
    - hard rows A3/A9/A10/A13: PASS/PASS/PASS/PASS
    - W19 HOW firewall: PASS
    - development boundary: PASS
    - AGENTS.md is repo-local editing guardrail only, not product
      acceptance authority.

    Boundary:
    This does not prove durable state, runtime/dogfood, real daily use,
    storage writer/replay, UI/API/vendor/scheduler/automation, or exact
    schema/layout. Those remain later-child work.

route_status: g-zara-operate-contract_done_next_bet_decision_open

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

  First child remains g-zara-operate-contract. Shape bounced it back to converge, converge
  repaired the authority WHAT rows that had encoded the wrong forbidden-domain/blacklist
  model, trace repair fixed invalid glossary references, converge-verify passed, and shape
  has now activated the bounded contract implementation bet.

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

tasks: []

recurring: []
decisions:
  - id: D-zara-operate-next-bet-001
    status: open
    created: 2026-07-02
    q: |
      Which Zaratusta operating-manager child should be shaped next after
      g-zara-operate-contract closed as done?
    facts: |
      g-zara-operate-contract review verdict is met/done at the
      authority-substrate level. Product repo commit
      79578ac87c73591000409f9f82a3bb4d0e33aa5b preserves A1-A13 coverage
      and the W19 HOW firewall. This does not prove durable state,
      runtime dogfood or process evolution.
    terms: |
      shape = session that turns a parked node into a bounded active bet.
      state = durable Zaratusta operating context and audit/recovery
        boundary.
      runtime = real owner week/day/intake/planning/review loop.
      evolution = evidence-gated process improvement, not hidden
        self-mutation.
    options:
      - |
        A (recommended): shape g-zara-operate-state.
        why_now: it is the prerequisite for trustworthy memory, audit,
          replay/recovery boundaries and no Direction OS write path before
          runtime dogfood.
        bad_because: delays daily-use/runtime proof by one bet.
      - |
        B: shape g-zara-operate-runtime.
        why_now: attacks daily use and real-depth evidence sooner.
        bad_because: without durable state it risks becoming a chat
          wrapper that cannot preserve decisions/evidence/open loops
          safely.
      - |
        C: shape g-zara-operate-evolution.
        why_now: uses the accepted process/source/context model to design
          process mutation/review mechanics.
        bad_because: premature before the system has durable state or real
          runtime processes to evolve.
    recommendation: |
      A, because the contract creates authority substrate for state and
      runtime. State is the narrowest next risk: Zaratusta must preserve
      context and audit boundaries in its own workspace before a runtime
      loop can be trusted.
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
  - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta
  - live/solmax/history/2026-07-01-s-zara-operate-contract-repair-t1-t3-state-sync-007.md
  - live/solmax/history/2026-07-02-s-zara-operate-contract-t3-verify-corrected-map-008.md
  - live/solmax/history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md
  - live/solmax/work/calls/c-zara-operate-state-shape-001.md
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b/checks/w20-a1-a13-acceptance-map.md

next: work/calls/c-zara-operate-state-shape-001.md
END_OF_FILE: live/solmax/NOW.md
