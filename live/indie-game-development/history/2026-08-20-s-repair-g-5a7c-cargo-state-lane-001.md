RESULT s-repair-g-5a7c-cargo-state-lane-001
direction: indie-game-development
play: repair
node/task: g-5a7c/t-cargo-delta-1
outcome: |
  Рассинхрон до B1 устранён на уровне Direction authority.

  B1 теперь имеет одну обязанность: sparse-доставка позы и удержания. Глобально наблюдаемое
  gameplay-state предметов вынесено в отдельную задачу `t-cargo-state-lifecycle-1` и отдельный
  blocked engineering CALL `c-exec-g-5a7c-cargo-state-lifecycle-1-001`. Эта задача обязана завершиться
  до B1 и несёт ordered start/change/end, server tick + sequence/revision,
  late-join current-state catch-up, клиентского потребителя и запрет room-interest фильтрации.

  Уменьшающийся `ThingRemainingSeconds` больше не может быть обычным dirty-полем B1: конечное
  состояние выражается authoritative end tick под монотонной revision, а клиент выводит остаток
  локально. `Integrity`, `ThingStateId`, `ThingRemainingSeconds` и `Moved` не резервируются и не едут
  мёртвым заделом: state-задача удаляет нечитаемые wire-поля после переноса живой семантики,
  внутреннее техническое состояние остаётся только на сервере.

  Свежий порядок зафиксирован так: B0 runtime evidence + интегрированный repair A +
  интегрированный beam → global item-state lifecycle → B1 pose/hold → C → D. Реализация,
  Unity-слоты и screenshot wave этой repair-ногой не затронуты.
evidence: |
  Fresh Direction basis после fetch/reset:
  origin/main = `2c3e7412fc3dcd0808779658913be3e30d31f4d4`.
  `uv run --locked python osctl.py context --for t-cargo-delta-1`:
  владелец ничего не должен; текущий continuation =
  `c-exec-g-5a7c-cargo-delta-1-002`, status blocked.
  `uv run --locked python osctl.py check --direction indie-game-development`:
  механических проблем нет; 61 существующее неблокирующее замечание — baseline этой ноги.

  Owner authority:
  `history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md`:
  «Игровые состояния предметов, которые существуют в мире — звон, разлив, след и их окончание, —
  должны быть видны или слышны каждому клиенту. Внутренние технические состояния показывать не
  требуется. Способ передачи выбирает инженерия; мёртвые поля ради будущего держать не надо.
  В текущую волну скриншотов реализацию не добавлять.»

  Direction engineering reconstruction (не owner quote):
  sparse pose/hold delta остаётся отдельной полосой, а глобально наблюдаемое gameplay-state
  получает отдельный lifecycle carrier/consumer с server tick/sequence, start/change/end и
  late-join current-state catch-up; уменьшающийся RemainingSeconds не делает предмет dirty каждый
  tick; room interest в будущем не фильтрует эту state-полосу; внутренние/нечитаемые поля
  удаляются, не резервируются. Direction вывела этот технический разрез из фактического owner
  invariant выше плюс research/B0 evidence ниже. Delegated engineering prompt был ошибочно принят
  за owner word; forward repair:
  `history/2026-08-20-s-repair-g-5a7c-cargo-owner-provenance-001.md`.

  `history/2026-08-20-s-research-g-5a7c-interactive-density-part1-recheck-001.md`:
  current `AlarmClockCargoThing` уменьшает `RemainingSeconds` каждый такт; compare-all-fields
  оставляет неподвижный звонящий предмет dirty 30 раз/с; room interest нельзя применять к
  глобальным звон/разлив/след и их окончаниям.

  `history/2026-08-20-s-work-g-5a7c-cargo-delta-b0-checkpoint-001.md`:
  B0 опубликована на product tip `97ca2c98485f158d3367103b202000481e1e74d7` без изменения
  получателей/full-array delivery; live counter/serialized bytes/60-second idle остаются в
  `c-exec-g-5a7c-cargo-delta-1-002`. Значит B0 не реализовала state-observability и не даёт
  права подключать её timer-dirty predicate как B1.

  Fresh dependency cards:
  `c-exec-g-5a7c-cargo-sleep-repair-1-002` = running на WIN-U2, contract 36;
  `c-exec-g-5a7c-beam-1-001` = ready на WIN-U1;
  `c-exec-g-5a7c-cargo-delta-1-002` = blocked до освобождения Unity-слота.
  Старые dependency ids `-001` сохранены только как история и не используются новым графом.

  Engineering contract current = 36; `C:\projects\Unity\GasCoopGame_dev\validation.config`
  `synced_contract_version = 36`. Новый root CALL законно pin-ится на 36 и остаётся blocked.
