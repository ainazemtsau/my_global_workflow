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

## 10. Первая принятая Active Wave и четырёхстрочный Daily Brief

22 июля владелец сообщил доступный owner-attention точными словами `60 минут`, увидел fresh resource graph и выбрал exact option `A`. Принята волна размера **1**: зарегистрировать один bounded Canon outcome request о законности Hook Discovery. Это допуск target disposition, а не запуск Canon work и не обещание, что за час появятся карточки.

### Resource graph на момент verdict

- **Agents:** выполнялась только owner-present сессия Диспетчерской; активного product executor не было.
- **Worktrees/files:** Direction HEAD `8a352276`, NOW blob `0c8490a1`, strategy blob `aef6118`; tracked drift отсутствовал, чужая `.claude/` сохранена. Product `dev` и `slot/win-u1` были чисты на `1a6373b8`; запрос не касается product-файлов.
- **Editor/machine:** Unity, `dotnet` и Git work process отсутствовали; для target disposition они не нужны.
- **Owner/review/integration:** дефицит — 60 минут owner attention. Grid G02 и Gas node-1 требуют того же owner-present PLAN; Character candidate `caab93e0` имеет product G4/G5, но ещё не имеет Deliver/publication/Direction close и требует отдельного свежего Control admission.

### Выбранный поток

`c-outcome-canon-demo-hook-discovery-001` просит Canon вернуть только `ACCEPT`, `COUNTER` или `BLOCKED` на один observable need: 2–3 сравнимые concept cards, обязательно реакции газовых сфер плюс содержательно иной вариант, с owner choose/revise/reject exit. Текущий Canon pilot остаётся `WAITING` на owner-approved Demo Contract. Запрос не выбирает hook, не создаёт карточки, Contract, дерево, prototype/playtest или implementation.

**Observable exit:** точный target disposition с proof/limit/useful event либо blocker+unblock proof. **Immediate refill:** любой ответ, expiry или иной material result немедленно возвращает Диспетчерскую к fresh admission; daily boundary и fixed flow count отсутствуют.

### Daily Brief — ровно четыре строки

1. **Product/external result:** **НЕТ** — hook, Demo Contract и playable demo отсутствуют.
2. **Proof + limit:** стратегия и Canon workflow приняты; Grid G01 выпущен, Character candidate проверен, но это не demo hook и не закрытый Character result.
3. **Missing + nearest outcome:** ближайший пробел — сильный hook; первая принятая работа — законный Canon `ACCEPT/COUNTER/BLOCKED` на bounded discovery need.
4. **Other flows + next event:** Character остаётся inherited closing wait, Grid/Gas — отдельные owner-present PLAN; любой Canon disposition немедленно вызывает новый admission без automatic launch.

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

### First-cycle receipt

| Требование first-cycle CALL | Результат |
|---|---|
| Fresh identity and resources | **PASS:** 22 July 18:43 +03:00; HEAD `8a352276`, NOW `0c8490a1`, TREE `bd5903c4`, strategy `aef6118`; current roots/receipts, app tasks, product worktrees and processes were checked |
| 0/1/many Active Wave | **PASS:** owner saw one concrete size-1 wave with product result `НЕТ`, proof limits, exact surfaces, observable exit and immediate refill |
| Canon route | **PASS:** one auxiliary disposition request preserves the waiting pilot and requires target `ACCEPT/COUNTER/BLOCKED`; no concept wins by default |
| Other lineages | **PASS:** Character/Grid/Gas were excluded from new admission because they collide for owner attention or require a separate product Control route; every foreign root/status survives |
| Four-line Brief + verdict | **PASS:** exactly four lines were shown; owner inputs were `60 минут`, then exact verdict `A` |
| Activation boundary | **PASS:** only a ready disposition CALL is registered. Canon/product/foreign work, technical HOW and public action remain not launched; one same-track refill root holds the next event frontier |

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

## 14. Canon readiness refill — вторая принятая Active Wave

После первого Canon `COUNTER` владелец выбрал ровно одну новую волну точными
словами: `Так, давай сегодня вот именно это, следующие 60 минут, это задача, не
выдумывай ничего, вот именно нужно отправить запрос как минимум, чтобы начал. Не
знаю, займет 60 минут, не 60, именно чтобы канун, трек канона доделал свои
планы. То есть полностью запустить, чтобы он там как-то эффективно, быстро
закончился своим и был готов к принятию наших требований.`

