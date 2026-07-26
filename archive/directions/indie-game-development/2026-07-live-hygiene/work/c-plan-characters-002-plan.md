# FROZEN PLAN — c-plan-characters-002 · трек g-6d4e «Игровые персонажи» · Волна В2 (тело)

- status: FROZEN 2026-07-14 by s-plan-characters-v2-freeze-001
- node: g-6d4e (character presentation/embodiment track; parallel track, NOT a 2nd bet — хребет g-9c41 остаётся приоритетом №1)
- owner approvals (in-session, cite):
  - спек к заморозке: «1 да»
  - рэгдолл = PuppetMaster изолированным косметическим слоем (рекомендация): «2 да»
  - объём = две BUILD-ноги (headless-реакция отдельно, engine-тело отдельно): «3 как ты рекомендуешь»
- предшественники: В1 socket DELIVERED + G5-CONFIRMED (knowledge/g6d4e-char-v1-socket-delivered.md);
  frozen В1 spec work/c-plan-characters-001-plan.md; P2a0 verdict Кандидат A
  (GasCoopGame origin/main@0e9eed02 docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md).

## 0. Что доказано разбором (baked-in, не переоткрывать)

Два вывода из first-hand разбора кода p2a0_002@db69aba6 — они формируют спек:

- **F1 (архитектура реакции).** Наивное «косметический рэгдолл вообще не трогает авторитетную позицию»
  НЕ держится: В2 сидит на В1-плейсхолдере (ввод), а `InputBodyStateSource.Update()` интегрирует WASD
  БЕЗУСЛОВНО каждый кадр, `PlayerBodyView.Update()` пишет `_socket.Current` в трансформ БЕЗУСЛОВНО — оба не
  знают про реакцию. Значит держишь W в нокдауне → авторитетная капсула едет по полу, тело «лежит но идёт».
  РЕШЕНИЕ: реакция обязана (а) ГЕЙТИТЬ источник, пока State ≠ Normal (ввод не двигает позу), и (б) на GetUp
  ПЕРЕСЕЛИТЬ авторитетную позу в точку покоя (авторитет ← rest), а не «дёргать картинку к старой позе».
  Реализуется тонкой **knockdown-aware `IAuthoritativeBodyState`-обёрткой** между вводом и сокетом. Сейм-ТИПЫ
  (`IAuthoritativeBodyState`/`PlayerBodySocket`/`BodyPose`) при этом БАЙТ-ИДЕНТИЧНЫ — это просто новый источник
  ЗА сокетом, ровно то, ради чего сокет делался. Кандидат A сохранён: рендер-рэгдолл косметичен, но реакция
  управляет источником. Этот контракт (гейт+reconcile) — headless-тестируемое ядро и главный риск В2.

- **F2 (magenta — НЕ удалённый материал).** guid `31321ba15b8f8eb4c954353edc038b1d` — это ДЕФОЛТНЫЙ URP-материал
  пакета (`Library/PackageCache/com.unity.render-pipelines.universal@…/Runtime/Materials/Lit.mat.meta`,
  fileID 2100000, type 2); ни один tracked `Assets/**/*.mat.meta` его не владеет. На него ссылается пол-проекта:
  `Assets/Settings/UniversalRenderPipelineGlobalSettings.asset` (m_DefaultMaterial) + 2 ГАЗОВЫЕ сцены
  (GasSourcePhase0Demo, GasRoomScene), не только 4 файла персонажа. ⇒ Пинить новый материал под ЭТОТ guid
  ЗАПРЕЩЕНО (коллизия GUID с пакетом → недетерминированный импорт, перекраска газовых сцен, перекрытие
  проектного URP-дефолта). ПРАВИЛЬНЫЙ фикс: дать демо-персонажу СВОЙ проектный low-poly материал и назначить
  его ТОЛЬКО на 4 character-ассета; сам URP-guid не трогать. Сам magenta = протухший PackageCache → переимпорт
  URP. Фикс сворачивается в арт-задачу В2 (Leg 2) бесплатно.

