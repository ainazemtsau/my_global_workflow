# CHARTER — indie-game-development

direction_id: indie-game-development
status: live_shell_created

## Mission

Создать направление для разработки оригинальной indie co-op игры через Direction OS, начиная не с продукта, а с проверенной live-оболочки: CALL/RESULT/writer loop должен сначала доказать, что состояние направления можно безопасно создавать, читать и обновлять.

Игровая/product-амбиция направления сохраняется как будущая цель: инновационная игра с сильным системным ядром, включая будущую работу с симуляцией газа, grid/topology и co-op взаимодействиями. Эта оболочка не является переносом старого направления и не является стартом разработки игры.

## Success criteria

1. `live/indie-game-development/` существует как новый чистый live direction с базовыми файлами `CHARTER.md`, `TREE.md`, `NOW.md`, `LOG.md`.
2. Следующий шаг маршрутизирован в `play: shape` для проверки setup/live-loop, а не в product execution.
3. Любой будущий перенос знаний из `archive/directions/indie-game-development` оформляется отдельной bounded transfer/import работой с evidence, без автоматического legacy import.
4. Product execution начинается только после явного shape/review маршрута и отдельного CALL; не в этом bootstrap frame.

## Hard constraints

- Do not restore `archive/directions/indie-game-development`.
- Do not import legacy state.
- Do not launch Codex/product execution.
- Do not create a Unity project.
- Do not transfer old code.
- Do not treat old project files as source of truth.
- Archive may be mentioned only as a future evidence source for separate later transfer/import work.
- Direction state lives in `live/indie-game-development/`.

## Lenses

- workflow: CALL/RESULT/writer loop, state shape, OS compliance.
- product: game direction, player-facing value, co-op/systemic novelty.
- technical: future engine/runtime/prototype constraints, gas/grid/topology feasibility.
- evidence: every done claim needs concrete proof; no confidence-only closure.

## Product repos

- workflow_state_repo: `github.com/ainazemtsau/my_global_workflow`
- product_repo: none selected in this frame
- future_product_repo: to be decided by a later shaped bet

## Pre-mortem

This direction failed three years from now because:

1. Legacy archive was blindly imported and polluted the new live direction.
   - mitigation: archive is parked as future evidence only; no import in bootstrap.
2. Product execution started before the OS loop was verified.
   - mitigation: first next CALL is setup/live-loop shape, not Codex/product work.
3. Unity/project/code decisions were made before scope and evidence gates existed.
   - mitigation: product repo, Unity project, and code transfer are explicitly out of scope.
4. The game direction collapsed into disconnected gas-only documents.
   - mitigation: product and technical lenses must stay connected in later shape work.
5. Claims of completion were accepted without durable state or writer evidence.
   - mitigation: done claims must point to live files, RESULT packets, commits, or explicit check output.

## Outside view

New AI-assisted game directions usually fail early when they jump from ambition directly into implementation. Simulation-heavy indie games add extra risk: prototypes can consume time before the core loop and project discipline are proven. The correct first sequence is therefore operational, not creative: create the live direction shell, verify that CALL/RESULT/writer loop works, then shape the first real product foundation bet.

END_OF_FILE: live/indie-game-development/CHARTER.md
