# CALL c-review-near-gas-l1b-v29-loopback-final-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-loopback-review-dispatch-001)
engineering_contract: 29

goal: |
  Produce a fresh independent review verdict for the complete approved final range from carrier `62db` through
  correction `T=6fa101b4`: either `REVIEW GREEN` eligibility for the lawful HBP/integration admission or exact
  in-scope findings that prevent it.

context: |
  This is the same root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29—not a new PLAN/design, repair,
  BUILD, mutation, integration, Deliver or L1B close. The prior independent review found a live TraceRunner
  same-wrong StepPreparationSource owner/epoch false-green; PAIR-FREEZE now says the immutable final range is
  eligible for this fresh review.

  Inspect the full ordered final range, including each exact commit's manifest/diff and its actual-parent relation:
  - approved pair-base carrier `62dbb64abd35a684c62f9069d0d9996022113351`;
  - RED `75e0d86d61354a151cb31821269c9a6bf3f2661d`, direct child of 62db;
  - immutable BUILD `4df54a2b024d6c95e4c7095da4018ce4e2cc2dad`, direct child of 75e0;
  - immutable correction `T=6fa101b4ad8011598e18567c6a97428cd78f340c`, direct child of 4df, tree
    `dc4979f17fbe2445049d599b3196653a0d34a938`, exactly
    `tests/**/NearGasL1bTestSupport.cs`, `tests/**/NearGasL1bPropertyAssertions.cs`, and
    `tests/**/NearGasL1bNegativeControlTests.cs`, zero fourth path.

  The review must test the prior finding rather than trust the labels: 4df captures prepared source owner/epoch only
  into the existing fault-hit carrier before deliberate fault, without normal-Step/public-API/acceptance change.
  T samples expected atoms pre-Step, obtains observed atoms from the real fault hit, and requires owner+epoch
  presence/equality per peer. The real TraceRunner NC supplies both peers the same foreign owner/epoch while the
  independently expected source remains unchanged; loopback must reject it.

  PAIR-FREEZE evidence to verify/reproduce where the read-only venue safely permits: 75e0+(4df..T) intended assertion
  RED 1/1; exact T focused positive GREEN 1/1; exact T real same-wrong NC GREEN 1/1; full T 1835/1835, hygiene and
  tools/check.ps1 GREEN. Root binding remains N/A until dev ancestry. Aperture RESULT
  `c-exec-structure-aperture-authority-v1-surface-freeze-001` blocks later integration/mutation/Deliver only.

launch:
  lane: A / NearGas core / fresh final-range independent review
  venue: WIN-CTRL admitted Target Local -> registry-resolved review venue
  target_local: resolve exact project path and review lease through WIN-CTRL; infer no local path here
  machine: PC
  base: clean immutable range 62db→75e0→4df→T; current venue state is evidence only, never a reset target
  conflict_surface: exact range, frozen authority, trace runner/source-atom evidence and gates only
  depends_on: PAIR-FREEZE `FRESH INDEPENDENT REVIEW ELIGIBLE`
  merge_queue: none
  gates: engineering_contract 29; fresh reviewer independence; REVIEW GREEN HBP/integration eligibility or findings

boundaries: |
  Keep the review read-only with respect to product state: no edit, repair, ref/ref-worktree mutation, branch switch,
  reset, stash, clean, rebase, merge, push, publication, configuration/tooling change or new artifact committed in
  the product. Existing review commands may be run solely to verify evidence; this does not authorize a BUILD stage,
  production candidate, mutation/Stryker, integration or Deliver. Mutation remains deferred until the final
  integrated dev H. No owner question, PLAN/spec/design reopening, new family/API/behavior or successor CALL.

  If any in-scope defect is found, record it as an exact finding and return it; do not fix it. Do not call review
  green from counts alone, a synthetic substitute, a source-text scan, inherited PAIR-FREEZE prose or a fresh runner
  result without inspecting the complete range and source/semantic chain.

done_when: |
  1. HOME records a fresh reviewer identity independent of the BUILD/test author, PAIR-FREEZE refuter and prior
     review; Target Local readback, exact object availability, current status and undeclared-byte preservation.
  2. Review proves the ordered range 62db→75e0→4df→T and each manifest/diff/actual-parent relation, including
     T's supplied tree/three-file/zero-fourth-path proof. It verifies 4df has no normal Step/public API/acceptance
     behavior beyond its bounded fault-hit source capture.
  3. Review directly verifies the former loopback finding is fixed: independently-derived pre-Step expected versus
     real-fault-hit observed owner/epoch atoms, per-peer presence/equality, and same-wrong foreign owner/epoch NC
     rejection with unchanged expected source. It performs a same-class sweep of related source-atom projection,
     construction and comparison paths and names every inspected site/disposition.
  4. Review runs or verifies relevant targeted TraceRunner positive/NC and current full/hygiene/check gates with raw
     commands/output; failures are classified as intended behavior, compile/discovery/fixture/harness/environment or
     unrelated—not collapsed into a count.
  5. Review checks frozen PLAN/decision/spec boundaries, five-family count, passive-observer/deterministic-order/
     atomicity invariants, no hidden acceptance behavior and every declared cut. It records root-binding N/A and the
     aperture/mutation final-dev-H boundary without weakening either.
  6. HOME returns exactly `REVIEW GREEN — HBP/INTEGRATION ELIGIBLE` for immutable range 62db→75e0→4df→T, or exact
     findings with severity, evidence, affected claim and required return stage. It claims no integration, Deliver,
     mutation, final dev H, HBP completion or L1B completion.

return: |
  Product FINAL-RANGE INDEPENDENT REVIEW HOME: root/contract; reviewer independence and Target Local proof; exact
  ordered-range ancestry/manifests/diffs; prior-finding and same-class-sweep dispositions; raw relevant test/gate
  evidence and failure classifications; frozen-boundary/five-family/invariant/cut checks; root-binding/aperture/
  mutation boundary; and only REVIEW GREEN HBP/integration eligibility or exact findings. No repair, successor,
  integration, Deliver or mutation claim.

budget: one bounded fresh independent review session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-review-near-gas-l1b-v29-loopback-final-001-call.md
