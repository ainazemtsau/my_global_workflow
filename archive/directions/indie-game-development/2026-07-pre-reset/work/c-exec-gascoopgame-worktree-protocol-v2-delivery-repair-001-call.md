# CALL c-exec-gascoopgame-worktree-protocol-v2-delivery-repair-001

to: executor
direction: indie-game-development
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: worktree-protocol-v2-delivery-repair
issued: 2026-07-16 (s-work-gascoopgame-worktree-protocol-v2-blocker-a-001)
parent: s-work-gascoopgame-worktree-protocol-v2-blocker-a-001

goal: |
  GasCoopGame worktree protocol v2 честно доставлен по current product authority: два guarded folder-meta
  конфликта получили repository-correct disposition, fresh-leg preservation доказана, closing gates зелёные,
  а поведение игры и весь unrelated WIP не изменились.

context: |
  Владелец выбрал вариант A точным ответом `A`. Это разрешает один bounded repair и означает: историческую
  start-of-task byte identity первой попытки восстановить невозможно; новая попытка доказывает сохранность только
  от собственной fresh current-state базы. Owner ack: `owner-2026-07-16-worktree-protocol-repair-a`.

  Current OS и product contract = v26. Product implementation и BLOCKED report сохранены в
  `docs/results/c-exec-gascoopgame-worktree-protocol-v2-001.md`; Direction context —
  `live/indie-game-development/work/gascoopgame-worktree-protocol-v2.md`. Historical evidence candidate
  `767a8f8ff2de439a64c59d2e7a8b8bbc6a198fd0` не является base/branch/venue pin: executor заново обнаруживает
  current repo state и следует root AGENTS + canonical registry.

  Известный узкий conflict surface: `Assets/GasCoopGame/Characters.meta` и
  `Assets/GasCoopGame/Core/Field/NearGas.meta`. Предыдущий live integrated-state Deliver прошёл build,
  1714/1714 tests, hygiene и scans, затем остановился на DF-5 из-за этих двух untracked файлов. Clean exact-commit
  checkout не заменяет required closing state.

boundaries: |
  Разрешён только repository-correct disposition двух названных folder-meta conflicts и минимальные product-owned
  registry/result/dashboard evidence edits, необходимые для честного handback. Не менять game source, tests, scenes,
  packages, gameplay assets или поведение; не начинать characters, Dungeon Architect или NearGas L1B work.
  Не трогать WIP/refs/worktrees вне fresh registered venue; не делать broad cleanup/preservation project и не
  реконструировать historical manifests. Не ослаблять DF-5 или другие gates; запрещены exclude, stash, temporary
  remove/restore и clean-checkout подмена. Не выбирать GUID произвольно: если repository-correct disposition нельзя
  доказать в этом scope, STOP/BLOCKED. Любой второй blocker class или потребность в новой topology/policy = STOP.

done_when: |
  1. Current product authority содержит committed, доказуемо корректный disposition ровно двух folder-meta conflicts;
     под guarded roots не осталось связанного untracked blocker, arbitrary GUID choice отсутствует.
  2. Fresh first-hand start/end evidence этой новой leg доказывает, что все остальные legacy worktrees/WIP, единственный
     Editor, product behavior/source/tests, L1a score/artifacts и remote refs не изменились; historical first-attempt
     gap явно назван owner-accepted non-evidence, а не восстановленным proof.
  3. Committed delta ограничена двумя conflict metas и минимальными protocol registry/dashboard/RESULT evidence;
     committed pre-write admission и serial registry/integration lifecycle соблюдены по current product authority.
  4. Repo-native result-check, diff/hygiene и полный closing `tools/check.ps1 -Deliver` на required integrated state
     GREEN без Stryker, bypass или clean-checkout substitution; все прежние protocol P1 class+sweep closures сохранены.
  5. Product RESULT правдиво фиксирует DELIVERED, exact commits/diff/check outputs/preservation hashes и repo-local
     integration/publication readback, если current product delivery contract их требует. До всех GREEN ничего не
     интегрируется и не публикуется; невозможность безопасного close возвращается точным BLOCKED, без импровизации.

return: |
  Product RESULT HOME: final status; fresh base/final commits; exact diff; meta disposition evidence; complete
  start/end preservation manifest identities; admission lifecycle; check/Deliver outputs; integration/push/readback;
  explicit confirmation that characters/DA/L1B, unrelated WIP, Unity behavior and L1a score were untouched.

budget: one focused half-day maximum; stop on scope growth or a second blocker class
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-gascoopgame-worktree-protocol-v2-delivery-repair-001-call.md