`60 минут` — блок внимания владельца, не обещание срока, SLA или hard stop.
Grid, Gas, Character, Hook cards и product work не выбраны.

### Fresh truth и resource graph

- **Product/external result:** по-прежнему **НЕТ**; Hook, Contract, playable
  demo и публичный результат отсутствуют.
- **Direction/Canon authority:** принятый Demo-Driven workflow rebuild уже
  binding-закрыт receipt `s-work-g-d3a8-demo-workflow-rebuild-accepted-001` и
  опубликован во внешний Canon как `6296cdbe`; его нельзя ложно переоткрывать
  как незавершённый.
- **Новая lineage:** live owner authority сообщает о более свежей
  process/plan работе, но committed Direction state, clean внешний Canon и
  доступные Codex receipts не дают ей stable id. Это обязательный первый proof
  target request, а не разрешение придумать внутреннюю задачу.
- **Split surface:** внешний Canon одновременно показывает Demo-Driven v4 в
  `AMENDMENTS/CONSTITUTION/QUEUE/board` и старый v3 во входных
  `README/START/SESSION`. Это material evidence для reconciliation, но не
  доказательство scope новой lineage.
- **Agents/tasks:** доступен completed task применения workflow и live source
  task с owner authority; отдельного active Canon execution task при admission
  не найдено. После commit target request явно dispatch'ится в новую свежую
  Codex-задачу.
- **Files/worktrees:** Direction стартовал с clean tracked HEAD `a69718ca`,
  NOW blob `d601626`, strategy blob `c1d4f29`; внешний Canon clean и совпадает
  с `origin/main@6296cdbe`. Чужой untracked `.claude/` не затрагивается.
- **Editor/machine/product:** Unity, dotnet и git work processes не запущены и
  для Markdown/task disposition не нужны. Product worktrees и shared runtime
  surfaces эта волна не занимает.
- **Scarce surface:** owner attention и один binding Canon Direction
  close/receipt. Временная оценка не заменяет receipt.

### Выбранный поток

Active Wave размера **1**: auxiliary request
`c-outcome-canon-current-process-plan-readiness-001` просит Canon вернуть только
`ACCEPT`, `COUNTER` или `BLOCKED` на один observable need — фактическая текущая
process/plan lineage binding-закрыта либо явно cut, demo-design routing surface
освобождена, Canon готов принять следующий lawful requirement.

**Observable exit:** exact stable lineage + owning Canon close/receipt + полный
учёт остатка планов + fresh Direction/external-Canon readback. Если lineage или
законный исполнитель не идентифицируются, exit — точный blocker и unblock
evidence, не выдуманный план.

**Immediate refill:** disposition, owner-verdict gate, exact blocker, expiry или
другой material result немедленно возвращают Диспетчерскую к fresh admission.
Ни request, ни его dispatch не меняют waiting pilot и не открывают Hook,
Contract, product, portal или автоматический successor.

### Daily Brief — ровно четыре строки

1. **Product/external result:** **НЕТ** — Hook, Contract, playable demo и публичный результат отсутствуют.
2. **Proof + limit:** workflow принят и опубликован как `6296cdbe`, но owner сообщает о более свежей незакрытой lineage; её stable id/receipt пока не найден, а внешние v3/v4 entry surfaces расходятся.
3. **Missing + selected flow:** ближайший результат — binding Canon readiness close; выбран ровно один READY outcome request, который сначала обязан назвать фактическую lineage.
4. **Other flows + next event:** Grid, Gas, Character, cards и product исключены; следующее точное событие — evidence-backed Canon `ACCEPT/COUNTER/BLOCKED`, после которого refill запускается немедленно.

## 15. План на 23 июля — принята Active Wave A

Владелец сообщил доступный ресурс точными словами: `Ну, где-то часов
двенадцать, если по сфокусированному времени.` После fresh-разбора Canon,
Character/Program, Grid, Gas и продуктовых поверхностей он выбрал предложенный
вариант точным ответом `A`.

Это принятие дневной управляющей волны, а не принятие Grid PLAN, Character
close или разрешение на BUILD. Никакая foreign work этой записью автоматически
не запускается.

### Fresh truth и предел доказательства

