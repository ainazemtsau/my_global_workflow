# CALL c-exec-poligon-a0-001 — Полигон М1 A0: read-only activity seam

> **STATUS: PLAN HANDOFF REPLACED FOR LAUNCH.** Owner-approved PLAN frozen at
> `f80bf700c26376edb7965eef3481cc04607834c3`; launch the separate BUILD-only packet
> `work/c-exec-poligon-a0-001-build-call.md`. This file remains the original outcome contract.

to: executor
direction: indie-game-development
node: g-9c41
task: M1-A0
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
issued: 2026-07-10 (s-shape-poligon-m1-001; owner «А»)

goal: |
  Газовое ядро отдаёт канонический read-only снимок активных клеток и измеримые счётчики
  работы одного шага, пригодные для лаборатории, S4 и сетевого профилирования, при этом
  авторитетное состояние, результат тика и MeaningChecksum остаются byte-identical.

context: |
  Прочитать live/indie-game-development/work/poligon-m1-shape-2026-07-10.md,
  knowledge/g9c41-gas-engine-SPEC.md и knowledge/g9c41-lanes-venues.md.
  Phase 0 одновременно идёт в C:\projects\Unity\GasCoopGame_dev и переносит continuous
  source injection в authoritative step. Этот лег получает отдельный
  C:\projects\Unity\GasCoopGame_core, branch core. До первого изменения сравнить текущий
  Phase-0 diff/status read-only: BUILD разрешён только при доказанно непересекающейся
  поверхности. Last verified product base из live-state = origin/main @a644e5db;
  обязательны fetch + §Re-sync и запись фактического SHA.

boundaries: |
  Только read-only diagnostics/API и тесты. Не строить collapse, rollup, auto-partition,
  sleep/wake policy, network wire, Unity UI или render. Не менять MeaningChecksum и не
  добавлять diagnostics в authoritative state. Не трогать source injection, SimInstance
  path или любой файл, изменённый in-flight Phase 0. Не редактировать GasCoopGame_dev.
  Если ActiveCell seam невозможно получить без пересечения с Phase 0 либо с горячими
  VoxelField.cs/VoxelFaceFlow.cs, STOP с checkpoint — ожидание лучше конфликтного кода.

done_when: |
  1. GasCoopGame_core создан/проверен по карте площадок: branch core от свежего origin/main,
     worktree clean, tools/check.ps1 green до изменений, UnityLockfile отсутствует.
  2. Предполётный overlap-report перечисляет Phase-0 changed files и доказывает нулевое
     пересечение с A0 diff; иначе корректный исход = STOP/checkpoint без кода.
  3. Публичный read-only снимок перечисляет каждую текущую активную клетку ровно один раз
     в каноническом порядке и отдаёт счётчики работы шага, достаточные различить active
     cells/faces и wake/sleep activity; чтение не может мутировать поле.
  4. С одинаковыми входами observer OFF и ON дают byte-identical authoritative bytes,
     MeaningChecksum и loopback trajectory; planted mutation/ordering controls падают.
  5. Снимок оплачивается только по явному запросу; обычный Step не получает domain-scan
     или диагностическое выделение памяти. Стоимость запроса и нулевая цена OFF записаны.
  6. Independent RED-first tests, zero-float/int-overflow guards по применимому Core scope,
     tools/check.ps1 -Deliver green, fresh-session G5 could-not-refute.
  7. До merge: дождаться c-exec-lv-ingest-phase0-001 MERGED, rebase на новый origin/main,
     повторить полный check; merge slot 2. До этого ветка может быть готова, но не мержится.

return: |
  RESULT с точным SHA/base, overlap-report, путями API/tests, observer OFF/ON byte evidence,
  counter sample, cost evidence, -Deliver transcript, fresh G5 verdict/family и статусом
  merge dependency. review: n/a — light additive diagnostics change, если PLAN не поднимает
  frozen-spec/strong-check изменение; иначе вернуть обязательное review-evidence.

budget: максимум половина focused day; при выходе за бюджет STOP и вернуть split.

launch:
  lane: A
  venue: C:\projects\Unity\GasCoopGame_core (branch core; СОЗДАТЬ/ПРОВЕРИТЬ; headless)
  machine: ПК
  base: origin/main @a644e5db last verified; §Re-sync фиксирует фактический SHA
  conflict_surface: только новый read-only diagnostics/API + tests; ноль Phase-0 files
  depends_on: []
  merge_queue: слот 2, только после c-exec-lv-ingest-phase0-001 MERGED
  gates: G5 = свежая сессия; owner-eye = n/a, headless evidence

END_OF_FILE: live/indie-game-development/work/c-exec-poligon-a0-001-call.md
