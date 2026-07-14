# CALL c-exec-near-gas-core-authority-001-execute-003

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
project: GasCoopGame
node: g-9c41
task: NearGas-L1-BUILD
phase: EXECUTE-003 / independent RED + BUILD
issued: 2026-07-14 (s-work-near-gas-l1-v21-published-binding-001)
parent: s-work-near-gas-l1-v21-published-binding-001

goal: |
  NearGas L1 is delivered as a reviewed, gate-green dormant engine-free Core authority with atomic generation
  replacement and deterministic Step, while every historical checkpoint remains truthful NOT DELIVERED evidence.

context: |
  This is a NEW execution session, not a continuation of the original BUILD or execute-002 checkpoints. Start from
  the exact current published authority and commission a new independent spec-only RED author before implementation.
  The earlier aborted RED attempts left no eligible test commit or surviving evidence and are not reused.

  Published product authority is exact origin/main@9dc4957548111c99980f7efbbb9e7adbda17332b. Its parent is integration
  merge fed1073d53d5894946b8ad6e9ffd14d6c79ec69a, whose parents are
  db69aba6847a47ce2544ad1314f3567b327805d7 and frozen-packet commit
  21acd415209dc4261aaa692c13cc56d0e6d9f59f. Both fed1073d and 21acd415 are ancestors of the published main.

  Fresh Direction binding authority:
  - live/indie-game-development/history/2026-07-14-s-work-near-gas-l1-v21-published-binding-001.md
  - verdict GREEN: 13 Acceptance Requirements + 12 unique NegativeControls + 4 Properties = 29/29 PASS;
    zero unresolved/inferred cells and zero process gaps.
  - this verdict accepts the packet only as execution planning authority. NearGas L1 is still NOT DELIVERED.

  Frozen execution authority at the exact published base:
  - AGENTS.md and validation.config, synced contract version 21;
  - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md;
  - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md;
  - docs/results/c-exec-near-gas-core-authority-001.md;
  - docs/gas-simulation/PROGRAM.md.

  Exact raw-Git-blob SHA-256 identity:
  - ADR: ccc75150a7de90dd97363f1f3b7f595066cab8e907dfdb2d79ebc53d7495ea10
  - PLAN: bcc9de92f9e4ac0efddb6c066daa66319969599a10d67b2c73549cb44193b3e0
  - proposal: d44ac6df503e649a0bd3732dedeae7c56d18e6fe103ca6cd5d6be7d33c76c704
  - spec: 8419ba161de7787600fac6c20087df819c9c73e7f91f294b520c7075bb42b28e
  - tasks: ab32ed4a43b76d906d7ac75a1722e2a769121b184c65eb421c6c484e22710fe2
  - published aggregate identity: 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e

  The packet binds the real public owned NearGasGenerationDefinition.Create(...), immutable built-in Core
  handler-type maps, complete F0-F8 fixtures/oracles, finite domain/fault/permutation catalogs, exact internal
  NearGasFaultSite values and same-private-path ForTesting entries. It keeps option A: one caller-serialized,
  non-reentrant, serial concurrency-ready L1. Actual workers remain a separate future leg only after delivered
  L1/L2/C1 and fresh profiling.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core — existing assigned headless core worktree; create NEW branch
      codex/c-exec-near-gas-core-authority-001-execute-003
    machine: ПК
    base: origin/main @9dc4957548111c99980f7efbbb9e7adbda17332b (exact; if it moved, STOP and return)
    conflict_surface: NearGas Core authority, source/reaction/flow/loopback seams, new independent tests and gate evidence
    depends_on: [published v21 packet at 9dc49575; fresh Direction binding GREEN at s-work-near-gas-l1-v21-published-binding-001]
    merge_queue: one exclusive mutating lane-A slot; return final branch/result HOME, no merge or push in this CALL
    gates: new independent spec-only RED first; different-family final-tip review; binding G5 = separate fresh session;
      owner-eye = n/a for dormant engine-free L1

boundaries: |
  At entry recheck that C:\projects\Unity\GasCoopGame_core is clean, has no Unity lockfile, lane A has no other
  mutating leg, the new branch name is unused, origin/main is the exact base above and contract stamp is exactly v21.
  Create the branch from that base. Dirty/occupied worktree, conflicting branch, moved base, changed packet blob or
  contract drift is STOP; do not reset, clean, overwrite, silently rebase or accept a new base.

  Do not assign, switch, clean, stage, overwrite or otherwise use C:\projects\Unity\GasCoopGame_dev for this leg.
  It contains foreign uncommitted work and is non-authoritative. Never reuse its pre-existing untracked NearGas
  fixtures as RED evidence. Do not use C:\projects\Unity\GasCoopGame as the authoritative working venue.

  The independent test-author is a fresh role and reads ONLY the exact frozen sim-core spec before authoring. It first
  owns and commits all 13 requirement witnesses, all 12 named NegativeControls and all four required Property tests
  under a fresh non-colliding NearGas test path. Only after that immutable RED commit may the builder read production
  implementation and build. The builder SHALL NOT edit the independently authored tests.

  The builder SHALL NOT edit or reinterpret frozen PLAN.md, proposal.md, sim-core spec, tasks ledger, ADR-E-0011 or
  acceptance meaning. Only the proper non-builder evidence integrator may flip ledger rows or update the product
  RESULT/dashboard after opening their required evidence. No local redesign repairs a contradiction: STOP and return
  CHECKPOINT / NOT DELIVERED with the exact frozen gap.

  Implement exactly amended option A. Do not add Thread/Task/Parallel, jobs, workers, worker counts, scheduler,
  partitions, locks, concurrent collections or public thread-safety surfaces. Do not open the future concurrency leg.
  Real workers stay deferred until delivered L1/L2/C1 plus fresh profiling and a separate Direction-issued CALL.

  Do not add L2 limits, C1 digest/revision, M0/L3 Unity authority, PlayerSense, render, replay, networking/save,
  runtime emitter movement, doors/topology/destruction, legacy deletion, Phase 0 or c-visual-009 scope. Do not launch
  Unity, PlayMode, MCP or a game build; this L1 is engine-free/headless. Do not merge or push in this CALL.

  Contract v21 is binding: this CALL, product AGENTS.md, frozen packet and validation.config are the execution
  authority. Optional global skills/tools cannot add requirements or become blockers. A repo-authority-required tool
  becoming unavailable is STOP under contract v16; never substitute a source scan, parser, checker or reduced-fidelity
  proxy for behavior or semantic evidence.

  Preserve as immutable history: original BUILD checkpoint b94806deaaa3cbb56a8b6cda9baa75ac52f028c3, execute-002
  checkpoint 5c783e07b5378dece1e0664b203c4e147edacd68, owner-approved v21 packet commit
  21acd415209dc4261aaa692c13cc56d0e6d9f59f and its publication ancestry. Never resume, rewrite, squash into or
  present a historical checkpoint as this execution's RED/BUILD ancestry.

