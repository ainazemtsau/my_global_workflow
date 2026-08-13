---
id: i-alarm-binds-to-weight-class-not-to-the-thing-001
_kind: issue
level: execution
route: work
status: open
_pos: 86
---

## issue
На опубликованной сцене runtime-порядок классов уже `0,0,1,2`, а Host инициализирует alarm rule по
class id для каждого cargo; поэтому behavior вещи выведен из физического параметра и случайно
наследуется несколькими экземплярами, а preserve-раскладка увеличила бы их до пяти. Новый
owner-handoff требует stable definition-based dispatch, а не прежний class selector.
## review_when
`c-exec-g-5a7c-loot-foundation-001`: только явно выбранное alarm definition получает stable
`BehaviorId`, остальные definitions нейтральны независимо от массы; прежние states/timing/event path
сохраняются. Закрыть после публикации миграции и regressions.
## evidence
`c485b30e`: `IntegratedHouse.unity` + `GameRulesSettings.CreateCargoSpawnState` /
`AlarmClockCargoThing.InitialStateFor`; `work/2026-08-13-loot-owner-architecture-handoff.md`;
`origin/main:docs/results/c-exec-g-5a7c-loot-1-001.md`.
## журнал
2026-08-13 · владелец выбрал один полный первый BUILD лута вместо split/cut; точный handoff сохранён, старый candidate оставлен PRESERVED-PAUSED, выпущен отдельный child CALL от свежего origin/main со stable IDs, physical supports, network/visual/behavior seams и stale-contact fix · history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
END_OF_FILE: live/indie-game-development/cards/i-alarm-binds-to-weight-class-not-to-the-thing-001.md
