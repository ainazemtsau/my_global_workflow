# NOW: indie-game-development
updated: 2026-07-13 by s-work-near-gas-l1-plan-amend-binding-close-001

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
    Обязательный gas-engineering маршрут: GasCoopGame_dev@f5c1d650:docs/gas-simulation/PROGRAM.md.
    Dashboard-зеркало закрыто; owner-approved L1 PLAN @1e4e78c и PLAN-AMEND @a58ee356 влиты в
    origin/main@32107343. Fresh Direction binding-refutation приняла public owned Create(...) + operation-local
    internal semantic fault selector: исходные spec-only construction/fault gaps закрыты без fixture/reflection/
    controller-костылей. Original BUILD @b94806de остаётся историческим CHECKPOINT / NOT DELIVERED без test commit и
    реализации; вместо его продолжения открыт fresh EXECUTE c-exec-near-gas-core-authority-001-execute-002 от
    origin/main@32107343 с новым independent spec-only RED. Вариант A — serial concurrency-ready, реальные workers
    возможны только отдельной будущей легой после delivered L1/L2/C1 и свежего профиля.
    Маршрут идёт L1→L2→C1→M0→L3→I1→L4→L5→L6→I2.
    P2a0 ЗАКРЫТ (Кандидат A, owner 2026-07-13): ядро владеет авторитетной позицией тела, PuppetMaster-рэгдолл косметичен;
    параллельный трек g-6d4e (Игровые персонажи, презентация) заведён; грид-баллистика = будущий слой ядра g-9c41.
  against: |
    Полная PROGRAM-дорога не считается молча помещённой в старый appetite: предел 13 легов и дата сохраняются.
    L3 пересекается с сохранённым dirty visual BUILD; M1-GAS-PROBE/CORE и engine S4/A1 остаются NEEDS SOURCE
    после I2/A0. Legacy exact checksum — медленный audit oracle, не runtime dirty/sync primitive.
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
    technical_feasibility: PROGRAM.md@f5c1d650; L1 PLAN @1e4e78c + owner-approved PLAN-AMEND @a58ee356 влиты в origin/main@32107343 и fresh binding-refuted GREEN; public owned Create + operation-local internal semantic fault selector закрывают два spec-only gap без костылей. Original BUILD @b94806de — historical CHECKPOINT / NOT DELIVERED; fresh EXECUTE c-exec-near-gas-core-authority-001-execute-002 готов от @32107343 с новым independent RED. Вариант A неизменен, реальные workers — только после L1/L2/C1 и свежего профиля.
    scope_production: not_needed — cut_list и один уровень держат solo-scope.
    audience_workflow: final evidence leg; отдельная соцсеть-задача не нужна.

tasks:
  - id: NearGas-dashboard
    goal: Владелец видит простую актуальную карту gas-engineering пути, статусов, блокеров, вопросов и недавней работы.
    done_when: |
      c-exec-near-gas-dashboard-001 возвращает committed light doc-only RESULT: ручное статическое dashboard-зеркало
      и product AGENTS always-read/update правило существуют, render/readback green, product code/tests/scenes/Unity/
      visual/L1 не затронуты; отдельная Direction-сессия после этого может выпустить свежий L1 PLAN.
    status: done
  - id: NearGas-L1-PLAN
    goal: |
      Владелец понимает и утверждает детальный L1 PLAN для единственного engine-free Core-владельца,
      атомарной замены generation и одного полного deterministic Step без запуска BUILD.
    done_when: |
      c-exec-near-gas-core-authority-001 возвращает committed owner-approved frozen PLAN: простое подробное
      объяснение технических решений и границ L1, builder-ready spec/tasks/ADR/evidence map, сохранность legacy-audit
      смыслов и dirty product files; product code, RED tests, Unity и BUILD не начаты, следующий BUILD выдаёт DirectionS.
    status: done
  - id: NearGas-L1-BUILD
    goal: |
      NearGas получает доставленного dormant engine-free Core-владельца с атомарной заменой generation
      и одним полным deterministic Step по утверждённому варианту A.
    done_when: |
      c-exec-near-gas-core-authority-001-build-001 возвращает reviewed, gate-green DELIVERED L1 по замороженному
      PLAN @1e4e78c: independent RED и binding fresh G5 доказывают атомарность/детерминизм/legacy-audit preservation;
      реализация остаётся serial concurrency-ready без реальных workers, Unity и child-leg scope, а foreign work сохранён.
    status: active
    note: |
      PLAN-AMEND @a58ee356 merged in origin/main@32107343 и fresh Direction binding-refuted GREEN: exact public owned
      Create(...) + literal production recipe и operation-local internal NearGasFaultSite/ForTesting seam закрывают
      исходный blocker. Original BUILD @b94806de остаётся historical CHECKPOINT / NOT DELIVERED. Fresh execution идёт
      только по c-exec-near-gas-core-authority-001-execute-002: GasCoopGame_core, new branch
      codex/c-exec-near-gas-core-authority-001-execute-002, base origin/main@32107343, новый independent spec-only RED;
      GasCoopGame_dev foreign changes не назначаются/не трогаются. Вариант A и deferred workers неизменны.
  - id: M1-P2a0
    goal: |
      PuppetMaster получает проверенный root-authority маршрут для сетевого игрока, которого могут
      физически сбивать камни и импульсы, до заморозки production controller.
    done_when: |
      c-exec-player-puppetmaster-p2a0-002 freezes an owner-approved live-source proof PLAN; a later separately-issued
      BUILD under that frozen change returns accepted Puppet→Unpinned→GetUp evidence, A/B comparison + bounded C
      kill-probe, multiplayer authority inventory and fresh G5, without FishNet BUILD, damage or product merge.
    status: done
    note: |
      DONE 2026-07-13 через owner-eye гейт. Тяжёлый done_when выше СОЗНАТЕЛЬНО заменён owner-authorized
      лёгким спайком (c-exec-player-puppetmaster-p2a0-lean-spike-build-001): владелец сыграл живой стенд
      PuppetMaster и вынес вердикт = Кандидат A (ядро/контроллер владеет авторитетной позицией тела;
      PuppetMaster-рэгдолл = косметический локальный вид, никогда не авторитетен; B отклонён — недетерминированный
      PhysX на авторитетном пути = рассинхрон между машинами). Слово владельца в сессии 2026-07-13: «Кандидат A — да».
      Потребность в геймплей-физике закрыта дизайном: детерминированный слой «грид-баллистика» в ЯДРЕ (не физ-движок),
      маршрутизирован будущим слайсом ядра g-9c41. Сознательно НЕ сделано под лёгким разворотом (owner-acked cut):
      bounded-C kill-probe и свежий G5 — связывающим гейтом этого ДИЗАЙН-решения был глаз владельца. Канонический
      источник (single source): GasCoopGame origin/main@0e9eed02 docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md.

