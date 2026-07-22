# Диспетчерская демо — кандидат основы

Снимок: 22 июля 2026 года, после свежей остановки Grid до начала следующего плана.

Статус: **КАНДИДАТ**. Этот документ ещё не является принятым рабочим планом, новым milestone или разрешением запускать работу. Сначала точную версию должен попытаться опровергнуть отдельный свежий review, затем владелец сможет исправить или принять её.

## 1. Где здесь правда и зачем нужен этот документ

Диспетчерская не создаёт второй план проекта и не хранит собственную копию состояния.

| Что нужно узнать | Единственный источник | Роль этого документа |
|---|---|---|
| К каким результатам вообще идёт проект | [Дерево целей](../../TREE.md) | Показывает причинную дорогу только для текущей цели demo |
| Что прямо сейчас готово, ждёт, заблокировано или приостановлено | [Текущее состояние](../../NOW.md) | Делает одноразовый производный снимок для выбора волны |
| Что фактически произошло и чем доказано | [История результатов](../../history/) и журнал | Ссылается на доказательства, но не переписывает их как новую истину |
| Что нельзя вырезать из demo | [Принятый договор demo](stabilization-baseline.md) | Переводит договор в причинные результаты и проверки |
| Как устроена сама Диспетчерская | [Принятая замена старого подхода](../../history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md) и [карточка Диспетчерской](../../history/2026-07-22-s-map-launch-control-demo-control-room-refit-001.md) | Применяет принятые правила WIP, вопросов, доказательств и маршрутов |

Правило против теневого состояния:

- при расхождении всегда побеждает источник из таблицы, а соответствующая строка здесь считается устаревшей;
- статус работы, решение или доказательство нельзя поправить только здесь — сначала появляется законный RESULT в owning track, затем этот производный вид пересобирается;
- документ обновляется только когда меняется причинная логика demo, внешний маршрут, scope, важное доказательство, ресурсное ограничение или состав Active Wave;
- обычное завершение дня без материального изменения не создаёт новую версию и не требует ручной синхронизации;
- дневные четыре строки и ближайший Runway — представления этого же документа, а не отдельные артефакты;
- документ не отправляет задания сам по себе. После принятия Диспетчерская может назвать наблюдаемый результат, а целевой трек сохраняет право принять запрос, предложить эквивалентный результат или вернуть точный блокер и всегда сам выбирает технический способ.

Термины ниже:

- **результат** — наблюдаемое изменение игры, доказательства или способности выпустить demo, а не список действий;
- **Runway** — только ближайшая последовательность подготовленных результатов с реальными зависимостями и ресурсами, не календарная фантазия;
- **Active Wave** — работа, которой сейчас действительно разрешено занимать владельца, review, продуктовый слот и общие поверхности;
- **SUPPORTED / AT RISK / UNFORECASTABLE / MISSED** — соответственно маршрут поддержан доказательствами, находится под риском, пока не прогнозируется или уже пропущен.

## 2. Миссия и неизменяемая граница demo

Нужна маленькая, публично надёжная Steam-демоверсия **настоящей игры**, а не техническая лаборатория: минимум два игрока на двух компьютерах проходят короткую опасную экспедицию, понимают состояние газа и мира, совместным действием меняют ситуацию и получают понятный результат. Конкретные механики, содержание экспедиции и игровой feel определяет Canon, а не Диспетчерская.

### MUST — нельзя вырезать ради даты

1. Реальная сетевая игра минимум на двух компьютерах.
2. Один воспроизводимый путь от запуска до результата без помощи разработчика.
3. Видимая причинность: газ, мир, игроки и последствие связаны и понятны.
4. Хотя бы один момент сотрудничества реально меняет результат.
5. Один согласованный authoritative outcome; расхождение состояния становится громкой ошибкой, а не скрытой нормой.
6. Demo понятно без объяснения архитектуры.
7. Steam-установка, подключение и повторный запуск работают.
8. Публично утверждается только то, что доказано representative evidence.

### SHOULD — сохраняется только если помещается после MUST

