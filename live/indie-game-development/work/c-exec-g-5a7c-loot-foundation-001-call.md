# CALL — c-exec-g-5a7c-loot-foundation-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
mode: ПРОБА — режим по умолчанию контракта 36; ОПОРА не включена и сама не включается.
direction: indie-game-development
node: g-5a7c
track: house-and-things
task: t-loot-1
parent: c-exec-g-5a7c-loot-1-001
issued: 2026-08-13 by s-work-g-5a7c-loot-foundation-dispatch-001
status: ready
basis: `c485b30e704b1706675dd92d15c5223b0d166b92` — `origin/main` = `origin/dev`, перемерено
       `git ls-remote origin` перед выпуском 2026-08-13.
preserved-input: `e0a301947c28ef04a8465a411104098f54d9b9f7` —
  `preserve/c-exec-g-5a7c-loot-1-001-win-u1-local-20260813`; только улика/салвейдж, не база и не
  место для патча.

**OWNER-APPROVED OVER-BUDGET TOKEN, ДОСЛОВНО:** «Первый BUILD — входит: data
types/catalog/layout/support, validation, migration 10 items, primitive IDs in host state/network
snapshot, functional prefab-selection seam with fallback, definition-based behavior dispatch seam,
Inspector, stale-contact correction, headless + Unity tests, full RESULT and real rollback/reapply if
required by issued CALL». И его прямой приказ Направлению: «выпусти отдельный полноценный
loot-CALL/наряд».

Старый RESULT и frozen candidate **НЕ ПЕРЕОТКРЫВАТЬ, НЕ МЕНЯТЬ И НЕ ПАТЧИТЬ**. Этот CALL — отдельный
child прежнего paused root только для законного графа дорожки. Работа начинается от свежего
`origin/main`; из preserve-кандидата можно переносить только проверенные данные/находки с явной
повторной валидацией на свежей голове.

Если `origin/main` сдвинулся, семантически перебазируйся на свежую голову и повтори затронутые
проверки. Перед terminal REPORT перечитай remote ещё раз. Любой настоящий продуктовый выбор,
противоречащий решениям ниже, — ESCALATE домой; обычный технический HOW принадлежит PLAN.

## slot

Слот заранее не присвоен: выбери селектором один реально `CLEAN / AVAILABLE` из `WIN-U1..WIN-U4`,
захвати его lease `c-exec-g-5a7c-loot-foundation-001:<stage>` и работай только там. На момент выпуска
Направление не смогло законно прочитать selector из своего workflow-worktree, поэтому не выдумывает
свободный слот. Занятый/грязный слот — выбрать другой; ни одного чужого дерева не очищать.

**UNITY НУЖЕН:** scene-owned supports/layout, реальные colliders/Rigidbody, prefab selection и
owner-eye matrix не доказываются одним headless-прогоном.

## goal

**В ДОМЕ ЕСТЬ ДЕСЯТЬ ИМЕНОВАННЫХ ПРЕДМЕТОВ 5/3/2, КОТОРЫЕ ПОЯВЛЯЮТСЯ НА РЕАЛЬНЫХ ФИЗИЧЕСКИХ
ОПОРАХ НЕЗАВИСИМО ОТ ПОКРЫТИЯ, НЕСУТ СТАБИЛЬНУЮ ИДЕНТИЧНОСТЬ ТИПА ЧЕРЕЗ HOST/NETWORK/CLIENT,
ВЫБИРАЮТ МОДЕЛЬ И ПОВЕДЕНИЕ ПО DEFINITION И НЕ ВЫСТРЕЛИВАЮТ ПРОТУХШИМ КОНТАКТОМ ПОСЛЕ PICKUP.**

Владелец не принимает `LootLibrary` frozen-кандидата как долгосрочную архитектуру. Его
owner-agreed контур: тип предмета отделён от физического профиля и экземпляра; высота выводится из
exact physical support; `CargoId`, `DefinitionId` и physics-profile id независимы; сеть несёт только
primitive IDs; presentation и behavior выбираются по definition; плохие данные валят Host громко.

## binding product decisions — результат владельца, не место для нового выбора

