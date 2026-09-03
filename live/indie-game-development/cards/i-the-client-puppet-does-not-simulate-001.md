---
id: i-the-client-puppet-does-not-simulate-001
_kind: issue
level: execution
route: shape
status: open
evidence: history/2026-09-03-s-review-g-5a7c-wave-11-close-001.md
_pos: 222
---

## issue
**КЛИЕНТСКАЯ КУКЛА НИЧЕГО НЕ СЧИТАЕТ — ОНА РИСУЕТ ПОЛУЧЕННОЕ. ПЛАН ОПИСЫВАЕТ ДРУГОЕ.**

Замерено review 2026-09-03 по байтам, `Presentation/HouseholderBalanceBody.cs`, метод
`SetAuthority(bool authority)`:

```
_behaviour.collisionLayers = authority ? _authorityCollisionLayers : 0;
_behaviour.groundLayers    = authority ? _authorityGroundLayers    : 0;
if (!authority) { _behaviour.SetState(BehaviourPuppet.State.Puppet);
                  _puppetMaster.mode = PuppetMaster.Mode.Kinematic; }
```

То есть на неавторитетной копии кукла **кинематическая с пустыми масками столкновений**. По
проводу идут `BalancePhase` плюс **поза корня** — `BalanceOffsetX/Y/Z` и `BalanceTiltX/Y/Z/W`, —
и `NetworkHouseholder.Show` зовёт `ShowReceivedBalance(...)`.

**ЧТО ГОВОРИТ ПЛАН.** Решение Р2: «Каждая копия крутит свою куклу от того же импульса и сходится к
исходу хоста». Построено не это. Построено «хост считает, клиент рисует полученную позу корня».

**ГДЕ ЭТО ЧЕСТНО И ГДЕ ЛОМАЕТСЯ.** Для окна равновесия (наклон до 35°) позы корня достаточно, и
приёмка это выдержит. **Для полного падения — нет:** поза корня не выражает раскинутых конечностей,
и на клиенте выйдет наклонённая целиком фигура в позе ходьбы. Для вылета из пушки (Д6) — тем более.

**СЛЕДСТВИЕ, КОТОРОЕ НУЖНО РЕШИТЬ ЕГО СЛОВОМ, А НЕ ПО ФАКТУ РАСХОЖДЕНИЯ.** Запасной путь плана
(«хост шлёт корень и шесть ключевых костей с малой частотой») — не запасной, а **основной** для
полного падения. Сам план говорит, что этот путь есть исключение из его правила и требует его
слова. Значит слово нужно **до Р3**, а не после первого расхождения на четырёх экранах.

Второй вариант — включить клиенту куклу и мирить исходом — упирается в
`i-one-field-carries-the-only-stepped-puppet-001`.
END_OF_FILE: live/indie-game-development/cards/i-the-client-puppet-does-not-simulate-001.md
