RESULT s-repair-g-5a7c-cargo-delta-b0-contract-001
direction: indie-game-development
play: repair
node/task: g-5a7c/t-cargo-delta-1
outcome: |
  B0 continuation contract сделан технически исполнимым без изменения product delivery
  и без освобождения текущего blocker.

  Published basis остаётся `97ca2c98485f158d3367103b202000481e1e74d7`.
  После освобождения Unity-слота executor вправе создать один минимальный committed
  measurement-harness `run_head`, чей единственный parent — exact published basis.
  Этот harness является только измерительным артефактом и не переименовывает basis.

  Runtime acceptance теперь честно разделяет четыре слоя: exact FishNet serialization
  реального полного `CargoSnapshot[]`; exact `counterfactual_delta_v1` serialization
  staged would-publish `CargoSnapshot[]` + removed `int[]`; aggregate per-peer LiteNetLib
  datagram-payload bytes/packets для одного реального remote RPC recipient; и явную
  недоступность cargo-only UDP attribution при неизменном combined RPC. Aggregate transport
  запрещено называть cargo traffic.

  Call-card остаётся `blocked` с прежним `unblock_when`. B1, item-state lifecycle, Repair A,
  beam, screenshot scope, NOW, ставка и product repo этой ногой не меняются.
evidence: |
  Fresh Direction basis:
  - `git fetch origin main`: `HEAD == origin/main ==
    24c66006f827e25629da6633d5a6173ea8caeb6a`; detached worktree был чист.
  - `osctl context --direction indie-game-development --for
    c-exec-g-5a7c-cargo-delta-1-002`: current bet `g-5a7c`, task
    `t-cargo-delta-1`, owner waits = nothing.
  - `osctl check --direction indie-game-development`: 61 pre-existing non-blocking
    observations; mechanical problems = none.
  - Base blobs: work CALL `092b3ee645048d1e6c9fa1403ce53426fa3277ed`;
    call-card `564908760c1e058e23aa6984dc35dbff1004a6de`.
  - No direction owner-panel declaration was found in current knowledge.

  Committed Direction evidence:
  - `history/2026-08-20-s-work-g-5a7c-cargo-delta-b0-checkpoint-001.md`
    names exact published basis and re-derives that current courier passes the same full
    cargo array to host-local Apply and the existing ObserversRpc, with live serialized/wire
    bytes and idle capture still open.
  - Current work CALL done_when 2 asks for literal cargo wire bytes while its boundaries
    forbid changing RPC/delivery/recipients. Those two requirements cannot both be satisfied
    after the source audit below.

  Delegated engineering source audit (not owner words):
  - `<codex_delegation>` source thread
    `01a01d08-42a9-7080-ba66-34eb203656f9` reports on exact product basis
    `97ca2c98485f158d3367103b202000481e1e74d7` that one FishNet ObserversRpc carries
    walkers + cargo + householder + delivery; cargo-only UDP/datagram bytes therefore
    cannot be attributed inside that combined RPC without changing transport.
  - The same audit reports that no runtime diagnostic command/seam exists on unchanged
    `97ca`; a named direct-child measurement-harness commit is required while normal
    delivery remains byte/recipient-semantically unchanged.
  - This delegated instruction supplies engineering evidence and scopes this repair.
    It is not cited as a new human-owner quote or owner-only product decision.

  Actual owner authority remains unchanged:
  `history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md` records
  «Способ передачи выбирает инженерия», «ожидаем чистое решение, расширяемое, лучшее»,
  «никаких костылей», «обязательно жёсткая проверка всего», «нужна проверка кода» and
  «В текущую волну скриншотов реализацию не добавлять». Durable product invariant
  `knowledge/gameplay-item-state-is-observable-to-every-client.md` is not modified.
