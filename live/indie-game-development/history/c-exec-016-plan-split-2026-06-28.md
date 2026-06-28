# c-exec-016 PLAN RESULT (imported) — S2 PLAN concluded SPLIT-NEEDED

Imported 2026-06-28 by s-work-025 from the GasCoopGame_dev build-session PLAN (owner present). Source of truth =
GasCoopGame project memory `c-exec-016-plan-progress.md` (originSessionId 9f3bc0a8-9138-424c-9c7d-04c2d12a4e4c). The PLAN
session made NO code/git/openspec changes (PLAN-only; STOP after split-needed per the CALL's budget clause). This file is
the home-side record of that hand-back; the OS application of it = s-work-025.

## PLAN conclusion = SPLIT-NEEDED (owner «Split S2a+S2b»)

done_when 1 (PLAN) DONE. The c-exec-016 (S2 multiplayer lockstep loopback) scope was found too big for one leg → split.
Build runs as FRESH executor sessions under direction-authored sub-CALLs (the builder does NOT author them).

## Owner-signed PLAN decisions (2026-06-28)

1. **SPLIT** → **S2a** = ZERO-LEGACY reconstruction-spine RETIREMENT (delete both legacy families + keep/prune surgery +
   rewrite tests, all green, NO new behavior); **S2b** = lockstep loopback LOAD-BEARING (2-endpoint hash over the FULL
   forced-flow scenario + all RED controls + Adapters R14 3-mode owner-eye + frozen spec). Direction authors both sub-CALLs.
2. **done_when 2(b) RNG control = Variant A → DROP as inapplicable + record intentional spec-silence.** There is NO RNG on
   the gas authoritative path (deterministic-by-INPUT; the only RNG is the out-of-scope ADR-0002 Sim toy). The
   order/wrap/permutation controls (2a / 2c / 4e / 4f) cover the determinism-catch role. Reconciliation routed home →
   d-s2-rng-control-na-001.
3. **ZERO-LEGACY scope:** DELETE both reconstruction families; KEEP store/reducer/far-tier/input-bus.
4. **Housekeeping (approved, deferred to the S2a build session):** FF `dev` up to `main` (clean `--ff-only`, `dev ⊆ main`)
   + archive `c-014`/`c-015` openspec folders.

## Base correction (verified first-hand at the PLAN)

Build base = `main` @eed321b (NOT stale `dev`, which was ~22 behind; `dev ⊆ main`). `main` = 864 engine + ~106
visual-track tests ≈ 970 (resolves the CALL's "970"). The visual track (c-visual-001 S1–S3) touched ZERO `Core/**` → engine
Core on `main` == `dev`; S2 won't conflict. FF is a clean fast-forward — do it BEFORE any new dev commit.

## Migration-spine port-vs-delete inventory (done_when 6, inventory-first; 7-agent workflow wf_89e9d3c2)

- **DELETE — chunked-delta family** (test-only consumers, §7-buried): CoarseChunkFollower, ICoarseChunkLink,
  LoopbackCoarseChunkHub, FishNetChunkChannel (+ChunkBatchBroadcast), ChunkEncoder, ChunkDecoder,
  Chunk/ChunkBatch/ChunkCodecParams/ResolutionKey, RevisionBarrier.
- **DELETE — field-state-channel family:** IFieldStateChannel, InMemoryFieldStateChannel, FishNetFieldStateChannel
  (+FieldStateBroadcasts), FieldSnapshot (Факт-5 late-join), FieldDelta, FieldStreamDriver (+DesyncException), FieldHost,
  FieldHostFactory.
- **KEEP — survives lockstep / live infra:** FieldState/ZoneRecord/FieldStep (store+reducer reused by Layers; DROP the
  «followers must not re-run» framing + the Follower_OnlyMutatesViaApply guard — ADR-0010 inverts it; prune snapshot/
  delta-only mutators); CellHash (shared by surviving CoarseBandStore.Hash()); 2-band far-tier (keep-as-far-tier §8,
  retires at S4); RevisionFeed/IGridEventBus (live layer bus — NOT RevisionBarrier); FishNetTickInputBus/
  TickInputBroadcasts (surviving input-lockstep wire).
- **OUT-OF-SCOPE — leave untouched:** Core/Sim/* (ADR-0002 8×8 toy; 4 live consumers + accepted ADR; retiring it = a
  separate owner/ADR decision).
- **§7-burial check PASSED:** nothing anchors BandCount=2 as an authoritative collapse target (only coupling =
  CoarseChunkFollower.SectorMass, itself deleted).
- **Tests:** ~25 reconstruction/chunk/field-stream suites REWRITTEN or DELETED (Факт-6); EncapsulationGuardTests WireDtos
  whitelist edited; LayerRegistryTests oracle re-anchored on FieldStep; the DW9 input-bus coexistence assertion EXTRACTED
  before its file is deleted.

## Lockstep architecture (for S2b — done_when 2/3)

Genuine artifact = VoxelField.MeaningChecksum + the F11 two-endpoint re-run harness (ELEVATE). "Follower" = a 2nd VoxelField
re-running the same input stream (NOT the deleted CoarseChunkFollower); follower-parity = host-VoxelField.MeaningChecksum ==
follower-VoxelField.MeaningChecksum each tick. "2 process" = ONE machine, 2 in-process endpoints (in-process, NO UDP); gate
= -Deliver green; owner-eye shows endpoints agree; real 2 PCs = optional one-off, NEVER a gate.

## §9.5 / done_when 4(g) (for S2b)

3 named fields (bias register, region_id, face-state) all folded TODAY in MeaningChecksum (VoxelField.cs:236–326). ~20
foldable near-tier fields exist. NOT-YET-BUILT §9.5 members (scoped out + spec-silence): per-type/per-layer coarse mass,
promo-events, TypeId value (1 species), page-id, awake-queue order, loot-dose D6. Bitmap OUT-by-design (StructureChecksum
separate — count-IN/bitmap-OUT; add a negative-control row). Uniform fields (resolution/representation/cap/tick_divisor)
need single-cell/two-grid mutation to prove non-silent-absence.

## Gates / spec-hardening notes (for both legs)

check.ps1 = 5 always-run (core build, headless, hygiene, zero-float scan, int-overflow scan) + 4 -Deliver (RESULT fields,
leg-completion status, strong-check [mutation≥70 + spec-silence + ledger], coverage). AUTO-COVERAGE SEAM: both scans
hardcode $DefaultRoots=[Core/Field/Voxel, Core/Field/Structure] — any NEW authoritative subtree MUST be appended to BOTH
scan scripts as an explicit done_when bullet (else vacuously green). c-016/S2b IS G0-frozen → openspec/changes/<id>/ +
frozen spec + ledger + spec-silence + coverage + mutation-<id>.json ≥70 (floor tight: c-015 = 72.7%). -Deliver re-scans ALL
non-archived frozen folders → archiving c-014/c-015 removes coupling. RESULT.md status must read DELIVERED (not
"DONE-pending-owner-confirm") or -Deliver throws; owner-eye recorded as a separate owner-run step (c-015 pattern).
Spec-hardening RED criteria: F11 c-014 determinism stays green; Layers survive the channel delete; EncapsulationGuard
whitelist updates with deleted DTOs; CoarseBandStore.Hash() determinism holds (CellHash kept); input-bus coexistence preserved.

END_OF_FILE: live/indie-game-development/history/c-exec-016-plan-split-2026-06-28.md