1. **`LootDefinition`.** Stable nonnegative `DefinitionId`, `DisplayName`, обязательный physics
   profile, optional visual profile, optional behavior profile/`BehaviorId`. Не `CargoId`, не индекс,
   не имя. В definition нет room, world pose, support-Y и per-spawn mass.
2. **`LootPhysicsProfile`.** Stable `PhysicsProfileId`, совместимый на миграции с class ids 0/1/2;
   единый источник mass, body/collider dimensions, collider centre и optional COM. Профиль можно
   делить. Особая масса одного definition = отдельный профиль, не spawn override. Inspector получает
   required-holder count из того же production-закона, которым живёт игра, а не считает второй
   закон. Friction/grip tuning не добавляются.
3. **`LootVisualProfile`.** Prefab + optional local position/rotation/scale offsets. Cube — явный
   fallback только при отсутствии профиля. Production art не требуется, но настоящий lookup и
   instantiation path должен работать.
4. **`LootBehaviorProfile` / registry.** Stable `BehaviorId` маршрутизируется host-side в существующий
   cargo-thing rule; per-instance state остаётся в `CargoThingState`/engine-free аналоге. Alarm-clock
   больше не выбирается по physics/class id: только его конкретное definition получает alarm
   behavior, а опубликованные states/timing/event route не меняются. Это минимальный dispatch seam в
   существующем слое, не PaintCan, не handler composition и не общая система комбинаций.
5. **`LootCatalog`.** Все definitions/profiles, unique IDs, non-null refs, finite positive
   mass/dimensions, известные visual/behavior keys. Missing/duplicate/unknown данные дают ясную
   pre-Host ошибку. Silent fallback к первому class/profile запрещён. Catalog хранит типы, не
   экземпляры дома.
6. **`LootSpawnLayout`.** Definition/id, stable authoring `SpawnKey` либо доказуемый deterministic
   CargoId order, `SupportId`, local planar X/Z offset, initial yaw/rotation. Нет absolute world Y,
   mass/model/behavior/room duplicates. Room приходит из support/scene authority либо валидируется.
7. **`LootSupport`.** Stable unique `SupportId`, explicit enabled non-trigger collider, local up /
   allowed top surface, room authority. Запрос сверху вдоль `-up` обязан попасть именно в этот
   collider с допустимой нормалью. Pose = hit + physics bottom/pivot offset. Missing/miss/trigger/
   disabled/bad normal/initial penetration — fail before Host, без Y fallback. Floor support —
   structural collider, не visual mesh/ковёр; стол/тумба/полка — такие же физические опоры. Pickup/
   drop остаётся на реальном collider.
8. **Identity.** `CargoId` = instance, `DefinitionId` = type, `PhysicsProfileId`/compatible
   `CargoClassId` = physics. Первый migration шаг добавляет `DefinitionId` в `CargoState` и
   `CargoSnapshot` рядом с profile/class id. Host: layout → catalog → definition → physics → resolved
   support pose → state. `CargoBody` читает physics profile; client prefab lookup идёт по
   `DefinitionId`, никогда по `CargoId`/class.
9. **Inspector.** На строке видны CargoId/SpawnKey, name + DefinitionId, effective mass/dimensions,
   production-derived holder count + max warning, model/fallback, behavior, room/support, resolved
   pose/status и быстрые переходы к definition/profile. Profile edit проверяется после stop Play и
   нового Host start.

Полная owner-authority копия решения сохранена в Direction как
`work/2026-08-13-loot-owner-architecture-handoff.md`; CALL выше самодостаточен и не требует доступа к
workflow-репозиторию.

## current measured inputs — перепроверь в PLAN, не считай властью

- На `c485b30e` product contract stamp = 36. Три существующих профиля: `48 kg / 0.192×0.04×0.04`,
  `100 kg / 0.288×0.06×0.06`, `240 kg / 0.384×0.08×0.08`; lift thresholds `144/300/720 N`, max
  holders = 4. Значения мигрируют без изменения.
- `IntegratedHouse` сейчас несёт четыре `CargoSpawnPoint` в runtime-порядке class ids `0,0,1,2`.
  Удаление всех четырёх в frozen-ноге сломало component-inventory лаборатории. Новый PLAN обязан
  мигрировать lawful consumers/tests; если compatibility markers остаются, они явно инертны и тест
  доказывает, что они не второй источник spawn.
