# CALL c-ctrl-near-gas-l1b-v29-handback-integration-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-handback-integration-route-001)
engineering_contract: 29

goal: |
  Make the reviewed immutable L1B correction the exact integrated dev ancestor and record the final integrated H,
  leaving only formal final-H review, mutation and closing-evidence eligibility.

context: |
  Same root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29. Aperture serialization is cleared: external
  `c-exec-structure-aperture-authority-v1-surface-freeze-001` is PRESERVED-PAUSED; incomplete active RESULT was
  withdrawn losslessly. Carrier `3bbbc4c`, review/result commit `06b8a6e2`, review blob `00704214` and result blob
  `cdc17e5` remain preserved; U4 is clean, detached at `5af1d8db`, lease-free and unchanged. Aperture repair commit
  `8d7d8f859232a8c585d6b3586d5cf9102451ed02` is non-force published:
  `dev == origin/dev == 8d7d8f859232a8c585d6b3586d5cf9102451ed02`; `main == origin/main == 029279a7`.
  Result-check and normal check are GREEN, 1792/1792; zero L1B delta occurred.

  Exact reviewed L1B lineage is `62db → 75e0 → 4df54a2b024d6c95e4c7095da4018ce4e2cc2dad →
  T=6fa101b4ad8011598e18567c6a97428cd78f340c`; final T tree is
  `dc4979f17fbe2445049d599b3196653a0d34a938`. T directly follows BUILD, changes exactly three approved test files,
  and final-range independent review is GREEN. Focused real positive/NC, hygiene/check and full T 1835/1835 are
  GREEN. Implementation evidence id remains `c-exec-near-gas-l1b-pair-candidate-001`; its binding/tooling was N/A
  until dev ancestry and must become active through this integration, without changing its evidence design.

launch:
  lane: A / NearGas core / serialized handback and dev integration
  venue: WIN-CTRL admitted Target Local -> registry-resolved control venue
  target_local: resolve exact project path, control lease, clean dev venue and authorized refs through WIN-CTRL; infer no path/ref here
  machine: PC
  base: authenticated clean dev/origin-dev `8d7d8f859232a8c585d6b3586d5cf9102451ed02` and main/origin-main `029279a7`
  conflict_surface: L1B registry lifecycle, exact immutable lineage reachability, dev integration, root-binding and integration checks only
  depends_on: APERTURE SERIALIZATION CLEARED and FINAL-RANGE L1B REVIEW GREEN
  merge_queue: serialized; this is the sole L1B integration stage
  gates: engineering_contract 29; HANDBACK-PENDING readback; exact T ancestry; clean dev; core/hygiene/full checks; active root-binding; non-force dev readback

boundaries: |
  Transition only this L1B correction root to HANDBACK-PENDING using exact T and final-review identities. Integrate
  exact immutable T into current dev while preserving T as an ancestor: no cherry-pick, rebase, squash, rewrite or
  candidate edit. A conflict is a blocker unless byte-exact product authority explicitly permits its resolution; then
  record that authority, paths and preservation proof. Do not run mutation/Stryker, formal final-H review, L1B RESULT,
  closing evidence, Deliver or main publication. Do not alter aperture preservation, PLAN/spec/design, frozen carrier/RED/
  BUILD/T bytes, unrelated dev work, or ask the owner.

done_when: |
  1. HOME records WIN-CTRL identity, registry-resolved Target Local/control lease, preflight clean dev/origin-dev and
     main/origin-main refs, and legal transition of `c-exec-near-gas-l1b-pair-candidate-001` to HANDBACK-PENDING
     pinned to exact T and final-review identities.
  2. Current clean dev integrates exact T with `6fa101b4ad8011598e18567c6a97428cd78f340c` as an ancestor; immutable
     candidate manifests/bytes are unchanged. Any conflict has either explicit byte-exact authority and proof or
     returns as the exact blocker.
  3. Core, hygiene and full checks run on the final integrated dev state with exact commands/counts recorded; exact
     integrated H is selected only after those checks and active root-binding/tooling readback for implementation id
     `c-exec-near-gas-l1b-pair-candidate-001`.
  4. H is committed/pushed non-force and authenticated post-readback proves `dev == origin/dev == H`; main remains
     unchanged unless existing product authority independently requires and records otherwise. No mutation, review,
     RESULT, Deliver or publication is claimed.
  5. HOME returns exactly `FINAL INTEGRATED H — FORMAL REVIEW/MUTATION/CLOSING EVIDENCE ELIGIBLE`, naming H, ancestry,
     lifecycle, checks and root-binding, or one complete blocker.

return: |
  Product L1B HANDBACK/INTEGRATION CONTROL HOME: Target Local/lease and authenticated refs; exact HBP transition;
  T ancestry and immutable-manifest proof; exact integrated H; check/count and active root-binding readbacks; non-force
  dev push/readback; and only the exact final-H eligibility phrase or one blocker. No mutation, final-H review, RESULT,
  Deliver, main publication, owner relay or successor CALL.

budget: one bounded WIN-CTRL serialized handback/integration session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-v29-handback-integration-001-call.md
