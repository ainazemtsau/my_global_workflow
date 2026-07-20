# CALL c-shape-program-v2-v30-entry-001

to: session
direction: indie-game-development
track: build-tooling
play: shape
node: g-c5d1
task: v30-entry
issued: 2026-07-20 (s-map-program-v2-hot-migration-route-001)

goal: |
  Определить единственный законный current-authority entry из завершённой Program v2 map в
  V30-era product work, не реализуя feature и не предполагая заранее, применён V30 или нет.

context: |
  Сначала прочитать свежие `live/indie-game-development/NOW.md`, `TREE.md`, `CHARTER.md`,
  `work/program-v2-integration-lab-plan.md`, релевантные V29/V30 history packets и текущую product
  authority. Карта рекомендует после законного V30 entry первую продуктовую волну из маленького
  static Integration Lab shell, universal Grid/Layers seam и bounded Gas Simulation drop, но эта
  рекомендация не разрешает автоматически запускать ни один из них.

  Известная до свежей проверки картина: NearGas L1B terminal HOME выпущен на product revision
  `693e671b`; Character Leg 2 остаётся в review/closing; Level LV0 PLAN reported RELEASED at
  `b1698170`, но Direction close отсутствует; V30 ранее существовал в Direction history как
  неприменённый route/tag. Эти сведения являются входными гипотезами, а не заменой first-hand check.

  Standalone `.NET Gates` retired. Любая реально нужная build/tooling работа остаётся bounded задачей
  этого направления с названным product consumer.

boundaries: |
  Shape/reconciliation only. Не менять product code, dependencies, worktrees, branches, versions,
  generated assets или Unity scenes; не запускать re-sync, PLAN, RED, BUILD, merge, Deliver или
  publication. Не перезапускать frozen L1B, Character, Level или visual CALLs. Не проводить Level LV0
  review в этой сессии. Не расширять legacy Character Leg 2 новой Actor Layer. Не воскрешать
  `.NET Gates` как track.

  Применить Conflict Guard. Если Direction card, V30 packet, product SPEC/ADR/PLAN или фактический
  repository state расходятся, вернуть `CONFLICT / NEEDS RECONCILIATION` с обеими сторонами и одним
  bounded reconciliation CALL; не выбирать молча удобную версию.

work: |
  1. Доказать текущую Direction version authority и product revision/version state first-hand.
  2. Найти точный V30 intent/payload и проверить, был ли он уже законно применён или superseded.
  3. Если product действительно отстаёт и intent остаётся действующим, сформировать ровно один
     no-feature `re-sync:30` engineering CALL с preconditions, non-goals, validation и rollback.
  4. Если V30 уже применён или законно superseded, вернуть evidence-backed skip и 2–3 bounded
     owner-readable shape choices для следующего product frontier, преимущественно Integration Lab,
     Gas Simulation и Grid / Layers / World Change.
  5. Не создавать фиктивные product tasks ради заполнения всех направлений.

done_when: |
  1. Текущие V29/V30/Direction/product facts подтверждены точными first-hand evidence locations.
  2. Статус entry однозначен: `re-sync:30 required`, `already applied/superseded`, либо один честный
     `CONFLICT / NEEDS RECONCILIATION`.
  3. Есть ровно одна рекомендация владельцу и понятные последствия её принятия.
  4. Возвращён полный следующий CALL или настоящий owner decision; product work не запущен.
  5. RESULT содержит six-line handoff из `work/program-v2-track-handoff-template.md`.

return: |
  Один owner-readable shape RESULT: evidence table, verdict, одна рекомендация, максимум 2–3
  альтернативы там, где они действительно нужны, полный next CALL/decision и six-line handoff.

budget: one bounded shape/reconciliation session
surface: owner-present if a real choice remains; otherwise may return the single lawful CALL

END_OF_FILE: live/indie-game-development/work/c-shape-program-v2-v30-entry-001-call.md