- **Canon:** обе вчерашние дочерние задачи завершены. Последняя вернула точный
  `BLOCKED`: отдельной текущей process/plan lineage не найдено, terminal rebuild
  остаётся clean на внешнем Canon `6296cdbe`. Canon не является сегодняшним
  потоком без нового authoritative pointer.
- **Character product evidence:** product candidate `caab93e0` уже входит в
  current product history через `756273e3`; последующие commits закрывают
  delivery evidence (`8596e7bd`), архивируют repairs (`f94a9068`) и записывают
  archive review (`0d576fca`). Это сильное product evidence, но не binding
  Direction close.
- **Program product evidence:** product history уже содержит purge close
  `3db67e8a` и released-slot receipt `f6e4f725`. Direction root всё ещё BLOCKED,
  поэтому capacity нельзя считать освобождённой без отдельной Direction-сверки.
- **Product refs/surfaces:** clean `dev/main/origin` readback находится на
  `1a6373b8`; `slot/win-u1` clean. Unity, dotnet и Git work processes не
  запущены. Product execution всё равно остаётся serial через Control/review.
- **Grid:** G02 ordinary root уже READY, G01 terminal 1/11, false G01 blocker
  снят. Полный owner-readable PLAN подготовлен как evidence, но ещё не принят
  владельцем и не открывает implementation.
- **Gas:** node-1 PLAN уже показан до owner-verdict gate, но в Wave A он
  остаётся очередью; второй BUILD не открывается.
- **Direction publication:** local truth clean на `0eb81876`, на три commits
  впереди `origin/main@1882e5e2`. Новая local Codex-сессия может читать exact
  commit; web/remote dispatch со старого main нельзя считать fresh.
- **Scarce surfaces:** примерно 12 часов owner attention, один owner-primary
  plan/review gate, один serialized product Control/review/Deliver путь и один
  background BUILD slot. Фактический throughput и completion dates UNKNOWN.

### Выбранные потоки

Active Wave размера **2**:

1. **Character close-readiness disposition.** Один auxiliary outcome request
   получает только `ACCEPT`, `COUNTER` или `BLOCKED` по достаточности текущих
   product/owner/G5 evidence для свежего binding Direction review/close.
   Ordinary Character root остаётся WAITING; Program остаётся BLOCKED до
   последующего binding события.
2. **Grid G02 owner-present PLAN.** Используется уже существующий READY root.
   Он показывает полный понятный PLAN и ждёт фактическое `accept / revise /
   reject`; prepared draft не считается вердиктом. BUILD и downstream lifecycle
   не открываются этой волной.

Gas, Canon, Hook, Contract, network-run, Unity scene, Marketing, portal и
второй product BUILD не выбраны.

### Контур 12 сфокусированных часов

1. **Первый блок, до одного часа:** Character request становится готовым к
   target disposition; владелец получает полный G02 PLAN. Никакой BUILD ещё не
   стартует.
2. **После первого binding события:** Character `ACCEPT` открывает только
   свежую законную close-сверку, затем отдельный Program refill; Grid PLAN
   verdict делает G02 только eligible для следующего admission. COUNTER,
   BLOCKED или revision вызывают немедленный replan.
3. **Средний блок, ориентир шесть-восемь часов:** после освобождения
   Control/review поверхности допускается максимум одна product execution
   lineage. При отсутствии binding gate слот законно остаётся пустым.
4. **Последний блок, минимум два часа:** review, Deliver, Direction receipt и
   readback фактического результата. Если G02 заблокирован или закрыт рано,
   следующий owner-gate может быть Gas node 1 PLAN; новый длинный BUILD в конце
   дня не открывается автоматически.

**Exact next event:** первый binding Wave A receipt — Character
`ACCEPT/COUNTER/BLOCKED` либо фактический owner verdict по существующему G02
PLAN, в зависимости от того, что произойдёт раньше. Он немедленно возвращает
Диспетчерскую к fresh admission.

### Daily Brief — ровно четыре строки

1. **Product result:** Character V2 и Legacy Lab purge уже находятся в product history; Hook, Contract и playable demo отсутствуют.
2. **Proof + limit:** clean product `dev/main/origin@1a6373b8` содержит closing evidence, но product commits сами не являются binding Direction close.
3. **Missing + selected flow:** ближайший пробел — Character/Program Direction reconciliation; параллельно выбран owner-verdict по существующему G02 PLAN.
4. **Other flows + next event:** Canon остановлен, Gas в очереди; первый binding Character disposition или фактический G02 PLAN verdict вызывает немедленный refill без automatic BUILD.

