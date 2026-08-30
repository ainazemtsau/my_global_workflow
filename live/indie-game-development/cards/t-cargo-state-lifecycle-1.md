---
id: t-cargo-state-lifecycle-1
_kind: task
_bet: g-5a7c
status: open
goal: Каждый клиент наблюдает gameplay-state предмета через отдельный от pose/hold
  lifecycle
_pos: 92
---

## done_when
1. **GLOBAL ORDERED LIFECYCLE И ЖИВОЙ CONSUMER.** Для каждого gameplay-state предмета,
   существующего на выбранной product-базе, сервер выдаёт start/change/end с server tick и
   монотонной per-item sequence/revision; host и remote consumer делают состояние
   видимым/слышимым, duplicate/out-of-order input не воскрешает законченное состояние.
   Late join получает current active state и не проигрывает уже закончившееся.
2. **ВРЕМЯ НЕ ДЕЛАЕТ DIRTY КАЖДЫЙ TICK; STATE ГЛОБАЛЕН.** Конечное состояние несёт
   authoritative end tick под revision, клиент выводит остаток локально. Долгая длительность
   публикуется только на start, настоящем semantic change и end плюс catch-up; room interest
   и pose omission не могут скрыть start/change/end.
3. **МЁРТВОГО WIRE-ЗАДЕЛА НЕТ.** После переноса CargoSnapshot/serializer не содержат
   `Integrity`, `ThingStateId`, `ThingRemainingSeconds`, `Moved` или reserved placeholders без
   клиента-потребителя; внутреннее техническое состояние остаётся серверным. Тесты и
   runnable evidence покрывают host, remote, late join, ordering/end, отсутствие per-tick timer
   traffic, clean build, rollback и свежую binding review.
## note
**ФОНОВАЯ ИНЖЕНЕРИЯ, НЕ SCREENSHOT TASK.** Точные продуктовые слова:
`history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md`; инженерный режим:
`work/2026-08-20-background-cargo-engineering-mandate.md`.

**ЗАВИСИМОСТИ:** B0 runtime + интегрированный repair A + интегрированный beam → эта задача
→ B1 pose/hold → C → D. Никакой Unity-слот заранее не резервируется.

**HOW СВОБОДЕН.** RPC/SyncType/иной транспорт выбирает инженерия; фиксированы только
наблюдаемость каждым клиентом, lifecycle/order/catch-up, отсутствие timer-dirty traffic,
глобальный interest и отсутствие мёртвых wire-полей. Новое игровое содержание не изобретается:
мигрируются только состояния, реально существующие на fresh basis.
## журнал
2026-08-30 · восьмая волна закрыта partial: машина построена и перемерена, а его рук на ней не было ни минуты; и найдено, почему нарезка не видела НИ ОДНОЙ живой задачи — поле _bet несло id волны вместо id цели, выпадали все 28 · history/2026-08-30-s-review-g-5a7c-wave-8-close-001.md
2026-08-20 · B1 отделена от глобального gameplay-state — pose/hold остаётся sparse, lifecycle вынесен в отдельную blocked-задачу перед B1, мёртвые wire-поля не резервируются · history/2026-08-20-s-repair-g-5a7c-cargo-state-lane-001.md
END_OF_FILE: live/indie-game-development/cards/t-cargo-state-lifecycle-1.md
