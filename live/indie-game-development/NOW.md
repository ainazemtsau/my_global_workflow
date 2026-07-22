# NOW: indie-game-development

updated: 2026-07-22 by s-work-launch-control-demo-control-room-first-cycle-wave-accepted-001

bet: null

tasks: []

track_wip_limit: 99

tracks:
  - {id: program, label: "Integration Lab & Product Proof", mode: primary, for: g-9c41}
  - {id: launch-control, label: "Demo Control Room", mode: parallel, for: g-b847, outcome_dispatch: true}
  - {id: level, label: "Level & Environment", mode: parallel, for: g-8f20}
  - {id: canon, label: "Design & Canon", mode: parallel, for: g-d3a8}
  - {id: visual, label: "Presentation", mode: parallel, for: g-7e15}
  - {id: marketing, label: "Marketing & Audience", mode: parallel, for: g-2f8c}
  - {id: characters, label: "Character & Gameplay Contact", mode: parallel, for: g-6d4e}
  - {id: grid, label: "Grid / Layers / World Change", mode: parallel, for: g-4b92}
  - {id: gas, label: "Gas Simulation", mode: parallel, for: g-1a63}

open_calls:
  - id: c-exec-program-v2-legacy-lab-purge-release-001
    track: program
    status: blocked
    to: executor
    for: "g-9c41 / release the preserved legacy-lab purge candidate after the external Deliver baseline is green"
    issued: 2026-07-20
    call: work/c-exec-program-v2-legacy-lab-purge-release-001-call.md
    unblock_when: "The pre-existing Character review-evidence defect is closed so tools/check.ps1 -Deliver is GREEN on the preserved cleanup lineage; then serialized WIN-CTRL may publish/read back the root and release WIN-U1."
    receipts:
      - history/2026-07-20-s-work-program-v2-legacy-lab-purge-deliver-blocked-001.md
    note: "BLOCKED / V31 RELEASE CONTINUATION / ROOT NOT RELEASED. Product candidate 72c7c8c6 removes the 24 approved tracked paths, preserves KEEP, adds the <=400-word no-growth policy, passes fresh non-author G5 and normal gates (1829/1829), and is integrated only in local dev through c5c21c13 with blocker evidence baf8513c. Deliver is RED solely because pre-existing review-c-exec-char-v2-source-router-repair-001 does not account for source commit 413149ce after reviewed commit 8a0e33ec. No push/merge/release; origin refs remain 45b15623; WIN-U1 is DRAINING with lease preserved. Do not dispatch or return to feature work until unblock_when is true."

  - id: c-work-launch-control-demo-control-room-canon-disposition-refill-001
    track: launch-control
    status: ready
    to: session
    for: "g-b847 / immediate resource refill after the first bounded Canon Hook Discovery disposition"
    issued: 2026-07-22
    call: work/launch-control/c-work-launch-control-demo-control-room-canon-disposition-refill-001-call.md
    receipts:
      - history/2026-07-22-s-work-launch-control-demo-control-room-first-cycle-wave-accepted-001.md
    note: "READY / OWNER-ACCEPTED ACTIVE WAVE 1 / CANON OUTCOME REQUEST OPEN / PRODUCT RESULT NONE. The owner supplied `60 минут` of attention and accepted option `A`: one new bounded Canon disposition request, with no Grid, Gas, Character or other foreign launch. The auxiliary request c-outcome-canon-demo-hook-discovery-001 is the first actionable item; this same-track root holds immediate event-driven refill after ACCEPT/COUNTER/BLOCKED or another material event. It must rebuild fresh resources, preserve the waiting Canon pilot and every foreign root, and infer no hook, Contract, implementation or technical HOW."

  - id: c-exec-level-module-standard-v1-lv0-plan-001
    track: level
    status: waiting
    waiting_on: [direction-review-receipt-b1698170]
    to: executor
    for: "g-8f20 / inherited Level LV0 PLAN Direction receipt"
    issued: 2026-07-16
    call: work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
    note: "WAITING / DO NOT RELAUNCH. Product LV0 PLAN evidence exists at b16981706ece53c584848255de2bd92675b5de7b, but binding Direction close is missing. When the owner activates Level, first reconcile exact HOME, current V31 and product truth; preserved aperture RED 5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1 remains evidence, not permission to issue BUILD."

  - id: c-cartography-g-d3a8-demo-experience-tree-pilot-001
    track: canon
    status: waiting
    waiting_on: [owner-approved-launch-control-demo-contract]
    to: session
    for: "g-d3a8 / minimal owner-present Demo Experience Tree pilot: one immediate experience-spine child of the accepted Demo Contract"
    issued: 2026-07-22
    call: work/demo-workflow/c-cartography-g-d3a8-demo-experience-tree-pilot-001-call.md
    receipts:
      - history/2026-07-22-s-work-g-d3a8-demo-workflow-rebuild-accepted-001.md
      - work/demo-workflow/demo-driven-design-canon-workflow-v1.md
    note: "WAITING / LOCAL CANON HANDOFF / NO META-CHOICE / NO DESIGN DISPATCH. The owner accepted Demo-Driven Design & Canon Workflow v1 and explicitly required the Canon track to retain its own next CALL. Start only after Launch Control records one real owner-approved Demo Contract and exact acceptance receipt for work/launch-control/demo-control-room.md. Then propose only one immediate experience-spine child for owner approve/correct/reject under local/canon-cartography. No old question migration, Canon Forge, READY/NEXT tree data, portal/product work or automatic successor."
  - id: c-outcome-canon-demo-hook-discovery-001
    track: canon
    status: ready
    to: session
    request_kind: outcome
    requested_by: launch-control
    for: "g-d3a8 / minimal owner-present Demo Experience Tree pilot: one immediate experience-spine child of the accepted Demo Contract"
    issued: 2026-07-22
    call: work/launch-control/c-outcome-canon-demo-hook-discovery-001-call.md
    note: "READY / AUXILIARY TARGET DISPOSITION ONLY / CURRENT CANON ROOT UNCHANGED. Launch Control requests one exact ACCEPT/COUNTER/BLOCKED answer on whether the accepted pre-contract override can lawfully yield 2-3 comparable Demo Hook concept cards, including gas-sphere reactions and a materially different option. This request adds no WIP slot, does not activate the waiting Demo Experience Tree pilot, chooses no concept and authorizes no implementation, prototype, product work or automatic successor."
  - id: c-visual-009
    track: visual
    status: blocked
    to: executor
    for: "g-7e15 / inherited visual motion work"
    issued: 2026-07-10
    call: work/c-visual-009-movement-data-plan-call.md
    unblock_when: "A fresh V31/Conflict Guard review proves that the legacy prerequisites and read-model contract still match current product authority; the old M0+C1+L3+I1 wording alone is not permission to launch."
    note: "BLOCKED / LEGACY ROOT. Presentation remains mapped, but c-visual-009 must be reconciled against current V31/product truth before any dispatch."

  - id: c-marketing-wake-001
    track: marketing
    status: paused
    to: session
    for: "g-2f8c / minimal Marketing & Audience wake"
    issued: 2026-07-11
    call: work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md
    paused_by: history/2026-07-17-s-work-characters-resume-a1.md
    note: "PAUSED BY OWNER-CONTROLLED LOAD. On resume, keep the existing marketing-forge internals and first reconcile stale-route finding dr-20260712-001; accepted product proof comes from Integration/Presentation."

  - id: c-exec-char-v2-body-rig-ragdoll-build-001
    track: characters
    status: waiting
    waiting_on: [product-task-019f73c8-8fb0-7633-812f-ed45acc19af6]
    to: executor
    for: "g-6d4e / V2 Leg 2 — rig + procedural locomotion + cosmetic PuppetMaster ragdoll + character material"
    issued: 2026-07-14
    call: work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md
    receipts:
      - history/2026-07-17-s-work-char-v2-reaction-core-repair-002-admission-blocked-001.md
      - history/2026-07-18-s-work-char-v2-published-handback-release-route-001.md
      - history/2026-07-18-s-review-char-v2-published-handback-release-001.md
    note: "WAITING / PRODUCT REVIEW-CLOSING IN PROGRESS. Do not dispatch this frozen CALL again. It waits for owner LOOK, binding G5, product RESULT/Deliver and valid Direction close. A future Player Simulation / Actor Layer is fresh V31 work and cannot expand this lineage retroactively."

  - id: c-exec-grid-v1-g02-common-spatial-map-002
    track: grid
    status: ready
    to: executor
    for: "g-4b92 / G02 common spatial map after completed exact-12 G01 authority cleanup"
    issued: 2026-07-22
    call: work/c-exec-grid-v1-g02-common-spatial-map-002-call.md
    receipts:
      - history/2026-07-22-s-work-grid-v1-g01-direct-legacy-release-001.md
      - history/2026-07-22-s-repair-grid-v1-g02-false-g01-blocker-001.md
    note: "READY / FRESH OWNER-PRESENT PLAN / G01 COMPLETE 1 OF 11 / FALSE PRE-PLAN BLOCKER REMOVED / CONTRACT 31. The owner explicitly directed that the deferred cleanup-only workflow route, missing checker/selftest/wiring interpretation and frozen pending prose no longer appear or count as a G01/G02 blocker. Start in a fresh product session, confirm product validation.config contract 31, present the complete plain-language G02 PLAN and stop for the owner's actual verdict before implementation. Existing Gas/Voxel and Structure state and behavior remain read-only; no G01 repair, workflow work, G03+ or consumer adapter is in this root."

  - id: c-work-gas-v1-live-composition-plan-001
    track: gas
    status: ready
    to: session
    for: "g-1a63 / owner-present detailed plan for Gas V1 node 1 — live deterministic Gas composition"
    issued: 2026-07-21
    call: work/c-work-gas-v1-live-composition-plan-001-call.md
    receipts:
      - history/2026-07-21-s-work-gas-v1-master-plan-accepted-001.md
    note: "READY / NON-DEFAULT / OWNER-PRESENT / PLAN BEFORE BUILD. The owner accepted the nine-node Gas V1 master plan with exact words `Окей, подтверждаю план.` This root plans only node 1: connect the released NearGas foundation to one lawful production simulation tick and prove deterministic composition. It must re-read current product authority first-hand, present any material composition choice to the owner, preserve current behavior and atomicity, and open no BUILD before acceptance. The Demo Control Room refit is current default."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