state_changes: |
  1. Replace
     `live/indie-game-development/work/c-exec-g-5a7c-cargo-delta-1-002-call.md`
     against base blob `092b3ee645048d1e6c9fa1403ce53426fa3277ed` with:

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
       Получить на опубликованной B0 воспроизводимый runtime receipt, который честно
       разделяет exact cargo parameter serialization и aggregate peer transport
       и достаточен для решения о B1.
     context: |
       `published_basis`: 97ca2c98485f158d3367103b202000481e1e74d7.
       Product receipt:
       docs/results/c-exec-g-5a7c-cargo-delta-1-001.md.
       Direction order:
       live/indie-game-development/work/2026-08-17-call-cargo-delta-1.md.
       Repair authority before B1:
       t-cargo-state-lifecycle-1 and
       live/indie-game-development/work/2026-08-20-call-cargo-state-lifecycle-1.md.

       Published basis остаётся `97ca2c98485f158d3367103b202000481e1e74d7`.
       Для измерения разрешён один минимальный committed measurement-harness
       `run_head`, чей единственный parent — exact `published_basis`. Receipt называет
       оба commit id; `run_head` не становится новой published/delivery basis.

       На published basis один FishNet ObserversRpc несёт walkers + cargo +
       householder + delivery. Поэтому измеряются и называются раздельно:
       - `fishnet_full_cargo_v1`: exact FishNet serialization bytes реального полного
         параметра `CargoSnapshot[]`;
       - `counterfactual_delta_v1`: exact FishNet serialization bytes measurement schema
         `staged would-publish CargoSnapshot[] + removed int[]`, снятые в том же живом
         tick без rerun или estimate;
       - `litenetlib_peer_aggregate_v1`: exact bytes/packets UDP payload LiteNetLib для
         одного actual remote RPC recipient, включая весь traffic, retransmits и headers
         этого слоя, но не IP/UDP headers;
       - literal cargo-only UDP attribution: unavailable при неизменном combined RPC;
         peer aggregate нельзя называть cargo traffic.

       Actual remote RPC recipient на каждом tick — `NetworkObject.Observers` minus
       `LocalConnection` identity. Замер валиден только при ровно одном active remote
       recipient и fail-closed при изменении roster/observer membership или disconnect.
       CALL остаётся blocked, пока screenshot-wave не освободит Unity-слот.
     boundaries: |
       До перевода call-card в ready не резервировать слот и не запускать Unity.

       Measurement harness не меняет существующие RPC signature/attribute, host Apply,
       `NetworkObject.Observers`, recipients или normal gameplay delivery. Diagnostic
       error/receipt failure/roster change прерывает только diagnostic и никогда delivery.
       B1, sparse/delta RPC, removal delivery, catch-up и item-state не начинать.

       После completion, abort и server stop transport stats state восстановлен.
       Inactive path: никаких copies, serialization, writer, stats, file IO или allocations;
       только observer-presence branch поверх существующего B0 O(N).

       Не добавлять N-vs-0 override, scene/prefab/art change, packet workaround или future
       fields. Не трогать screenshot, householder, Repair A, beam, lifecycle CALL или
       работу скриншотной волны.
     done_when: |
       1. Runtime receipt на exact named `run_head`, direct child `published_basis`,
          записывает raw full/would-publish counters и три exact measurement layers:
          `fishnet_full_cargo_v1`, `counterfactual_delta_v1` и
          `litenetlib_peer_aggregate_v1`; delta bytes сняты из staged live data без
          rerun/estimate, aggregate включает весь LiteNetLib-layer traffic/retransmits/
          headers и явно не называется cargo-only.
       2. Отдельный idle capture с monotonic wall elapsed >=60s записывает
          monotonic start/end, tick start/end и tick count, exact cargo parameter
          serialization bytes per actual recipient плюс aggregate per-peer LiteNetLib
          datagram-payload bytes/packets; ровно один active remote проверен каждый tick,
          roster/observer/disconnect change aborts diagnostic, а literal cargo-only UDP
          attribution явно unavailable под неизменным combined RPC.
       3. Receipt называет `published_basis`, exact `run_head`, harness commit/manifest,
          Unity slot, artifact/run id, clean status before/after и serializer delegates
          proven present; runnable checks доказывают неизменность RPC/host Apply/
          observers/recipients/gameplay, diagnostic-only abort, stats restore на
          completion/abort/server stop, inactive-path zero work/allocations и отсутствие
          B1/item-state, с честным списком remaining gaps.
     return: |
       Полный product RESULT HOME: `published_basis` + exact `run_head`, harness
       commit/manifest, raw counters и все три строго названных byte/packet слоя,
       monotonic/tick/recipient evidence, Unity slot + artifact/run id, clean-tree
       status before/after, выполненные runnable checks, assumptions/cuts и честные gaps.
     budget: one focused session after unblock

     END_OF_FILE: live/indie-game-development/work/c-exec-g-5a7c-cargo-delta-1-002-call.md

  2. Через `osctl card set` и `osctl card block` изменить только
     `c-exec-g-5a7c-cargo-delta-1-002`:
     - description =
       `B0 runtime receipt: exact cargo serialization + aggregate per-peer datagrams после освобождения слота`
     - note block =

       Только B0 runtime measurement. Published basis остаётся
       `97ca2c98485f158d3367103b202000481e1e74d7`; после освобождения слота разрешён
       минимальный committed measurement-harness `run_head` с exact basis как единственным
       parent.

       Receipt разделяет exact FishNet bytes полного `CargoSnapshot[]`,
       `counterfactual_delta_v1` (`staged CargoSnapshot[] + removed int[]`) и aggregate
       per-peer LiteNetLib datagram-payload. Cargo-only UDP attribution недоступна под
       неизменным combined RPC; aggregate нельзя называть cargo.

       Normal RPC/host Apply/observers/recipients/gameplay не меняются. B1, sparse
       delivery и item-state эта нога не реализует.

       B1 остаётся только pose/hold и ждёт B0 runtime, интегрированные
       `c-exec-g-5a7c-cargo-sleep-repair-1-002` +
       `c-exec-g-5a7c-beam-1-001` и закрытую `t-cargo-state-lifecycle-1`.
       Global gameplay-state принадлежит
       `c-exec-g-5a7c-cargo-state-lifecycle-1-001` и не входит в room-interest scope.

     Сохранить без изменений id/_kind/_bet/status=`blocked`/to/for/play/issued/call/repo/
     engineering_contract/unblock_when/_pos и существующий журнал.

  3. Одним `osctl leg close` сохранить этот полный RESULT в
     `history/2026-08-20-s-repair-g-5a7c-cargo-delta-b0-contract-001.md`
     и добавить одну log-строку только в журнал
     `c-exec-g-5a7c-cargo-delta-1-002`.

  4. Не менять NOW, CHARTER, bet/node/task, B1/lifecycle/Repair A/beam, другие CALL/status/
     slot, issues, knowledge, owner invariant, screenshot scope, panel, product repo или
     `archive/**`.