- умеренная вариативность повторного прохождения;
- один сильный момент для capture;
- минимальный onboarding и необходимые настройки;
- ограниченный прогон с человеком вне текущей разработки, когда первый causal loop уже достаточно представителен.

### CUT — первая зона сокращения

- доказательство восьми игроков;
- полная экономика и progression;
- несколько карт и широкая генерация;
- полный набор газов, инструментов, реакций и level conditions;
- dedicated server, late join и полная матрица отказов;
- полное разрушение;
- полный будущий visual polish.

Quality floor остаётся прежним: representative run не падает и не застревает, чистая установка работает, две машины соединяются, старт и результат понятны, помощь разработчика не нужна. Дата фестиваля не может отменить этот минимум или честность claims.

## 3. Текущая правда о маршрутах

| Маршрут | Внешние точки | Статус сейчас | Почему |
|---|---|---|---|
| October 2026 | внутренняя проверка поддержки и cut — **10 августа**; регистрация — **31 августа**; optional Press Preview — **21 сентября**; обязательная передача на review — **5 октября**; событие — **19–26 октября** | **AT RISK + UNFORECASTABLE** | Содержание demo ещё не определено; постоянной start-to-result scene и двухмашинного proof нет; Program и Grid заблокированы, Level и Character не закрыты, Presentation не допущен, Marketing приостановлен; измеренной end-to-end скорости нет |
| February 2027 | регистрация — **10 января**; optional Press Preview — **25 января**; обязательная передача на review — **8 февраля**; событие — **22 февраля – 1 марта** | **законный fallback + UNFORECASTABLE** | Окно дальше, но неизвестные scope, integration throughput, network proof и Steam eligibility пока не позволяют обещать и эту дату |
| Денежная проверка | **11 декабря 2026** | **не заменена фестивалем** | Нужен результат больше $0, рекомендуемый — не меньше $1,000; при нуле и отсутствии правдоподобного пути пересматривается коммерческий подход или концепт |

10 августа — не новый M1 и не обещание готовой игры. Это последняя внутренняя точка, где October должен быть либо поддержан доказанной оставшейся дорогой и реальными ресурсами, либо владелец получает рекомендацию переключить планирование на February. Время на само сокращение scope и переключение маршрута входит в этот cut, а не считается бесплатным запасом.

Дополнительные правила маршрута:

- optional Press Preview можно вырезать первым; MUST и quality floor — нельзя;
- отсутствие реальной private Steam eligibility/registration route к 31 августа делает October **MISSED**, даже если код выглядит перспективно;
- отсутствие принятого кандидата в обязательном review к 5 октября делает October **MISSED**;
- guidance Steam review в несколько рабочих дней считается внешней очередью, а не скрытым буфером;
- сейчас не совершается ни публичное Steam-действие, ни трата денег, ни выбор названия/page claim.

## 4. Причинная Mission / Outcome Map

Это карта причин, а не последовательность технической реализации. Соседние capability-треки могут работать параллельно только там, где их границы уже устойчивы и они не занимают один и тот же owner/review/integration ресурс.

**Demo Contract**
→ **принят рабочий способ определять demo от целого к частям**
→ **принято фактическое Demo Experience Tree: путь игрока, минимальный scope, моменты причинности, сотрудничества, результата и требуемого звука**
→ **из него выведены наблюдаемые technical outcomes без выбора технического HOW**
→ **действующие Program / Grid / Gas / Level / Actor inputs законно закрыты и готовы к одной общей сцене**
→ **одна постоянная playable spine проходит start → expedition → consequence → outcome локально**
→ **две физические машины повторяют этот путь с одним authoritative result**
→ **неподготовленный человек понимает происходящее; presentation и placeholder audio закрывают смысл, а не маскируют механику**
→ **чистая установка, повторный запуск, stability, performance profile и честный capture приняты**
→ **private Steam eligibility и store materials собраны только из принятого proof**
→ **кандидат проходит Steam review**
→ **публичное demo доступно в выбранном окне и остаётся green на representative run**.

### Проверяемые ступени карты

