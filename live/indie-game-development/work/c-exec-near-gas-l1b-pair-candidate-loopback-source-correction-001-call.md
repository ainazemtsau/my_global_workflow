# CALL c-exec-near-gas-l1b-pair-candidate-loopback-source-correction-001

to: executor
direction: indie-game-development
track: core
kind: engineering
repo: ainazemtsau/GasCoopGame
node: g-9c41
task: L1B-Capture
issued: 2026-07-19 (s-work-near-gas-l1b-v29-evidence-binding-control-close-001)
engineering_contract: 29

goal: |
  NearGas L1B v29 has an independently-authored, test-only correction `T` whose real loopback oracle distinguishes
  the live StepPreparationSource owner/epoch from a same-wrong source, while unchanged BUILD candidate `4df54a2b`
  satisfies `T` and frozen carrier `62dbb64a` demonstrably does not.

context: |
  This is the same v29 implementation root `c-exec-near-gas-l1b-pair-candidate-001`, not a new root, PLAN, spec or
  design decision. Frozen `c-exec-near-gas-l1b-plan-001` remains docs-only/proof-bound carry-forward authority;
  PLAN/proposal/tasks/spec/decision/ADR and all prior review/RESULT evidence remain byte-identical.

  Product EVIDENCE-BINDING CONTROL HOME is complete:
  - remote admission is `ADMITTED-ACTIVE` at `dev == origin/dev ==
    25afa4aa4585d40a304d233c0b3f24b4e6bf34b3`;
  - its exact seven authorized control files are committed; WIN-CTRL is clean;
  - WIN-U3 is clean on its exact current branch at BUILD candidate
    `4df54a2b024d6c95e4c7095da4018ce4e2cc2dad`, tree
    `8a1c6a2697b7680dee43530d60a18f2915403b90`;
  - the root-binding self-test is GREEN and intentionally N/A until this candidate becomes a dev ancestor;
  - registry admits only this fresh independent test-author and exactly these existing files:
    `tests/**/NearGasL1bTestSupport.cs`, `tests/**/NearGasL1bPropertyAssertions.cs`, and
    `tests/**/NearGasL1bNegativeControlTests.cs`.

  Existing immutable evidence remains: carrier `62dbb64abd35a684c62f9069d0d9996022113351`, prior RED
  `75e0d86d61354a151cb31821269c9a6bf3f2661d`, binding PAIR-FREEZE thread
  `019f78c2-a17a-73e0-a56e-79db206fd5d3`, and product BUILD `4df54a2b`. The earlier independent review stays OPEN:
  direct Step fault checks see OwnerGenerationId/Epoch, but live five-family TraceRunner does not emit those two raw
  Step source facts. Frame-2 FaultAtoms contains StepResult only and FaultSourceAtoms only replacement-source facts,
  so same-wrong owner/epoch can still report FaultInjection/Loopback MET. Existing `step-preparation.*` NCs mutate a
  synthetic CompleteTrace, not the live runner.

  The correction's exact semantic obligation is limited to the existing test files:
  - TestSupport must construct independently expected and live-observed Step source atoms from the real TraceRunner;
  - PropertyAssertions must require their presence and equality for loopback;
  - NegativeControlTests must make same-wrong owner/epoch fail through the real trace, rather than only through a
    synthetic CompleteTrace. No new family, count or production API is permitted.

  The active root evidence id remains `c-exec-near-gas-l1b-pair-candidate-001` with its existing root validator and
  canonical review/mutation/result artifact paths. The unrelated aperture RESULT
  `c-exec-structure-aperture-authority-v1-surface-freeze-001` is an external serialized-dev STOP for later
  integration/mutation/Deliver only; it does not block this U3 test correction.

  launch:
    lane: A / NearGas core / v29 test-only PAIR-CANDIDATE correction
    venue: WIN-CTRL admitted Target Local -> registry-selected WIN-U3 current project only
    machine: PC
    base: clean candidate 4df54a2b and control HOME dev/origin/dev 25afa4aa; evidence only, never checkout targets
    conflict_surface: exactly three admitted NearGas L1B test/test-support files
    depends_on: ADMITTED-ACTIVE HBP and root-binding self-test GREEN/N-A-until-dev-ancestor
    merge_queue: none; no integration, publication or mutation in this stage
    gates: engineering_contract 29; fresh independent test-author; real 62db..T RED / 4df+T GREEN diagnostic; later binding PAIR-FREEZE

