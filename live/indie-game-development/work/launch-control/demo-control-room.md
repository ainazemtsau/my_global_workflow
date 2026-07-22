# Диспетчерская демо — принятая operating strategy

Снимок: 22 июля 2026 года, после отдельного owner verdict по полной стратегии.

Статус: **ПРИНЯТАЯ СТРАТЕГИЯ ДЛЯ ПЕРВОГО СОБЫТИЙНОГО ЦИКЛА**. Владелец сначала выбрал вариант `A` для разделения «Demo Skeleton → Canon Hook Discovery → Demo Contract», затем после показа всей стратегии ещё раз ответил `A`. Второй ответ принимает стратегию целиком: динамическую Диспетчерскую, Demo Skeleton, ограниченный Canon Hook Discovery override, versioned Demo Contract, причинную дорогу к proof и честные October/February routes. Это принятие управления, а не product result: фактическое изменение игры или внешнего мира по-прежнему **НЕТ**. Ни Canon, ни product, ни другой трек этой записью не запускается.

## 1. Где здесь правда

Диспетчерская не создаёт второй план проекта и не копирует состояние.

| Что нужно узнать | Единственный источник | Роль этого документа |
|---|---|---|
| К каким результатам идёт проект | [TREE](../../TREE.md) | Показывает причинную дорогу текущей demo-цели |
| Что сейчас готово, ждёт, заблокировано или приостановлено | [NOW](../../NOW.md) | Даёт fresh снимок для выбора следующей Active Wave |
| Что фактически произошло и чем доказано | [history](../../history/) и [LOG](../../LOG.md) | Ссылается на receipts, но не переписывает их как новую истину |
| Минимальная release/quality граница | [stabilization baseline](stabilization-baseline.md) | После owner verdict читается как **Demo Skeleton**, а не как выбранный hook или финальный Demo Contract |
| Как Canon строит demo от целого к частям | [Demo-Driven Design & Canon Workflow v1](../demo-workflow/demo-driven-design-canon-workflow-v1.md) | Сохраняет Canon design authority и parent trace; ниже записан один точный временный override до выбора hook |
| Почему это одна Диспетчерская | [replacement receipt](../../history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md) и [refit receipt](../../history/2026-07-22-s-map-launch-control-demo-control-room-refit-001.md) | Сохраняет один launch-control track, bounded outcome requests и authority целевых треков |

Правила против теневого состояния:

- при расхождении побеждает fresh source из таблицы;
- статус, proof или owner decision сначала появляются в законном RESULT owning track и только затем отражаются здесь;
- `track_wip_limit: 99` — совместимость формата, не target загрузки и не измеренная capacity;
- `NOW.next` не является selector и не управляет работой;
- Runway, Active Wave и четырёхстрочный Brief — производные виды этой стратегии, не новые системы;
- Диспетчерская может сформулировать наблюдаемый outcome. Целевой трек отвечает `ACCEPT`, `COUNTER` или `BLOCKED` и полностью владеет technical HOW;
- commit, handback или product RESULT без обязательных review/integration/Direction close evidence не освобождает ресурс автоматически.

Термины:

- **product / external-world result** — наблюдаемое изменение игры, build, поведения игрока, distribution или рынка; если его нет, пишется **НЕТ**;
- **enabling outcome** — решение, план или доказательство, которое уменьшает неизвестность, но не выдаётся за product result;
- **Demo Skeleton** — обязательная рамка масштаба, качества и проверки; она намеренно не выбирает игровую зацепку;
- **Demo Hook** — короткое обещание переживания: почему игрок захочет попробовать и запомнит demo;
- **Demo Contract vN** — выбранная владельцем, проверяемая и заменяемая гипотеза конкретного demo;
- **Runway** — ближайшая причинная последовательность результатов с реальными зависимостями;
- **Active Wave** — все одновременно допущенные независимые потоки, для которых хватает фактических ресурсов и есть observable exit;
- **SUPPORTED / AT RISK / UNFORECASTABLE / MISSED** — маршрут подтверждён, под риском, пока не прогнозируется или пропущен.