| Ступень | Наблюдаемый outcome | Какое доказательство закрывает | Что она открывает | Cut / остановка |
|---|---|---|---|---|
| A. Способ проектировать demo | Владелец принял replacement workflow, где каждый нижний узел имеет родителя в опыте demo | Owner verdict + законный следующий parented outcome | Создание фактического Demo Experience Tree | Не строить portal, изображения или pipeline вместо workflow; неприкреплённые вопросы парковать |
| B. Фактическое demo определено | Принят один минимальный player journey с началом, угрозой, причинностью, co-op изменением и результатом; MUST/SHOULD/CUT применены | Owner/Canon evidence; видны открытые варианты и явные unknowns | Точным трекам можно назвать нужные observable outcomes | Не выбирать здесь mechanics; всё вне минимального пути сначала CUT |
| C. Technical work make-ready | Для каждого нужного capability известен owning track, принятый boundary, integration event, proof receiver и blocker | Current track plan/receipt + отсутствие semantic collision | Один bounded BUILD или closure за раз | Нет устойчивой границы, receiver или integration event — работа остаётся в очереди |
| D. Первая общая causal loop | Одна постоянная сцена локально проходит от старта до результата и показывает газ/world/player consequence | Machine evidence: reproducible run, negative failure visible | Ранний comprehension test, profiling и сетевой кандидат | Не расширять карту, roster или polish; чинить/резать то, что ломает spine |
| E. Реальный co-op | Две машины соединяются, проходят representative path и приходят к одному результату | Physical-machine/network evidence; divergence fails loudly | Claim «co-op demo», install repetition, capture | Не заменять двумя процессами на одной машине; eight-player/dedicated/late join CUT |
| F. Понятность и presentation | Человек без архитектурного объяснения понимает state, cause, cooperation и outcome; ключевые события слышимы там, где звук нужен для смысла | Unfamiliar-player observation + accepted capture + placeholder audio proof | Финальные readability/stability fixes и честные materials | Если смысл непонятен — redesign/cut/retest, а не поясняющий marketing text |
| G. Distribution и market readiness | Чистая Steam install/connect/relaunch повторяется; page/capture claims следуют accepted proof | Machine + market/Steam evidence | Mandatory review submission | Public claim без proof запрещён; broad campaign и SHOULD режутся первыми |
| H. Festival-ready | Review green, demo live, representative run всё ещё green, известен rollback/critical-only режим | Steam response + final machine proof | October или February event | Новые features заморожены; при провале обязательной даты маршрут MISSED |

Четыре класса evidence не заменяют друг друга:

1. **Machine** — код/сборка действительно работает на заявленной среде.
2. **Owner** — смысл, scope, feel и consequential cuts приняты владельцем.
3. **Unfamiliar player** — человек без подсказок понимает и способен пройти representative loop.
4. **Market / Steam** — install, eligibility, review и публичные claims подтверждены внешней поверхностью.

## 5. Неизвестные, которые нельзя превращать в проценты

- Фактический Demo Experience Tree и точный release scope ещё не приняты.
- Неизвестно, какие exact capability outcomes потребуются после определения player journey.
- Нет измеренной скорости прохождения цепочки «план → build → fresh review → integration → публикация → законное закрытие».
- Program cleanup технически сохранён, но не выпущен; его внешний Character evidence blocker не закрыт.
- Текущая Character lineage построена, но ещё ждёт owner look, независимую проверку, product publication checks и Direction close.
- Grid G01 физически опубликован, но current authority не доказывает собственное закрытие; G02 правильно остановлен до плана.
- Gas имеет принятый high-level route, но подробный node-1 plan ещё не принят, а build не открыт.
- Level имеет product-plan evidence без binding Direction receipt.
- Presentation опирается на legacy prerequisites и не допущен к новому work.
- Permanent start-to-result scene, representative local loop, two-machine proof, unfamiliar-player proof и Steam install proof отсутствуют.
- Binding min-spec намеренно отложен до representative build. Слабый Windows-ноутбук владельца — полезная будущая наблюдаемая среда, но сейчас не спецификация.
- Назначенный owner/track для audio meaning пока **UNKNOWN**. Это gap управления, а не разрешение молча отдать звук Presentation или Canon.
- Steam AppID/name/page/eligibility route в текущем evidence не доказан; Marketing приостановлен.
- Дальний объём после ближайшей make-ready цепочки — **UNKNOWN / UNBOUNDED**. Ни completion percentage, ни календарная дата из этого снимка не выводятся.

