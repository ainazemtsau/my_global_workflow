# Бэклог ночного рефакторинга — GasCoopGame

updated: 2026-07-11 (s-work-control-layer-delta-001; сид = read-only скан wf_1fe01b6f-9bb, 2 сканера, база GasCoopGame main @a644e5db, все строки проверены first-hand по файлам/grep)
rules: plays/refactor-night.md (нулевое изменение поведения; доказательства обязательны; мерж — только владельческий утренний батч)
statuses: ready | in-flight | proven (ветка ждёт мержа) | failed:<причина> | merged | day-lane | DO-NOT-TOUCH

## П1 — первоочередные (рекуррентная боль / мёртвый код)

| id | Что | Зона | Файлы | Размер |
|---|---|---|---|---|
| R-01 | Чинка false-RED `-Deliver` на смерженных легах: no-delta fallback `result-check.ps1:186-192` валидирует ВСЕ docs/results, а статус-regex (:111) режет ретро-правленные «MERGED to main» у c-exec-021/c-visual-005. Ночной вариант = (b) docs-only: переписать 2 статус-строки в уже допустимую форму «DELIVERED on `dev` (merged to `main` @…)». Вариант (a) — аддитивно принять терминальную форму «MERGED to main» в regex + selftest-кейсы | tools/docs | tools/result-check.ps1(+selftest), docs/results/c-exec-021.md, c-visual-005.md | S |
| R-02 | Удалить мёртвый класс ReactionLayer (t-3 игрушечный producer, ноль инстанцирований; grep чист по Assets/tests/tools) + поправить прозаический комментарий GridEvent.cs:48 | Core | Core/Field/Layers/ReactionLayer.cs(+.meta), Core/Field/Events/GridEvent.cs | S |
| R-03 | Убрать мёртвый coarse-сценарный стек Core/Sandbox: GasScenario+GasScenarioJson+GasScenarioApplicator (TickPacer ОСТАВИТЬ — единственный продакшн-потребитель Sandbox). Снимает коллизию двух одноимённых GasScenario. Тесты стека удалить; SandboxCoverageTests — только их секции | Core | Core/Sandbox/*, tests/Sandbox/* (кроме TickPacer*), zero-float-scan.ps1 (только комментарий :11) | M |
| R-04 | ASCII-санация tools/*.ps1: 11 BOM-less скриптов с non-ASCII (нарушают FRICTION.md:18, латентный класс поломки под PS 5.1/ru-RU ANSI). Только комментарии + 1 Write-Host строка (type-hardcode-scan.ps1:213) — матчеры не трогать | tools | 11 файлов (список в скане) | M |

## П2 — гигиена документов и мелкий код

| id | Что | Зона | Размер |
|---|---|---|---|
| R-05 | INTERIM-COARSE-FAR-TIER.md: дописать пропущенный S4-коллатерал (Sandbox-стек из R-03 + Field/Chunks/CellHash.cs — потребители только REMOVE-list) | docs | S |
| R-06 | Core/AGENTS.md «## Status» протух («Still NO gas simulation (t-2+)» при 112-файловом движке) — обновить только Status, Rules не трогать (проверены — точны) | docs | S |
| R-07 | ADR-0010: дописать датированный аддендум «DA correction» (commit 8def7f2f) — DoorSill.cs:6 и IKeyedLevelProducer.cs:10 цитируют несуществующую секцию; историю D5/D6 не переписывать | docs | S |
| R-08 | c-exec-023 tasks.md:72 — датированная поправка стейл-чисел (70.8/×4=283 → committed matrix 88.8165/355.266); чекбоксы `- [x]` НЕ трогать (их читает -Deliver) | docs | S |
| R-09 | FRICTION.md DF-2 строка «Durable fix DEFERRED» → дописать «RESOLVED by c-exec-028 (ADR-P-0005)» | docs | S |
| R-10 | TopologyDocument.cs:16 — битый XML-cref на несуществующий namespace (класс живёт в Topology.Coarse, не Field.Coarse); comment-only | Core | S |
| R-11 | Дедуп guard-хелперов CheckCell(×2)/AddChecked(×2) по Voxel-файлам → один internal static helper; строки сообщений сохранить дословно (никакой тест их не пиннит, но держим ноль-поведение). НЕ приближаться к строкам 286-288 SparseDominantNearGasField (см. DNT-1) | Core | S |
| R-12 | Дедуп приватных GasTypeRegistry-билдеров в 4 тест-файлах → overloads на существующих fixtures; только хойст конструкторов, ни одного assert/имени/тела теста не менять; кол-во тестов до/после идентично (1525) | tests | M |

## П3 — усиление ворот (ночь-с-оговоркой: аддитивно; если live-прогон краснит существующее — НЕ садить, вынести в дневной CALL)

| id | Что | Зона | Размер |
|---|---|---|---|
| R-13 | DF-7: strong-check принимает фабрикованный `{"score":100}` — валидировать полную схему mutation-score.v1 (schema+changeId+validMutants>0) + seeded-miss в selftest; каждый существующий mutation-json проверить на диске ДО посадки | tools | M |
| R-14 | DF-9: hygiene.ps1 assert-guard пофайловый → по-методный; seeded miss; live-прогон обязан остаться зелёным, иначе day-CALL | tools | M |
| R-15 | DF-11: review-check.ps1 — Int32-overflow номера finding'а даёт сырой exception вместо кастомного FAIL; отрицательный Rounds не отвергается; два однострочника + selftest-кейсы | tools | S |

## DO-NOT-TOUCH регистр (ночная линия НЕ планирует эти места никогда)

- **DNT-1** Чексум-стабы literal-0: SparseDominantNearGasField.cs:286-288 (BiasChecksum/ImpulseQueueChecksum/FluxCarryChecksum) — пиннуты тестами (!=0; before==after на throw-путях). «Упрощение» = смена чексум-поверхности.
- **DNT-2** НЕ «дедупить» TopologyStableIds.Mix на Fnv1a64.StepInt32: те же константы, РАЗНАЯ функция (int32-целиком vs по-байтно) — унификация меняет все StableId/ProfileHash.
- **DNT-3** НЕ перенумеровывать дубли ADR-id (2×ADR-0012, 2×ADR-0016): result-check v18 валит -Deliver на висячих цитатах из docs/results. Только аддитивная дизамбигуация.
- **DNT-4** Дублирование тест-fixtures между областями (VoxelTestFixtures vs TopologyTestFixtures vs Coarse) — НАМЕРЕННАЯ независимость независимого тест-автора; не дедупить.
- **DNT-5** DEFERRED-FINDINGS DF-1/3/4/6/8 — поведенческие фиксы с owner-ack'нутыми отложенными CALL: полный дневной контур (RED-автор и т.д.), не ночь.
- **DNT-6** LoopbackOwnerEyeDirector → в сцену: day-lane (Unity + owner-eye), не ночь.
- **DNT-7** type-hardcode-scan «enum-only» ограничение: расширение = изменение поведения ворот с риском false-positive — дневная судейская работа.
- **DNT-8** Архивация merged openspec-папок (чтобы -Deliver их не перегейтивал) — действие писаря/владельца, не ночной ход.

## Примечания скана

- TODO/HACK/FIXME/[Obsolete] по Core/tests/tools: НОЛЬ. «Живые» кандидаты, оказавшиеся используемыми (не садить): SparseLoopbackResult, Sense*-хелперы, реакционные хендлеры, CoreBuildMarker (retained по Core/AGENTS.md), RepresentationTags-константы (named seams в чексуме).
- «Медленные тесты» first-hand не проверяемы (нет per-test таймингов) — кандидат-S: опциональный `--logger trx` для будущего триажа.
- Зависимости: R-03 сажает → R-05 сжимается до строки CellHash; R-11 диff держать вдали от DNT-1 строк.

END_OF_FILE: live/indie-game-development/work/refactor/backlog.md