## 2. Demo Skeleton: пол качества, а не «постный контракт»

Нужна маленькая публично надёжная Steam-demo настоящей co-op игры. Она должна использовать реальные симуляции проекта и бить в одну понятную эмоцию, но сам hook ещё не выбран.

### Обязательная рамка

1. Короткий воспроизводимый путь минимум для двух игроков на двух физических компьютерах.
2. Симуляция создаёт решение и последствие, а не служит фоновым эффектом.
3. Есть один **signature moment**, который понятно описать одной фразой и хочется показать другому человеку.
4. Сотрудничество причинно меняет исход; второй игрок не является декоративным присутствием.
5. Начало, опасность, совместное действие и результат читаются без объяснения архитектуры.
6. Один authoritative outcome; расхождение состояния становится громкой ошибкой.
7. Чистая Steam-установка, подключение и повторный запуск воспроизводимы.
8. Масштаб ограничен: одна сильная loop важнее нескольких слабых систем.
9. У hook есть falsification test: заранее понятно, какое наблюдение заставит его исправить или заменить.
10. Публичные claims следуют только representative evidence.

### SHOULD

- умеренная вариативность повторного прохождения;
- один сильный capture beat;
- минимальный onboarding и необходимые настройки;
- дешёвый placeholder sound там, где без него теряется смысл;
- ранний тест с незнакомым игроком после появления representative loop.

### CUT первым

- восемь игроков, dedicated server, late join и полная failure matrix;
- несколько карт, широкая генерация, экономика и progression;
- полный набор газов, инструментов, реакций и условий;
- полное разрушение и широкий production polish;
- optional Press Preview, если она конкурирует с MUST.

Quality floor нельзя обменять на фестивальную дату: representative run не падает и не застревает, две машины соединяются, старт и исход понятны, помощь разработчика не нужна.

## 3. Полная причинная стратегия

```text
CURRENT TRUTH
  ↓
DEMO SKELETON
  рамка масштаба, настоящая co-op причинность, simulation, signature moment,
  quality floor и falsification — без выбранной механики
  ↓
CANON HOOK DISCOVERY
  2–3 сравнимых concept cards; реакции газовых сфер — обязательный кандидат,
  но не заранее выбранный победитель
  ↓ owner выбирает / исправляет / отклоняет
DEMO CONTRACT v1
  конкретное обещание игроку, короткий journey, signature capture,
  MUST/SHOULD/CUT и проверки; гипотеза меняется только по evidence + owner verdict
  ↓
CANON DEMO EXPERIENCE TREE
  experience spine → причинные дочерние outcomes → точные capability needs
  ↓
TARGET TRACKS: ACCEPT / COUNTER / BLOCKED
  каждый трек выбирает HOW и возвращает evidence
  ↓
INTEGRATED PROOFS
  permanent local loop → two-machine authoritative co-op → unfamiliar player
  → clean install/relaunch → performance/capture
  ↓
STEAM ROUTE
  eligibility/registration → review → live demo → October 2026
  либо evidence-triggered switch → February 2027
```

Ни одна стрелка не означает automatic successor. После каждого результата Диспетчерская перечитывает fresh truth и заново допускает 0, 1 или несколько совместимых потоков.

## 4. Canon Hook Discovery override и versioned Contract

Принятый Canon workflow обычно требует принятого parent. Здесь владелец явно разрешил один ограниченный pre-contract поиск, потому что Skeleton намеренно не выбирает «огонёк» demo.

### Точная граница override

- **missing parent:** выбранный Demo Contract;
- **временный parent:** принятый Demo Skeleton и это точное owner verdict;
- **outcome:** 2–3 сравнимых hook concept cards, не реализация и не дерево механик;
- **обязательный кандидат:** физические взаимодействия и реакции газовых сфер;
- **обязательное сравнение:** минимум один содержательно иной hook, чтобы газовый вариант не победил по умолчанию;
- **метод:** сначала paper/visual reasoning и уже существующее evidence; bounded prototype или playtest — только если без него нельзя различить конкретную гипотезу и только после отдельного законного допуска;
- **exit:** owner `choose / revise / reject`; выбранный concept становится входом Demo Contract v1;
- **expiry:** override исчезает сразу после owner verdict по concept либо при точном Canon `BLOCKED/COUNTER`;
- **запрет:** discovery не открывает implementation, потомков, portal, art pipeline, public claims или автоматический Canon successor.

