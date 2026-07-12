# NOW: indie-game-development
updated: 2026-07-12 by s-research-q-investigation-readiness-canon-admission-002

bet:
  node: g-9c41
  goal: |
    Полигон М1 доказывает representative networked co-op scene: регулируемый DA-уровень,
    gas gameplay, S4, controlled breach, full flood, две реальные машины и слабое железо.
  appetite: |
    Максимум 13 product legs, started 2026-07-10; разовая owner-authorized exception 2026-07-11
    для M1-GAS-PROBE + M1-GAS-CORE, дальнейшего автоматического продления нет. Checksum foundation
    занимает один слот, а будущие M1-9 + M1-10 остаются одним final evidence leg. P2a0 — risk-first
    opening уже существующего M1-5 player-tracking leg, не 14-й leg; остаток M1-5 не продлевается молча.
  kill_by: |
    2026-07-24 либо 13 легов, что раньше; immediate review, если M1-GAS-PROBE не даёт
    deterministic mass-exact bounded body/no-tail или M1-A1 не даёт bounded exact/no-pop.
    Финальный профиль: ≤50 ms green; 50–100 ms owner decision; >100 ms/desync/meaning-loss = not done.
  forecast: |
    После Phase 0 MERGED checksum foundation убирает legacy full-scan polling, successor A0 даёт
    дешёвую observability, затем M1-GAS-PROBE выбирает закон, M1-GAS-CORE меняет authority,
    c-visual-009 разблокируется, и только после этого M1-A1 проверяет S4 handoff. Параллельно P2a0
    в disposable lab проверяет player root authority и сетевую пригодность до production controller.
  against: |
    Packed-body law может не пройти determinism/no-tail или прочитаться как вода; dirty visual BUILD
    потребует fresh rebase. S4, DA-authoring и weak-peer flood всё ещё могут съесть appetite;
    legacy exact checksum остаётся медленным oracle, а не runtime dirty/sync primitive.
  cut_list:
    - Sc-damage остаётся HELD; нет damage/consequence.
    - Нет врагов, миссии, production UI/audio/VFX и новой газовой энциклопедии.
    - Только один контролируемый стеновой пролом; нет полной разрушаемости.
    - Нет save/load, late join, matchmaking и host migration.
    - Один Полигон и минимальный DA module set; не контент-производство.
  lens_verdicts:
    commercial_traction: final evidence leg даёт capture-пакет существующим visual/marketing линиям.
    core_gameplay_depth: M1-5..7 — tracking, reactions, breach.
    coop_first: объединённый M1-9+10 — две реальные машины, sync и owner verdict.
    technical_feasibility: Phase 0 + checksum foundation + successor A0 + M1-GAS-PROBE/CORE, затем A1 и M1-2..4.
    scope_production: not_needed — cut_list и один уровень держат solo-scope.
    audience_workflow: final evidence leg; отдельная соцсеть-задача не нужна.

tasks:
  - id: Lv-ingest
    goal: Phase 0 завершает deterministic authoritative gas-source seam для hand-tagged уровня.
    done_when: c-exec-lv-ingest-phase0-001 проходит собственные gates, binding fresh G5 и подтверждён MERGED.
    status: active
  - id: M1-A0
    goal: Ядро отдаёт canonical read-only ActiveCell snapshot и step counters без изменения authority.
    done_when: |
      Fresh successor change id (не c-exec-poligon-a0-001) доставляет snapshot без implicit legacy
      global checksum, проходит owner-approved PLAN, BUILD gates, review, binding fresh G5 и merge.
    status: blocked
    unblock_when: Phase 0 MERGED + checksum foundation DELIVERED/MERGED + fresh owner-approved successor A0 PLAN.
  - id: M1-P2a0
    goal: |
      PuppetMaster получает проверенный root-authority маршрут для сетевого игрока, которого могут
      физически сбивать камни и импульсы, до заморозки production controller.
    done_when: |
      c-exec-player-puppetmaster-p2a0-002 freezes an owner-approved live-source proof PLAN; a later separately-issued
      BUILD under that frozen change returns accepted Puppet→Unpinned→GetUp evidence, A/B comparison + bounded C
      kill-probe, multiplayer authority inventory and fresh G5, without FishNet BUILD, damage or product merge.
    status: active

