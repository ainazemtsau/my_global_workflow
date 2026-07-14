# Полигон M1 — принятый маршрут сильной интеграционной сцены

status: OWNER-ACCEPTED
accepted: 2026-07-14, owner actual words: «Маршрут принимаю»
scope: Direction route; не BUILD и не разрешение запускать product CALL
accounting_rule: числового потолка product legs нет; 24.07 — контрольный review, не стоп проекта

## 1. Что именно строим

Финиш M1 — одна регулируемая сетевая сцена, в которой:

- Dungeon Architect собирает минимальный набор project-owned модулей;
- хотя бы один модуль получен из PGG как editor-time dependency-free static prefab;
- reusable character V1 подключён к стабильному сокету авторитетной позиции и не владеет Core-позой;
- газ имеет одного Core-владельца и один атомарный deterministic Step;
- реакции и тестовый взрыв наблюдаемы;
- один контролируемый стеновой пролом действительно меняет топологию и поток между областями;
- full flood и дальний/S4 tier видимы;
- один и тот же сценарий повторяется на двух реальных машинах;
- названное слабое железо даёт реальный timing/admission ceiling;
- HUD показывает agree/divergence, planted divergence обнаруживается;
- потеря peer/host явно и контролируемо завершает текущий прогон;
- snapshots, telemetry, видео, fresh G5 и owner verdict позволяют закрыть результат доказательствами.

Это не шесть отдельных песочниц. NearGasSimulationLab остаётся внутренним gas-стендом; M1 закрывается только общей сценой.

## 2. Что сознательно не входит

- враги, миссия и damage/consequence;
- production UI, production audio, save/load;
- late join, matchmaking, host migration;
- полная разрушаемость и большой content/module set;
- Character V2 как обязательный гейт; V3 находится за пределами M1.

## 3. Шесть трасс

| Трасса | Текущая правда | Предпосылка | Результат трассы | Площадка | Главный конфликт | Proof и merge |
|---|---|---|---|---|---|---|
| 1. Gas authority | L1 не доставлен; execute-002@5c783e07 — CHECKPOINT / NOT DELIVERED; product v20 отстаёт от OS v21 | Полный PLAN-AMEND/Re-sync, whole-packet semantic GREEN и отдельный fresh Direction binding review | Один engine-free Core-владелец, bounded work/memory, atomic Step, checksum/replay seams, Unity integration path | lane A, отдельный `GasCoopGame_core` | Любая другая работа, меняющая Core/PROGRAM authority | Каждый gas leg проходит свой RED/review/G5; одновременно только один Core-mutating BUILD; merges в main по одному |
| 2. Level / DA / PGG | PGG spike доказал bake → dependency-free static prefab → SnapGridFlow/BuiltSceneRoomReader; production stage провалился из-за отсутствия нашего Level/Module Contract | Свежий current-v21 PLAN successor; project-owned 0.5 m grid, sockets, portals, occupancy/apertures, anchors и validators | DA runtime composition + PGG только editor-time bake/import + минимальный M1 module set | lane D, новый проверенный levels worktree, один Unity Editor | `LevelIngestion`, сцены, module prefabs и общие import-настройки | Contract/validators сначала; DA adapter и PGG baker после контракта; merge каждого слоя отдельно; старой Phase 0 в маршруте нет |
| 3. Character | Owner-approved V1 PLAN frozen; существующий BUILD CALL не является launch authority | Собственная current-v21 full-packet проверка и свежая площадка | Reusable prefab, input/control/follow-camera и stable authoritative-position socket; Core-поза остаётся внешней | свежий presentation worktree, без Core | player prefab, input wiring и integration scene | EditMode contract + owner PlayMode decouple proof; merge отдельно до общей сцены |
| 4. Visual | `c-visual-009` LOCKED и основан на старых authority/scene assumptions | M0+C1+L3+I1; motion также ждёт immutable per-Step datum, остальные эффекты — E1/D1/X1 | Минимальная читаемость движения газа, источника, двери и controlled breach на текущем ABI | lane B / `dev2` только после reconciliation | `GasView`, Render и общие сцены | Fresh visual reconciliation; performance/readability evidence; merge после foundation, по одному |
| 5. Common M1 scene | Единой launch-authority сцены пока нет; старые Phase0/P2a0 площадочные допущения устарели | Свежая assignment-проверка lane C/lab; M0+C1+L3+I1 и доставленные Level/Character seams | Базовая сцена → реакции/взрыв → реальный breach → flood/S4 | lane C/lab после свежего preflight | сцены, bootstrap, wiring всех подсистем | Интеграционные acceptance runs после каждого merge; финальная склейка последовательна |
| 6. Network / min-spec / evidence | Критерии ратифицированы; конкретное binding min-spec железо ещё не выбрано | Объединённая сцена, input-bus/FishNet edge, две реальные машины и названный CPU/GPU/RAM | Sync/divergence/admission/disconnect proof, профиль, capture, fresh G5 и owner verdict | lane E: PC + Mac/Windows VM/вторая физическая машина | network bootstrap, build artifacts и финальная сцена | Один и тот же scripted scenario, planted divergence, controlled disconnect; binding fresh G5 отдельной сессией; owner close последним |