## 1. Track roadmap (напоминание)

| Волна | Отдаёт | Ждёт ядро? |
|---|---|---|
| **В1** ✅ | Socket (авторитетная поза ← сменный источник) + drop-in управляемая капсула + follow-camera. | Нет |
| **В2** (этот план) | Тело: knockdown-aware источник + reaction state machine (headless) → риг + процедурная локомоция + косметический PuppetMaster рэгдолл (изолированный слой) + свой материал. ≈80% «характера». | Нет — тот же placeholder |
| **В3** | Grid-ballistics CORE (g-9c41 slice) кормит сейм; 2-machine FishNet proof. | **Да** |

## 2. Подход (shape-хайджин G6)

Рассмотрены 3 структурно разных механизма; выбран **B**:
- **A. Полный кастомный риг + рэгдолл.** Bet: соло-дев успевает авторить И тюнить полный humanoid-риг + физ-рэгдолл
  + blend-back в аппетит. *Плохо:* это крупнейшая арт+физ-стоимость всего трека, почти весь тюнинг — owner-eye
  итерации, множит поверхности утечки физики в авторитет → сносит аппетит.
- **B. Реюз-риг + рэгдолл косметичный, минимальный headless state machine (ВЫБРАН).** Bet: реюз low-poly humanoid
  + рэгдолл на косметической иерархии + knockdown-aware источник дают достаточно присутствия И реальный flop, а
  сейм байт-идентичен, т.к. ничего физическое не пишет в авторитетный трансформ (пишет только обёртка-источник по
  явному контракту F1). *Плохо:* реюз-риг может спорить с low-poly идентичностью (retarget-трение), get-up→pose
  blend требует owner-eye тюнинга — приемлемо для косметики.
- **C. Чисто процедурный, без скин-рига и PhysX.** Bet: стилизованный скриптовый tip-over продаёт реакцию и
  убирает retarget/физику/утечку. *Плохо:* теряет emergent-физику/комедию настоящего flop — ровно тот
  Lethal-Company charm, который просит тон-регистр; читается «деревянно».

**Почему B:** видимый персонаж И настоящий flop (тон-выигрыш) при соло-аппетите, вся физика заперта в
write-only косметическую иерархию + обёртку-источник, сейм неизменен. A сносит аппетит на риг/blend-тюнинге;
C убирает риск ценой charm, ради которого волна и существует. (A, C → captures.)

**Рэгдолл-технология (owner-decision, решено).** PuppetMaster УСТАНОВЛЕН локально
(`Assets/Plugins/RootMotion/`), но **gitignored** (per-machine paid vendor asset, НЕ коммитится). Владелец выбрал
PuppetMaster («2 да») — это ратифицированный Кандидат-A выбор и уже куплен. **Дисциплина зависимости:** рэгдолл —
ИЗОЛИРОВАННЫЙ косметический слой; базовый (авторитетный) player-префаб работает и БЕЗ RootMotion, вендор нужен
только «слою сока». Любой worktree/машина без RootMotion получает рабочую авторитетную капсулу через сейм; missing
PuppetMaster-скрипты не ломают ядро. **Named fallback (только по явному owner-ack):** встроенный рэгдолл Unity
(Rigidbody + Character Joint) — first-party, коммитится целиком; выбрать только если owner-eye по PuppetMaster-blend
неудовлетворителен ИЛИ владелец захочет ноль вендор-связки. Смена named-подхода = ESCALATE, не тихий downgrade.

## 3. Гейтинг v20→v21 (решено в PLAN)

Продукт-репо GasCoopGame стоит на **v20** (root AGENTS.md + validation.config `synced_contract_version:20`);
OS-контракт — **v21**. Единственная дельта v21 = «Plan-to-RED готовность»; её тяжёлые проверки (five-field
рецепты, pre-freeze RED-ревьюер, независимый RED-автор, negative-control, property-слой) бьют по HEADLESS-строкам
приёмки — у В2 их мало (Leg 1) или ноль (Leg 2). v21 — семантическая PLAN-дисциплина, НЕ новый deliver-скрипт
(«no parser/regex/schema/conformance»).

