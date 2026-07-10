# CALL c-exec-poligon-a0-001 — BUILD: Полигон М1 A0 read-only activity seam

> **STATUS: FIRE-READY BUILD-only.** Это отдельный свежий BUILD после owner-approved PLAN.
> Frozen plan/base commit: `f80bf700c26376edb7965eef3481cc04607834c3`.
> Owner approval: `owner-ack:owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved`.

to: executor
direction: indie-game-development
node: g-9c41
task: M1-A0
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
issued: 2026-07-10 (s-work-poligon-a0-build-call-001)
phase: BUILD-only

goal: |
  Газовое ядро отдаёт канонический read-only снимок активных клеток и измеримые счётчики
  работы одного шага, пригодные для лаборатории, S4 и сетевого профилирования, при этом
  авторитетное состояние, результат тика и MeaningChecksum остаются byte-identical.

context: |
  Работать только в C:\projects\Unity\GasCoopGame_core, branch core. Единственный
  архитектурный контур BUILD — owner-approved frozen PLAN в commit
  f80bf700c26376edb7965eef3481cc04607834c3; approval token =
  owner-ack:owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved. До любого RED или
  production edit проверить clean worktree, exact HEAD/ancestry этого commit и перечислить
  plan/spec/ledger artifacts, которые он замораживает. Approval не разрешает отклонения,
  подмены или cuts вне exact frozen PLAN: такое расхождение требует STOP и нового owner-ack.

  Исходный outcome-контракт и shape evidence:
  live/indie-game-development/work/c-exec-poligon-a0-001-call.md,
  live/indie-game-development/work/poligon-m1-shape-2026-07-10.md,
  live/indie-game-development/knowledge/g9c41-gas-engine-SPEC.md и
  live/indie-game-development/knowledge/g9c41-lanes-venues.md.

  Phase 0 = c-exec-lv-ingest-phase0-001 в C:\projects\Unity\GasCoopGame_dev. A0 BUILD
  разрешён параллельно только после read-only overlap-preflight по frozen PLAN surface;
  merge A0 запрещён до проверенного MERGED Phase 0 в origin/main.

boundaries: |
  BUILD-only: не переоткрывать и не переписывать frozen PLAN. Только утверждённые
  read-only diagnostics/API и tests. Не строить collapse, rollup, auto-partition,
  sleep/wake policy, network wire, Unity UI или render. Не менять MeaningChecksum, не
  добавлять diagnostics в authoritative state, не трогать source injection, SimInstance
  path, GasCoopGame_dev или любой Phase-0 changed file. Если frozen PLAN/BUILD требует
  пересечения с Phase 0 либо с горячими VoxelField.cs/VoxelFaceFlow.cs, STOP с checkpoint.
  До MERGED Phase 0 нельзя merge/push-to-main/заявлять DELIVERED; ожидание зависимости —
  корректный checkpoint. Builder не редактирует тесты independent RED test-author.

done_when: |
  1. Preflight фиксирует: venue = C:\projects\Unity\GasCoopGame_core; branch core; clean
     worktree; UnityLockfile отсутствует; frozen PLAN commit ровно
     f80bf700c26376edb7965eef3481cc04607834c3 существует, является стартовым HEAD/base,
     его plan/spec/ledger paths перечислены, baseline tools/check.ps1 зелёный до RED/BUILD,
     а approval token записан без расширения scope.
  2. До production-кода отдельный independent RED-first test-author в свежем контексте
     читает только этот CALL + exact frozen PLAN и коммитит acceptance battery. Вернуть
     identity/session, отдельный RED-test commit и transcript, где тесты падают на frozen
     implementation по ожидаемым причинам. Builder не авторит и не редактирует эти тесты;
     конфликт тестов при rebase возвращается test-author либо даёт STOP.
  3. Предполётный overlap-report перечисляет текущие Phase-0 changed files и frozen PLAN
     build surface; пересечение = 0 до BUILD. После BUILD тот же отчёт подтверждает нулевое
     пересечение уже по фактическому A0 diff; иначе STOP/checkpoint без merge.
  4. Публичный read-only snapshot перечисляет каждую текущую active cell ровно один раз в
     canonical order и отдаёт step counters, достаточные различить active cells/faces и
     wake/sleep activity; чтение не может мутировать поле.
  5. При одинаковых входах observer OFF/ON дают byte-identical authoritative bytes,
     MeaningChecksum и loopback trajectory; planted mutation и ordering controls падают.
  6. Snapshot оплачивается только по явному запросу: обычный Step не получает domain-scan
     или diagnostic allocation. Записаны request cost и нулевая цена OFF.
  7. Применимые Core guards (zero-float/int-overflow), вся independent RED battery и
     tools/check.ps1 -Deliver зелёные на build candidate. Если frozen PLAN объявляет
     frozen/openspec strong-check change, обязателен tree-fresh docs/reviews/review-<id>.md
     с fully dispositioned findings; иначе RESULT содержит `review: n/a — light additive
     diagnostics change` с обоснованием.
  8. Merge gate: дождаться подтверждённого MERGED c-exec-lv-ingest-phase0-001 в свежем
     origin/main, rebase A0 на этот tip, повторить overlap-report, всю battery и -Deliver.
     Затем отдельная fresh-session binding G5 на final post-rebase candidate пытается
     опровергнуть exactness/no-mutation/no-OFF-cost/Phase-0-disjoint claims и возвращает
     COULD-NOT-REFUTE. Только после этого разрешён merge slot 2.

return: |
  RESULT с frozen/base SHA, plan/spec/ledger paths, approval token, RED test-author
  identity/session + отдельным RED commit/transcript, builder commits, pre/post overlap
  reports, API/test paths, observer OFF/ON byte evidence, counter/cost samples, guard и
  -Deliver transcripts, review disposition, Phase-0 merge commit, final rebase SHA,
  binding fresh G5 verdict/session/family и фактический merge SHA. Если Phase 0 ещё не
  MERGED либо post-rebase gates не пройдены, вернуть BUILD-GREEN/WAITING-MERGE или другой
  честный checkpoint; не заявлять c-exec-poligon-a0-001 закрытым и оставить merge pending.

budget: один focused half-day на RED+BUILD, ожидание Phase 0 не входит; выход за бюджет → STOP/split checkpoint

launch:
  lane: A
  venue: C:\projects\Unity\GasCoopGame_core (branch core; fresh BUILD session; headless)
  machine: ПК
  frozen_base: f80bf700c26376edb7965eef3481cc04607834c3
  owner_approval: owner-ack:owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved
  build_dependency: none after clean/frozen/zero-overlap preflight
  merge_dependency: c-exec-lv-ingest-phase0-001 MERGED in origin/main
  merge_queue: slot 2, post-Phase-0 rebase + full rerun + binding fresh G5

END_OF_FILE: live/indie-game-development/work/c-exec-poligon-a0-001-build-call.md
