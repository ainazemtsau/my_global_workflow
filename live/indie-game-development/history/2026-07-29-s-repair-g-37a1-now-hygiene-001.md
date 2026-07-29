# RESULT s-repair-g-37a1-now-hygiene-001

direction: indie-game-development · play: repair · node/task: g-37a1/NOW
date: 2026-07-29

outcome: |
  `NOW.md` снова является текущим состоянием, а не журналом: свежая после параллельного
  render repair база 606 строк / 308,922 байта стала 249 строками / 28,957 байтами.
  Сохранены все 11 задач, пять execution lanes, WIP=5 и пять живых CALL. Forecast остаётся
  `no_basis`; историческая аргументация заменена work/history pointers.

evidence: |
  Fresh apply base: HEAD `058a1f4a0dd8e8dde27d9d52ed422d488c0072d2`; origin/main
  `66522f2a302794f0f1c620050a868fdd69459f57` является его предком.
  До repair: `NOW.md` blob `542d41a3e6fadec0d65dd6dfc3e315a6efded77c`, 606 строк,
  308,922 байта, 23 issues, 12 open_calls, 10 decisions и 11 tasks. После repair:
  blob `e5f22a2f8cb435d08e945ddc55da217807f48f6a`, 249 строк, 28,957 байт,
  14 unresolved issues, 5 live open_calls, 1 pending decision и один EOF trailer.
  Все пять сохранённых CALL-файлов существуют. `git diff --check` проходит.
  Исторический cleanup `fb72837b` был 69 строк / 5,202 символа; после него NOW трогали
  44 коммита, а этот apply пришлось сериализовать после параллельного render-коммита.

state_changes: |
  `live/indie-game-development/NOW.md` нормализован по stable ids поверх свежего render blob
  `542d41a3e6fadec0d65dd6dfc3e315a6efded77c`:

  - Сохранены без смены смысла bet g-37a1, tasks t-1…t-11, их статусы,
    `track_wip_limit: 5` и lanes t-sim/t-body/t-venue/t-render/t-coop. Длинные bet/evidence
    поля сокращены до текущего утверждения и work/history pointer.
  - Полностью сохранён semantic delta коммита `058a1f4a`: t-5 blocked; t-7 переписана на
    sparse Solid/Partial/Empty + mask-delta; t-10/t-11 добавлены blocked; t-render указывает
    на t-11; новый `c-work-g-37a1-render-vp4-micro-adapter-001` blocked; coop root blocked;
    resolution/routing point 3 остаются в `i-gas-core-open-questions-001`.
  - Старый завершённый `c-repair-g-37a1-render-vp4-task-001`, удалённый render-коммитом,
    не восстановлен. Старый `openedCells` нигде не восстановлен как authority: он остаётся
    только отрицательной меткой отменённого coop-контракта.
  - `direction_forecast` сохранён как `no_basis`, `as_of` обновлён на 2026-07-29, drivers
    сокращены до четырёх текущих факторов; численная вероятность не вводилась.
  - Удалены historical CURRENT/PRIOR headings и running narrative.
  - Из свежей базы удалены девять resolved/admitted issues с сохранением disposition:
    - `i-core-topology-live-vs-dead-tier-001` — consumed t-1;
    - `i-sim-build-task-missing-001` — admitted в t-6/t-7;
    - `i-gas-deadzone-uncalibrated-001` — admitted в t-6;
    - `i-core-form-seams-from-concept-001` — consumed shape;
    - `i-engine-fit-decision-ladder` — owner verdict и shape завершены;
    - `i-card-clauses-unverifiable` — surviving work admitted в tasks;
    - `i-core-acceptance-instrument-unpriced` — apparatus cut владельцем, остаток admitted;
    - `i-flow-model-unmeasured` — envelope work admitted в t-10 коммитом `058a1f4a`;
    - `i-concept-frame-admission` — superseded frame не является live authority.
    `i-render-task-missing-after-vp4-decision-001` уже отсутствовал на свежей render-базе и
    этим repair повторно не удалялся.
  - Оставлены и сокращены 14 действительно unresolved issues. Mixed issue
    `i-gas-core-open-questions-001` теперь несёт только текущий verdict/routing;
    `i-substance-passage-open-questions` — только отложенную открытую половину.
  - По точным словам владельца удалены из `open_calls` семь terminal rows:
    `c-work-g-37a1-topology-boundary-001`,
    `c-converge-verify-g-37a1-core-rows-cut-repair-check-001`,
    `c-converge-g-37a1-core-rows-cut-repair-001`,
    `c-converge-verify-g-37a1-core-rows-cut-check-001`,
    `c-research-g-37a1-concept-extraction-001`,
    `c-map-g-37a1-engine-ladder-brief-001`,
    `c-converge-g-37a1-core-rows-repair-002`. Их CALL/result артефакты не удалялись.
  - Сохранены пять live calls: три ready product roots и два blocked direction roots.
    Ранее одобренный переход старого render repair `ready -> running` стал moot: свежая база
    уже содержит завершённый repair и его новый blocked successor, поэтому устаревший CALL
    не возвращён.
  - Удалены ANSWERED decisions `d-sim-build-task-001`, `d-core-value-below-001`,
    `d-core-run-lifecycle-001`, `d-core-outcome-exit-test-001`,
    `d-core-acceptance-format-001`, `d-core-level-authoring-001`,
    `d-core-geometry-and-view-001`, `d-post-verify-route-001`; outcomes живут в TREE/tasks/history.
    Open `d-october-route-charter` свёрнут без потери вопроса в
    `i-october-route-not-a-condition` до его frame trigger. Оставлен только pending
    `d-air-counter-visibility-001`, привязанный к t-body, с тремя вариантами и рекомендацией.
  - В `LOG.md` добавлен один newest-first индексный ряд. В `os/FRICTION.md` записан третий
    рецидив enforcement-gap и фактическая concurrent-apply коллизия; EOF trailer перенесён
    в настоящий конец. OS-правила не менялись.

captures: []

decisions_needed: []

play_check:
  - 1 name contradiction: done — schema требует unresolved-only и roughly one-screen hot state, а NOW был 606-строчным журналом с terminal rows.
  - 2 reconstruct: done — fresh HEAD/origin, CHARTER, TREE, LOG tail, NOW stable ids и named receipts сверены newest-first; render `058a1f4a` принят как apply base.
  - 3 propose corrected state: done — каждому удалению дана disposition; outstanding state и concurrent render facts сохранены как schema fields/pointers.
  - 4 confirm (owner): done — владелец написал «Применяй пакет очистки. Удаляй из open_calls:» и поимённо перечислил все семь удалённых call ids.
  - 5 friction: done — третий рецидив и реальная apply-коллизия записаны в `os/FRICTION.md`; отдельный maintenance fix здесь не выполнялся.

log: repair g-37a1/NOW: 606-line history journal reduced to current state; terminal calls and resolved entries cleared by exact owner-approved batch

next: |
  return-to-owner — cleanup применён. Enforcement-механизм должен быть отдельной свежей
  MAINTENANCE-сессией; этот repair его не проектировал и не менял.

END_OF_FILE: live/indie-game-development/history/2026-07-29-s-repair-g-37a1-now-hygiene-001.md
