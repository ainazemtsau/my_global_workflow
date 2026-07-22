# Release-control baseline — Demo & Launch Control

status: ACCEPTED 2026-07-22
owner_verdict: `ПРИНИМАЮ BASELINE И GATE 2026-07-26`
authority: этот документ управляет дорогой к публичному Steam demo на уровне результатов, сроков, рисков и cuts; он не заменяет планы продуктовых треков и не решает за них внутренний дизайн.

## Первый экран — вся стратегия

**Цель:** выпустить маленькое, публично надёжное Steam demo настоящей игры. В нём минимум два игрока на двух компьютерах проходят короткую повторяемую экспедицию, видят состояние газа и мира, совместным действием меняют ситуацию и получают понятный результат. Точные механики и контент выбирает Canon, а не Launch Control.

**Календарь:**

- условная цель — Steam Next Fest 19–26 октября 2026;
- принятый fallback — Steam Next Fest 22 февраля – 1 марта 2027;
- денежный gate из CHARTER — 11 декабря 2026: нужна внешняя платная проверка; рекомендуемый результат не меньше $1,000, минимальный — больше $0. Если денег нет и правдоподобного пути к ним тоже нет, пересматривается коммерческий подход или концепт.

**Текущий release milestone:** M0 — управление релизом становится рабочим. Продуктовая Program-дорога имеет 2 из 10 принятых технических milestones, но постоянной общей playable scene ещё нет. Cleanup-кандидат технически готов и проверен, однако его выпуск заблокирован внешним Character review-evidence defect.

**Ближайший gate:**

> 2026-07-26 — Launch Control operational: baseline принят, один ручной Daily Command завершён, первая законная work wave выбрана/запущена, по каждому demo-critical треку известны current truth / next release outcome / date range / blocker / collision risk, а determining chain и scenario forecast v1 обновлены.

**Цепочка, которая сейчас определяет срок:**

Character evidence defect закрыт → сохранённый Program cleanup законно выпущен → Grid contract и первый lawful Grid result → живой Gas loop → Level и Actor inputs → одна постоянная сцена от старта до результата → реальный co-op на двух компьютерах → presentation/stability/store readiness → Steam review.

**Первые пять дней:** принять baseline; один раз вручную составить Daily Command; выбрать первую законную волну без конфликтов; зафиксировать правду, blocker и диапазон даты каждого demo-critical трека; обновить цепочку срока и прогноз.

**Как работает ежедневное управление:** один короткий Daily Command показывает один главный фокус владельца, безопасную параллельную работу AI, работу в очереди, blockers/решения, текущую цепочку срока, прогноз и ближайший риск/cut. Следующий пересчёт происходит после результата, нового blocker, owner verdict или сдвига даты — не ради заполнения числа слотов.

## Основание

### Вводные владельца

- Нужен глобальный стратег, который ведёт к релизу, а не углубляется в чужую механику.
- Нужна целая стратегия с milestones и понятным ежедневным следующим действием.
- Параллельной работы должно быть много, когда она действительно безопасна.
- Идеи владельца — гипотезы, а не автоматические требования.
- Launch Control отвечает за бизнес-результат, календарь, cuts и удержание фокуса.
- October — условная цель; February — принятый fallback.
- Публичное demo требует реального co-op минимум на двух компьютерах; финальная проверка восьми игроков остаётся позже.
- Demo должно быть маленьким, но публично надёжным. Полная экономика для него не обязательна.
- Компактная повторяемая экспедиция подходит как рамка; точные механики и содержание принадлежат Canon.

Фактическое принятие: `ПРИНИМАЮ BASELINE И GATE 2026-07-26`.

### State evidence

- `live/indie-game-development/CHARTER.md` — миссия, риски и денежный gate 2026-12-11.
- `live/indie-game-development/NOW.md` — свежие статусы всех девяти треков, blockers, решения и открытые CALL.
- `live/indie-game-development/TREE.md` — границы направлений.
- `live/indie-game-development/work/program-v2-integration-lab-plan.md` — техническая Program-дорога и текущие 2/10.
- `live/indie-game-development/work/grid-v1-critical-path-plan.md` и текущие Grid receipts — Grid 0/11 и обязательный multiplayer handoff.
- `live/indie-game-development/work/gas-v1-master-plan.md` — принятый девятиузловой Gas V1 route.
- Текущие Canon, Marketing, Level, Character и Presentation receipts — только как факты о готовности, зависимостях и release-обязательствах; их внутренний дизайн здесь не меняется.