boundaries: |
  Work only in the registry-admitted Target Local venue and preserve all undeclared bytes. Do not create, switch,
  rename, reset, stash, clean, rebase, merge, push, force, delete, overwrite or discard any project workspace data.
  Do not modify production/carrier/BUILD code or metadata, `Assets/**`, public APIs, frozen authority, the seven
  control files, review/mutation/result artifacts, validation.config, tools, registry, branch/ref state or a fourth
  test file. The builder may not edit these tests. A required fourth file, status/identity drift, or inability to
  retain exactly the three-file manifest is `FOURTH-FILE REQUIRED`/STOP with proof and no edit.

  Do not run mutation/Stryker, integrate into dev, run Deliver, publish, perform final review/G5, or claim L1B
  completion. Do not mutate the aperture RESULT or use it as a reason to alter this test scope. Do not implement a
  fallback production guard, comparator, telemetry, callback, observer, sixth family, Unity/gameplay/networking,
  L2/C1/workers/S4/Level/DA/PGG work, or any fake behavior churn.

done_when: |
  1. Fresh evidence records test-author identity and independence from the original candidate/BUILD author, the
     open-review author, later PAIR-FREEZE/refutation/reviewer/validator roles and every builder. It records admitted
     WIN-CTRL/WIN-U3 route, exact pre/post HEAD/status and preservation of undeclared bytes.
  2. The exact test-only commit `T` directly follows candidate `4df54a2b`; HOME records parent/commit/tree, three-file
     manifest, per-file diff/blobs and aggregate hash. No path outside the three authorized test files changes; carrier,
     RED history, BUILD source, public behavior and frozen authority remain byte-identical.
  3. The real TraceRunner now appends independently expected and live-observed Step source atoms; loopback assertion
     requires each atom's presence and equality; a seeded same-wrong OwnerGenerationId/Epoch source is rejected by the
     live trace. Expected values may not copy a fault row, proxy Owner/Epoch, hardcode a value or correlate actual and
     expected through the same object. Existing synthetic CompleteTrace-only NC evidence does not discharge this item.
  4. Exact diagnostic topology is artifact-backed without changing WIN-U3: materialize a disposable,
     registry-approved diagnostic copy from carrier `62dbb64abd35a684c62f9069d0d9996022113351`; apply only the
     three-file test manifest `git diff --binary 62db..T -- <three admitted paths>`; run the real filtered command.
     It must RED at the intended corrected source assertion. Run the identical filtered command at `4df54a2b + T`; it
     must GREEN. Record both trees, test-diff hash, commands, raw discovery/executed/passed/failed counts and exact
     assertion traces. Compile/discovery/Arrange/fixture/harness/environment failure is a blocker, not RED evidence.
  5. Repo-native build/hygiene and the required non-NearGas baseline remain GREEN; full current discovery/execution
     counts are recorded rather than asserted from prose. The 4df baseline evidence (1835/1835) is reconciled to the
     exact post-T run; any count difference has named test identities and no unrelated failure.
  6. HOME records the complete disposition of the OPEN review finding, exact `T` commit/manifest, three-file proof,
     diagnostic RED/GREEN evidence, raw counts, assumptions/cuts/cost and root-validator status. It returns only one
     next-stage class: fresh read-only binding PAIR-FREEZE/refutation of exact `4df + T`, then a fresh independent
     review round. Mutation, integration and Deliver remain prohibited until that review is GREEN and final dev H is
     legal; the aperture STOP remains explicit.

return: |
  Product TEST-ONLY PAIR-CANDIDATE CORRECTION HOME: `PAIR-FREEZE ELIGIBLE` or exact blocker; root id and contract 29;
  independent test-author/role separation; registry admission and WIN-U3 pre/post proof; frozen authority and
  production/carrier/BUILD preservation; exact T parent/commit/tree, manifest/diffs/blobs/aggregate; source-atom and
  live-NC dispositions; isolated 62db..T RED and 4df+T GREEN commands/raw counts/assertion traces; build/hygiene/
  baseline dispositions; root-binding self-test status, aperture STOP and every done_when disposition. On GREEN name
  only fresh binding PAIR-FREEZE then independent review eligibility; no mutation/integration/Deliver/G5/completion
  claim and no successor CALL or owner question.

budget: one bounded fresh test-author session; stop on route/identity/independence/scope/diagnostic/gate mismatch
surface: Codex Desktop, registry-admitted Target Local / WIN-U3

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-l1b-pair-candidate-loopback-source-correction-001-call.md