- `GameRulesSettings.CreateCargoSpawnState` вызывает `AlarmClockCargoThing.InitialStateFor(classId)`
  для каждого cargo. Значит опубликованная сцена уже случайно связывает alarm с двумя class-0
  экземплярами, а preserve-раскладка связала бы с пятью. Целевая семантика — один явно названный
  alarm definition; правило его поведения сохраняется, параметр массы больше не identity вещи.
- Preserve-кандидат даёт допустимый состав 5/3/2: Bedside Radio, Kitchen Timer, Hall Key Box, Remote
  Control, Desk Clock; Tool Box, Food Crate, Record Case; Strongbox, Travel Trunk. Room totals 2/3/1/4.
  PLAN может уточнить DisplayName единственного alarm definition только без двусмысленности и без
  изменения состава/весового распределения.
- Preserve-доказательство твёрдости: реальная local `PhysicsScene`, 10 240 steps, collision-off
  303.835 ms, solid 370.383 ms, delta 66.548 ms ≈ 0.00650 ms/step; solver не сломался. Повтори
  затронутое доказательство на новой архитектуре, не переноси claim вслепую.
- Publication blocker: inactive cargo оставляет collider/detectCollisions включёнными, но контактное
  окно не читается/не очищается до activation; накопленный удар может позже дать false noise rank 3
  и подавить реальный sight rank 2.5.

## migration and one-authority rule

- Создать три profiles с прежними значениями, десять named definitions 5/3/2 и десять layout rows.
- Table/counter rows привязать к их physical supports, floor rows — к structural floor collider, не к
  временному покрытию. Покрытие можно удалить/заменить без изменения layout Y.
- После миграции существует один authoritative path. Старый `LootLibrary`/`CargoSpawnPoint` fallback
  не остаётся вторым молча работающим источником: все lawful consumers/tests мигрированы, либо
  compatibility контракт узкий, явный, fail-closed и доказан.
- Никакого silent fallback при unknown class/profile/definition/behavior/visual key.

## mandatory stale-contact correction

Resting cargo остаётся твёрдым. Contact, накопленный while inactive, не превращается в force/noise
после later activation. Transition inactive → active сбрасывает соответствующее окно, не ломая live
contacts и one-shot noise. Обязательная регрессия: strike resting cargo → wait → pickup = no stale
noise; fresh active collision = normal noise once; real sight/situation не подавляется stale cargo
event.

## ПОПРАВКИ АРХИТЕКТУРНОГО РАЗБОРА — 2026-08-13, обязательны

Полный разбор: `live/indie-game-development/work/2026-08-13-loot-architecture-review.md`. Структура
handoff владельца НЕ отменяется ни в одной строке; ниже — условия исполнимости и уточнения.

**БЛОКИРУЮЩИЕ.**

1. **«Отказ ДО старта Host» переносится туда, где он возможен.** Сегодня чтение раскладки и создание
   грузов вызывается из сетевого пути, срабатывающего ПОСЛЕ подъёма сервера: отказ там даст поднятый
   сервер, неподписанный тик и висящее «Host is listening» вместо ошибки. Каталог и раскладку читает
   обычный компонент сцены; проверка бежит внутри кнопки «Host» ДО подъёма сервера; отказ печатается
   человеческим текстом в поле статуса лобби. Точную точку вызова перепроверь в PLAN — Направление
   проверило пассивность `StartConditions.cs`, но самого вызывающего не открывало.
2. **ПЕРВЫЙ коммит расширяет подпись шва поведений.** Перемерено Направлением:
   `Core/Cargo/CargoThing.cs:63-72` — `bool KeepsBodyActive(CargoThingState state)` получает ТОЛЬКО
   состояние, без предмета. При двух видах диспетчер не может понять, чьё это состояние. Передай туда
   груз целиком (~10 строк, груз под рукой в обоих местах вызова). **Без этого гейт второго вида
   непроходим, и СТОП будет не твоей виной, а нашей невыполненной подготовкой.**

**ВАЖНЫЕ.**

3. Тихих подстановок класса **четыре**, и главная бежит в файле настроек, а не в каталоге, который в
   продакшене не строится ни разу. В возврате перечисли каждую поимённо: снята или недостижима, и чем
   доказано.
