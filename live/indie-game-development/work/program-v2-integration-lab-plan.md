# Program v2 — Integration Lab & Product Proof plan

owner: g-9c41 / Integration Lab & Product Proof
approved: 2026-07-20 — s-map-program-v2-hot-migration-route-001
last_verified: 2026-07-20 against current Direction and product V31 state; product facts must be refreshed by the next Integration Lab ownership shape
status: active global route; product implementation not started by this map

## Для чего существует этот файл

Это единый глобальный план доведения тестовой сцены до product proof. Он отвечает на четыре
простых вопроса:

1. На каком этапе находится общая сцена?
2. Что уже доказано, а что ещё осталось?
3. Какой результат должен передать каждый трек?
4. Что Integration Lab принимает следующим и почему?

Это не десятый трек и не замена `NOW.md`, `TREE.md`, SPEC/ADR или product PLAN. Integration Lab
владеет этим маршрутом и принимает capability drops; направления владеют своей реализацией и
своими доказательствами. Dashboard только отображает этот файл и живое состояние.

## Простая схема работы

```text
направление делает bounded work
        ↓
проверяет результат в своём fixture/lab
        ↓
возвращает six-line handoff через Direction RESULT
        ↓
Integration Lab проверяет seam + proof + общий smoke
        ↓
writer обновляет этот план и перегенерирует dashboard
```

Направление не редактирует этот файл и HTML напрямую. Если drop не принят, он остаётся в своём
направлении с названным blocker; Integration Lab не копирует незавершённую работу внутрь общей сцены.

## Authority и Conflict Guard

Перед каждой новой задачей сессия перечитывает текущие:

1. product code, product SPEC/ADR/PLAN и фактические validators;
2. `NOW.md`, `TREE.md` и релевантный принятый Direction evidence;
3. эту карточку маршрута как индекс ожидаемого результата.

Карточка не сильнее авторитетного продукта. Если название, предположение, seam или `done_when`
расходятся, сессия возвращает `CONFLICT / NEEDS RECONCILIATION` с двумя сторонами расхождения.
Нельзя молча выбрать более удобную версию и начать реализацию. После reconciliation writer обновляет
маршрут только через валидный Direction RESULT.

## Текущая картина

- Program v2 map, направления, handoff и dashboard настроены этой сессией.
- NearGas L1B V29 имеет терминальный product/Direction close: пять observation families, real
  loopback и binding fresh G5 выпущены на product revision `693e671b`. Старые внутренние пункты
  `L1B-Classify`, `L1B-Trace`, `L1B-G5` не являются оставшейся работой.
- Character Leg 2 построен и находится в review/closing. Frozen CALL нельзя запускать повторно или
  расширять новой Actor Layer задним числом.
- Level LV0 product PLAN reported RELEASED at `b1698170`, но binding Direction review отсутствует.
  Старый PLAN не перезапускается; проверка делается только при активации Level.
- V30 существует в Direction history как исторический route. Current engineering authority на
  `origin/main` — V31, и product уже имеет принятый process-only `re-sync:31`; V30 re-sync полностью
  superseded. Новый product root всё равно перечитывает current product authority, а не получает
  разрешение на feature автоматически.
- Static Integration Lab scene, универсальный Grid drop, живой Gas drop и остальные scene drops этой
  картой не заявлены как существующие.

## Прогресс общей сцены

Текущий этап: **M1 — current-authority entry доказан**.

Следующий рекомендованный шаг: **shape ownership общего Integration Lab entry перед M2 static shell**.

Счёт: **2 из 10 milestones приняты; 8 остаются**. Это счёт принятых результатов, не процент готовности
игры и не оценка effort.

- [x] **M0. Program map и control plane** — направления, владельцы, Conflict Guard, global plan,
  six-line handoff и простой dashboard приняты.
- [x] **M1. Current-authority entry** — V30 route проверен и superseded: `origin/main` имеет current
  engineering contract V31, а product stamped/re-synced V31. Новый feature root не создавался.