### Внешние даты Steam

Официальная страница October 2026: <https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october>

- фестиваль: 19–26 октября 2026;
- регистрация: до 31 августа;
- опциональная готовность к Press Preview review: 21 сентября;
- все обязательные материалы на review: 5 октября;
- к фестивалю нужны публичная store page и публично доступное demo;
- базовая игра должна оставаться upcoming и выходить после завершения фестиваля 26 октября;
- одна игра может участвовать только в одном Next Fest.

Официальная страница February 2027: <https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027>

- фестиваль: 22 февраля – 1 марта 2027;
- регистрация: до 10 января;
- опциональная готовность к Press Preview review: 25 января;
- все обязательные материалы на review: 8 февраля;
- также нужны публичная store page и публично доступное demo;
- базовая игра должна оставаться upcoming и выходить после завершения фестиваля 1 марта;
- после участия повторный Next Fest для той же игры невозможен.

## Demo Contract

Это release-обещание. Оно говорит, что должно быть доказано для публичного demo, но не предписывает внутреннюю архитектуру или точные игровые правила.

### Обещание игроку

Два или больше игроков входят в короткую опасную экспедицию, понимают состояние газа и мира, совместным действием меняют ситуацию и доводят попытку до ясного результата. Это кусок настоящей игры, а не лабораторный стенд.

### Форма одной попытки

Короткая подготовка → повторяемая экспедиция → понятный исход. Точные правила, длительность, инструменты, противники, условия и визуальный язык принимает Canon отдельными решениями.

### MUST — без этого публичного demo нет

1. Настоящее сетевое прохождение минимум на двух компьютерах.
2. Один воспроизводимый путь от старта до результата без помощи разработчика.
3. Видимая причинная связь «газ / мир / игроки / последствие».
4. Хотя бы один момент, где сотрудничество действительно меняет результат.
5. Один согласованный authoritative result; расхождение между машинами становится громким failure, а не скрывается.
6. Игрок понимает происходящее без объяснения архитектуры.
7. Demo устанавливается через Steam, соединяется и повторно запускается.
8. Публичные обещания описывают только уже доказанное.

### SHOULD — полезно, но можно cut без потери обещания

- небольшая вариативность повторных попыток;
- один сильный момент для capture;
- минимальный onboarding и необходимые настройки;
- ограниченный внешний прогон не владельцем. Точный набор участников, вопросы и численные thresholds принимаются отдельно.

### CUT — не входит в минимальное demo

- полный eight-player proof;
- полная экономика и progression;
- несколько карт и ширина генератора;
- полный roster газа, инструментов, реакций и level conditions;
- dedicated server, late join и полная матрица сетевых отказов;
- полное разрушение мира;
- полный будущий visual polish.

### Нижняя граница качества

Representative run проходит без crash и тупика; чистая установка работает; две машины соединяются; старт и результат понятны; разработчик не помогает пройти попытку. Численные thresholds и questionnaire сюда намеренно не добавлены — это отдельное решение, когда появится измеримый кандидат.

## Release milestones

Program milestones — вложенные технические доказательства. Они поддерживают этот release plan, но не заменяют его.

| Milestone | Результат | Владельцы результата | Вход | Exit gate | Полезная дата October / February | Явно не входит |
|---|---|---|---|---|---|---|
| M0 — Control operational | Принятый baseline, один ручной Daily Command, первая законная волна, свежая цепочка и прогноз | Launch Control + owner | Принят трек Launch Control и собрана текущая правда | Gate 2026-07-26 выполнен и принят владельцем | 26 Jul / 26 Jul | Новый dashboard, recurring automation, продуктовые изменения |
| M1 — Scope и Steam route frozen | Demo Contract, обязанности треков, cuts, min-spec/network owner и выбранный Steam route известны | Launch Control, Canon, Program, Marketing | M0; открытые решения названы | Один непротиворечивый release scope; владелец принял критические choices | 10 Aug / 30 Sep | Детальный gameplay design, полный контент, implementation |
| M2 — Technical spine | Чистая Program base, lawful Grid contract/result, живой Gas loop, Level/Actor inputs доступны для интеграции | Program, Grid, Gas, Level, Characters | M1; Character/cleanup blocker закрыт | Каждый input имеет accepted handoff и проверяемое evidence | 31 Aug / 30 Nov | Полный Gas V1, генератор во всю ширину, eight players |
| M3 — Маленькая игра от старта до результата | Одна постоянная сцена даёт повторяемую короткую экспедицию с причинной связью газа, мира и игроков | Program + все capability tracks; Canon принимает meaning | M2 | Чистый representative run от старта до результата без dev assistance | 14 Sep / 21 Dec | Несколько карт, полная экономика, полный roster |
| M4 — Real co-op candidate | Устанавливаемый кандидат работает на двух компьютерах и даёт capture/store materials | Program/Multiplayer, Presentation, Marketing | M3 стабилен локально | Two-machine evidence, повторный install/connect/run и честный capture | 21 Sep / 25 Jan | Eight-player final, dedicated server, late join |
| M5 — Steam release candidate | Кандидат стабилен, внешняя проверка принята, store page/demo submitted for Steam review | Launch Control, Program, Presentation, Marketing, owner | M4; page/app/account route готов | Required items submitted и release blocker list пуст | 5 Oct / 8 Feb | Новые features после freeze |
| M6 — Festival-ready live | Публичная page и demo доступны, monitoring/rollback известны, команда чинит только критическое | Launch Control + Program + Marketing | Steam review green, M5 accepted | Demo live до начала события; representative run остаётся green | 19 Oct / 22 Feb | Scope growth; только critical fixes |

