# c-exec-018 (S2b) RESULT — imported + verified — load-bearing lockstep loopback (determinism by construction)

Imported + verified first-hand 2026-06-29 by s-work-028 from the GasCoopGame build session. Source of truth = GasCoopGame
`origin/main` RESULT.md @ the merge `adb9255`. S2b = the SECOND half of the S2 split (d-s2-split-001); its delivery CLOSES
the whole S2 slice (S2a + S2b).

## outcome (builder, verified)

The two-VoxelField loopback determinism proof is now LOAD-BEARING over the full S1 forced-flow scenario: a new engine-free
`Core/Field/Determinism/` harness replays a recorded integer input stream on two INDEPENDENT endpoints, asserts
byte-identical (MeaningChecksum, StructureChecksum) each tick, and HALTS LOUDLY (fail-fast) on first divergence.
Determinism BY CONSTRUCTION (integer path + the build-time zero-float scan, the #6 auto-coverage seam extended to the new
subtree). §9.5 membership verified against canon (count-IN/bitmap-OUT); not-yet-built members spec-silenced. Lock = ADR-0002,
NOT reopened. ADR-0017.

**Status: DELIVERED + MERGED + PUSHED 2026-06-29 (owner-authorized after a clean code review).**

## first-hand verification (s-work-028)

- Merge: `origin/main` = `adb9255` (`--no-ff` merge; parents `2e24a24` (post-S2a) + `3197694` (S2b leg tip)); merged tree
  = the as-tested dev tree (handback). ✅
- Deliverable EXISTS on main: `Assets/GasCoopGame/Core/Field/Determinism/` = `LockstepLoopback.cs` +
  `LockstepDivergenceException.cs` (the loud halt) + `MeaningMembers.cs` + `GasScenario.cs`. ✅ (a real harness, not a stub.)
- `docs/adr/ADR-0017-s2b-lockstep-loopback.md` present. ✅
- Lock intact: the S2a-deleted families (CoarseChunkFollower / IFieldStateChannel / FieldSnapshot) still 0 production hits
  on main → ADR-0002 not reopened, no resurrection. ✅
- RESULT.md on main = DELIVERED + MERGED + PUSHED. ✅
- Gate evidence (accepted from RESULT.md + the build session's binding fresh-session G5; not re-run from the OS repo):
  check.ps1 -Deliver GREEN · headless 923/923 (902 baseline byte-identical) · mutation 73.51% ≥70 · coverage 10/10 ·
  fresh-session G5 (Sonnet, different family) COULD-NOT-REFUTE on 9 targets · post-delivery: 3 Codex review rounds + a
  5-skeptic adversarial convergence panel, all COULD-NOT-REFUTE, no active holes.

## SCOPE-HONESTY (important — what S2 did and did NOT prove)

S2 proved DETERMINISM BY CONSTRUCTION in a 2-process LOOPBACK (two in-process VoxelFields, ONE machine) — the foundation
the cheap detail/event model + S4 no-pop ride on. It did NOT wire gas into the actual networked tick-input-bus: the
genuinely seam-crossing multiplayer version (gas as an `ITickInputBus` citizen + the per-peer-secret false-green guard) is a
LARGER seam the builder explicitly defers to ~S4. "Multiplayer determinism foundation" = DONE; "gas is a live networked
lockstep citizen" = a named later seam. (Consistent with canon: S2 = loopback gate; real networking = the R14 edge wrapper.)

## findings for the next direction CALL (captures / deferrals)

1. **Scan-root parity gap (HARDENING — flag for the S3 PLAN):** `Core/Field/{FieldStep,FieldState}.cs` (+ `Coarse/Chunks`)
   sit OUTSIDE both determinism scan roots, and `$DefaultRoots` is duplicated verbatim in the two scan scripts with nothing
   enforcing parity → a float could slip into an authoritative subdir undetected (vacuous-green class). Builder's fix idea:
   a self-test asserting every authoritative `Core/Field` subdir is listed in BOTH scans. Cheap; address at the S3 PLAN or a
   small hardening leg.
2. **Gas-as-`ITickInputBus`-citizen** (the networked lockstep version + per-peer-secret false-green guard) → a larger seam,
   likely ALONGSIDE S4.
3. **Chunk-span geometry retirement** (`CoarseChunkSpan`/`IsWireEncodable`/`ChunkSpan`/`ChunkCount`) → fold into the S4
   2-band far-tier cleanup (carried from S2a).
4. **ADR numbering across tracks:** engine ADR-0017 (this leg) vs the visual track on dev2 (holds 0013/0014/0015) — no
   collision yet, but a future visual ADR could claim 0017. Process note: rename-by-track if it happens.

## next

Next slice = **S3 (height / layering)** — canon §5 S3 (near real-height already emergent from S0; the coarse FAR-tier gets
a few VERTICAL layers for height-routing in player-LESS rooms — NOT near "crouch bands"). Open question for its PLAN: the
far-rollup vertical-strata count (canon §6 п.4, decided at PLAN S3/S4) + the S3-vs-S4 far-tier sequencing. The direction
frames the S3 executor CALL (PLAN-first, ведро classification); a fresh GasCoopGame_dev session builds it (owner present).

END_OF_FILE: live/indie-game-development/history/c-exec-018-s2b-result-2026-06-29.md
