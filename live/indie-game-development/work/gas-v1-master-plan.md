# Gas V1 — принятый ступенчатый master plan

status: ACCEPTED
accepted: 2026-07-21
owner_verdict: `Окей, подтверждаю план.`

## Что мы строим

Gas V1 — это полный путь от уже выпущенного подробного ядра NearGas до газа, который:

- работает во время настоящей игры;
- появляется из игровых источников;
- понимает сгенерированный уровень;
- выдерживает полный масштаб;
- реагирует на двери и разрушения;
- влияет на игроков;
- одинаково считается в кооперативе;
- принимается одной постоянной Integration Lab.

Master plan показывает дорогу, зависимости и критерии готовности. Он не проектирует заранее
внутреннее устройство каждого узла. Перед реализацией каждого крупного узла проводится отдельный
owner-present подробный PLAN.

В частности, этот документ не выбирает:

- модель оптимизации полного уровня;
- binding min-spec hardware;
- точный Grid API;
- generated-level storage layout;
- parallel algorithm;
- multiplayer runtime.

## Откуда начинаем

Сейчас NearGas уже умеет детерминированно считать подробный газ по клеткам 50 см:

- массу и перенос;
- разные типы газа;
- вес;
- реакции;
- направленный поток;
- атомарный шаг и диагностическую наблюдаемость.

Но пока это выпущенная foundation, а не готовая система полного уровня. Она ещё не подключена к
настоящему production simulation loop, runtime-источникам, generated Level, живым изменениям мира,
authoritative игрокам и общей сетевой сессии.

## Вся дорога одной строкой

```text
Газ работает в игре
→ игровые объекты могут создавать газ
→ остальные системы безопасно читают его состояние
→ газ принимает настоящий сгенерированный уровень
→ выдерживает полный масштаб
→ реагирует на двери и разрушения
→ влияет на игроков
→ одинаково работает в кооперативе
→ собирается в одной настоящей игровой сцене
```

# Узлы Gas V1

## 1. Live deterministic Gas composition

**Что получаем для игры**

Газ действительно запускается и обновляется вместе с игровым миром. Это больше не отдельный
технический стенд: обычная игровая сессия имеет одного законного владельца Gas tick.

**Зачем этот узел**

Без настоящего игрового владельца тика источники, Level, игроки и сеть будут подключаться к
лабораторной заготовке, а не к production capability.

**Вход**

Выпущенная NearGas foundation и свежая product authority по simulation composition.

**Готово, когда**

Одинаковое начальное состояние и одинаковые упорядоченные действия всегда дают одинаковый Gas
result; текущие transport/types/reactions/forced-flow способности сохранены; незаконченный шаг,
случайный Unity event order или скрытая внешняя мутация не могут изменить результат.

**Внешний handoff**

Program получает bounded live-Gas capability. Gas не забирает session или transport ownership.

**Перед BUILD**

Отдельно принимается подробный план владельца Gas tick, composition seam, legacy cuts,
failure/atomicity boundary и доказательств.

---

## 2. Runtime source lifecycle

**Что получаем для игры**

Труба, оборудование, сценарное событие или другой игровой объект может создать утечку, изменить её,
переместить, выключить или удалить.

**Зачем этот узел**

Газ должен появляться потому, что что-то произошло в игре, а не только потому, что разработчик
заранее положил emitter в тестовый мир.

**Вход**

Принятый и доказанный узел 1.

**Готово, когда**

Create/change/move/disable/remove воспроизводимы; duplicate, stale и out-of-order команды имеют
однозначный результат или громко отвергаются; удалённый источник больше не производит массу.

**Внешний handoff**

Level, equipment и gameplay producers позднее отдают source commands, но не меняют внутреннее Gas
state напрямую.

**Перед BUILD**

Отдельно принимаются identity источника, command semantics, порядок, atomicity и migration от
generation-time emitters.

---

## 3. Committed Gas publication и ordinary digest

**Что получаем для игры**

После каждого законченного Gas tick существует одна официальная и неизменяемая картина:

- где газ;
- сколько его;
- какого он типа;
- что изменилось;
- совпадает ли результат у разных peers.

