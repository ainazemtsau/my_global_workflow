RESULT s-work-publish-integration-lab-entry-main-001 (call: owner-direct-publish-integration-lab-entry-main-20260720)
direction: indie-game-development
track: program
play: work
node/task: g-9c41/repository-main

outcome: |
  По прямому указанию владельца exact Integration Lab shape snapshot
  `21e3d4947ed511525ca57ff8a74dce593d14365e` опубликован без force в обе authoritative remote refs:
  `origin/main` и `origin/wt/indie-game-development`.

  Обе remote refs до публикации совпадали на `46f694cc1c71fe6997cf63595d2ce387653db127`.
  `21e3d49` был чистым прямым потомком ровно на один коммит, поэтому один atomic fast-forward перенёс
  только принятый RESULT одной постоянной Integration Lab и его готовый read-only purge-audit CALL.
  Merge commit, replay, force, product repository work и изменения текущего маршрута не потребовались.

evidence: |
  - Owner instruction: «Запушь и залей в main изменения».
  - Fresh preflight after `git fetch origin`:
      local HEAD = `21e3d4947ed511525ca57ff8a74dce593d14365e`;
      origin/main = `46f694cc1c71fe6997cf63595d2ce387653db127`;
      origin/wt/indie-game-development = `46f694cc1c71fe6997cf63595d2ce387653db127`;
      worktree clean; both remote refs are ancestors of local HEAD;
      range count `46f694c..21e3d49` = 1.
  - Atomic non-force push output:
      `46f694c..21e3d49  HEAD -> main`;
      `46f694c..21e3d49  HEAD -> wt/indie-game-development`.
  - Independent `git ls-remote` readback returned exact
    `21e3d4947ed511525ca57ff8a74dce593d14365e` for both refs.
  - Current `NOW.next` remains ready `c-audit-program-v2-legacy-lab-surface-001`; its complete artifact
    remains unchanged and product `validation.config` is stamped contract 31, matching the CALL pin.

state_changes: |
  live/indie-game-development/history/2026-07-20-s-work-publish-integration-lab-entry-main-001.md:
    - SAVE this complete RESULT once with its exact END_OF_FILE trailer.
  live/indie-game-development/LOG.md:
    - APPEND the declared publication line once before END_OF_FILE.
  live/indie-game-development/NOW.md, TREE.md, CHARTER.md, knowledge/, dashboard, plans, CALL artifacts,
  product/canon repositories, generated assets, dependencies and versions:
    - NO CHANGE.
  Repository publication receipt:
    - COMMIT only this history receipt and LOG append on top of `21e3d49`.
    - PUSH that receipt commit atomically and without force to `refs/heads/main` and
      `refs/heads/wt/indie-game-development`.
    - VERIFY both remote refs equal the receipt commit by independent exact-ref readback.

captures: []
decisions_needed: []

play_check:
  - "1 Recite: done — publish exactly the accepted Integration Lab shape commit to the worktree remote and main, then preserve the ready audit route."
  - "2 Owner inputs (owner): skipped — repository publication is technical transport, not owner-authored content; scope authority is the owner’s exact instruction «Запушь и залей в main изменения»."
  - "3 Do the work: done — clean one-commit ancestry allowed one atomic non-force fast-forward of both remote refs."
  - "4 Self-check: done — ls-remote returned exact SHA equality for main and wt; local worktree remained clean and NOW/default were unchanged."
  - "5 Close: done — publication receipt only; the existing V31 read-only purge-audit CALL remains ready/default and is returned in full."

log: 2026-07-20 · s-work-publish-integration-lab-entry-main-001 · work/publish · program · g-9c41/repository-main: owner-requested Integration Lab shape snapshot 21e3d49 was atomically fast-forwarded without force to origin/main and origin/wt/indie-game-development with exact remote readback; the ready read-only purge-audit CALL remains the unchanged default. → history/2026-07-20-s-work-publish-integration-lab-entry-main-001.md

