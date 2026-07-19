# NOW: indie-game-development
updated: 2026-07-19 by s-work-near-gas-l1b-v29-loopback-review-dispatch-001
bet:
  node: g-9c41
  goal: |
    Доставленный NearGas L1a проверяемо наблюдаем через ровно пять internal observation families:
    retry snapshot, fault injection, handler classification, kernel rows и loopback trace; observer не меняет authority, atomicity и deterministic Step.
  appetite: |
    3 focused days; владелец выбрал «а» 2026-07-16. Шесть задач по ≤0.5 focused day; продления нет.
  kill_by: |
    Automatic review 2026-07-24 или при исчерпании 3 focused days, что раньше. Kill без продления, если acceptance <5/5,
    любая family требует cut capability, observer меняет L1a semantics/order/atomicity или fresh G5 опровергает любую family.
  forecast: |
    Ранний сигнал = L1B-Acceptance: 5/5 falsifiable positive/negative oracles на реальном L1a path без excluded dependency.
    Ожидаем внутреннюю instrumentability + binding evidence за 6 half-day tasks, но не Unity/gameplay/M1 delivery.
    Cross-bet 34+ route остаётся ledger, не cap; 24.07 остаётся контрольным review, не stop.
    next_if_true: fresh review закрывает L1B только как internal instrumentability и возвращает владельцу выбор следующей ставки из route; нет automatic L2/C1/Unity launch.
  against: |
    Логи могут наблюдать суррогат, неоднозначно связывать retry/fault/handler или влиять на timing/order. Любой такой сигнал
    переключает ставку в NOT MET/review; fake-harness обход запрещён.
    next_if_false: L1a остаётся DELIVERED, v22 — FORBIDDEN; L1B закрывается NOT MET с названной failed family и возвращается на owner review без surrogate workaround.
  cut_list: ["Нет L2 resource admission, work/memory bounds и performance ceiling.", "Нет C1 committed digest или новой checksum authority.", "Нет Unity cutover, debug UI и gameplay wiring.", "Нет workers/concurrency.", "Нет S4, Level/DA/PGG, common scene, real network и two-machine proof.", "Нет общего telemetry/export/persistence/replay framework."]
  lens_verdicts:
    commercial_traction: "not_needed: внешнего сигнала нет; это короткий capped технический мост к M1."
    core_gameplay_depth: "not_needed: механики и player decisions не заявляются."
    coop_first: "not_needed: loopback = internal diagnostic, не co-op evidence."
    technical_feasibility: "L1B-Acceptance→L1B-G5: falsifiability, passive observer, deterministic integrated trace и fresh refutation."
    scope_production: "L1B-Acceptance + L1B-G5: cuts проверяются до PLAN и на close."
    audience_workflow: "not_needed: internal trace не объявляется публичным артефактом."

tasks:
  - id: L1B-Acceptance
    goal: "[session] Frozen owner-approved child acceptance различает real L1a observability и surrogate evidence для 5/5 families."
    done_when: "5/5 families имеют falsifiable positive/negative oracle; adversarial dry-run не требует cut capability; владелец принял artifact."
    status: done
  - id: L1B-PLAN
    goal: "[executor] Owner-approved product PLAN фиксирует evaluator, rollback и disjoint observation ownership без authority/Unity/C1/L2 expansion."
    done_when: "PLAN frozen по current v26 contract; владелец принял; next handoff соблюдает compiled-carrier/RED guards."
    status: done
  - id: L1B-Capture
    goal: "[executor] Retry snapshot и fault injection дают стабильное пассивное наблюдение реального L1a path."
    done_when: "Genuine RED ловит retry/fault planted controls; delivery не меняет L1a result/order/atomicity."
    status: open
  - id: L1B-Classify
    goal: "[executor] Handler classification и kernel rows однозначно связывают attempt/generation/phase."
    done_when: "Planted misclassification ловится; rows коррелируются без C1 digest и authority change."
    status: open
  - id: L1B-Trace
    goal: "[executor] Loopback trace сводит 5/5 families в один детерминированный internal scenario."
    done_when: "Trace различает agree/planted divergence и не заявляет real-network, gameplay или M1 delivery."
    status: open
  - id: L1B-G5
    goal: "[session] Fresh binding refutation даёт честный verdict по 5/5 families, passive-observer invariant и cuts."
    done_when: "Separate fresh review reruns first-hand gates, пытается опровергнуть каждую family и закрывает только по 5/5 + scope GREEN."
    status: open