Площадки из старой карты перед любым BUILD проходят свежий preflight: карта C/D могла устареть после Phase 0 и P2a0.

## 4. Что может идти параллельно

| Период | Можно параллельно | Нельзя параллельно |
|---|---|---|
| Сейчас | Этот Direction route (закрыт), NearGas PLAN-AMEND/Re-sync planning-only, read-only подготовка min-spec, отдельная g-d3a8 reconciliation | Любой product BUILD, Unity mutation или старый Level/Character executor CALL |
| После полного v21 handoff + fresh Direction review | Gas L1 BUILD; свежий Level PLAN; current-v21 Character V1 check; назначение worktrees | Два Core-mutating gas BUILD; два Unity Editor на одной площадке; merges общей сцены |
| После Level Contract | Level validators, DA adapter, PGG baker и Character V1 могут идти рядом с gas на разных worktrees | Одновременные изменения `LevelIngestion`/scenes/modules; одновременные merges |
| После M0+C1+L3+I1 | Fresh visual reconciliation и подготовка common-scene integration | Продолжение старого visual BUILD без reconciliation |
| После I2 | Far-tier и runtime-topology планы могут готовиться рядом | Core BUILDs всё равно идут последовательно |
| Финал | Подготовка scripts/capture checklist может идти заранее | Product merges, двухмашинный run, min-spec run, binding G5 и owner verdict идут в проверяемой последовательности |

Главное правило: независимые worktrees могут строить независимые seams одновременно; общие authority, сцены и main объединяются по одному.

## 5. Точный текущий ledger, а не потолок

На момент принятия маршрут видит **34 обязательных логических product legs** и условные legs ниже. Число служит прозрачному accounting. Оно не является бюджетом, лимитом или причиной выкидывать нужную работу.

### Gas — 20

| Код | Leg |
|---|---|
| G01 | L1 Core authority |
| G02 | L2 bounded work/memory |
| G03 | C1 committed identity |
| G04 | M0 Unity migration |
| G05 | L3 единственный Unity integration path / lab foundation |
| G06 | L4 source handling |
| G07 | L5 doors/apertures |
| G08 | L6 topology/read model |
| G09 | A0 integration adaptation successor |
| G10 | M1-GAS-PROBE |
| G11 | M1-GAS-CORE |
| G12 | S4-OPEN |
| G13 | S4-ROLLUP |
| G14 | S4-PARTITION |
| G15 | R0 reactions |
| G16 | E1 emitting/moving source |
| G17 | D1 doors |
| G18 | T1 test explosion |
| G19 | X1 controlled breach/topology change |
| G20 | GAS-LAB integration close |

### Level / DA / PGG — 6