Каждая concept card должна уместиться в один owner-readable экран и содержать:

1. hook одной фразой;
2. fantasy игрока;
3. короткую дугу `start → pressure → joint action → consequence → result`;
4. signature moment / capture beat;
5. почему co-op причинный;
6. какая реальная simulation создаёт игру;
7. минимальные capability outcomes без technical HOW;
8. что CUT;
9. falsification test;
10. главный риск October-route.

### Demo Contract v1 и последующие версии

Contract появляется **только после owner choice**. Он фиксирует выбранный hook, journey, promise, signature moment, MUST/SHOULD/CUT, representative test и известные unknowns. Это гипотеза, а не вечный lock.

Новая версия допустима, когда named evidence опровергает текущий hook или показывает существенно более сильный вариант. Замена требует:

1. evidence и предел его применимости;
2. видимую цену изменения для уже начатой работы;
3. что сохраняется, режется и становится устаревшим;
4. explicit owner verdict.

Пока Contract не принят, текущий Canon Demo Experience Tree pilot остаётся `WAITING`. Принятая стратегия делает Hook Discovery законным кандидатом следующего межтрекового outcome, но не меняет Canon root и не считается dispatch.

## 5. Событийный алгоритм Диспетчерской

### Admission loop

1. **READ FRESH:** NOW, новые RESULT/close receipts, blockers и реальные ресурсы.
2. **NAME GAP:** какой ближайший observable result уменьшает критический разрыв Demo Skeleton → Steam.
3. **BUILD RESOURCE GRAPH:** свободные agents; независимые worktrees/files; Unity Editor и shared scene/prefab/schema/settings; физические машины; owner attention; review, integration и publication queues.
4. **SCREEN CANDIDATES:** causal parent, observable exit, evidence receiver, target authority, bounded scope и отсутствие запрещённой semantic/physical collision.
5. **ADMIT 0 / 1 / MANY:** запускается столько независимых потоков, сколько фактически проходит screen. Ноль — законный ответ, если все кандидаты заблокированы или создают опасную очередь.
6. **OBSERVE EXIT:** accepted result, exact blocker, counter-outcome, failed evidence или explicit discard. Долгая работа остаётся WIP, но не блокирует независимый слот по названию.
7. **REFILL IMMEDIATELY:** любое событие возвращает к шагу 1. Нет утренней квоты, ожидания следующего дня или фиксированного числа background flows.

Owner-facing решения сериализуются в момент фактического внимания владельца, но за день их может быть несколько. Это scarce surface, не лимит «один вопрос в сутки». Review, integration и machines работают так же: считать нужно реальную очередь и collision, а не количество названий треков.

### Stop / replan triggers

| Событие | Реакция |
|---|---|
| Любой result, counter, blocker, failed proof или discard | Сразу fresh read и новый admission; слот не ждёт завтра |
| Owner concept choice | Собрать Demo Contract v1; Canon tree и product work не auto-launch |
| Contract принят | Reconcile текущий Canon pilot; только target `ACCEPT/COUNTER/BLOCKED` открывает следующий lawful route |
| Character получает binding close | Пересчитать review/product capacity; Program blocker может стать проверяемым, но не снимается автоматически |
| Grid PLAN или Gas PLAN возвращён | Не превращать план в BUILD без owner verdict и отдельного root |
| Queue/collision/owner load растут | Остановить refill на конфликтной поверхности; закрывать хвост или резать SHOULD/CUT |
| Representative proof опровергает hook, comprehension, stability или route | Redesign / cut / retest; при material hook change — новая Contract version с owner verdict |
| Нет кандидата с causal parent и observable exit | Активная волна законно равна нулю; записать точный blocker, не создавать busywork |

## 6. Текущий снимок девяти треков

