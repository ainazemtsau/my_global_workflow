# CALL c-exec-poligon-checksum-foundation-plan-001 — Checksum Foundation (PLAN ONLY)

> **FIRE-READY PLAN-only.** Run in a fresh owner-present GasCoopGame product session. The session ends after the
> owner-readable technical plan is explicitly approved; RED tests and BUILD belong to a later fresh session.

to: executor
direction: indie-game-development
node: g-9c41
task: M1-A0
repo: C:\projects\Unity\GasCoopGame_core
kind: engineering
change_id: c-exec-poligon-checksum-foundation
runs_in: fresh owner-present product PLAN session only
planning_base: latest origin/main at PLAN start; observed origin/main@a644e5db538d1102f726630d6a4ac2f3f1bdcf5a on 2026-07-11

## goal

An owner-approved implementation contract exists for a low-cost authoritative state-change and synchronization
foundation, so ordinary render/sense/snapshot consumers no longer require a full-domain `MeaningChecksum` scan and
future successor A0, M1-GAS and S4 work can observe committed state without changing its meaning.

## context

- Direction authority: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`;
  `history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md`;
  `history/2026-07-11-s-repair-visual-sim-upstream-001.md`.
- Owner sequencing decision: first establish the checksum/state-change foundation, then resume successor A0. The
  current M1 appetite is the later owner-confirmed maximum **13** product legs; GAS-PROBE and GAS-CORE follow A0,
  c-visual-009 remains blocked on GAS-CORE, and S4 follows the gas-law work.
- Old `c-exec-poligon-a0-001` is terminal STOP / NOT DELIVERED and is immutable evidence, not a branch to resume:
  `docs/results/c-exec-poligon-a0-001.md` and
  `docs/measurements/overlap-c-exec-poligon-a0-001.md` at checkpoint
  `0d2a8ae7084434f46a795efbd913d4c784ed17f3`.
- Read-only preflight on 2026-07-11: `GasCoopGame_core` is clean at that checkpoint while
  `origin/main=a644e5db538d1102f726630d6a4ac2f3f1bdcf5a`; the PLAN must re-check/fetch latest main and must not use the
  stopped branch as its planning base. `GasCoopGame_dev` Phase 0 remains unmerged at
  `f30e3a38ac57102de4ff823a03550082e0d9c8ce` versus the same origin/main and currently has a dirty working tree.
- Engineering contract is synchronized: product `validation.config` and Direction OS are both contract v19.
- Verified pressure: legacy `MeaningChecksum` is an exact sequential full-domain FNV fold; `RealGasViewSource` polls
  it per enabled Unity frame and `PlayerSense` includes it per observation. Historical strong-machine evidence at
  196,608 cells measured Step about 0.4045 ms versus `MeaningChecksum` about 28.2085 ms in
  `docs/measurements/c-exec-023-kernel-scaling-matrix.json`; this is evidence of the problem, not a current guarantee.
- Current Net/FishNet paths do not yet transport or compare this checksum. This PLAN defines the foundation before
  live gas networking/S4 consumes it; it does not claim that networking already exists.

Owner-approved outcome constraints, to be converted by the product Planner into a detailed architecture rather than
treated as a pre-written implementation:

1. Legacy `MeaningChecksum` remains byte-for-byte the exact slow audit/golden/debug oracle; old golden values remain.
2. A separate monotonic state revision serves dirty/change detection and is never called or sold as a checksum.
3. Automatic per-frame/per-sense consumers stop invoking the legacy full-domain checksum.
4. A versioned incremental synchronization digest distinguishes session-static meaning from transactionally changing
   state; an ordinary committed-root read is O(1), and an ordinary sparse step performs no full-domain scan.
5. Successor A0 activity snapshots never call the legacy global checksum; any exact hash exposure is explicitly slow.
6. Sequential FNV is not relabelled as an equivalent incremental hash. The new digest lives beside the legacy oracle.

## boundaries

- **PLAN ONLY:** product code, RED/acceptance tests, BUILD changes, runtime assets, scenes and delivery evidence are
  forbidden in this session. Product planning documents/spec/ADR/tasks are allowed.
- The output must be a detailed but simple owner-readable plan naming every technical decision and why. Machine
  artifacts may accompany it but cannot replace it. Stop for the owner's actual approval words.
- Do not edit, reopen, rebase or continue old `c-exec-poligon-a0-001`; do not plan successor A0 in this change.
- Do not implement or plan M1-GAS, S4, visual movement, damage, reactions, networking behavior or Phase 0.
- PLAN work may occur before Phase 0 merges. Any later checksum-foundation BUILD is blocked until Phase 0 is confirmed
  MERGED, then starts from fresh latest origin/main in a separate builder session.
- Preserve deterministic integer authority, existing serialized/golden meanings and current public behavior unless the
  owner explicitly approves a named user-perceivable change. No GPU/render state may feed Core.
- The Planner owns the detailed representation and algorithms. If the six outcome constraints cannot coexist, STOP
  with the exact contradiction and 2–3 owner-readable options; do not silently weaken a constraint.

## done_when

1. Latest product base and the actual current checksum/revision, mutation, render/sense polling, snapshot and Net/S4
   consumer surfaces are recorded from source; the stopped A0 and unmerged Phase 0 receive explicit dispositions.
2. One detailed owner-readable PLAN explains the problem in plain language, compares credible architectures, selects
   one, and states why it satisfies all six owner-approved outcome constraints without pretending that revision equals
   digest or that an incremental digest equals legacy FNV.
3. The selected contract specifies ownership and lifetime, session-static versus dynamic meaning, versioning,
   transaction/commit/rollback behavior, every mutation entrypoint, data representation, ordinary read/update costs,
   full-scan behavior, failure/rebuild behavior, serialization/compatibility, and how successor A0, M1-GAS and S4 may
   consume it without bypassing the authoritative mutation seam.
4. The evidence design can falsify: legacy-golden drift; missed mutation paths; partial-tick/exception corruption;
   traversal/order or replay nondeterminism; ordinary sparse-step full scans; non-O(1) committed-root reads;
   per-frame/per-sense legacy polling; stale revision/digest reads; session-static mismatch; and unacceptable memory,
   tick or rebuild cost. It names independent RED-first tests, property/negative controls, measured regimes, mutation
   scope, review evidence and binding fresh G5 for the later BUILD.
5. The PLAN makes the later BUILD prerequisite explicit: Phase 0 MERGED, fresh origin/main, separate builder session,
   full repository gates and a separate Direction-OS return before successor A0. It neither authors nor opens that
   BUILD route itself.
6. Owner approval words/token and frozen planning artifacts are committed on a PLAN branch. The returned diff contains
   planning artifacts only: no production code, test, shader, scene, asset, BUILD or delivery change.

## return

Return the PLAN handoff: current base SHA; selected and rejected architectures; owner-readable plan path; frozen
spec/ADR/tasks paths and commit; exact owner approval words/token; Phase-0 disposition; later BUILD prerequisites; and
proof that no code, RED test, runtime asset, scene, successor A0, M1-GAS, S4 or visual BUILD work occurred. Direction
OS will decide and issue any later BUILD route.

## budget

One owner-present PLAN session. Stop at owner approval or at the first irreconcilable constraint; no BUILD in the same
session.

END_OF_FILE: live/indie-game-development/work/c-exec-poligon-checksum-foundation-plan-001-call.md