**Решение:** одноразовая ТЕКСТОВАЯ пересинхронизация v20→v21 как ПЕРВЫЙ шаг Leg 1 (mirror клаузы в root AGENTS.md
+ OpenSpec guidance, bump `synced_contract_version` 20→21; НЕ трогать product source/tests/gate-scripts; идемпотентно
— если уже 21, пропустить). Далее В2 планируется/строится сразу под v21. **В2 НЕ ждёт NearGas** — v21-routing repair
оставил character «HELD до собственной v21-проверки», т.е. отдельная разрешённая линия, не хвост критического пути
ядра. Re-sync репо-глобален и разделён с NearGas: если какая-то нога уже смёржила v21 в общий main — Leg 1 детектит
и пропускает (при этом NearGas-ветка сейчас unmerged, поэтому Leg 1 закладывается на собственный идемпотентный bump).
Реально гейтит В2: engine-side EXISTENCE-доказательство (Leg 2) + owner-eye LOOK (Leg 2) + один cross-family G4-ревью
(каждая нога) + связывающий свежий KERNEL-G5 в ОТДЕЛЬНОЙ сессии (каждая нога).

## 4. Две BUILD-ноги (owner: «две»)

### Leg 1 — headless-ядро реакции (RUNNABLE сейчас)
CALL: work/c-exec-char-v2-reaction-core-build-001-call.md. Строит ЛОГИКУ, снимает главный риск F1 БЕЗ арта:
- Открывающий шаг: идемпотентный v20→v21 re-sync (см. §3).
- Independent test-author RED из ЭТОГО spec ДО билда (builder не редактирует), затем builder → green:
  - **reaction state machine**: Normal→Knockdown→GettingUp→Normal; переход по АБСТРАКТНОМУ reaction-токену
    (`BodyImpulse`), не по газу/урону; таймеры/длительности knockdown+getup; инвариант «одно активное состояние»;
    детерминизм при (event, time); неизвестный/нулевой токен = no-op; реализует `IBodyReactions`.
  - **knockdown-aware `IAuthoritativeBodyState`-обёртка** (контракт F1, headless): при State=Normal — прозрачно
    пропускает вход-источник; при State≠Normal — авторитетная поза ЗАМОРОЖЕНА (вход не двигает); `GetUp(restPose)`
    ставит авторитетную позу = restPose (reconcile = авторитет ← rest, НЕ картинка ← авторитет).
  - Сейм-ТИПЫ `IAuthoritativeBodyState`/`PlayerBodySocket`/`BodyPose` — БАЙТ-ИДЕНТИЧНЫ (проверяется в spec-freeze
    инвентарём + тестом «обёртка реализует существующий интерфейс, старые Characters-тесты зелёные без правок»).
- done_when: все headless-строки зелёные (переходы, single-active-state, детерминизм, no-op negative-control,
  гейт-входа-в-нокдауне, reconcile-на-GetUp); pre-freeze RED-ревьюер вернул полный gap-list и по скелету на строку;
  один cross-family G4 read-only; связывающий свежий G5 (отдельная сессия) = CONFIRMED; сейм байт-идентичен;
  ветка НЕ на main. Evidence-class: **headless**.

### Leg 2 — engine-side тело (HELD до Leg 1 G5-CONFIRMED)
CALL: work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md (выпускает review-сессия по возврату Leg 1).
- Реюз low-poly скин-humanoid, привязанный к drop-in капсуле через НЕИЗМЕННЫЙ сокет-адаптер PlayerBodyView.
- Процедурная локомоция: планарная скорость + turn-rate из последовательных `BodyPose.Current` → blend-параметр
  (foot-slide на low-poly допустим); НЕ меняет сейм.
