# RESULT — s-research-level-platform-phasing-001 (2026-07-11)

session: s-research-level-platform-phasing-001 (Codex; play: research; checkpoint awaiting owner phase verdict)
direction: indie-game-development / g-9c41 / Lv-ingest phases

## Owner summary

Phase 0 — не «первая половина Dungeon Architect», а уже построенный вертикальный proof независимого шва:
простая built scene → integer topology/grid, placed `GasSourceMarker` → `GasSourceSpec`, continuous injection →
authoritative step/checksum. Он намеренно не решает production module contract, irregular occupancy, exact apertures,
items, validators или runtime DA handshake.

Текущая Phase 1 слишком широкая и стоит в неправильном порядке: она одновременно обещает настоящие DA-модули,
runtime build, seed/ProfileHash и «тот же reader без изменений». PGG-спайк опроверг последний premise. Рекомендация:
Phase 1 переопределить как generator-neutral Level/Module Contract + validation platform; старую DA/PGG integration
перенести в Phase 2; production modules/features — в Phase 3. Альтернатива с меньшим rename-churn — Phase 1A/1B.
Ничего не ратифицировано без owner verdict; primary `NOW.next` остаётся Phase 0.

```text
RESULT s-research-level-platform-phasing-001 (call: owner-plain-level-phasing-2026-07-11)
direction: indie-game-development   play: research   node/task: g-9c41/Lv-ingest-phases
outcome: |
  CHECKPOINT / AWAITING OWNER VERDICT. Phase 0 и заявленная Phase 1 разведены по ответственности; найдено, что
  нынешняя Phase 1 объединяет generic contract, vendor adapters и runtime integration в неправильном порядке.
  Подготовлен research brief work/level-platform-phasing-2026-07-11.md. Recommended architecture: project-owned
  Module Contract → ModuleValidator → normalized Built Level Manifest → BuiltLevelValidator → engine-free
  TopologyDocument/exact structure/typed feature specs → Voxelizer/sim. Recommended phasing: Phase 1 generic
  contract+validators; old DA/PGG Phase 1 becomes Phase 2 adapters/runtime; Phase 3 production extensions/content.
  No phasing/canon/CALL has been ratified or opened; primary NOW.next remains Phase 0 close.
evidence: |
  Direction sources: work/c-exec-lv-ingest-phase0-call.md and knowledge/g9c41-da-level-ingestion-plan.md define
  Phase 0 as hand-tagged geometry + authoritative gas-source seam and old Phase 1 as real SGF modules/flow,
  LevelBootstrap, shared seed/ProfileHash and unchanged reader/seeder. history/2026-07-11-s-spike-pgg-001-close-001.md
  records production FAIL_STAGE and exact occupancy/aperture/anchor gaps.
  Product code inspected read-only at GasCoopGame_dev@991ca1ed: TopologyDocument/ITopologyProducer and Voxelizer are
  generator-agnostic; DaLevel/IDaRoomReader/DaTopologyProducer retain vendor-shaped names; BuiltSceneRoomReader emits
  one AABB RoomSpec per module and derives only vertical opening size from an active Door kit; SceneTopologyComposer
  emits Array.Empty<TopologyAnchor>(). ApertureSpec represents a 25 cm rectangle, but StructureVoxelizer validates it
  against the shared region boundary rather than independently proving the actual mesh hole. TopologyConformance is
  an engine admission gate, not a prefab/module validator.
  Canon evidence: knowledge/g9c41-gas-engine-SPEC.md and work/gas-engine-layered-reshape-R1-2026-06-26.md require
  50 cm gas + 25 cm structure, project-module geometric markers, and independent mesh→sub-face re-derivation;
  trusting declared geometry is explicitly a forbidden substitution.
  Established: responsibilities/gaps above and the dependency contract-before-adapters. Inference needing PLAN:
  provisional names/container split, occupancy-mask vs rectangular-decomposition representation, and exact typed
  feature registry design. review: n/a — research-only, no product or canonical architecture change.
state_changes: |
  ADD work/level-platform-phasing-2026-07-11.md as a non-canonical research brief.
  live/indie-game-development/NOW.md: set updated to
  `2026-07-11 by s-research-level-platform-phasing-001`; UPSERT pending decision id
  `d-level-platform-phasing-001` with the three options/recommendation below; preserve bet, tasks, open_calls,
  all existing decisions, recurring and primary `next` exactly as current.
  live/indie-game-development/LOG.md: append exactly the `log:` line below once.
  live/indie-game-development/work/board/dashboard.html: add d-level-platform-phasing-001 to the owner batch and
  add this checkpoint to the 2026-07-11 journal; preserve all other live/historical sections.
  Save this full RESULT once at
  live/indie-game-development/history/2026-07-11-s-research-level-platform-phasing-001.md.
  No CHARTER.md, TREE.md, knowledge canon, task status, open_call, product repo or NOW.next change.
captures:
  - Two normalized contracts are needed: a reusable project Module Contract and a post-composition Built Level
    Manifest; DA/PGG/library inputs normalize into them instead of leaking vendor special cases into Core.
  - Validation is layered: ModuleValidator before registration, vendor adapter/bake conformance, BuiltLevelValidator
    after composition, then existing TopologyConformance/Voxelizer engine admission.
  - Extensibility should split WHERE (`LevelAnchor`) from WHAT (typed GasSource/ItemSpawn/PlayerSpawn/Machine/Valve/
    LootSocket specs); do not turn TopologyDocument into an untyped universal payload bag.
  - Irregular rooms need coarse region/envelope truth plus exact 25 cm structure occupancy; one renderer AABB cannot
    serve both far topology and near-grid geometry.
decisions_needed:
  - q: d-level-platform-phasing-001 — choose the level-platform phasing after Phase 0.
    options: ["A: clean rephase — Phase 1 contract/validators; old Phase 1 becomes Phase 2 adapters/runtime; Phase 3 production extensions/content", "B: keep numbering — Phase 1A contract/validators; Phase 1B adapters/runtime; Phase 2 production", "C: keep current Phase 1 unchanged and add the standard later"]
    recommendation: "A, because the generic contract and validators are prerequisites for real DA/PGG modules; C repeats the spike's build-before-contract failure, while B is viable only as a naming-conservation choice."
play_check:
  - 1 Recite: done — bounded question = explain Phase 0/current Phase 1, test overlap, and recommend Phase 1 revision vs later phase; return = readable architecture/phasing brief within one session.
  - 2 Investigate: done — inspected current direction CALL/knowledge/canon, PGG terminal evidence, and live product contracts/readers/validators at dev@991ca1ed; no web or product writes needed.
  - 3 Confidence: done — separated code/canon facts from provisional naming/data-model inferences and named the PLAN decisions that could change the recommendation.
  - 4 Close: done as checkpoint — human brief + work artifact + one batched owner decision; no phasing or downstream CALL ratified before owner words.
log: 2026-07-11 — research/checkpoint (g-9c41/Lv-ingest phases, s-research-level-platform-phasing-001): Phase 0/1 overlap проверен по live code и канону; premise текущей Phase 1 «тот же reader без изменений» устарел, поэтому generator-neutral Level/Module Contract + validation platform рекомендованы перед DA/PGG adapters. Открыто d-level-platform-phasing-001; primary next остаётся закрытием Phase 0. → history/2026-07-11-s-research-level-platform-phasing-001.md
next: |
  awaiting_decision d-level-platform-phasing-001; primary direction next remains
  work/c-exec-lv-ingest-phase0-call.md. On owner A/B verdict, a fresh session revises the phase contract and authors
  the PLAN-only executor CALL; no BUILD starts from this checkpoint.
```

END_OF_FILE: live/indie-game-development/history/2026-07-11-s-research-level-platform-phasing-001.md
