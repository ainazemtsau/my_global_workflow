# CALL c-exec-level-module-standard-v1-lv0-plan-001

to: executor
direction: indie-game-development
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: Level-LV0-PLAN
issued: 2026-07-16 (s-repair-level-lv0-parallel-launch-001)
parent: s-repair-level-lv0-parallel-launch-001

goal: |
  Level/Module Standard v1 имеет owner-approved current-product LV0 PLAN, который превращает принятую
  архитектурную основу D1=A / D2=A в однозначный ограниченный контракт для последующей отдельной LV1/LV2
  реализации, не открывая BUILD.

context: |
  Владелец принял `work/level-module-standard-v1-candidate-2026-07-16.md` как архитектурную основу, выбрал
  D1=A (canonical sparse 25 cm cell/sub-face structural truth с измеримым size/time ceiling) и D2=A
  (представлять и валидировать +/-Z сейчас, а неподдержанный engine admission завершать громким отказом).
  Это обязательные Direction constraints; точные product-facing решения ещё не заморожены.

  В отдельном owner directive владелец уточнил dispatch semantics: текущие `NOW.bet`/`NOW.next` задают
  приоритетный маршрут, а не глобальный запрет на другие линии; Level/DA/PGG должен стартовать параллельно,
  начиная с этого LV0 PLAN. NearGas, extraction, character и остальные линии сохраняют собственное состояние.

  LV0 обязан явно заморозить ровно восемь названных тем: canonical encoding, shared-surface ownership,
  socket terminal states, transform rules, deterministic build input, registries/versioning, sampler authority
  и size/time ceiling. Preserve уже доказанные lower seams, Project Module Contract + Built Level Manifest shape,
  four-boundary validator/fixture package, PGG editor-only cleanup boundary и old-task ledger; не проектировать
  стандарт заново без конкретного current-product конфликта.

  Current dispatch authority: `work/gascoopgame-worktree-protocol-v2.md`. GasCoopGame root `AGENTS.md`, current
  product contract/registry and committed pre-write admission own venue, lifecycle worktree, branch and integration.
  Direction не назначает physical path, branch или SHA. Published product main/dev@5cd18250 is prior evidence,
  never a launch pin; re-read current product authority before any docs write and STOP on a real conflict.

  Old `Lv-ingest`, Phase 0, fixed lane-D/`GasCoopGame_levels` assignment and
  `c-exec-level-platform-phase1-plan-001` are obsolete/NEVER RESUME/NEVER ISSUE evidence only.

boundaries: |
  PLAN session only, owner present. No production source, public carrier, tests/test-support, package, prefab,
  scene, module asset, DA adapter, PGG baker/importer, Unity import, Unity Editor, SURFACE-FREEZE, RED-FREEZE,
  BUILD, common M1 scene or integration mutation. Do not revive Phase 0 or patch the superseded PLAN.
  Do not change D1/D2 or weaken exact 1:N full-3D truth without a new explicit owner verdict. Do not silently
  coerce/drop +/-Z, use vendor/Unity objects as authority, make runtime PGG, or introduce a universal metadata bag.
  Product-owned admission may choose the legal planning venue; this CALL must not prescribe a local path/branch/SHA.
  Missing current authority, unavailable required evidence, scope growth or an irreconcilable lower-API conflict = STOP.

done_when: |
  1. A current-product LV0 planning package is committed, internally consistent and owner-readable; it names the
     exact current product authority/admission used and records the owner's actual final PLAN approval words.
     Without those words, return an honest PLAN checkpoint and keep this CALL open.
  2. Canonical encoding is frozen down to versioned semantic bytes/order/hash, sparse 25 cm cell/sub-face identity,
     diagnostics/provenance exclusions and a measured size/time ceiling with a STOP condition.
  3. Shared-surface ownership, socket lifecycle/terminal states and integer transform rules are unambiguous for
     internal/external boundaries, +/-X/+/-Y/+/-Z, legal yaw/handedness, room ownership and aperture preservation.
  4. Deterministic build input, ids, registries/versioning and independent sampler authority are frozen with loud
     unknown/unsupported behavior and repeatability/negative-fixture evidence expectations.
  5. The PLAN maps Project Module Contract and Built Level Manifest into the proven lower topology/aperture/
     voxel/typed-feature seams, preserves the four validator boundaries and defines the smallest LV1/LV2 probe;
     unsupported vertical engine admission remains an explicit named refusal, never a structural validation failure.
  6. Every cut remains explicit. Repo-native docs/plan/spec/ledger/result checks and hygiene are GREEN; Unity is
     not launched and implementation is untouched. Only after owner approval may the product RESULT propose one
     separate LV1/LV2 implementation handoff; it does not launch SURFACE-FREEZE, RED or BUILD or author a new
     Direction CALL itself.

return: |
  Product LV0 PLAN RESULT HOME: status; owner verdict words; exact commits and docs-only diff; current-authority
  and pre-write admission evidence; frozen disposition for all eight required topics; D1/D2 and lower-seam
  reconciliation; cuts; checks; one legal separate LV1/LV2 handoff or exact BLOCKED reason. No implementation claim.

budget: one focused half-day maximum; stop at owner approval or earlier on scope/authority conflict
surface: owner-present

END_OF_FILE: live/indie-game-development/work/c-exec-level-module-standard-v1-lv0-plan-001-call.md
