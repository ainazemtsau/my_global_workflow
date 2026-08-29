---
id: i-house-plan-in-the-game-has-no-furniture-001
_kind: issue
level: execution
route: work
status: open
evidence: work/2026-08-29-research-householder-plan-architecture.md
_pos: 153
---

## issue
**В СОБРАННОЙ ИГРЕ ХОЗЯИН ХОДИТ СКВОЗЬ ВСЮ МЕБЕЛЬ, И ДВА ДЕФЕКТА МАСКИРУЮТ ДРУГ ДРУГА.**

Перемерено первой рукой на `68c4e933`, перепроверено на `782349bd` (эти файлы между ними не менялись).

1. `Assets/TunnelCrew/World/SceneHousePlan.cs:63` — `return new HousePlan(name, rooms, places, passages);`
   Это **четырёхаргументный** конструктор; он передаёт `furnishings: null`. **У дома, который видит
   хозяин в игре, НОЛЬ предметов обстановки** — при 59 авторских в `first-house.house.json`.
2. `HouseholderWalkTuning.WithBody(...)` имеет во всём репозитории **ровно одного вызывающего, и это
   ТЕСТ** (`tests/TunnelCrew.Core.Tests/HouseWalkAroundFurnitureTests.cs:518`). Боевой конструктор
   подставляет `WalkingBody.Unstated` (`HouseholderWalkTuning.cs:408`). **Тело хозяина не объявлено.**

**Они скрывают друг друга.** `HouseWalk.cs:259`:
`if (house.Furnishings.Count > 0 && !body.IsStated) return NoWay(..., BodyUnstated);`
Мебели ноль → отказ не срабатывает → ходьба «работает». Сквозь мебель.

**Цена.** Весь слой обхода мебели — `HouseWays` (477 строк), `HouseGap` целиком, препятствия, углы,
обход — **в запущенной игре не исполняется ни разу**. Он живёт только в тестах.

**ЭТО ЛОВУШКА ДЛЯ СЛЕДУЮЩЕЙ НОГИ, И ПОЭТОМУ УЛИКА ЗАВЕДЕНА СЕГОДНЯ.** Любой из четырёх способов
построить план хозяина требует, чтобы дом рассказал про обстановку. В тот день, когда `SceneHousePlan`
начнёт отдавать `furnishings`, второй дефект перестанет быть скрытым: `HouseWalk` начнёт отказывать
**КАЖДОМУ** пути с `BodyUnstated`, `AdvanceAlong` будет вечно возвращать «не дошёл», и хозяин
**встанет намертво**. Ни один поступок больше не проставится — ни по делу, ни по шуму.

Это НЕ та же улика, что `i-householder-walks-through-walls-001`: та про край капсулы в проёме, эта про
то, что мебели в его карте нет вообще.
## fix_when
**Первым шагом восьмой волны, до любой работы по §6 и по плану хозяина.** Две строки: пятый аргумент
в `SceneHousePlan.cs:63` и объявленное тело в боевом тюнинге. Обе правки обязаны приехать вместе —
поодиночке первая роняет хозяина, а вторая ничего не чинит.
END_OF_FILE: live/indie-game-development/cards/i-house-plan-in-the-game-has-no-furniture-001.md
