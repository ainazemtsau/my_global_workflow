# Character road — shape (2026-06-29, s-work-030)

Owner approved «можем оформлять» (d-character-road-001). This shapes the CHARACTER ROAD — the ordered near-term slice
spine that builds the visible "jewel" (gas with character), chosen OVER the far-tier S3/S4 plumbing (deferred to "when
levels get big"). Rolling-wave: only the FIRST slice is detailed here; the rest are named + dependency-tagged and shaped
when their turn comes. Basis: the plan audit (work/gas-engine-plan-audit-2026-06-29.md) + the decided seams in
d-character-road-001 (R15 layered params, day-one TypeId socket, moddability seam, dense-vs-sparse, port-old-far-tier-math).

## The ordered road (near-term spine, replaces the "S6+ ellipsis" + reprioritizes ahead of far-tier)

1. **Sc-types — META-TYPE / TYPE PARAM STRUCTURE (ACTIVE, first).** The substrate everything else keys off.
2. **Sc-weight — WEIGHT / BUOYANCY.** Per-type vertical drift (heavy sinks / light rises, tunable). Keys off Sc-types.
3. **Sc-rep — SPARSE-DOMINANT RE-REPRESENTATION (owner-lock 2026-06-30, s-reshape-sparse-dominant-001).** Re-represent the
   near gas field dense `[species][cell]` → sparse-dominant (dominant + amount + bounded inline overlay) + per-cell dominant
   STAMP socket (enables env-derived dynamic typing/waves) + preserve the collapse/expand seam + the FIRST hangar measurement.
   ENGINE-ONLY; no typing mechanism (socket only). Keys off Sc-types/Sc-weight. (full shaped card → §SLICE Sc-rep below.)
4. **Sc-reactions — REACTIONS.** Integer chemistry: ≥2 types react → telegraph + bang = coarse event; the cell's overlay IS the
   blended cell. Keys off Sc-rep (sparse-dominant) + ≥2 types. (CALL c-exec-021 HELD + re-scoped onto sparse-dominant.)
5. **Sc-damage — DAMAGE / TEMPERATURE.** Dose-from-coarse (gas hurts; type-specific); temperature as a sink-layer.
   Keys off Sc-types + Sc-weight; the first real gameplay payoff. The co-op-interdependence affordance
   (d-coop-interdependence-repin-001) is folded into this + Sc-reactions PLANs (where a shared gas consequence the 2nd
   player feels lives).

DEFERRED (not deleted) — the far-tier S3 (height-routing layers) / S4 (coarse rollup + no-pop) / S5 (breach): scale-plumbing
for big/~150-room levels, NOT urgent at the current small scale. Re-prioritize when levels grow. (S5 breach carries the
sub-face-bitmap checksum trip-wire when it lands — canon §4 шов 5.)

## SLICE 1 detailed — Sc-types (META-TYPE / TYPE PARAM STRUCTURE)

GOAL (outcome): the engine carries MORE THAN ONE gas type, and types behave DIFFERENTLY, driven by a 3-LAYER DATA-DRIVEN
param structure — so the owner SEES two test gases behave visibly differently (in the engine's debug view), and the
foundation for weight/reactions/damage is laid. ENGINE-ONLY (no visual-track hookup this slice).

What it builds:
- **3-layer param structure (R15):** shared PARENT params common to ALL gases (density / packing, ratio-to-air = weight
  class, spread speed, …) defined ONCE → per-META-TYPE group params → per-type/per-instance tuning (env intensity/danger at
  spawn). A type = pure DATA/config; NOTHING about a type hardcoded in C#.
- **The engine actually carries ≥2 meta-types** (flip speciesCount>1; the [species][cell] shape is already there) that
  differ via the params that EXIST today — primarily SPREAD SPEED (per-type Kp) + density/packing — so the difference is
  real + visible (one gas billows fast, one creeps slow). (WEIGHT difference = Sc-weight; REACTIONS = Sc-reactions —
  out of this slice; do NOT build them here.)
- **TEST types, not lore:** ship 2-3 PLACEHOLDER meta-types chosen to SPAN the behaviour range (e.g. a light-fast vs a
  heavy-slow), explicitly marked TEST/placeholder. Purpose = exercise different behaviour; real lore types replace the
  config later with ZERO structure change.
- **Day-one DETERMINISM socket:** per-cell dominant-TypeId folded into the MeaningChecksum (canon §9.5 wanted it day-one;
  was skipped) — so reaching more types later is NOT a painful networked-schema migration. Safe to add now (loopback only;
  network ~S4).
- **MODDABILITY seam (reserve, don't build the mechanism):** the type set = an ORDERED, CONTENT-HASHED, session-FIXED
  REGISTRY; its content-hash reserved as a hook for the future lockstep session-start handshake (Факт-5 no-late-join makes
  this natural). Ship a fixed built-in TEST set; later DLC/mod types = more registry entries. DEFER actual external
  mod-loading (asset bundles / mod API / workshop).

Boundaries / STOP:
- NO visual-track hookup (engine-only; the look connects in a later step; visual track continues on dev2 independently).
- NO weight/buoyancy, NO reactions, NO damage, NO temperature (those are Sc-weight/Sc-reactions/Sc-damage).
- NO lore-canon types (test placeholders only). NO real mod-loader (seam only).
- NO hardcoded-in-C# type enum/switch (would weld moddability shut). Lock = ADR-0002; determinism preserved.

done_when (verifiable, set at framing):
- PLAN (owner present): §Re-sync; ingest d-character-road-001 + R15 + canon §3/§4/§9.5/Факт-4; DECIDE the representation
  (dense [species][cell] vs Факт-4 sparse-dominant — dense ok at few test types, but record the decision); classify ведро.
  ⚠ UPDATED 2026-06-30: this representation fork is now RESOLVED = sparse-dominant (owner lock, SPEC Факт-4 / A1,
  s-reshape-sparse-dominant-001); Sc-types shipped DENSE and the new **Sc-rep** slice (§below) re-represents it. This line
  stands as HISTORY, not a live open fork.
- Engine carries ≥2 test meta-types behaving differently (per-type spread/density) — RED tests proving they DIVERGE in
  behaviour AND that a single-type run reproduces today's S0/S1 goldens byte-identical.
- The 3-layer param table is data-driven (a type = a data asset/registry entry; an independent RED test proves NO type is
  hardcoded — adding a test type touches only data).
- Per-cell dominant-TypeId in the MeaningChecksum (RED: two peers with different type assignment diverge); the registry
  content-hash exists + is reserved for the handshake (RED: a different registry → different hash).
- check.ps1 -Deliver GREEN + mutation ≥70 on new Core + spec-silence + deliverable-coverage; loopback determinism hash
  green (the new per-type code inside BOTH zero-float/int-overflow scan roots — close the scan-root parity gap here);
  ZERO-LEGACY; fresh-session G5; owner-eye (sees 2 test gases behave differently in the debug view — confidence, not a gate).
- ведро: substrate → ведро-2 (the type set + per-cell TypeId are in-checksum, shared); no ведро-1/3.

ведро / cut list (G6):
- CUT this slice: visual hookup; weight/reactions/damage/temperature; lore types; the real mod-loader; far-tier.
- The riskiest assumption tested first: that ≥2 types behave differently AND stay deterministic in loopback (the per-type
  param path must not introduce float / order-dependence).

## SLICE Sc-rep detailed — SPARSE-DOMINANT RE-REPRESENTATION (shaped 2026-06-30, s-reshape-sparse-dominant-001)

Owner-approved «беру рекомендации» (appetite «да» = one slice). Inserted AFTER Sc-weight, BEFORE Sc-reactions, per the
2026-06-30 owner design lock (work/gas-reaction-typing-design-2026-06-30.md) + SPEC Факт-4. Drafts adversarially vetted
(workflow wf_967a4625-2a4: 29 findings → 24 survived → folded; 5 refuted). This is the authoritative shape-basis the framing
CALL c-exec-022 ingests.

GOAL (outcome): the near gas field stores gas SPARSE-DOMINANT (per active cell: dominant type + amount + small bounded inline
mix-overlay), every active cell carries a per-cell dominant-type STAMP, roster size = config, a single-type run reproduces the
post-Sc-weight golden BYTE-IDENTICAL, determinism preserved (ADR-0002), the big-space collapse/expand seam preserved (S4 plugs
in later without core edits), and the architecture's one unmeasured number — the hangar — is measured first-hand. ENGINE-ONLY.
The STAMP is the SOCKET env-derived dynamic typing + condition-waves + reactions key off later; this slice lays the socket, NOT
the typing/reaction MECHANISM.

What it builds:
- **Sparse-dominant cell layout:** dense `int[species][cell]` → per active cell `{dominant TypeId + amount + K bounded inline
  mix-overlay slots}`, a FIXED-SIZE INLINE value (NOT a per-cell hashmap/Dictionary, NOT per-cell heap on the hot path).
- **Per-cell dominant STAMP** (mutable per-cell field absent in dense) folded into MeaningChecksum CELL-KEYED (canonical X,Y,Z).
- **Roster size = config** (owner-set default; ~128 a suggested start; not welded).
- **Collapse/expand seam preserved** so S4 (big halls) plugs in without core edits — reserved, not built.
- **FIRST hangar measurement** (the SPEC §6 п.3 one unmeasured number, re-homed here).

done_when (verifiable; folds the vetting must/should-fixes):
- **PLAN (owner present):** §Re-sync FIRST; ingest SPEC Факт-4 sparse-dominant lock + §5 dynamic-typing requirement + §4 шов
  2/4/5/7 + §9.5 (stamp+overlay) + §6 п.3 hangar. DECIDE+RECORD: (i) cell layout (inline dominant+amount+K bounded overlay; K +
  overflow policy — overflow = LOUD THROW [mass-conserving] by default; «drop-smallest» legal ONLY as an EXPLICIT DATA-declared
  sink with a canonical tiebreak the conservation RED distinguishes from a leak; a bare silent drop is forbidden; a declared
  SINK is a reactions-DESIGN choice, NOT this slice); (ii) per-cell dominant-stamp checksum fold (CELL-KEYED — never a
  bag/sum/sort-by-value; the PLAN records whether the stamp gets its own MeaningMembers bit or rides the rebuilt sparse layout
  fold, but the 3 RED controls bind either way); (iii) roster-size config mechanism; (iv) the no-regression mapping — VERIFY
  FIRST-HAND at the tip WHICH committed golden carries the post-Sc-weight gas path (it already contains Sc-weight Z-face
  buoyancy creep); pinning a pre-Sc-weight golden = STOP; (v) the new ADR number = ADR-0021 (supersedes the ADR-0018 dense
  `[species][cell]` decision — history says D1; verify the sub-number at the tip) + sibling check `git ls-tree -r --name-only
  dev2 -- docs/adr` + main; (vi) the hangar harness + the documented weak-profile-proxy METHOD.
- **Sparse-dominant layout** shipped + cache-shape gated (NOT just an adjective): structural assertion the per-cell store is a
  contiguous fixed-size value array (no per-cell ref/dict) + a GC-ZERO check over a STEADY-STATE active scene (stepping N ticks
  allocates zero per-cell heap on the hot path; a planted `new`/Dictionary realization MUST trip it). [The hangar absolute
  budget stays the deferred reactions-shape fork; this binds the STRUCTURAL claim hardware-independently.]
- **Per-cell dominant STAMP present + folded CELL-KEYED, with THREE RED controls:** (i) ISOLATION — masking the stamp's
  checksum member (`All & ~<member>`) fails parity when stamps are non-trivial (proves it is folded, not a dead field);
  (ii) DISTINCTNESS (single-endpoint) — two fields IDENTICAL in per-type masses but the stamp on DIFFERENT cells / a different
  TypeId per cell MUST DIVERGE the single-endpoint checksum (the non-relational falsifier the loopback A==B hash cannot give);
  (iii) cross-peer DIVERGENCE — two peers with a different dominant assignment diverge.
- **Conversion CONSERVES cell-total mass EXACTLY:** for every cell, Σ(dense species masses) == dominant amount + Σ(overlay
  amounts) [+ a DATA-declared sink amount, if any], INCLUDING cells with >K co-resident species. Independent-author RED: a >K
  multi-type cell whose dominant is NOT the highest TypeId MUST be stamped with the MAX-MASS species (tie → lowest TypeId,
  resolved identically at both loopback endpoints); a naive «drop-smallest» discarding remainder MUST FAIL the conservation RED;
  on overflow the conversion THROWS loudly (field byte-unchanged), never a silent drop/wrap.
- **No-regression BYTE-IDENTICAL:** a single-type run reproduces the post-Sc-weight committed gas golden byte-identical (golden
  verified first-hand per PLAN (iv)).
- **Determinism preserved (ADR-0002):** integer-only; the new code covered by BOTH zero-float + int-overflow scans — if it lands
  under an already-scanned root, VERIFY both cover the new files; ONLY IF it introduces a NEW authoritative directory, add it to
  BOTH root lists (kept identical) + a planted-violation RED self-test there. Loopback two-endpoint MeaningChecksum green over a
  multi-type sparse run; planted float / order-dependence RED controls.
- **Collapse/expand seam preserved:** per-region structure intact; collapse body-identity still passes; an explicit check that
  the S4 seam (`representation_tag {fine-3D|coarse|bucket}` + collapse/expand) is NOT welded shut by the new layout.
- **FIRST hangar measurement (MEASURE-ONLY, honest partial):** record active_cells/cores (×4-8) on the owner machine + a
  DOCUMENTED weak-profile-proxy method, explicitly noting this is a strong-machine + proxy reading, NOT the SPEC §6 п.3
  weakest-peer absolute ceiling (that stays the deferred target-hardware fork). Not a pass/fail gate.
- **check.ps1 -Deliver GREEN** (build + headless + zero-float + int-overflow + type-hardcode + mutation ≥70 on new Core +
  spec-silence + deliverable-coverage). **ZERO-LEGACY:** the dense `[species][cell]` near path REMOVED at completion (git is
  rollback) — DELETE only AFTER a §Re-sync read-path check confirms NO live near-read consumer depends on the dense layout
  (specifically the dev2 visual track's near read-model, RealGasViewSource / VoxelField render-only, g-7e15); if one does, adapt
  it in the same slice or STOP-escalate. **fresh-session G5** (could-not-refute). **owner-eye** (sees the same scenes behave
  identically post-re-representation + the hangar number — confidence, not a gate).
- **ведро:** substrate → ведро-2 (per-cell stamp + sparse layout are in-checksum, shared); no ведро-1/3.

appetite / split-trip (G6): ONE executor slice. Split-trip BY MACHINERY if it overflows — leg1 = the full sparse-dominant CELL
LAYOUT (dominant + amount + bounded overlay) INCLUDING the per-cell dominant STAMP folded CELL-KEYED into MeaningChecksum
(DISTINCTNESS RED) + byte-identical no-regression + determinism + the FIRST hangar measure; leg2 (only if leg1 overflows) = the
bounded overlay's K/overflow-policy + the collapse/expand seam-preservation check. The dominant-STAMP field + its checksum fold
are INTRINSIC to the representation = leg1; deferring them silently breaks determinism for a whole leg = forbidden. The typing
MECHANISM (accumulator/flip) is CUT entirely this slice.

cut list (G6, ≥1 real cut):
- CUT the env-derived dynamic-typing MECHANISM (exposure accumulator/flip) — only the STAMP socket lands (the real cut: tempting
  to build typing now since the stamp enables it).
- CUT reactions / condition-waves / damage / temperature / temperature-keyed typing rows.
- CUT S4 big-space rollup BUILD (collapse/expand seam preserved only).
- CUT visual-track hookup (engine-only; do NOT touch the dev2 visual track).
- CUT setting the hangar BUDGET/threshold + the target weak-hardware (measure-only; deferred to the reactions shape).
- CUT the real mod-loader (roster = a fixed built-in registry, config SIZE only).
- CUT splitting that defers the dominant-stamp checksum fold out of leg1 (it is intrinsic to the representation).

lens sweep (G6 — verdict per CHARTER lens):
1. Commercial/traction: **not_needed** (engine-only; no new player-facing artifact — owner-eye sees the SAME scenes). Honest
   justification: this is the engine track's 4th consecutive engine-only slice (Sc-types, Sc-weight, Sc-rep, then Sc-reactions)
   — the CHARTER's guarded risk_posture + pre-mortem #2 (private-engineering-tunnel) is acknowledged; the parallel g-7e15 visual
   track is the project-level player-facing surface keeping proof flowing (render-only, does not yet consume the new rep); the
   chain commits to a dated surface — the NEXT slice (re-scoped c-021 reactions) terminates in the owner-eye visible
   telegraph+bang, and the sparse-dominant rep is what g-7e15 consumes toward the 2026-07-24 visible-gas target. Cheapest moment
   to do the re-representation = now, before reactions/typing pile onto dense.
2. Core gameplay depth: **not_needed** as a task (depth lands at reactions/damage) — this slice is the enabling substrate.
3. Co-op-first: **not_needed** (no shared-consequence mechanic yet; lives at reactions/damage, d-coop-interdependence-repin-001).
4. Technical feasibility: **TASK** (the core lens) — determinism preserved + no-regression byte-identical + cache-shape gate +
   the hangar measurement.
5. Scope/production: **TASK/constraint** — bounded overlay (no unbounded per-cell structures), the cut list, the split-trip;
   solo-shippable.
6. Audience workflow: **not_needed** (engine-only, no external artifact).

riskiest assumption → task (ordered FIRST): the two SILENT-CORRUPTION gates are co-first — (a) the dense→sparse re-representation
stays BYTE-IDENTICAL on a single-type run against the SHIPPED Sc-weight-inclusive golden, and (b) the new MUTABLE per-cell
dominant STAMP folds into MeaningChecksum cell-keyed + collision-free (§9.5/шов-5; Факт-1 «чексумм ЗЕЛЁНЫЙ, физика мусор»). Task
ordered first = the no-regression byte-identical RED + the stamp-DISTINCTNESS RED. The FIRST hangar number is the first
MEASUREMENT (not the first risk) — measure-only, with a known on-file lock-safe fallback.

kill_by: 2026-07-05 de-risk-wall checkpoint. next_if_true → the road rolls to Sc-reactions (the re-scoped c-exec-021).
next_if_false (the hangar blows the plausible ceiling even on the owner's strong machine, OR no-regression/determinism cannot be
preserved): STOP + re-shape to a lock-safe fallback — at Sc-rep time the ACTIONABLE fallback is smaller fully-fine levels (reduce
the active-cell ceiling); «all-peers-all-bubbles» (§6 п.3) presumes the detail-bubble mechanism not yet built, so it is a
future-fallback, not an immediate remedy. Do NOT silently coarsen gas cells (cracks ADR-0002).

## NEXT (updated 2026-06-30)
Frame **Sc-rep** as the executor CALL **c-exec-022** (PLAN-first, owner present; builder does NOT author it; verify c-exec-022 is
free at framing, bump+record if taken) → adversarial-hardening workflow (like c-018/c-021's 12-lens pass) → owner opens it in a
fresh GasCoopGame_dev session. Then the road rolls to Sc-reactions (the re-scoped c-exec-021).

— HISTORY (Sc-types framing, done): Frame Sc-types as the executor CALL c-exec-019 (PLAN-first, owner present) → adversarially
harden (like c-016/c-018) → owner opens it in a fresh GasCoopGame_dev session. Then the road rolls to Sc-weight.

END_OF_FILE: live/indie-game-development/work/character-road-shape-2026-06-29.md