## 6. Ближайший Runway: сейчас → решение о поддержке October 10 августа

Runway событийный. Даты внутри него появляются только как внешние anchors; внутренние длительности не выдумываются.

| Порядок допуска | Outcome | Admission / dependency | Дефицитный ресурс | Доказательство завершения | Текущий disposition |
|---|---|---|---|---|---|
| 0. Текущая настройка управления | Точная основа Диспетчерской пережила свежую попытку опровержения и получила owner fix-or-accept verdict | Этот кандидат неизменен между review и verdict | Одна fresh review session; затем короткое owner decision | Claim-by-claim review RESULT + фактические слова владельца | **IN PROGRESS как setup, не product BUILD** |
| 1. Owner-primary | Replacement workflow Canon принят целиком и породил один parented outcome для определения фактического demo | Диспетчерская принята; owner-present Canon root остаётся свежим | Один owner-primary session; не совмещать с Gas decision batch | Accepted workflow artifact + owner words + lawful next root | **READY, но не запускать автоматически** |
| 2. Demo-definition | Принято фактическое Demo Experience Tree с минимальным journey, scope, звуковыми meaning points и открытыми вариантами | Ступень 1 закрыта; Canon сохраняет дизайн-власть | Owner/Canon judgment; fresh verification; никаких technical HOW | Accepted tree/ledger result; every technical demand has causal parent | **NOT YET DERIVABLE** |
| 3a. Закрытие существующего хвоста | Character lineage законно закрыта; внешний Character evidence defect либо закрыт, либо отделён точным blocker | Уже начатая работа, не relaunch | Owner look + независимая проверка + product/Direction closure capacity | Binding close receipts | **WAITING / продолжать только существующее closing** |
| 3b. Выпуск Program cleanup | Сохранённый cleanup повторно проверен на свежем состоянии и законно выпущен | Внешний Character defect закрыт; общий product gate green | Serialized product integration/publication slot | Published readback + valid Direction close | **BLOCKED; candidate не менять** |
| 3c. Grid make-ready | Current authority доказывает G01 close и eligibility следующей Grid-ступени | После принятия Диспетчерской свежо подтвердить, что blocker не изменился; целевой Grid track принимает/контрит запрос | Один product-process slot, target planning/review; shared gate files | Fresh binding proof G01 closed / next stage eligible | **первый кандидат на будущий background slot; сейчас BLOCKED и запрос не выдан** |
| 3d. Gas make-ready | Принят подробный node-1 plan живой deterministic composition | Отдельный owner slot; fresh product authority; важные composition choices показаны владельцу | Owner decision load; будущий Program integration surface | Owner-accepted detailed plan; build root ещё отдельный | **READY план, не BUILD; в очереди после primary** |
| 4. Первая causal spine | Accepted inputs собраны в одной постоянной сцене от start до outcome | Outcomes ступени 2 определяют нужные inputs; Program владеет integration | Shared scene/schema/settings; serialized integration; fresh verification и publication close | Representative local run | **UNKNOWN / UNBOUNDED до ступеней 2–3** |
| 5. Evidence ramp | Local machine → two-machine evening run → unfamiliar-player comprehension → install/capture | Representative candidate; named environments | Физические машины; несколько вечеров в неделю, максимум один реальный network run в день и только вечером; review/capture | Отдельные evidence receipts | **не планировать как ежедневную бесконечную retry-loop** |
| 6. Steam route | Private eligibility/registration → mandatory review → live | Route остаётся SUPPORTED; claims имеют proof; owner разрешил public/spend action отдельно | Steam external queue + owner/Marketing capacity | Steam receipts and green representative run | **Marketing PAUSED; public action закрыт** |