Эту картину могут независимо читать игрок, UI, Presentation, Grid и Multiplayer.

**Зачем этот узел**

Без общей подтверждённой картины нельзя надёжно показывать газ, применять последствия или
обнаруживать сетевое расхождение.

**Вход**

Узел 1. Точный adapter ждёт freeze общего Grid contract.

**Готово, когда**

Mid-tick read запрещён; два потребителя видят одну revision; чтение одним ничего не забирает у
другого; planted divergence меняет ordinary digest; медленный полный checksum остаётся
независимым audit oracle.

**Внешний handoff**

Grid получает только Gas-side adapter. Program/Multiplayer получает digest и ordered Gas events.
Gas не строит общий Grid commit clock или generic delivery.

**Перед BUILD**

После Grid freeze отдельно принимаются revision semantics, adapter, event order, digest coverage
и performance budget.

---

## 4. Generated-Level intake

**Что получаем для игры**

Генератор создаёт станцию, а Gas понимает её комнаты, коридоры, этажи, стены, двери, проёмы и
стартовые Gas inputs. Система больше не зависит от одной специально подготовленной комнаты.

**Зачем этот узел**

Static fixture не доказывает продукт. Настоящий Gas V1 должен работать с заменяемым output
генератора.

**Вход**

Узлы 1-2, общий Grid coordinate contract и Level/Generation profile contract.

**Готово, когда**

Один seed даёт одинаковый Gas intake; доказаны боковые, длинные и вертикальные пути; malformed
input отвергается; static и procedural sources проходят один заменяемый boundary.

**Внешний handoff**

Level владеет generation и topology output. Structure владеет правдой поверхностей и проёмов.
Gas возвращает intake validation и Gas-ready generation result.

**Перед BUILD**

Отдельно принимаются input vocabulary, validation, generation identity, replaceability и memory
ownership. Storage layout здесь не выбирается.

---

## 5. Full-level scale and optimization

**Что получаем для игры**

Gas доказан на целевом полном уровне:

- около 150 комнат;
- средняя комната примерно 8x4x8 м;
- вариация размера примерно 20-30%;
- длинные коридоры;
- вертикальные связки;
- восемь игроков, одновременно создающих активность в разных местах.

**Зачем этот узел**

Работа в нескольких комнатах не доказывает работу всей станции.

**Вход**

Узлы 1-4, representative generated profiles от Level, committed/digest surface, binding решение
`d-m1-min-spec-hardware-001` и отдельный owner verdict по optimization approach.

**Representative evidence**

- пустой уровень;
- один источник;
- распространение через несколько комнат;
- восемь разнесённых активных мест;
- заполненные, но уснувшие комнаты;
- длинный коридор;
- вертикальная связка;
- дверь или пролом, повторно будящий Gas.

**Stress/kill evidence**

- широкое заполнение существенной части уровня;
- много одновременно активных областей;
- худший допустимый generated profile;
- binding слабый CPU;
- отсутствие незаявленного роста allocations и memory.

Измеряются preparation time, memory, idle tick, ordinary active tick, digest cost, allocations и
worst observed spike.

**Внешний handoff**

Level даёт профили, но не выбирает Gas algorithm. Program/Multiplayer получает Gas-side load
evidence. Финальный живой восьмипользовательский тест не принадлежит внутреннему Gas BUILD.

**Перед BUILD**

Владелец отдельно получает сравнение допустимых моделей и принимает одну. Этот master plan не
выбирает между полностью подробной общей симуляцией, общей дешёвой дальней правдой с общими
активными подробными областями или грубой общей правдой с локальным visual refinement.

Giant hangars не входят в обещание Gas V1.

---

## 6. World-change reaction

**Что получаем для игры**

Открытая дверь, закрытая гермодверь, пробитая стена или другое принятое изменение мира действительно
меняет распространение газа.

**Зачем этот узел**

Без него Gas работает только внутри заранее неизменяемой коробки.

**Вход**

Узлы 3-4, Grid revision/change delivery и authoritative Level/Structure change.

