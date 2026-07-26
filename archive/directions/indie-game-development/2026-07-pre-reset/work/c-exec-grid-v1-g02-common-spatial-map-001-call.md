# CALL c-exec-grid-v1-g02-common-spatial-map-001

to: executor
direction: indie-game-development
track: grid
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-4b92
task: G02-COMMON-SPATIAL-MAP
issued: 2026-07-22 (s-work-grid-v1-g01-direct-legacy-release-001)
engineering_contract: 31

goal: |
  Grid V1 has one released engine-free common spatial map whose integer base lattice, positive integral scale,
  address, half-open region and canonical projection let the existing 25 cm Structure and 50 cm Gas coordinate paths
  describe equivalent space without transferring their state or behavior into Grid.

context: |
  Read fresh product authority first. G01 is binding-reviewed and published at product dev/main
  `1a6373b84b6bf4da95a24efc3015e23b9ba5d419`; the exact twelve legacy normative files are absent and the nine current
  authority paths are active. Direction authority is `work/grid-v1-executor-plan.md` exact accepted blob
  `2c95e10fd9261da0dfdbc0eab1522dd85f6001cf`, especially G02 and the serial G01→G02 route, plus
  `history/2026-07-22-s-work-grid-v1-g01-direct-legacy-release-001.md`. The owner's one-time direct-release waiver was
  only for G01 cleanup and does not waive this root's PLAN, review, test or Deliver gates.

boundaries: |
  Owner-present detailed product PLAN before implementation. No implementation or downstream lifecycle stage before
  the owner's actual PLAN verdict. Keep existing Gas/Voxel and Structure state, ownership and behavior read-only;
  G02 is an additive neutral addressing contract plus equivalence proof, not state migration. Do not reopen deleted or
  historical Grid documents, change G01 authority, repair workflow, add consumer behavior, run G03+, touch Unity
  scenes/assets, or claim Gas/Wind/Character/Level/Multiplayer/Integration delivery.

done_when: |
  1. The owner has accepted a complete plain-language product PLAN that names the gameplay/program value, exact current
     source surfaces, public contract, proof strategy, rollback and cuts.
  2. The released map uses integer coordinates and positive integral scales, defines half-open regions and canonical
     projection/enumeration, and rejects invalid scale, overflow and non-canonical inputs deterministically.
  3. Runnable proofs cover round trips, negative coordinates, boundaries, overflow, invalid scales, canonical
     enumeration and 25 cm/50 cm equivalence without moving existing state.
  4. Existing Gas/Voxel and Structure behavior remains unchanged and no downstream Grid leg or real consumer adapter
     is opened or claimed.
  5. The exact result passes ordinary contract-31 review, evidence and release gates and is published/read back on the
     canonical product refs, or returns one exact honest blocker.

return: |
  Gated RELEASED HOME with owner PLAN words, exact product identities, diff, proof results, review evidence, preserved
  boundaries and release readback; or one exact ESCALATE. No successor Direction CALL.

budget: one bounded G02 product root
surface: owner-present PLAN, then fresh product sessions

END_OF_FILE: live/indie-game-development/work/c-exec-grid-v1-g02-common-spatial-map-001-call.md
