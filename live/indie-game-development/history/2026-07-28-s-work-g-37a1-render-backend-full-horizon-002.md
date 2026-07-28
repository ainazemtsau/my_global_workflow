# RESULT s-work-g-37a1-render-backend-full-horizon-002

RESULT s-work-g-37a1-render-backend-full-horizon-002 (call: c-work-g-37a1-render-backend-owner-verdict-002)
direction: indie-game-development
track: t-render
play: work
node/task: g-37a1/t-4

outcome: |
  Прежний вывод «не покупать, максимум около двух дней выигрыша» исправлен: он считал только
  минимальный render-backend первого ядра и не считал названный владельцем полный горизонт.
  Консервативная непересекающаяся база из изменяемого chunk-world, destruction/debris,
  underground visibility/large coordinates и visual material machinery даёт примерно 8–14
  сфокусированных дней чисто избегаемой реализации после нашей Core/FishNet/QA-интеграции.
  Это выше порога владельца примерно в пять дней, поэтому рекомендация меняется на покупку Voxel
  Play 4 за консервативные $149.99 и установку его под Core-grid. Это checkpoint: точного buy/no-buy
  владельца не было, поэтому t-4 и d-topology-backend-purchase-001 остаются открыты.

evidence: |
  - Точные слова владельца, исправившие scope: «нам же визуал», «относительно большие уровни»,
    «блоки там взрываться, там, возможно, какие-то падать» и «весь функционал, который нам в будущем
    пригодится»; это не buy/no-buy verdict.
  - Полный исправленный расчёт, анти-double-counting, остатки интеграции, исключённый speculative
    upside и F3 boundary:
    live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28-v2.md
  - Предыдущий расчёт сохранён как evidence только минимального current-core backend и прямо
    superseded для денежного решения:
    live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28.md
  - Официальные первичные источники: chunks/lifecycle
    https://kronnect.com/docs/voxel-play-4/chunks/
    https://kronnect.com/docs/voxel-play-4/chunk-lifecycle/ ; structural collapse/debris
    https://kronnect.com/docs/voxel-play-4/structural-collapse/ ; dynamic voxel physics
    https://kronnect.com/docs/voxel-play-4/voxel-properties-api/ ; underground occlusion
    https://kronnect.com/docs/voxel-play-4/occlusion-culling/ ; visual/material stack
    https://kronnect.com/docs/voxel-play-4/microvoxels/
    https://kronnect.com/docs/voxel-play-4/connected-textures/
    https://kronnect.com/docs/voxel-play-4/anti-tiling/ ; loading/editor/API limits
    https://kronnect.com/docs/voxel-play-4/loading-saving/
    https://kronnect.com/docs/voxel-play-4/world-editor/
    https://kronnect.com/docs/voxel-play-4/multiplayer-api/
  - Цена $149.99 взята с канонической product page, а не из flash-sale карточки:
    https://assetstore.unity.com/packages/tools/game-toolkits/voxel-play-4-391842
  - Self-check: optional Super Chunks, save/editor, microvoxels, generation, gameplay systems,
    multiplayer savings and colliders score zero in the base; package docs establish implemented
    machinery, not local compatibility; no purchase/install/product mutation occurred.

state_changes: |
  - Create live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28-v2.md with
    the corrected full-horizon calculation and END_OF_FILE trailer; preserve v1 unchanged as the
    narrower current-core evidence.
  - Create live/indie-game-development/work/c-work-g-37a1-render-backend-owner-verdict-003-call.md
    as the same-lane continuation for the owner's exact buy/no-buy words.
  - NOW.md:
    - set updated to 2026-07-28 by s-work-g-37a1-render-backend-full-horizon-002;
    - preserve bet, tracks, all unrelated tasks/calls/decisions/issues and t-4 status active;
    - replace only t-4.goal/done_when with the owner's corrected full-horizon choice and threshold
      test: DIY cost minus unavoidable package integration/testing, plus exclusions and authority
      boundaries;
    - clear open_calls[c-work-g-37a1-render-backend-owner-verdict-002];
    - add open_calls[c-work-g-37a1-render-backend-owner-verdict-003] ready in t-render for t-4,
      pointing to its CALL file and v2 evidence;
    - keep decisions[d-topology-backend-purchase-001] open; replace its stale minimal-mesher
      question/options plus recommendation/note with the full-horizon own-stack choice, the
      superseding 8–14-day BUY recommendation and the unchanged F3/Core authority.
  - LOG.md: prepend the exact log line once.
  - Save this full RESULT once as
    live/indie-game-development/history/2026-07-28-s-work-g-37a1-render-backend-full-horizon-002.md.
  - No CHARTER.md, TREE.md, product repository, purchase, install, task status, other call or other
    lane changes.

captures: []

decisions_needed:
  - q: "Покупаем Voxel Play 4 под Core-grid или сознательно строим свой voxel-world stack?"
    options:
      - "Покупаем Voxel Play 4 и ставим его под нашу логическую сетку."
      - "Не покупаем Voxel Play 4; сознательно строим свой voxel-world stack."
    recommendation: "Покупать: консервативная непересекающаяся база полного названного горизонта избегает примерно 8–14 сфокусированных дней против порога примерно 5; Core-grid/FishNet/QA остаются нашими."

play_check:
  - "1 Recite: done — checkpoint сверён с active bet g-37a1, task t-4, lane t-render и возвращающим owner-verdict CALL."
  - "2 Owner inputs (owner): done — scope исправлен его точными словами «нам же визуал», «относительно большие уровни», «блоки там взрываться, там, возможно, какие-то падать», «весь функционал, который нам в будущем пригодится»; buy/no-buy из них не выведен."
  - "3 Do the work: done — четыре независимых owner-named subsystem оценены как DIY, VP4 residual и net avoided; возможности/ограничения сверены по официальной документации и записаны в v2 artifact."
  - "4 Self-check: done — строки не задвоены; optional/uncertain upside и запретные colliders/multiplayer score поставлены в ноль; точная цифра помечена средней уверенности, а пакет не назван доказанно совместимым до установки."
  - "5 Close: done as checkpoint — returning id cleared, same-lane owner-verdict continuation registered; t-4 and decision remain open because no exact verdict exists."

log: 2026-07-28 | s-work-g-37a1-render-backend-full-horizon-002 | t-render | work | direction | g-37a1/t-4: прежний 0/2-дневный no-buy счёт отозван как расчёт только минимального backend первого ядра; четыре названных владельцем контура полного продукта дают примерно 8–14 сфокусированных дней чисто избегаемой реализации, поэтому рекомендация меняется на покупку VP4 под Core-grid, а точный вердикт остаётся за владельцем -> history/2026-07-28-s-work-g-37a1-render-backend-full-horizon-002.md

next: |
  CALL c-work-g-37a1-render-backend-owner-verdict-003
  to: session
  direction: indie-game-development
  track: t-render
  play: work
  node: g-37a1
  task: t-4
  goal: Владелец зафиксировал окончательный выбор между VP4 под Core-grid и собственным voxel-world stack.
  context: corrected full-horizon evaluation at
    live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28-v2.md;
    net avoided about 8–14 focused days at conservative $149.99; recommendation buy; exact owner
    words required.
  boundaries: no inferred verdict or purchase/install; preserve Core-grid/FishNet authority, direct
    grid collision and all other lanes.
  done_when: exact owner verdict closes d-topology-backend-purchase-001 and t-4 and routes the
    corresponding next render step.
  return: RESULT with the owner's exact words.
  budget: one short owner answer

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-work-g-37a1-render-backend-full-horizon-002.md
