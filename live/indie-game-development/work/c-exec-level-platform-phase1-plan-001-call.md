# CALL c-exec-level-platform-phase1-plan-001 — Generic 3D Level/Module Contract + Validation Platform (PLAN ONLY)

> **STATUS: PREPARED, NOT ISSUED, BLOCKED.** Do not dispatch before `c-exec-lv-ingest-phase0-001` is DELIVERED,
> owner-gated and MERGED into `origin/main`. This artifact is not an active `NOW.open_call` and does not authorize
> RED tests, product code, Unity assets or BUILD.

> ⚠️ contract: drift-unknown — the GasCoopGame `validation.config` stamp was unreadable from the Direction-bound
> session that authored this parked CALL. Current OS engineering contract = v19. At dispatch, read the product stamp,
> perform §Re-sync if behind, and record the exact post-Phase-0 base before any mutation.

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame
node: g-9c41
task: Lv-ingest / Phase 1 platform PLAN
goal: |
  Существует одобренный владельцем и замороженный исполнимый план независимой от генератора 3D-платформы
  уровней/модулей, по которой простые комнаты можно принимать сейчас, а будущие вертикальные compound-модули —
  добавлять без замены базовой модели; каждый принятый модуль и собранный уровень имеет проверяемую точную
  topology/structure truth и расширяемые типизированные level features.
context: |
  Owner verdict on 2026-07-11: `A`. Ratified phase boundary:
  - Phase 0 closes only the existing generator-blind built-scene + authoritative GasSource seam.
  - Phase 1 is the technology-neutral 3D Level/Module Contract and validation platform.
  - Phase 2 is DA SnapGridFlow runtime composition, PGG editor-time bake/import, optional library adapters and the
    shared seed/normalized manifest hash handshake.
  - Phase 3 is production module content and typed feature/vertical-content expansion through Phase 1 seams.

  Standing owner requirement: future levels are vertical; a placed module may contain 1:N logical rooms at different
  heights, including routes through upper floors. Reserve this now with a tiny stacked-room proof, but do not build the
  illustrative 80x80x20-40 m content, traversal or streaming now. Module is a placement/bake container; room/region is
  topology/gas truth. Connections and apertures must be expressible across +/-X, +/-Y and +/-Z.

  Read as input evidence, not as a binding architecture spec:
  - C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\level-platform-phasing-2026-07-11.md
  - C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md
  - C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-da-level-ingestion-plan.md
  - C:\projects\Unity\GasCoopGame_pgg_spike\docs\results\c-spike-pgg-001.md
  - C:\projects\Unity\GasCoopGame_dev\docs\results\c-exec-lv-ingest-phase0-001.md

  The PGG spike proved static prefab -> SnapGridFlow -> BuiltSceneRoomReader but failed the production stage because
  AABB occupancy, door-kit bounds, socket count and item metadata are not a project contract. The lower engine already
  has useful generator-neutral integer topology/voxelization pieces. Preserve compatible proven seams; do not assume
  the current vendor-shaped reader or provisional names are the final design.
boundaries: |
  PLAN ONLY and owner-present. Stop after owner approval of a detailed, plain-language technical plan plus frozen
  machine artifacts. No RED test commission, code, refactor, package import, prefab/scene/asset creation, Unity build,
  DA/PGG adapter, library conversion, or runtime handshake in this session.

  Do not make DA, PGG or a library asset format authoritative. Do not standardize around the spike prefab. Do not
  collapse module=room, approximate irregular floor by a full AABB, derive an aperture from whole Door-kit bounds, or
  create an untyped universal metadata bag. Do not expand TopologyDocument into all gameplay payloads without an
  explicit compatibility decision.

  Defer giant vertical content, production stairs/ladders/elevators, navigation, streaming/occlusion policy, arbitrary
  vertical destruction and content-tool polish. Do not silently exceed the active bet's maximum 13 product legs: if
  the honest Phase 1/2 split does not fit, return explicit cuts/deferrals and an owner decision instead of extending.
