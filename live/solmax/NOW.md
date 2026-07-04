# NOW — solmax
project:
  name: Zaratusta
  product_repo: github.com/ainazemtsau/zaratusta

active_bet:
  status: none
  note: |
    No active bet. g-zara-operate-contract closed as done on 2026-07-02
    at the Markdown/GitHub-readable authority-contract substrate level.

    Accepted baseline evidence:
    - authority-contract substrate:
      github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
    - operating-manager-v1 Markdown surface:
      github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631,
      including commit 469e6996ea120073168bf350d54cf8e56135f30d.

    Route repair:
    The previous state-only/state-converge route is superseded. The next bet
    must close the full Markdown operating-manager-v1 workspace/state surface
    that the owner clarified: inbox/intake, backlog/open loops, current
    operating state, week/day, reviews, decisions/commitments, source/context,
    audit/replay, process mutation and examples/checks. This is the complete
    current Markdown product layer, not app/runtime/API/database/automation.

    Boundary: contract and Markdown operating-manager-v1 surface evidence are
    accepted baseline only. Durable state, runtime/dogfood, automation, UI, API,
    storage writer/replay, exact schema/layout, external integrations and full
    product readiness are not done.

route_status: g-zara-operate-contract_done_b92_baseline_accepted_markdown_manager_v1_full_shape_ready

owner_directive: |
  The first Zaratusta implementation route is g-zara-operate: the LifeReset-derived
  personal operating-manager capability becomes the real Personal Operating System
  phase of Zaratusta, not a PoC and not a separate LifeReset project.

  Owner-approved split from 2026-06-26 remains: g-zara-operate-contract,
  g-zara-operate-state, g-zara-operate-runtime, g-zara-operate-evolution.

  Preserved operating boundary: topic-open through process/source/context; writes
  default only to the Zaratusta workspace/repo; other repos/directions/projects
  are read-only sources by default; future non-Zaratusta writes require explicit
  narrow integration/procedure; deep research is a first-class process route.

  Owner clarification in c-solmax-zaratusta-b92-state-route-repair-002 resolves
  the next route: do not use an incomplete/manual reduced version; quality and
  full readiness matter; route state-first/full-readiness, not manual-use-now.

  Owner correction in c-solmax-zaratusta-markdown-manager-v1-route-repair-004:
  the next bet must not narrow to state/replay/converge-only work. It must
  shape and then implement the full Markdown operating-manager-v1 layer:
  inbox/intake, backlog/open loops, week/day, reviews, current state,
  source/context, audit/replay, process mutation, examples/checks and
  handback rules. Quality remains priority; this layer must be complete in
  Markdown before later app/runtime/automation work.

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
  - live/solmax/history/2026-06-27-s-zara-operate-contract-converge-verify-owner-boundary-002.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-trace-repair-003.md
  - live/solmax/history/2026-06-28-s-zara-operate-contract-converge-verify-trace-repair-004.md
  - live/solmax/history/2026-07-01-s-zara-operate-contract-repair-t1-t3-state-sync-007.md
  - live/solmax/history/2026-07-02-s-zara-operate-contract-t3-verify-corrected-map-008.md
  - live/solmax/history/2026-07-02-s-zara-operate-contract-review-bounce-repair-001.md
  - live/solmax/history/2026-07-04-c-solmax-zaratusta-b92-handback-repair-001.md
  - live/solmax/history/2026-07-04-c-solmax-zaratusta-b92-state-route-repair-002.md
  - live/solmax/work/calls/c-zara-operate-state-shape-001.md
  - live/life-reset/CHARTER.md
  - github.com/ainazemtsau/life-reset-manager/SPEC.md
  - github.com/ainazemtsau/zaratusta
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b/checks/w20-a1-a13-acceptance-map.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
  - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/contracts/operating-manager-v1-source-basis.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/docs/decisions/0002-operating-manager-v1-surface.md
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631/examples/operating-manager-v1-examples.md
  - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
  - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

next: work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md
END_OF_FILE: live/solmax/NOW.md