- [ ] **M2. Static Integration Lab shell** — маленькая hand-authored сцена с одним entry point,
  fixture slots, common smoke и machine-readable capture; без заявления live simulation.
- [ ] **M3. Universal Grid / Layers seam** — committed revisions, event transport и как минимум два
  независимых consumer layers; без gas-specific notification.
- [ ] **M4. Live Gas drop** — authoritative gas step работает в Lab через принятый Grid seam и имеет
  positive/negative proof.
- [ ] **M5. World Change drop** — реальное controlled topology change публикует revision; Gas и ещё
  один заинтересованный слой реагируют через общий контракт.
- [ ] **M6. Character & Gameplay Contact drop** — authoritative Actor/contact и не-authoritative View
  встроены без смешения authority.
- [ ] **M7. Level / Generation drop** — static fixture заменяется или дополняется валидным generator
  output через replaceable ingestion adapter; вертикальные и боковые пути доказаны.
- [ ] **M8. Presentation drop** — состояние газа, опасность и изменение мира читаемы и держат budget;
  capture воспроизводим.
- [ ] **M9. Product Proof** — одна representative playable сцена сводит принятые drops, показывает
  core loop и возвращает evidence для design/marketing/owner review. Co-op заявляется только если
  отдельный co-op acceptance действительно пройден.

Milestones задают зависимости, а не обязательную последовательность всей внутренней работы. Например,
Gas и Grid могут готовить независимые harness proofs параллельно после M1, но Integration принимает M4
только после совместимого M3 seam. Level может стартовать позднее по выбору владельца и не блокирует
ранний static Lab.

## Рекомендованная первая продуктовая волна после M1

Три совместимых, но раздельно владеющих результата:

1. **Integration Lab:** только маленький static shell и контракт приёма drops.
2. **Grid / Layers / World Change:** universal committed-event seam и минимальный proof с двумя
   consumers.
3. **Gas Simulation:** bounded live-gas capability, работающая против принятого seam/fixture.

Это рекомендация порядка, не квота активных треков. Владелец запускает столько направлений, сколько
считает полезным. Dashboard показывает фактическую загрузку, но не предлагает «добрать до лимита».

## Оставшаяся работа по направлениям

### 1. Integration Lab & Product Proof — primary

Назначение: держать глобальный маршрут, принимать drops и доказывать совместную сцену.

Текущее состояние: карта готова; самой Lab scene ещё нет.

Осталось до M9:

- [ ] Сначала shape-only определить, является ли общий entry point новой оболочкой, частью
  `NearGasSimulationLab` или требует reconciliation; только затем формировать bounded PLAN/BUILD для M2 static shell.
- [ ] Зафиксировать минимальный scene/drop contract и общий smoke, не дублируя contracts треков.
- [ ] Принимать M3–M8 только с six-line handoff и first-hand proof.
- [ ] На каждом приёме обновлять milestone, остаток и conflict state через Direction RESULT.
- [ ] Свести одну playable proof loop и отдельно проверить любые co-op claims.
- [ ] Передать capture/evidence в Design & Canon и Marketing & Audience.

Не владеет: внутренними алгоритмами остальных направлений.

### 2. Gas Simulation

Назначение: authoritative gas behavior и его gameplay consequences.

Текущее состояние: NearGas L1B observability delivered/released at `693e671b`; это foundation evidence,
но не scene-ready M4 drop.

Осталось до M4/M5:

- [ ] После Integration Lab ownership shape перечитать current Gas SPEC/product и сформировать свежий V31 shape/PLAN.
- [ ] Сверить transport/types/equipment inputs с универсальным committed Grid seam.
- [ ] Доказать deterministic positive/negative gas behavior в track-owned harness.
- [ ] Вернуть scene-ready M4 drop без rendering и без surrogate path.
- [ ] Для M5 доказать реакцию на committed topology revision.
- [ ] Позднее определить gas damage/consequence здесь; Character только потребляет результат.

