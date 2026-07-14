# NOW: indie-game-development
updated: 2026-07-14 by s-work-publish-near-gas-v21-main-and-open-binding-001

bet:
  node: g-9c41
  goal: |
    Полигон М1 доказывает representative networked co-op scene: регулируемый DA-уровень,
    gas gameplay, S4, controlled breach, full flood, две реальные машины и замер на названном
    слабом железе; финальный стенд явно показывает deterministic agree/divergence,
    ловит planted divergence и показывает admission ceiling.
  appetite: |
    Максимум 13 product legs, started 2026-07-10; owner-authorized exception 2026-07-11 только для
    M1-GAS-PROBE + M1-GAS-CORE. P2a0 — opening существующего M1-5, checksum foundation — один слот,
    M1-9+10 — один final-evidence leg; Direction-задача M1-Integration-ROUTE не является product leg.
  kill_by: |
    2026-07-24 либо 13 product legs, что раньше; immediate review при провале deterministic gas-body/A1.
    Финальный профиль: ≤50 ms green; 50–100 ms owner decision; >100 ms/desync/meaning-loss = not done.
  forecast: |
    Главный owner-view — work/board/dashboard.html; принятый cross-bet route лежит в
    work/poligon-m1-integration-route.md. Он связывает gas, Level/DA/PGG, character, visual, common scene и
    network/evidence в 34 обязательных логических product legs плюс условные, но это прозрачный ledger, не cap.
    Владелец сказал «Да, именно так»: числового ограничения нет, а 24.07 — контрольный review, не остановка;
    затем «Маршрут принимаю». Текущая ставка всё ещё формально хранит старые appetite/kill_by и по G3 не может
    быть продлена work-сессией, поэтому свежий review закрывает её и предлагает следующую ставку.
    Ратифицированный level path сохранён: project-owned Level/Module Contract → DA runtime + PGG editor-time
    bake → production modules; новый Level executor CALL не выпущен.
    NearGas publication update: the owner-approved v21 packet is now on product origin/main@9dc49575 with exact
    raw-Git-blob aggregate 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e.
    L1 remains NOT DELIVERED and no EXEC/BUILD may start until
    c-work-near-gas-l1-v21-published-binding-001 returns a fresh binding verdict.
  against: |
    Gas PROGRAM — обязательный дочерний маршрут, но не весь M1 и не разрешение молча превысить 13 legs.
    Старый level PLAN ждёт Phase 0, которая больше никогда не возобновляется; новый маршрут обязан сперва
    показать точный пересчёт legs/cuts. Visual всё ещё LOCKED; M1-P2a0 lifecycle/G5 drift чинится отдельно.
  cut_list:
    - Sc-damage остаётся HELD; нет damage/consequence.
    - Нет врагов, миссии, production UI/VFX и новой газовой энциклопедии.
    - Production-звук сознательно не входит в Полигон М1; это будущая visual-линия.
    - Только один контролируемый стеновой пролом; нет полной разрушаемости.
    - Нет save/load, late join, matchmaking и host migration; потеря пира/хоста явно и контролируемо
      завершает текущий прогон М1.
    - Один Полигон и минимальный DA module set; не контент-производство.
  lens_verdicts:
    commercial_traction: final evidence leg отдаёт capture-пакет visual/marketing линиям.
    core_gameplay_depth: M1-5..7 — tracking, reactions, breach.
    coop_first: M1-9+10 — две реальные машины, sync и owner verdict.
    technical_feasibility: NearGas L1 NOT READY FOR EXECUTION; v21 planning authority is published at product origin/main@9dc4957548111c99980f7efbbb9e7adbda17332b with packet aggregate 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e. Fresh Direction binding review c-work-near-gas-l1-v21-published-binding-001 is still required before any independent RED or EXEC/BUILD. Level/DA/PGG route remains ratified.
    scope_production: not_needed — cut_list и один уровень держат solo-scope.
    audience_workflow: final evidence leg; отдельная соцсеть-задача не нужна.

