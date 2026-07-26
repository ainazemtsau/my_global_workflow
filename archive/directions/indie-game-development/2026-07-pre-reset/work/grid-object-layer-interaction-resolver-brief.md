# Handoff в Grid/Layers: Object ↔ Layer Interaction Resolver

status: planning input; not a PLAN; not BUILD authority
owner: g-4b92 / Grid / Layers / World Change
requested_by: Gas Simulation planning, 2026-07-20
read_by: Grid/Layers map, converge/converge-arch and shape sessions before any object↔layer implementation

## Коротко

Во время восстановления Gas Simulation обнаружился общий игровой контракт, который нельзя
правильно решить внутри Gas: объектам игры нужен единый способ взаимодействовать с независимыми
пространственными слоями.

Пример: объект должен уметь определять, что он находится в газе. В будущем другой объект может
реагировать на иной слой, а один объект — на несколько слоёв. Если каждый слой самостоятельно
начнёт знать Player, Loot и все остальные типы объектов, возникнут дублированные пространственные
поиски и попарная связанность `объекты × слои`. Если всё собрать в центральный Grid, он станет
god object.

Рекомендуемое направление для Grid planning:

> Grid/Layers владеет общим пространством, committed-ревизиями и отдельным
> Object ↔ Layer Interaction Resolver. Слои сохраняют собственные данные и типизированные
> read-models; объекты объявляют только интересующие их слои; resolver пакетно пересчитывает
> затронутые пары и детерминированно выдаёт изменения контакта.

Этот документ описывает проблему, границы и обязательные свойства. Он **не выбирает сигнатуры,
контейнеры, layout, cadence или конкретные Unity/C# классы** — это обязанность Grid PLAN после
сверки текущего продукта.

## Жёсткое ограничение примеров

Вода и ветер ниже используются только как простые примеры расширяемости.

- **Water реализовывать не нужно.** Не создавать Water Layer, water fixture, water adapter,
  placeholder, stub, интерфейс с водной семантикой или будущий water backlog из этого handoff.
- **Wind реализовывать заново не нужно.** Не создавать новый Wind Layer, не проектировать ветер,
  не фиксировать его игровое поведение и не расширять текущий scope ради него.
- Текущий Gas-код уже содержит поведение, называемое «ветер»/forced-flow: целочисленный bias на
  газовых гранях, полезный в тестах. Оно может оказаться gas-local механизмом, а не независимым
  слоем. Этот handoff **не разрешает** его удалять, переделывать или объявлять общим Wind authority.
- Grid PLAN сначала классифицирует текущий ветер. Только если в продукте уже существует настоящий
  независимый Wind Layer с чистым read-model и подключение к resolver является маленьким
  behavior-preserving adapter-proof, PLAN может предложить его как **опциональный примитивный
  второй реальный consumer**. Это всё равно требует явного включения в утверждённый PLAN.
- Если независимого Wind Layer нет или его статус неясен, универсальность resolver доказывается
  нейтральными синтетическими TestLayerA/TestLayerB. Они не являются заглушками Water/Wind и не
  получают игровую семантику.

Итоговый scope: **создать и доказать resolver, а не создать набор будущих симуляций**.

## Почему вопрос возник сейчас

Первый предполагаемый Gas outcome был сформулирован как: один газ, несколько источников и
универсальный объект, который одинаково регистрирует `inside/outside`.

Простую gas-only проверку можно сделать напрямую по позиции объекта и газовой клетке. Но такая
связь не отвечает на продуктовый вопрос:

- кто владеет подтверждённой позицией объекта;
- как объект с объёмом занимает общие spatial addresses;
- как независимый слой сообщает, что его состояние изменилось вокруг неподвижного объекта;
- как новый слой подключается без правок Gas, Player и центрального Grid;
- как исключить полный перебор всех объектов, слоёв и клеток;
- как сохранить одинаковый порядок и результат в multiplayer;
- где заканчивается общий spatial contract и начинается семантика конкретного слоя.

Это не gas-only вопрос. Он влияет на Player, Loot, будущие симуляционные слои, multiplayer runtime
и Integration Lab. Поэтому владелец — `g-4b92 / Grid / Layers / World Change`, а Gas является первым
реальным consumer.

## Уже принятое основание

