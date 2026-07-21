# NOW: indie-game-development

updated: 2026-07-21 by s-review-grid-v1-executor-plan-001

bet: null

tasks: []

track_wip_limit: 9

tracks:
  - {id: program, label: "Integration Lab & Product Proof", mode: primary, for: g-9c41}
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

  - id: c-exec-level-module-standard-v1-lv0-plan-001
    track: level
    status: waiting
    waiting_on: [direction-review-receipt-b1698170]
    to: executor
    for: "g-8f20 / inherited Level LV0 PLAN Direction receipt"
    issued: 2026-07-16
    call: work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
    note: "WAITING / DO NOT RELAUNCH. Product LV0 PLAN evidence exists at b16981706ece53c584848255de2bd92675b5de7b, but binding Direction close is missing. When the owner activates Level, first reconcile exact HOME, current V31 and product truth; preserved aperture RED 5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1 remains evidence, not permission to issue BUILD."

  - id: c-cartography-g-d3a8-visual-workflow-reconciliation-001
    track: canon
    status: ready
    to: session
    for: "g-d3a8 / reconcile admitted visual workflow with the still-text-only Canon Forge boundary"
    issued: 2026-07-21
    call: work/c-cartography-g-d3a8-visual-workflow-reconciliation-001-call.md
    receipts:
      - history/2026-07-21-s-forge-g-d3a8-visual-contract-canon-admission-001.md
    note: "READY / OWNER-PRESENT / TEXT ONLY. c-003 is admitted, but local/canon-forge still forbids images. Reconcile only that process/map boundary and obtain an exact owner-approved diff. Do not generate images, answer V1, choose appearance or modify c-003."
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

  - id: c-work-grid-v1-launch-control-handoff-001
    track: grid
    status: ready
    to: session
    for: "g-4b92 / owner-present planning-only launch control before any future G01 admission"
    issued: 2026-07-21
    call: work/c-work-grid-v1-launch-control-handoff-001-call.md
    receipts:
      - history/2026-07-21-s-review-grid-v1-executor-plan-001.md
    note: "READY / DEFAULT / OWNER-PRESENT / PLANNING ONLY / NO PRODUCT MUTATION. Binding fresh-session G5 could not refute the accepted Grid V1 executor plan against the locally observed clean product snapshot f6e4f725. Grid remains parallel and product progress is 0/11. This session prepares one binary launch-control handoff for possible later G01 admission, pins fresh v31/registry/venue/serialization checks and records the owner's exact words. It cannot issue G01, PAIR-CANDIDATE, BUILD or any engineering CALL, allocate a product venue, run product checks, amend the plan or retire the track."

  - id: c-work-gas-v1-master-plan-001
    track: gas
    status: ready
    to: session
    for: "g-1a63 / owner-present staged Gas V1 master plan"
    issued: 2026-07-21
    call: work/c-work-gas-v1-master-plan-001-call.md
    receipts:
      - history/2026-07-21-s-map-gas-track-resume-001.md
      - history/2026-07-21-s-work-gas-v1-current-authority-audit-accepted-001.md
    note: "READY / NON-DEFAULT / OWNER-PRESENT / PLAN ONLY / NO PRODUCT MUTATION. The owner accepted a full Gas V1 master plan now with staged implementation, then clarified that it must remain a route map: every major node receives its own detailed owner-present plan before implementation, especially full-level optimization. The accepted audit separates the released detailed NearGas foundation from missing live composition, runtime sources, committed publication, generated-level scale, world-change, player consequence and multiplayer proof. Gas owns simulation/evidence only; Program/Multiplayer owns session/identity/input delivery and must return the mandatory network proof. Target scale is about 150 rooms averaging roughly 8x4x8 m with size variation and long/vertical routes; giant hangars stay paused. Grid-dependent signatures wait for contract freeze, independent Wind stays deferred, default remains Grid and BUILD stays closed."

recurring: []

decisions:
  - id: d-m1-min-spec-hardware-001
    track: program
    q: "d-m1-min-spec-hardware-001 — какое конкретное слабое железо становится binding min-spec финального прогона M1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; gas simulation CPU-bound, поэтому CPU должен быть назван явно."

next:
  call: c-work-grid-v1-launch-control-handoff-001

END_OF_FILE: live/indie-game-development/NOW.md
