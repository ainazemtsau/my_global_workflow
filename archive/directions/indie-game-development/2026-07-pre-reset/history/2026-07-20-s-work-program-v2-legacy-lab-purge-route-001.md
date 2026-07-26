RESULT s-work-program-v2-legacy-lab-purge-route-001 (call: c-audit-program-v2-legacy-lab-surface-001)
direction: indie-game-development
track: program
play: work
node/task: g-9c41/legacy-lab-surface-audit

outcome: |
  Read-only audit закрыт простым владельческим решением: сейчас удаляются только четыре семейства,
  для которых first-hand проверка не нашла current consumer. Семь спорных scenes не удаляются и не
  получают новых consumers; кроме SampleScene, они уже отсутствуют в Build Settings, runtime loading
  и Addressables. Character V2 fixtures и shared production/test support остаются KEEP.

  Единственный следующий Program root — bounded V31 cleanup. Он удаляет доказанный мусор, закрепляет
  короткую current-authority границу `legacy validator / no new consumers / delete after replacement
  proof` и возвращает terminal REPORT. Integration Lab, feature functionality, Lab framework и debug
  tools этим root не строятся; после его REPORT Program возвращается к функциональной работе.

evidence: |
  - Audit HOME проверил clean product `main` до/после на
    `45b15623120f395b4295e43ac6cc5ed0c3aa108c`, `origin/main +0/-0`, zero worktree/cached diff. Unity,
    import, tests, build, PLAN/PAIR/BUILD, merge и publication не запускались.
  - Inventory: 13 tracked `.unity`, 12 game-owned и одна unreferenced vendor demo; Build Settings/default
    содержит только `Assets/Scenes/SampleScene.unity`; runtime loaders и Addressables refs отсутствуют.
  - DELETE-now: stale `CharacterV1SceneSetup`; `GasBenchmarkScene` + director/editor;
    `ReactionSandboxScene` + component; orphaned DA GasLab assets (`CoopSmallSGF`, `GasLabSingle..`,
    `GasLabDB`, `Room_A`, `SnapGridFlowModuleBounds`) и stale `docs/c-exec-012-lab-guide.md`.
  - RETAIN/freeze-no-growth: Sample, Phase0, Buoyancy, GasVoxel, GasVisual, analytic GasLab и GasRoom.
    KEEP: three Character V2 proof scenes plus shared Core/Sandbox, topology, GasView/render, render
    profiles and referenced Dungeon Architect support.
  - Simple durable explanation: `work/legacy-lab-purge-boundary-2026-07-20.md`; exact cleanup contract:
    `work/c-exec-program-v2-legacy-lab-purge-001-call.md`.
  - Owner words: «какие можно удалить, удали их», «чтобы этот мусор не разрастался» and «мне нужен
    сейчас один вердикт, так, чтобы за следующий шаг мы закрыли этот вопрос и начали двигаться дальше».
  - Audit six-line handoff:
    status: ELIGIBLE — owner-present purge PLAN may proceed.
    base: main@45b15623120f395b4295e43ac6cc5ed0c3aa108c; clean before/after; contract 31.
    DELETE: stale V1 builder; benchmark family; reaction family; orphaned DA GasLab content/stale guide.
    KEEP: Character V2 fixtures; shared production/test support; Sample profile; referenced vendor code.
    BLOCKED: seven retained scenes stay until their exact replacement proofs exist.
    routing: executor created no successor; this Direction RESULT issues one bounded cleanup root.
  - review: n/a — read-only audit.

state_changes: |
  live/indie-game-development/NOW.md:
    - CLEAR returned/default program root `c-audit-program-v2-legacy-lab-surface-001`.
    - ADD ready/default root `c-exec-program-v2-legacy-lab-purge-001` in track `program`, pinned
      `engineering_contract: 31`, for one safe deletion/no-growth authority close.
    - SET `next.call` to `c-exec-program-v2-legacy-lab-purge-001`.
    - Preserve every unrelated track, call and `d-m1-min-spec-hardware-001` unchanged.
  live/indie-game-development/work/c-exec-program-v2-legacy-lab-purge-001-call.md:
    - CREATE the complete owner-present V31 engineering root with exact DELETE, RETAIN, KEEP, no-growth,
      budget and terminal REPORT boundaries.
  live/indie-game-development/work/legacy-lab-purge-boundary-2026-07-20.md:
    - CREATE the plain-language one-verdict explanation, delete/retain lists and consequence summary.
  live/indie-game-development/work/program-v2-integration-lab-plan.md:
    - RECORD audit complete, four DELETE-now families, seven frozen/no-growth validators and one cleanup
      root before feature work; keep milestone count at 2/10 because product has not changed yet.
  live/indie-game-development/work/board/dashboard.html:
    - REGENERATE Board, Journal, Problems and M2/Program mirrors from fresh NOW/LOG/plan: cleanup is the
      ready/default root, the audit is closed, and the simple verdict links to its owner-readable artifact.
  live/indie-game-development/LOG.md:
    - APPEND the declared one-line entry once.
  live/indie-game-development/history/2026-07-20-s-work-program-v2-legacy-lab-purge-route-001.md:
    - SAVE this complete RESULT once.
  live/indie-game-development/TREE.md, CHARTER.md, knowledge, unrelated work artifacts and every product
  repo file/branch/worktree: unchanged.

