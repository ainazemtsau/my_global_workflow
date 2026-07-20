RESULT s-shape-program-v2-v30-entry-001 (call: c-shape-program-v2-v30-entry-001)
direction: indie-game-development
track: build-tooling
play: shape
node/task: g-c5d1/v30-entry

outcome: |
  Verdict: already applied/superseded. The old V30 route is not a pending product installation: current Direction
  authority is V31, V31 explicitly carries the V30 root route forward, and the product is already stamped and
  documented as re-synced to V31. A `re-sync:30` CALL would therefore repeat a retired version step and is not lawful.

  The owner selected the one recommended next frontier: a short, no-feature shape in the existing primary
  `Integration Lab & Product Proof` track. Its only job is to decide whether the common scene is a new thin shell,
  part of the planned `NearGasSimulationLab`, or needs reconciliation. No product task, scene or PLAN/BUILD work was
  opened here.

evidence: |
  | Question | First-hand evidence | Finding |
  | --- | --- | --- |
  | Current Direction contract | `origin/main:os/engineering/CONTRACT_VERSION`, introduced by `6d1858ba6a78529e254b4fe81fb17703eb09c182` | `current: 31`; V31 says a re-sync carries forward the V30 root route and preserves earlier roots. |
  | Exact V30 intent | tag `engineering-contract-v30` at `2e7d4b51ed0536d4b57ec45d97d181457b74e5b1` | V30 was a bounded root-route replacement, not a feature. The V30 tag is ancestral to V31, so V31 lawfully supersedes its cumulative route. |
  | Current product state | `C:\projects\Unity\GasCoopGame` at clean `main` `45b15623120f395b4295e43ac6cc5ed0c3aa108c`; `validation.config` lines 5, 8, 15, 21, 53 | Product is stamped `synced_contract_version: 31`, selector `re-sync:31`, source `6d1858...`, with V29/V30 retained as legacy evidence. |
  | Product acceptance of V31 | `docs/adr/ADR-P-0014-c-maint-contract-v31-resync-001-exact-input-venue-evidence.md` and commit `793bd7d4780aa91fd3013de589f746e62f550f70` | Accepted process-only `re-sync:31`; it keeps V30 pinned roots while adding V31 controls. |
  | Existing scene seam to reconcile | `docs/gas-simulation/PROGRAM.md` lines 166–202; `openspec/specs/sim-core/spec.md` headings at lines 37, 45, 69 and 85 | A planned engine-owned `NearGasSimulationLab` and Layer/Revision seams already exist in product authority; a common Lab must not silently duplicate them. |

  Direction/product facts do not form a Conflict Guard contradiction: the current authority expressly supersedes the
  older V30 packet, and the product carries the matching V31 stamp and accepted ADR. The old V30 wording in the map
  was historical navigation, now updated to state that V31 is current; it was not treated as permission to choose a
  different version silently.

recommendation: |
  Enter the existing primary Integration Lab track with one owner-present shape-only CALL. It is the smallest safe
  step because it prevents two competing test scenes before Gas or Grid receive an implementation task, while keeping
  all already split tracks parked and preserving their own ownership.

alternatives: |
  1. Gas Simulation shape first — useful later, but it risks treating the planned NearGas lab as the common scene
     before Integration has defined the acceptance boundary.
  2. Grid / Layers shape first — useful later, but it cannot decide who owns the scene entry point or prevent scene
     duplication.
  Both remain parked; neither is a rejected product direction.

owner_verdict: |
  The owner selected the recommendation after the plain-language explanation: «Да, переходим в трек общей сцены».

state_changes: |
  live/indie-game-development/NOW.md:
    - CLEAR returned root `c-shape-program-v2-v30-entry-001`.
    - ADD ready/default program root `c-shape-program-v2-integration-lab-entry-001`, a shape-only ownership decision
      for the common Integration Lab entry; preserve all unrelated calls, tracks and the pending min-spec decision.
    - SET `next.call` to that new ready root.
  live/indie-game-development/work/c-shape-program-v2-integration-lab-entry-001-call.md:
    - CREATE the complete owner-present shape CALL; no product repository target or implementation authority.
  live/indie-game-development/work/program-v2-integration-lab-plan.md:
    - MARK M1 accepted as V30 superseded by installed V31; make the next recommended step the Integration Lab
      ownership shape before M2 and update later new-root references from V30 to V31.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE Board, Problems and Journal from current NOW, LOG and findings; show M1 complete, the new default,
      V31 truth and the non-blocking existing findings in plain language.
  live/indie-game-development/LOG.md:
    - APPEND the declared one-line entry once.
  live/indie-game-development/history/2026-07-20-s-shape-program-v2-v30-entry-001.md:
    - SAVE this complete RESULT.
  live/indie-game-development/TREE.md, CHARTER.md, product/canon repositories, frozen CALLs, branches, worktrees,
  scenes, generated assets, versions and dependencies: unchanged.

captures: []
decisions_needed: []

play_check:
  - "1 Recite: done — the bounded task was to prove the one lawful entry from the completed Program v2 map without assuming that V30 had been applied."
  - "2 Appetite: done — the one-session, no-feature budget was held; the only proposed continuation is another shape, not an implementation task."
  - "3 Approaches: done — Integration Lab, Gas Simulation and Grid / Layers were compared as bounded next shape frontiers."
  - "4 Scope hammer: done — re-sync, PLAN, RED, BUILD, scenes, product code, legacy relaunches and standalone .NET Gates stayed out."
  - "5 Lens sweep: done — common-scene ownership reduces duplicate work; V31 continuity protects legacy evidence; no early Lab claim is presented as co-op or live simulation."
  - "6 Riskiest assumption: done — planned NearGasSimulationLab may overlap with the common Lab; the successor exists to test that assumption before any scene is created."
  - "7 Tasks: done — no fictitious product task was created; one real program-track shape CALL is the only continuation."
  - "8 Kill criteria: done — if product PROGRAM, SPEC/ADR or scene facts cannot support one ownership boundary, the successor returns CONFLICT / NEEDS RECONCILIATION and opens no build."
  - "9 Close: done — owner verdict words are «Да, переходим в трек общей сцены»."

handoff: |
  status: superseded
  result: Historical V30 re-sync is superseded by current, product-installed V31; no feature or product change was authorized.
  proof: `origin/main` CONTRACT_VERSION is 31, V30 tag is ancestral to V31, and product validation.config plus accepted ADR-P-0014 record re-sync:31.
  scene_drop: none
  blocker: none — the next shape must only settle common Lab ownership against planned NearGasSimulationLab before implementation.
  next: CALL c-shape-program-v2-integration-lab-entry-001

log: 2026-07-20 · s-shape-program-v2-v30-entry-001 · shape · build-tooling · g-c5d1/v30-entry: first-hand authority check found the historical V30 route fully superseded by current product-installed V31; no re-sync or product work issued, and the owner selected a shape-only common Integration Lab entry as the single next step. → history/2026-07-20-s-shape-program-v2-v30-entry-001.md

next: |
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

END_OF_FILE: live/indie-game-development/history/2026-07-20-s-shape-program-v2-v30-entry-001.md