open_calls:
  - id: c-exec-unity65-mac-revision-build-001
    to: executor
    for: g-9c41 / Unity 6.5 Mac revised BUILD and closeout
    issued: 2026-07-12
    note: "READY fresh BUILD from owner-approved successor PLAN `A`: product PLAN commit 8a344e97, candidate parent df1e5ca, approach unity65-coordinated-wire-v2-repair-closeout. Same-version peers use full-width scene handles; mixed protocol versions reject before scene-broadcast decode. Fresh spec-only RED test-author first; builder cannot edit those tests. Repair every close-check class; no merge/push/Windows work. Preserve unstaged .vscode/settings.json and CoopSmallSGF.asset. work/c-exec-unity65-mac-revision-build-001-call.md."
  - id: c-exec-lv-ingest-phase0-001
    to: executor
    for: Lv-ingest
    issued: 2026-07-09
    note: "NOT MERGED/NOT DELIVERED: dev@8fc25d90 (round-8 фиксы закоммичены, запись раунда 8 не закоммичена в dev worktree), origin/main@a644e5d; owner 2026-07-11 «пусть там работает» — цикл ревью продолжается до чистого binding-раунда; work/c-exec-lv-ingest-phase0-call.md."
  - id: c-shape-sc-damage-001
    to: session
    for: Sc-damage
    issued: 2026-07-09
    note: "Pending owner-present shape CALL; current M1 cut keeps Sc-damage HELD; owner 2026-07-11: кооп-взаимозависимость обсуждается отдельным вопросом канона (кандидат Gate Q, work/canon-question-candidates-2026-07-11.md), Sc-damage стартует только с готовой канон-спекой; work/c-shape-sc-damage-call.md."
  - id: c-visual-009
    to: executor
    for: g-7e15 / Stage 3.5 movement-data BUILD reconciliation
    issued: 2026-07-10
    note: "BLOCKED on M1-GAS-CORE: approved PLAN @a0db28a2 + dirty BUILD preserved on codex/c-visual-009-build; no continuation/close; history/2026-07-11-s-repair-visual-sim-upstream-001.md."
  - id: c-exec-player-puppetmaster-p2a0-002-build-001
    to: executor
    for: M1-P2a0 / trustworthy PuppetMaster live-source authority proof BUILD
    issued: 2026-07-12
    note: "PARENT BUILD remains open for final fresh G5 and owner verdict. Checkpoint @a2d50c2a proved clean venue + immutable RED and stopped before builder. Owner requested “Я хочу продолжить в Claude Code”; child continuation c-exec-player-puppetmaster-p2a0-002-build-continuation-001 is READY with a two-hour cap and 60-minute settled-smoke checkpoint. Product RESULT: C:\projects\Unity\GasCoopGame_p2a0_002\docs\results\c-exec-player-puppetmaster-p2a0-002.md."
  - id: c-exec-player-puppetmaster-p2a0-002-build-continuation-001
    to: executor
    for: M1-P2a0 / fresh Claude Code PuppetMaster builder continuation
    issued: 2026-07-12
    note: "READY from clean product checkpoint a2d50c2a: fresh Claude Code builder, immutable RED c73b0195 must not be edited or repeated; maximum two hours, hard checkpoint at 60 minutes without settled live smoke; no G5/verdict/merge/-Deliver. work/c-exec-player-puppetmaster-p2a0-002-build-continuation-001-call.md."
  - id: c-marketing-wake-001
    to: session
    for: g-2f8c / минимальное пробуждение маркетинга
    issued: 2026-07-11
    note: "READY: owner verdict «будить минимально» 2026-07-11 + расширение и v2-уточнение тем же днём; сессия исполняет substrate строго по work/marketing/wake-minimal-2026-07-11.md и несёт research-мандат из §Расширение (стратегия не-generic, путь к деньгам — издатель/Kickstarter/прямые продажи, автономный контур «маркетинговый эксперт», AI-пайплайн без слопа, дашборд трека); единственное жёсткое требование — деньги последний ресурс, всё через AI-процессы; публичные действия БЕЗ отдельного owner-«да» НЕ входят; запуск-текст work/marketing/wake-launch-2026-07-11.md; параллельна инженерным линиям."
recurring: []

decisions:
  - q: "d-m1-acceptance-criteria-001 — ратифицировать 5 дополнений к критериям приёмки Полигона М1 (замер на named min-spec железе; лампа детерминизма в HUD; политика выхода пира/хоста; admission ceiling виден в стенде; звук сознательно НЕ в М1)?"
    options: ["Ратифицировать все 5", "Ратифицировать выборочно", "Отклонить — критерии не расширяем"]
    recommendation: "Ратифицировать все 5: дёшево и делает final evidence leg доказуемым; min-spec требует owner-выбора конкретного железа. Источник: owner-lane вырезанной лестницы 10.07 — критерии нигде больше не жили (s-repair-board-m1-ladder-purge-001)."
next:
  CALL: work/c-exec-player-puppetmaster-p2a0-002-build-continuation-001-call.md

END_OF_FILE: live/indie-game-development/NOW.md
