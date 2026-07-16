# CALL c-repair-gascoopgame-worktree-protocol-v2-blocker-001

to: session
direction: indie-game-development
play: work
node: g-9c41
task: worktree-protocol-v2-blocker-disposition
issued: 2026-07-16 (s-work-gascoopgame-worktree-protocol-v2-blocked-001)
parent: s-work-gascoopgame-worktree-protocol-v2-blocked-001

goal: |
  Владелец явно разрешил один узкий безопасный repair, способный честно завершить product protocol delivery,
  либо явно оставил NearGas L1B product launch заблокированным.

context: |
  Product implementation существует на GasCoopGame `dev@767a8f8ff2de439a64c59d2e7a8b8bbc6a198fd0`.
  Committed pre-write admission, registry lifecycle, dated inventory и truthful dashboard установлены. Никаких
  game source/tests/assets/scene/package изменений в committed delta нет; merge/push не выполнялись.

  Closing `tools/check.ps1 -Deliver` на обязательном integrated live `dev` прошёл build, 1714/1714 tests,
  hygiene и scans, затем остановился на DF-5 из-за двух заранее существовавших untracked файлов:
  `Assets/GasCoopGame/Characters.meta` и `Assets/GasCoopGame/Core/Field/NearGas.meta`. Они сохранены byte-identical.
  Clean exact-commit checkout не является допустимой заменой live-dev closing gate. Дополнительно исходная сессия
  сняла по другим dirty legacy worktrees только status/count evidence, но не точные start-of-task content identities;
  ретроактивно доказать их прежнюю byte identity нельзя.

  Владелец отдельно потребовал: characters поставить на паузу; если начинается перепланирование, новый большой
  контекст или preservation project — сразу остановиться и написать; узкий фактический repair допустим.

  Owner-visible options:
  A (recommend): явно разрешить отдельный bounded product repair. Он может исследовать и корректно disposition'ить
  только два guarded `.meta`, сначала зафиксировать fresh current-state preservation baseline, затем повторить
  исходные closing gates. Владелец одновременно признаёт, что историческую start-of-task byte identity первой
  попытки восстановить невозможно; новая попытка доказывает сохранность только от своей fresh базы.
  B: не разрешать product repair; protocol и L1B product launch остаются BLOCKED без обхода DF-5.

boundaries: |
  Эта owner-present сессия ничего не пишет в product repo и не запускает executor. Не выбирать `.meta` здесь;
  не создавать preservation project, новую topology/policy, manifests задним числом или дополнительный review loop;
  не трогать characters, Dungeon Architect, L1B source, legacy WIP, Unity Editor, gates, main или remotes.
  Не предлагать exclude/stash/temporary remove-restore/clean-checkout как способ получить ложный GREEN.

done_when: |
  1. Владелец видит короткое различие между уже установленным protocol implementation и незакрытым delivery gate.
  2. Владелец фактическими словами выбирает A или B; recommendation = A.
  3. При A выпущен ровно один outcome-only executor CALL на bounded meta/current-baseline repair без characters/DA/L1B,
     legacy cleanup или gate weakening. При B downstream product CALL не выпускается.
  4. RESULT сохраняет фактические слова владельца и оставляет L1B-PLAN BLOCKED до отдельного GREEN product close.

return: |
  Owner verdict A/B и ровно один следующий route: bounded repair CALL либо явный сохранённый BLOCKED.

budget: one owner decision; no product work
surface: owner-present

END_OF_FILE: live/indie-game-development/work/c-repair-gascoopgame-worktree-protocol-v2-blocker-001-call.md
