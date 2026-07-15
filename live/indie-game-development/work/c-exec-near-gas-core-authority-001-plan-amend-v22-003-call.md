# CALL c-exec-near-gas-core-authority-001-plan-amend-v22-003

> **SUPERSEDED / NEVER ISSUE (2026-07-15):** the owner explicitly forbade this legacy v22 PLAN-AMEND route.
> NearGas L1a was delivered through the experimental skeleton → independent RED → BUILD → fresh-refutation
> carrier and pushed to product `dev` and `main` at exact 400ef8eca1e747378493c97530770286c7e26ff1.
> Do not collect, execute, restore or use this packet to reopen L1a. It is retained only as historical evidence;
> the next workflow action is a separate maintenance B1 session, and L1b remains a separate product leg.

to: executor
direction: indie-game-development
kind: engineering
repo: C:\projects\Unity\GasCoopGame_core
project: GasCoopGame
node: g-9c41
task: NearGas-L1-BUILD
phase: CONTRACT-v22 PLAN-AMEND ONLY
issued: 2026-07-14 (s-work-gascoopgame-contract-v22-resync-close-001)
parent: s-work-gascoopgame-contract-v22-resync-close-001

goal: |
  NearGas L1 has an owner-approved v22 PLAN-AMEND whose frozen packet gives a fresh independent RED-FREEZE author
  a complete, compile-ready behavioral test contract while every non-test obligation is routed to real evidence.

context: |
  This is a new owner-present PLAN-AMEND session. It is not RED-FREEZE, artifact review or BUILD. NearGas-L1-BUILD
  remains active and NOT DELIVERED throughout this call.

  GasCoopGame's repo-local engineering contract v22 is the exact local commit
  874a08258558b556dfecf230ae9a84200ee70afb on branch
  codex/c-exec-gascoopgame-contract-v22-resync-001. Its parent is exact product origin/main
  86e7927f82c1e48a9d5ab7255ac8004dc12c10eb. The commit changes only AGENTS.md, validation.config,
  openspec/README.md, openspec/CHANGE_SPEC_TEMPLATE.md, docs/engineering/ESCAPE-CLASSES.md and docs/FRICTION.md;
  synced_contract_version is 22. Product origin/main remains 86e7927f; the v22 commit is not merged or pushed.

  Read the current v22 authorities first: root AGENTS.md, validation.config, openspec/README.md,
  openspec/CHANGE_SPEC_TEMPLATE.md, docs/engineering/ESCAPE-CLASSES.md and docs/FRICTION.md. The required handoff is
  four separate sessions: PLAN/PLAN-AMEND -> independent RED-FREEZE -> binding fresh artifact review -> BUILD.
  Before RED-FREEZE, split every mixed row and classify every atomic obligation exactly once as `behavioral-red`
  or `evidence-only`. Each behavioral-red row needs an exact test file/method and a complete
  `fixture | call | observe | source | negative` recipe. Each evidence-only row needs a real evidence venue and is
  excluded from the RED numerator. A PLAN/PLAN-AMEND return may route only to RED-FREEZE, never directly to BUILD.

  The current NearGas planning authority was frozen at
  21acd415209dc4261aaa692c13cc56d0e6d9f59f and carried byte-identically through product main
  86e7927f82c1e48a9d5ab7255ac8004dc12c10eb and contract commit 874a0825. The original 12-path planning scope is:
  - AGENTS.md;
  - docs/FRICTION.md;
  - docs/adr/ADR-E-0011-c-exec-near-gas-core-authority-001-atomic-core-owner.md;
  - docs/gas-simulation/dashboard.html;
  - docs/results/c-exec-near-gas-core-authority-001.md;
  - openspec/CHANGE_SPEC_TEMPLATE.md;
  - openspec/README.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/PLAN.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/proposal.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/specs/sim-core/spec.md;
  - openspec/changes/c-exec-near-gas-core-authority-001/tasks.md;
  - validation.config.

  Exact pre-amend raw-Git-blob SHA-256 identity of the five frozen NearGas files:
  - ADR: ccc75150a7de90dd97363f1f3b7f595066cab8e907dfdb2d79ebc53d7495ea10
  - PLAN: bcc9de92f9e4ac0efddb6c066daa66319969599a10d67b2c73549cb44193b3e0
  - proposal: d44ac6df503e649a0bd3732dedeae7c56d18e6fe103ca6cd5d6be7d33c76c704
  - spec: 8419ba161de7787600fac6c20087df819c9c73e7f91f294b520c7075bb42b28e
  - tasks: ab32ed4a43b76d906d7ac75a1722e2a769121b184c65eb421c6c484e22710fe2
  - aggregate: 2f676a071731bd8ae6f787eb4aeb01fdc440e676d476ebc54956eba803ed3a0e

  Binding contract-v22 refutation of the former prose 29/29 found three planning defects:
  1. AR-01, AR-06, AR-12 and AR-13 mix behavioral obligations with path/history/owner-verdict/review/gate evidence.
     Split them into atomic rows and classify each row exactly once. Re-derive the full inventory from the exact
     packet; do not preserve 29 as a target count and do not place evidence-only rows in the RED numerator.
  2. F5 asks for all three VoxelStepResult fields plus flattened pending impulses, but the current packet does not
     freeze a complete reference-result/pending-impulse comparison surface. Define the complete observable surface,
     ownership and comparison recipe so a fresh test author need not invent an API. If this requires a genuinely new
     production symbol, freeze its exact name/signature/semantics and mark the corresponding future RED narrowly as
     compile-RED; otherwise require discovered assertion-RED against existing surfaces.
  3. The four Property rows name CsCheck 3.2.2, seed 0x4E474C31, shrinking and 1,024 cases but do not give a
     compile-ready invocation. Fact-check the locally available/authoritative CsCheck 3.2.2 API and freeze the exact
     generator, sample/check call, seed, case count and shrinking/reporting pattern. Do not guess framework syntax.

  Preserve the already accepted option A: one caller-serialized, non-reentrant, serial concurrency-ready L1; real
  workers remain deferred until delivered L1/L2/C1 and fresh profiling. Preserve the public owned
  NearGasGenerationDefinition.Create(...), immutable built-in Core handler-type maps, literal valid single-cell
  recipe, exact NearGasFaultSite inventory/values and same-private-path ForTesting entries unless first-hand review
  proves an actual v22 planning contradiction. Any such contradiction is presented to the owner; it is never repaired
  silently or by implementation.

  launch:
    lane: A
    venue: C:\projects\Unity\GasCoopGame_core — existing assigned headless core worktree; create NEW branch
      codex/c-exec-near-gas-core-authority-001-plan-amend-v22-003
    machine: ПК
    base: exact local contract-v22 commit 874a08258558b556dfecf230ae9a84200ee70afb
    conflict_surface: NearGas PLAN/proposal/spec/tasks/ADR plus truthful product RESULT/dashboard planning status
    depends_on: [contract-v22 re-sync 874a0825; EXECUTE-003 consumed checkpoint 0/29; L1 active/NOT DELIVERED]
    merge_queue: none in this call; return committed PLAN-AMEND HOME, no merge or push
    gates: actual owner approval before freeze/commit; later RED-FREEZE and binding review are separate sessions

