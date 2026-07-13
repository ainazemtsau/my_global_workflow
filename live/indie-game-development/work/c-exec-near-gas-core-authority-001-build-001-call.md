# CALL c-exec-near-gas-core-authority-001-build-001

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
node: g-9c41
task: NearGas-L1-BUILD
phase: BUILD
issued: 2026-07-13 (s-work-near-gas-l1-plan-close-001)
parent: c-exec-near-gas-core-authority-001

goal: |
  Deliver NearGas L1 as one reviewed, gate-green dormant engine-free Core authority whose generation replacement
  and complete deterministic Step are atomic, while preserving exact legacy-audit meanings and every foreign file.

context: |
  The owner-approved product contract is frozen in commit 1e4e78c12510ad4e2e0e9fcaa2a490f8d073fba8 and merged
  into origin/main at 13917123f71aaa556bac0991021ee5793fb50bc1. Binding artifacts:
  - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md
  - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md
  - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md
  - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md
  - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md
  - docs/results/c-exec-near-gas-core-authority-001.md

  Owner verdict: «Я подтверждаю твой рекомендованный вариант А» and «по плану я подтверждаю … и там двигаемся
  дальше». Accepted option A is a serial concurrency-ready L1. Actual multithreading belongs only to a separately
  issued future c-exec-near-gas-concurrency-001 after delivered L1/L2/C1 and fresh profiling; DirectionS decides
  whether the measured need justifies that leg.

  Root AGENTS.md, validation.config contract v19, docs/gas-simulation/PROGRAM.md and the frozen artifacts above are
  authority. The frozen tasks ledger starts every BUILD row failing and may be updated only by the evidence role it
  names. The product result remains PLAN FROZEN / BUILD NOT STARTED / NOT DELIVERED until this separate leg proves it.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core (assigned exclusive core worktree; headless; no Unity Editor)
    machine: ПК
    base: origin/main @13917123f71aaa556bac0991021ee5793fb50bc1 (§Re-sync обязателен)
    conflict_surface: NearGas Core authority plus the frozen source/reaction/flow/loopback seams, tests and gate metadata
    depends_on: owner-approved frozen PLAN @1e4e78c merged and Direction binding-refuted at @13917123
    merge_queue: one exclusive mutating core slot; no concurrent core leg
    gates: independent spec-only RED; different-family review; G5=fresh session; owner-eye=n/a for dormant engine-free L1

boundaries: |
  Implement exactly the frozen L1. Builder and test-author do not edit or reinterpret PLAN/spec/tasks/ADR/acceptance
  text or independent RED tests. Only the proper non-builder evidence integrator may flip a frozen BUILD-ledger row
  after opening its cited evidence; no role changes its wording or criteria. Any contradiction, missing required tool,
  shared-kernel fidelity loss, raw mutable escape, second transaction, full-field clone, catch/restore, or need for a
  child-leg API is STOP, not a local redesign.

  Option A is binding: one caller-serialized non-reentrant writer, deterministic candidate-only preparation, stateless
  handlers, per-generation/Step scratch and one serial commit. Do not add Thread/Task/Parallel, jobs, workers, worker
  counts, scheduler/partition/lock/concurrent-collection APIs, public thread-safety claims or speculative worker tests.
  Do not start c-exec-near-gas-concurrency-001; it remains a future measured leg after delivered L1/L2/C1 and a fresh
  profile, and may stay parked if the profile shows no need.

  Do not implement L2 limits, C1 digest/revision, M0/L3 Unity authority, PlayerSense, render, replay, networking/save,
  runtime source movement, doors/topology/destruction, legacy deletion, Phase 0 or c-visual-009. Do not launch Unity,
  PlayMode, MCP or a game build; L1 evidence is engine-free/headless.

  Preserve every foreign dirty/untracked path in GasCoopGame_dev exactly, including both pre-existing untracked
  NearGas fixture files. Do not reuse, overwrite, stage, clean or treat those fixtures as independent RED evidence.
  Never substitute the dirty dev checkout for an invalid assigned core venue.

done_when: |
  1. A fresh independent test-author reads only the frozen spec and first commits discovered failing acceptance,
     NegativeControl and all four required Property test classes; ancestry proves the builder never edited them or
     the frozen contract/ledger.
  2. One dormant engine-free NearGasSimulation owns a defensively built generation, exposes only the frozen minimal
     scalar read surface, swaps a complete candidate atomically, rejects stale reads and leaks no raw mutable state.
  3. Its sole public Step owns the frozen source-before-flow canonical order through the existing kernel and performs
     one prepare/validate/result/commit transaction; every planted failure preserves visible and hidden retry state,
     and retry plus continuation remains twin-equivalent.
  4. Exact legacy MeaningChecksum/StructureChecksum goldens and source isolation remain unchanged through explicit
     slow CaptureLegacyAudit only. Ordinary replacement/read/Step/result performs and publishes no full-domain FNV;
     local generation ids remain local and loopback delegates the same public Step.
  5. The delivered code is serial concurrency-ready exactly as option A: deterministic owned candidates, stateless
     handlers, per-Step scratch and one serial commit, with no actual multithreading, scheduler/worker surface, speedup
     claim or fake concurrency evidence. The future measured concurrency leg remains unopened here.
  6. Integer/overflow and zero-float guards, exact boundary/golden/door/source/peer regimes, complete existing headless
     regressions and planted controls are green without reduced-fidelity scans or proxies.
  7. Core build/test, repository checks, NegativeControls, properties, diff mutation >=70, independent final-tip review,
     binding fresh-session G5 and deliver gate are mutually green; the proper evidence integrator updates each BUILD
     ledger row and the product report to DELIVERED only after its required evidence is opened.
  8. No Unity/product activation or child leg ran, all ten foreign dev paths are byte-for-byte preserved, and the
     returned RESULT names the final branch/commit, exact changed files, transcripts, review/G5 evidence and rollback.

return: |
  Product BUILD RESULT HOME with final branch/commit and ancestry; exact changed-file summary; independent RED commit
  and immutable-test proof; evidence disposition for every frozen acceptance/NegativeControl/Property/ledger row;
  opened build/test/check/mutation/review/binding-G5/deliver artifacts; updated result path and rollback; confirmation
  that option A stayed serial, c-exec-near-gas-concurrency-001 was not started, no Unity/child-leg scope ran, and all
  ten foreign dev paths were preserved. On any unresolved gate or STOP, return CHECKPOINT / NOT DELIVERED and leave
  the Direction open_call pending. Do not author the next Direction CALL.

budget: one focused L1 BUILD/delivery leg; no child leg or Unity work
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-build-001-call.md