done_when: |
  1. Preflight records the exact fresh `origin/main` containing the MERGED Phase 0, reconciles Phase 0's actual
     delivered contracts/tests against this CALL, reads the current product run-contract/version and records any
     required §Re-sync before planning from the code as it exists.
  2. One detailed but simple owner-readable plan spells out every major technical decision and why. Alongside it,
     frozen product artifacts under one named change id record requirements, ADRs/interfaces, acceptance properties,
     task ledger, dependency order, cuts and migration/compatibility notes.
  3. The plan chooses exact project-owned representations and names for reusable module authoring truth and normalized
     built-level truth. It defines ownership, schema/profile versions, deterministic identities, local-to-world
     normalization and the boundary from normalized output to existing TopologyDocument/Voxelizer/GasSource seams;
     alternatives rejected are named with reasons.
  4. The model is full integer 3D and preserves 50 cm gas cells plus 25 cm structure/placement truth. It supports one
     module instance -> 1:N stable logical rooms/regions, separate internal room connections and external sockets,
     an external socket's owning internal room, six-direction connection/aperture planes, and deterministic global ids
     derived from module instance + local ids. The plan explicitly decides what Phase 1 implements versus merely
     represents for Z-normal apertures; a wall-only data model is not allowed.
  5. The plan chooses a deterministic exact-geometry truth path for irregular occupancy and door apertures, keeping a
     coarse room/envelope view distinct from exact near-grid structure. It states how declared 25 cm occupancy,
     clearance and aperture placement are independently checked against built geometry/colliders rather than trusted.
  6. Validation responsibilities and machine-readable diagnostics are defined at four boundaries: reusable module,
     adapter/bake normalization, assembled built level, and existing engine admission. Acceptance covers off-grid
     frames/pivots/envelopes, role/socket rules, connection clearance, gap/overlap/profile mismatch, duplicate/unstable
     ids, dropped vendor information, exact occupancy/apertures, anchors/features, deterministic repeat builds and
     loud rejection of unknown authoritative kinds.
  7. Extensibility separates structural truth from gameplay payload and WHERE from WHAT. The plan decides the typed
     anchor/feature catalog or registry seam, full 3D orientation/ownership/versioning, and how GasSource, item/player
     spawn, machine, valve, loot or later feature specs extend the platform without vendor special cases or an untyped
     bag. Cosmetic-only ignore behavior, if any, is explicit and cannot swallow authoritative data.
  8. The frozen acceptance design contains a simple horizontal control plus a minimal compound module with two logical
     rooms at different Z and one internal vertical connection. Generator-neutral one-, two-, three- and four-module
     configurations verify exact occupancy, aperture position/size, internal/external connection ownership, anchor
     resolution and same-input manifest/hash determinism. These are contract/validator fixtures, not production art,
     traversal or proof of DA runtime generation.
  9. The plan names the adapter boundary for hand-authored modules, DA, PGG and optional library imports, while leaving
     their implementation in Phase 2. PGG runtime components/vendor state cannot leak past bake; a library module that
     cannot normalize is rejected or wrapped outside authority rather than special-cased in Core.
  10. A minimal ordered BUILD split is proposed within the current 13-leg maximum, with each later session's outcome,
      conflict surface, executable evidence and stop/kill condition. Phase 1 contract/validator work is separated from
      Phase 2 vendor/runtime work and Phase 3 content. Any appetite conflict is surfaced for owner choice.
  11. Review evidence exists at `docs/reviews/review-<change-id>.md` with all findings dispositioned and refutation
      markers/register lines required by the current contract. The owner gives actual approval words for the readable
      plan. The session then stops and returns proof that no RED tests, product code/assets or BUILD were started.
return: |
  RESULT with exact base/contract version; owner-readable plan and frozen change/spec/ADR/task paths; chosen decisions
  and rejected alternatives; full-3D/cardinality/id/geometry/feature-extension model; validator and fixture acceptance
  matrix; Phase 1/2/3 boundary; minimal BUILD split and 13-leg accounting; review-evidence path; commit; owner's actual
  approval words; and explicit no-RED/no-BUILD proof. Never author or start the BUILD in this product PLAN session.
budget: one owner-present PLAN session; STOP at plan approval

launch:
  lane: D
  venue: C:\projects\Unity\GasCoopGame_levels (levels branch/worktree; create or verify only after Phase 0 MERGED)
  machine: PC; Unity Editor is not required for PLAN
  base: fresh origin/main containing the MERGED c-exec-lv-ingest-phase0-001; capture exact SHA at dispatch
  conflict_surface: product plan/spec/ADR/review artifacts only; BUILD conflict surface is decided, not touched
  depends_on: [c-exec-lv-ingest-phase0-001 DELIVERED + owner-gated + MERGED]
  merge_queue: none for PLAN; later BUILD slots are proposed within the existing 13-leg appetite
  gates: owner-present plan approval + current-contract review evidence; BUILD and binding fresh G5 remain later sessions

END_OF_FILE: live/indie-game-development/work/c-exec-level-platform-phase1-plan-001-call.md