boundaries: |
  At entry fetch read-only, record product origin/main, and verify exact commit 874a0825, its parent 86e7927f, the
  six-path contract diff, stamp 22, clean source worktree, no Unity lock and unused local/remote target branch. Verify
  all five pre-amend raw-blob hashes and preserve a manifest of every foreign worktree/head/dirty path. If the base,
  contract diff, branch availability, frozen identity or worktree changed, STOP with exact drift; do not reset,
  clean, switch a foreign worktree, silently rebase or choose another authority.

  PLAN-AMEND only. The mutable planning surface is limited to the five NearGas packet files: PLAN.md, proposal.md,
  sim-core/spec.md, tasks.md and ADR-E-0011. Update docs/results/c-exec-near-gas-core-authority-001.md and
  docs/gas-simulation/dashboard.html only as truthful PLAN-AMEND / NOT DELIVERED evidence if the repo-local contract
  requires it. AGENTS.md, validation.config, OpenSpec templates/guidance and docs/FRICTION.md are v22 authority and
  must remain byte-identical to base in this leg. Do not reformat unrelated text.

  Do not create or edit production code, tests, test support, fixtures, packages, tools, scenes or Unity assets. Do
  not author RED, run product build/tests/check/review/mutation/Deliver, launch Unity/MCP, implement NearGas, merge or
  push. Read-only inspection of repository types, project/package metadata and locally available authoritative
  CsCheck sources/docs is allowed only to freeze compile-ready planning truth; do not execute a test/build tool.

  Do not use a parser, scanner, schema compiler, prose N/N, skeleton inventory or semantic dry-run as a substitute
  for atomic classification and executable recipes. Do not create test-local helpers or production surfaces merely
  to make the plan look complete. Evidence-only obligations must name real future evidence artifacts, not fake tests.

  Before committing, present the owner a normal human technical brief: exact atomic obligation inventory and class;
  proposed F5 comparison surface; exact CsCheck invocation; any genuine choices with recommendation; resulting
  behavioral RED count and evidence-only count; and the focused file diff. Stop and wait for the owner's actual
  approval/revision/rejection words. A CALL is not approval. Without owner approval, return CHECKPOINT with the same
  PLAN-AMEND still pending and no commit/downstream handoff.

  Preserve all historical checkpoints, publication ancestry, frozen pre-amend identities and foreign worktrees.
  Do not create a Direction CALL. A successful return may name only the eligible phase `separate RED-FREEZE`; it may
  not claim that RED, artifact review, BUILD or feature delivery has started.