## 16. Wave A event refill — точный blocker до первого события

Fresh readback не нашёл событие, ради которого был открыт refill. Это не
отменяет принятую Wave A и не выбирает новую работу: Диспетчерская фиксирует
нулевой новый execution admission до появления binding evidence.

### Receipt / verdict / still-open truth

- **Character event: отсутствует.** Auxiliary request
  `c-outcome-characters-v2-published-close-readiness-001` остаётся `READY`; в
  Direction history и свежих Codex tasks нет его `ACCEPT`, `COUNTER` или
  `BLOCKED` RESULT. Ordinary Character root остаётся `WAITING`, Program root —
  `BLOCKED`. Product commits не меняют эту правду.
- **Grid event: отсутствует.** `c-exec-grid-v1-g02-common-spatial-map-002`
  остаётся `READY` только к fresh owner-present PLAN. Старый preparation task
  содержит proposed PLAN, но не слова владельца `accept / revise / reject` и не
  lawful receipt. Поэтому G02 implementation eligibility не возникла.
- **Product/collision drift: отсутствует.** `dev`, `main`, `origin/dev`,
  `origin/main` и `slot/win-u1` остаются clean на `1a6373b8`; новых commits и
  активных Unity/dotnet/git work-процессов нет.
- **Owner load:** принятые `примерно 12 часов` и вариант `A` остаются входом
  дневного плана. Сколько часов реально осталось сейчас — `UNKNOWN`: без нового
  owner input Диспетчерская не вычитает время и не изображает capacity.

### Свежий ресурсный граф

| Поток / результат | Текущий proof и предел | Дефицитная поверхность | Observable exit |
|---|---|---|---|
| Character close-readiness | Auxiliary request `READY`; product closing evidence есть, binding disposition нет | один fresh Direction review/close gate; owner LOOK/G5 evidence | committed `ACCEPT`, `COUNTER` или `BLOCKED`; сам disposition ordinary root не закрывает |
| Character ordinary + Program | Character `WAITING`, Program `BLOCKED`; product history впереди Direction | serialized Control/review/Deliver и binding Direction close | отдельный lawful Character close; только затем fresh Program refill |
| Grid G02 PLAN | Ordinary root `READY`; G01 1/11, false blocker снят, owner verdict отсутствует | owner-primary PLAN attention; затем serialized product Control/review | фактические owner words `accept / revise / reject` плюс lawful receipt; prepared draft не считается |
| Launch Control refill | returning READY id был вызван до события и потому consumed как exact blocker | один causal receipt, а не время или status | новый same-track root `BLOCKED` до первого из двух binding events |
| Gas | node-1 PLAN `READY`, но остаётся очередью после Wave A | отдельный owner PLAN gate; второй BUILD запрещён | только отдельные слова владельца в новом admission |
| Canon | ordinary pilot `WAITING`; readiness truth `BLOCKED` на missing authoritative lineage pointer | точный owning pointer/receipt и owner-approved Demo Contract | unblock proof из Canon; automatic launch отсутствует |
| Level / Presentation / Marketing | соответственно `WAITING` / `BLOCKED` / `PAUSED` | их собственные receipts, review или owner wake | только отдельный трековый event; Wave A их не меняет |

Новый execution admission — **0**. Единственный выбранный continuation —
same-track blocker `c-work-launch-control-demo-control-room-wave-a-binding-event-wait-001`;
он не запускает Character, Grid, Gas, Canon или product и не расходует
background BUILD slot.

### Daily Brief — ровно четыре строки

1. **Product result:** нового binding результата нет; product по-прежнему clean на `1a6373b8`.
2. **Proof + limit:** Character disposition не возвращён, а у G02 нет actual owner verdict; commits и prepared draft недостаточны.
3. **Missing + selected flow:** Wave A сохраняет Character close-readiness и Grid owner gate, но новый execution admission равен нулю.
4. **Other flows:** Gas остаётся в очереди, Canon — вне admission на точном blocker; все foreign roots и неизвестное оставшееся owner time сохранены.

