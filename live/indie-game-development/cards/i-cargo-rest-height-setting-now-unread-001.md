---
id: i-cargo-rest-height-setting-now-unread-001
_kind: issue
level: execution
route: work
_pos: 41
---

## issue
`_cargoRestHeight: 0.02` по-прежнему стоит в `NetworkPlaySettings.asset` и едет в `CargoRules.CargoRestHeight`, но после `t-scale-7` его НЕ ЧИТАЕТ НИКТО: центр спавна теперь выводится из `class.Height / 2`. Поиск `.CargoRestHeight` по `Assets/**` пуст. Настройка выглядит живой ручкой и ею не является: нога, которая завтра будет крутить «на какой высоте лежит груз», поменяет число и не увидит ничего. Сегодня оба источника дают одно и то же `0.02`, поэтому поведение не расходится — расхождение появится вместе с первым классом другой высоты.
## review_when
В первой же задаче, трогающей спавн груза или сам файл настроек: либо поле и свойство удаляются, либо `_cargoRestHeight` снова становится источником и класс на него не влияет. Дёшево в обе стороны; опасна только видимость живой ручки. Закрывается вместе с этой правкой.
## evidence
Перемерено первой рукой 2026-08-10 на опубликованной голове `43648b2d`: база `918600ba` брала `_cargoRestHeight` третьим аргументом `CreateCargoSpawnState`, HEAD берёт `cargoClass.CenterYOnFloor`; `grep -rn "\.CargoRestHeight" Assets/ --include=*.cs` пуст; `_cargoRestHeight: 0.02` и `_height: 0.04` класса `standard-cargo` дают одно и то же число.
END_OF_FILE: live/indie-game-development/cards/i-cargo-rest-height-setting-now-unread-001.md