done_when: |
  1. Preflight proves exact clean base 874a0825, parent/origin-main relationship, six-path v22 contract diff, stamp 22,
     unused target branch, unchanged five-file pre-amend manifest and preserved foreign worktrees.
  2. The exact current packet is re-derived into a complete inventory of atomic obligations. Every obligation is
     classified exactly once as behavioral-red or evidence-only; AR-01/06/12/13 mixed content is split; no obligation
     is lost, duplicated or retained merely to preserve the historical 29 count.
  3. Every behavioral-red row names one exact future test file and method plus a complete executable
     fixture | call | observe | source | negative recipe. Existing-surface rows require assertion-RED; any narrow
     compile-RED row names only exact genuinely new production symbols and expected diagnostics.
  4. Every evidence-only row names its real future evidence venue, owner/process/review/gate sequence where relevant,
     and exclusion from the RED numerator. No path/history/approval/review/gate obligation is posed as a test.
  5. F5 freezes a complete all-VoxelStepResult-fields plus flattened pending-impulse observable/comparison surface,
     including exact ownership, order/canonicalization, expected data and negative witness, with no API invention left
     to the RED author.
  6. All four Property rows freeze a first-hand fact-checked, compile-ready CsCheck 3.2.2 generator/check invocation
     with seed 0x4E474C31, exactly 1,024 cases, shrinking and useful failure reporting; no guessed package call remains.
  7. PLAN/proposal/spec/tasks/ADR are mutually consistent, owner-readable and stamped contract v22. Product RESULT/
     dashboard, if updated, say only PLAN-AMEND COMPLETE / L1 NOT DELIVERED and record the exact new behavioral/evidence
     counts and identities. Option A and deferred-worker boundaries remain unchanged.
  8. The owner receives the full technical brief and gives actual recorded approval after seeing the final proposal.
     Approval-only edits, if any, are separated from semantic changes and the owner's exact words are reported.
  9. The committed branch has a clean focused planning/evidence diff, new raw-Git-blob SHA-256 manifest and aggregate,
     exact changed-path list, base ancestry and `git diff --check` green. Packet/source/tests/tools/foreign worktrees
     outside the allowed scope remain unchanged; forbidden build/test/RED/Unity/merge/push actions are NOT RUN.
  10. Return HOME as PLAN-AMEND COMPLETE / PRODUCT FEATURE NOT DELIVERED. No RED commit, artifact-review verdict,
      BUILD authorization, merge/push or downstream Direction CALL exists. The only eligible next phase is a future
      separate RED-FREEZE after Direction reconciles this return.

return: |
  Product CONTRACT-v22 NearGas PLAN-AMEND RESULT HOME with base/branch/commit and ancestry; actual owner words;
  exact changed paths and diff summary; complete atomic obligation table with behavioral-red/evidence-only counts;
  every behavioral test file/method and fixture|call|observe|source|negative recipe; every evidence-only venue; exact
  F5 comparison surface; exact CsCheck 3.2.2 invocation; pre/post five-file raw-blob manifests and aggregates;
  product RESULT/dashboard status; foreign-worktree preservation; git diff --check; explicit NOT RUN list; rollback;
  and confirmation that L1 remains NOT DELIVERED and no RED/review/BUILD/merge/push/downstream CALL occurred. If any
  item cannot be met, return CHECKPOINT / NOT DELIVERED with the complete gap list and no downstream handoff.

budget: one focused owner-present PLAN-AMEND leg; checkpoint rather than cross into RED or implementation
surface: any

END_OF_FILE: live/indie-game-development/work/c-exec-near-gas-core-authority-001-plan-amend-v22-003-call.md
