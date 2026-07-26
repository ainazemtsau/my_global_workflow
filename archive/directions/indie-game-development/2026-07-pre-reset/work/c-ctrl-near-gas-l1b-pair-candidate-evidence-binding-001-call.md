# CALL c-ctrl-near-gas-l1b-pair-candidate-evidence-binding-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-loopback-review-open-route-001)
engineering_contract: 29

goal: |
  NearGas L1B v29 имеет один admitted, non-design implementation-evidence binding для root
  `c-exec-near-gas-l1b-pair-candidate-001`, который fail-closed связывает независимый review, mutation и
  closing RESULT с будущим exact integrated dev HEAD, не переписывая frozen PLAN/spec и не ослабляя Deliver.

context: |
  This consumes the independent review of the existing v29 candidate, not a new design decision. Frozen
  `c-exec-near-gas-l1b-plan-001` is docs-only carry-forward authority: PLAN/proposal/tasks/spec/decision/ADR stay
  immutable and no `openspec/changes/<root>/specs/**` folder may be created. Its prior review/RESULT are immutable
  proof, not the implementation evidence subject of this root.

  Exact product facts supplied to Direction:
  - root `c-exec-near-gas-l1b-pair-candidate-001`, `engineering_contract: 29`; frozen PLAN adoption unchanged;
  - immutable carrier `62dbb64abd35a684c62f9069d0d9996022113351`, RED
    `75e0d86d61354a151cb31821269c9a6bf3f2661d`, binding PAIR-FREEZE thread
    `019f78c2-a17a-73e0-a56e-79db206fd5d3`;
  - BUILD candidate `4df54a2b024d6c95e4c7095da4018ce4e2cc2dad`, tree
    `8a1c6a2697b7680dee43530d60a18f2915403b90`, is exact one-file production wiring and 1835/1835 GREEN;
  - registry HBP is published at `dev@8cff0a285eebe898e0010897662c66b58995c7c4`;
  - the independent review of `27f8aa19..4df54a2b` has Critical none and one Important in-scope finding OPEN;
    mutation was intentionally not run.

  The OPEN finding is frozen verbatim as a review obligation: the direct Step fault test checks
  `StepPreparationSource.OwnerGenerationId/Epoch`, but live five-family `TraceRunner` does not project these raw
  Step-source facts. Frame-2 FaultAtoms contains StepResult only; FaultSourceAtoms contains replacement-source only.
  Same-wrong owner/epoch can therefore report FaultInjection/Loopback MET. Existing `step-preparation.*` NCs mutate a
  synthetic `CompleteTrace`, not the live runner. The expected correction surface is exactly the existing test files
  `tests/**/NearGasL1bTestSupport.cs`, `tests/**/NearGasL1bPropertyAssertions.cs`, and
  `tests/**/NearGasL1bNegativeControlTests.cs`; current sites are TestSupport ~895 and ~1080-1105,
  PropertyAssertions `AssertFaultSources` ~449-458, and NegativeControlTests ~373-417/~631-633.

  The authoritative implementation-evidence id is exactly `c-exec-near-gas-l1b-pair-candidate-001` (never the
  frozen PLAN id and never a newly invented PLAN). Its canonical artifact names are exactly:
  - `docs/reviews/review-c-exec-near-gas-l1b-pair-candidate-001.md`;
  - `docs/measurements/mutation-c-exec-near-gas-l1b-pair-candidate-001.json`;
  - `docs/results/result-c-exec-near-gas-l1b-pair-candidate-001.md`.
  Current Deliver discovers only living OpenSpec G0 folders; this root has none, while the frozen docs-only PLAN id is
  correctly skipped. HBP forbids unadmitted spec/tool/config edits, so this Direction CALL authorizes the one bounded
  metadata/tooling remedy below before any mutation head exists.

  A separate serialized dev item, `c-exec-structure-aperture-authority-v1-surface-freeze-001`, currently has a changed
  `RESULT` with `NOT DELIVERED`. Auto-result detection can block L1B Deliver until that earlier dev state is drained and
  published. It is unrelated: do not edit, relabel, publish or absorb it into this root.

  launch:
    lane: A / NearGas core / evidence-binding control
    venue: WIN-CTRL / Target Local / registry-resolved admitted project only
    machine: PC
    base: registry HBP `dev@8cff0a285eebe898e0010897662c66b58995c7c4`; Direction does not select a path, branch, checkout or SHA
    conflict_surface: registry/HBP admission plus Deliver metadata/tooling and evidence paths only
    depends_on: failed review round remains OPEN; frozen PLAN carries forward unchanged
    merge_queue: registry-controlled; no feature integration or publication in this stage
    gates: engineering_contract 29; WIN-CTRL HBP -> ADMITTED-ACTIVE; explicit root validator; external dev serialization checked

