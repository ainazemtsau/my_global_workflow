# CALL c-exec-018 — S2b: LOCKSTEP LOOPBACK LOAD-BEARING — детерминизм ПО ПОСТРОЕНИЮ на 2 эндпойнтах

Direction: indie-game-development / g-9c41 / S2b. The SECOND half of the S2 split (d-s2-split-001). Builds on the CLEAN
post-S2a base: c-exec-017 (S2a, ZERO-LEGACY reconstruction-spine retirement) DELIVERED + merged to GasCoopGame `main`
@2e24a24 (both pre-lockstep host-authoritative families deleted; 857/857; -Deliver GREEN; fresh-session G5 COULD-NOT-REFUTE).
Executor: a FRESH GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner present).
State source = NOW.md (active_tasks S2b). Canon = knowledge/g9c41-gas-engine-SPEC.md (§Факт-1, the «Детерминизм—как-гарантируется»
§2 paragraph (d-reflux-gate-001), §5 S2, §8, §9 шов 5 / §9.5 («Чексумм покрывает СМЫСЛ»); **§1 ADR correction: the
input-lockstep lock = ADR-0002, NOT ADR-0010 — ADR-0010 is the test-sandbox**).

## Why this leg (and the lock id)

S2a retired the legacy host-authoritative reconstruction spine; the tree is now ZERO-LEGACY under input-lockstep. S2b
ELEVATES the loopback determinism proof to LOAD-BEARING on that clean base — it is the netcode determinism core the cheap
detail/event model + S4 no-pop ride on (canon §5 hidden-deps). The fork is resolved (lockstep STANDS), so this is deliberate.
**Lock id correction (d-adr-lockstep-citation-001):** the input-lockstep lock is **ADR-0002** ("lockstep over FishNet,
input-bus only"); the repo's ADR-0010 is the unrelated test-sandbox. Use ADR-0002 everywhere the lock is named.

## goal (outcome, not method)

Two ENDPOINTS produce the SAME per-tick **MeaningChecksum** (host + 1 in-process follower = a 2nd `VoxelField` re-running
the SAME seeded input stream — NOT the deleted `CoarseChunkFollower`), loopback on ONE machine, over a SEEDED scenario that
EXERCISES the S1 forced-flow events (выброс + ветер/fork + one-way valve + jet) AND CONCURRENT same-face writes.
Determinism **BY CONSTRUCTION** — integer-only authoritative path + build-time zero-float scan + single-owner-per-face +
gather-then-apply + canonical traversal order + integer mass-clamp with **loud asserts** — NOT via re-flux, NOT via 2
physical machines. A divergence HALTS LOUDLY (canon Факт-1 «рассинхрон = громкая остановка»), never drifts silently.

This ELEVATES the existing `F11LoopbackDeterminismTests` (the VoxelField MeaningChecksum two-endpoint re-run harness that
S0 seeded + S1 extended with the bias register) to load-bearing — it does NOT rebuild from scratch; verify it first-hand at
the tip and build only the delta.

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract to its CURRENT version FIRST.**
2. **Canon (mandatory, applied):** §Факт-1 (input-lockstep conditions; desync = громкая остановка; scale bound = weakest
   peer's CPU) + the «Детерминизм—как-гарантируется» §2 paragraph (d-reflux-gate-001) (single-owner-per-face +
   gather-then-apply + canonical order + the integer mass-clamp trap: a silent wrap is bit-identical on all peers ⇒
   checksum GREEN while physics is garbage ⇒ hard-clamp to [0,cap] with a LOUD assert) + §5 S2 + §8 follower-parity warning
   + **§9 шов 5 / §9.5** (the binding meaning-checksum membership — «Чексумм покрывает СМЫСЛ»). **Read «ADR-0010 (lock)»
   everywhere as ADR-0002** (§1 поправка).
3. **Genuine artifact to ELEVATE (verify first-hand):** `tests/GasCoopGame.Core.Tests/Field/Determinism/F11LoopbackDeterminismTests`
   (two INDEPENDENT in-process VoxelField builds of the SAME seeded sequence ⇒ byte-identical per-tick MeaningChecksum, the
   S1 bias register folded in) + the canonical-order machinery (`tests/GasCoopGame.Core.Tests/Field/ForcedFlow/RW5OrderIndependenceTests.cs`
   for concurrent same-face writes — under Field/ForcedFlow/, NOT the Field/Determinism/ folder F11 lives in).
   S2b's job = make this LOAD-BEARING over the FULL forced-flow scenario + add the load-bearing RED controls + the §9.5
   membership proof + the loud halt-on-divergence + the Adapters 3-mode owner-eye. The follower = a 2nd VoxelField, NOT a
   chunk-receiver (the host-broadcast `CoarseChunkFollower.ComputeHash` path is GONE — S2a; do NOT resurrect it).
4. **The legacy is GONE (S2a):** the chunked-delta + field-state-channel families are deleted. Do NOT re-introduce any of
   them, and do NOT anchor the loopback hasher or any collapse target on the 2-band model as an AUTHORITATIVE goal (§7
   burial; 2-band authority belongs to S4). If a port seems to need them back → STOP-escalate.
5. **§9.5 membership state at the tip (c-016 PLAN finding):** 3 named fields (the S1 bias register, `region_id`, face-state)
   are folded in MeaningChecksum TODAY (VoxelField.cs ~236–326); ~20 foldable near-tier fields exist. NOT-YET-BUILT §9.5
   members are scoped OUT with intentional spec-silence: per-type/per-layer coarse mass, promo-events, multi-species TypeId
   value (1 species today), page-id, awake-queue order, loot-dose (D6). The sub-face occupancy BITMAP stays OUT (StructureGrid;
   count-IN/bitmap-OUT). KEEP it OUT: the §9 шов-5 trip-wire (canon §4 шов 5) that would FORCE folding the occupancy bitmap
   into the meaning-checksum fires only at the FIRST effect depending on WHICH sub-faces are open (directional breach /
   asymmetric expansion / one-half valve / direction-mask = S5/S6) — OUT of S2b scope; if tempted to fold it here,
   STOP-escalate (do not migrate the checksum schema in this leg).
6. **AUTO-COVERAGE SEAM (c-016 PLAN gate finding):** the zero-float scan + the int-overflow scan hardcode
   `$DefaultRoots=[Core/Field/Voxel, Core/Field/Structure]`. Any NEW authoritative subtree S2b adds MUST be appended to BOTH
   scan scripts as an EXPLICIT done_when bullet — else the gate is vacuously green (a real hole). c-018 is G0-frozen →
   needs openspec/changes/<id>/ + frozen spec + ledger + spec-silence + coverage + mutation-<id>.json ≥70 (floor tight:
   c-015 = 72.7%); RESULT.md status must read DELIVERED or -Deliver throws.

## ведро classification of this slice (PLAN reconfirms)

S2b is the determinism/replication SUBSTRATE, not a gameplay mechanic.
- **Ведро-2 (coarse-promotable, IN-checksum, shared by all peers):** the WHOLE authoritative meaning-set S2b proves
  byte-identical — the FULL canon §9.5 membership («Чексумм покрывает СМЫСЛ») that EXISTS today (verify against canon; the not-yet-built
  members of #5 are spec-silenced, not vacuously claimed). This is the backbone all later ведро-2 mechanics ride.
- **Ведро-1 (off-checksum local detail bubble):** EXCLUDED; S2b proves the checksum spans exactly the ведро-2 meaning and
  NOT any ведро-1 detail (the projected conductivity COUNT is IN, the per-sub-face occupancy BITMAP is OUT — keep it OUT).
- **Ведро-3 (sub-room AND shared):** ABSENT (arrives with S4).

## boundaries (out of scope / STOP-escalate if tempted)

- **NO real 2 physical machines** — loopback (2 in-process endpoints, ONE machine, NO UDP) IS the gate; integer cross-CPU
  is GIVEN (canon §Детерминизм), guaranteed by the zero-float scan on one machine. Real 2 PCs = OPTIONAL one-off, NEVER a gate.
- **NO network vendor / transport change** (FishNet stays the default; transport is an edge adapter, R14). NO actual
  UDP/transport wiring is required for the gate.
- **NO stored velocity / float on the authoritative path / advection** (RESERVED tier — cracks the lock **ADR-0002**;
  STOP-escalate, d-gas-richness-tiers-001). **NO re-flux-as-gate** (d-reflux-gate-001). **NO RNG RED-control** — there is
  no RNG on the gas authoritative path (deterministic-by-INPUT; d-s2-rng-control-na-001) → DROP it + record the intentional
  spec-silence; the order/wrap/permutation/fold controls cover the determinism-catch role.
- **Chunk-span full excision is S4, NOT here** — `CoarseChunkSpan`/`IsWireEncodable`/`ChunkSpan`/`ChunkCount` are now
  wire-purposeless but retain surviving far-tier consumers (S2a KEEP); leave them, flagged for the S4 cleanup.
- NO reactions/chemistry (S6); NO height/layering (S3); NO coarse-rollup/LOD (S4); NO basic breach / latent-edge flip
  (S5 — canon §5 «Базовый пролом»; the first effect depending on WHICH sub-faces are open ⇒ would force the bitmap IN; keep
  it OUT, STOP-escalate); NO big-hall/sparse-solver (d-sparse-solver-defer-001). NO re-introduction of the S2a-deleted
  reconstruction families.
- Laws live in headless **Core/**; Adapters/** only renders + drives input + hosts the loopback harness composition root
  (R13/R14, 3 modes). Gas-50, R5, R12 unchanged. The lock is ADR-0002.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync FIRST; ingest canon §Факт-1/§Детерминизм/§5 S2/§8/§9.5 + the §1 ADR-0002 correction +
   the S0/S1/S2a artifacts; reconfirm ведро; scope the seeded scenario; confirm no new authoritative subtree escapes the
   scan roots (#6); set owner-expectation (loopback = the gate; real 2 PCs = optional).
2. **2-ENDPOINT LOOPBACK HASH HARNESS (load-bearing):** host + 1 in-process follower (a 2nd VoxelField re-running the same
   input stream) produce BYTE-IDENTICAL per-tick MeaningChecksum over a SEEDED run that EXERCISES the S1 forced-flow events
   (выброс + ветер/fork + one-way valve + jet) AND CONCURRENT same-face writes (canonical order-independent rule). The
   harness ASSERTS byte-identity each tick and HALTS LOUDLY on first divergence (canon Факт-1).
3. **FOLLOWER MEANING-PARITY (canon §8):** the follower's checksum-of-MEANING == the host's each tick (host
   `VoxelField.MeaningChecksum` == follower's), proven by an independent RED test (a narrower-subset follower MUST fail).
4. **DETERMINISM BY CONSTRUCTION + RED controls (independent test-author; each MUST trip the loud halt — asserted-but-
   unfalsifiable is not allowed):** integer-only authoritative path; zero-float scan spans ALL new code (planted-float RED
   control fails); integer mass-clamp loud-asserts on every gather-then-apply (planted silent-wrap RED control fails);
   **(a)** planted order-dependent same-face write diverges; **(b)** planted non-canonical ACTIVE-FRONT / active-set
   ITERATION permutation diverges — the sparse active-set fold is by canonical owning-face INDEX (verify at the tip:
   the VoxelField.MeaningChecksum active-set loop), so that canonical traversal order is the falsifiable target (canon
   §Детерминизм canonical-order); the §9.5 «канонический порядок awake-очереди» member PROPER is spec-silenced per
   context #5 (no sleep/wake structure is built yet — bind a true awake-queue-order control only when one lands);
   **(c)** NO region-fold-order RED control at S2b — record the intentional spec-silence: canon «сортировки чексуммы по
   region_id» sits in the Far room-graph ROLLUP context (collapse/expand = S4), and the live near-tier MeaningChecksum
   folds region_id as a per-cell VALUE (no per-region rollup loop, no region-keyed sort) → there is no region fold-order to
   perturb at S2b; region_id divergence is already covered by (d). If the PLAN's first-hand re-sync finds a built
   region-rollup fold at the tip, re-scope this to a planted swap of the canonical CELL/active-set traversal order that MUST
   diverge — never leave a MUST-trip aimed at an unbuilt S4 seam; **(d)** planted per-meaning-field divergence (the bias
   register, `region_id`, face-state EACH separately) trips the halt (proves each is actually FOLDED — a silently-absent
   field stays green = FAIL). **(NO RNG control — d-s2-rng-control-na-001; record the spec-silence.)**
5. **§9.5 MEMBERSHIP proof:** the byte-identity spans the full §9.5 set that EXISTS today (verify against canon); the
   count-IN/bitmap-OUT boundary holds (a negative-control row: same count, different bitmap, gas-checksum unchanged); the
   not-yet-built §9.5 members (#5) are declared spec-silenced (future), not vacuously claimed; uniform fields
   (resolution/representation/cap/tick_divisor) proven non-silently-absent via single-cell/two-grid mutation.
6. **check.ps1 -Deliver GREEN** (build + headless + zero-float scan + int-overflow scan + mutation ≥70 on new Core +
   spec-silence + deliverable-coverage). If S2b adds a new authoritative subtree, BOTH scan-script roots are extended
   (#6 seam) — verified by a planted-float in the new subtree that the scan CATCHES.
7. **G0-FROZEN:** openspec/changes/<id>/ + frozen spec + ledger + mutation-<id>.json ≥70; RESULT.md status = DELIVERED.
8. **ZERO-LEGACY** (no deleted-family resurrection; tests rewritten not dragged).
9. **OWNER-EYE (confidence, NOT a gate):** Adapters R14 3-mode composition root — owner sees the 2 endpoints agree per-tick
   (a planted divergence stops loudly). Real 2 PCs = optional one-off; owner-run, no self-marking.

## discipline / gates (carried)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN ·
mutation ≥ floor (70%) · a FRESH-SESSION G5 (different model family) refuting the determinism / canonical-order /
hash-parity / mass-clamp-assert / §9.5-membership seams — COULD-NOT-REFUTE is the bar · STOP-discipline (a blocked/
infeasible approach, a crutch, OR any need for stored velocity / float on the authoritative path / re-flux-as-gate /
re-introducing the deleted reconstruction families / reopening the lock **ADR-0002** = mandatory STOP + escalate).

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the loopback harness + its RED-control trips, the §9.5 membership + spec-silence record) + findings for the
planner. dev→main merge + push is OWNER-GATED. next slice after S2 = S3 (height/layering).

## budget

One slice. If the PLAN finds the full forced-flow-inclusive harness + all RED controls + the §9.5 membership proof is too
big for one leg, STOP and return "split needed" (e.g. the 2-endpoint harness + halt + the 4 RED controls land first; the
full §9.5 membership proof + uniform-field mutation second) — do not silently build a blob.

END_OF_FILE: live/indie-game-development/work/c-exec-018-call.md