## Текущее состояние по трекам

`Безопасно параллельно` означает отсутствие известного конфликта с текущей главной работой при соблюдении своего CALL. Это не автоматический приказ запускать всё сразу.

| Трек | Что уже доказано | Следующий release-результат | Blocker / dependency | Риск столкновения | Безопасно параллельно сейчас |
|---|---|---|---|---|---|
| Program — Integration Lab & Product Proof | Cleanup candidate `72c7c8c6` прошёл fresh G5 и normal gates 1829/1829; Program 2/10 | Законно выпустить preserved cleanup, затем вернуть чистую base и permanent-scene route | Внешний Character review-evidence defect делает Deliver RED | WIN-U1 и общий release path сериализованы | Нет, пока blocker не снят; только lawful closure |
| Launch Control | Трек принят; этот baseline и gate 2026-07-26 приняты | Один ручной Daily Command и первая законная волна | Нет продуктового blocker; нужен отдельный owner verdict на dry run | Owner review/decision load; нельзя подменить владельцев треков | Да, как management work без продуктовой мутации |
| Grid / Layers / World Change | Принятый 11-leg route; progress 0/11; owner-authorized V31 receipt repair READY | Lawful G01 plan close, затем общий Grid contract/result для consumers | Receipt-chain должна правдиво связать re-freeze; first four legs serial | Документы/process authority и будущие shared contracts — горячая поверхность | Только bounded текущий repair; Grid implementation ещё закрыта |
| Gas Simulation | NearGas foundation выпущена; девятиузловой Gas V1 plan принят | Принятый план и затем lawful live deterministic Gas composition | Exact Grid adapter ждёт Grid freeze; composition seam ещё не выбран | Shared Program composition и будущий Grid interface | Planning node 1 — да; BUILD только после отдельного verdict |
| Level & Environment | Product LV0 PLAN evidence существует | Binding Direction receipt и затем Level inputs для permanent scene | Текущий legacy root ждёт Direction reconciliation | Scene/ingestion surface пересечётся с Program integration | Сейчас нет: старый root не перезапускать |
| Character & Gameplay Contact | Character Leg 2 построен и находится в review/closing | Owner LOOK, binding G5, Deliver и Direction close; затем отдельный Actor input | Текущий product review/closing; его defect блокирует Program Deliver | Нельзя расширять frozen lineage новым Actor scope | Нет для повторного BUILD; только closure |
| Design & Canon | Один graph/Forge; c-001..c-003 и routing приняты; V1 visual question READY | Минимальные принятые meaning/readability решения для Demo Contract | Exact внешний вид и mechanics открыты | Решения могут раздувать scope или публичное обещание | Да, один bounded owner-present вопрос за раз |
| Presentation | Legacy route сохранён | Readability/capture/performance result над принятыми read models | Старые prerequisites не reconciled с V31/current product | Высокий риск строить над устаревшим simulation contract | Нет до fresh Conflict Guard review |
| Marketing & Audience | INOMAND/domain substrate и checkpoint существуют; track paused | Steam app/page/name/positioning/capture route, основанный только на proof | Paused owner-controlled; positioning зависит от Canon, claims — от product proof | Раннее обещание может зафиксировать неверный scope | Нет до owner wake; factual prep можно выбрать позже |

## Цепочка срока и работа рядом с ней

### Определяющая цепочка