open_calls:
  - id: c-exec-unity65-mac-revision-002-build-001
    to: executor
    for: g-9c41 / local .NET repository-gate runner prerequisite
    issued: 2026-07-12
    note: "READY NON-PRIORITY after owner-approved PLAN `Одобряю PLAN c-exec-unity65-mac-revision-002`: product PLAN commit 7a3e747, parent 8a344e97, approach lan-local-dotnet-gates-adapter-only. Build/deliver the local cross-platform .NET 8 gate runner with full parity and independent RED evidence; do not resume revision-001, Unity/FishNet, Windows, merge or push. Preserve unstaged .vscode/settings.json and CoopSmallSGF.asset. work/c-exec-unity65-mac-revision-002-build-001-call.md."
  - id: c-exec-near-gas-core-authority-001-execute-002
    to: executor
    for: NearGas-L1-BUILD / fresh execution amended frozen L1 от нового independent RED
    issued: 2026-07-13
    note: "READY NEW EXECUTE after fresh Direction binding GREEN: project GasCoopGame; existing clean assigned worktree C:\\projects\\Unity\\GasCoopGame_core; create new branch codex/c-exec-near-gas-core-authority-001-execute-002 from exact origin/main@32107343d75240d6b3bc850d7010bd3f17dc4ca8. Start over with a new independent spec-only RED author; do not resume original build-001@b94806de or reuse its aborted author. Frozen PLAN/proposal/spec/tasks/ADR and independent tests are builder-immutable. Contract v20; option A stays serial concurrency-ready; real workers only after delivered L1/L2/C1 + fresh profile. C:\\projects\\Unity\\GasCoopGame_dev has foreign uncommitted changes: never assign/clean/overwrite it. No Unity/child leg/merge/push. work/c-exec-near-gas-core-authority-001-execute-002-call.md."
  - id: c-shape-sc-damage-001
    to: session
    for: Sc-damage
    issued: 2026-07-09
    note: "Pending owner-present shape CALL; current M1 cut keeps Sc-damage HELD; owner 2026-07-11: кооп-взаимозависимость обсуждается отдельным вопросом канона (кандидат Gate Q, work/canon-question-candidates-2026-07-11.md), Sc-damage стартует только с готовой канон-спекой; work/c-shape-sc-damage-call.md."
  - id: c-visual-009
    to: executor
    for: g-7e15 / preserved visual motion work awaiting fresh reconciliation
    issued: 2026-07-10
    note: "LOCKED under PROGRAM.md@f5c1d650; historical PLAN @a0db28a2 and dirty dev_2 BUILD are preserved but non-runnable. Fresh owner-present reconciliation PLAN only after M0+C1+L3+I1 delivered/reviewed; motion BUILD also needs sufficient detached immutable committed-per-Step Flux/history from L3 or delivered c-exec-near-gas-visual-motion-data-seam-001. Moving-source visual waits E1; door/destruction visual waits D1/X1."
  - id: c-plan-characters-001
    to: session
    for: g-6d4e / дорожная карта персонажей + замороженный spec первого drop-in слайса
    issued: 2026-07-13
    note: "READY parallel track (owner 2026-07-13 «трек ... ок», «поехали»). PLAN-сессия: выдать owner-approved дорожную карту трека «Игровые персонажи» (персонаж-first ORDER: drop-in префаб + стабильный adapter-API → управление/процедурные реакции/косметический рэгдолл → [ядро] граница грид-баллистики) и builder-ready spec ПЕРВОГО слайса = переиспользуемый префаб игрока + стабильный adapter-API против ЗАГЛУШКИ авторитетной позиции (seam R13/R14, свап на реальное ядро без правки трека). PLAN-only: без продуктового кода/тестов/RED/BUILD/Unity/MCP/мержа/пуша (BUILD идёт отдельной свежей GasCoopGame_dev сессией); independent-test-author RED-план отметить по проектному builder-quality правилу. Грид-баллистика НЕ в build-scope трека — это слайс ядра g-9c41 (input-lockstep, целочисленно, ждёт delivered grid+Step+lockstep), назван для позже; захватить как downstream + обязательный 2-машинный FishNet-proof. Канон вердикта P2a0: GasCoopGame origin/main@0e9eed02 docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md. Газовый хребет (next = fresh L1 EXECUTE c-exec-near-gas-core-authority-001-execute-002) остаётся приоритетом №1. work/c-plan-characters-001-call.md."
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
  CALL: work/c-exec-near-gas-core-authority-001-execute-002-call.md

END_OF_FILE: live/indie-game-development/NOW.md