captures: []

decisions_needed: []

play_check:
  - "1 Recite: done — audit's purpose was exact safe deletion boundary before the one permanent Integration Lab; the HOME met all six done_when bullets."
  - "2 Owner inputs (owner): done — this is not a personal owner-content artifact; business verdict is the owner's actual words «какие можно удалить, удали их», «чтобы этот мусор не разрастался» and «за следующий шаг мы закрыли этот вопрос и начали двигаться дальше»."
  - "3 Do the work: done — consumed the audit HOME, reduced it to one plain verdict, recorded a durable simple boundary and issued exactly one V31 cleanup root; no product execution occurred."
  - "4 Self-check: done — every game-owned scene family has one current disposition; DELETE targets have no consumer, retained validators keep exact reasons, Build/loading/addressable facts and authority conflicts are carried into the root, and scope remains <=0.5 focused day."
  - "5 Close: done — returned audit root is cleared, unrelated tracks survive, the new program root is ready/default, owner panel mirrors fresh state, and no successor was invented by the executor."

log: 2026-07-20 · s-work-program-v2-legacy-lab-purge-route-001 · work · program · g-9c41/legacy-lab-surface-audit: consumed the clean read-only audit and owner's fast-close verdict; four unused legacy families are DELETE-now, seven scenes are frozen/no-growth validators, and one V31 cleanup root is the sole ready/default continuation before feature work. → history/2026-07-20-s-work-program-v2-legacy-lab-purge-route-001.md