boundaries: |
  WIN-CTRL alone resolves the exact Target Local workspace and writes the admission record. Do not select, create,
  switch, reset, stash, clean, rebase, merge, push, force, delete or otherwise alter a project workspace from this
  CALL. Do not alter `Assets/**`, production source, carrier `62db...`, RED `75e0...`, candidate `4df...`, frozen
  PLAN/proposal/tasks/spec/decision/ADR, the five-family inventory, or any test file. Do not create an OpenSpec PLAN,
  proposal, task list, delta spec or `specs/**` subtree for this root. Do not run BUILD, Stryker/mutation, integration,
  Deliver, PAIR-FREEZE, final review or L1B G5.

  The review finding remains `OPEN` in the existing independent review; do not mark it fixed/refuted or claim review
  green. A fourth test file is not authorized: if the later correction cannot be expressed in the three named existing
  test files, return `FOURTH-FILE REQUIRED` with a unique-path/readback proof and no edit; Direction alone decides a
  subsequent bounded exception. The aperture RESULT is outside scope and cannot be bypassed by changing auto-detection.

done_when: |
  1. WIN-CTRL readback records HBP `HANDBACK-PENDING -> ADMITTED-ACTIVE` for one exact test-only
     PAIR-CANDIDATE correction manifest under root `c-exec-near-gas-l1b-pair-candidate-001`, contract 29, the three
     named test files, a fresh independent test-author lease, builder-test-write prohibition, and the frozen OPEN
     review finding. Registry resolution, not Direction, supplies Target Local path/branch/current SHA.
  2. Repo-local Deliver gains exactly one non-design root-validator binding: `validation.config` maps the authoritative
     implementation id to the three canonical review/mutation/result paths above, and `tools/check.ps1 -Deliver`
     loads that mapping and fails closed when any named path is absent, when the review has an in-scope OPEN/missing
     disposition, or when the mutation/result evidence names another implementation id. No OpenSpec/spec authority is
     created or changed.
  3. The root validator additionally requires mutation evidence to name the final integrated dev HEAD `H`, requires its
     authoritative diff base/head/scope and mutation-input snapshot to equal `H`, and rejects any mutation-input delta
     after `H`. It must reject a Stryker run on WIN-U3/current candidate and cannot accept a score before exact dev
     integration. A seeded-miss/readback proves these fail-closed conditions.
  4. The manifest records the lawful later oracle topology without executing it: keep WIN-U3 at its candidate; form a
     disposable registry-approved diagnostic copy from exact carrier `62db...`; apply the complete final test manifest
     diff `62db..T` only to the three authorized test files; the real filtered runner must fail there at the intended
     source assertion and pass at candidate `4df...` plus the same `T` test blobs. Record trees, diff/blob hashes,
     commands and raw output; compile/discovery/Arrange/harness failure is a blocker. No revert/reset/switch of U3.
  5. The external dev serialization is read back. If the aperture RESULT remains changed/NOT DELIVERED or unpublished,
     record exact `STOP: DEV-SERIALIZATION-APERTURE-RESULT-PENDING`; do not integrate L1B, choose final `H`, run
     mutation, run Deliver or claim a closing RESULT. Its own route must drain/publish it independently.
  6. HOME returns only `CORRECTION-MANIFEST ADMITTED` or one complete blocker, with HBP transition, exact root-validator
     diff and seeded-miss output, all artifact paths, three-file manifest, OPEN review disposition, external-dev
     disposition and the next-stage class. It makes no implementation, mutation, integration, Deliver or completion
     claim and authors no successor CALL.

return: |
  Product EVIDENCE-BINDING CONTROL HOME: status `CORRECTION-MANIFEST ADMITTED` or exact blocker; root and contract 29;
  WIN-CTRL HBP pre/post status plus registry-resolved Target Local evidence; frozen-authority preservation; exact
  `validation.config` and `tools/check.ps1 -Deliver` binding diff, canonical review/mutation/result paths, seeded-miss
  results and root-validator behavior; frozen OPEN review finding; exact three-file test manifest and fresh
  independent-test-author lease; future `62db..T` diagnostic topology; current aperture-result readback and either
  its explicit STOP or its independently published clearance. State only the eligibility for a separate test-author
  correction, then fresh PAIR-FREEZE and independent review; mutation/integration remain prohibited until that review
  is GREEN and final dev `H` is legal. No successor CALL and no owner question.

budget: one bounded WIN-CTRL process/control session; stop on admission, authority, metadata/tooling, seeded-miss or external-dev serialization mismatch
surface: Codex Desktop, WIN-CTRL registry with Target Local resolution

END_OF_FILE: live/indie-game-development/work/c-ctrl-near-gas-l1b-pair-candidate-evidence-binding-001-call.md
