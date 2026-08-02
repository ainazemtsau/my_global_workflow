# s-writer-g-6b13-a1b-close-001

session: writer
direction: indie-game-development
node: g-6b13
task: a-1b
track: переноска
date: 2026-08-02

## Что закрыто

Задача `a-1b` — «Один игрок ходит, и правило движения лежит в слое правил. Сети нет вообще.»

Закрытие стоит на слове владельца, а не на продуктовом RESULT. Продуктовый RESULT
принят как УЛИКА по правилу AGENTS.md: builder/executor handback и product RESULT
не являются закрытием в Direction OS.

## Вердикт владельца

Он выполнил Play/Game/WASD в Local `WIN-U3` и ответил дословно **«ходит»**.
Записано в `docs/measurements/c-exec-rules-layer-and-single-walker-001-owner-eye.md`,
статус PASS, с явной пометкой, что автоматической проверки сцены/объекта/видимого
движения взамен не заводилось (`knowledge/no-checks-the-owner-makes-by-eye.md`).

## Перепроверка первой рукой в этой сессии

Сессия отдельная от сборки. Проверены все три части `done_when`.

| Часть done_when | Как проверено | Результат |
|---|---|---|
| Жмёшь играть один — человечек ходит | глаз владельца, вне чата сборки | «ходит» |
| Правило даёт результат при вызове ВНЕ Unity | свой прогон `dotnet test tests/TunnelCrew.Core.Tests` | 4 обнаружено, 4 пройдено, 0 упало, 8 ms, `net8.0`, Unity в контуре нет |
| Слой правил заведён, в нём лежит настоящее правило | чтение `Assets/TunnelCrew/Core/` | `*.asmdef` несёт `noEngineReferences: true`; внутри `MovementInput.cs`, `PlayerMovement.cs`, `PlayerMovement.Rule.cs`, `PlayerState.cs` |

Дополнительно проверено первой рукой:

- `origin/main` = `cbc0334c1174f7837d299a68ad80c8a8d8ef6f47` — опубликовано.
- `docs/reviews/review-c-exec-rules-layer-and-single-walker-001.md` присутствует в дереве HEAD.
- `docs/adr/ADR-E-0019-...-engine-free-rules-and-courier-boundary.md` присутствует в дереве HEAD.

## Закрытый долг предыдущей задачи

Открытый факт задачи `a-1` — «в `Core` ноль `.cs`, а `EnableDefaultCompileItems=false`
с одним glob-ом, значит focused build это сборка пустоты и доказательством не является» —
умер, как и было записано при его внесении: в `Core` теперь четыре живых файла и настоящий
прогон тестов. Сторожа на это не заводилось.

## G5

Закрыт собственной проверкой владельца, сделанной его руками вне чата сборки и вне этого
чата — тот же маршрут, которым закрылась `a-1`.

## Состояние слота

`WIN-U3`: CLEAN / AVAILABLE, lease none, selector `CLAIMED → AVAILABLE`,
фиксированная ветка `slot/win-u3@cbc0334c`.

## Что разблокировано

- Задача `b-1` (сцена хозяина): `blocked` → `open`. Её `unblock_when` требовал закрытия
  `a-1b` после Play владельца — условие выполнено.
- Наряд `c-work-host-walker-frontier-001`: `blocked` → `ready`.
- Открыта вторая полоса при `track_wip_limit: 2`.

Следующие законные шаги — `a-2` (двое по сети; приёмка усилена его словом: правило
движения из `a-1b` не меняется ни строкой) и `b-1` (сцена хозяина).

`a-4` и `b-2` остаются закрытыми архитектурным разбором, который владелец не подписывал.

## Отмечено честно

В этой же сессии инженерный контур переведён на контракт v36: режим ПРОБА стал режимом
по умолчанию, тяжёлый режим ОПОРА включается только явным словом владельца. Поэтому `a-1b` —
последняя нога, прошедшая полный тяжёлый круг. Дальнейшие задачи по умолчанию идут лёгким
маршрутом, и решение «это остаётся, закрепляем» принимает владелец в конце ноги.

## Полный продуктовый RESULT (улика)

```
# RESULT — c-exec-rules-layer-and-single-walker-001

Status: DELIVERED on `dev`

Outcome: The first TunnelCrew product slice is built in three layers. The engine-free
`TunnelCrew.Core` rule receives a player state plus finite movement input and returns the
next state. The Unity world reads WASD, invokes that rule, and applies only the returned
X/Z to a primitive Walker in `SingleWalker.unity`. No courier/network layer exists in this
task. The initial finite-axis normalization defect and its first unit-boundary correction
defect are closed by widened double norm arithmetic. Three owner-authorized ordinary NUnit
regressions retain both failure regimes while the original frozen literal test remains
byte-identical.

Evidence:
- Final rule implementation: 8006cb91a4325411526cc14d20785498e766c663
- Numeric regression tests: 45f9bee749b38f984db5224ec1e5569801f6051d
- Fresh validation and review receipt: 0aac411db448a89f054113b43309fbfd3f1471d2
- Permanent owner-authorized PowerShell launcher repair: b3c6cb38ab2c3affabd32d46431269021fe7314b
- Current-product review/staged guard repair: 511e87e6849454c0f0bcf5c0b249746b506ad168
- Fresh Release build: 0 warnings, 0 errors in 1.3 s
- Fresh headless test run: 4 discovered, 4 passed, 0 failed/skipped in 2.1 s
- Unity ForceSynchronousImport green in 5.7287 s; recent Unity Error log empty
- Post-launcher-fix routine tools/check.ps1 green in 7.9 s and again in 8.8 s; no legacy/full suite
- Independent final review: no Critical, Important, or Minor findings
- Layering rationale: docs/adr/ADR-E-0019-...

Assumptions:
- The visible movement claim is discharged by the owner's exact `ходит` verdict.
- The current host-owned multiplayer rule remains unchanged: a future host/judge invokes this
  engine-free rule and a future courier distributes results. Networking is not silently
  implemented here.
- The owner explicitly authorized any number of added tests without repeating formal pair
  stages, and separately authorized the permanent repository-wide pwsh.cmd repair.

Cuts: no FishNet, NetworkBehaviour, connection flow, replication, lobby, settings, Canvas,
OnGUI, animation, physics movement rule, collision, gamepad binding, rebinding, custom shader,
renderer feature, or visual polish. No automated scene/object/presence or visible-movement
checker was added. No legacy Assets/GasCoopGame/** or tests/GasCoopGame.Core.Tests/** behavior
was changed or validated.

Cost: one v35 pair/freeze/build route, one BUILD retry for the finite normalization failure
class, three small numeric regressions, fresh validation/review, one two-file repository
launcher repair, one five-file current-product gate-root repair with black-box regressions.

Manual-acceptance: PASS. In Local WIN-U3 the owner ran the requested Play/Game/WASD check and
replied exactly `ходит` on 2026-08-02. No automated substitute was used.

Closing state: dev = cbc0334c; published main/origin/main = cbc0334c; remote readback exact
match; origin/dev deliberately unchanged at 8a346c6f; Deliver GREEN; RELEASED receipt
d87f73cd; WIN-U3 CLEAN/AVAILABLE; lease none; selector CLAIMED → AVAILABLE.
Legacy/full suite not run.
```

END_OF_FILE: live/indie-game-development/history/2026-08-02-s-writer-g-6b13-a1b-close-001.md
