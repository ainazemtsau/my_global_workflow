# CALL — c-work-a3-close-verification-001

to: session
direction: indie-game-development
track: переноска
play: work
node: g-6b13
task: a-3
status: ready

## goal

Независимо установить, выдерживает ли результат «один носильщик берёт, несёт и кладёт груз»
попытку опровержения и можно ли закрыть эту задачу в Direction OS.

## context

- `live/indie-game-development/NOW.md`, задача `a-3` и её обязательная форма.
- Исходный инженерный наряд:
  `live/indie-game-development/work/c-exec-one-carries-cargo-proba-001-call.md`.
- Продуктовый репозиторий: `C:/projects/Unity/GasCoopGame_dev`; проверенный опубликованный tip
  `origin/main = origin/dev = dev = 8219f6c0bdc5e28d29353b2b29ed08932dc7253d`.
- Продуктовый отчёт:
  `docs/results/c-exec-one-carries-cargo-proba-001.md` на опубликованном tip.
- Exact-history: basis `cca530a0`; candidate `22d55e775e1e606811c3dea50118d776ee2d8e6a`;
  отчёт `e469eeae`; отдельная owner-directed установка Multiplayer Play Mode `a8ddb891`;
  handoff-fix `4ba8d0f1`; Control lease `2e9116fa`; merge `8ca106a9`; delivered marker
  `2c51ab2c`; terminal release `8219f6c0`.
- Дословная приёмка владельца: «работает»; «Так всё работает. Я одним поднял, вторым, который
  подключился, видно, что другой таскает, в новом месте остаётся. Как бы я никаких проблем не
  обнаружил.»
- Терминальный селектор 2026-08-03: WIN-U3, head `8219f6c0`, `CLEAN`, `AVAILABLE`, lease `none`.

## boundaries

- Только read-only проверка и Direction-close задачи a-3. Ничего не писать в продуктовый репозиторий.
- Не решать схему двух держателей, не строить a-4 и не выпускать инженерный наряд на неё.
- Не считать product RESULT, owner-eye, merge, зелёные проверки или свободный слот по отдельности
  достаточным закрытием; проверить их связь с каждым пунктом исходного `done_when`.
- Отдельный коммит Multiplayer Play Mode не приписывать задаче a-3; проверить, что он действительно
  отделён и что утверждение о слове владельца не подменено пересказом.

## done_when

Каждая часть a-3 получила exact evidence и выдержала попытку опровержения: владелец в двух окнах
взял, перенёс и положил груз; обе копии показывали одно место; судья владеет решением; груз —
самостоятельный объект без родительства; поза считается вне Unity из списка держателей длины один;
обязательные поля формы присутствуют без поведения для двух держателей; три заявленных теста,
сборка и routine check зелёные; четыре блоба движения не изменены; кандидат сохранён в
опубликованной exact-history; WIN-U3 терминально освобождён.

PASS оформлен полным Direction RESULT: закрыть a-3, убрать этот CALL и открыть в той же полосе
owner-present отдельный архитектурный разбор a-4. Любой разрыв даёт FAIL/checkpoint с одним точным
пробелом и продолжением той же задачи, без запуска a-4.

## return

Полный RESULT по play `work`: verdict PASS либо точный FAIL, доказательства по каждому пункту,
state_changes только для a-3/этого CALL и законный same-lane handoff.

budget: one fresh physical session

END_OF_FILE: live/indie-game-development/work/c-work-a3-close-verification-001-call.md
