# CALL c-exec-near-gas-l1b-pair-freeze-v29-loopback-source-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-pair-freeze-loopback-route-001)
engineering_contract: 29

goal: |
  Produce a fresh binding read-only verdict whether immutable BUILD `4df54a2b` plus immutable test correction
  `T=6fa101b4` is independently evidenced, semantically genuine and free of hidden acceptance behavior, making it
  eligible for a separate fresh independent review; otherwise return one complete blocker.

context: |
  This is the same implementation root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29—not a PLAN, design,
  product implementation, BUILD or L1B close. Frozen PLAN `c-exec-near-gas-l1b-plan-001`, all prior PLAN/review/
  RESULT evidence and public behavior remain immutable.

  Exact pair under refutation:
  - immutable BUILD `4df54a2b024d6c95e4c7095da4018ce4e2cc2dad`;
  - immutable T `6fa101b4ad8011598e18567c6a97428cd78f340c`, direct parent 4df, tree
    `dc4979f17fbe2445049d599b3196653a0d34a938`, with exactly
    `tests/**/NearGasL1bTestSupport.cs`, `tests/**/NearGasL1bPropertyAssertions.cs`, and
    `tests/**/NearGasL1bNegativeControlTests.cs`; WIN-U3 is clean at T.

  Complete diagnostic evidence is input to attack, not a verdict:
  - frozen `75e0d86d61354a151cb31821269c9a6bf3f2661d` is direct child of carrier
    `62dbb64abd35a684c62f9069d0d9996022113351`; only binary 4df..T overlay was used, patch SHA-256
    `96459A1BDFC72886FD6A2DAFB7E8D71E49B9C1564BF9195BCBEB8A956CB4652B`, overlay tree
    `b1a211219b5468145f6281a47a1867eb656d5620`, zero fourth path;
  - focused real TraceRunner positive at 75e0+overlay compiled/discovered 1 and failed 1 only at the new live
    source-sensitive FaultInjection/loopback assertion under frozen placeholder;
  - byte-identical focused command at T discovered/passed 1/1; real same-wrong owner+epoch TraceRunner NC at T
    discovered/passed 1/1. Expected source is sampled pre-Step and observed source comes from the real fault hit;
  - exact T full suite is 1835/1835 GREEN; hygiene and `tools/check.ps1` GREEN (1735 ordinary plus v29/self-checks/
    scans). Temp worktree/patch is removed and pruned.

  Root binding is intentionally N/A until dev ancestry. The aperture RESULT
  `c-exec-structure-aperture-authority-v1-surface-freeze-001` blocks only later integration/mutation/Deliver.

launch:
  lane: A / NearGas core / fresh v29 binding PAIR-FREEZE
  venue: WIN-CTRL admitted Target Local -> registry-resolved read-only product venue
  target_local: resolve exact project path and read-only registry lease through WIN-CTRL; infer no local path here
  machine: PC
  base: immutable Git objects 4df and T plus recorded 75e0-overlay evidence; current clean venue is evidence only
  conflict_surface: exact pair manifests/diffs, recorded diagnostic evidence and frozen authority only
  depends_on: DIAGNOSTIC-COMPLETION HOME `PAIR-FREEZE ELIGIBLE`
  merge_queue: none
  gates: engineering_contract 29; fresh independent artifact-backed refutation; review eligibility or blocker only

boundaries: |
  Be read-only. Do not edit/write product, tests, evidence, registry, control files, refs, worktrees, configuration
  or frozen authority; do not create/switch/reset/stash/clean/rebase/merge/push/publish/delete a workspace or ref.
  Do not run BUILD, test runners, mutation/Stryker, integration, Deliver, final review/G5 or a full L1B close. Inspect
  the recorded raw command outputs and Git objects; do not replace evidence through a new run. Any missing exact
  object, relevant dirty state, route/identity collision or inaccessible recorded artifact is a blocker.

  Do not repair or reinterpret anything: no fourth path, source/API/behavior change, new observation family, synthetic
  substitute, fake behavior churn, PLAN/spec/design/owner interview, or downstream CALL. No owner question. This
  PAIR-FREEZE may return only a fresh independent review eligibility statement for exact 4df+T or one complete blocker.

done_when: |
  1. Evidence records fresh refuter identity/context and disjointness from the BUILD/candidate/test-author, original
     review author and future review/validator roles; WIN-CTRL registry route, Target Local lease, exact object
     readback and preserved venue bytes are shown.
  2. Exact Git inspection proves T directly follows 4df, has the supplied tree and exactly the three named test paths;
     its diff/manifests expose no hidden production/acceptance behavior. It records 4df's exact relevant diff/manifest
     against its actual parent without inferring behavior from commit text.
  3. Exact diagnostic topology is verified: 75e0 is direct child of 62db; only binary 4df..T overlay hash/tree above
     was used, zero fourth path, and temporary overlay is absent. The former 62db+T compiler failure remains invalid
     topology—not behavioral RED.
  4. The refuter inspects the saved raw focused evidence: 75e0+overlay compiled/discovered 1 then failed only at the
     new live owner/epoch assertion; byte-identical T positive and real same-wrong owner+epoch NC each discovered/
     passed 1/1. It verifies expected source is pre-Step and observed source is the real fault hit, not copied,
     proxied, hardcoded, synthetic or co-derived through one object.
  5. The refuter verifies literal full-T 1835/1835, hygiene and tools/check evidence, and checks that no hidden
     acceptance behavior, carrier/test coupling, scope expansion or substituted acceptance criterion is masked by
     counts. Root-binding N/A and aperture later-only STOP are recorded correctly.
  6. A claim-by-claim artifact-backed refutation records every above disposition and returns exactly one class:
     `FRESH INDEPENDENT REVIEW ELIGIBLE` for immutable 4df+T, or one complete blocker naming the failed claim and
     required return stage. It claims no BUILD, mutation, integration, Deliver, review-GREEN or L1B completion.

return: |
  Product PAIR-FREEZE HOME: root id and contract 29; refuter independence/Target Local read-only proof; 4df/T
  ancestry/tree/manifest/diff evidence; 75e0/62db overlay hash/tree/zero-fourth-path and cleanup proof; raw recorded
  RED/GREEN/NC/full/hygiene/check evidence dispositions; carrier/test independence and hidden-acceptance refutation;
  root-binding/aperture status; every done_when disposition; and only `FRESH INDEPENDENT REVIEW ELIGIBLE` or one
  complete blocker. No successor CALL, edits, BUILD, mutation, integration, Deliver or owner question.

budget: one bounded fresh read-only PAIR-FREEZE/refutation session
surface: Codex Desktop, WIN-CTRL registry-resolved Target Local

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-pair-freeze-v29-loopback-source-001-call.md