Ресурсные ограничения Runway:

- в один момент есть один owner-primary outcome; median административной нагрузки пилота не должен превышать 10 минут в день, обычный тяжёлый день — 20 минут, а день без нужного решения — 0 минут;
- fresh review, returned fixes, owner look, integration, publication и законное закрытие — реальная работа, а не бесплатный хвост;
- общие scene/prefab/schema/settings, simulation clock, contract authority, product gate files, integration slot, machine и owner-decision domain считаются collision surfaces;
- один вечер даёт максимум один настоящий network run. Перед ним AI/треки подготавливают candidate, checklist и expected evidence; провал превращается в один диагностический результат, а не в серию незапланированных owner retries;
- performance получает provisional budgets и ранний profiling на representative loop; binding min-spec появляется только после такой сборки на названной или валидированной слабой машине;
- Steam review и registration — внешняя capacity; внутренний план не может вернуть потерянную внешнюю дату дополнительным AI-параллелизмом.

## 7. Состояние каждого demo-critical трека

| Трек | Следующий outcome для demo | Полезное событие / окно | Зависимость | Collision risk | Законный disposition сейчас |
|---|---|---|---|---|---|
| Диспетчерская демо | Основа проходит fresh refutation и owner fix-or-accept; после принятия поддерживает один причинный план | До любого межтрекового запроса или признания плана действующим | Exact candidate + fresh current state | Теневая правда, лишняя админка, самопринятие собственного плана | Текущая setup-сессия; затем **один fresh review**, без foreign dispatch |
| Design & Canon | Сначала принять replacement workflow, затем отдельным outcome определить фактический Demo Experience Tree | Первый owner-primary после принятия Диспетчерской; actual content — только после workflow | Владелец; принятый Demo Contract и portal boundary | Scope/claims/механики могут быть заморожены случайным техническим вопросом | READY owner-present, non-default; не считать workflow уже определённым demo |
| Program / Integration | Законно выпустить сохранённый cleanup; позже принять в одну permanent scene только доказанные demo inputs | После закрытия внешнего Character evidence defect; integration — после exact Demo Tree outcomes | Character closure, fresh product state, serialized publication | Общая scene, integration slot, stale WIN assumptions, незакрытый candidate | BLOCKED; не менять и не relaunch candidate |
| Character & Gameplay Contact | Закрыть текущую lineage; будущий Actor input вывести свежо из Demo Tree | Текущий close receipt; новый Actor outcome только после demo-definition | Owner look, independent review, product/Direction close | Расширение frozen lineage новым actor scope; owner review queue | WAITING, существующее closing продолжается; нового BUILD нет |
| Grid / World Change | Восстановить доказательство G01 close и следующей stage eligibility; технический план остаётся Grid | После принятого bounded request и target response; обязательно до повторного G02 pre-plan | Current product authority, target-owned plan/review | Shared spatial contract и product gate files; лечение predecessor внутри G02 | BLOCKED before plan; не relaunch. Первый кандидат на свободный background slot после fresh admission |
| Gas Simulation | Принять подробный план одного live deterministic production tick; build только отдельным решением | Следующий свободный owner-planning slot после primary; exact Grid adapter — после Grid freeze | Released NearGas, Program composition surface, будущий Grid interface | Simulation clock, shared composition, owner choice, premature adapter | READY plan/non-default; не маскировать owner plan под автономный background BUILD |
| Level & Environment | Получить binding Direction receipt для существующего LV0 plan; точный demo input вывести позже | Когда владелец активирует Level и после свежей сверки; content input — после Demo Tree | Current product/V31/home, accepted player journey | Scene ingestion/aperture/shared geometry | WAITING; старый root не relaunch |
| Presentation | Сначала пересверить read-model contract; затем доказать readability/performance/capture над representative events | После стабильных event semantics и доступных read models; capture — после representative loop | Current product contract, Demo Tree meaning, integrated loop | Legacy prerequisites, premature polish, визуал как ложная simulation authority | BLOCKED; никакого build до fresh reconciliation |
| Marketing & Audience | При поддержанном маршруте подготовить private Steam eligibility/admin; claims и capture только из proof | Решение о route 10 августа; registration 31 августа для October; proof-trigger позднее | Owner wake, Canon meaning, accepted machine/player evidence | Раннее публичное обещание, name/page scope, owner load | PAUSED; никакого public action/spend. Wake только по доказанному trigger |