next: |
  # CALL c-exec-program-v2-legacy-lab-purge-001

  to: executor
  direction: indie-game-development
  track: program
  kind: engineering
  repo: ainazemtsau/GasCoopGame
  node: g-9c41
  task: legacy-lab-purge
  issued: 2026-07-20 (s-work-program-v2-legacy-lab-purge-route-001)

  goal: |
    Текущий продукт не содержит доказанно неиспользуемый legacy lab/demo surface, а оставшиеся временные
    validators имеют одну недвусмысленную границу: они не являются постоянными product entry points и не
    получают новых consumers до естественной замены одной Integration Lab.

  context: |
    Владелец после read-only аудита сказал дословно: «какие можно удалить, удали их», «чтобы этот мусор
    не разрастался» и «мне нужен сейчас один вердикт, так, чтобы за следующий шаг мы закрыли этот вопрос
    и начали двигаться дальше».

    Один принятый практический вердикт: сейчас удалить только четыре семейства с доказанным отсутствием
    current consumer; семь спорных сцен не удалять и не переделывать. Они уже отсутствуют в runtime
    loading/addressables/Build Settings, кроме `SampleScene`, которая остаётся единственной launch/default
    scene до появления настоящей Integration Lab. Не добавлять технический quarantine framework или guard:
    короткая current-authority запись запрещает новые consumers, а каждый retained validator удаляется,
    когда реальный gameplay path естественно заменит его proof.

    Read-only audit на clean product `main` `45b15623120f395b4295e43ac6cc5ed0c3aa108c` нашёл 13 tracked
    `.unity`, из них 12 game-owned и одну unreferenced vendor demo. Build Settings содержит только
    `Assets/Scenes/SampleScene.unity`; runtime scene loaders и Addressables refs отсутствуют. SHA — evidence
    аудита, не freshness lock: перед изменениями перечитать current product authority и incoming refs.

    DELETE-now surface; парные `.meta` входят в ту же границу:

    1. `Assets/GasCoopGame/Adapters/Characters/Editor/CharacterV1SceneSetup.cs` — stale V1 builder без
       внешнего consumer, способный перезаписать текущие V2 fixtures.
    2. `Assets/GasCoopGame/Adapters/GasView/GasBenchmarkScene.unity`,
       `Assets/GasCoopGame/Adapters/GasView/VoxelBenchmarkDirector.cs`,
       `Assets/GasCoopGame/Adapters/GasView/Editor/VoxelBenchmarkDirectorEditor.cs`.
    3. `Assets/GasCoopGame/ReactionSandboxScene.unity`,
       `Assets/GasCoopGame/Adapters/GasView/ReactionSandbox.cs`.
    4. `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`,
       `Assets/GasCoopGame/Levels/GasLab/Flow/GasLabSingle..asset`,
       `Assets/GasCoopGame/Levels/GasLab/Modules/GasLabDB.asset`,
       `Assets/GasCoopGame/Levels/GasLab/Modules/Room_A.prefab`,
       `Assets/GasCoopGame/Levels/GasLab/Modules/SnapGridFlowModuleBounds.asset`,
       `docs/c-exec-012-lab-guide.md`; empty folder/meta may disappear, shared
       `GasLabBounds.asset` и `GasLabRoom.mat` remain.

    RETAIN/freeze-no-growth scenes: `SampleScene`, `GasSourcePhase0Demo`, `GasBuoyancyDemoScene`,
    `GasVoxelSandboxScene`, `GasVisualScene`, `GasLabScene`, `GasRoomScene`. KEEP current Character V2 proof
    scenes and shared Core/Sandbox, topology, GasView/render and referenced Dungeon Architect support.
    Exact dependency explanations are recorded in Direction artifact
    `live/indie-game-development/work/legacy-lab-purge-boundary-2026-07-20.md` and the returning audit HOME.

    Current authority conflicts include `docs/gas-simulation/PROGRAM.md`, ADR-E-0010, ADR-0012,
    ADR-0016, ADR-0020, canonical gas-visual requirements RGS-OWNER/LAB-OWNER and c-visual-003
    ROOM1/W1A-OWNER. Historical evidence remains history; current authority must no longer imply several
    permanent Labs or invite new dependencies on retained fixtures.

    Launch block: lane `program / Integration cleanup`; venue — fresh repo-runner-owned V31 workspace,
    never direct edits on the owner's main checkout; machine `PC`; depends_on `[]`; conflict surface is only
    the named DELETE families plus the smallest current-authority reconciliation; merge/publication follow
    the installed product V31 contract.

  boundaries: |
    Не создавать Integration Lab в этом root. Не удалять и не переписывать семь retained scenes, Character
    V2 fixtures, shared production/core/test support, `GasLabBounds.asset`, `GasLabRoom.mat`, render profiles
    или referenced vendor code. Не добавлять Lab framework, runtime disable layer, feature flags, stubs,
    MIGRATE/SHIM, module API, gameplay functionality или debug tools. Не переписывать исторические ADR/results
    так, будто их не существовало; current authority может явно supersede их clauses. Не расширять cleanup,
    если fresh refs показывают нового consumer: вернуть один exact ESCALATE blocker. Не тратить время на
    визуальный owner-eye — пользовательского результата здесь нет.

  done_when: |
    1. Все перечисленные DELETE-now paths и их `.meta` отсутствуют в final tracked tree; manifest перечисляет
       удалённые пути, а fresh incoming GUID/name/code scan подтверждает отсутствие потерянного consumer.
    2. Retained/KEEP surface не изменён. Build Settings/default по-прежнему указывает только SampleScene;
       новые runtime loaders, Addressables refs и consumers retained scenes не появились.
    3. Один короткий owner-readable current-authority документ (не более 400 слов) говорит простыми словами:
       одна future permanent Integration Lab; семь временно retained scene validators; Character V2/shared
       support KEEP; четыре удалённые семьи; запрет новых consumers; точный replacement/removal trigger.
    4. Current PROGRAM/spec authority больше не обещает отдельные permanent NearGas/visual Labs и не требует
       расширять legacy scenes. Исторические ADR clauses имеют явную superseded-связь, а действующие Phase0,
       visual и wiring proofs остаются честно обозначенными временными validators до замены.
    5. Repo-native V31 build/hygiene/relevant tests и deletion/reference checks GREEN; никаких claims о новой
       Lab, gameplay capability или визуальном proof не сделано.
    6. Gated V31 REPORT/RELEASED HOME содержит exact commits, deletion manifest, authority-document path,
       commands/results, assumptions/cuts, review-evidence и clean final status. Если root выходит за
       `<=0.5 focused day`, он возвращает один ESCALATE blocker вместо расширения scope.

  return: |
    Один простой REPORT HOME: «что удалено / что оставлено и почему / можно ли сразу вернуться к feature
    work», затем exact V31 evidence. Successor CALL executor не создаёт.

  budget: <=0.5 focused day
  surface: any
  engineering_contract: 31

  END_OF_FILE: live/indie-game-development/work/c-exec-program-v2-legacy-lab-purge-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-20-s-work-program-v2-legacy-lab-purge-route-001.md