| Трек | Fresh disposition 22 июля | Что это значит для первой волны |
|---|---|---|
| Launch Control | стратегия принята; один same-track execution continuation должен стать READY | Выбрать resource-feasible Active Wave; ничего не dispatch автоматически |
| Design & Canon | `WAITING` на owner-approved Contract по текущему pilot | Hook Discovery доступен только через принятый bounded override и lawful target response; существующий pilot не подменять |
| Character | `WAITING`, product review/closing уже идёт | Долгий inherited flow; не relaunch и не считать свободным до binding close |
| Program / Integration | `BLOCKED` внешним Character review-evidence defect | Сохранённый candidate не менять; после реального unblock перепроверить fresh |
| Grid | `READY` к owner-present G02 PLAN; G01 complete 1/11 | Возможный независимый planning flow, если есть product/worktree/review/owner capacity; BUILD не открыт |
| Gas | `READY` к owner-present node-1 PLAN | Возможный следующий decision flow; не автономный BUILD и может конфликтовать за owner attention |
| Level | `WAITING` на binding Direction receipt | Старый root не relaunch |
| Presentation | `BLOCKED` до fresh contract reconciliation | Не полировать отсутствующий representative hook/loop |
| Marketing | `PAUSED` owner-controlled load | Нет public action, name/page claim или spend |

Текущий actual result остаётся **НЕТ**. Приняты Canon workflow, Demo Control Room foundation и эта operating strategy; это enabling/management evidence, не playable proof.

## 7. Пример одного реального дня — не обещание запуска

Пример показывает алгоритм на текущих фактах. Это не расписание и не свидетельство, что перечисленная работа уже началась.

**09:00 — fresh admission.** Character closing продолжает долгий inherited flow. Program остаётся blocked. При наличии независимых agent/worktree/review surfaces Диспетчерская может одновременно рекомендовать: Canon Hook Discovery как owner-primary outcome и Grid G02 PLAN как отдельный planning flow. Gas PLAN не добавляется, если два решения создают owner queue; при file/editor/product collision Grid тоже не допускается. Поэтому допустимый размер волны в этот момент — 1, 2 или только inherited Character, а не заранее заданное число.

**11:30 — Canon cards вернулись до обеда.** Это enabling result, не product result. Не ждём завтра: сразу перечитываются NOW, owner availability, Grid/Character events и очереди. Если владелец доступен, освободившийся owner slot заполняется выбором/исправлением/reject hook. Если не доступен, Canon не выдумывает победителя; независимый Grid PLAN может продолжать работу.

**12:00 — владелец выбрал hook.** Сразу появляется следующий bounded outcome: Launch Control собирает Demo Contract v1 из выбранной card и Skeleton. Canon Experience Tree и implementation всё ещё не запускаются. Если Grid PLAN уже вернулся, его owner verdict ставится в ту же реальную очередь внимания, а не считается автоматически принятым.

**14:30 — Contract принят в примере.** Событие немедленно запускает новый admission: текущий Canon pilot сверяется и получает только lawful `ACCEPT/COUNTER/BLOCKED` route. Character может всё ещё закрываться часами; это не запрещает независимый Markdown/Canon flow. Program остаётся blocked до binding Character evidence. Gas PLAN допускается только если owner/review capacity освободилась и он не вытесняет demo-critical решение.

**Вечер.** Реальный network slot используется только при наличии representative build, двух готовых машин, install/connect checklist и expected evidence. В текущей правде такого build нет, поэтому «занять машины для прогресса» нельзя. Если к будущему вечеру candidate готов, один диагностический two-machine run может быть лучшим outcome; Unity Editor, shared integration scene, review или owner fatigue способны уменьшить wave до одного потока или нуля.

## 8. От Hook до integrated proof

