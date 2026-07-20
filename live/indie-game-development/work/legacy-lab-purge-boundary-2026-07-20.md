# Legacy Lab purge — простой вердикт

## Один ответ

**Сейчас удаляем только доказанный мусор. Остальные сцены не переделываем, не расширяем и не подключаем
к новой функциональности. Integration Lab создаётся позже вместе с первым реальным feature, которому она
нужна.**

Это самый быстрый безопасный путь: после одного cleanup-root можно вернуться к функционалу, а не строить
отдельный проект по миграции старых демо.

## Удалить сейчас

1. Старый `CharacterV1SceneSetup` builder — никем не вызывается и способен испортить V2 fixtures.
2. `GasBenchmarkScene` + её director/editor — текущего consumer нет; headless benchmark отдельный.
3. `ReactionSandboxScene` + `ReactionSandbox` — только исторические отчёты, current validator нет.
4. Неиспользуемые Dungeon Architect GasLab assets (`CoopSmallSGF`, `GasLabSingle..`, `GasLabDB`,
   `Room_A`, `SnapGridFlowModuleBounds`) и устаревший `docs/c-exec-012-lab-guide.md`.

Точные пути закреплены в `c-exec-program-v2-legacy-lab-purge-001-call.md`.

## Оставить, но не наращивать

- `SampleScene` — единственная стартовая/default scene. Удаление сейчас оставит проект без входа.
- `GasSourcePhase0Demo` — пока держит действующий proof источника газа и двери.
- `GasBuoyancyDemoScene` — на неё ещё ссылается принятый visual proof.
- `GasVoxelSandboxScene` — пока обязательна текущим gas-visual spec.
- `GasVisualScene` — текущий fake-data seam proof.
- `GasLabScene` — текущий analytic visual proof.
- `GasRoomScene` — текущие wiring, lighting и owner-eye validators.
- Три Character V2 proof scenes — действующие character validators, не мусор.

Все семь спорных сцен, кроме Sample, уже не запускаются автоматически: они отсутствуют в Build Settings,
runtime loading и Addressables. Поэтому отдельный runtime «выключатель» только добавит новый мусор. Нужна
одна короткая product-authority запись: **legacy validator, новых consumers не добавлять, удалить сразу
после появления replacement proof в реальной Integration Lab**.

## Что будет, если удалить всё прямо сейчас

- Без Sample проект потеряет текущую launch scene.
- Phase0/GasVoxel/GasRoom удаления сделают действующие specs и tests ложными или красными.
- Мы потеряем текущие visual/topology proofs до появления их реальной замены и потратим больше времени на
  восстановление, чем сэкономим на cleanup.

## Следующий и последний cleanup-шаг

Один V31 root удаляет четыре безопасных семейства, создаёт короткую authority-запись и явно supersede-ит
старые обещания нескольких постоянных Labs. Он **не строит Integration Lab** и **не начинает новую
архитектуру**. После его REPORT Program возвращается к feature work.

END_OF_FILE: live/indie-game-development/work/legacy-lab-purge-boundary-2026-07-20.md