| Код | Leg |
|---|---|
| LV0 | Fresh owner-approved PLAN; старой Phase 0 нет |
| LV1 | Project Level/Module Contract |
| LV2 | Validators |
| LV3 | DA runtime composition adapter |
| LV4 | PGG editor-time baker/importer |
| LV5 | Minimal M1 modules, включая хотя бы один PGG-derived module |

### Character — 1

| Код | Leg |
|---|---|
| CH1 | V1 stable socket + drop-in player prefab |

### Visual — 2

| Код | Leg |
|---|---|
| VIS1 | Fresh reconciliation под текущие ABI/данные + gas motion/look/perf |
| VIS2 | Минимальные runtime visuals источника, двери и breach |

### Common scene — 2

| Код | Leg |
|---|---|
| SCN1 | DA+PGG+CH1+sole gas authority+HUD+manual step base scene |
| SCN2 | Reactions/test explosion/breach/flood/S4 integrated scenario |

### Network / evidence — 3

| Код | Leg |
|---|---|
| NET1 | Input-bus/FishNet edge integration |
| NET2 | Two-machine run + controlled peer/host disconnect |
| EVD1 | Named min-spec, timing/admission, divergence, capture, fresh G5, owner verdict |

### Условные legs

- `P1` — только если R0 действительно требует отдельной PlayerSense/topology migration implementation;
- `VIS-DATA` — только если L3 не отдаёт достаточный immutable per-Step movement datum;
- `RUNNER` — только если current-v21 проверка подтвердит его как реальную предпосылку;
- `CH-V2` — опционально и не закрывает M1; `CH-V3` вне M1.

## 6. Последовательность

1. Закрыть старое appetite-состояние свежим Direction `review`: числовой cap снимается, 24.07 становится контрольным review, принятый финиш и cuts сохраняются.
2. Завершить NearGas PLAN-AMEND/Re-sync и вернуть точный v21 handoff в отдельный fresh Direction binding review.
3. Только после GREEN открыть новый Gas L1 BUILD и параллельно подготовить свежие Level PLAN / Character V1 current-packet check / площадки.
4. Доставить Core foundations и Level Contract; затем развести DA, PGG, Character и gas по независимым worktrees.
5. Последовательно слить foundation seams в common M1 scene; только затем reconciled visual и runtime topology/reactions.
6. Завершить общую сцену, сеть, две машины, named min-spec, capture, binding fresh G5 и owner verdict.

## 7. Текущие HOLD

Свежий Level executor CALL **не выпущен**. До него обязательны одновременно:

- текущий OS engineering contract v21 прочитан целиком и отражён в полном handoff packet;
- свежая repo/base/branch/worktree authority и отсутствие конфликтующего Unity Editor доказаны;
- lane D назначен заново, а lane C/D assumptions сверены после Phase 0/P2a0;
- PLAN не содержит старую Phase 0 и начинает с project-owned Level/Module Contract;
- owner видит и принимает PLAN; BUILD остаётся отдельным CALL.

Character BUILD, visual BUILD и общий scene BUILD также не открываются этим маршрутом. Принятие маршрута — разрешение считать и планировать зависимости, а не разрешение мутировать продукт.

## 8. Исторические свидетельства, не launch authority

- старая Phase 0 — NOT DELIVERED / NEVER RESUME;
- старый A0 — STOP / NOT DELIVERED;
- checksum plan и прежние Unity attempts — входы для successor, не разрешение продолжить;
- PGG spike завершился `fail_stage`, но доказал editor-time bridge;
- NearGas dashboard закрыт, однако gas PROGRAM остаётся только дочерней трассой M1;
- P2a0 выбрал Candidate A, но lifecycle/fresh-G5 drift чинится отдельно;
- G01 сейчас канонически NOT DELIVERED; незакоммиченные planning-only изменения продукта не являются Direction-прогрессом.

END_OF_FILE: live/indie-game-development/work/poligon-m1-integration-route.md
