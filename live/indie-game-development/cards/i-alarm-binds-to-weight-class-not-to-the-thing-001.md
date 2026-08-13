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
2026-08-13 · ДЕФЕКТ НЕ БУДУЩИЙ, А ЖИВОЙ ПРЯМО СЕЙЧАС, и это перемерено Направлением лично: в опубликованной сцене IntegratedHouse.unity на origin/main = c485b30e у четырёх точек появления _cargoClassId равен 0, 0, 2, 1 (строки 166, 323, 722, 880), а будильник привязан к классу 0 — значит в игре СЕГОДНЯ звонят ДВА груза из четырёх, а не один; прежняя запись говорила про пять будильников как про последствие замороженного кандидата с десятью предметами, то есть как про будущее — на деле удвоение уже произошло и владелец может увидеть его своим прогоном без всякого лута; это усиливает срочность привязки поведения к определению и снимает возможное возражение «пока предметов мало, проблемы нет» · history/2026-08-13-s-repair-g-5a7c-loot-architecture-review-006.md
2026-08-13 · владелец выбрал один полный первый BUILD лута вместо split/cut; точный handoff сохранён, старый candidate оставлен PRESERVED-PAUSED, выпущен отдельный child CALL от свежего origin/main со stable IDs, physical supports, network/visual/behavior seams и stale-contact fix · history/2026-08-13-s-work-g-5a7c-loot-foundation-dispatch-001.md
END_OF_FILE: live/indie-game-development/cards/i-alarm-binds-to-weight-class-not-to-the-thing-001.md
