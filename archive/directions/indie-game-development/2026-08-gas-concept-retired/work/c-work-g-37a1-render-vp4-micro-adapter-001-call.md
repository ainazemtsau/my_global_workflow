# CALL c-work-g-37a1-render-vp4-micro-adapter-001


> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

to: session
direction: indie-game-development
track: t-render
play: work
node: g-37a1
task: t-11
for: t-11
issued: 2026-07-29 by s-repair-g-37a1-render-vp4-task-001
budget: one short Direction session plus one product child no larger than half a focused day

## goal

Доказать на настоящем VP4-чанке, что авторитетная разреженная микромаска Core отображается без
потери смысла, а текущие критерии визуальной читаемости имеют один ограниченный продуктовый выход.

## context

- `live/indie-game-development/NOW.md`: t-7 задаёт канонический sparse microtopology contract;
  t-11 задаёт границу первой VP4-интеграции и visual responsibility.
- `history/2026-07-29-s-repair-g-37a1-render-vp4-task-001.md`: точный owner-verdict,
  принятая архитектура и причины срезов.
- `work/voxel-play-4-backend-evaluation-2026-07-28-v2.md`: F3/Core-grid остаётся единственным
  источником истины, VP4 — заменяемое производное представление.
- Ответ Kronnect: per-microvoxel delta не выдаётся; `OnChunkChanged` сообщает dirty chunks;
  `GetMicroVoxels == null` неоднозначен для полного solid/empty; latest beta обещает
  `OnChunkGeometryApplied` и geometry revisions после установки collider.

## boundaries

- Этот root остаётся blocked, пока t-7 не завершена, VP4 не доступен локально и владелец не назвал
  свободный product slot. Repair ничего не покупает, не импортирует и не меняет product repository.
- Core — единственная игровая правда. VP4 не определяет topology, gas, snapshot/hash, FishNet order,
  player controller или исход DigCommand; float-кисть пакета не становится авторитетной командой.
- Product child выдаётся только с owner-selected slot и `engineering_contract: 31`; не использовать
  `GasCoopGame_dev`. Никакого второго render/backend контура в этой задаче.
- В первый Core тело считает Partial твёрдым. Micro-aware player collision, полный будущий горизонт
  VP4 и массовая полировка картинки остаются вне этой задачи.

## done_when

После фактической установки VP4 адаптер пакетно переводит Solid/Empty/Partial и точную Core-маску
в `VoxelChunk`/`MicroVoxels`. Debug round-trip совпадает с Core, включая различение полного solid,
полного empty и неоднозначного `null` от `GetMicroVoxels`. `OnChunkChanged` используется только как
dirty-сигнал; готовность представления подтверждается geometry revision / `OnChunkGeometryApplied`,
а не становится игровой правдой. Одна тестовая сцена показывает два различимых вида вещества и
читаемую до реза породу. Записаны mesh/collider latency и отображение вариантов базового блока
0,5 и 1 м. Core, газ, FishNet и player controller пакет не подменяет.

## return

Checkpoint RESULT регистрирует один bounded product child с точным slot и contract pin. Закрывающий
RESULT приходит только после product evidence и отдельной свежей G5-проверки, сопоставленной со
всеми пунктами done_when; до этого t-11 и root остаются открыты.

END_OF_FILE: live/indie-game-development/work/c-work-g-37a1-render-vp4-micro-adapter-001-call.md