| Ступень | Observable exit | Что открывает | Что не происходит автоматически |
|---|---|---|---|
| Hook Discovery | 2–3 complete cards + owner choose/revise/reject | Contract drafting | Прототип, дерево, BUILD |
| Demo Contract v1 | Owner-approved promise, journey, signature moment, cuts and tests | Canon Experience Tree reconciliation | Технические задачи |
| Demo Experience Tree | Принята experience spine и непосредственные causal children | Bounded capability outcome requests | Выбор HOW за треки |
| Target make-ready | Каждый нужный трек дал `ACCEPT/COUNTER/BLOCKED`, boundary, proof receiver и integration event | Bounded PLAN/BUILD lineages | Параллельный старт при collisions |
| Permanent local loop | Reproducible start → pressure → joint action → consequence → result | Early comprehension, profiling, network candidate | Scope expansion |
| Two-machine co-op | Две физические машины приходят к одному authoritative result; divergence fails loudly | Честный co-op claim | Eight-player/dedicated proof |
| Unfamiliar-player proof | Человек без архитектурного объяснения понимает state, cause, cooperation и result | Readability fixes and capture | Маркетинговое объяснение провала |
| Distribution proof | Clean Steam install/connect/relaunch + accepted capture | Mandatory Steam review | Public claims/spend без owner action |

Evidence classes не заменяют друг друга: machine, owner, unfamiliar player и Steam/market.

## 9. Steam routes и вычисляемый switch

### Official gates

| Route | Registration | Optional Press Preview review | All required items submitted for review | Event |
|---|---|---|---|---|
| October 2026 | 31 Aug 2026, 11:59pm PDT | 21 Sep 2026 | 5 Oct 2026 | 19–26 Oct 2026 |
| February 2027 | 10 Jan 2027 | 25 Jan 2027 | 8 Feb 2027 | 22 Feb–1 Mar 2027 |

Для October Steam требует публичную base-game store page, playable demo к событию, unreleased base game до 26 октября и допускает игру только в один Next Fest. Источники: [Steamworks October 2026](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english) и [Steamworks February 2027](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027).

October сейчас **AT RISK + UNFORECASTABLE**: hook, Contract, tree, permanent loop, two-machine proof, unfamiliar-player proof и clean install отсутствуют; measured end-to-end throughput отсутствует. February — законный fallback, но тоже **UNFORECASTABLE**, пока остаются те же неизвестные.

Switch не назначается произвольной датой. После каждого material event вычисляется:

```text
remaining_route = conservative measured duration of every unresolved critical-path outcome
                + external review/admin queues
                + time to execute the chosen CUT
                + owner/review/integration/machine margin

latest_safe_switch = 5 Oct 2026 - remaining_route
```

Пока хотя бы один critical-path duration не имеет evidence-bound estimate или путь не определён Contract/Tree, `latest_safe_switch = UNKNOWN`. Когда inputs появляются, October считается `SUPPORTED` только если registration остаётся достижимой и remaining route помещается до mandatory review с quality floor. Если текущая дата достигла вычисленной точки, а маршрут не supported, Диспетчерская рекомендует explicit switch на February и выполняет named CUT. Пропуск 31 августа или 5 октября сразу делает October `MISSED`; дополнительный AI-параллелизм внешнюю дату не возвращает.

Optional Press Preview и SHOULD/CUT scope уходят первыми. MUST, honest claims и two-machine quality floor не режутся. Денежная проверка 11 декабря 2026 остаётся отдельной: фестиваль её не заменяет.

## 10. Четырёхстрочный Daily Brief

Brief — только производный снимок текущей Active Wave, а не стратегия и не дневная квота. Текущий предиспетчерский пример:

1. **Product/external result:** **НЕТ** — игра, build и Steam-поверхность этой стратегией не изменены.
2. **Proof + limit:** владелец принял Demo Skeleton → Hook Discovery → Contract → Tree и event-driven Control Room; это доказывает способ управления, не hook и не playable demo.
3. **Missing + nearest outcome:** сильный hook и Contract v1 отсутствуют; ближайший кандидат — bounded Canon Hook Discovery с 2–3 cards, включая gas-sphere reactions, только через lawful target response.
4. **Other flows + next event:** Character closing продолжает inherited wait; Grid и Gas готовы только к отдельным owner-present PLAN, Program blocked; любой result/blocker/verdict вызывает immediate fresh refill, без fixed daily/background count.

