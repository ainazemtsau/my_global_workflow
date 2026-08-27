---
id: c-exec-g-5a7c-cargo-state-lifecycle-1-001
_kind: call
_bet: bet-g-5a7c-wave-5
status: parked
to: executor
for: t-cargo-state-lifecycle-1
play: work
issued: 2026-08-20
call: work/2026-08-20-call-cargo-state-lifecycle-1.md
repo: C:\projects\Unity\GasCoopGame_dev
engineering_contract: 36
description: Глобальный item-state lifecycle/consumer отдельно от sparse pose/hold
unblock_when: B0 runtime принят; repair A и beam интегрированы на одной fresh product
  main; слот заранее не резервировать
_pos: 110
---

## note
Не screenshot task и не ready work. После unblock инженерия выбирает transport HOW,
но сохраняет global delivery, ordered lifecycle/catch-up, end-tick без per-tick dirty
и удаляет мёртвые wire-поля. B1 ждёт закрытия `t-cargo-state-lifecycle-1`.
## журнал
2026-08-20 · B1 отделена от глобального gameplay-state — pose/hold остаётся sparse, lifecycle вынесен в отдельную blocked-задачу перед B1, мёртвые wire-поля не резервируются · history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md
END_OF_FILE: live/indie-game-development/cards/c-exec-g-5a7c-cargo-state-lifecycle-1-001.md
