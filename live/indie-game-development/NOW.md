# NOW: indie-game-development

updated: 2026-07-22 by s-repair-launch-control-demo-control-room-unblock-001

bet: null

tasks: []

track_wip_limit: 99

tracks:
  - {id: program, label: "Integration Lab & Product Proof", mode: primary, for: g-9c41}
  - {id: launch-control, label: "Demo Control Room", mode: parallel, for: g-b847}
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

  - id: c-map-launch-control-demo-control-room-refit-001
    track: launch-control
    status: ready
    to: session
    for: "g-b847 / owner-approved refit of the sole management track into Demo Control Room"
    issued: 2026-07-22
    call: work/launch-control/c-map-launch-control-demo-control-room-refit-001-call.md
    receipts:
      - history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md
      - history/2026-07-22-s-repair-launch-control-demo-control-room-unblock-001.md
    note: "READY / DEFAULT / SAME TRACK REFIT / NOT A SECOND PLANNING TRACK. The separate owner-authorized OS maintenance and its fresh hardening review are complete. This existing root may now refit g-b847 and open only one bounded Demo Control Room foundation; no product or foreign-track work is launched."

  - id: c-exec-level-module-standard-v1-lv0-plan-001
    track: level
    status: waiting
    waiting_on: [direction-review-receipt-b1698170]
    to: executor
    for: "g-8f20 / inherited Level LV0 PLAN Direction receipt"
    issued: 2026-07-16
    call: work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
    note: "WAITING / DO NOT RELAUNCH. Product LV0 PLAN evidence exists at b16981706ece53c584848255de2bd92675b5de7b, but binding Direction close is missing. When the owner activates Level, first reconcile exact HOME, current V31 and product truth; preserved aperture RED 5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1 remains evidence, not permission to issue BUILD."

  - id: c-work-g-d3a8-demo-workflow-rebuild-001
    track: canon
    status: ready
    to: session
    for: "g-d3a8 / owner-present replacement of question-first Canon workflow with Demo Experience Tree, Canon Ledger, parented execution and Markdown-first visual portal"
    issued: 2026-07-22
    call: work/demo-workflow/c-work-g-d3a8-demo-workflow-rebuild-001-call.md
    receipts:
      - history/2026-07-22-s-work-g-d3a8-markdown-first-portal-acceptance-001.md
    note: "READY / NON-DEFAULT / OWNER-PRESENT / PROCESS REBUILD ONLY / NO DESIGN QUESTION / NO PORTAL BUILD. The owner explicitly said Canon may continue independently while Demo Control Room is rebuilt, but the now-unblocked Demo Control Room refit is the current default. Draft and co-create one exact replacement workflow artifact. Preserve accepted canon and Frames. Current question-front is suspended as scheduling authority. The accepted portal contract requires Markdown/media authority and a replaceable generated read-only site; Zensical is only the first renderer candidate. Do not generate images, define demo content, implement the portal, create AI pipelines or mutate os/**."
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

  - id: c-exec-grid-v1-g02-common-spatial-map-001
    track: grid
    status: ready
    to: executor
    for: "g-4b92 / G02 common spatial map after released exact-12 authority cleanup"
    issued: 2026-07-22
    call: work/c-exec-grid-v1-g02-common-spatial-map-001-call.md
    receipts:
      - history/2026-07-22-s-work-grid-v1-g01-direct-legacy-isolation-blocked-001.md
      - history/2026-07-22-s-work-grid-v1-g01-direct-legacy-release-001.md
    note: "READY / NON-DEFAULT / G02 PRODUCT ROOT / OWNER-PRESENT PLAN GATE FIRST / GRID 1 OF 11. G01 exact-12 cleanup is binding-reviewed and published at product dev/main 1a6373b8; all twelve legacy normative files are absent and WIN-U1 is AVAILABLE. This root delivers only the additive neutral integer spatial map and its proofs. It must obtain the owner's actual detailed PLAN verdict before implementation and use ordinary contract-31 gates; the one-time G01 Deliver waiver does not carry forward. The root is lawful but not launched or selected as default; the Demo Control Room refit is current default."

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
next:
  call: c-map-launch-control-demo-control-room-refit-001

END_OF_FILE: live/indie-game-development/NOW.md
