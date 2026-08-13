# Лут — точный owner-agreed архитектурный handoff

**Источник и власть:** сообщение владельца, переданное из продуктового чата
`019ff6e0-0753-73d0-8254-eabde2493f6c` 2026-08-13. Это более свежее решение, чем историческое ревью
в `2026-08-13-loot-structure-proposal.md`. Старый RESULT
`c-exec-g-5a7c-loot-1-001` и кандидат `e0a30194…` не переоткрываются и не меняются; кандидат остаётся
`PRESERVED-PAUSED` и служит уликой/входом.

## Зачем нужен новый отдельный BUILD

- `LootLibrary` замороженного кандидата не принимается как долгосрочная архитектура.
- Временное напольное покрытие может исчезнуть или замениться; править его и лечить размещение
  ручным `supportPosition Y` запрещено.
- Высота появления зависит от физической опоры, не от визуала.
- Разные предметы должны уметь иметь разные модели и разные интерактивные реакции.
- Замороженный кандидат несёт stale-contact дефект: покоящийся коллайдер копит контакт, который
  после pickup может стать ложным шумом.

## Согласованная структура

### 1. `LootDefinition` — тип предмета

Отдельный `ScriptableObject` на тип предмета: стабильный неотрицательный `DefinitionId` (не
`CargoId`, не индекс массива и не display name), `DisplayName`, ссылка на `LootPhysicsProfile`,
необязательная ссылка на `LootVisualProfile`, необязательный `LootBehaviorProfile`/`BehaviorId`.
Комнаты, мировая позиция, support-Y и per-spawn mass override запрещены.

### 2. `LootPhysicsProfile` — единый источник физики

Стабильный `PhysicsProfileId`, на миграции совместимый с нынешними `CargoClassId` 0/1/2; масса,
размеры тела/коллайдера, центр коллайдера и необязательный центр масс. Несколько definitions могут
делить профиль; отдельная масса одного типа означает отдельный профиль, не override строки
раскладки. Friction/grip tuning — только отдельным будущим решением. Inspector показывает
read-only требуемое число обычных полносильных носильщиков, запрашивая живой production-закон из
mass, cargo gravity и per-hand lift ceiling, а не реализуя его второй раз.

### 3. `LootVisualProfile` — presentation в Unity

Prefab и при необходимости локальные position/rotation/scale offsets. Куб допустим только как
явный fallback при отсутствии профиля. Production-модели не обязаны входить в этот BUILD, но путь
выбора prefab обязан реально работать и быть проверен.

### 4. `LootBehaviorProfile` / registry

Definition выбирает стабильный `BehaviorId`; host-side registry направляет его в правило поведения;
per-instance состояние остаётся в `CargoThingState` или явно расширенном engine-free аналоге.
Существующий alarm-clock переводится с выбора по весовому классу на выбор по definition без скрытой
смены его состояний, тайминга, источника события и реакции. BUILD создаёт рабочий seam/dispatch, но
не реализует краску, пятна, новые звуки/VFX или набор новых контентных реакций. Это узкий dispatch в
уже существующем cargo-thing слое, не общий конвейер комбинаций/handler composition.

### 5. `LootCatalog` — каталог типов

Каталог содержит definitions и используемые profiles. До старта Host он проверяет уникальность
`DefinitionId` и `PhysicsProfileId`, обязательные ссылки, finite positive mass/dimensions и известные
visual/behavior keys. Missing, duplicate и unknown data дают явную ошибку; silent fallback к первому
cargo class запрещён. Каталог — не список экземпляров дома.

### 6. `LootSpawnLayout` — раскладка экземпляров

Каждая строка несёт definition reference/`DefinitionId`, стабильный authoring `SpawnKey` либо
детерминированный порядок для runtime `CargoId`, `SupportId`, локальный планарный X/Z offset и
начальный yaw/rotation. Absolute world Y и дубли mass/model/behavior/room запрещены. Room выводится
из support/scene authority либо валидируется против неё.

### 7. `LootSupport` — scene-owned физическая опора

Стабильный уникальный `SupportId`, явный enabled non-trigger `Collider`, локальное up-направление /
разрешённая верхняя поверхность и room identity/parent-room authority. Из локальных X/Z выполняется
запрос сверху вдоль `-up`, который обязан попасть именно в collider этой опоры с допустимой нормалью.
Spawn pose = hit point + рассчитанный bottom/pivot offset физического профиля. Missing support, miss,
trigger, disabled collider, unsuitable normal и initial penetration валят запуск до Host; Y-fallback
нет. Floor использует структурный невидимый collider, а не ковёр/visual mesh. Столы, тумбы и полки —
такие же опоры. Декор, пересекающий физическую поверхность, является отдельным content defect и не
маскируется spawn-системой. После pickup/drop предмет опирается на тот же реальный collider.