done_when: |
  1. Preflight records exact project/worktree/new branch/base, clean status, no Unity lock, exclusive lane-A slot,
     repo contract v21, unchanged five-blob packet identity and fresh foreign-work preservation. Ancestry starts at
     origin/main@9dc49575; historical checkpoints remain historical.
  2. A new independent spec-only RED author first commits executable coverage for all 13 requirement identities,
     all 12 unique NegativeControls and all four Properties, with every exact fixture/call/observe/source/negative
     recipe and skeleton instantiated without reading production, reusing old/dev fixtures or inventing a crutch.
     RED evidence proves discovery and the intended absent/wrong failure before production implementation begins.
  3. One dormant engine-free NearGasSimulation owns a defensively built generation, exact minimal scalar read and one
     complete deterministic Step through the existing kernel with candidate-only preparation and one non-throwing
     commit; no raw mutable state, formula copy, full-field clone, catch/restore or second transaction exists.
  4. Construction A is exact: public owned Create(...), two immutable Core kind-to-System.Type maps and the frozen
     literal recipes work; caller alias mutation is inert; the complete definition/domain/replacement/null corpus
     preserves none/old generation, ids, reads, counters and hidden state; no fixture/reflection/mutable registry,
     builder, handler instance or alternate construction path appears.
  5. Fault A and handler extensibility are exact: the frozen selector inventory/values and internal entries share the
     public private paths; None parity, mismatch/undefined rejection, all sites, counters, terminal primer and
     retry-twin continuation pass; handler aliases, exact one-defect masks, fresh object ownership and semantic
     product/arity validation pass without callbacks/controllers/global fault state or numeric-only dispatch.
  6. Exact input/result/domain/order/emitter/canonicalization behavior passes the full F0-F8 and F7-DOMAIN/
     F7-FAULT-CONTRACT/F7-PERMUTATION/F7-COMMAND-REFERENCE catalogs, including full zero-bearing mass/read evidence,
     source/event/impulse order, aperture/valve duplicate/conflict rules and every same-assertion wrong subject.
  7. Exact legacy MeaningChecksum/StructureChecksum goldens, source isolation, OpenDoorFlow and full default/typed/
     false-source loopback mapping remain unchanged through explicit slow CaptureLegacyAudit only. Ordinary
     replacement/read/Step/result performs and publishes no full-domain FNV; loopback calls public Step once per
     peer/tick, the raw overload is absent and generation ids remain local.
  8. Option A remains serial concurrency-ready: owned immutable inputs, canonical semantic order, stateless handlers,
     generation/Step-owned scratch and one serial commit; no worker/scheduler surface or speedup/thread-safety claim
     enters L1.
  9. Core build/tests, repository checks, all NegativeControls, all Properties, zero-float/int-overflow plants,
     diff-scoped mutation >=70, independent different-family final-tip review, finding disposal, binding fresh-session
     G5 and tools/check.ps1 -Deliver are opened and mutually green. Same-session helpers count only as pre-pass.
  10. The proper evidence integrator—not the builder—updates every BUILD ledger row and the product RESULT to
      DELIVERED only after opening all evidence. Frozen packet and independent tests remain immutable; no Unity/
      product activation, child feature leg, merge or push ran; every foreign GasCoopGame_dev path is preserved.

return: |
  Product EXECUTE-003 RESULT HOME with final branch/commit and ancestry from 9dc49575; exact changed paths; immutable
  independent RED commit/author boundary; disposition/evidence for every one of the 29 identities and ledger rows;
  opened build/test/check/NegativeControl/Property/mutation/review/binding-G5/Deliver artifacts; updated report status
  and rollback; confirmation that construction A/fault A used no crutches, option A stayed serial, workers remained
  deferred, no Unity/child leg/merge/push ran and foreign dev work was preserved. On any contradiction, moved base,
  unavailable required tool or incomplete gate, return CHECKPOINT / NOT DELIVERED with the exact blocker and leave
  the Direction task open. Do not author the next Direction CALL.

budget: one focused L1 execution/delivery leg; mandatory fresh-session gates may force a checkpoint, never a shortcut
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-execute-003-call.md