**Готово, когда**

Принятое изменение меняет Gas flow; stale, duplicate, unfinished и mid-tick changes не влияют на
результат; масса и deterministic order сохраняются.

**Внешний handoff**

Level/Structure владеет изменением мира. Grid публикует revision. Gas владеет только своей реакцией.
M5 не закрывается без второго настоящего заинтересованного слоя.

**Перед BUILD**

Отдельно принимается Gas reaction plan после freeze change envelope. Gas не чинит exact-aperture
defect и не создаёт свою topology authority.

---

## 7. Player consequence output

**Что получаем для игры**

Контакт с газом начинает иметь authoritative игровое последствие: exposure, dose, hazard state или
другой принятый typed result.

**Зачем этот узел**

До него Gas остаётся техническим полем, а не игровой угрозой или возможностью.

**Вход**

Узел 3, Grid Object-to-Layer Resolver boundary и Character/Actor stable identity, committed footprint
и lifecycle.

**Готово, когда**

Нулевой overlap даёт нулевое consequence; enter/change/exit не дублируются; одинаковый контакт даёт
одинаковое накопление; view, ragdoll или cosmetic collider не становятся authority; stale footprint
отвергается.

**Внешний handoff**

Grid сообщает общий контакт. Character поставляет Actor identity/footprint и применяет Gas
consequence. Presentation только читает принятый результат.

**Перед BUILD**

Отдельно принимаются consequence vocabulary, accumulation, checksum/digest participation и граница
simulation truth versus balance. Точные цифры урона и экономика здесь не выбираются.

---

## 8. Multiplayer proof handoff

**Что получаем для игры**

Разные компьютеры получают один и тот же Gas result при одинаковых действиях игроков.

Gas обязан вернуть:

- deterministic reducer;
- stable identity и строгий order source/topology/player events;
- ordinary per-tick digest;
- громкое обнаружение divergence;
- load evidence восьми одновременно активных мест.

Program/Multiplayer владеет:

- session и peer identity;
- input delivery и общий order;
- связью network player с authoritative Actor;
- stall, leave, disconnect и host policy;
- transport и network runtime;
- настоящим two-machine composition;
- поздним eight-player session proof.

**Вход**

Узлы 1-7 и принятое scale evidence узла 5.

**Готово, когда**

1. Gas deterministic harness GREEN.
2. Ранний loopback/two-process proof GREEN.
3. Две настоящие сетевые машины получают одинаковые Gas revisions, digest и events.
4. Общий сценарий включает topology change и Actor contact.
5. Финальный eight-player proof возвращён Program/Integration.

**Внешний handoff**

Gas передаёт доказуемую simulation capability. Program/Multiplayer доказывает сеть и сессию.

**Перед BUILD**

Проводится отдельный Gas-side Multiplayer handoff PLAN. Если Program не может удержать session/runtime
работу в bounded slices, отдельный Multiplayer track создаётся только новой map-сессией.

---

## 9. One permanent Integration intake

**Что получаем для игры**

Одна настоящая сцена показывает полную цепочку:

1. уровень создан генератором;
2. в мире появляется настоящая утечка;
3. Gas распространяется по комнатам;
4. игроки открывают или ломают путь;
5. Gas реагирует;
6. Actor получает consequence;
7. peers видят одинаковый результат;
8. сцена держит принятый scale/performance profile.

**Зачем этот узел**

Это превращает набор отдельных доказательств в маленький, но настоящий фрагмент будущей игры.

**Вход**

Принятые outputs узлов 4-8 и Integration intake contract.

**Готово, когда**

Production command/event path используется без surrogate; generated Level действительно подаёт
input; topology change меняет Gas; Actor получает consequence; stale/wrong revision control падает;
capture воспроизводим; co-op claim появляется только после network gates.

**Внешний handoff**

Integration владеет сценой, общей проверкой и product proof. Gas возвращает capability drop и smoke
boundary, но не строит вторую Lab.

**Перед BUILD**

Проводится отдельный Gas drop acceptance PLAN. Он определяет Gas package, а не архитектуру всей Lab.