Не владеет: event bus, topology authority, character view, gas rendering.

### 3. Grid / Layers / World Change

Назначение: универсальная связь независимых слоёв и authoritative публикация изменения мира.

Текущее состояние: архитектурная роль принята картой; отдельный V31 implementation/drop ещё не принят.

Осталось до M3/M5:

- [ ] После Integration Lab ownership shape сверить current SPEC/ADR и выбрать минимальный настоящий seam slice.
- [ ] Доказать common coordinates, cell→region/sector ownership и commit clock.
- [ ] Доказать publish/subscribe для минимум двух разных consumers, не только Gas.
- [ ] Запретить live mid-tick cross-layer read и planted stale revision.
- [ ] Вернуть M3 scene drop с machine-readable ordering proof.
- [ ] Вернуть M5 controlled topology/world-change drop; без расчёта поведения consumer layers.

Не владеет: gas/wind/damage/equipment calculations и presentation.

### 4. Level & Environment

Назначение: валидное пространство и replaceable procedural ingestion.

Текущее состояние: LV0 PLAN reported RELEASED at `b1698170`; Direction review missing. Трек не нужно
ревьюить в ходе настройки карты.

Осталось до M7:

- [ ] Когда владелец активирует Level, сначала сверить frozen LV0 HOME, current product и V31.
- [ ] Закрыть или исправить Direction receipt; старый PLAN не запускать повторно.
- [ ] Проверить geometry/connectivity/aperture contract и generator adapters.
- [ ] Доказать вертикальные и боковые пути в track-owned scene.
- [ ] Доказать, что static и procedural sources отдают один ingestion contract.
- [ ] Вернуть M7 drop и reproducible seed/evidence.

Не владеет: симуляцией слоёв и общей Integration Lab.

### 5. Character & Gameplay Contact

Назначение: authoritative игрок в мире плюс отдельное визуальное воплощение.

Текущее состояние: legacy Character Leg 2 в review/closing; текущий frozen CALL не перезапускается.

Осталось до M6:

- [ ] Закончить owner LOOK, binding G5, product RESULT/Deliver и Direction close текущего Leg 2.
- [ ] После close и M1 сформировать свежий V31 PLAN для Player Simulation / Actor Layer.
- [ ] Решить по evidence: полноценный grid layer или bounded module над Grid/Layer seam.
- [ ] Сохранить Character View отдельным consumer authoritative state.
- [ ] Доказать movement/contact/reaction без превращения ragdoll/view в authority.
- [ ] Вернуть reusable prefab + actor contract как M6 drop.

Не владеет: вычислением gas consequence и topology.

### 6. Presentation

Назначение: читаемый gas/world/character state и capture-ready визуальный результат.

Текущее состояние: legacy `c-visual-009` blocked; его prerequisites и карточка должны пройти V31/
Conflict Guard review до запуска.

Осталось до M8:

- [ ] После появления подходящих read models сверить старый visual route с current authority.
- [ ] Выбрать bounded visual proof slice и performance budget.
- [ ] Доказать читаемость gas states, hazard и topology change без своей simulation authority.
- [ ] Вернуть capture-ready M8 drop и negative proof на stale/wrong read model.

Не владеет: authoritative state и публикацией маркетингового материала.

### 7. Design & Canon — service lane

Назначение: превращать системные возможности в согласованную игровую фантазию и правила.

Текущее состояние: canon-forge работает; текущий READY root —
`c-cartography-g-d3a8-post-gas-behavior-admission-front-001` после admission gas-behavior card c-002.

Осталось для текущей сцены:

- [ ] Актуализировать карту design questions и сохранить floor-loop findings.
- [ ] Дать owner-readable решения по тем вопросам, которые реально блокируют текущий milestone.
- [ ] Проверять, что integrated proof создаёт решения игрока, а не только техническую демонстрацию.
- [ ] Перед M9 проверить fantasy/loop/co-op claims по фактической сцене.