Текущая Direction architecture задаёт следующие ограничения, которые новый PLAN не должен молча
вскрывать:

1. Grid — общий координатный/адресный каркас, ownership map, commit clock и event transport; он
   не хранит данные всех слоёв и не считает их физику.
2. Каждый слой владеет своими данными и может иметь собственное разрешение. Gas авторитетно
   использует 50 см; Structure по текущему контракту использует 25 см.
3. Cross-layer чтение идёт только из committed read-model. Live mid-tick чтение чужого слоя
   запрещено; допустимая базовая семантика — один тик задержки.
4. Gas input-lockstep детерминирован по построению и имеет loopback-доказательство, но Gas ещё не
   доказан как реальный участник общей сетевой input-шины.
5. Integration Lab должна быть одна постоянная, однако трековая fixture/validator допустима, пока
   она остаётся необходимым доказательством.

Pointers:

- `live/indie-game-development/TREE.md` — `g-4b92` и соседние consumers;
- `live/indie-game-development/work/program-v2-integration-lab-plan.md` — M3/M4/M5 и Conflict Guard;
- `live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md` — §2 Facts 1–2,
  committed cross-layer read и текущий статус wind/lockstep.

Если current product SPEC/ADR/code противоречит этому описанию, Grid session возвращает
`CONFLICT / NEEDS RECONCILIATION` с обеими формулировками. Она не выбирает более удобную версию
молча.

## Какую проблему должен решить resolver

Нужно поддержать оба симметричных случая:

### Объект вошёл в неизменный слой

Actor/Entity committed-position изменился. Resolver проверяет только переместившийся объект и
только слои, указанные в его interaction profile.

### Слой пришёл к неподвижному объекту

Например, газ распространился в занятую объектом клетку. Слой пакетно публикует изменившиеся
spatial addresses/regions; resolver через object spatial index находит затронутые объекты и
перечитывает только нужные пары.

Чистые movement events пропускают второй случай. Collider на каждую клетку не подходит как
авторитетная основа из-за объёма, Unity/PhysX callback order, GC и determinism. Поэтому требуемая
модель — **authoritative state + batched dirty notifications**, а не «events вместо состояния».

## Рекомендуемое разделение ответственности

### Spatial/Grid Core

Владеет:

- общими spatial addresses и region/sector identity;
- детерминированной проекцией координат между разрешениями;
- layer/region ownership;
- committed tick/revision;
- базовым transport изменившихся spatial ranges;
- fail-closed поведением для stale и live mid-tick доступа.

Не владеет значениями Gas и семантикой Player/Loot.

### Simulation Layer

Каждый слой предоставляет поведенческий контракт:

- стабильный `LayerId`/kind;
- coverage/address projection;
- committed typed read-model;
- компактное описание изменившихся addresses/regions;
- возможность ответить на sample/query для занимаемого объектом пространственного объёма.

Layer не знает конкретные классы Player, Loot или Character View.

### Actor/Entity spatial authority

Предоставляет:

- стабильный object/entity id;
- committed occupancy: point, cells, bounds или другой принятый spatial footprint;
- изменение occupancy при move/spawn/despawn/teleport;
- interaction profile: какие Layer kinds объект действительно потребляет.

Unity Transform/View не должен молча становиться checksummed authority.

### Object ↔ Layer Interaction Resolver

Владеет:

- поиском только затронутых пар `object × subscribed layer`;
- чтением committed layer state;
- кэшем предыдущего подтверждённого контакта;
- детерминированным сравнением previous/current;
- выдачей типизированных `entered / changed / exited` либо эквивалентного принятого результата;
- canonical ordering и semantics checksum;
- счётчиками и telemetry горячего пути.

Resolver не применяет урон, силы или gameplay consequences. Consumer решает, что означает контакт.

## Что resolver не должен поглощать

### Layer ↔ Layer physics

`Wind → Gas`, `Structure → Gas` или любая другая связь слоёв не проходит через Object resolver.
Это отдельные consumer-driven contracts: слой читает committed read-model другого слоя и считает
своё следующее состояние. Новый слой не создаёт автоматическое взаимодействие со всеми соседями.

### Multiplayer transport

