CALL c-zara-operate-state-shape-001
to: session
direction: solmax
play: shape
node: g-zara-operate-state
goal: |
  An owner-approved bounded bet card exists for durable Zaratusta
  operating state and context.
context: |
  Route authority:
  - Owner clarification in c-solmax-zaratusta-b92-state-route-repair-002
    resolved D-zara-operate-next-bet-001 toward g-zara-operate-state.
  - b92/469 is accepted baseline evidence for the Markdown
    operating-manager-v1 contract surface, not proof of durable state,
    runtime, dogfood, automation, UI, API, storage/replay or full readiness.
  - Product-authored next CALL c-zara-operate-markdown-manager-v1-t2-001
    is not authoritative and is superseded by this OS-authored CALL.
  - The owner does not want an incomplete/manual reduced version; quality
    priority and full operating-manager readiness govern the route.

  Current direction state:
  - live/solmax/CHARTER.md
  - live/solmax/TREE.md
  - live/solmax/NOW.md
  - live/solmax/LOG.md

  Closed prerequisite:
  - g-zara-operate-contract closed as done by
    s-zara-operate-contract-review-bounce-repair-001.
  - Product repo: github.com/ainazemtsau/zaratusta.
  - Verified contract commit:
    79578ac87c73591000409f9f82a3bb4d0e33aa5b.
  - Accepted operating-manager-v1 baseline:
    b92de14eedda436e06a6de457f50aae483b7c631 includes
    469e6996ea120073168bf350d54cf8e56135f30d.
  - Key product evidence:
    README.md,
    checks/w20-a1-a13-acceptance-map.md,
    checks/markdown-foundation-checklist.md,
    contracts/manager-role.md,
    contracts/workspace-boundaries.md,
    contracts/source-context.md,
    contracts/process-contracts.md,
    contracts/owner-context.md,
    contracts/context-loading.md,
    contracts/operating-manager-v1.md,
    contracts/operating-manager-v1-source-basis.md,
    examples/operating-examples.md,
    examples/operating-manager-v1-examples.md,
    docs/decisions/0001-markdown-only-reset.md,
    docs/decisions/0002-operating-manager-v1-surface.md.

  Contract facts to preserve:
  - W20/A1-A13 is the accepted authority surface.
  - W19 HOW choices remain not chosen.
  - Topic handling is open through process/source/context, not a generic
    domain blacklist.
  - Direction OS and other repos/projects are read-only sources by default.
  - Zaratusta writes only to its own workspace/repo unless a future narrow
    integration/procedure is approved.
  - External, irreversible, spend, deletion, message/send or cross-system
    effects require explicit scoped owner approval before effect.

  Review boundary:
  - The closed contract bet proves authority substrate only.
  - The b92/469 operating-manager-v1 surface proves a Markdown process
    contract surface only.
  - g-zara-operate-state, g-zara-operate-runtime and
    g-zara-operate-evolution remain not done.
boundaries: |
  Do not modify product repo in this shape session.
  Do not route to manual-use-now as the readiness answer.
  Do not start runtime/dogfood.
  Do not implement UI/channel/API/vendor/scheduler/automation/spend controls.
  Do not create any Direction OS write path.
  Do not mark durable state, runtime, dogfood, automation, UI, API, storage,
  replay, exact schema/layout or full product readiness as done.
  Do not choose exact database/storage engine/exact schema/exact file layout
  unless shape proves it is the minimal necessary WHAT and the owner approves
  that shape artifact.
  Preserve W20/A1-A13 and the W19 HOW firewall unless a fresh converge
  explicitly changes WHAT.
done_when: |
  Shape produces one owner-approvable bet card for g-zara-operate-state
  with appetite, kill_by, cut list, lens sweep, riskiest assumption task
  and <=3 half-day tasks. The bet tests the durable-state prerequisite
  without smuggling runtime/UI/API/vendor/scheduler/automation/spend or
  exact schema/layout as contract.
return: |
  RESULT with owner-approved shape state_changes, exact active_bet if
  approved, and next CALL.
budget: one focused shape session
parent: c-solmax-zaratusta-b92-state-route-repair-002
surface: chatgpt

END_OF_FILE: live/solmax/work/calls/c-zara-operate-state-shape-001.md