next: |
  # CALL c-audit-program-v2-legacy-lab-surface-001

  to: executor
  direction: indie-game-development
  track: program
  kind: engineering
  repo: ainazemtsau/GasCoopGame
  node: g-9c41
  task: legacy-lab-surface-audit
  issued: 2026-07-20 (s-shape-program-v2-integration-lab-entry-001)

  goal: |
    Установить точную first-hand границу удаления старых lab/demo scenes и scene-only support surface,
    чтобы новая постоянная Integration Lab начиналась без лишнего legacy и без потери действующей
    продуктовой authority или validator.

  context: |
    Владелец утвердил дословно: «Принимаю: одна постоянная Integration Lab, реальные gameplay paths,
    минимум debug-функций и сначала read-only purge-аудит».

    Постоянный product-proof entry один: Integration Lab. Она со временем принимает разные размеры и
    профили Dungeon Architect level generation и проверяет модули через настоящие gameplay objects,
    commands/events и production consumers. Debug-действие допустимо только как тонкий вызов того же
    production path, если без него проверка действительно неудобна. Track-specific fixture может жить
    лишь пока он является доказанно нужным validator; отдельная постоянная NearGasSimulationLab заранее
    не принята. Конкретные Gas, Grid, Level, Character, loot, benchmark и другие возможности формируются
    отдельными shape/PLAN по мере необходимости; универсальный Lab framework сейчас не заказан.

    First-hand shape evidence на clean product `main`
    `45b15623120f395b4295e43ac6cc5ed0c3aa108c` нашло 12 `.unity` scenes, но не нашло существующей
    `IntegrationLab` или `NearGasSimulationLab`. `docs/gas-simulation/PROGRAM.md` пока планирует новую
    engine-owned NearGasSimulationLab и временное сохранение старых gas/demo scenes; это нужно назвать
    как конфликт с новым owner verdict, а не молча перенести в cleanup. Current product authority и
    ссылки надо перечитать заново; указанный SHA — evidence shape-сессии, не freshness lock.

    Launch block: lane `program / Integration audit`; venue — текущий product `main` строго read-only,
    без отдельного worktree и без Unity Editor; machine `PC`; depends_on `[]`; merge_queue `none`;
    conflict_surface `none`, потому что продуктовые файлы не меняются. Gate — точные branch/HEAD/status
    до и после совпадают.

  boundaries: |
    Только read-only аудит. Не менять code, scenes, prefabs, assets, docs, specs, ADR, dependencies,
    packages, versions, branches или worktrees. Не запускать PLAN, PAIR, RED, BUILD, Unity, tests,
    import, merge, Deliver или publication. Ничего не удалять и не создавать. Не проектировать новую
    Lab architecture, module API или debug tool; не предлагать MIGRATE/SHIM как автоматическую судьбу
    legacy. Не считать archive authority. Vendor/sample assets не включать, если на них не ссылается
    game-owned surface. Если действующая authority или validator зависит от семейства, это KEEP либо
    BLOCKED, но не предположительный DELETE.

  done_when: |
    1. Собран полный game-owned inventory `.unity` scenes и их Build Settings/loading/addressable refs,
       setup/editor scripts, scene-only components, prefabs, tests, docs/spec/ADR и GUID/code refs.
    2. Каждое scene/support family имеет ровно один verdict `DELETE | KEEP | BLOCKED` с точными путями,
       прямыми ссылками, владельцем/consumer и коротким first-hand обоснованием.
    3. `DELETE` доказан отсутствием текущего consumer; `KEEP` называет действующую authority/validator;
       `BLOCKED` называет точную зависимость и один вопрос reconciliation. `MIGRATE/SHIM` не используется.
    4. Явно перечислены clauses текущих product PROGRAM/ADR/SPEC, конфликтующие с owner-approved purge
       и одной постоянной Integration Lab.
    5. Branch, HEAD и status до/после идентичны; Unity и tests не запускались; HOME сообщает команды,
       количества и точные blind spots.
    6. Возвращён six-line handoff с eligibility для owner-present purge PLAN либо одним точным blocker;
       successor CALL не создаётся executor-сессией.

  return: |
    Один self-contained audit HOME: inventory matrix, dependency evidence, DELETE/KEEP/BLOCKED boundary,
    authority conflicts, blind spots и six-line handoff. `review: n/a — read-only audit`.

  budget: <=0.5 focused day
  surface: any
  engineering_contract: 31

  END_OF_FILE: live/indie-game-development/work/c-audit-program-v2-legacy-lab-surface-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-20-s-work-publish-integration-lab-entry-main-001.md