Resolver обязан быть детерминированным и пригодным к checksum, но не строит собственную сеть.
Общий Multiplayer Runtime должен предоставить tick/input/identity/order и authoritative entity
occupancy. До проверки product authority нельзя объявлять gas loopback общим multiplayer runtime.

### Gameplay semantics

Первая Gas-интеграция требует только `inside/outside`. Concentration, dose, damage, buoyancy,
wind force, Player/Loot handlers и balance не входят в resolver core.

### Integration Lab

Первое доказательство может жить в headless harness или bounded Grid-owned validator. Этот handoff
не запускает Integration Lab и не создаёт вторую постоянную сцену.

## Обязательные свойства расширяемости

Grid PLAN должен доказать или явно отклонить следующие свойства:

1. Новый слой подключается регистрацией/adapter-реализацией принятого контракта, а не правкой
   алгоритма resolver и всех существующих object types.
2. Новый object type объявляет интересующие Layer kinds, а слои не узнают его игровой класс.
3. Разные layer resolutions не требуют универсального наименьшего общего dense grid.
4. Payload остаётся типизированным: Gas presence не превращается в безымянное общее `value`.
5. Неподписанный слой не опрашивается и не создаёт contact state.
6. Отсутствующий слой — нормальное состояние, а не hard failure всей игры.
7. Spawn/despawn/teleport и изменение subscription profile имеют однозначную lifecycle-семантику.
8. Добавление слоя не включает автоматически Layer ↔ Layer coupling.

## Performance-инварианты

Главный ожидаемый выигрыш resolver — исключить стоимость
`all objects × all layers × all cells`.

План и доказательство должны обеспечить:

- работа пропорциональна переместившимся объектам, их subscriptions и объектам внутри dirty
  spatial ranges, а не размеру всего уровня;
- layer changes передаются пакетами/bitsets/ranges/chunks/regions, а не отдельным heap-event на
  каждую клетку;
- canonical batched buffers переиспользуются; горячий путь не создаёт GC на каждый contact;
- static/sleeping objects ничего не стоят, пока не двигаются и их область не меняется;
- object spatial index не сканирует весь entity roster на каждое изменение слоя;
- один объект, занимающий несколько адресов, не получает дублированный enter/exit;
- resolver telemetry отдельно показывает:
  `moved objects`, `dirty ranges`, `candidate pairs`, `sampled pairs`, `contact changes`,
  `allocations`, `elapsed time`;
- stress proof включает объект, движущийся через стабильный слой, и стабильный объект, на который
  приходит слой;
- authoritative proof не использует GameObject/Collider на каждую sim-cell.

Точный миллисекундный бюджет этот handoff не назначает: он зависит от binding min-spec CPU,
simulation tick и ожидаемого object envelope. Grid PLAN обязан назвать измеримый budget и профиль,
а не использовать слова «должно быть быстро».

## Determinism и multiplayer-инварианты

- Resolver читает только committed snapshots одного явно названного тика/ревизии.
- Same-tick live cross-layer/object read fail-closed.
- Candidate pair order и contact emission order канонические и не зависят от hash-map iteration,
  Unity callback order или thread race.
- Один и тот же object/layer input даёт один и тот же meaning result и checksum.
- Намеренное изменение object occupancy, layer sample или ordering member вызывает loud divergence.
- Internal resolver events не обязаны передаваться по сети при input-lockstep: они могут
  детерминированно выводиться на каждом пире. Grid PLAN не должен молча превращать их в network
  broadcast protocol.
- Raw Unity PhysX/Transform не объявляется общей multiplayer authority без отдельного решения.

## Минимальное доказательство универсальности

Не строить Water/Wind ради теста. Достаточно нейтрального набора:

1. `TestLayerA` и `TestLayerB` имеют разные разрешения и разные typed sample payloads.
2. Object profile A подписан только на A; profile B — на A+B; profile C — только на B.
3. Движение объекта в стабильный Layer A создаёт один enter, удержание не дублирует его, выход
   создаёт один exit.
4. Изменение Layer A вокруг неподвижного объекта создаёт тот же смысловой переход.
5. Layer B не опрашивается для object A.
6. Перестановка входных batch-порядков сохраняет одинаковый результат.
7. Stale revision и live mid-tick read отклоняются.
8. Stress-profile доказывает заявленную сложность и отсутствие per-contact GC.
9. После общего proof Gas может стать первым реальным adapter: один газ, generic object,
   `inside/outside`; это отдельная совместная Grid+Gas точка.

