# CALL c-exec-016 — S2: МУЛЬТИПЛЕЕР (LOCKSTEP) — детерминизм ПО ПОСТРОЕНИЮ на 2 процессах (loopback)

Direction: indie-game-development / g-9c41 / S2. Frames the S2 slice (canon §5 S2). Rolls on S0 (c-exec-014, GasCoopGame
`main` @824948d) + S1 forced-flow (c-exec-015 / scope S1a, `main` @0adae83, 970 green). Executor: a FRESH GasCoopGame_dev
session (Unity-MCP + branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner present).
State source = NOW.md (active_tasks S2). Canon = knowledge/g9c41-gas-engine-SPEC.md (§Факт-1, §Детерминизм line 57, §5 S2, §8,
AND §9 шов 5 / line 106 — the authoritative meaning-checksum membership baseline that the ведро-2 set the PLAN proves
byte-identical IS, extended by the S1 directional-bias register; verify against §9.5, do NOT re-paraphrase).

## Why this slice NOW (fork resolved — lockstep STANDS)

The architecture fork (input-lockstep vs host-authority/float-clouds) was RESOLVED 2026-06-28 (`d-clouds-fork-resolved-001`,
owner «точно у игрока, грубо везде»): input-lockstep STANDS, ADR-0010 is NOT un-locked, the host-state-sync float-clouds
matrix is archived as NON-adopted history. So S2 deliberately HARDENS the lockstep apparatus — there is no risk of building
on a spine about to be discarded. S2 is the determinism core the cheap detail/event model + S4 no-pop all ride on (canon §5
hidden-deps: «S2-детерминизм должен стоять рано — вся дешёвая модель на нём»).

## goal (outcome, not method)

The coarse integer sim produces the SAME per-tick **MeaningChecksum** on **2 PROCESSES** (host + 1 follower, loopback,
ONE machine), over a SEEDED scenario that EXERCISES the S1 forced-flow events (decaying directional-bias / impulse:
выброс + ветер/fork-split + one-way valve + jet-emitter) AND CONCURRENT same-face writes. Determinism **BY CONSTRUCTION** —
integer-only authoritative path + build-time zero-float scan + single-owner-per-face + gather-then-apply + canonical
traversal order + seeded RNG + integer mass-clamp with **loud asserts** — NOT via re-flux, NOT via 2 physical machines.
A divergence HALTS LOUDLY (canon Факт-1 «рассинхрон = громкая остановка»), never drifts silently.

This is the REAL HOME of the loopback hash that S0 seeded (an optional ordering/RNG tripwire) and S1 extended (bias folded
into the checksum + concurrent same-face writes). S2 ELEVATES it to the load-bearing lockstep slice and reconciles the
migration spine — it does NOT rebuild from scratch (verify what already exists first; build only the delta).

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract to its CURRENT version FIRST** (do not assume the S1-era version — re-read).
2. **Canon SPEC (mandatory, applied):** §Факт-1 (input-lockstep determinism conditions: integer/fixed arith + seeded RNG +
   fixed traversal order + per-tick meaning-checksum; desync = громкая остановка; scale bound = weakest peer's CPU, NOT the
   channel; host-migration near-free) + the §Детерминизм paragraph (line 57): single-owner-per-face + gather-then-apply +
   canonical order + seeded RNG + the **integer mass-clamp trap** — a silent wrap/overflow is bit-identical on all peers ⇒
   checksum stays GREEN while the physics is garbage ⇒ every gather-then-apply MUST hard-clamp to [0,cap] with a LOUD
   assert, never a silent wrap. Plus §5 S2 + the §8 build warnings + **§9 шов 5 / line 106** (the binding enumeration of
   what the meaning-checksum covers — the ведро-2 set below MUST match it, verify against canon, do not re-paraphrase).
