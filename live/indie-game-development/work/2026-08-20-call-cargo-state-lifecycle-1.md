# НАРЯД: глобальный lifecycle игрового состояния предметов — t-cargo-state-lifecycle-1

CALL c-exec-g-5a7c-cargo-state-lifecycle-1-001
to: executor
direction: indie-game-development
play: work
node: g-5a7c
task: t-cargo-state-lifecycle-1
repo: C:\projects\Unity\GasCoopGame_dev
kind: engineering
engineering_contract: 36
goal: |
  Каждый клиент наблюдает существующее gameplay-state предмета, включая его окончание,
  независимо от sparse pose/hold и будущего room interest.
context: |
  Product authority:
  live/indie-game-development/history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md.
  Durable invariant:
  live/indie-game-development/knowledge/gameplay-item-state-is-observable-to-every-client.md.
  Timer/interest evidence:
  live/indie-game-development/history/2026-08-20-s-research-g-5a7c-interactive-density-part1-recheck-001.md.
  B0/B1 repair boundary:
  live/indie-game-development/work/2026-08-17-call-cargo-delta-1.md.
  Background mandate:
  live/indie-game-development/work/2026-08-20-background-cargo-engineering-mandate.md.

  CALL остаётся blocked до принятого B0 runtime receipt, интегрированного repair A и
  интегрированного beam на одной fresh product main. После этого исполнитель сам снимает
  fresh basis и выбирает transport HOW.
boundaries: |
  Не менять screenshot tasks, screenshot scenes/art/assets или их слоты и не делать эту
  работу воротами текущей волны. Не изобретать новые gameplay-state или presentation meaning:
  мигрировать только состояния, реально существующие на fresh basis.

  Sparse pose/hold остаётся отдельной B1. Не использовать уменьшающийся RemainingSeconds
  как dirty field, не фильтровать gameplay-state room interest, не держать Integrity,
  ThingStateId, ThingRemainingSeconds, Moved или reserved placeholders без потребителя.
  Внутренние технические состояния остаются серверными.

  RPC, SyncType, отдельный stream или иной transport выбирает инженерия. Не начинать product
  work до unblock receipt; слот заранее не резервировать. Требуемый repo-native инструмент
  недоступен — честный STOP, не workaround.
done_when: |
  1. Для каждого gameplay-state предмета, существующего на выбранной базе, server-authoritative
     start/change/end несёт server tick и монотонную per-item sequence/revision; host и remote
     client consumer делают состояние видимым/слышимым, duplicate/out-of-order input не
     воскрешает end, а late join получает ровно current active state.
  2. Конечное состояние выражено authoritative end tick под revision: клиент выводит остаток
     локально, а длительность не делает предмет dirty каждый tick. Runnable evidence показывает
     traffic только на start, semantic change, end и catch-up; room-interest/pose filter не скрывает
     ни одно из них.
  3. После миграции CargoSnapshot и его writer/reader не содержат Integrity, ThingStateId,
     ThingRemainingSeconds, Moved или reserved placeholders без consumer; внутреннее состояние
     не экспортируется. RESULT даёт exact basis/commits/manifests, host/remote/late-join/order/
     end/no-timer-traffic evidence, build/gates, rollback и fresh binding review receipt.
return: |
  Полный product RESULT HOME с disposition каждой из трёх строк, exact basis/commits/manifests,
  runnable artifacts/check output, assumptions/cuts и ссылкой на fresh binding review.
  Никакой delivery claim без полного repo-native contour.
budget: one focused half-day after unblock

END_OF_FILE: live/indie-game-development/work/2026-08-20-call-cargo-state-lifecycle-1.md