4. **Имя предмета берётся из названия типа**, а не из порядкового номера («Cargo 7» — это позиция в
   раскладке, вставка строки в середину переименует всё ниже).
5. **ДОСЯГАЕМОСТЬ — ЗАКРЫТО СЛОВОМ ВЛАДЕЛЬЦА 2026-08-13. РУЧНАЯ РАСКЛАДКА КУДА УГОДНО, ЗАПРЕТА НЕТ.**
   Его слова: «я хочу руками раскладывать вот на полочку, на шкаф, где-то ещё положить в любое место…
   я могу и высоко, естественно, на полку… просто когда вручную я могу видеть, что, ага, сюда мыши
   могут забраться, сюда не могут».
   Следствия, все обязательные:
   - **Полки, шкафы и холодильник РАЗРЕШЕНЫ как опоры наравне с полом.** Прежний временный запрет
     этого наряда снят.
   - **Жёсткого отказа по высоте НЕТ ни одного.** Раскладка не имеет права не дать поставить предмет.
   - **Подсказка есть и она полезна ЕМУ, а не проверке:** инспектор показывает, достаёт ли налётчик
     до предмета стоя (потолок подбора ≈ `1.40` м) — это ровно то «я вижу, куда мыши заберутся», о
     котором он говорит. Подсказка не блокирует ничего и не является строкой приёмки.
   - **Раскладка только РУЧНАЯ.** Его слово: «вначале это только ручной будет». Процедурная и
     полуслучайная раскладка — НЕ в этой волне, и это не задел, а прямой вырез.
   - **Его архитектурный ориентир, записанный дословно: «лут, в принципе, от спавна не шибко-то и
     должен зависеть».** Описание предмета не знает ни комнаты, ни координат — структура это уже
     соблюдает, и отступать от этого запрещено.
6. **Доставку не чинишь** (верно), но назови в возврате, какая строка раскладки является целью захода:
   цель смотрит на первый добавленный груз.
7. **Назови в возврате, что твёрдые предметы становятся укрытиями для крысы** и сколько их прибавилось:
   это трогает самое рискованное допущение волны, и обнаружить это на прогоне зрения нельзя.
8. **Назови пересечение с дорожкой `body`** (клиентская отрисовка) вслух: право волны на три дорожки
   выдано на измеренном нулевом пересечении файлов.

**ЖИВОЙ ДЕФЕКТ, который ты увидишь сразу:** на опубликованной сцене `_cargoClassId` у четырёх точек =
`0, 0, 2, 1`, а будильник привязан к классу `0` — **в игре сегодня звонят ДВА груза, а не один.**
Привязка поведения к определению это чинит; подтверди числом в возврате. Владелец 2026-08-13: «значит,
надо менять» — починка куплена его словом.

**9. ЦЕНТР КОЛЛАЙДЕРА И ЦЕНТР МАСС — РЕШЕНО НАПРАВЛЕНИЕМ, это инженерный выбор, не игровой.**
Владелец прямо сказал, что вопроса не понимает («ну, я не понимаю, что это значит»), и переложил
решение на нас — значит нога решает и отвечает за него.
- **`Collider Center` остаётся полем профиля, но обязан быть нулевым.** Ненулевое значение валит
  запуск явным человеческим сообщением. Основание: у слоя правил понятия «центр» нет вовсе — все
  четыре судейских ответа (луч подбора, блокировка ходока, на что можно встать, где держат руки)
  строят коробку симметрично вокруг точки предмета. Заавторенное поле, которого правила не читают,
  развело бы четыре разные вещи; на классе 48 кг сдвиг 2 см — половина предмета.
- **`Center Of Mass` в этой волне НЕ ЗАВОДИТСЯ вовсе.** Ядра он не касается, потребителей ноль,
  добавляется позже одной строкой.
- Строка его handoff при этом НЕ отменяется: поле стоит и честно ждёт первой несимметричной модели.
  В тот день решение принимается отдельно, и оно будет его.

