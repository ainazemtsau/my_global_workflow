# CALL c-exec-poligon-s4-opening-001 — Полигон М1 A1: bounded S4 no-pop proof

to: executor
direction: indie-game-development
node: g-9c41
task: M1-A1
repo: github.com/ainazemtsau/GasCoopGame
kind: engineering
issued: 2026-07-10 (s-shape-poligon-m1-001; owner «А»)

goal: |
  Одна размеченная газовая область переходит fine→collapsed→fine с точным сохранением
  авторитетного смысла и без видимого скачка, а дешёвый детерминированный digest ловит
  смысловое расхождение и даёт надёжную основу следующим S4-легам.

context: |
  Стартовать только после MERGED c-exec-lv-ingest-phase0-001 и MERGED
  c-exec-poligon-a0-001. Прочитать live/indie-game-development/work/
  poligon-m1-shape-2026-07-10.md, knowledge/g9c41-gas-engine-SPEC.md
  (Факт 2–5, §3 collapse/expand, §4 швы 4–5, §5 S4, §6 п.2/4) и карту площадок.
  PLAN обязан сверить текущие MeaningChecksum members и source-injection semantics на
  фактическом tip; старый пересказ не является источником.

boundaries: |
  Это micro-proof одной заранее размеченной области, не production S4. Не строить общий
  room-rollup transport, runtime LOD manager, automatic sub-partition production code,
  150-room level, far vertical strata, DA content, network wire, damage или новую визуальную
  систему. Не расширять и не оживлять CoarseBandStep. Не вскрывать архитектурный лок.
  Auto-subpartition и area-aware rollup здесь получают только проверяемую декомпозицию/RED
  контракт следующих легов. Любая попытка спрятать их build в этот CALL = STOP/split.

done_when: |
  1. Owner-readable PLAN на свежем merged tip принят владельцем до BUILD; он перечисляет
     все сохраняемые meaning fields, held-vs-discard semantics, источник truth для digest,
     rollback и точный cut между micro-proof и следующими S4-легами.
  2. Independent RED-first battery падает на потере массы/TypeId/mix-overlay/region meaning,
     неканоническом порядке, silent digest collision в planted meaning mutation, boundary
     pop и диагностике, случайно попавшей в checksum.
  3. На одной labelled held-region fine→collapsed→fine сохраняет все актуальные
     authoritative meaning members byte-/value-exact по принятому PLAN; соседняя область
     не получает re-flux расхождения.
  4. Cheap digest одинаков для одинакового смысла, меняется на каждом planted meaning
     mutation из PLAN и на одном и том же flooded fixture стоит менее 10% времени полного
     MeaningChecksum; обе стоимости записаны.
  5. Owner-eye на существующем минимальном debug consumer: переход через границу области
     не даёт видимого скачка концентрации/формы; слова владельца записаны. Никакой новой
     render-полировки ради гейта.
  6. Отдельный next-slice contract перечисляет следующие bounded legs: area-aware
     room-rollup, deterministic auto-subpartition открытого объёма и runtime near/far;
     production code этих трёх частей отсутствует в текущем diff.
  7. tools/check.ps1 -Deliver green, применимые scans/negative controls green,
     fresh-session binding G5 could-not-refute; merge slot 3 только после полного
     merged-main check.

return: |
  RESULT с owner-approved PLAN words, commits, micro-proof paths, точной таблицей meaning
  preservation, digest mutation/cost table, owner-eye words, -Deliver transcript, review
  evidence по текущему product contract, binding fresh G5 verdict/family и next-slice
  contract. Любой незакрытый done_when пункт остаётся explicit checkpoint, не DELIVERED.

budget: максимум половина focused day; при выходе за бюджет STOP и вернуть split.

launch:
  lane: A
  venue: C:\projects\Unity\GasCoopGame_core (branch core; headless; Unity только owner-eye)
  machine: ПК
  base: origin/main @<SHA после MERGED Phase 0 + M1-A0>; §Re-sync обязателен
  conflict_surface: Core/Field S4 micro-proof + tests; один mutating core leg
  depends_on: [c-exec-lv-ingest-phase0-001 MERGED, c-exec-poligon-a0-001 MERGED]
  merge_queue: слот 3
  gates: G5 = свежая сессия; owner-eye = no-pop в существующем debug consumer

END_OF_FILE: live/indie-game-development/work/c-exec-poligon-s4-opening-001-call.md
