# CALL c-exec-023 — Sc-kernel: SPARSE TICK KERNEL / ACTIVE-FRONT ITERATION (ENGINE-ONLY)

> Fires ONLY after: (1) ✅ owner SIGNED d-sparse-tick-kernel-001 «да» (2026-07-02); (2) ✅ Sc-rep merged to
> GasCoopGame main (origin/main @5442be0, s-work-037) + fresh G5 COULD-NOT-REFUTE + owner-eye. Base = post-Sc-rep
> `main` @5442be0. Slice position: AFTER Sc-rep, BEFORE Sc-reactions (c-exec-021 stays HELD behind it).
> HARDENED at framing (s-work-038, owner present — «все подтверждаю» 2026-07-02) with the 2026-07-02 sim-plan audit
> §Package item 4 additions (audit-gas-sim-plan-2026-07-02.md; each additive line carries its source finding-id) +
> a standard adversarial pass (wf_ff1612b9-ec5: 11 raised → 2 confirmed folded, 9 refuted). Like c-018/c-021/c-022.

Direction: indie-game-development / g-9c41 / Sc-kernel. Base = post-Sc-rep-merge GasCoopGame `main` @5442be0.
Executor: a FRESH `C:\projects\Unity\GasCoopGame_dev` session. Opens with a PLAN (**owner present — the c-exec-022
PLAN deviation must not repeat**). Canon = knowledge/g9c41-gas-engine-SPEC.md (Факт-4 «главная экономия — sparse-awake
через активный фронт»; §6 п.3 hangar; Факт-1 weakest-peer CPU; ADR-0002 determinism; §4 seams 2/4/5/7).
Evidence base = docs/measurements/sc-rep-hangar-real-measurement-2026-07-02.md (dev @8db3ee1) +
docs/measurements/c-exec-014-benchmark-readout.md (its point 2 already named this «the #1 optimization»).

## why (measured, not argued)

Sc-rep delivered the sparse-dominant STORE but the tick kernel still expands it into dense per-species planes every
tick (`OldMassScratch`/`CopyPlane` over ALL cells per REGISTERED species → dense face-flow over all open faces per
species → `ReplaceFromPlaneMassesValidated` rebuild). Measured cost ∝ roster × domain cells, independent of actual
gas: hangar (196,608 cells, 1,562 active) = 18 ms/tick @roster-1 → 587 ms @roster-64 (~9 ms per registered type);
roster-128 ≈ 1.16 s vs the 50–100 ms tick budget; weak peer 2–4× worse. This breaks the lockstep weakest-peer
premise (Факт-1) before reactions/typing add their own cost.

## goal (outcome, not method)

The authoritative tick computes over the SPARSE store / ACTIVE cells directly: per-tick cost scales with ACTIVE cells
(+ their open faces + bounded co-resident types), NOT with registered roster × domain cells. Behavior byte-identical
to the post-Sc-rep goldens. Determinism preserved (ADR-0002). ENGINE-ONLY.

**approach token = `active-front-tick-kernel-over-sparse-store`** (no per-tick dense plane expansion on the
authoritative path). Keeping the dense expand/rebuild round-trip as the authority = approach substitution →
`owner-ack:<sig|esc-id>` or STOP-escalate. A per-cell Dictionary/hashmap active set, or a stored-velocity field,
is also a substitution.

## done_when (verifiable; PLAN, owner present, decides the exact kernel shape)

1. **PLAN (owner present):** §Re-sync GasCoopGame run-contract at tip FIRST (wire escape-class registry walk into
   deliver/spec-silence; bump validation.config only when the repo gate is synced; STOP if it can't be synced
   safely). Ingest SPEC Факт-4/§6 п.3 + the two measurement docs + the Sc-rep RESULT. DECIDE + RECORD:
   - active-set/front data structure + **canonical iteration order** (deterministic, pinned; an awake-set-order RED
     control MUST trip);
   - how dormant saturated gas byte-sleeps (Факт-4) and exactly which events re-awaken a cell — the **WAKE-TRIGGER
     REGISTRY seam** [audit 4c / global-scale-4, types-mixing-3]: ACTIVE triggers day-one = boundary flux,
     conductivity/occupancy change (breach), impulse-event footprint; RESERVED stubs (named, not built) = env-vector
     delta, reaction front, temperature delta; honesty note recorded: lazy catch-up ≠ equivalent to a wake source.
     This is the single most rework-preventing line — it protects BOTH the active-front economy AND the future
     env-derived typing («зеркало среды»), which mutates otherwise-sleeping cells. **Each ACTIVE trigger carries an
     independent RED (leg1) [hardening s-work-038 P2]:** a cell that settles and byte-sleeps, then receives that
     trigger (boundary mass flux / face conductivity-occupancy change/breach / impulse footprint), MUST re-wake —
     byte-identical to the retained dense oracle (done_when 9) over the settle→sleep→re-wake round-trip; a planted
     «slept cell ignores incoming flux/breach/impulse» MUST trip. Without it a cell can byte-sleep and never re-wake,
     silently dropping a region that should be live (R2 «симуляция везде» violation) while every other gate passes.
     RESERVED rows stay seam-only (no wake-behavior test);
   - scratch strategy (NO roster-sized dense planes on the hot path);
   - **checksum-scaling decision** [audit 4a / global-scale-3]: the scaling gates time the FULL authoritative path
     (Step + MeaningChecksum) OR add a named checksum-scaling gate. If the checksum must become an active-set fold to
     hold the «cost ∝ active cells» contract, take that as a SCHEMA decision NOW — canonical X,Y,Z sorted-active fold
     that preserves the existing hash meaning (no live-node migration; loopback-only until ~S4);
   - ADR = next free **ADR-E-*** per ADR-P-0001 (verify at tip — OS docs do not pre-assign).
2. **Scaling gates (the point of the slice; same harness as 2026-07-02):**
   (a) **roster-independence** — hangar ms/tick at roster 1 vs 64 differs by ≤ ~10–20% (was 32.5×); **PLUS a
       roster-128 row** [audit 4d / types-mixing-6] so the advertised config ceiling stops being an extrapolation;
   (b) **active-scaling** — hangar with 1,562 active cells costs a small fraction of the 2026-07-02 dense-kernel
       number (target class: single-digit ms on the owner machine; PLAN sets the recorded threshold);
   (c) **adversarial «hangar flooded»** — ALL ~196k cells active: measured and recorded vs the 50–100 ms budget with
       the weak-peer ×2–4 caveat. **measure-and-BIND** [audit 4b / global-scale-2]: if the weak-peer projection is
       over budget, the RESULT AUTO-OPENS owner decision **d-hangar-flood-fallback-001** (levers, all owner-signed to
       activate: segment-authored halls FIRST per «второстепенное»; sub-partition; mid-2.5D far-only; GAP-4
       tick_divisor; all-peers-all-bubbles; volume cap; multicore). No silent pass;
   (d) **checksum timed** per the 1-PLAN decision (full-path timing OR the named checksum-scaling gate) — the
       «active cells» contract is not allowed to exclude an O(domain-cells) checksum silently.
3. **Measurement matrix before/after** (TYPICAL + HANGAR × roster 1/4/16/64/128, 40 timed + 5 warmup) — recorded in
   docs/measurements/ side-by-side; PLUS:
   - **MINE/SHAFT probe row** [audit 4f / verticality-far-reentry]: a tall stacked shaft + side rooms, light gas
     released at the bottom; record ms/tick + active-set trajectory during the rise — the TIER-0 vertical archetype's
     FIRST number (flat-hangar keying is no longer the only evidence);
   - **all-cores measure-only naive-split row** [audit 4e / global-scale-5]: the REAL multicore divisor on record
     before anything cites ×4–8 (measure-only; no multicore build this slice);
   - **bytes/cell + store memory row** [audit 4h];
   - **Unity-runtime capture** (owner-run Editor/PlayMode — the 2026-07-02 numbers were CoreCLR console; the owner-run
     absolute is the honest number; an owner-run step is NOT done until the owner confirms).
4. **No-regression:** single-type AND multi-type runs byte-identical to the post-Sc-rep committed goldens; loopback
   two-endpoint MeaningChecksum green over a multi-type sparse run; NO golden rebaselining (if byte-identity can't
   hold with a sparse kernel — ordering! — STOP and surface, do not rebaseline silently).
5. **Determinism (ADR-0002):** integer-only; new code under BOTH zero-float + int-overflow scan roots (kept paired);
   planted float / order-dependence / awake-set-order RED controls trip. **Close the Coarse/ scan-root hole here**
   (add Coarse/ to both root lists + a planted-violation self-test) — folded from the 2026-06-29 plan-audit so it
   stops floating.
6. **GC-zero steady-state** holds on the new hot path (no per-tick roster-sized allocations; a planted per-tick
   `new int[cells]` MUST trip).
7. **Near-vertical multi-room fixture** [audit 4g / verticality-near-multiroom-unproven]: a **TwoStackedRooms**
   Z-adjacent fixture + independent REDs — light gas rises through the Z-band portal, heavy gas does not — closes the
   untested near-vertical multi-room seam (the existing helper is X-only). ENGINE-ONLY behavior test, not a level.
8. **check.ps1 -Deliver GREEN** (full battery: build + headless + zero-float + int-overflow + type-hardcode where
   relevant + mutation ≥70 on new Core + spec-silence + deliverable-coverage + v-current escape-class walk + RESULT.md)
   + independent-author REDs (builder cannot edit them) + **fresh-session G5** + owner-eye (owner sees the same scenes
   behave identically + the before/after table + the flooded number).
9. **ZERO-LEGACY:** the per-tick dense expand/rebuild path removed at completion (git is rollback); dense remains ONLY
   where it is a one-time migration/test-oracle input, never per-tick authority.
10. **Field-level storage guard (folds the Sc-rep G5 P2 finding):** the existing hashmap-substitution guards inspect
    the cell RECORD (SparseDominantCellRecord) but not the FIELD authority storage — a private
    `Dictionary<int, SparseDominantCellRecord>` authority inside SparseDominantNearGasField could pass today (G5
    evidence: SparseDominantLayoutAcceptanceTests.cs:43, SparseDominantGuardrails.cs:15,
    ScRepRegressionDeterminismAndSeamAcceptanceTests.cs:79 reject only int[,]/int[][]). Add a structural assertion
    that the field's authority store is contiguous arrays; a planted Dictionary-backed realization MUST trip it.

## framing meta (recorded in the CALL + NOW)

- **JEWEL GUARD** [audit 4j / words-vs-docs-002]: Sc-kernel is the LAST pre-reactions engine-only insertion. No sixth
  engine-only slice may precede Sc-reactions absent an explicit owner re-affirmation quoting R1. (R1 = «очень
  правдоподобный, геймплейно-интересный газ у игрока» is now five owner-signed engine-only slices deep.)
- **2026-07-24 visible-gas milestone re-affirmed HERE** [audit 4k / words-vs-docs-006], not moved via «tail movable»:
  the VISUAL branch is FROZEN by the owner hold («сначала симуляция»; NOW: VISUAL ON HOLD), so W1b / «two-type visual
  on the REAL sim» is NOT a live milestone carrier until visual un-holds. With visual on hold the SOLE live
  player-facing terminus is the Sc-reactions telegraph+bang owner-eye — the lens-sweep justification of engine-only
  slices (a parallel visual «keeping proof flowing») no longer holds as written and is NOT cited as a counterweight.
  Sc-kernel itself is engine-only (no player-visible proof). The owner consciously accepts the cost of «сначала
  симуляция» until Sc-reactions (R7 unchanged; visual stays held).
- **weak-peer CPU proxy class** [audit 4i]: the flooded projection and every future weak-peer budget cite a NAMED
  proxy class with a documented ×2–4 rule (recorded once, reused), not an ad-hoc multiplier.

## boundaries / STOP

- NO reactions / typing / waves / damage / temperature. NO S4 rollup build (seam preserved). NO visual hookup, NO
  dev2 edits (may verify read-paths only; if avoiding breakage needs a dev2 edit — STOP). NO K/overflow policy change
  (that is the c-exec-021 shape's named fork, banner items 13/15).
- NO float, no unseeded RNG, no wall-clock on the authoritative path; ADR-0002 not reopened; NO stored-velocity field
  (that is TIER-3, its own signed reopen of the no-stored-velocity representation boundary — NOT this slice).
- If byte-identity vs the post-Sc-rep goldens cannot hold with a sparse kernel (ordering!), STOP and surface — do NOT
  rebaseline silently.
- Split-trip BY MACHINERY if oversized: **leg1** = the active-front kernel + roster-independence (2a) + no-regression
  (4) + determinism (5) + the field-storage guard (10) + GC-zero (6) + the wake round-trip RED (done_when 1) — this is
  the KILL-test leg (see kill_by);
  **leg2** = the flooded-hangar adversarial capture (2c) + checksum-scaling (2d) + Coarse/ scan-root closure (5) +
  the mine/shaft + TwoStackedRooms + all-cores + memory rows (3, 7) + Unity-runtime capture. The wake-trigger seam
  and its RED (1) and the JEWEL GUARD stay in leg1 (they are design decisions, not deferrable measurements).

## kill_by (owner-set at framing — «все подтверждаю» 2026-07-02)

Appetite = one slice (split-trip by machinery allowed; leg1 carries the kill-test). **Kill condition = the
active-front approach is refuted, not extended:** if gate 2(a) roster-independence CANNOT reach ≤ ~20% roster-1-vs-64
delta on the hangar, OR gate 4 byte-identity cannot hold with a sparse kernel, the slice is KILLED and re-shaped — no
silent rebaseline, no appetite extension. Date = **2026-07-16** (leg1 checkpoint; owner-set). A flooded number over
the weak-peer budget is NOT a kill — it AUTO-OPENS d-hangar-flood-fallback-001 (the slice still succeeds; the fallback
is a separate owner decision).

## return

RESULT routed HOME: commits/PR, -Deliver transcript, mutation json, before/after measurement table (+ flooded hangar +
mine/shaft + TwoStackedRooms + all-cores divisor + bytes/cell + Unity capture), independent RED list, fresh G5 verdict,
owner-eye note, chosen ADR-E number, wake-trigger registry as recorded + the wake round-trip RED result,
checksum-scaling decision as taken, and — IF the flooded projection is over budget — d-hangar-flood-fallback-001 opened
for owner sign-off. The RESULT also FILLS the SPEC §6 п.2 LEVEL-DESIGN CONTRACT ceiling number (measured fully-fine
ceiling). dev→main merge + push owner-gated. On GREEN the road rolls to Sc-reactions (re-harden c-exec-021 per its
banner items 11–17; the richness-ladder re-trigger axes ride Sc-reactions' bang-read + Sc-damage's open-space jet).

END_OF_FILE: live/indie-game-development/work/c-exec-023-call.md
