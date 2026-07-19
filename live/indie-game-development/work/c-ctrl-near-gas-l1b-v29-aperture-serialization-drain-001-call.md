# CALL c-ctrl-near-gas-l1b-v29-aperture-serialization-drain-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-aperture-serialization-route-001)
engineering_contract: 29

goal: |
  Clear the external DEV-SERIALIZATION-APERTURE-RESULT-PENDING blocker by lawfully validating and, if still pending,
  draining/publishing the existing aperture result/review evidence, leaving current dev/main stabilized and making the
  next L1B HANDBACK-PENDING/integration-control stage eligible; otherwise return one exact blocker.

context: |
  This is a control dependency for the same immutable L1B root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29.
  FINAL-RANGE INDEPENDENT REVIEW is `REVIEW GREEN — HBP/INTEGRATION ELIGIBLE` for immutable
  `62db→75e0→4df→T=6fa101b4`; U3 is clean at T tree
  `dc4979f17fbe2445049d599b3196653a0d34a938`. The review found the prior same-wrong loopback finding fixed and
  same-class sweep safe; focused positive 1/1, real NC 1/1, Step fault capture, full 1835/1835, hygiene and check
  are GREEN. No further L1B candidate, test or review work is required before integration control.

  The only known stop is external `DEV-SERIALIZATION-APERTURE-RESULT-PENDING` for existing
  `c-exec-structure-aperture-authority-v1-surface-freeze-001`. Reuse its existing result/review evidence; do not
  reconstruct, redesign, alter its product behavior or invent new aperture product work. Determine current authenticated
  dev/origin-dev/main/origin-main and aperture registry/result state before acting. If already clear, prove it rather
  than repeating publication.

launch:
  lane: A / NearGas core / external serialized-dev aperture control
  venue: WIN-CTRL admitted Target Local -> registry-resolved control venue
  target_local: resolve exact project path, control lease and authorized refs through WIN-CTRL; infer no path/ref here
  machine: PC
  base: current authenticated dev/main and existing aperture result/review evidence
  conflict_surface: aperture registry/lifecycle/result-review publication and serialized refs only; L1B is read-only
  depends_on: final-range L1B REVIEW GREEN and external aperture pending result
  merge_queue: serialized; no L1B integration in this stage
  gates: engineering_contract 29; existing aperture evidence; authenticated ref readback; no L1B delta

boundaries: |
  Do not modify L1B production/test/frozen authority/candidate T, its evidence binding, review/mutation/result paths,
  HBP state or registry row. Do not integrate T, select final H, run mutation/Stryker, Deliver, final-H review, or
  claim L1B integration/release. Do not create a new aperture design, source/test feature, PLAN/spec or owner question.

  Only the minimum already-authorized aperture lifecycle/result/review publication/drain operation is allowed, after
  fresh validation proves it is necessary. Do not force push, reset, discard, overwrite unrelated bytes, broaden to
  unrelated dev work or silently substitute a fresh aperture implementation. A ref/registry/result conflict is a
  blocker, not permission to alter L1B or bypass serialization.

done_when: |
  1. HOME records WIN-CTRL identity, registry-resolved Target Local/control lease, authenticated pre/post dev and main
     refs, clean-state/undeclared-byte proof and exact current aperture registry/result/review disposition.
  2. Existing `c-exec-structure-aperture-authority-v1-surface-freeze-001` result/review evidence is reused and
     mechanically validated. If pending, only its lawful serialization drain/publish actions occur; if already clear,
     evidence proves no duplicate mutation. No L1B path, commit, evidence artifact or registry row changes.
  3. Post-operation readback proves serialized dev/main stability and no remaining aperture result-pending blocker for
     the L1B integration path. Any required publication has exact non-force ref/result readback and named artifact IDs.
  4. HOME returns exactly `APERTURE SERIALIZATION CLEARED — L1B HANDBACK-PENDING/INTEGRATION CONTROL ELIGIBLE`, or
     one complete blocker with current refs, missing evidence/authority and required return stage. It does not mark
     HANDBACK-PENDING itself, integrate T, choose H, run formal final-H review/mutation or claim Deliver.

return: |
  Product APERTURE-SERIALIZATION CONTROL HOME: exact control route/refs/status; reused aperture result/review IDs and
  lifecycle disposition; every permitted publication/drain action and non-force readback; zero-L1B-delta proof; and
  only aperture-cleared eligibility for a separate L1B HANDBACK-PENDING/integration control or exact blocker. No
  L1B integration, final H, mutation, Deliver, owner question or successor CALL.

budget: one bounded WIN-CTRL serialized-control session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-v29-aperture-serialization-drain-001-call.md