- Косметический PuppetMaster рэгдолл ИЗОЛИРОВАННЫМ слоем (write-only в косметические трансформы; на Knockdown
  blend анимация→физика, на GetUp blend назад к авторитетной позе из обёртки Leg 1); НИКОГДА не пишет в
  сокет/авторитетный трансформ. Базовый префаб работает без RootMotion.
- **Magenta-фикс (F2):** создать проектный low-poly материал и назначить ТОЛЬКО на 4 character-ассета
  (PlayerCapsule.prefab, PlayerDropIn_A/B.unity, PlayerDecoupleProof.unity); URP-guid не трогать; в RESULT
  отметить, что это НЕ resolve-ит guid в GlobalSettings/газовых сценах (там URP-дефолт, корректно).
- done_when: НЕ-тривиальный префаб под `Assets/**` (Test-Path existence, НЕ имя sibling-теста) инстанцируется через
  НЕИЗМЕННЫЙ сейм (сейм re-confirmed байт-идентичен); запись MCP/скрин под `docs/measurements/**` показывает
  idle→locomotion→knockdown→getup как персонажа; magenta закрыт своим материалом; owner-eye LOOK «да» (владелец
  запускает PlayMode: ходит, реальный flop, вставание БЕЗ рывка, ввод не двигает тело в нокдауне); один
  cross-family G4; связывающий свежий G5 (отдельная сессия) = CONFIRMED. Evidence-class: **engine + owner-eye**.

## 5. Scope hammer (cut list, ≥1 реальный рез)

- Полный лицевой/кистевой риг → parked (никогда в В2).
- Реакция от КОНКРЕТНОГО газа → В3 / Sc-reactions; В2 реагирует на абстрактный токен, не на газ.
- Сетевая консистентность рэгдолла (все клиенты видят один flop) → В3 / FishNet; В2 рэгдолл клиент-локальный косметичный.
- Нокдаун ОТ УРОНА (сила удара → интенсивность) → Sc-damage HELD; В2 триггерит state machine абстрактным событием.
- PuppetMaster active-muscle тонкий тюнинг сверх «flop+getup» → отложен; V2 доставляет базовый косметический blend.

## 6. Riskiest assumption (тест первым, дёшево)

«Реакция ГЕЙТИТ источник в нокдауне и на GetUp reconcile-ит авторитет ← rest, при этом сейм-типы байт-идентичны»
(F1). Убивающая сила: утечка даже в один кадр в авторитетный трансформ → коррупция детерминированного ядра и
разрыв В1-контракта. **Тестируется headless в Leg 1** (обёртка-источник — engine-free; вход-в-нокдауне и
reconcile-на-GetUp проверяются EditMode без рэгдолла и без крутилок) — ДО дорогого арта Leg 2. Owner-eye Leg 2
лишь подтверждает, что это ВЫГЛЯДИТ верно (нет рывка, реальный flop).

## 7. Lens sweep (CHARTER-линзы)

- core_gameplay_depth: **task** — тело, которое M1-5..7 роняют/двигают; ≈80% характера.
- coop_first: `not_needed` — сеть = В3 (cut).
- technical_feasibility: **task** — F1-контракт де-рискует сейм↔реакция seam headless до арта.
- commercial_traction / audience_workflow: `not_needed` сейчас — droppable персонаж кормит будущие capture-сцены (В3+).
- scope_production: `not_needed` — solo-scope держится (реюз-риг, ноль контент-производства, один материал).

## 8. Downstream (captured, НЕ строится здесь)

- Grid-ballistics = g-9c41 CORE slice (Ф1 одно тело ≈80% feel; Ф2 chains + loot/doors); блокирован core-маршрутом.
- Обязательная сетевая нога: 2-machine FishNet proof, что «авторитетная grid-баллистика + локальный косметический
  рэгдолл» консистентны между машинами; очередь с grid-ballistics core slice.
- A (полный риг) и C (процедурный) подходы → captures.

END_OF_FILE: live/indie-game-development/work/c-plan-characters-002-plan.md