## 8. Active Wave и правило пополнения

### Текущая setup-волна

- **Управленческий outcome:** закончить этот candidate → отдельный fresh review → owner fix-or-accept. Это временная установка системы, а не доказательство движения игры.
- **Владелец до готового review:** не нужен. После review нужен один короткий verdict по целому документу, а не серия разрозненных вопросов.

### Первая рабочая волна после принятия кандидата

- **Owner-primary:** принять Canon replacement workflow, который позволит строить actual Demo Experience Tree от целого player journey к дочерним outcome. Это ещё не выбор mechanics и не замена отдельной content-сессии.
- **Background BUILD limit:** 1.
- **Фактический inherited load:** выше лимита. Как минимум Character lineage находится в review/closing, а отдельный Program cleanup candidate ждёт release/integration. Оба считаются WIP до принятого закрытия или явного discard; их нельзя объявить свободной capacity только потому, что build-команда уже вернула RESULT.
- **Новый background BUILD:** 0. Сначала закрывается inherited queue. Grid-integrity — первый make-ready кандидат после освобождения capacity и fresh admission; Gas пока owner-present plan, не background BUILD.

Background-кандидат допускается только если одновременно доказаны:

1. принятая устойчивая граница;
2. полезность для всех живых demo-вариантов **или** названное событие будущей integration;
3. отсутствие semantic collision с активной работой;
4. независимый получатель evidence;
5. pinned base/input manifest и обязательная integration revalidation;
6. отсутствие незапланированного owner interruption;
7. target track принял outcome или вернул эквивалентный counter; технический HOW остался у него.

Capacity освобождается только после review, fix при необходимости, integration/publication и принятого close либо explicit discard. Один RESULT, commit, handback или «технически готово» слот не освобождает.

### Точные refill / replan / stop triggers

| Событие | Реакция Диспетчерской |
|---|---|
| Candidate принят владельцем | Сделать Canon workflow единственным owner-primary; перед любым Grid request перечитать NOW |
| Canon workflow принят | Открыть один parented outcome для actual Demo Experience Tree; не генерировать technical tasks до его содержания |
| Character/Program получают binding close | Пересчитать inherited WIP. Только при свободной capacity проверить admission Grid-integrity; ничего не relaunch автоматически |
| Grid blocker остаётся тем же и capacity свободна | Сформулировать для Grid только наблюдаемый outcome «доказан G01 close и eligibility следующей стадии»; Grid отвечает accept/counter/blocked и владеет планом |
| Gas owner-primary slot освободился | Провести существующий node-1 planning root; build открывается только после принятого detailed plan и свободного WIP |
| Появился exact Demo Tree outcome, меняющий capability need | Обновить causal map и запросы до запуска build; закрыть/park работу без causal parent |
| Review queue, blocker age, collision или owner load растут | STOP REFILL; закрывать один хвост, сокращать SHOULD/CUT, не повышать AI utilization |
| Representative proof опровергает comprehension, stability или route assumption | Redesign/cut/retest; пересчитать route, не объяснять провал маркетинговым текстом |
| К 10 августа October не SUPPORTED доказанной оставшейся дорогой и ресурсами | Рекомендовать владельцу переключить рабочий маршрут на February и выполнить cut, сохранив MUST/quality |
| Пропущена registration или mandatory review date | Пометить соответствующий маршрут MISSED; не изображать его живым |

## 9. Первый рабочий план-кандидат

План действует только после fresh review и owner acceptance этого документа. Он не обещает внутренние даты, которых evidence пока не даёт.

### Сейчас, оставшаяся часть 22 июля