1. Character evidence defect и Direction close.
2. Program cleanup release и освобождение чистой base.
3. Lawful Grid foundation/contract.
4. Live Gas composition.
5. Level и Actor inputs.
6. Одна permanent scene: start → expedition → outcome.
7. Two-machine network proof.
8. Readability, stability, install, capture и store submission.
9. Steam review и festival-ready release.

Любой сдвиг этих звеньев двигает release date, пока не доказана обходная дорога с тем же Demo Contract.

### Почти определяющая работа

- Steam developer/app/page/name route и регистрация;
- минимальные Canon decisions, без которых нельзя понять или честно описать demo;
- binding min-spec hardware и раннее profiling;
- owner review/G5/Deliver пропускная способность;
- Presentation/capture после появления устойчивого кандидата.

Эту работу можно вести рядом с цепочкой, но только когда она не создаёт ложное публичное обещание и не забирает горячую продуктовую поверхность.

## Прогноз

Это управленческие сценарии, а не статистическая вероятность. Проценты показывают текущую долю уверенности и пересчитываются после каждого результата, blocker или owner verdict. Сумма 100% описывает три взаимоисключающих окна при нынешней информации.

| Сценарий | Текущее окно | Условная уверенность | Должно оказаться правдой |
|---|---|---:|---|
| Оптимистичный | October Next Fest; required review к 5 Oct, festival 19–26 Oct | 15% | Character/cleanup закрываются немедленно; M1 принят к 10 Aug; регистрация/page route закрыты до 31 Aug; M2 к 31 Aug; permanent slice к 14 Sep; two-machine/capture к 21 Sep; после freeze нет серьёзной переделки |
| Наиболее вероятный | February Next Fest; review к 8 Feb, festival 22 Feb–1 Mar | 60% | Летом/осенью стабилизируются contracts и permanent slice; реальный co-op и store route проходят до 25 Jan; money gate 11 Dec даёт сигнал продолжать; scope остаётся в MUST |
| Консервативный | Mar–May 2027 — публичное demo или другая внешняя проверка вне February Next Fest | 25% | February сдвигается из-за network/integration/performance/store proof; качество MUST не режется; коммерческий route пересматривается по money gate |

### Пределы уверенности

- Нет устойчивой скорости прохождения новых Program/Grid/Gas legs, поэтому точный day-by-day forecast был бы выдумкой.
- October нельзя обещать: до регистрации меньше шести недель, а permanent scene и two-machine candidate отсутствуют.
- October нельзя автоматически списать: часть foundations и планов уже доказана, а Demo Contract намеренно мал.
- Выбор Next Fest необратим для этой игры после участия, поэтому October разрешается только при выполнении ранних gates; надежда не считается evidence.
- Первый обязательный пересчёт — в manual Daily Command; далее после каждого события, меняющего цепочку или scope.

## Риски, cuts и даты решения

| Риск | Ранний сигнал | Владелец | Предотвращение | Contingency | Именной cut | Последняя полезная дата решения |
|---|---|---|---|---|---|---|
| October превращается в ложное обещание | M1 не закрыт к 10 Aug или M2 явно не помещается до 31 Aug | Launch Control + owner | Еженедельный scenario forecast; работать только по цепочке | Переключить публичный route на February | Участие в October, но не quality floor | 10 Aug 2026; hard registration 31 Aug |
| Product pipeline остаётся RED | Character/Deliver blocker стареет, cleanup не released | Program + Characters | Один exact blocker owner, serialized closure, никаких новых features на WIN-U1 | Сохранить frozen candidate, направить review capacity на defect | Дополнительный legacy cleanup и feature refill | Ежедневно; первый stop 26 Jul |
| Сетевое доказательство приходит поздно | До M3 нет named two-machine owner/environment или state diverges | Program/Multiplayer | Рано назначить две машины и reproducible run | Выпустить только 2-player hosted path, если он выполняет Demo Contract | Eight players, late join, dedicated server | 14 Sep Oct / 21 Dec Feb |
| Scope/Canon расползается | Новый design вопрос не закрывает milestone или MUST | Launch Control + Canon | Каждый вопрос привязан к gate, риску или cut | Freeze одной компактной экспедиции | Полная economy, roster, tools, maps и conditions | Каждый Daily; финально 10 Aug |
| Performance/min-spec неизвестны | Нет binding hardware; full-level/representative run выходит за бюджет | Program + Gas + owner | Выбрать реальную слабую машину; профилировать representative slice рано | Уменьшить активный объём, число одновременных ситуаций и visual cost | Ширина уровня/симуляции, не двухмашинный proof | Hardware 10 Aug; первый profile 14 Sep |
| Нет честной store page/capture | App/name/page owner не назначены; M3 нечего снимать | Marketing + Presentation + owner | Factual prep параллельно; claims только из accepted proof | Одна простая честная page и один representative capture | Широкие каналы и campaign breadth | Route 10 Aug; registration 31 Aug; capture 21 Sep |
| Owner review становится bottleneck | Очередь verdict/G5/LOOK растёт, решения стареют | Launch Control + owner | Батч решений, один owner-primary, stop-refill при перегрузе | Сериализовать цепочку и закрывать один gate за раз | Параллельные эксперименты и SHOULD | Проверять каждый Daily; stop немедленно |
| Money gate не получает signal | К 1 Dec нет измеримого платного пути или offer | Launch Control + Marketing + owner | До декабря выбрать один прямой paid-validation route | Reframe commercial approach/concept | Каналы без измеримого signal | 11 Dec 2026 hard gate |

