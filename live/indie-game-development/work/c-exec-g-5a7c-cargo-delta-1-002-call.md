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