3. **EXISTING loopback machinery you HARDEN, not reinvent (verify first-hand at the current tip):** the 2-process loopback
   bit-identity hash already built across the S0 foundation + the S1 step-0 spike (the S1 bias register folded into
   MeaningChecksum; concurrent same-face writes under a canonical order-independent rule — see `RW5OrderIndependenceTests`).
   S2's job = make this LOAD-BEARING over a full forced-flow scenario + close the migration spine + add the load-bearing RED
   controls — NOT a from-scratch build.
   - **The GENUINE artifact to elevate** = the VoxelField MeaningChecksum re-run determinism harness
     (`tests/GasCoopGame.Core.Tests/Field/Determinism/F11LoopbackDeterminismTests` — two INDEPENDENT in-process VoxelField
     builds of the SAME seeded sequence ⇒ byte-identical per-tick MeaningChecksum, the S1 bias register folded in) — verify
     it BY NAME at the current tip. The harness SHAPE for the load-bearing 2-process follower run is the PLAN's call.
   - **Two DECOYS the PLAN must NOT "harden" as the gas apparatus:** (a) the `Core/Sim` skeleton
     (`SimCore`/`SimState`/`SimInstance`/`ITickInputBus`) — an 8×8 int-grid risk-spike toy tied to ADR-0002, explicitly NOT
     the locked ADR-0010 gas path; (b) `CoarseChunkFollower.ComputeHash` — the §7-buried host-authoritative reconstruction
     path (it APPLIES a chunk stream, NEVER re-runs the sim; flagged legacy in context #4 / done_when 3 / done_when 6).
   - **Locate the prior artifacts** via the c-exec-015 RESULT (home `history/s-work-023.md`; source `GasCoopGame/RESULT.md`)
     + merged commits @824948d (S0) / @0adae83 (S1a); the S1 spike record `docs/c-exec-015-spike-findings.md` is supporting
     context only. These are HISTORY, not authority — verify the hasher against the live tip per §Re-sync, build only the delta.
4. **Migration-spine tension (canon §8 line 184 + §7 «ПОХОРОНЕНО» line 162):** the WHOLE host-authoritative reconstruction
   spine is the OLD model's machinery; under input-lockstep (ADR-0010) ONLY inputs cross the wire and each peer recomputes
   the whole sim. At the current tip it is TWO pre-lockstep families: **(i) the coarse chunked-delta family** —
   `CoarseChunkFollower` / `ChunkEncoder` / `ChunkDecoder` / `RevisionBarrier` / `LoopbackCoarseChunkHub` / `ICoarseChunkLink`;
   **(ii) the field-state-channel family it parallels** — `IFieldStateChannel` / `InMemoryFieldStateChannel` /
   `FishNetFieldStateChannel` / `FieldStateBroadcasts` / `FieldStreamDriver` / `FieldSnapshot` / `FieldState` / `FieldDelta`
   (the asymmetric host-PUBLISHES / followers-CONSUME path; `FieldDelta` belongs to THIS family, not the chunked-delta one).
   This enumeration is **NON-exhaustive** — the PLAN INVENTORIES the full host-authoritative-reconstruction surface at the
   current tip FIRST (verify first-hand, do not trust this list), then decides port-vs-delete per symbol. It INCLUDES the
   **late-join / full-snapshot path** (`IFieldStateChannel.PublishSnapshot` / `RequestSnapshot` / `FieldSnapshot`): under
   canon **Факт-5** (line 51 — «НЕТ позднего входа → нет обязательства полного снапшота; база↔рейд = чистая граница сессии»)
   it is DELETED unless a part demonstrably survives the lockstep model — never kept «for reconnect» (resurrecting late-join
   reopens a buried Факт-5 → STOP-escalate). The PLAN decides port-vs-delete under ZERO-LEGACY; if a port turns out to need a
   lock-crack, STOP-escalate (do not silently reopen ADR-0010).
   **WARNING (canon §8 line 177/187 + §7 line 161):** the reconstruction machinery rides the CURRENT coarse sim, which §8
   establishes IS the 2-band model (`CoarseSectorGraph` BandCount=2, `CoarseBandStep`). Porting it MUST NOT re-anchor the
   loopback hasher or any replication/collapse target on 2-band as an AUTHORITATIVE goal — per §7 the authoritative role of
   the 2-band CODE belongs to S4 room-rollup (NOT S0/S2); treating 2-band as authority here RESURRECTS a §7-buried concept
   while the checksum stays green («так полосы и воскресают», §8:187). The follower hasher (done_when 3) reflects ведро-2
   MEANING only, never 2-band as a collapse authority. If the port cannot proceed without re-asserting 2-band authority,
   STOP-escalate.
5. **§8 follower-parity warning (→ done_when 3):** the near-checksum MEANING must be reflected on the follower's hash
   (`CoarseChunkFollower.ComputeHash` parity, or its ZERO-LEGACY replacement) or host≠follower — verify on build.

## ведро classification of this slice (PLAN reconfirms)

S2 is not a gameplay mechanic — it is the determinism/replication SUBSTRATE. Classification of WHAT it touches:
- **Ведро-2 (coarse-promotable, IN-checksum, shared by all peers):** the WHOLE authoritative meaning-set S2 replicates
  bit-identically — the FULL canon §9.5 (line 106) checksum membership (verify against canon, do NOT narrow): coarse mass
  by type/layer, `region_id`, face-state, the S1 directional-bias register, promo-events, `TypeId`, live cell-size/tier,
  page-id, the projected structure→gas conductivity COUNT, the awake-queue canonical order, and loot dose (D6). S2's
  deliverable IS proving this FULL §9.5 set is byte-identical on 2 processes — the byte-identity check must span the whole
  set, not a subset (a green checksum over a partial set still diverges — Факт-1). This is the backbone all later ведро-2
  mechanics ride.
- **Ведро-1 (off-checksum local detail bubble):** EXPLICITLY EXCLUDED from the checksum. S2 must prove the checksum spans
  exactly the ведро-2 meaning and NOT any ведро-1 detail (none is built yet — the boundary is asserted, not exercised).
  The one §9.5 membership boundary LIVE today: the projected conductivity COUNT is IN-checksum, the per-sub-face occupancy
  BITMAP is OUT (present-but-stubbed, §9.9). S2 must keep the count IN and the bitmap OUT — it must NOT fold the bitmap in;
  the §9.5 trip-wire that would require folding it fires only at the first effect depending on WHICH sub-faces are open
  (directional breach / asymmetric valve / direction-mask = S5/S6, OUT of S2 scope; if tempted, STOP-escalate).
- **Ведро-3 (sub-room AND shared, expensive):** NOT in this slice (arrives with S4 + a deliberate per-room «эта комната
  считает деталь для всех пиров»).

## boundaries (out of scope / STOP-escalate if tempted)

- **NO real 2 physical machines** — loopback (2 processes, ONE machine) IS the gate; integer cross-CPU is GIVEN (banks-style,
  canon §Детерминизм), guaranteed BY CONSTRUCTION by the zero-float scan on one machine. Real 2 PCs = an OPTIONAL one-off
  owner run, NEVER a gate.
- **NO network vendor / transport change** — FishNet stays the default; transport is an edge adapter under R14. S2 proves
  determinism of the CORE, NOT a wire; **NO actual UDP/transport wiring is required for the gate** (loopback is in-process).
- **NO stored velocity / float on the authoritative path / advection** (RESERVED tier — cracks the lock; STOP-escalate,
  `d-gas-richness-tiers-001`). **NO re-flux-as-gate** (determinism is by construction, `d-reflux-gate-001`).
- NO reactions/chemistry (S6); NO height/layering (S3); NO coarse-rollup/LOD (S4); NO big-hall / sparse-solver optimization
  (deferred-UNVALIDATED, `d-sparse-solver-defer-001`).
- Laws live in headless **Core/**; Adapters/** only renders + drives input + hosts the loopback harness composition root
  (R13/R14, 3 modes). Gas-50 law, R5, R12 (one player hosts, no dedicated server, ever) unchanged.

## carried hardening (already shipped — keep green)

- **H1** class-wide int*int overflow build-scan guard (shipped in S1, `d-overflow-guard-001`): the new replication /
  canonical-order math adds integer multiplies; the existing scan auto-covers — keep it GREEN + the planted RED control failing.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync contract → current FIRST; ingest canon §Факт-1 / §Детерминизм / §5 S2 / §8 + the
   S0/S1 artifacts; reconfirm the ведро classification; decide port-vs-delete of the host-broadcast machinery under
   ZERO-LEGACY; scope the seeded scenario; set owner-expectation (loopback = the gate; real 2 PCs = optional one-off).
2. **2-PROCESS LOOPBACK HASH HARNESS (load-bearing):** host + 1 in-process follower produce BYTE-IDENTICAL per-tick
   MeaningChecksum over a SEEDED run that EXERCISES the S1 forced-flow events (выброс + ветер/fork + one-way valve + jet)
   AND CONCURRENT same-face writes (canonical order-independent rule). The harness ASSERTS byte-identity each tick and
   HALTS LOUDLY on first divergence (canon Факт-1). Independent-author RED controls that MUST trip the halt: (a) a planted
   order-dependent same-face write; (b) a planted unseeded/mis-seeded RNG; (c) a planted silent mass-wrap.
3. **FOLLOWER MEANING-PARITY (canon §8):** the follower's checksum-of-MEANING mirrors the host
   (`CoarseChunkFollower.ComputeHash` parity, or its ZERO-LEGACY replacement) — near-checksum meaning reflected on the
   follower — proven by an independent RED test (host meaning ≠ follower meaning must fail).
4. **DETERMINISM BY CONSTRUCTION:** integer-only authoritative path; the S1 bias register + `region_id` + face-state all
   in MeaningChecksum; zero-float scan spans ALL new code (planted-float RED control fails); integer mass-clamp asserts on
   every gather-then-apply (no silent wrap — loud assert; planted-wrap RED control fails); single-owner-per-face + canonical
   traversal order + seeded RNG enforced. Three seams EACH carry an independent-author RED control that MUST trip the loud
   halt (asserted-but-unfalsifiable is NOT allowed): **(e)** a planted non-canonical awake-queue / active-front permutation
   (two peers iterate active faces/cells in different order) MUST diverge the per-tick MeaningChecksum (canon §Детерминизм
   line 57 «закреплённый порядок обхода»; §9.5 line 106 «канонический порядок awake-очереди») — a SEPARATE seam from
   done_when 2's same-face write-order control (a); **(f)** a planted region-fold-order perturbation — regions folded into
   the per-tick checksum out of canonical `region_id` order (reverse / hash-of-reference) — MUST trip the halt (canon §3
   line 78 «сортировки чексуммы по region_id»), so two peers with byte-identical per-region content but different fold order
   cannot pass; **(g)** a planted host/follower divergence in EACH meaning-field — the S1 bias register, `region_id`, and
   face-state EACH separately — MUST trip the halt, proving each is actually FOLDED into the hash (a field silently absent
   stays byte-identical/green = FAIL — the §9.5 / Факт-1 «чексумм ЗЕЛЁНЫЙ, физика мусор» class).
5. **check.ps1 -Deliver GREEN** (build + headless + zero-float scan + int*int scan + mutation ≥70 on new Core + spec-silence
   + deliverable-coverage).
6. **ZERO-LEGACY (inventory-first):** the host-authoritative reconstruction spine (canon §8 line 184; §7 line 162 buries
   the whole host-broadcast / «клиенты реконструируют» / chunked-delta concept under ADR-0010) must be PORTED-or-DELETED on
   finish, never left half-migrated. The PLAN INVENTORIES the full surface at the current tip FIRST (the TWO families named
   in context #4 are a non-exhaustive starting point — verify first-hand), then decides port-vs-delete per symbol. This
   INCLUDES the Факт-5-buried late-join / full-snapshot path (`PublishSnapshot`/`RequestSnapshot`/`FieldSnapshot`): DELETED
   unless a part demonstrably survives the lockstep model — never kept «for reconnect» (→ STOP-escalate, it reopens Факт-5).
   No unused reconstruction machinery may remain (rollback via git history only); tests rewritten, not dragged. A port that
   needs a lock-crack = STOP-escalate.
7. **OWNER-EYE (confidence, NOT a gate):** owner sees the 2 processes agree (the harness reports per-tick identity; a
   planted divergence stops loudly). Real 2 PCs = optional one-off; owner-run, no self-marking.

## discipline / gates (carried from S0/S1)

RED-first by an INDEPENDENT test-author (builder cannot edit the red tests) · Core/** placement · -Deliver GREEN ·
mutation ≥ floor (70%) · a FRESH-SESSION G5 (different model family) that tries to REFUTE the determinism / canonical-order /
hash-parity / mass-clamp-assert seams + the migration-spine ZERO-LEGACY honesty — COULD-NOT-REFUTE is the bar ·
STOP-discipline (a blocked/infeasible named approach, a crutch, OR any need for stored velocity / float on the authoritative
path / re-flux-as-gate / reopening ADR-0010 = mandatory STOP + escalate) · build in small steps.

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, -Deliver transcript, mutation json, G5
verdict, the loopback hash harness + its RED-control trips, the port-vs-delete ZERO-LEGACY disposition) + findings/decisions
for the planner. dev→main merge + push is OWNER-GATED. next slice after S2 = S3 (height/layering).

## budget

One slice. If the PLAN finds the migration-spine port (host-broadcast → input-lockstep loopback) + the full
forced-flow-inclusive harness is too big for one leg, STOP and return "split needed" (e.g. the determinism-core port +
basic loopback hash land first; the full forced-flow scenario + the 3 concurrent-write/RNG/wrap RED controls second) —
do not silently build a blob.

END_OF_FILE: live/indie-game-development/work/c-exec-016-call.md