Если существующий независимый Wind Layer удовлетворяет ограничениям из начала документа, он может
заменить **один** синтетический consumer только по утверждённому PLAN. Его отсутствие ничего не
блокирует.

## Зависимости и разрешённая параллельная работа

### Grid/Layers может делать независимо

- current product inventory;
- R0 behavioral contract;
- architecture comparison и owner-readable recommendation;
- synthetic two-layer resolver proof;
- performance/determinism harness.

### Gas может делать параллельно

- сверку current engine/SPEC;
- один газ, источники и transport;
- gas-owned static topology fixture;
- deterministic harness;
- внутренний sample клетки;
- S4/scale работу, не зависящую от object contacts.

Gas не фиксирует универсальные public signatures и не объявляет `Object ↔ Gas` готовым до принятия
Grid contract.

### Multiplayer требует отдельной проверки

Read-only inventory должен ответить, существует ли общий product multiplayer runtime. Если нет,
Direction отдельно формирует Multiplayer outcome/track. Resolver не заполняет эту дыру собой.

### Совместная точка закрытия

Gas contact считается универсально доказанным только когда:

1. Grid/Layers resolver принят;
2. Gas adapter использует его без gas-only обхода;
3. generic object получает правильный `inside/outside`;
4. multiplayer proof использует общий runtime, если done_when заявляет multiplayer.

## Failure modes, которые PLAN обязан закрыть

- central Grid хранит данные всех слоёв и решает gameplay;
- каждый слой знает Player/Loot classes;
- полный перебор всех objects/layers/cells;
- per-cell GameObject/Collider/event allocation;
- contact пропускается, когда слой приходит к неподвижному объекту;
- duplicate enter/exit из-за multi-cell footprint;
- stale/live mid-tick read проходит тихо;
- unordered collection создаёт межпировый drift;
- resolver начинает считать Layer ↔ Layer physics;
- gas-only test выдаётся за доказательство расширяемости;
- Water/Wind создаются как «заглушки на будущее»;
- current gas-local wind случайно объявляется независимым Wind authority;
- resolver строит собственный multiplayer transport;
- Grid PLAN одновременно превращается в BUILD без owner verdict.

## Что должна вернуть Grid planning session

Ожидается не код, а owner-readable planning package:

1. Current product inventory: существующие grid/layer/entity/tick/event/read-model механизмы и их
   фактические владельцы.
2. Conflict table: Direction expectation против current product SPEC/ADR/code.
3. 2–3 архитектурных варианта, включая минимум central-god-object, per-layer observers и
   coordinator+resolver; каждый refuted по determinism, scale, extensibility и ownership.
4. Рекомендованная module/authority boundary.
5. Behavioral contracts для Grid, Layer, Entity и Resolver; HOW/signatures остаются PLAN-owned.
6. Dependency verdict по Multiplayer Runtime.
7. Отдельная классификация current wind: gas-local test mechanism или независимый layer; никаких
   продуктовых правок из этой классификации.
8. Малые dependency-ordered implementation legs, каждый с проверяемым результатом и rollback.
9. Synthetic proof matrix, performance envelope, counters и min-spec dependency.
10. Явный cut list, повторяющий запрет на Water/Wind scope, gameplay consequences и Integration Lab.

После owner approval этого planning package Grid может сформировать собственный bounded engineering
root по действующему product contract. Этот handoff сам по себе не является launch authority.

## Короткий текст для запуска Grid-сессии

> Прочитай `live/indie-game-development/work/grid-object-layer-interaction-resolver-brief.md` как
> автономный planning input для `g-4b92 / Grid / Layers / World Change`. Сначала сверь current
> product authority и верни owner-readable план Object ↔ Layer Interaction Resolver. Не запускай
> BUILD. Water и Wind в документе — примеры; не реализуй их и не создавай заглушки. Текущий wind
> только классифицируй; предложить его примитивным consumer можно лишь если он уже является чистым
> независимым слоем и это не расширяет scope.

END_OF_FILE: live/indie-game-development/work/grid-object-layer-interaction-resolver-brief.md