1. Закончить exact candidate, открыть отдельный fresh review и не задавать владельцу промежуточные вопросы.
2. Fresh reviewer пытается опровергнуть источник истины, причинную карту, каждый current-track disposition, ресурсный Runway, route/cuts и четыре строки дня.
3. Если review чистый — показать владельцу один целостный fix-or-accept brief. Если refuted — исправить только доказанные findings и повторить fresh review; план не считается принятым.
4. После принятия, если у владельца остался один рабочий слот, owner-primary становится Canon workflow. Gas-план не конкурирует за тот же слот, а новый product BUILD не стартует.

### Следующие события, не выдуманные дни

1. **Workflow outcome:** принят способ строить Demo Experience Tree и parented work.
2. **Demo-definition outcome:** принят минимальный journey и из него выведены exact observable needs, включая audio meaning.
3. **Queue-drain outcome:** существующие Character/Program closure lineages либо законно закрыты, либо имеют один точный blocker/decision, без ложного освобождения WIP.
4. **Make-ready outcome:** первый свободный background slot получает лучший admitted result. По текущим фактам это Grid-integrity, но только если blocker остаётся свежим и Grid принимает request; Gas detailed plan остаётся следующим owner-present outcome.
5. **Playable-spine outcome:** owning tracks возвращают принятые inputs в Program integration; order и HOW определяются их планами, а не этим документом.
6. **Evidence outcome:** local representative run предшествует scarce two-machine evening run; затем unfamiliar-player, install/capture и Steam evidence.
7. **10 августа:** классифицировать October. Пока факты не меняются, текущий verdict остаётся **AT RISK / UNFORECASTABLE**, а не «мы успеваем».

### Четыре строки владельцу на оставшуюся часть 22 июля

1. **Изменение мира:** довести основу Диспетчерской до свежей проверки и одного решения владельца; после принятия — один фокус на Canon-процессе, который откроет построение фактического дерева demo.
2. **Доказательство:** отдельная свежая проверка не смогла опровергнуть точную версию, и владелец принял её; для Canon — принят весь процесс и появился один дочерний результат без выбора игровой механики.
3. **Фон:** новую техническую разработку не запускаем — Character и Program уже образуют незакрытую очередь; Grid заблокирован, Gas ждёт отдельного планирования с владельцем.
4. **Пополнение / пересчёт:** принятие Canon открывает фактическое дерево demo; законное закрытие Character и Program позволяет заново посчитать занятое место и первым проверить Grid; один возвращённый результат сам по себе место не освобождает.

## 10. Звук, performance, сеть и Marketing — где они входят

### Звук

- В первом Demo Experience Tree каждый важный момент помечается: должен ли игрок понять его без звука, со звуком или обоими каналами.
- Если comprehension зависит от звука, в первый representative loop входит дешёвый placeholder cue и отдельное наблюдаемое evidence.
- Production audio начинается только после стабилизации event semantics, чтобы не полировать событие, которое ещё меняется или будет вырезано.
- Диспетчерская обязана до make-ready назвать outcome и owning track для audio meaning. Сейчас owner **UNKNOWN**; Canon определяет смысл, но это не означает автоматическое владение производством звука.

### Performance и min-spec

- До representative build используются provisional budgets и раннее profiling на реальных тяжёлых местах.
- Binding min-spec сейчас не выбирается и не превращается в отдельную owner-задачу.
- Когда representative loop существует, слабый Windows-ноутбук владельца можно использовать как один named observation. Если он непредставительно слаб или неисправен, это будет evidence о машине, а не автоматически market requirement.
- При проблеме сначала сокращается активный объём, число одновременных ситуаций и visual cost из CUT/SHOULD; реальный two-machine proof не вырезается.

### Network ownership и редкие прогоны

- Program/Multiplayer владеет session/runtime proof и authoritative-result environment; Gas, Grid, Level и Character возвращают inputs, но не присваивают сеть.
- Реальный owner network slot доступен несколько вечеров в неделю и максимум один раз в день.
- До слота должны быть готовы exact candidate, install/connect steps, ожидаемый outcome и способ собрать divergence/crash evidence.
- Неудачный прогон закрывается диагностическим результатом и новым admission, а не просьбой владельцу повторять попытки весь вечер.

