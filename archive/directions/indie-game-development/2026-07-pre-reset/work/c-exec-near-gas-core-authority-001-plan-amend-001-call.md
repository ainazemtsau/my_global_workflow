# CALL c-exec-near-gas-core-authority-001-plan-amend-001

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
node: g-9c41
task: NearGas-L1-BUILD
phase: PLAN-AMEND
issued: 2026-07-13 (s-work-near-gas-l1-build-checkpoint-001)
parent: c-exec-near-gas-core-authority-001-build-001

goal: |
  Produce an owner-approved frozen amendment that makes the NearGas L1 independent RED contract executable from the
  spec alone, without widening L1 or changing the accepted serial concurrency-ready option A.

context: |
  The original owner-approved PLAN is commit 1e4e78c12510ad4e2e0e9fcaa2a490f8d073fba8, merged into product
  origin/main at 13917123f71aaa556bac0991021ee5793fb50bc1. The separate BUILD started on
  codex/c-exec-near-gas-core-authority-001-build-001, completed contract §Re-sync v19→v20 in
  7cb8fbc40eb4b1724414ff089b07c3a8b5493caa and stopped cleanly at checkpoint
  b94806deaaa3cbb56a8b6cda9baa75ac52f028c3 before any test or implementation commit.

  The blocking evidence is in docs/results/c-exec-near-gas-core-authority-001.md. The frozen sim-core spec currently:
  - binds ReplaceGeneration(NearGasGenerationDefinition) at line 46 and says what the definition owns at lines 70–73,
    but binds no constructor, factory or spec-only fixture that can construct an admitted definition;
  - requires throw plants at six minimum internal fault sites at lines 265–267 while intentionally leaving exact
    private fault enum/member names unconstrained at line 444, so a spec-only test author cannot address those sites.

  The prior owner verdict remains binding: «Я подтверждаю твой рекомендованный вариант А» and «по плану я
  подтверждаю … и там двигаемся дальше». It approved a serial concurrency-ready L1. Actual multithreading remains a
  separate possible c-exec-near-gas-concurrency-001 only after delivered L1/L2/C1 and fresh profiling.

  Binding authority to reconcile:
  - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md
  - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md
  - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md
  - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md
  - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md
  - docs/results/c-exec-near-gas-core-authority-001.md
  - docs/gas-simulation/dashboard.html

  The original BUILD CALL stays pending and blocked. This amendment neither resumes it nor authorizes a builder. A
  later fresh Direction binding-refutation decides whether the amended authority is sufficient and what BUILD resume
  packet, if any, may be issued.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core (assigned exclusive core worktree; headless planning; no Unity Editor)
    machine: ПК
    base: checkpoint branch codex/c-exec-near-gas-core-authority-001-build-001 @b94806deaaa3cbb56a8b6cda9baa75ac52f028c3, on origin/main @13917123f71aaa556bac0991021ee5793fb50bc1; contract v20 already synced @7cb8fbc4
    conflict_surface: frozen NearGas L1 planning/spec/ADR/evidence authority only
    depends_on: [clean BUILD checkpoint @b94806de; original BUILD remains pending]
    merge_queue: same exclusive lane-A slot; PLAN amendment only, no product-main merge
    gates: owner verdict on both new contract shapes; later G5=fresh Direction session; owner-eye=n/a

boundaries: |
  PLAN-AMEND only. Do not create or edit production code, tests, RED fixtures, scenes, packages or gate scripts; do
  not run RED, tests, mutation, review execution, tools/check, Unity Editor, PlayMode, MCP, game build or child legs.
  Read-only product-source inspection is allowed only as planning evidence; the resulting frozen contract must still
  be sufficient for a future independent author who reads the spec and no production source.

  No frozen amendment may be committed until the owner gives actual words approving one exact constructible
  generation-definition/fixture contract and one exact stable fault-site test contract in this fresh session. The
  prior option-A verdict does not answer these two newly surfaced questions. Without both verdicts, return a
  checkpoint with the frozen authority unchanged.

  Change only the minimum planning/spec/ADR/evidence text needed to close these two gaps. Do not redesign L1, relax
  atomicity or kernel fidelity, add L2/C1/L3 APIs, make private implementation names public, or add actual threads,
  tasks, parallel workers, schedulers, partitions, locks or speculative concurrency tests.

  Preserve commits 7cb8fbc4 and b94806de, every unrelated product path and all ten foreign GasCoopGame_dev paths.
  Work from a dedicated codex/c-exec-near-gas-core-authority-001-plan-amend-001 branch created at the checkpoint. Do
  not merge or push to product main, and do not resume the original BUILD or author its successor CALL.

done_when: |
  1. The frozen amendment records the owner's actual approval words for one exact construction contract and one exact
     stable fault-site test contract; without both, status remains CHECKPOINT / AUTHORITY UNCHANGED.
  2. From the amended spec alone, a fresh independent test author can construct valid and deliberately invalid owned
     generation definitions with exact topology, roster/configuration, initial mass, emitters and handler roster, then
     exercise replacement, Step, golden, permutation and stale-read cases without reading production source or
     inventing an API/fixture.
  3. From the amended spec alone, that author can select each of the six required fault phases independently and prove
     whole-operation atomicity/retry equivalence without depending on private enum/member names or widening the public
     production surface; unused/private implementation details remain unbound.
  4. PLAN, proposal, sim-core spec, tasks ledger, ADR and evidence map agree on both contracts, their ownership and
     their exclusion boundaries. Every BUILD ledger row remains default-failing and no implementation/test evidence
     is fabricated.
  5. The accepted option A remains serial concurrency-ready with one serial commit; c-exec-near-gas-concurrency-001
     remains unopened until delivered L1/L2/C1 plus fresh profiling, and no Unity or child-leg scope enters L1.
  6. A committed PLAN-AMEND branch tip has a clean focused diff, exact changed-file list and updated report/dashboard
     status PLAN AMENDED / BUILD CHECKPOINT / NOT DELIVERED; production/tests are unchanged and all ten foreign dev
     paths are byte-for-byte preserved.

return: |
  Product PLAN-AMEND RESULT HOME with the owner's exact two verdicts; final branch/commit and ancestry; exact changed
  files; a spec-only constructibility/addressability matrix covering done_when 2–3; frozen-artifact consistency and
  diff-check evidence; confirmation that no RED/tests/BUILD/review execution/Unity/MCP/child leg/merge/push ran, option
  A and the future measured-concurrency boundary stayed intact, and all ten foreign dev paths were preserved. Keep the
  original BUILD status CHECKPOINT / NOT DELIVERED and return to Direction for a separate fresh binding-refutation.

budget: one owner-present PLAN amendment session; no RED, BUILD or Unity execution
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-plan-amend-001-call.md