state_changes: |
  1. В `work/2026-08-17-call-cargo-delta-1.md` добавить видимую repair-границу перед прежним текстом:
     B0/его runtime continuation не расширяются; B1 служит только pose/hold и не читает
     `Integrity`/`ThingStateId`/`ThingRemainingSeconds`/`Moved` как dirty-поля; global item-state принадлежит
     `t-cargo-state-lifecycle-1`; окончание выражается end tick/revision без timer-dirty; state не
     фильтруется room interest; порядок B0 runtime + A + beam → state task → B1 → C → D.
     Прежняя доказательная часть work-документа сохраняется.

  2. `t-cargo-delta-1`: сохранить id/_kind/_bet/status/_pos/журнал; goal уточнить до
     «Sparse pose/hold: неизменившийся груз не едет каждый tick, а gameplay-state живёт отдельно».
     В done_when сохранить B0 registry/shadow/zero-behavior, но определить B1 как атомарный sparse pose/hold
     после B0 runtime + A + beam + state task, отдельно доказать host/remote/stale catch-up, ноль pose/hold
     bytes за 60 секунд покоя и one-commit rollback. В note сохранить B0 checkpoint/runtime pointer и записать
     новый dependency graph и границу «B1 = pose/hold, state = отдельная задача».

  3. `c-exec-g-5a7c-cargo-delta-1-002`: сохранить blocked/status/call/repo/contract/unblock_when и прочие поля;
     note уточняет, что нога даёт только B0 runtime evidence, B1 после неё остаётся pose/hold и ждёт current A
     `-002`, beam `-001` и `t-cargo-state-lifecycle-1`; global state не входит в room-interest scope.

  4. `work/c-exec-g-5a7c-cargo-delta-1-002-call.md`: добавить в context ссылки на state task/CALL;
     boundaries уточнить, что runtime-нога не реализует item-state и не считает его B1/C-полем.

  5. Создать `t-cargo-state-lifecycle-1`: task, `_bet: bet-g-5a7c-wave-5`, status blocked, goal =
     «Каждый клиент наблюдает gameplay-state предмета через отдельный от pose/hold lifecycle»,
     unblock после принятого B0 runtime, интегрированных A + beam на fresh product main, без предварительной
     резервации слота. Done_when — три строки: ordered global lifecycle + live consumer + late join;
     end-tick/revision без per-tick dirty и без room-interest фильтра; отсутствие мёртвых wire-полей при доказанных
     host/remote/late-join/order/end/no-timer-traffic/build/rollback/binding-review checks. Note содержит
     owner/mandate pointers, dependency graph, свободу transport HOW и запрет изобретать отсутствующее gameplay.

  6. Создать полный `work/2026-08-20-call-cargo-state-lifecycle-1.md` и CALL packet
     `c-exec-g-5a7c-cargo-state-lifecycle-1-001`: to executor, direction/node/task/repo указаны, kind engineering,
     `engineering_contract: 36`; goal — every-client state observability independent of pose/room; context ссылается на
     owner history, knowledge, research, B0/B1 boundary и background mandate; boundaries запрещают screenshot expansion,
     новое gameplay, timer-dirty, room filtering, dead/reserved fields и запуск до unblock; transport остаётся инженерии.
     Done_when содержит ровно три пункта из карточки; return требует exact basis/commits/manifests,
     runnable evidence, assumptions/cuts и fresh binding review; budget one focused half-day after unblock.

  7. Создать `c-exec-g-5a7c-cargo-state-lifecycle-1-001`: call, `_bet: bet-g-5a7c-wave-5`, status blocked,
     to executor, for `t-cargo-state-lifecycle-1`, play work, issued 2026-08-20,
     call `work/2026-08-20-call-cargo-state-lifecycle-1.md`, repo `C:\projects\Unity\GasCoopGame_dev`,
     engineering_contract 36, description «Глобальный item-state lifecycle/consumer отдельно от sparse pose/hold»,
     тот же compact unblock, note с global/order/catch-up/end-tick/dead-fields boundaries и записью, что B1 ждёт task close.

  8. `i-three-snapshot-fields-ride-and-nobody-reads-them-001`: сохранить id/kind/level/route/_pos/журнал;
     evidence = `work/2026-08-20-call-cargo-state-lifecycle-1.md`; issue фиксирует нечитаемые поля, timer-dirty улику и запрет
     B1 считать/резервировать/молча удалить их как delta-поля; review_when — возврат state task до B1 с
     lifecycle/order/catch-up/global/end-tick/no-dead-wire evidence, иначе B1 остаётся blocked.

  9. `i-all-cargo-travels-every-tick-001`: сохранить header/evidence/журнал; issue отделяет текущую full pose/hold
     цену и будущий B1 от global semantic state lifecycle; review_when требует B0 runtime+B1 pose/hold evidence,
     отдельные state-task traffic/order/catch-up checks и итоговую runtime-research до issue close.

  10. Одним `osctl leg close` сохранить полный RESULT в
      `history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md` и добавить одну log-строку в журналы:
      `t-cargo-delta-1`; `c-exec-g-5a7c-cargo-delta-1-002`; `t-cargo-state-lifecycle-1`;
      `c-exec-g-5a7c-cargo-state-lifecycle-1-001`;
      `i-three-snapshot-fields-ride-and-nobody-reads-them-001`; `i-all-cargo-travels-every-tick-001`.

  11. `NOW.md`, bet/node/CHARTER, существующие statuses/slots других CALL, repair A, beam,
      research continuation, screenshot tasks, knowledge, product repo и `archive/**` не менять.
      Треки не создаются и не удаляются; owner panel для этого направления не объявлен.
