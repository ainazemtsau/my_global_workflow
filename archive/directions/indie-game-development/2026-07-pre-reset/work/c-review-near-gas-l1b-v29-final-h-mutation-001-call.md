# CALL c-review-near-gas-l1b-v29-final-h-mutation-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-final-h-review-mutation-route-001)
engineering_contract: 29

goal: |
  Produce fresh independent formal review and mutation evidence bound to final integrated H, establishing only
  closing-control eligibility for the immutable L1B implementation root.

context: |
  Same root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29. Final integrated
  `H=bf76fa68183f186190a2d6221a241a0b48b975e1`; `dev == origin/dev == H`; main/origin-main is
  `029279a7a03af5869f32ddbb8b93aa49f2c6183f`. Exact
  `T=6fa101b4ad8011598e18567c6a97428cd78f340c` is an H ancestor; six frozen candidate blobs are exact. The sole
  dashboard control-plane conflict was resolved by preserving its authorized current-dev blob and recorded in the
  registry; no candidate edit occurred. At H: core build, hygiene, normal check 1813 and full suite 1915 are GREEN.
  Root binding is ACTIVE and pending this formal root review, reviewer mutation and root RESULT. No Deliver or main
  publication has occurred.

  Prior final-range review was GREEN, but this stage is the fresh non-author integrated-H review and must account for
  the full guarded H ancestry, exact frozen lineage `62db→75e0→4df→T`, the authorized control-plane resolution and
  their registry proof. Canonical implementation evidence paths are:
  `docs/reviews/review-c-exec-near-gas-l1b-pair-candidate-001.md`,
  `docs/measurements/mutation-c-exec-near-gas-l1b-pair-candidate-001.json`, and
  `docs/results/result-c-exec-near-gas-l1b-pair-candidate-001.md`.

launch:
  lane: A / NearGas core / fresh final-H review and reviewer mutation
  venue: WIN-CTRL admitted Target Local -> registry-resolved independent reviewer venue
  target_local: resolve exact clean reviewer path, lease and artifact custody through WIN-CTRL; U3 is forbidden and no path/ref is inferred here
  machine: PC
  base: authenticated final integrated H `bf76fa68183f186190a2d6221a241a0b48b975e1`
  conflict_surface: read-only H review/mutation evidence only; canonical review/mutation bytes are handed back for later control commit
  depends_on: FINAL INTEGRATED H, ACTIVE root binding, final-range review GREEN and exact frozen ancestry
  merge_queue: no evidence commit, Deliver or publication in this stage
  gates: engineering_contract 29; fresh non-author reviewer; Reviewed-commit=Mutation-reviewed-commit=H; same-class/G5/fix-class sweep; required tests; mutation provenance and configured score floor

boundaries: |
  Reviewer owns the review and mutation evidence, not candidate/product changes. Do not reopen design, edit carrier/RED/
  BUILD/T or any candidate blob, alter registry/control-plane state, integrate, write root RESULT, Deliver, publish main,
  or ask the owner. Do not run mutation in U3. Run mutation at H with
  `./pwsh.cmd tools/mutation.ps1 -ChangeId c-exec-near-gas-l1b-pair-candidate-001` before any mutation-input delta;
  no post-H mutation-input change is permitted. Preserve exact evidence bytes and hashes for the later control commit;
  do not commit them in this review stage.

done_when: |
  1. A fresh independent non-author review binds `Reviewed-commit=H`, inspects the full guarded integrated range and
     exact frozen blobs, verifies prior loopback fix at H, performs same-class/G5/fix-class sweep and required tests,
     and creates complete canonical review content with every finding disposition/refutation marker required by tooling.
  2. Reviewer runs real mutation at exact H with `Mutation-reviewed-commit=H`, records command, input/provenance,
     configured score floor and outcome in canonical JSON. Any floor/provenance/tool failure returns a blocker; no
     candidate edit or mutation-input delta may mask it.
  3. If GREEN, HOME returns the exact canonical review and mutation JSON bytes plus hashes/blob identities, H bindings,
     review finding/sweep dispositions, test/mutation outputs and active root-binding readback, ready for a separate
     WIN-CTRL evidence-commit/Deliver close. If not GREEN, return one exact blocker with preserved H and no mutation.
  4. HOME returns only `FINAL-H REVIEW/MUTATION GREEN — CLOSING CONTROL ELIGIBLE`, or one complete blocker. It does not
     commit evidence, write RESULT, Deliver, publish dev→main or release the root.

return: |
  Product FINAL-H INDEPENDENT REVIEW/MUTATION HOME: independent reviewer identity/venue; H and frozen-ancestry proof;
  canonical review bytes/hash/blob with findings, same-class/G5/fix-class dispositions and required-test outputs;
  canonical mutation JSON bytes/hash/blob with exact H provenance and score; active root-binding readback; and only
  closing-control eligibility or one blocker. No evidence commit, RESULT, Deliver, main publication, release or owner relay.

budget: one bounded fresh reviewer-owned final-H validation/mutation session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-review-near-gas-l1b-v29-final-h-mutation-001-call.md
