# CALL c-exec-near-gas-core-authority-001-execute-002

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
project: GasCoopGame
node: g-9c41
task: NearGas-L1-BUILD
phase: EXECUTE
issued: 2026-07-13 (s-work-near-gas-l1-plan-amend-binding-close-001)
parent: s-work-near-gas-l1-plan-amend-binding-close-001

goal: |
  Deliver NearGas L1 from the amended owner-approved frozen authority as a reviewed, gate-green dormant engine-free
  Core authority, while preserving the original BUILD checkpoint as historical NOT DELIVERED evidence.

context: |
  This is a NEW execution session, not a continuation of c-exec-near-gas-core-authority-001-build-001. Start again
  with a new independent spec-only RED author. The aborted authoring attempt left no test commit or surviving file and
  is not evidence.

  Published authority is exact product origin/main @32107343d75240d6b3bc850d7010bd3f17dc4ca8. It is a merge with
  parents 13917123f71aaa556bac0991021ee5793fb50bc1 and PLAN-AMEND
  a58ee3567f08ba8e2c16e88c851e3de89f0678c6; the amendment's sole parent is the historical original BUILD checkpoint
  b94806deaaa3cbb56a8b6cda9baa75ac52f028c3. The published tree equals the PLAN-AMEND tree. Do not treat the lagging
  C:\projects\Unity\GasCoopGame checkout as the authoritative tip.

  A separate fresh Direction binding-refutation read the published frozen packet and accepted construction A / fault
  A as closing the original blocker. Owner verdict, verbatim:
  «Подтверждаю construction A и fault A: публичный owned Create(...) и operation-local internal semantic fault
  selector. Без костылей.»

  Frozen execution authority at the published base:
  - AGENTS.md and validation.config (repo contract v20);
  - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md;
  - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md;
  - docs/results/c-exec-near-gas-core-authority-001.md;
  - docs/gas-simulation/PROGRAM.md.

  The amended spec binds a real public owned NearGasGenerationDefinition.Create(...), immutable built-in Core handler
  type maps, a literal known-valid single-cell recipe, and exact internal NearGasFaultSite values plus
  ReplaceGenerationForTesting(..., site) / StepForTesting(..., site) over the same private production paths. It keeps
  option A: one caller-serialized, non-reentrant, serial concurrency-ready L1. Actual workers remain a separate future
  leg only after delivered L1/L2/C1 and fresh profiling.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core — existing assigned headless core worktree; create NEW branch
      codex/c-exec-near-gas-core-authority-001-execute-002
    machine: ПК
    base: origin/main @32107343d75240d6b3bc850d7010bd3f17dc4ca8 (exact; if it moved, STOP and return)
    conflict_surface: NearGas Core authority, source/reaction/flow/loopback seams, new independent tests and gate evidence
    depends_on: [PLAN-AMEND a58ee356 merged in origin/main@32107343; fresh Direction binding verdict GREEN]
    merge_queue: one exclusive mutating lane-A slot; return the final branch/result home, no merge or push in this CALL
    gates: independent spec-only RED; different-family final-tip review; final binding G5 = a separate fresh session;
      owner-eye = n/a for dormant engine-free L1

boundaries: |
  At entry recheck that C:\projects\Unity\GasCoopGame_core is clean, has no Unity lockfile, the new branch name is
  unused, and origin/main is the exact base above. Create the new branch from that base. A dirty/occupied worktree,
  existing conflicting branch or moved base is STOP; do not reset, clean, overwrite, silently rebase or reuse another
  checkout.

  Do not assign, switch, clean, stage, overwrite or otherwise use C:\projects\Unity\GasCoopGame_dev for this leg. It
  contains foreign uncommitted work and is non-authoritative. Preserve its fresh path/hash inventory byte-for-byte;
  in particular, never reuse its pre-existing untracked NearGas fixtures as RED evidence. Do not use the main checkout
  C:\projects\Unity\GasCoopGame as an authoritative working venue.

  The independent test-author is a fresh role and reads ONLY the frozen sim-core spec before authoring. It first owns
  and commits all acceptance, NegativeControl and four required Property test classes under a fresh non-colliding
  NearGas test path. Only after that immutable RED commit may the builder read production implementation and build.
  The builder SHALL NOT edit the independently-authored tests.

  The builder SHALL NOT edit or reinterpret frozen PLAN.md, proposal.md, sim-core spec, tasks ledger, ADR-E-0011 or
  acceptance meaning. Only the proper non-builder evidence integrator may flip ledger rows or update the product RESULT
  and dashboard after opening their required evidence. No local redesign may repair a contradiction: STOP and return a
  checkpoint naming the exact frozen gap.

  Implement exactly amended option A. Do not add Thread/Task/Parallel, jobs, workers, worker counts, scheduler,
  partition, lock, concurrent-collection or public thread-safety surfaces. Do not open
  c-exec-near-gas-concurrency-001. Real workers remain after delivered L1/L2/C1 plus fresh profiling and a separate
  Direction-issued leg.

  Do not add L2 limits, C1 digest/revision, M0/L3 Unity authority, PlayerSense, render, replay, networking/save,
  runtime source movement, doors/topology/destruction, legacy deletion, Phase 0 or c-visual-009 scope. Do not launch
  Unity, PlayMode, MCP or a game build; this L1 is engine-free/headless. Do not merge or push in this CALL.

  Contract v20 is binding: this CALL, product AGENTS.md, frozen PLAN/spec and validation.config are the execution
  authority. Optional global skills/tools cannot add workflow requirements or become blockers. A genuinely required
  repo-authority tool becoming unavailable is STOP under contract v16; never substitute a source scan or reduced-
  fidelity proxy.

  The original branch/checkpoint codex/c-exec-near-gas-core-authority-001-build-001@b94806de remains immutable
  historical CHECKPOINT / NOT DELIVERED. Do not resume, rewrite, squash into or present it as this execution's ancestry.