Cut никогда не отменяет MUST, реальный co-op на двух компьютерах или честность публичных claims.

## Release Directive

Release Directive — это краткий запрос Launch Control к владельцу трека о нужном release-результате. Он не редактирует чужой план, не создаёт новый тип пакета и не является инженерным приказом.

Обязательные поля:

1. **Release need** — зачем результат нужен demo.
2. **Affected gate** — какой milestone/gate он закрывает.
3. **Required outcome** — наблюдаемый результат, без внутреннего HOW.
4. **Evidence** — чем результат будет доказан.
5. **Useful date** — когда результат ещё помогает текущему окну.
6. **Consequence / cut** — что сдвигается или режется при пропуске даты.
7. **Source** — baseline, owner verdict или принятый state pointer.

Ответ целевого трека идёт через обычный CALL/RESULT:

- `ACCEPT` — результат и диапазон даты помещаются в текущий lawful route;
- `COUNTER` — предлагается эквивалентный release outcome, другой диапазон и явный trade-off;
- `BLOCKED` — называется точный blocker, кто его снимает и что докажет unblock.

Launch Control принимает release trade-off; владелец трека сохраняет implementation authority. Directive не меняет Canon, capability plan, product repo или OS сам по себе.

## Operating model

1. **Owner-primary:** в каждый момент у владельца один главный фокус — verdict, LOOK, unblock или решение с максимальным влиянием на цепочку.
2. **Parallel-safe AI:** запускаются независимые planning/research/review/execution legs с разными поверхностями и готовыми CALL.
3. **Serial / collision-risk:** общая code surface, contracts, merge/Deliver и один и тот же owner decision идут по очереди.
4. **Queue-next:** готовая работа известна заранее, но не стартует до освобождения dependency, surface или review capacity.
5. **Review/decision load:** незакрытая owner/G5/Deliver очередь считается реальной нагрузкой, а не бесплатным хвостом.
6. **Event-driven refill:** новый безопасный leg добавляется после RESULT, unblock, owner verdict или изменения риска — не ради заполнения лимита.
7. **Stop-refill:** прекращаем добавлять работу, если растёт очередь review, blocker стареет, появляется collision, forecast двигается или новый leg не закрывает Demo Contract/gate.
8. `track_wip_limit: 99` — compatibility value состояния, не capacity, не цель и никогда не показывается как `X/99`.

## Daily Command — точный формат

Один ручной Daily Command содержит ровно 12 полей:

1. **Цель релиза** — одно предложение, что публично доказываем.
2. **Текущий milestone** — где мы на release-дороге.
3. **Ближайшая дата** — следующий gate и его условие.
4. **Вчера** — только принятые результаты и новые blockers.
5. **Главное сегодня** — один owner-primary outcome.
6. **Параллельно сегодня** — только безопасные CALL/results с объяснённой независимостью.
7. **Заблокировано** — blocker, владелец и unblock evidence.
8. **Нужны решения** — короткий owner batch с рекомендациями.
9. **Цепочка срока** — звенья, которые сейчас определяют дату.
10. **Прогноз** — optimistic / likely / conservative и что изменилось.
11. **Риск / cut** — главный сигнал, prevention и named cut.
12. **Следующее обновление** — конкретное событие или время пересчёта.

Daily Command не обязан запускать максимальное число работ. Он обязан сделать следующий день честным и управляемым.

## Обязательная цепочка планирования

