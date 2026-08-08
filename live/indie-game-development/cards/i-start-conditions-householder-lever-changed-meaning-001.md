---
id: i-start-conditions-householder-lever-changed-meaning-001
_kind: issue
_pos: 25
level: execution
route: work
---

## issue
РЫЧАГ ПАНЕЛИ СТАРТОВЫХ УСЛОВИЙ «где хозяин», доставленный закрытой `t-scene-3`, сменил смысл: маршрут больше не принадлежит корню хозяина, он принадлежит дому. Сдвинув корень, вы теперь задаёте только ТОЧКУ СТАРТА — оттуда он законным путём идёт к первому названному месту (`HouseholderSurroundings.StartPoint`). Поведение по умолчанию не изменилось: при нетронутой сцене тело стоит ровно в `Bedside`. Подсказки в `StartConditions` и её редакторе переписаны честно.

## review_when
Когда владелец в следующий раз собирает условия своей рукой, либо при наряде `t-scene-4` (собранный exe), либо при первом же наряде, открывающем `StartConditions`. Закрывается его словом, что рычаг в новом смысле его устраивает, либо возвратом прежнего смысла.

## evidence
`f03b1468:docs/results/c-exec-g-1d84-named-house-routes-001.md` §Cuts и §Manual-acceptance пункт 6 (единственный пункт приёмки, который он перечислением не подтверждал); `f03b1468:Assets/TunnelCrew/World/StartConditions.cs`, `Assets/TunnelCrew/Editor/StartConditionsEditor.cs` — оба в манифесте доставки.

END_OF_FILE: live/indie-game-development/cards/i-start-conditions-householder-lever-changed-meaning-001.md