tasks:
  - id: NearGas-dashboard
    goal: Владелец видит актуальную карту gas-engineering пути.
    done_when: Committed light dashboard принят owner-eye; history/2026-07-13-s-work-near-gas-dashboard-close-002.md.
    status: done
  - id: NearGas-L1-PLAN
    goal: Владелец понимает и утверждает frozen L1 PLAN одного engine-free Core-владельца.
    done_when: PLAN@1e4e78c + PLAN-AMEND@a58ee356 owner-approved и binding-refuted; BUILD отдельно.
    status: done
  - id: NearGas-L1-BUILD
    goal: NearGas получает delivered dormant engine-free Core-владельца с atomic generation replacement и deterministic Step.
    done_when: Reviewed, gate-green DELIVERED L1 с independent RED и binding fresh G5; no Unity/child-leg/workers.
    status: active
    note: |
      V21 PLANNING AUTHORITY PUBLISHED / L1 NOT DELIVERED. Product origin/main@9dc4957548111c99980f7efbbb9e7adbda17332b
      contains integration merge fed1073d53d5894946b8ad6e9ffd14d6c79ec69a and frozen packet commit
      21acd415209dc4261aaa692c13cc56d0e6d9f59f. Exact raw-Git-blob packet aggregate is
      2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e; fresh pre-push semantic review was
      29/29 GREEN, zero gaps. Historical 52a47c52... is working-tree-byte chronology only.
      Product publication, owner approval and in-session semantic review do not close the Direction gate.
      c-work-near-gas-l1-v21-published-binding-001 must fresh-refute the exact published packet. Until GREEN,
      no independent RED, EXEC/BUILD, implementation, delivery gate, Unity or MCP is authorized. Option A and
      deferred workers remain; historical BUILD and execute-002 checkpoints stay evidence only.
  - id: M1-P2a0
    goal: PuppetMaster получает проверенный root-authority маршрут для сетевого игрока.
    done_when: Owner-approved live-source PLAN + later accepted BUILD, bounded-C, multiplayer inventory и fresh G5.
    status: done
    note: "Current owner-close = Candidate A; written done_when/G5 mismatch остаётся отдельным P1 repair dr-20260711-001, без переоткрытия Phase 0."
  - id: M1-Integration-ROUTE
    goal: Владелец имеет один согласованный путь до сильной интеграционной сцены Полигона М1.
    done_when: |
      Owner-approved dependency/parallelism map связывает gas, Level/DA/PGG, character, visual, network/min-spec/evidence;
      текущий точный ledger/cuts записан без числового cap, а новый Level PLAN successor честно gated текущим v21 route;
      no product BUILD.
    status: done
    note: |
      Owner accepted: «Да, именно так» = без числового потолка, 24.07 только контрольный review;
      «Маршрут принимаю». Принятый route: work/poligon-m1-integration-route.md — 34 обязательных логических
      product legs + условные, не cap. Старую Phase 0 не возвращает; новый Level executor CALL не выпущен.
      Формальное закрытие старой 13/24 ставки передано свежему c-review-poligon-m1-route-reset-001 по G3.

