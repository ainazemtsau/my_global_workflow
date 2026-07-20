# NOW: indie-game-development

updated: 2026-07-20 by s-shape-program-v2-v30-entry-001

bet: null

tasks: []

track_wip_limit: 9

tracks:
  - {id: program, label: "Integration Lab & Product Proof", mode: primary, for: g-9c41}
  - {id: build-tooling, label: "Build & Tooling", mode: parallel, for: g-c5d1}
  - {id: level, label: "Level & Environment", mode: parallel, for: g-8f20}
  - {id: canon, label: "Design & Canon", mode: parallel, for: g-d3a8}
  - {id: visual, label: "Presentation", mode: parallel, for: g-7e15}
  - {id: marketing, label: "Marketing & Audience", mode: parallel, for: g-2f8c}
  - {id: characters, label: "Character & Gameplay Contact", mode: parallel, for: g-6d4e}

open_calls:
  - id: c-shape-program-v2-integration-lab-entry-001
    track: program
    status: ready
    to: session
    for: "g-9c41 / choose one common Integration Lab entry without duplicating the planned NearGas lab"
    issued: 2026-07-20
    call: work/c-shape-program-v2-integration-lab-entry-001-call.md
    note: "READY / DEFAULT / SHAPE ONLY. Current product is lawfully on V31; the historical V30 route is superseded and needs no re-sync. Reconcile common Lab ownership against planned NearGasSimulationLab before any scene, PLAN or BUILD. No product mutation or new feature task."

  - id: c-exec-level-module-standard-v1-lv0-plan-001
    track: level
    status: waiting
    waiting_on: [direction-review-receipt-b1698170]
    to: executor
    for: "g-8f20 / inherited Level LV0 PLAN Direction receipt"
    issued: 2026-07-16
    call: work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
    note: "WAITING / DO NOT RELAUNCH. Product LV0 PLAN evidence exists at b16981706ece53c584848255de2bd92675b5de7b, but binding Direction close is missing. When the owner activates Level, first reconcile exact HOME, current V31 and product truth; preserved aperture RED 5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1 remains evidence, not permission to issue BUILD."

  - id: c-cartography-g-d3a8-post-gas-behavior-admission-front-001
    track: canon
    status: ready
    to: session
    for: "g-d3a8 / reconcile current design-question map after gas-behavior canon admission"
    issued: 2026-07-19
    call: work/c-cartography-g-d3a8-post-gas-behavior-admission-front-001-call.md
    receipts:
      - history/2026-07-19-s-repair-g-d3a8-gas-behavior-admission-route-001.md
    note: "READY / CARTOGRAPHY ONLY / SAME WORKING CANON PROCESS. c-002 is admitted; reconcile the stale question map, preserve floor-loop findings and return 2–3 plain-language next-question options. No automatic design answer, canon mutation, greybox or implementation."

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

recurring: []

decisions:
  - id: d-m1-min-spec-hardware-001
    track: program
    q: "d-m1-min-spec-hardware-001 — какое конкретное слабое железо становится binding min-spec финального прогона M1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; gas simulation CPU-bound, поэтому CPU должен быть назван явно."

next:
  call: c-shape-program-v2-integration-lab-entry-001

END_OF_FILE: live/indie-game-development/NOW.md
