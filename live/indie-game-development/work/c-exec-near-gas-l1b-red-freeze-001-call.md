# CALL c-exec-near-gas-l1b-red-freeze-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-17 (s-work-near-gas-l1b-surface-freeze-close-001)

goal: |
  NearGas L1B имеет неизменяемый независимо созданный RED-артефакт, который на exact frozen carrier
  `163dffaa5649cc4f9b010a61ba84f4838f974337` компилируется, обнаруживается настоящим runner и падает
  только на ещё отсутствующем поведении ровно пяти принятых observation families.

context: |
  Это отдельный RED-FREEZE после закрытого SURFACE-FREEZE, а не BUILD и не продолжение surface-author session.
  Direction acceptance `live/indie-game-development/work/neargas-l1b-acceptance.md` фиксирует ровно пять families:
  retry snapshot, fault injection, handler classification, sparse-kernel rows и test-side loopback trace. Owner-approved
  product authority: `openspec/changes/c-exec-near-gas-l1b-plan-001/PLAN.md`, proposal/tasks/delta spec в том же change,
  `docs/neargas-L1b-decisions.md` и ADR-E-0013. Владелец ранее принял PLAN точными словами «Принимаю PLAN».

  SURFACE-FREEZE HOME закрыт Direction-сессией
  `s-work-near-gas-l1b-surface-freeze-close-001`. Frozen carrier:
  `163dffaa5649cc4f9b010a61ba84f4838f974337`; его фактический Git parent
  `e15914cd95f55a009d4c58e05be449ffee1a6e48`, cumulative freeze-parent для лимита
  `409ef4a7cf661fd5639a74364b7cd0469a673031`. Exact production manifest между cumulative parent и carrier:
  `Assets/GasCoopGame/Core/Field/NearGas/NearGasSimulation.cs` +269/-3,
  `Assets/GasCoopGame/Core/Field/Voxel/Reactions/VoxelField.Reactions.cs` +37/-6,
  `Assets/GasCoopGame/Core/Field/Voxel/VoxelField.cs` +91/-1; итого +397/-10. Decision page — 326 слов,
  blob `1e1ae42a5145f2510eecf9214b491fca88c9844e`. Новых C#-файлов не было; все три существующих `.cs.meta`
  tracked. Public `ReplaceGeneration`/`Step` сохранились; ordinary L1a path проходит с `observation == null`.
  Unity compilation, `dotnet build`, 1793/1793 existing tests, full `tools/check.ps1`, hygiene и fresh non-author
  review exact carrier — GREEN. Product HOME сообщил current clean `dev == origin/dev @
  4967455c25f1a537ef68015f18248481a1478dc0`; carrier и handback остаются его предками. Эти SHAs пинят evidence,
  но не назначают venue, worktree или branch.

  Direction engineering contract current = v28; HOME честно сообщил product stamp v27. Terminal v28 Re-sync остаётся
  известной отдельной control-plane обязанностью. Не смешивать её файлы с tests/test-support-only RED artifact и не
  заявлять stamp 28 без фактического re-sync. Этот CALL сам требует terminal HOME handback: executor не создаёт и не
  просит у владельца successor. Если свежая repo authority требует re-sync до RED writes, STOP до тестовых изменений
  и верни точный blocker; не обходи и не встраивай re-sync в immutable RED diff.

  launch:
    lane: A / NearGas core, headless
    venue: current product registry assigns; Direction pins no path, branch or workspace
    machine: PC; Unity Editor only if fresh product authority explicitly requires it
    base: fresh current product authority; frozen carrier 163dffaa is the exact RED target, not a branch tip
    conflict_surface: tests and test-support for NearGas L1B only
    depends_on: Direction-closed SURFACE-FREEZE GREEN at exact carrier 163dffaa
    merge_queue: product registry and integration queue own admission/publication
    gates: independent non-surface-author test author; real compile/discovery/behavior RED; fresh refutation remains next

boundaries: |
  The immutable RED commit/diff is tests and test-support only. Do not edit the three frozen production files, public
  surface, decision page, PLAN/spec/ADR, production recording/comparison/evaluator behavior, fault throwing or L1a.
  Product-required registry/RESULT/lifecycle evidence may use separate control-plane commits, never the RED artifact.
  Do not run BUILD, implement production, make tests pass, start mutation, re-author the carrier, open the binding
  refutation, or author/ask for its CALL. Do not add a sixth family, generalized telemetry/observation framework,
  runtime persistence/export/replay, Unity/gameplay/networking, L2, C1, workers, S4, Level/DA/PGG or character work.
  Loopback exists only in test support and consumes the four actual-path raw families; it cannot reconstruct them.
  Compile failures, Arrange failures, direct `VoxelField`/legacy/mirror surrogates, public-count/checksum inference and
  source-text scans are ineligible RED. Any carrier mismatch, required production/public change, authority conflict,
  unavailable required tool or budget overrun is STOP with the exact blocker.

done_when: |
  1. Current product registry legally admits one exact independent RED-FREEZE venue before writes; lifecycle and
     serialized integration are recorded truthfully and do not overlap admitted work.
  2. One immutable RED commit pins carrier `163dffaa5649cc4f9b010a61ba84f4838f974337`; its exact Git manifest/diff is
     tests/test-support only, authored by a fresh non-surface-author, with zero production/public-surface change.
  3. The frozen PLAN obligation inventory is reconciled once: every atomic item is `behavioral-red` or `evidence-only`;
     all five families exercise their actual-path positive, planted-negative/surrogate and passive-observer controls,
     while test-side loopback consumes rather than recreates the four raw families.
  4. The repo-native test command compiles, discovers every intended RED test and fails on missing behavior rather than
     compile/Arrange/harness error. Existing L1a tests remain GREEN on the declared baseline command; test hygiene and
     required repo-native checks are recorded. No test count, prose recipe or named blocker substitutes for output.
  5. HOME names exact RED commit+parent, carrier pin, Git manifest/numstat, fixture/support meaning, test names and
     categories, compile/discovery/failure output, ordinary-suite/hygiene evidence, admission/lifecycle, every
     done_when disposition and all preserved cuts. It reports binding fresh artifact refutation as eligible or the
     exact blocker, but claims neither BUILD nor L1B delivery and authors no successor CALL.

return: |
  Product RED-FREEZE RESULT HOME: status; exact admission/lifecycle; pinned surface commit; exact immutable RED
  commit+parent and tests/test-support-only manifest; obligation-inventory disposition; plain-language fixture and
  test-support meaning; named tests/categories; real compile/discovery/behavior-RED output; ordinary L1a baseline and
  hygiene results; independence evidence; every done_when disposition; cuts and unrelated-track preservation; exact
  fresh-refutation eligibility/blocker. No BUILD, production implementation or full-L1B claim; no successor request.

budget: one focused half-day maximum; stop earlier on authority, carrier, independence, compile, tool or scope mismatch
surface: product-repo Codex session

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-red-freeze-001-call.md
