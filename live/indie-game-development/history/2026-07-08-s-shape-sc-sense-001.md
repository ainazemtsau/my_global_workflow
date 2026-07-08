# RESULT s-shape-sc-sense-001 (call: owner continuation from interrupted Claudia/Codex chat)
direction: indie-game-development   play: shape   node/task: g-9c41 / Sc-sense

outcome: |
  The post-Sc-reactions road is re-scoped again: Sc-catalog is parked before firing, and Sc-sense is now the active
  next engineering slice. The ready executor handoff is `work/c-exec-035-sc-sense-call.md`: player actor position/volume
  reads exposure from the authoritative near gas field, integrates integer dose over time, records a separate
  player-kinematics/dose digest, and shows an owner-eye Unity capsule debug readout. Damage, detection gameplay, visuals,
  and new gas-type authoring are explicitly out of scope.

evidence: |
  Owner source:
  - From the interrupted chat: owner prioritised the sensing/dose foundation as «фундаментально точно нужен».
  - Detection/detective axis: owner said «хорошобы заложить это НО пока неделаем так как нет четких требований».
  - Owner-eye actor: owner said «ок и давай за игрока возьиеи обычную капсулу пока».
  - Continuation approval in Codex: owner said «ok работай».

  Artifacts:
  - `live/indie-game-development/work/c-exec-035-sc-sense-call.md` is READY and hardened.
  - `live/indie-game-development/work/c-exec-034-sc-catalog-call.md` is marked PARKED, not deleted, preserving the ready
    type-authoring artifact for later revival.
  - `live/indie-game-development/NOW.md` now has Sc-sense active and `c-exec-035` in open_calls / next.

  Code/canon grounding checked read-only:
  - `knowledge/g9c41-gas-engine-SPEC.md`: input-lockstep = ADR-0002; what bites/triggers reads the authoritative shared
    field, not private detail; §4 seam 7 names a separate player-kinematics hash before first forceful player mechanic.
  - Product code anchors read read-only from the available GasCoopGame_dev_2 working copy for name grounding: the coarse
    read-model files carry the banner `INTERIM far-tier ... DO NOT add new dependencies`; near field exposes
    `VoxelField.ConcentrationAt(cell, species)`, `DominantTypeIdOrEmpty`, and `CellGrid.TryGetCellAt`; current
    `MeaningMembers` ends at `TypeId = 1 << 5`; current `TickInput` is `tick/peerId/command/arg`, so the CALL requires
    an explicit input schema decision instead of opaque bit-packing. The executor still must re-sync against the target
    GasCoopGame main/dev tip before PLAN.

state_changes: |
  NOW.md:
  - updated: `2026-07-08 by s-shape-sc-sense-001`.
  - bet.goal road changed from `... Sc-reactions → Sc-catalog → Sc-damage` to
    `... Sc-reactions → Sc-sense → Sc-damage`; Sc-catalog/type-authoring is PARKED until canon gives a real roster.
  - task `Sc-catalog`: status `active` → `parked`; done_when now points to the preserved ready artifact
    `work/c-exec-034-sc-catalog-call.md` and says it returns when roster/authoring need is real.
  - task `Sc-sense`: added as `active` with goal/done_when matching `c-exec-035`.
  - open_calls: removed `c-exec-034`; added `c-exec-035` for `g-9c41 / Sc-sense`.
  - next: changed from `CALL c-exec-034` to `CALL c-exec-035` with pointer
    `work/c-exec-035-sc-sense-call.md`; parallel tracks preserved.

  work/:
  - `work/c-exec-035-sc-sense-call.md`: READY hardened; key hardening folded:
    separate player-kinematics/dose digest; accumulated dose folded now; gas `MeaningChecksum` no-regression preserved;
    no opaque one-int actor-input crutch; Unity capsule quantizes at adapter boundary; no mutable `_near` escape.
  - `work/c-exec-034-sc-catalog-call.md`: status banner changed to PARKED/not fired; artifact preserved.

  LOG.md:
  - appended one line for `s-shape-sc-sense-001`.

  history/:
  - saved this RESULT as `history/2026-07-08-s-shape-sc-sense-001.md`.

captures: []

decisions_needed: []

play_check:
  - 1 Recite: done — g-9c41 remains the active gas-core node; parent/root still requires a shipped co-op gas/grid expedition game, not a tech demo.
  - 2 Appetite first: done — appetite stays within the existing g-9c41 rolling-wave wall; no silent bet extension.
  - 3 Approaches, then minimal solution: done — compared Sc-catalog/type-authoring vs Sc-sense/foundation; owner prioritised sensing as canon-independent foundation.
  - 4 Scope hammer: done — cut damage/consequence, detection gameplay, visuals, new gas types, catalog/type-authoring, env-derived typing, and real player-controller/network-player breadth.
  - 5 Lens sweep: done — commercial/traction justified only as anti-private-tunnel owner-eye capsule; gameplay-depth yes as first player↔gas consequence substrate; co-op-first socketed via multi-actor/rescue later, not built; technical-feasibility is the top risk via lockstep/digest/dose; scope lens passes via explicit cuts; audience workflow not needed now beyond future-readable debug evidence.
  - 6 Riskiest assumption: done — top risk is deterministic lockstep-safe dose from actor position + authoritative near gas, with separate player-kinematics/dose digest.
  - 7 Tasks: done — one executor CALL `c-exec-035` prepared; PLAN and BUILD remain separate v19 sessions with independent RED test-author first in BUILD.
  - 8 Kill criteria: done — governed by existing g-9c41 de-risk wall and 2026-07-24 visible-gas milestone; slice stops/re-shapes if actor/dose/digest proves too large or not deterministic.
  - 9 Close: done — owner approved continuation with «ok работай»; NOW now points to c-exec-035.

log: |
  shape/re-scope Sc-sense: parked Sc-catalog c-exec-034, hardened Sc-sense c-exec-035, next = c-exec-035

next: |
  CALL c-exec-035 → executor (GasCoopGame_dev): `work/c-exec-035-sc-sense-call.md`. Fresh owner-present PLAN under
  contract v19, then a separate BUILD session with independent RED test-author first. Return RESULT HOME; dev→main merge
  + push owner-gated.

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-shape-sc-sense-001.md