Daily Command нельзя составлять напрямую из списка готовых задач. Он всегда выводится сверху вниз:

**Demo Contract → release milestones → план текущего milestone → результат текущего дня → внутридневной refill.**

Для текущего ближайшего milestone Launch Control поддерживает один owner-accepted operating plan. В нём обязательно видны:

- точный exit gate и уже принятые результаты;
- весь оставшийся outcome-объём и явные unknowns;
- зависимости, определяющая и почти определяющая цепочки;
- результат каждого оставшегося дня только до ближайшего gate;
- owner-primary, parallel-safe, serial и queue-next размещение;
- календарный buffer, optimistic / likely / conservative forecast и consequence / cut при пропуске результата дня.

Точность скользящая: текущий milestone планируется по дням, следующий — по outcomes, зависимостям и диапазонам дат, более дальние — по gates и окнам. После RESULT, blocker, owner verdict, collision или сдвига даты план текущего milestone пересчитывается, и только затем обновляется Daily Command.

Список «что запустить следующим» без этой связи является черновиком и не может быть принят как Daily Command.

## Process Adaptation Contract

Launch Control может предложить изменить собственные cadence, поля Daily Command, правила refill/lanes/review, форму Directive, будущий dashboard или risk/capacity model, если есть evidence:

- реальная скорость результатов отличается от прогноза;
- blockers стареют;
- collisions или review queue повторяются;
- текущий формат создаёт лишнее трение;
- forecast систематически ошибается.

Материальное изменение сначала показывается владельцу с причиной, trade-off и expected effect. После фактического одобрения оно записывается обычным Direction RESULT/history.

Границы:

- Launch Control меняет свой управляющий процесс, но не внутренний план целевого трека;
- implementation/technical choices остаются у owning track и product contour;
- изменение общих правил `os/**` идёт отдельным `MAINTENANCE REQUEST`, не через этот baseline;
- никакая адаптация не ослабляет owner verdict, G5, Deliver или доказательства Demo Contract;
- compatibility `99` никогда не превращается в план capacity.

### Communication recovery

- Сначала показывать владельцу всю стратегию, потом детали.
- Писать обычным русским; внутренний термин сразу объяснять или не использовать.
- Чат — основной owner interface: владелец не обязан читать markdown-файлы; ids, paths, hashes и названия внутренних gates/checks не попадают в главный ответ без его запроса.
- Не превращать release session в gameplay workshop.
- Не открывать цепочку микрорешений, если можно показать один цельный draft.
- Идеи владельца оставлять гипотезами до явного verdict.
- Спорить со scope, календарной ценой и коммерческой пользой, а не автоматически соглашаться.
- Каждый разговор привязывать к milestone, дате, риску/cut или dispatch decision.
- После двух неудачных correction rounds делать checkpoint и свежую recovery-сессию.

## Будущий dashboard

Отдельный Launch Control dashboard пока **не создан**. После принятого manual Daily Command dry run он может быть рассмотрен отдельным CALL. Это только read-only render над принятым состоянием, а не второй источник правды.

Его первый экран прямо зеркалит 12 полей Daily Command:

1. цель релиза;
2. текущий milestone;
3. ближайшая дата;
4. вчера;
5. главное сегодня;
6. параллельно сегодня;
7. заблокировано;
8. нужны решения;
9. цепочка срока;
10. прогноз;
11. риск / cut;
12. следующее обновление.

Внутренние ids допустимы только мелкой ссылкой для traceability. `X/99` запрещён. Dashboard ничего не dispatch'ит и ничего не решает.

## Первый gate и единственное продолжение

Принятый gate:

> 2026-07-26 — Launch Control operational: baseline принят, один ручной Daily Command завершён, первая законная work wave выбрана/запущена, по каждому demo-critical треку известны current truth / next release outcome / date range / blocker / collision risk, а determining chain и scenario forecast v1 обновлены.

Владелец принял его вместе с baseline точными словами:

> ПРИНИМАЮ BASELINE И GATE 2026-07-26

Первый dry run был исправлен владельцем до принятия: Daily Command обязан выводиться из отдельного плана текущего milestone. Ровно одно текущее продолжение: `c-work-launch-control-m0-operating-plan-and-daily-command-001` — свежая owner-present сессия строит план M0 до 2026-07-26 и только из него выпускает новый Daily Command. Отдельный Launch Control dashboard, recurring control, Release Directive dispatch и продуктовая работа этим исправлением не открыты.

END_OF_FILE: live/indie-game-development/work/launch-control/stabilization-baseline.md
