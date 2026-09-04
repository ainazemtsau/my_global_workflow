---
id: c-exec-g-5a7c-cargo-delta-1-002
_kind: call
_bet: bet-g-5a7c-wave-5
status: dropped
to: executor
for: t-cargo-delta-1
play: work
issued: 2026-08-20
call: work/c-exec-g-5a7c-cargo-delta-1-002-call.md
repo: C:\projects\Unity\GasCoopGame_dev
engineering_contract: legacy:c-exec-g-5a7c-cargo-delta-1-001
description: 'B0 runtime receipt: exact cargo serialization + aggregate per-peer datagrams
  после освобождения слота'
unblock_when: скриншотная волна освободила Unity-слот; до подтверждения слот не резервировать
  и Unity не запускать
_pos: 108
---

## note
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
## журнал
2026-08-30 · ЗАКРЫТ ЗАКРЫТИЕМ ВОСЬМОЙ ВОЛНЫ. Стоял статусом parked, которого у наряда в схеме нет (ready|running|waiting|blocked|paused), а законный paused требует paused_by со словом владельца — слова нет. Его ставка, пятая волна, закрыта 2026-08-27, то есть открытый наряд на закрытой ставке это дрейф по G2. Содержание держит живая улика i-all-cargo-travels-every-tick-001; текст наряда цел в work/ · history/2026-08-30-s-review-g-5a7c-wave-8-close-001.md
2026-08-20 · B0 continuation исправлен — direct-child measurement harness разрешён, cargo serialization отделена от aggregate per-peer datagrams, cargo-only UDP признана недоступной · history/2026-08-20-s-repair-g-5a7c-cargo-delta-b0-contract-001.md
2026-08-20 · B1 отделена от глобального gameplay-state — pose/hold остаётся sparse, lifecycle вынесен в отдельную blocked-задачу перед B1, мёртвые wire-поля не резервируются · history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md
2026-08-20 · B0 опубликована как code/control checkpoint без изменения доставки; live counter/bytes и 60 секунд покоя остаются, continuation ждёт Unity-слот · history/2026-08-20-s-work-g-5a7c-cargo-delta-b0-checkpoint-001.md
END_OF_FILE: live/indie-game-development/cards/closed/c-exec-g-5a7c-cargo-delta-1-002.md
