CALL c-zara-operate-markdown-manager-v1-full-surface-t1-001
to: executor
direction: solmax
play: work
node: g-zara-operate-state
task: t-1
repo: github.com/ainazemtsau/zaratusta
kind: engineering
goal: |
  The Zaratusta product repo has a Markdown-readable full-surface coverage
  scaffold for the complete operating-manager-v1 workspace/state layer.
context: |
  Active bet:
  - b-zara-operate-markdown-manager-v1-full-surface-001
  - node: g-zara-operate-state
  - task: t-1
  - appetite: 3 focused days
  - kill_by: 2026-07-11

  Direction OS context to read:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/LOG.md
  - live/solmax/history/2026-07-04-c-solmax-zaratusta-markdown-manager-v1-route-repair-004.md
  - live/solmax/history/2026-07-05-s-zara-operate-markdown-manager-v1-full-shape-repair-001.md
  - live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-shape-001.md

  Product baseline evidence:
  - github.com/ainazemtsau/zaratusta@79578ac87c73591000409f9f82a3bb4d0e33aa5b
  - github.com/ainazemtsau/zaratusta@b92de14eedda436e06a6de457f50aae483b7c631
  - github.com/ainazemtsau/zaratusta@469e6996ea120073168bf350d54cf8e56135f30d

  Product files to read at current main before editing:
  - README.md
  - AGENTS.md
  - checks/w20-a1-a13-acceptance-map.md
  - checks/markdown-foundation-checklist.md
  - contracts/manager-role.md
  - contracts/workspace-boundaries.md
  - contracts/source-context.md
  - contracts/process-contracts.md
  - contracts/owner-context.md
  - contracts/context-loading.md
  - contracts/operating-manager-v1.md
  - contracts/operating-manager-v1-source-basis.md
  - examples/operating-examples.md
  - examples/operating-manager-v1-examples.md
  - docs/decisions/0001-markdown-only-reset.md
  - docs/decisions/0002-operating-manager-v1-surface.md

  Required full surface to map:
  - inbox/intake: owner input capture, triage, missing context, not silently
    turning capture into commitment.
  - backlog/open loops: deferred items, waiting items, research routes,
    rejected/superseded assumptions, next decision point.
  - current operating state: current week/day, accepted commitments, protected
    commitments, current objective, current constraints.
  - week flow: week plan, protected items, routine, wishes/new volume, cuts,
    accepted/proposed status.
  - day flow: day start, protected items, main objective, next action,
    disruption rebuild, free log, day close.
  - reviews: day review and week review, including evidence, misses, protected
    item status, process conclusions and next gates.
  - decisions/commitments: capture vs proposal vs accepted commitment vs
    completed work.
  - source/context: loaded basis, missing context, source permissions,
    freshness/trust and allowed use.
  - audit/replay: enough Markdown trace to reconstruct why a plan, decision
    or review exists, without choosing a DB/runtime/replay engine.
  - process mutation: owner-approved recipe/process changes only; no hidden
    self-mutation.
  - examples/checks: manual examples and checklist covering the whole flow
    end-to-end.
  - handback/reporting: product report must return Direction OS carry-back
    evidence, not a product-authored next CALL.

  Preserve:
  - operating-manager-v1 is a Markdown product layer.
  - Topic handling remains open through process/source/context.
  - Direction OS and other repos/projects are read-only sources by default.
  - Zaratusta writes only to its own workspace/repo unless a future narrow
    integration/procedure is approved.
  - External, irreversible, spend, deletion, message/send or cross-system
    effects require explicit scoped owner approval before effect.
  - W20/A1-A13 and the W19 HOW firewall remain binding unless a fresh converge
    or owner-approved route explicitly changes WHAT.
boundaries: |
  Do not modify the Direction OS repo or any non-Zaratusta repo.
  Do not route to manual-use-now.
  Do not narrow this to state/replay-only, converge-only, check-only,
  verification-only or manual-use prose.
  Do not cut inbox/intake, backlog/open loops, current state, week/day,
  reviews, decisions/commitments, source/context, audit/replay, process
  mutation, examples/checks or handback from the coverage scaffold.
  Do not implement UI/channel/API/vendor/scheduler/automation/spend controls.
  Do not choose database/storage engine/app runtime/vendor/API.
  Do not choose exact permanent schema or future non-Markdown architecture.
  Do not create any Direction OS write path.
  Do not introduce a generic topic/domain blacklist.
  Do not claim runtime, automation, dogfood, app readiness, or full autonomous
  product readiness.
  Keep all changes inside the Markdown product surface.
done_when: |
  - Product repo commit/PR contains a Markdown-readable coverage scaffold
    mapping every required surface to concrete product artifacts/checks:
    inbox/intake, backlog/open loops, current operating state, week/day,
    reviews, decisions/commitments, source/context, audit/replay, process
    mutation, examples/checks and handback/reporting.
  - Scaffold identifies which existing baseline files are reused and which
    Markdown artifacts/templates/contracts/examples/checks need creation or
    update.
  - Scaffold marks W19/HOW items explicitly not chosen: UI/channel/app,
    API/vendor/framework, DB/storage/replay engine/durable writer,
    scheduler/automation/spend controls/external integration, exact permanent
    schema/future non-Markdown architecture.
  - Scaffold preserves W20/A1-A13, topic-open source/context handling,
    Zaratusta-only writes, read-only external repos/sources by default, and
    owner approval before external/irreversible/spend/deletion/message/
    cross-system effects.
  - Scaffold is sufficient for an independent verifier to catch missing
    required surfaces before t-2 implementation proceeds.
return: |
  RESULT with:
  - product repo commit or PR reference;
  - changed files;
  - concise manual check output against checks/markdown-foundation-checklist.md
    and checks/w20-a1-a13-acceptance-map.md;
  - explicit table of required surfaces -> artifact/check coverage;
  - explicit W19/HOW not-chosen check;
  - any gaps or risks found;
  - no product-authored Direction OS state changes or next CALL.
budget: half focused day
parent: s-zara-operate-markdown-manager-v1-full-shape-repair-001
surface: cli

END_OF_FILE: live/solmax/work/calls/c-zara-operate-markdown-manager-v1-full-surface-t1-001.md