Внутреннее устройство направления не перестраивается этой картой.

### 8. Build & Tooling — service lane

Назначение: устранять конкретные общие workflow/version/build blockers.

Текущее состояние: standalone `.NET Gates` retired; V30 entry проверен и superseded current V31 authority.

Осталось для текущей сцены:

- [x] Доказать current V29/V30/product state и выбрать один lawful entry: V30 superseded by installed V31.
- [x] Не выдавать ложный `re-sync:30`: product `re-sync:31` уже принят, feature не запускалась.
- [ ] Добавлять re-sync/tooling только если будущая конкретная работа докажет named product consumer.
- [ ] Добавлять validators/tooling только из доказанного cross-track need.
- [ ] Не создавать постоянный технический roadmap без product consumer.

### 9. Marketing & Audience — service lane

Назначение: превращать реальные product proofs в понятное обещание и внешний сигнал.

Текущее состояние: marketing-forge сохранён и paused по owner-controlled WIP swap; storefront и
audience остаются вложенными outcomes, не отдельными live tracks.

Осталось для текущей сцены:

- [ ] При пробуждении сверить stale-route finding `dr-20260712-001` и current product truth.
- [ ] Получать только принятый capture/proof от Integration/Presentation.
- [ ] Выбрать нужный artifact, channel и момент через существующий forge.
- [ ] Не обещать co-op, destruction или visual quality раньше evidence.
- [ ] Вернуть внешний feedback в глобальные приоритеты через новый Direction RESULT.

Единственный редкий ориентир этой карты — Factorio Friday Facts: реальная техническая работа может
порождать регулярный публичный proof. Это ориентир для формы, не автоматическая стратегия и не
обязательство публиковать каждый milestone.

## Capability drop: что обязан вернуть трек

Каждый завершённый bounded task, который может изменить глобальный прогресс, возвращает ровно:

```text
status: accepted-candidate | blocked | not-ready | superseded
result: что фактически изменилось или доказано
proof: first-hand tests / revision / capture / negative control
scene_drop: что именно может принять Integration Lab; none если принимать нечего
blocker: none или один точный blocker/конфликт
next: один bounded следующий шаг или owner decision
```

Полные правила: `work/program-v2-track-handoff-template.md`.

`accepted-candidate` ещё не означает интеграционный close. Integration Lab проверяет совместимость
seam, proof и общий smoke. Только валидный Direction RESULT может изменить этот план, milestone или
dashboard.

## Параллельность без конфликтов

| Направление | Своя зона записи | Общая граница |
|---|---|---|
| Integration | Lab scene, integration adapters, common smoke | принимает только published drops |
| Gas | gas layer + gas harness | committed Grid read model/events |
| Grid | grid/layer contracts + topology harness | не пишет consumer algorithms |
| Level | modules/generators + level fixtures | replaceable ingestion output |
| Character | actor/view modules + character fixture | Grid/Layer seam + published consequences |
| Presentation | render/VFX/capture fixture | read-only accepted models |
| Design | canon/question artifacts | не пишет product implementation |
| Build | tooling/version/build artifacts | только доказанный consumer need |
| Marketing | marketing artifacts | только accepted capture/product truth |

Если два направления должны менять один product seam или общий файл, они не делают это параллельно:
Integration/Build shape возвращает один serial owner и порядок интеграции.

## Retired / superseded

- `damage` standalone track — retired. Gas consequence принадлежит Gas Simulation; Character
  потребляет и визуально показывает результат.
- `.NET Gates` standalone track — retired. Новый конкретный blocker может стать bounded задачей
  Build & Tooling после свежего доказательства.
- `core` как один широкий трек — split между Integration, Gas и Grid.
- Старый `program` label — superseded новым Integration Lab & Product Proof.
- Старый `visual` label — renamed Presentation; старый root остаётся blocked evidence, не разрешением
  на автоматический запуск.

END_OF_FILE: live/indie-game-development/work/program-v2-integration-lab-plan.md
