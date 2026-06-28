# s-work-024 — work (g-9c41 / S2): FRAME + HARDEN the S2 executor CALL (c-exec-016)

Date: 2026-06-28
Play: work
Direction / node / task: indie-game-development / g-9c41 / S2 (multiplayer lockstep loopback)
Job: session (writer-after-RESULT on this OS repo)

## outcome

The S2 executor CALL is FRAMED + adversarially HARDENED → `work/c-exec-016-call.md` (build-ready).
S2 stays ACTIVE awaiting its executor return; the CALL is ready to OPEN in a fresh GasCoopGame_dev session (PLAN, owner present).
This session FRAMED the outcome + evidence pointers only — it did NOT design the solution (architecture = the build session's
PLAN, owner present) and changed NOTHING in the lock.

The CALL frames S2 = the coarse integer sim produces the SAME per-tick MeaningChecksum on 2 PROCESSES (host + 1 follower,
loopback, ONE machine) over a SEEDED scenario that EXERCISES the S1 forced-flow events (выброс / ветер-fork / one-way valve /
jet) + CONCURRENT same-face writes; determinism BY CONSTRUCTION (integer-only + build-time zero-float scan + single-owner-
per-face + gather-then-apply + canonical traversal order + seeded RNG + integer mass-clamp with loud asserts), NOT via
re-flux, NOT via 2 physical machines; a divergence HALTS LOUDLY (canon Факт-1).

Key framing sharpenings (verified against the committed canon, NOT invented):
- **NOT a from-scratch build.** The loopback hash was seeded in S0 (optional ordering/RNG tripwire) + extended in S1
  (bias in checksum + concurrent same-face writes). S2 ELEVATES it to the load-bearing slice. Genuine artifact to elevate =
  `F11LoopbackDeterminismTests` (verified to exist). Two decoys fenced: the `Core/Sim` ADR-0002 8×8 toy + `CoarseChunkFollower.ComputeHash`.
- **Migration spine** (canon §8:184 / §7:162): the Wave-1/2 host-broadcast reconstruction is LEGACY under input-lockstep —
  TWO families (coarse chunked-delta + field-state-channel) + the Факт-5-buried late-join/snapshot path. The PLAN inventories
  first-hand + decides port-vs-delete under ZERO-LEGACY; a 2-band-as-authority resurrection guard added.
- **ведро classification:** S2 is the determinism/replication SUBSTRATE → ведро-2 backbone (the FULL canon §9.5 in-checksum
  meaning-set proven byte-identical); ведро-1 EXCLUDED (count-IN / bitmap-OUT §9.5 trip-wire held); ведро-3 ABSENT (arrives S4).

## evidence (matches done_when of the work task = the CALL artifact exists + is hardened)

- Artifact: `live/indie-game-development/work/c-exec-016-call.md` — all six KERNEL §4 CALL fields present
  (goal / context / boundaries / done_when / return / budget) + discipline + ведро classification + END_OF_FILE trailer.
- Adversarial hardening: workflow `wf_6a2fc85f-06e` — 32 agents, 8 adversarial lenses (determinism / lock-integrity / scope /
  drift / verifiability / ведро / migration-legacy / format) → per-finding refute-verify → synthesis. 22 raised → 12 survived
  refutation → **2 must-fix + 5 should-fix** folded; ZERO lock-change, ZERO re-design (all text-only). The refute pass killed
  the weak findings (the "approach-token" and "re-sync" parity findings refuted as ungrounded; several "already-covered" rejected).
- Folds applied: (M1) three determinism RED controls added to done_when 4 (awake-queue permutation / region-fold-order /
  per-meaning-field divergence); (M2) ZERO-LEGACY rescoped to the WHOLE reconstruction spine, inventory-first, incl. the
  Факт-5 late-join path; (S1) ведро-2 = full §9.5 membership + count-IN/bitmap-OUT trip-wire; (S2) §9.5 canon pointer added;
  (S3) 2-band-authority §7 resurrection warning; (S4) F11 / Core.Sim decoy fence; (S5) prior-artifact pointers.
- Symbol verification (first-hand, GasCoopGame `main` tip `eed321b`): all baked-in symbol names confirmed to exist —
  `IFieldStateChannel` / `InMemoryFieldStateChannel` / `FishNetFieldStateChannel` / `FieldStateBroadcasts` / `FieldStreamDriver` /
  `FieldSnapshot` / `FieldState` / `FieldDelta` / `CoarseChunkFollower` / `ChunkEncoder` / `ChunkDecoder` / `RevisionBarrier` /
  `LoopbackCoarseChunkHub` / `ICoarseChunkLink`; `F11LoopbackDeterminismTests`; `Core/Sim` `SimCore`/`SimState`/`SimInstance`/`ITickInputBus`;
  bonus `RW5OrderIndependenceTests` (S1 order-independence harness). No unverified symbol was asserted as fact.

## play_check (work play steps)

1. Recite — DONE. Restated S2 goal/done_when + the bet (g-9c41 rolling-wave slice S2); confirmed S2 active, fork resolved.
2. Owner inputs (owner) — SKIPPED w/ reason: the CALL is a machine artifact for the build session, NOT owner-content the owner
   lives by/operates/sends as his own; no owner-only inputs are required to FRAME it. The owner participates at the build PLAN
   (where architecture is decided) — explicitly deferred there, per the work-play call:executor rule.
3. Do the work (call:executor) — DONE. Framed the full executor CALL (outcome + evidence pointers; did NOT design the solution).
   Optional adversarial hardening run (as S0/S1 CALLs were hardened). CALL recorded into open_calls (state_changes).
4. Self-check — DONE. Compared the artifact against the work-task done_when point by point (all six CALL fields + ведро
   classification + the task's mandated done_when content: loopback hash incl. forced-flow + concurrent writes + follower
   parity + zero-float + -Deliver + fresh-session G5 + STOP-discipline). Every baked-in symbol traced to a first-hand grep.
5. Close — DONE (this RESULT). Task S2 stays ACTIVE (awaiting executor return); next = open c-exec-016.

## state_changes
- NOW.md open_calls: + c-exec-016 (status: framed).
- NOW.md active_tasks S2: status note updated (CALL framed+hardened; next = open in GasCoopGame_dev).
- NOW.md next: IMMEDIATE NEXT updated FRAME→OPEN c-exec-016; push paragraph += s-work-024 commit.
- LOG.md: + one line.
- history/s-work-024.md: this file.

## captures
- (none new) — the hardening surfaced an existing `LoopbackCoarseChunkHub`/`ICoarseChunkLink` loopback coarse-chunk path
  in-tree; recorded inside the CALL's migration-spine inventory (the PLAN dispositions it), not a separate capture.

## decisions_needed
- (none) — everything S2 needs was already decided (fork resolution + the 4-decision bundle, s-work-023). No new owner decision.

## log
2026-06-28 — work (g-9c41/S2): c-exec-016 (multiplayer lockstep loopback) executor CALL FRAMED + adversarially HARDENED.

## next
OPEN c-exec-016 in a FRESH GasCoopGame_dev build session (opens with a PLAN, owner present, §Re-sync contract FIRST).
RESULT applied home by a separate OS writer. Closes S2 done ONLY on c-exec-016's GREEN return (2-process loopback hash +
follower-parity + zero-float + -Deliver + fresh-session G5). May split (PLAN scopes). next slice after S2 = S3 (height/layering).

END_OF_FILE: live/indie-game-development/history/s-work-024.md
