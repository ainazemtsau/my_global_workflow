RESULT s-work-g-5a7c-cargo-delta-b0-checkpoint-001 (call: c-exec-g-5a7c-cargo-delta-1-001)
direction: indie-game-development
play: work
node/task: g-5a7c/t-cargo-delta-1
outcome: |
  Часть B0 опубликована и принята Направлением как сильный code/control checkpoint, но НЕ как
  закрытие t-cargo-delta-1 и НЕ как полностью выполненная B0.

  Exact reviewed candidate a67d1d038f7b40c581177fc560801fb8ff6005f1 вошёл вторым parent
  merge 403d66e8ad6ebf83bbf982b19d208e43b589d020 и опубликован tip
  97ca2c98485f158d3367103b202000481e1e74d7 в origin/main и origin/dev. Реестр,
  state machine, last-published drift, removal/re-entry, NaN safety, timer dirty reason,
  invalid-config fail-safe и durable negative/default controls имеют code/test/review evidence.

  B0 не поменяла получателей и доставку: тот же полный CargoSnapshot[] по-прежнему идёт в
  host-local ApplySnapshots и существующий ObserversRpc; sparse/delta RPC и B1 отсутствуют.
  Но live Unity shadow counter, реальные serialized/wire bytes и 60 секунд покоя не сняты.
  Поэтому экономия числом не выдумывается, t-cargo-delta-1 остаётся ready, а продолжение
  c-exec-g-5a7c-cargo-delta-1-002 регистрируется blocked до освобождения Unity-слота
  скриншотной волной. Unity сейчас не запускается и слот не резервируется.

  Инвариант владельца про звон, разлив, след и их окончания остаётся обязательной приёмкой
  B1/C. B0 его не реализует и не объявляет реализованным. NOW и screenshot-wave не меняются;
  B0 не становится гейтом пяти кадров.
evidence: |
  Product handback:
  C:\projects\Unity\GasCoopGame_dev\docs\results\c-exec-g-5a7c-cargo-delta-1-001.md
  Исходная полная candidate-версия:
  C:\my_global_workflow\52c8\GasCoopGame_dev\docs\results\c-exec-g-5a7c-cargo-delta-1-001.md

  Перепроверено этой ногой read-only на product checkout:
  - checkout чист, branch dev, HEAD 97ca2c98485f158d3367103b202000481e1e74d7;
  - git ls-remote origin: refs/heads/main == refs/heads/dev ==
    97ca2c98485f158d3367103b202000481e1e74d7;
  - a67d1d038f7b40c581177fc560801fb8ff6005f1 parent =
    cb0a8b019b97a32d389392547f60fb12c0f6f1d9;
  - 403d66e8ad6ebf83bbf982b19d208e43b589d020 parents =
    9a6abec80cea5b865c9c235686fbd75c4ba57cf2 +
    a67d1d038f7b40c581177fc560801fb8ff6005f1;
  - merge manifest ровно 10 путей: CargoSnapshotRegistry.cs + meta,
    NetworkWalkerCourier.cs, NetworkConnectionSettings.asset/.cs, product RESULT,
    три registry test files и test csproj;
  - на этих десяти путях candidate -> merge diff пуст; candidate -> published меняет
    только docs/results/c-exec-g-5a7c-cargo-delta-1-001.md, остальные девять blobs
    byte-identical;
  - код опубликованного NetworkWalkerCourier сначала делает shadow ObserveFullSnapshot(cargo),
    затем передаёт тот же cargo в host-local ApplySnapshots и ReceiveSnapshotsObserversRpc;
    ObserversRpc по-прежнему вызывает ApplySnapshots с тем же полным массивом.

  Product receipt записывает повторённые на интегрированной линии проверки:
  targeted 38/38 PASS; full Release 442/442 PASS; tools/check.ps1 green;
  tools/check.ps1 -Deliver green. Manifest не содержит scene, prefab, art, screenshot,
  presentation или householder paths.

  review-evidence: делегированный handback из source thread
  01a01d08-42a9-7080-ba66-34eb203656f9 записывает отдельную свежую физическую
  review-сессию exact a67d1d038f7b40c581177fc560801fb8ff6005f1: PASS без материальных
  findings. Она подтвердила registry/state machine, last-published drift, removal/re-entry,
  NaN safety, timer dirty reason, invalid-config fail-safe, durable negative controls,
  default metrics control, неизменённую full-array delivery, exact manifest и clean tree.
  Fresh checks в той review: 38/38, 442/442, tools/check green.
  refuted-register: none — финальная exact-candidate review не вынесла findings.

  Честные границы review/receipt: не проверены live Unity counter, реальные serialized/wire
  bytes, 60-second idle capture, Unity compile/import и B1.

  Построчная сверка t-cargo-delta-1:
  1. registry/headless tests — code/control evidence есть;
  2. shadow implementation — есть, но live count/bytes и число экономии ОТКРЫТЫ;
  3. zero recipient/delivery change — подтверждено manifest, blob parity и прямым чтением
     опубликованного courier;
  4. B1 atomic delivery/catch-up/consumer change — НЕ начиналась;
  5. single host sees house — live evidence ОТСУТСТВУЕТ;
  6. 60 seconds idle / zero cargo bytes — measurement ОТСУТСТВУЕТ;
  7. финальный one-commit rollback — остаётся частью будущей B1 acceptance.
