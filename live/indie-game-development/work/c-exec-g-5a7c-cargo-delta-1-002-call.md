CALL c-exec-g-5a7c-cargo-delta-1-002
to: executor
direction: indie-game-development
play: work
node: g-5a7c
task: t-cargo-delta-1
repo: C:\projects\Unity\GasCoopGame_dev
kind: engineering
engineering_contract: legacy:c-exec-g-5a7c-cargo-delta-1-001
goal: |
  Получить на опубликованной B0 честные живые baseline-измерения трафика груза,
  достаточные для решения о B1.
context: |
  Published basis: 97ca2c98485f158d3367103b202000481e1e74d7.
  Product receipt:
  docs/results/c-exec-g-5a7c-cargo-delta-1-001.md.
  Direction order:
  live/indie-game-development/work/2026-08-17-call-cargo-delta-1.md.
  Repair authority before B1:
  t-cargo-state-lifecycle-1 and
  live/indie-game-development/work/2026-08-20-call-cargo-state-lifecycle-1.md.
  B0 уже даёт live shadow metrics API, но ни одного runtime-числа ещё не снято.
  CALL остаётся blocked, пока screenshot-wave не освободит Unity-слот.
boundaries: |
  До перевода call-card в ready не резервировать слот и не запускать Unity.
  Не начинать B1, sparse/delta RPC, removal delivery, catch-up или изменение
  получателей/клиентской full-replacement семантики. Не трогать screenshot,
  scene, art, prefab, householder и работу скриншотной волны.
  Не реализовывать item-state и не считать его B1/C-полем: он принадлежит отдельной
  t-cargo-state-lifecycle-1. B1 после неё остаётся только pose/hold.
done_when: |
  1. Live host/server run на точном named commit записывает raw full/would-publish
     counters, ticks/duration/roster и реальные serialized bytes полного и
     would-be delta payload; экономия вычислена из raw numbers, не оценена.
  2. Отдельный 60-second idle capture записывает фактические cargo wire bytes;
     ненулевой результат называется и объясняется, а не превращается в «ноль».
  3. RESULT называет Unity/slot/run artifacts и exact basis, подтверждает, что
     опубликованная full delivery/получатели не менялись, B1 не начиналась,
     и перечисляет все оставшиеся runtime gaps.
return: |
  Полный product RESULT HOME: exact basis, raw counters/bytes, способ и длительность
  замера, run artifacts, выполненные проверки, clean-tree status и честные gaps.
budget: one focused session after unblock

END_OF_FILE: live/indie-game-development/work/c-exec-g-5a7c-cargo-delta-1-002-call.md