### 8. Runtime/network identity

`CargoId` — runtime identity экземпляра; `DefinitionId` — identity типа; `PhysicsProfileId` /
совместимый `CargoClassId` — identity физического профиля. Первый безопасный шаг добавляет
`DefinitionId` в `CargoState` и `CargoSnapshot` рядом с существующим class/profile id; core/network
передают только стабильные primitive IDs, никогда `UnityEngine.Object`. Host-цепочка:
layout → catalog → definition → physics profile → support-resolved pose → `CargoState`.
`CargoBody` читает physics profile; snapshot несёт `DefinitionId`; client выбирает prefab по
`DefinitionId`. Модель нельзя выводить из `CargoId` или physics/class id.

### 9. Authoring / Inspector

Для каждой строки видны `CargoId`/`SpawnKey`, item name + `DefinitionId`, effective mass/dimensions,
derived required holders + max-holders warning, выбранная модель/fallback, behavior, room/support и
resolved pose/validation status. Есть быстрые переходы к definition/profile. Массу меняют только в
physics profile; проверяют после остановки Play и нового Host start; общий профиль влияет на все
использующие его definitions.

### 10. Миграция текущих данных

Три существующих профиля переносятся без изменения: 48/100/240 кг и текущие dimensions. Создаются
десять named `LootDefinition` с распределением 5/3/2 и десять строк layout. Список замороженного
кандидата — допустимый вход: Bedside Radio, Kitchen Timer, Hall Key Box, Remote Control, Desk Clock;
Tool Box, Food Crate, Record Case; Strongbox, Travel Trunk. Конкретное definition старого будильника
должно быть недвусмысленно названо и единственное получать alarm behavior; его опубликованное
правило поведения не меняется. Table/counter placements привязываются к физическим опорам, floor
placements — к структурному floor collider, не к временному покрытию. После миграции остаётся один
authoritative path. Старые `LootLibrary`/`CargoSpawnPoint` consumers/tests удаляются или мигрируют;
если четыре legacy-компонента нужны контракту лаборатории, их совместимость должна быть явно
ограничена и тестом доказана как неавторитетная — второго молча работающего fallback нет.

### 11. Обязательный stale-contact correctness fix

Покоящийся cargo остаётся твёрдым. Contact, накопленный пока cargo inactive, не может стать
force/noise после поздней activation. Переход inactive → active очищает/сбрасывает соответствующее
окно, не ломая live contacts и one-shot noise. Регрессия: ударить resting cargo, подождать, поднять —
stale noise нет; свежая active collision — обычный noise ровно один раз; реальный sight/situation не
подавляется протухшим cargo event.

### 12. Acceptance matrix

**Headless:** все copy/with/snapshot paths сохраняют `DefinitionId`, profile identity и
`ThingState`; три identity независимы; behavior dispatch идёт по definition; duplicate/missing IDs,
invalid profiles и unknown keys отвергаются; silent class fallback отсутствует.

**Unity EditMode/PlayMode:** каждая layout-строка попадает в exact support collider; низ реального
`CargoBody` касается опоры без penetration; invalid support падает явно; mass/dimensions доходят до
реального `Rigidbody`/collider; client visual выбирается по `DefinitionId`, cube fallback работает;
resting/carried solidity зелёная; stale-contact последовательность зелёная.

**Owner-eye/manual:** выделить одному definition отдельный лёгкий/тяжёлый profile, перезапустить
Host и проверить реальный carry-height/lift outcome разным числом рук; удалить/заменить покрытие без
правки layout Y; проверить named item/model mapping на Host и client.

### 13. Граница первого BUILD

**Входит одним owner-approved BUILD:** data types/catalog/layout/support, validation, миграция десяти
предметов, primitive IDs в host state/network snapshot, работающий prefab-selection seam с fallback,
definition-based behavior dispatch seam, Inspector, stale-contact correction, headless + Unity
tests, полный RESULT и настоящий rollback/reapply, если этого требует выпущенный контракт.

**Не входит без отдельного контентного решения:** production art/models, paint/decal, новые
sounds/VFX, market/personal value, sale, damage/destruction, procedural/random loot generation.

## Оценка Направления

Структура пригодна: она разделяет тип/экземпляр/физику, не выводит идентичность из индекса или массы,
даёт один валидируемый источник данных, отвязывает физическую высоту от временного визуала и
сохраняет сетевой авторитет primitive-only. Нового продуктового решения перед BUILD не требуется.
Технический PLAN свободен выбрать конкретные числовые IDs, форму registry, authoring key и размещение
классов по файлам, пока все инварианты и acceptance matrix выше остаются целиком.

END_OF_FILE: live/indie-game-development/work/2026-08-13-loot-owner-architecture-handoff.md