**Exact next event:** первый committed Character
`ACCEPT/COUNTER/BLOCKED` receipt либо actual owner `accept/revise/reject` по
fresh G02 PLAN с lawful receipt — то из двух, что появится раньше.

## 17. Wave A event refill — Character review admitted

Первое binding-событие Wave A теперь действительно принято внутри
Диспетчерской: Character outcome request вернул committed `ACCEPT`. Владелец
правильно уточнил: `мы же сейчас с тобой в Launch Control работаем. Куда мне
вернуться, я не понимаю.` Возвращаться в другой Launch Control не нужно — эта
сессия и есть requester refill.

### Receipt / verdict / still-open truth

- **Receipt:** `history/2026-07-23-s-work-characters-v2-published-close-readiness-accept-001.md`.
  Он связывает candidate `caab93e0`, corrective BUILD `a45bd787`, integration
  `756273e3`, publication/control `413149ce`, owner LOOK, repaired binding
  product G5 и поздний GREEN Deliver/archive chain.
- **Verdict:** `ACCEPT` означает достаточность доказательств ровно для одной
  свежей binding Direction review/close-сессии.
- **Still open:** `c-exec-char-v2-body-rig-ragdoll-build-001` остаётся
  `WAITING`; Program остаётся `BLOCKED`. ACCEPT, product publication и старый
  G5 сами по себе их не закрывают.
- **Freshness boundary:** текущая Launch Control сессия не может одновременно
  быть отдельной свежей Character review-сессией. Поэтому нужен новый чат
  только для review, а не возвращение в другой управляющий чат.

### Свежий ресурсный граф

| Поток / результат | Proof и предел | Дефицитная поверхность | Observable exit |
|---|---|---|---|
| Character Direction close | ACCEPT receipt с exact product/owner/G5 evidence | одна отдельная fresh review-сессия; product read-only | committed `MET` закрывает ordinary root; `PARTIALLY MET / NOT MET` оставляет exact blocker |
| Program capacity | product purge/release evidence уже существует, но Direction root BLOCKED | serialized Direction reconciliation после Character close | отдельный Program refill только после lawful Character close |
| Grid G02 | владелец уже запустил owner-present PLAN chat; в Direction пока нет verdict receipt | owner attention; actual `accept / revise / reject` | lawful Grid receipt; prepared draft не считается |
| Product / machines | `dev/main/origin@1a6373b8` clean; активных Unity/dotnet/git work-процессов нет | review/control очередь, а не BUILD slot | новый product work не допускается этим refill |
| Owner load | исходно около 12 focused hours и вариант `A` | фактический остаток времени UNKNOWN | новый owner input либо material result, без вычитания времени по догадке |

Новый product execution admission — **0**. Новая выбранная работа — **1 fresh
Character Direction review**, которую владелец открывает отдельной сессией.
Grid не отменяется и не перезапускается; Gas, Canon и остальные foreign roots
не меняются.

### Готовое сообщение для новой Character review-сессии

> Продолжаем Character. Это новая свежая сессия для binding Direction
> review/close существующего root
> `c-exec-char-v2-body-rig-ragdoll-build-001`. Прочитай current NOW, frozen
> root CALL и committed close-readiness receipt
> `history/2026-07-23-s-work-characters-v2-published-close-readiness-accept-001.md`;
> read-only попытайся опровергнуть все семь done_when. Не перезапускай BUILD и
> не изменяй product. При MET законно закрой root; при PARTIALLY MET или NOT
> MET оставь точный blocker и lawful continuation.

### Daily Brief — ровно четыре строки

1. **Product result:** Character V2 остаётся опубликованным в clean `dev/main/origin@1a6373b8`; нового BUILD этим refill нет.
2. **Proof + limit:** committed ACCEPT связывает product, owner LOOK, G5 и Deliver evidence, но ещё не является binding Direction close.
3. **Missing + selected flow:** выбран ровно один новый шаг — отдельная свежая Character review/close-сессия; ordinary root WAITING, Program BLOCKED.
4. **Other flows:** уже запущенный Grid PLAN не тронут; Gas и Canon не запускаются, оставшееся owner time UNKNOWN.

**Exact next event:** committed fresh Character Direction review RESULT с
`MET`, `PARTIALLY MET` или `NOT MET` по всем семи done_when существующего root.

END_OF_FILE: live/indie-game-development/work/launch-control/demo-control-room.md