## 11. Guardrails по звуку, performance, сети и Marketing

- Canon определяет смысл звука; production owner пока `UNKNOWN`. Placeholder cue входит рано, если без него непонятен causal moment.
- Binding min-spec не выбирается до representative loop. Сначала provisional budgets и profiling на named environments; слабый ноутбук владельца — observation, не автоматическая market specification.
- Program/Multiplayer владеет session/runtime proof; Gas, Grid, Level и Character возвращают inputs, но не присваивают сеть.
- Физический network run требует exact candidate, двух машин, checklist и evidence capture. Провал создаёт diagnostic result, не бесконечные owner retries.
- Marketing остаётся `PAUSED`. AppID/name/page, public accounts, spend и claims требуют отдельного owner-controlled события и accepted proof.
- Technical HOW, scene architecture, simulation contract и implementation остаются у owning tracks.

## 12. Acceptance receipt и self-check

Владелец сначала выбрал `A` для предложенной структуры. Затем ему была показана полная стратегия: Skeleton criteria, Canon override, concept-card contract, versioning, dynamic resource graph, immediate refill, текущие треки, full-day example, Steam gates/switch и четырёхстрочный Brief. После вариантов `A — принять всю стратегию / B — поправить / C — отклонить` он снова ответил exact `A`. Только второй `A` является whole-strategy verdict.

| Требование returning CALL | Результат |
|---|---|
| Fresh state and drift | **PASS:** HEAD `9cd9ff7c5949901fe70cbce65ff3827d559c00ac`, NOW blob `10fc7629fa01c1bdff318aef36222ae7f2900c16`, accepted foundation blob `70b9c9bad4c2f017f3d796be7c710fe9d38ce6b4`; девять current roots проверены, tracked drift отсутствовал |
| Complete schematic | **PASS:** current → Skeleton → Hook Discovery → Contract → Tree → target responses → integrated proofs → Steam/fallback |
| Event-driven algorithm | **PASS:** fresh resource graph, observable exits, immediate refill и динамические 0/1/many flows без дневной квоты |
| Revisable Contract + Canon opportunity | **PASS:** exact bounded override, 2–3 cards, обязательный gas-sphere candidate, owner choice и evidence-versioning |
| Full-day current example | **PASS:** before-lunch Canon result, immediate refill, long Character flow и named owner/review/integration/machine collisions |
| Steam route | **PASS:** official dates, honest UNKNOWN, cuts and computed evidence-triggered switch |
| Daily Brief | **PASS:** ровно четыре производные строки |
| Actual owner verdict | **PASS:** full-strategy options were shown; exact second `A` accepted option A. No foreign work was launched |

## 13. Source / evidence matrix

| Утверждение | Источник |
|---|---|
| Demo quality/release floor | [stabilization baseline](stabilization-baseline.md), reclassified by this owner verdict as Demo Skeleton rather than selected Hook Contract |
| Accepted Control Room foundation | [foundation acceptance RESULT](../../history/2026-07-22-s-work-launch-control-demo-control-room-foundation-accepted-001.md) and exact pre-strategy blob `70b9c9bad4c2f017f3d796be7c710fe9d38ce6b4` |
| Correction constraints | [two-strikes checkpoint](../../history/2026-07-22-s-work-launch-control-demo-control-room-first-operating-plan-checkpoint-001.md) |
| Canon workflow and current waiting pilot | [workflow](../demo-workflow/demo-driven-design-canon-workflow-v1.md), [pilot CALL](../demo-workflow/c-cartography-g-d3a8-demo-experience-tree-pilot-001-call.md) and [NOW](../../NOW.md) |
| Current nine-track dispositions | [NOW](../../NOW.md) and each listed root/receipt; Grid current truth includes [route repair](../../history/2026-07-22-s-repair-grid-v1-g02-false-g01-blocker-001.md) |
| October official gates and eligibility | [Steamworks October 2026](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october?l=english) |
| February official gates | [Steamworks February 2027](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027) |

END_OF_FILE: live/indie-game-development/work/launch-control/demo-control-room.md