**10. ШАБЛОНЫ ЛУТА — ЕГО СЛОВО, И ОНИ УЖЕ ЕСТЬ В СТРУКТУРЕ. Ничего нового не строится.**
Его слова: «возможно, у нас есть какие-нибудь шаблоны для лута, с которых я могу уже разные вещи
делать. У них, например, заполнено — лёгкий, тяжёлый, средний лут», и его же оговорка «не факт, что
так и надо делать». Ответ: три физических профиля (`48` / `100` / `240` кг) — это и есть лёгкий,
средний и тяжёлый шаблоны; новый предмет создаётся копией готового описания и заменой того, что надо.
**Обязанность наряда:** назвать три профиля человеческими именами в инспекторе (лёгкий / средний /
тяжёлый, а не `Profile 0/1/2`) и показать в возврате, сколько действий занимает завести новый предмет
из шаблона. Отдельной системы шаблонов НЕ строить — это его догадка, а не заказ.

## ПОПРАВКИ ВТОРОГО КРУГА — 2026-08-13, из вопросов владельца о весе и коллайдере

**11. ФОРМА КОЛЛАЙДЕРА: РАЗДЕЛИ ДВА СТОЛКНОВЕНИЯ ВСЛУХ И НЕ ОБЕЩАЙ ЛИШНЕГО.**
Перемерено Направлением: `Network/CargoBody.cs:113` берёт `gameObject.GetComponent<Collider>()` — то
есть ЛЮБОЙ коллайдер, который автор положил на префаб (цилиндр, сфера, меш). А ядро
(`Core/Cargo/CargoGeometry.cs:190-206`) считает `HalfLength/HalfHeight/HalfWidth` тремя
`IntersectSlab` — то есть ТОЛЬКО коробкой, и других форм не знает.
- В возврате **назови вслух**: физическое столкновение — любая форма; четыре судейских ответа (луч
  подбора, блокировка ходока, на что встать, где держат руки) — всегда коробка вокруг точки предмета.
- **ДЕФЕКТ, найденный вопросом владельца:** `GetComponent<Collider>()` возвращает ОДИН коллайдер, и
  включение/выключение (`:181,217,224`) переключает только его. На префабе из нескольких коллайдеров
  остальные останутся включёнными всегда — предмет получится наполовину проходимым, наполовину нет,
  и это ломает купленное им «лут не должен через друг друга проходить». **Почини:** переключай все
  коллайдеры тела, а не первый найденный. Если чинить дороже, чем кажется — СТОП домой с числами.

**12. «КГ» — НАША ВЫДУМКА, И ЕЁ НАДО УБРАТЬ ИЗ АВТОРСКОЙ ПОВЕРХНОСТИ.**
Перемерено: `git grep -ci "kg\|килограмм"` по `Assets/TunnelCrew` → **ноль вхождений**. Поле
называется просто «масса», подписи «кг» в игре нет нигде — килограммы приписали мы в своих же
документах и в этом наряде. Владелец возмутился нашей подписью, а не игрой.
Происхождение числа `48`, из сообщений коммитов: ящик массой `4` → мир сжат в 12.5 раз, масса поднята
`4 → 50` **чтобы не перенастраивать пороги шума** → ускорили переноску, `50 → 20` по той же причине →
ввели силу руки `200`, поставили `20 → 48` без объяснения; `100` и `240` подобраны, чтобы лестница
вышла «1 / 2 / 4 руки». **Число никогда не было массой предмета — это ручка «сколько рук нужно».**
- **Нигде в инспекторе, в подсказках и в возврате не писать «кг».** Подпись поля — «тяжесть» либо
  «сколько рук», единиц не изобретать.

**13. ИНСПЕКТОР ПОКАЗЫВАЕТ ДВЕ ВЕЩИ, А НЕ ОДНУ.** `handoff` обещает только число носильщиков — это
половина ответа. Вес решает ещё и **громкость**: пороги `_cargoRustleForce 60`,
`_cargoKnockForce 150`, `_cargoHeavyNoiseForce 400` — это СИЛЫ, и удар растёт с массой.
По замеру проверки, при обычной скорости переноски **всё тяжелее ≈18.5 попадает в самый громкий ранг
при любом задевании стены**, то есть все три нынешних класса всегда орут на максимум, а средние
полосы шума построены и ни разу не использованы. Инспектор обязан показывать **и носильщиков, и
ожидаемый ранг шума**. Ядро не трогается, обе величины считаются из существующих настроек.