captures: []
decisions_needed: []
play_check:
  - 1 Name the contradiction: done — B1/C acceptance смешивала sparse pose/hold с глобальным gameplay-state, а свежий B0 registry уже умеет помечать timer dirty.
  - 2 Reconstruct: done — newest-first прочитаны origin/main 2c3e7412, B0 checkpoint/current continuation, running repair A -002, ready beam -001, owner authority, research evidence и обе issue-card.
  - 3 Propose corrected state: done — Direction engineering reconstruction: отдельная blocked task/CALL перед B1; B1 только sparse pose/hold; state lane несёт lifecycle carrier/consumer, server tick + sequence/revision, start/change/end, late-join catch-up, end-tick без timer-dirty и global interest; C/D наследуют раздельные interest-границы; все текущие факты сохранены.
  - 4 Confirm (owner): done — фактические слова владельца: «Игровые состояния предметов, которые существуют в мире — звон, разлив, след и их окончание, — должны быть видны или слышны каждому клиенту»; «Внутренние технические состояния показывать не требуется»; «Способ передачи выбирает инженерия; мёртвые поля ради будущего держать не надо»; «В текущую волну скриншотов реализацию не добавлять» — источник `history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md`.
  - 5 Friction: skipped — OS-hole нет; это ожидаемый concurrent state desync после B0/A checkpoint, исправляемый repair без изменения правил.
log: B1 отделена от глобального gameplay-state — pose/hold остаётся sparse, lifecycle вынесен в отдельную blocked-задачу перед B1, мёртвые wire-поля не резервируются
next: |
  return-to-owner; writer после атомарного apply/commit/push возвращает fresh frontier,
  не запускает существующий ready/running/blocked CALL внутри этой ноги.
END_OF_FILE: live/indie-game-development/history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md