# Порядок и безопасная параллельность

## Обязательная первая линия

1. Подробно спланировать узел 1.
2. Реализовать и независимо доказать узел 1.
3. Подробно спланировать и доказать узел 2.
4. После Grid contract freeze закрыть точный plan узла 3.

## После committed boundary можно планировать параллельно

- generated-Level intake — после Level contract;
- world-change reaction — после Grid и Level/Structure contract;
- player consequence — после Grid Resolver и Actor contract;
- scale evidence suite — после binding min-spec.

## Последовательный финал

1. Full-level scale/optimization proof.
2. Gas Multiplayer handoff.
3. Program two-machine proof.
4. Final eight-player product proof.
5. Приём Gas drop одной permanent Integration Lab.

Grid остаётся Direction default. Gas plan не меняет глобальную очередь автоматически.

# Границы между треками

| Трек | Что приходит в Gas | Что Gas возвращает | Когда ждём |
|---|---|---|---|
| Grid | coordinates, committed revisions/changes, generic Resolver | Gas adapter, revision/digest/events, typed sampling | exact signatures ждут Grid freeze |
| Level/Structure | generated profiles, topology, authoritative changes, aperture truth | intake validation, Gas reaction evidence, scale measurements | world-change proof ждёт реальный change |
| Character/Actor | stable identity, committed footprint, lifecycle | authoritative Gas consequence | integration ждёт Actor contract |
| Program/Multiplayer | session, input delivery/order, peer identity, network runtime | deterministic reducer, digest, ordered events, load evidence | co-op ждёт two-machine и eight-player proof |
| Integration | один intake contract и permanent Lab | scene-ready Gas drop и smoke | Lab не заменяет track proofs |
| Wind | ничего в Gas V1 | сохраняется gas-local forced flow | independent Wind deferred |
| Presentation | accepted read model | visual/capture result | Gas не владеет rendering |
| Design/Canon | поздние игровые смыслы и content | требования к consequence/content vocabulary | balance и roster отдельно |

# Deferred, cuts и return triggers

- **Giant hangars** — не входят. Возврат: конкретный generated Level выходит за принятый профиль
  или владелец отдельно возвращает обещание.
- **Independent Wind Layer** — не создаётся. Возврат: отдельная map-сессия после появления producer,
  второго consumer, committed Wind state и доказуемого tick order.
- **Late join** — не входит. Возврат: отдельное решение по session model.
- **Dedicated server** — не входит. Текущий путь остаётся player-hosted input-lockstep.
- **Вторая permanent Lab** — не входит.
- **Gas authority тоньше 50 см** — не вводится. Возможный refinement остаётся read-only/off-checksum.
- **Lattice rooms или fixed-point inertia** — возвращаются только после owner-eye evidence, что
  текущего forced flow недостаточно.
- **Balance, production roster и каноническое содержание** — отдельные поздние plans.

Не возобновляются как launch authority:

- S0-S6;
- Sc-damage;
- Sc-catalog executor;
- Lv-ingest Phase 0;
- host-broadcast Gas state;
- destructive legacy RevisionFeed/LayerRegistry;
- interim coarse path как новая база;
- несколько постоянных Gas Labs.

Доставленные способности сохраняются, но старые road/status документы не открывают BUILD.

# Первый следующий подробный план

Первым открывается **узел 1 — Live deterministic Gas composition**.

Он превращает выпущенную foundation из лабораторного компонента в настоящую часть игрового мира,
не требует заранее выбирать scale architecture и не требует изобретать Grid signatures.

Следующая сессия остаётся owner-present PLAN. До отдельного принятия этого подробного плана BUILD
не открывается.

# Что не запускалось

При принятии master plan не изменялись product code, tests, assets, scenes или product docs.
Не запускались Unity, tests, build, Deliver или benchmarks. Не создавались product branch/worktree,
executor CALL, BUILD authority, optimization model, Grid API, Resolver implementation, Character
implementation, Multiplayer runtime, Wind surface, aperture repair или вторая permanent Lab.

END_OF_FILE: live/indie-game-development/work/gas-v1-master-plan.md
