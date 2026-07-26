# Start here — PuppetMaster P2a0

status: READY; owner chose A on 2026-07-11

## Короткий ответ

Да, пригодность PuppetMaster для нашей сетевой игры надо проверить заранее. Но это не ещё один большой бумажный
research: первичные ограничения уже найдены, а следующий правильный шаг — короткий lab-эксперимент, который проверяет
root authority и превращает результат в сетевую матрицу A/B/C.

Физическая кукла не становится частью integer-lockstep газа. Для игрока нужен отдельный host/server-authority маршрут:
либо gameplay-root всегда остаётся у контроллера, либо на падении временно переходит pelvis/puppet, либо весь locomotion
становится физическим. Независимо симулировать ragdoll на каждом пире и считать это общей истиной нельзя.

## Что workflow сделает сам

1. Проверит отдельный lab-worktree, Unity/MCP, версию и лицензию PuppetMaster, assembly и collision-layer ограничения.
2. Соберёт бросовый humanoid-стенд: ходьба, камень/импульс, падение, подъём.
3. Сравнит A: controller-root всегда, B: controller→pelvis→controller, C: full active-ragdoll kill-probe.
4. Для каждого варианта запишет, что является сетевой истиной, что можно считать локально и что придётся исправлять.
5. Свежая независимая сессия попробует опровергнуть вывод; затем владелец получит два коротких клипа и рекомендацию.

## Как запустить — одно действие

Открыть новую Codex task на C:\projects\Unity\GasCoopGame и отправить одну строку:

Запусти CALL c-exec-player-puppetmaster-p2a0-001 из C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-exec-player-puppetmaster-p2a0-001-call.md. Сам веди workflow; спрашивай меня только если нужен Unity/Asset Store или финальный verdict.

Если task остановится на Unity/Asset Store, она обязана дать одну точную пошаговую инструкцию. Не надо заранее читать
CALL или вручную готовить сцену. После spike от владельца нужен только короткий A/B/C verdict; production-код до него
не начинается.

## Бюджет и место в M1

P2a0 — risk-first opening уже существующего M1-5 player-tracking leg. Он не добавляет 14-й leg. M1-GAS-PROBE временно
выведен из трёхслотового окна и вернётся после Phase 0 + checksum foundation + successor A0. Если setup съедает
полудня или ни один вариант не переживает multiplayer-ограничения, правильный результат — ранний checkpoint/kill.

END_OF_FILE: live/indie-game-development/work/player-puppetmaster-p2a0-start-2026-07-11.md
