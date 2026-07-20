# CALL c-shape-program-v2-integration-lab-entry-001

to: session
direction: indie-game-development
track: program
play: shape
node: g-9c41
task: integration-lab-entry
issued: 2026-07-20 (s-shape-program-v2-v30-entry-001)

goal: |
  Утвердить единственный минимальный смысл, границу и ownership общего Integration Lab entry point,
  который сможет принимать будущие product drops без дублирования уже запланированной NearGas lab.

context: |
  Перед решением прочитать свежие `live/indie-game-development/NOW.md`, `TREE.md`, `CHARTER.md`,
  `work/program-v2-integration-lab-plan.md`, текущие product SPEC/ADR/PLAN и фактическое дерево сцен.
  Предыдущая shape-проверка first-hand установила, что V30 route исторический и полностью superseded
  current engineering contract V31: `os/engineering/CONTRACT_VERSION` на `origin/main` показывает
  `current: 31`, а product `validation.config` stamped 31 и product ADR фиксирует process-only
  `re-sync:31`. Это разрешает новые V31 roots, но не разрешает создавать сцену автоматически.

  В product `docs/gas-simulation/PROGRAM.md` уже запланирован engine-owned
  `NearGasSimulationLab`; current `openspec/specs/sim-core/spec.md` уже описывает Layer registry и
  revision feed. Program v2 map предлагает маленький static Integration Lab shell как следующий
  milestone, но не определяет, является ли он тем же entry point, оболочкой вокруг NearGas lab или
  отдельной общей сценой. Эта неопределённость должна быть решена до PLAN/BUILD, чтобы не создать
  две конкурирующие сцены.

boundaries: |
  Shape/reconciliation only. Не менять product code, dependencies, scenes, generated assets, worktrees,
  branches, versions или product documents; не запускать PLAN, RED, BUILD, re-sync, Unity, tests,
  merge, Deliver или publication. Не открывать Gas, Grid, Level, Character, Presentation или tool work
  как feature task. Не менять frozen legacy calls и не считать старую сцену принятой Program v2 drop.

  Применить Conflict Guard. Если Direction map, product PROGRAM, SPEC/ADR или фактическая сцена
  расходятся, вернуть `CONFLICT / NEEDS RECONCILIATION`, назвать обе стороны и выдать ровно один
  bounded reconciliation CALL; не выбирать молча более удобную интерпретацию.

done_when: |
  1. First-hand evidence показывает, существует ли уже подходящая scene/lab и как она соотносится с
     планируемой NearGasSimulationLab и common Integration Lab.
  2. Владелец выбрал один из максимум трёх простых вариантов ownership/acceptance: общий entry point,
     Gas-owned lab с Integration intake или честный reconciliation blocker.
  3. Есть ровно один bounded следующий product CALL или owner decision с named consumer, non-goals,
     validation и rollback; scene/product work не начата в этой сессии.
  4. RESULT содержит six-line handoff из `work/program-v2-track-handoff-template.md`.

return: |
  Один owner-readable shape RESULT: простая картина фактов, 2–3 вариантов, одна рекомендация,
  owner verdict, scope cut, риски/kill condition и полный следующий CALL либо честный blocker.

budget: one owner-present shape session
surface: owner-present

END_OF_FILE: live/indie-game-development/work/c-shape-program-v2-integration-lab-entry-001-call.md