open_calls:
  - id: c-review-poligon-m1-route-reset-001
    to: session
    for: g-9c41 / current bet close and next-bet choice after accepted M1 route
    issued: 2026-07-14
    note: |
      PRIMARY / FRESH OWNER-PRESENT REVIEW: close, do not extend, the current 13/24 bet; preserve the accepted
      no-cap cross-bet route and make 24.07 a control review in the owner-chosen next bet. Product/TREE/canon read-only;
      no executor CALL or BUILD. work/c-review-poligon-m1-route-reset-001-call.md.
  - id: c-research-level-module-standard-v1-001
    to: research
    for: g-9c41 / Level-DA-PGG project Standard v1 candidate and old-task recovery
    issued: 2026-07-14
    note: |
      READY PARALLEL / DIRECTION-ONLY: reconstruct established seams versus the missing project-owned standard;
      produce the two-contract Standard v1 candidate, validator/fixture matrices and old-task disposition package.
      No product/Unity/PLAN/BUILD, no Phase 0 revival, no owner acceptance implied.
      work/c-research-level-module-standard-v1-001-call.md.
  - id: c-map-g-d3a8-frame-v2-reconciliation-001
    to: session
    for: g-d3a8 / TREE and design-canon branch reconciliation
    issued: 2026-07-14
    note: "READY PARALLEL: owner-present G9 reconciliation of only g-d3a8 against accepted Minimum Game Frame v2 and the eight-player requirement; no canon/CHARTER/product change. history/2026-07-14-s-repair-minimum-game-frame-v2-001.md."
  - id: c-research-q-coop-interdependence-002
    to: session
    for: g-d3a8 / co-op composition question
    issued: 2026-07-14
    note: "HELD until c-map-g-d3a8-frame-v2-reconciliation-001 closes; then resume the preserved paper question under Frame v2 without canon admission or Sc-damage release. history/2026-07-14-s-repair-minimum-game-frame-v2-001.md."
  - id: c-exec-unity65-mac-revision-002-build-001
    to: executor
    for: g-9c41 / local .NET gate runner prerequisite
    issued: 2026-07-12
    note: "HELD / NON-RUNNABLE: pre-v21 CALL and PLAN refs 7a3e747/8a344e9 do not resolve from fetched refs. After repo v21 Re-sync it still needs its own current-v21 full-packet check; CALL content is unchanged. work/c-exec-unity65-mac-revision-002-build-001-call.md."
  - id: c-exec-near-gas-core-authority-001-plan-amend-resync-002
    to: executor
    for: NearGas-L1-BUILD / contract v20→v21 Re-sync + full frozen-packet repair
    issued: 2026-07-14
    note: "PENDING DIRECTION CLOSE / DO NOT RERUN: product planning evidence is published on origin/main@9dc49575; keep this call open until c-work-near-gas-l1-v21-published-binding-001 returns the required fresh binding verdict. No EXEC/BUILD."
  - id: c-work-near-gas-l1-v21-published-binding-001
    to: session
    for: NearGas-L1-BUILD / binding refutation of exact published v21 planning authority
    issued: 2026-07-14
    note: |
      READY PARALLEL / FRESH DIRECTION BINDING: read-only refutation of product origin/main@9dc49575 and exact
      packet aggregate 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e. L1 stays NOT DELIVERED;
      no product mutation, RED, EXEC/BUILD or delivery gate. If and only if GREEN, this fresh session may clear the
      planning return and issue a future independent-RED executor CALL. Global PRIMARY remains the M1 bet review.
      work/c-work-near-gas-l1-v21-published-binding-001-call.md.
  - id: c-shape-sc-damage-001
    to: session
    for: Sc-damage
    issued: 2026-07-09
    note: "HELD until ready canon spec; work/c-shape-sc-damage-call.md."
  - id: c-visual-009
    to: executor
    for: g-7e15 / preserved visual motion work
    issued: 2026-07-10
    note: "LOCKED until M0+C1+L3+I1 delivered/reviewed; motion also needs immutable per-Step data, later visuals wait E1/D1/X1."
  - id: c-marketing-wake-001
    to: session
    for: g-2f8c / minimal marketing wake
    issued: 2026-07-11
    note: "READY from the 2026-07-11 wake brief; owner mandate includes INOMAND research/substrate and no public action or spend without a separate owner yes. Route is known stale against the committed INOMAND checkpoint: dr-20260712-001."
recurring: []

decisions:
  - q: "d-m1-min-spec-hardware-001 — какое конкретное слабое железо становится binding min-spec финального прогона М1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; газ CPU-bound, поэтому CPU должен быть назван явно."
  - q: "d-char-v1-post-g5-001 — В1 G5-CONFIRMED (owner-eye + свежий binding G5, same-family Opus; заявки a–f не опровергнуты, P1 нет). Что дальше по character-треку?"
    options: ["Merge В1 в main + открыть В2 следующим", "Сначала Codex cross-family G5-проход (routing-предпочтение) + фикс magenta-материала, затем merge/В2", "В1 done; В2/merge в очередь за spine (route-reset review) — сейчас не запускать"]
    recommendation: "Заявки не опровергнуты и boundary чист → Codex-проход не обязателен (только доп-строгость на Unity-adapter/input); magenta — косметика для В2. Merge гоняешь ты. Пока НЕ авто-мержу и НЕ авто-открываю В2. Знание: knowledge/g6d4e-char-v1-socket-delivered.md."

next:
  CALL: work/c-review-poligon-m1-route-reset-001-call.md

END_OF_FILE: live/indie-game-development/NOW.md