captures: []
decisions_needed: []
play_check:
  - 1 Name the contradiction: done — literal cargo-only UDP bytes недоступны внутри combined RPC, а current CALL одновременно требует их и запрещает транспортное изменение/measurement seam.
  - 2 Reconstruct: done — newest-first прочитаны fresh origin/main, current bet/task/call-card/work CALL, B0 checkpoint, state-lane/provenance repairs, actual owner mandate/knowledge и delegated source audit; product implementation не открывалась как write target.
  - 3 Propose corrected state: done — разрешён только direct-child committed measurement harness; exact cargo serialization, counterfactual schema и aggregate per-peer transport разделены; normal delivery и весь соседний scope, включая lifecycle room-interest boundary, сохранены.
  - 4 Confirm (owner): done — изменение находится внутри уже записанных слов «Способ передачи выбирает инженерия», «никаких костылей», «обязательно жёсткая проверка всего», «нужна проверка кода» и «В текущую волну скриншотов реализацию не добавлять»; delegated source audit не выдан за новые слова владельца.
  - 5 Friction: skipped — OS-hole нет; это противоречивый continuation contract, который repair исправляет без изменения правил.
close: repair — product outcome и task done не заявлены; call остаётся blocked, поэтому binding G5/review не имитируется и не открывается.
log: B0 continuation исправлен — direct-child measurement harness разрешён, cargo serialization отделена от aggregate per-peer datagrams, cargo-only UDP признана недоступной
next: |
  return-to-owner; writer применяет/проверяет/коммитит/push-ит этот repair.
  `c-exec-g-5a7c-cargo-delta-1-002` остаётся blocked до освобождения Unity-слота;
  никакой существующий ready/running/blocked CALL этой ногой не запускается.
END_OF_FILE: live/indie-game-development/history/2026-08-20-s-repair-g-5a7c-cargo-delta-b0-contract-001.md