**14. «ЧИСЛО НОСИЛЬЩИКОВ ИЗ ЖИВОГО ЗАКОНА» — БЛОКИРУЮЩАЯ: ТАКОГО ЗАКОНА В ИГРЕ НЕТ.**
Проверка нашла: игра нигде не спрашивает «сколько рук нужно» — она складывает силы и сравнивает с
весом внутри физики; в коде есть только «сколько рук держит СЕЙЧАС». Значит нога пишет ПЕРВЫЙ
экземпляр этого закона, а не читает существующий, и **обязана сказать это в возврате вслух**. Наивная
формула «вес ÷ 200» соврёт на краю. Границы, замеренные прогоном настоящего кода подъёма: ниже ≈12
предмет дрожит в руках; `12…200` рабочий диапазон; `200…266` поднимается, но окно удержания сжимается
до сантиметров; выше ≈266 не поднимет никто (4 руки × 200 ÷ гравитация 3). Инспектор обязан отмечать
попадание в две последние зоны.

**15. ЛЮБОЙ ВЕС РАЗРЕШЁН.** Список весов ничем не ограничен; «три класса» — это просто три заведённые
строки, а не закон. Владелец прямо потребовал возможность ставить `180` и `12`. Ограничений по числу
весов не вводить.

**16. ВЕС ЖИВЁТ НА САМОЙ ВЕЩИ — ВЫБОР ВЛАДЕЛЬЦА, ВАРИАНТ «А», 2026-08-13. ЭТО ОТМЕНЯЕТ ЧАСТЬ ЕГО ЖЕ
HANDOFF, И ОТМЕНЯЕТ ЕГО СОБСТВЕННЫМ СЛОВОМ.**

Ему были показаны два варианта с ценой каждого; он ответил **«А»**. Формулировка выбора, которую он
принимал: «вес пишу прямо на вещи, заготовки нужны только чтобы копировать» против «вес пишу в общей
карточке, а чтобы дать вещи свой вес, завожу ей отдельную карточку». Названная ему цена варианта А
принята вместе с ним: **правка числа в заготовке больше не меняет уже созданные предметы**, каждый
правится отдельно.

**ЧТО ИМЕННО ОТМЕНЯЕТСЯ, ПОИМЁННО:**

- `2026-08-13-loot-owner-architecture-handoff.md` §2 — «`LootPhysicsProfile` — **единый источник
  физики**» в части МАССЫ, и «отдельная масса одного типа означает отдельный профиль».
- Этот наряд, binding-решение 2 (строки ~64-65) — «единый источник mass…», «Особая масса одного
  definition = отдельный профиль».
- `handoff` §9 в части «общий профиль влияет на все использующие его definitions» — для массы это
  больше не так.

**ЧТО ОСТАЁТСЯ В СИЛЕ БЕЗ ИЗМЕНЕНИЙ:** запрет per-spawn override (масса в РАСКЛАДКЕ по-прежнему
запрещена — один предмет весит одинаково везде, и довод handoff про «разные комнаты» этим полностью
исполнен); профиль как носитель ФОРМЫ тела/коллайдера; всё остальное содержание §2.

**НОВАЯ ФОРМА, дословно:**
- Масса — поле САМОГО определения предмета. Живая настройка одного предмета во время игры сохраняется
  полностью (масса перечитывается каждый тик).
- Три существующие карточки (`48 / 100 / 240`) остаются **ЗАГОТОВКАМИ**: с них копируют при создании
  предмета, в игре их массу не читает никто.
- **ЗАПРЕЩЕНО заводить декоративный номер профиля ради строки приёмки.** Поле, которого правила не
  читают, — ровно тот дефект, что уже осуждён поправкой 9 про центр коллайдера.

**СЛЕДСТВИЕ ДЛЯ СТРОКИ 2 `done_when`: идентичностей ДВЕ, а не три** — экземпляр в раскладке
(`CargoId`) и тип предмета (`DefinitionId`). Третья (физический профиль) в игре после этой правки не
существует, и требовать её независимости — требовать невыполнимого. Строка 2 читается с этой
поправкой; исполнителю запрещено подгонять под прежнюю редакцию.