state_changes: |
  1. Закрыть возвращённую call-card c-exec-g-5a7c-cargo-delta-1-001 и переместить её в
     cards/closed/, сохранив все текущие поля и журнал. Причина:
     «B0 handback принят как code/control checkpoint; t-cargo-delta-1 не закрыта, потому что
     live counter/serialized bytes и 60 секунд покоя отсутствуют; продолжение
     c-exec-g-5a7c-cargo-delta-1-002 зарегистрировано blocked».
  2. t-cargo-delta-1 сохранить status: ready и весь done_when без изменений. Блок note заменить
     на точный post-checkpoint текст:

     **НЕ СЛУЖИТ ПЯТИ КАДРАМ, ЗАКРЫТИЕ ВОЛНЫ НЕ ГЕЙТИТ.** Вторая из четырёх ног
     по физике груза.

     **B0 ОПУБЛИКОВАНА КАК СИЛЬНЫЙ CODE/CONTROL CHECKPOINT, НО НЕ ЗАКРЫТА.**
     Exact reviewed candidate `a67d1d038f7b40c581177fc560801fb8ff6005f1` опубликован
     в `origin/main` и `origin/dev` tip
     `97ca2c98485f158d3367103b202000481e1e74d7`. Registry/state machine,
     headless 38/38, full Release 442/442 и независимая exact-candidate review зелёные.
     Полный `CargoSnapshot[]` всё ещё доезжает тем же получателям; B1/sparse delivery нет.

     **B0 ЕЩЁ ТРЕБУЕТ ЖИВОГО ЗАМЕРА.** Нет Unity shadow counter, реальных
     serialized/wire bytes и 60 секунд покоя; экономия числом не заявлена.
     `c-exec-g-5a7c-cargo-delta-1-002` blocked до освобождения Unity-слота
     скриншотной волной. До этого Unity не запускать и слот не резервировать.

     **B1 ЖДЁТ ВОЗВРАТА И ИНТЕГРАЦИИ ОБЕИХ ЗАВИСИМОСТЕЙ:**
     `c-exec-g-5a7c-cargo-sleep-repair-1-001` и `c-exec-g-5a7c-beam-1-001`.
     До этого не начинать sparse/delta RPC, removal delivery, catch-up или смену
     клиентской full-replacement семантики.

     **STATE OBSERVABILITY НЕ РЕАЛИЗОВАНА B0.** Звон, разлив, след и их окончания
     должны оставаться видимы/слышны каждому клиенту как обязательная B1/C acceptance;
     технические состояния не нужны, мёртвые будущие поля не сохраняются.
  3. Создать work/c-exec-g-5a7c-cargo-delta-1-002-call.md с точным содержанием:

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
       B0 уже даёт live shadow metrics API, но ни одного runtime-числа ещё не снято.
       CALL остаётся blocked, пока screenshot-wave не освободит Unity-слот.
     boundaries: |
       До перевода call-card в ready не резервировать слот и не запускать Unity.
       Не начинать B1, sparse/delta RPC, removal delivery, catch-up или изменение
       получателей/клиентской full-replacement семантики. Не трогать screenshot,
       scene, art, prefab, householder и работу скриншотной волны.
       Не объявлять реализованной state-observability: это обязательная B1/C acceptance.
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
  4. Зарегистрировать call-card c-exec-g-5a7c-cargo-delta-1-002:
     _kind: call
     _bet: bet-g-5a7c-wave-5
     status: blocked
     to: executor
     for: t-cargo-delta-1
     play: work
     issued: 2026-08-20
     call: work/c-exec-g-5a7c-cargo-delta-1-002-call.md
     repo: C:\projects\Unity\GasCoopGame_dev
     engineering_contract: legacy:c-exec-g-5a7c-cargo-delta-1-001
     description: «Живые B0 shadow/serialized bytes и 60 секунд покоя после освобождения слота»
     unblock_when: «скриншотная волна освободила Unity-слот; до подтверждения слот не
     резервировать и Unity не запускать»
     note block:
     «Только B0 runtime evidence. B1 запрещена до возврата и интеграции
     c-exec-g-5a7c-cargo-sleep-repair-1-001 и c-exec-g-5a7c-beam-1-001.
     State-observability остаётся B1/C acceptance, а не результатом этой ноги.»
  5. NOW.md, bet-g-5a7c-wave-5, screenshot-wave, остальные task/call cards, slot state,
     knowledge и product repo не менять.
  6. Сохранить полный RESULT в
     history/2026-08-20-s-work-g-5a7c-cargo-delta-b0-checkpoint-001.md и записать log
     в журналы t-cargo-delta-1 и нового continuation CALL; закрытая возвращённая карточка
     получает ту же history-ссылку в причине закрытия.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done — перечитаны t-cargo-delta-1, исходный наряд B0/B1 и активная ставка g-5a7c; checkpoint не служит пяти кадрам и не гейтит их.
  - 2 Owner inputs (owner): skipped — владелец недоступен и уже поручил автономно «тебе самой нужно выстроить работу»; нога не выносит продуктового вердикта, не выдумывает runtime-числа и не запускает Unity.
  - 3 Do the work: done — product handback, published ancestry/manifest/blob parity, проверки и fresh exact-candidate review сведены в Direction checkpoint; выписано только узкое runtime-продолжение.
  - 4 Self-check: done — все семь done_when сверены по отдельности; live bytes, idle capture, B1, host-live и rollback оставлены открытыми; full-array delivery и неизменные получатели перепроверены.
  - 5 Close: checkpoint — возвращённый running id очищается, задача остаётся ready, новый blocked continuation сохраняет незакрытую работу; review CALL не открывается.
close: checkpoint — не light и не done; product review поддерживает code/control checkpoint, но live runtime evidence и B1 acceptance отсутствуют.
log: B0 опубликована как code/control checkpoint без изменения доставки; live counter/bytes и 60 секунд покоя остаются, continuation ждёт Unity-слот
next: |
  CALL c-exec-g-5a7c-cargo-delta-1-002 зарегистрирован blocked для t-cargo-delta-1.
  Его goal — живые B0 shadow/serialized measurements и 60-second idle capture.
  unblock_when: скриншотная волна освободила Unity-слот; до подтверждения не резервировать
  слот и не запускать Unity. B1 остаётся запрещена до возврата и интеграции cargo repair A
  и beam leg.

END_OF_FILE: live/indie-game-development/history/2026-08-20-s-work-g-5a7c-cargo-delta-b0-checkpoint-001.md