### Marketing и Steam

- Private eligibility/admin route можно подготовить по внешней дате, но пробуждение Marketing требует отдельного owner-controlled события.
- Game title, public page, публичные аккаунты, spend и claims здесь не выбираются.
- Early tester recruitment и hypothesis test допустимы только после named trigger и на видимом proof; store claims ждут accepted representative evidence.
- Если October всё ещё SUPPORTED на route-check, владелец получает отдельное решение о private Steam/Marketing wake до registration. Если не supported — такой wake не используется для создания ложной срочности.

## 11. Self-check кандидата

| Требование foundation CALL | Результат самопроверки |
|---|---|
| 1. Authority, update triggers, anti-shadow | **PASS:** источники и invalidation описаны; отдельной state database, dashboard или daily artifact нет |
| 2. Causal map, separate routes, evidence, latest-safe cuts | **PASS:** одна причинная цепь, четыре evidence class, October/February отдельно, route/cut dates и MISSED rules явны |
| 3. Resource-feasible Runway | **PASS:** owner/review/integration/publication/shared surfaces/machines/evening slots/Steam queue учтены; дальняя работа UNKNOWN/UNBOUNDED |
| 4. Every demo-critical track | **PASS:** все девять текущих треков имеют outcome/gap, event, dependency, collision и lawful disposition без изменения root |
| 5. Active Wave and WIP | **PASS:** один owner-primary, background limit 1, inherited over-limit queue, zero new BUILD, admission/refill/stop rules; RESULT не освобождает capacity |
| 6. First plan and four-line day brief | **PASS:** план событийный; четыре строки содержат world change, proof, background truth и refill; Grid/Gas disposition выведен из current evidence |
| 7. Demo boundaries unchanged | **PASS:** MUST/SHOULD/CUT, quality, claims, money gate, min-spec deferral и limited network slots сохранены; mechanics/HOW/public action отсутствуют |
| 8. Candidate then fresh review | **PASS FOR ROUTING:** документ явно не принят и открывает ровно один отдельный refutation review; принятие владельца ещё не заявлено |

## 12. Source / evidence matrix

| Утверждение | Свежий источник |
|---|---|
| Договор demo, quality floor, Steam anchors, money gate | [Принятый stabilization baseline](stabilization-baseline.md) — только сохранившиеся release facts, без superseded M1/процентов |
| Единственная Диспетчерская, WIP, question firewall, audio/min-spec/network правила | [Принятый replacement contract](../../history/2026-07-22-s-work-launch-control-m1-superseded-by-demo-control-room-001.md) |
| Текущая карточка цели и право на bounded outcomes | [Принятый refit](../../history/2026-07-22-s-map-launch-control-demo-control-room-refit-001.md) |
| Все статусы и ordinary roots | [NOW после свежего Grid result](../../NOW.md) |
| Program cleanup blocker | [Program blocked receipt](../../history/2026-07-20-s-work-program-v2-legacy-lab-purge-deliver-blocked-001.md) |
| Character closing | [Текущий Character root](../c-exec-char-v2-body-rig-ragdoll-build-001-call.md) и receipts в NOW |
| Grid G01/G02 truth | [Свежий pre-plan result](../../history/2026-07-22-s-work-grid-v1-g02-preplan-g01-integrity-blocked-001.md) |
| Gas route и node-1 plan status | [Принятый Gas master-plan result](../../history/2026-07-21-s-work-gas-v1-master-plan-accepted-001.md) и [текущий planning root](../c-work-gas-v1-live-composition-plan-001-call.md) |
| Canon workflow boundary | [Принятый Markdown-first contract result](../../history/2026-07-22-s-work-g-d3a8-markdown-first-portal-acceptance-001.md) и [текущий workflow root](../demo-workflow/c-work-g-d3a8-demo-workflow-rebuild-001-call.md) |
| Level, Presentation, Marketing status | Их current roots, перечисленные в [NOW](../../NOW.md); никаких новых планов за них здесь нет |

END_OF_FILE: live/indie-game-development/work/launch-control/demo-control-room.md