**Поправка 10 читается так же с заменой слова:** три карточки называются **заготовками**
(лёгкая / средняя / тяжёлая), а не «профилями», и в возврате показано число действий на новый предмет
из заготовки.

## boundaries

- **НЕ ТРОГАТЬ** старый RESULT, preserve-ref и frozen candidate; не строить поверх него второй
  авторитетный путь.
- **НЕ ПРАВИТЬ** временное floor covering/visual mesh и **НЕ ДОБАВЛЯТЬ** ручной support/world Y
  offset. Structural support collider разрешён и обязателен; content intersection не маскировать.
- Не менять masses/dimensions 48/100/240, lift law `144/300/720`, cargo gravity/per-hand ceiling,
  max holders, noise thresholds, situation reduction или delivery. Holder display читает production.
- Не передавать `UnityEngine.Object` через core/network. Не выбирать visual/behavior из CargoId или
  physics id. Не разрешать per-spawn mass/model/behavior/room overrides.
- Не делать production art/models, paint/decal, новые sounds/VFX, market/personal value, sale,
  damage/destruction, procedural/random loot generation.
- Не расширять behavior seam в generic handler pipeline/combinations. Дополнительные behaviors и
  контентные реакции — следующая волна/реальные кейсы.
- Никаких обходов недоступного Unity/tooling. Genuine tool/permission/irreversible boundary — STOP/
  ESCALATE с точным свидетельством.

## done_when

Три строки — потолок контракта 36; owner-approved полный scope вложен в них целиком.

1. **ОДИН ВАЛИДИРУЕМЫЙ ПУТЬ ДАННЫХ И ОПОР.** В production существуют `LootDefinition`, единый
   `LootPhysicsProfile`, optional visual/behavior profiles, `LootCatalog`, scene-owned
   `LootSpawnLayout` и exact-collider `LootSupport`; десять named items мигрированы 5/3/2 с прежними
   masses/dimensions и реальными floor/table/counter supports без world Y. До Host громко
   отвергаются missing/duplicate/unknown/invalid данные, bad support/normal/penetration; silent class
   fallback и второй spawn authority отсутствуют. Inspector показывает все согласованные effective
   поля и holder count из production-закона.

2. **ТРИ ID НЕ СМЕШИВАЮТСЯ, А VISUAL/BEHAVIOR ДОХОДЯТ ДО РЕАЛЬНОГО ЭКЗЕМПЛЯРА.** `CargoId`,
   `DefinitionId` и physics-profile identity независимы; every constructor/copy/with/world/snapshot
   path сохраняет `DefinitionId`, compatible profile id и `ThingState`; сеть несёт primitives;
   реальный client выбирает prefab по `DefinitionId`, а отсутствие profile даёт явный cube fallback.
   Host dispatch идёт по stable `BehaviorId`; ровно alarm definition сохраняет опубликованное
   alarm-clock rule/state, ordinary definitions его не наследуют из массы.

   **ГЕЙТ ВТОРОГО ВИДА — добавлен 2026-08-13 требованием владельца о расширяемости при планировании
   (`knowledge/core-is-extended-never-rewritten.md`).** Сегодня на `origin/main` реализация
   `ICargoThingRule` РОВНО ОДНА — `AlarmClockCargoThing`; диспетчер с одним поведением ничего не
   доказывает. Поэтому: **второй вид поведения въезжает ДОБАВЛЕНИЕМ и это доказано СОСТАВОМ
   КОММИТА.** Второй вид назван Направлением и НЕ сочиняется тобой: это **второй способ
   срабатывания — от переворота/ориентации, а не от удара**, ровно та форма, которую уже доказала
   закрытая `t-thing-1` (один файл на 26 строк, ядро не тронуто). Требуется: коммит, вводящий его,
   не трогает `Core/Cargo/CargoThing.cs`, `Core/Cargo/CargoRules.cs`, `Core/Cargo/AlarmClockCargoThing.cs`
   и `CargoState`/`CargoSnapshot`. **Это ГЕЙТ, а не содержание волны:** вырез 9 ставки и handoff
   владельца («не реализует набор новых контентных реакций») сохраняются — второй вид доказывается и
   может быть снят обратным коммитом, состав обоих коммитов идёт в возврат числом строк и списком
   путей. Если он НЕ въезжает добавлением — **СТОП домой с диффом**, это дефект формы, а не повод
   изобретать обход.