track_wip_limit: 6
tracks:
  - {id: core, label: "NearGas — ядро игры", mode: primary, for: g-9c41}
  - {id: program, label: "Программа и интеграционный стенд", mode: parallel, for: "g-a7f2 / Program v2 hot migration and Integration Lab control plane"}
  - {id: level, label: "Уровни, модули и генераторы", mode: parallel, for: "local: Level/DA/PGG Standard v1"}
  - {id: canon, label: "Геймдизайн и канон", mode: parallel, for: g-d3a8}
  - {id: damage, label: "Газовый урон — Sc-damage", mode: parallel, for: "local: Sc-damage"}
  - {id: visual, label: "Визуал и движение газа", mode: parallel, for: g-7e15}
  - {id: marketing, label: "Маркетинг и аудитория", mode: parallel, for: g-2f8c}
  - {id: characters, label: "Игровые персонажи", mode: parallel, for: g-6d4e}
  - {id: dotnet-gates, label: "Локальный запуск проверок .NET — пауза", mode: parallel, for: "local: cross-platform .NET repository-gate runner prerequisite"}

open_calls:
  - id: c-repair-program-v2-live-truth-001
    track: program
    status: ready
    to: session
    for: "g-a7f2 / hot-migration live-truth reconciliation before Program v2 route"
    issued: 2026-07-19
    call: work/c-repair-program-v2-live-truth-001-call.md
    note: "READY / OWNER-APPROVED SOFT MIGRATION / REPAIR ONLY. Reconcile Direction NOW/dashboard with verified current NearGas L1B, Character Leg 2, aperture, Level LV0 and V30 evidence before any route rewrite or new product root. No product mutation, V30 install, frozen-call rewrite, silent close or automatic BUILD. Existing core/character work continues independently; WIP becomes 6/6."
  - id: c-review-near-gas-l1b-v29-loopback-final-001
    track: core
    status: ready
    to: executor
    for: "g-9c41 / L1B-Capture - v29 fresh independent review of final approved pair-base through T range"
    issued: 2026-07-19
    call: work/c-review-near-gas-l1b-v29-loopback-final-001-call.md
    note: "READY / ROOT / FRESH INDEPENDENT REVIEW / engineering_contract: 29. PAIR-FREEZE found immutable 62db→75e0→4df→T review-eligible: T=6fa101b4 directly follows BUILD 4df54a2b/tree dc4979f1, exactly three test files/zero fourth; 4df captures prepared owner/epoch only into existing fault-hit carrier before deliberate fault, with no normal Step/public API/acceptance change. Review independently inspects the complete final range, verifies the old loopback same-wrong false-green is fixed, sweeps the same source-atom class and reruns relevant tests/gates. It returns REVIEW GREEN eligibility for lawful HBP/integration admission or exact findings only. No edits unless a finding routes later repair; no BUILD/mutation/Stryker (deferred to final integrated dev H), integration or Deliver. Root binding N/A until dev ancestry; aperture is later-only STOP."
  - id: c-exec-unity65-mac-revision-002-build-001
    track: dotnet-gates
    status: paused
    to: executor
    for: "g-9c41 / local .NET gate runner prerequisite"
    issued: 2026-07-12
    call: work/c-exec-unity65-mac-revision-002-build-001-call.md
    paused_by: history/2026-07-17-s-repair-near-gas-l1b-track-rebase-001.md
    note: "Preserved non-priority legacy CALL; resume only after pre-v21 refs reconcile to current authority and a fresh full-packet check → history/2026-07-12-s-repair-unity65-mac-revision-002-route-001.md."
  - id: c-exec-level-module-standard-v1-lv0-plan-001
    track: level
    status: ready
    to: executor
    for: "g-9c41 / parallel owner-present Level/Module Standard v1 LV0 PLAN"
    issued: 2026-07-16
    call: work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
    note: "READY witness + owner-approved parallel launch → history/2026-07-16-s-repair-level-lv0-parallel-launch-001.md."
  - id: c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001
    track: canon
    status: ready
    to: session
    for: "g-d3a8 / owner-present canon admission over q-gas-behavior-jobs-paper-decision-v1"
    issued: 2026-07-18
    call: work/c-forge-g-d3a8-gas-behavior-jobs-canon-admission-001-call.md
    receipts:
      - history/2026-07-18-s-forge-g-d3a8-gas-behavior-jobs-001.md
    note: "READY / OWNER-PRESENT / CANON-ADMISSION ONLY. Exact OWNER-SELECTED PAPER ANSWER A: movement-first Control Obligation grammar (Counter / Brake / Time), not movement-only; future additional effects remain open. No redesign, implementation or automatic canon mutation."
  - id: c-shape-sc-damage-001
    track: damage
    status: paused
    to: session
    for: Sc-damage
    issued: 2026-07-09
    call: work/c-shape-sc-damage-call.md
    paused_by: history/2026-07-17-s-work-characters-resume-a1.md
    note: "Owner paused this mechanically preserved legacy frontier. Its v19/base/canon assumptions are stale; a separate review should retire or rehome it without deleting the future damage obligation from core SPEC/knowledge."
  - id: c-visual-009
    track: visual
    status: blocked
    to: executor
    for: "g-7e15 / preserved visual motion work"
    issued: 2026-07-10
    call: work/c-visual-009-movement-data-plan-call.md
    unblock_when: "M0+C1+L3+I1 are delivered/reviewed and immutable per-Step data exists; later visuals also require E1/D1/X1."
  - id: c-marketing-wake-001
    track: marketing
    status: paused
    to: session
    for: "g-2f8c / minimal marketing wake"
    issued: 2026-07-11
    call: work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md
    paused_by: history/2026-07-17-s-work-characters-resume-a1.md
    note: "Paused in the owner-approved marketing→characters WIP swap. On a later resume, start from the committed INOMAND checkpoint and first reconcile stale-route finding dr-20260712-001."
  - id: c-exec-char-v2-body-rig-ragdoll-build-001
    track: characters
    status: ready
    to: executor
    for: "g-6d4e / В2 Leg 2 — rig + procedural locomotion + cosmetic PuppetMaster ragdoll + character material"
    issued: 2026-07-14
    call: work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md
    receipts: [history/2026-07-17-s-work-char-v2-reaction-core-repair-002-admission-blocked-001.md, history/2026-07-18-s-work-char-v2-published-handback-release-route-001.md, history/2026-07-18-s-review-char-v2-published-handback-release-001.md]
    note: "READY after binding fresh Direction review MET: exact candidate 0e5b2948 → integration 53453081 → published dev/main 029279a and all six admission-003 obligations survived refutation. Leg 1 is accepted only at bounded reaction-core height; DF-13/14/15 remain routed and C1–C4 remain mandatory. Owner exact decision «A — открывай Leg 2 после review» clears the final wait. READY permits only a separate fresh product executor session with current admission; it is not automatic dispatch or product mutation."

recurring: []

decisions:
  - id: d-m1-min-spec-hardware-001
    track: core
    q: "d-m1-min-spec-hardware-001 — какое конкретное слабое железо становится binding min-spec финального прогона М1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; газ CPU-bound, поэтому CPU должен быть назван явно."
next:
  call: c-repair-program-v2-live-truth-001

END_OF_FILE: live/indie-game-development/NOW.md