done_when: |
  1. Preflight records exact project/worktree/new branch/base, clean status, no Unity lock, repo contract v20 and fresh
     foreign-work preservation. Ancestry starts at origin/main@32107343; the original BUILD remains historical.
  2. A new independent spec-only RED author first commits executable acceptance coverage for every frozen property,
     all named NegativeControls and all four Property classes without reading production, reusing old/dev fixtures or
     inventing a fixture/reflection/controller seam; RED evidence names discovery and the intended absent/wrong failure.
  3. One dormant engine-free NearGasSimulation owns a defensively built generation, exact minimal scalar read and one
     complete deterministic Step through the existing kernel with candidate-only preparation and one non-throwing
     commit; no raw mutable state, formula copy, full-field clone, catch/restore or second transaction exists.
  4. Construction A is exact: public owned Create(...), two immutable Core kind-to-System.Type maps and the frozen
     literal recipe work; caller alias mutation is inert; invalid definition/replacement regimes preserve none/old
     generation, ids, reads and hidden state; no public constructor, fixture, reflection path, mutable registry/builder
     or handler-instance input appears.
  5. Fault A is exact: the frozen NearGasFaultSite inventory/values and two internal entrypoints share the public
     private paths; None parity, wrong-operation/undefined selector rejection, every named checkpoint, retry-twin
     continuation and no cross-call selector state are proven without callback/delegate/payload/exception factory,
     mutable controller/property, alternate algorithm or global/static switch.
  6. Exact legacy MeaningChecksum/StructureChecksum goldens, source isolation, OpenDoorFlow and loopback delegation
     remain unchanged through explicit slow CaptureLegacyAudit only. Ordinary replacement/read/Step/result performs
     and publishes no full-domain FNV; local generation ids remain local.
  7. Option A remains serial concurrency-ready: owned immutable inputs, canonical order, stateless handlers,
     generation/Step-owned scratch and one serial commit; no actual worker/scheduler surface or speedup claim enters L1.
  8. Core build/tests, repository checks, NegativeControls, Properties, diff-scoped mutation >=70, independent
     different-family final-tip review, finding disposal, a binding fresh-session G5 and tools/check.ps1 -Deliver are
     all opened and mutually green. Same-session helpers count only as pre-pass, never as the binding G5.
  9. The proper evidence integrator—not the builder—updates every BUILD ledger row and the product RESULT to DELIVERED
     only after its evidence is opened; frozen artifacts and independent tests remain immutable. Until the whole contour
     is green, status stays CHECKPOINT / NOT DELIVERED.
  10. No Unity/product activation, child feature leg, merge or push ran, and every fresh foreign GasCoopGame_dev path
      is byte-for-byte preserved.

return: |
  Product EXECUTE RESULT HOME with final branch/commit and ancestry from 32107343; exact changed files; independent RED
  commit/author boundary and immutable-test proof; disposition/evidence for every frozen acceptance, NegativeControl,
  Property and ledger row; opened build/test/check/mutation/review/final binding-G5/Deliver artifacts; updated report
  status and rollback; confirmation that construction A/fault A were implemented without crutches, option A stayed
  serial, real workers remained deferred, no Unity/child leg/merge/push ran, and all foreign dev paths were preserved.
  On any contradiction, unavailable required tool or incomplete gate, return CHECKPOINT / NOT DELIVERED with the exact
  blocker and leave the Direction task open. Do not author the next Direction CALL.

budget: one focused L1 execution/delivery leg; mandatory fresh-session gates may force a checkpoint, never a shortcut
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-execute-002-call.md