3. **ФИЗИКА И ПУБЛИКАЦИЯ ДОКАЗАНЫ НА НАСТОЯЩИХ ПУТЯХ.** Каждая layout row резолвится в exact
   support collider, низ реального `CargoBody` касается его без penetration, реальные
   `Rigidbody`/collider получают profile mass/dimensions, resting/carried cargo остаётся твёрдым, а
   stale-contact sequence не даёт поздний noise и не подавляет sight; fresh collision шумит один
   раз. Headless + Unity EditMode/PlayMode matrix ниже зелёная, owner-eye matrix исполнена/записана,
   полный contract-36 RESULT содержит paths/runs/review, fresh remote readback и настоящий
   rollback/reapply с равенством деревьев; только после этого candidate публикуется обычным путём.

## acceptance matrix — обязательная coverage, не подсказка тест-метода

**Headless:**

- every `CargoState` copy/with and `CargoSnapshot` preserves every field including `DefinitionId`,
  physics profile identity and `ThingState`;
- CargoId, DefinitionId and profile id vary independently;
- behavior dispatch is definition-based;
- duplicate/missing IDs, invalid profiles and unknown keys reject before Host;
- no silent class/profile fallback.

**Unity EditMode/PlayMode:**

- every layout entry resolves its exact support collider;
- spawned real `CargoBody` bottom touches support without penetration; invalid support fails clearly;
- profile mass/dimensions reach real `Rigidbody`/collider;
- client presentation selects visual by `DefinitionId`, and cube fallback works;
- resting/carried solidity remains green;
- stale-contact sequence and fresh one-shot sequence above remain green.

**Owner-eye/manual — до Direction-close:**

1. Выделить одному definition отдельный lighter/heavier profile, остановить Play, запустить новый
   Host и проверить реальный carry-height/lift outcome разным числом рук.
2. Удалить/заменить временное покрытие и убедиться, что layout Y не редактировался, а предметы стоят
   на structural support.
3. Проверить named item/model mapping на Host и client, включая один заданный prefab и cube fallback.

## return

Первая строка — расписка: **3 строки `done_when`**, basis и preserved-input, подтверждение «старый
RESULT/ref не изменялись».

Дальше:

- disposition по каждой из трёх строк и каждому acceptance bullet, без объединения обещаний;
- PLAN-решения: конкретные stable ids, SpawnKey/CargoId rule, support query/normal tolerance,
  compatibility disposition четырёх legacy components, one-authority proof;
- таблица 10 instances: CargoId/SpawnKey, DefinitionId/name, profile id/mass/dimensions, behavior,
  visual/fallback, room/support и resolved pose/status;
- manifest всех constructor/copy/network/presentation/behavior paths, где едет `DefinitionId`;
- pre-Host validation failures с точными сообщениями и отсутствие silent fallback;
- stale-contact proof: inactive hit/wait/pickup, fresh active collision once, sight coexistence;
- headless и Unity runs с command/method, counts, raw run artifact/Console status;
- owner-eye результаты по трём пунктам или точный waiting handoff — без заявления task-close, пока
  владелец их не вынес;
- полный diff path list; список неизменённых thresholds/laws и подтверждение запретных областей;
- independent review evidence и dispositions по контракту 36;
- настоящий rollback/reapply: commands, commits, tree ids и `diff --exit-code`;
- final `origin/main`/`origin/dev` readback перед REPORT, publication commit/ref, assumptions, cuts и
  всё неожиданное.

## budget

Один полноразмерный engineering root с обычными stage/retry gates контракта 36. Это осознанно больше
прежнего half-day наряда и разрешено дословным owner token выше; scope не режется на две Direction-
задачи и не переносит network/behavior/stale fix на потом. При невозможности завершить — законный
checkpoint/ESCALATE с сохранённым чистым carrier, не самовольный scope cut.

END_OF_FILE: live/indie-game-development/work/c-exec-g-5a7c-loot-foundation-001-call.md
