# PGG (Procedural Generation Grid, FImpossible Creations) — анализ 2026-07-10

session: s-pgg-analysis-001 (owner-задание «давай проведём анализ»; workflow wf_f8a59385-eda: исходники 801 .cs
из кэша Asset Store + User Manual 26 стр. + Quick Start + веб-разведка + fit-judge). Владелец «да» на спайк.
Версия в кэше = 1.6.6.2.12 = текущая в сторе (Jun 2026) — обновлять нечего.

## Вердикт

- **Роль (a) — редакторский помощник авторинга модулей: ПОДХОДИТ (механика подтверждена кодом), принять после спайка.**
  Edit-режим генерации раскладывает обычные префаб-инстансы под чистым контейнером БЕЗ живых PGG-компонентов
  (PrefabUtility.InstantiatePrefab: FGenerators.cs:17-37; GenerationMethods.cs:275-298). Сохранение контейнера
  статичным префабом = наш скрипт ~50 строк (паттерн: TileDesignerWindow.GUI.Panels.cs:590+; снять GridPainter +
  скрытый GridPainterData + ObjectStampEmitter; mesh-combine печь в ассет или выключить). GridPainter: рисуешь
  клетки + дверные направляющие (SpawnInstruction) по позициям сокетов DA. 113 SR_*-правил (стены/полы/двери/
  лестницы/мебель/кабели), Build Planner (185 узлов), Tile Designer (меши без 3D-пакета).
- **Роль (b) — батч-вариации по сидам: ПОДХОДИТ, скриптуется напрямую.** Public static API:
  IGeneration.GenerateFieldObjects(FieldSetup, grid, container, ...) / GenerateFieldObjectsRectangleGrid(preset,
  size, seed, container) — GenerationMethods.cs:264,351; готовый паттерн BuildPlannerExecutor.Generating.cs:556-633
  (RandomSeed=false, Seed=base+i). Ловушка: сид через ОДИН глобальный static System.Random (FGenerators.SetSeed) —
  батч-скрипт не должен дёргать чужой RNG посреди генерации.
- **Роль (c) — рантайм после DA: ОТКЛОНИТЬ.** Глобальный static System.Random + float/Perlin + опц. физика-осадка;
  сид-вывод менялся между версиями плагина минимум дважды (Readme 1.0.1; 1.6.6.2.11); детерминизм нигде не
  документирован; 5-летняя бета. Локстеп-яд. Не нужен: контент замораживается в префабы в редакторе; DA остаётся
  единственным рантайм-сборщиком; решение 2026-06 «PGG за швом» не нарушается.

## Пайплайн (подтверждён)

PGG наполняет комнату (редактор) → static prefab-модуль → регистрация в DA SnapGridFlow → DA собирает уровень в
рантайме по сиду → BuiltSceneRoomReader читает построенную сцену generator-blind → воксели/газ. Маркеры
(стены/двери/GasSourceMarker) — наши: печь в тайл-префабы или авто-навес через хук OnSpawnProcessor
(Core/Generating/OnSpawnProcessor.cs). CellSize FieldSetup ↔ габариты DA-модуля ↔ шаг газ-сетки — согласовать один раз.

## Чего PGG НЕ решает

Арта НОЛЬ — расставляет НАШИ префабы (Presets Directory пуст; демо = учебные примеры). Нужен один согласованный
low-poly кит (стены/пол/рамы/мебель/пропсы) — совпадает с каноном дешёвого враппера. Оболочки/сокеты DA-модулей
всё равно авторит владелец. Кривая обучения: «deep logic understanding, similar like visual scripting» (сам автор);
до первого модуля реалистично 2-4 дня; туториалы 2021-22 могут не совпадать с текущим UI.

## Красные флаги

1. **Unity 6.3 НЕ подтверждена** (API 2019-эры, IMGUI-окна) — kill-риск, проверяется в первый час спайка.
2. **Windows DPI-баг** прячет кнопку Paint (Readme) — лечится DPI-совместимостью; не путать с «сломалось на 6.3».
3. Бета 5 лет; поддержка «highly limited» (слова автора); фиксы — файлами на форуме; roadmap 1.6.7 не вышел.
4. Ноль прецедентов связки PGG+DA — первопроходцы; документации API нет, опора = полные исходники в пакете.
5. **Пиновать версию**; не обновлять посреди продакшена; статичные префабы иммунны к смене сид-вывода.
6. История багов: node-graph index-out-of-range (01.2024), asmdef missing-method (03.2023), Stack Spawner (05.2024).

## Ссылки

Store: assetstore.unity.com/packages/tools/utilities/procedural-generation-grid-beta-195535 · Форум:
discussions.unity.com/t/released-procedural-generation-grid/849158 (активен по 11.2025) · Manual PDF в пакете ·
Плейлист автора: youtube.com/playlist?list=PL6MURe5By90mRPke0_vkxaqu0lRfeI8zl · Распакованные исходники (temp):
scratchpad/pgg_src (пересобрать: tar -xzf из кэша Asset Store-5.x/FImpossible Creations/...).

Спайк: work/c-spike-pgg-001-call.md. Наследник результата: PLAN шага M1-4 Полигона (DA Phase 1 / модули).

END_OF_FILE: live/indie-game-development/work/pgg-analysis-2026-07-10.md
