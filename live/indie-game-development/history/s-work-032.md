# RESULT — s-work-032 (work, g-9c41 / Sc-weight / c-exec-020)

session: s-work-032
play: work
node: g-9c41
task: Sc-weight (2nd character-road slice; per-type vertical buoyancy)
date: 2026-06-29

## outcome

The Sc-weight executor CALL (c-exec-020) is FRAMED + adversarially HARDENED and build-ready → work/c-exec-020-call.md.
It frames the engine leg: near-tier gas acquires per-type VERTICAL BUOYANCY (a heavy-class type's mass SINKS, a
light-class type's RISES, tunable per meta-type) realized as an integer BIAS on Z-face flow producing a CREEPING front
(canon §3), ENGINE-ONLY. It wires the RESERVED GasParentParams.RatioToAir weight-class slot Sc-types laid. No build this
session (the build is a separate GasCoopGame_dev session, owner present at its PLAN). Sc-weight stays ACTIVE awaiting the
executor return; no TREE / active-bet change (G1 intact: 1 active task).

## evidence

- work/c-exec-020-call.md — the full hardened CALL (goal=outcome; PORT crux; mechanism; the ContentHash-fold gate; the
  per-tick MeaningChecksum trip-wire; the settle-floor-vs-true-term obligation; the no-hardcode-dispatch obligation;
  boundaries; ведро; 10 done_when; discipline/gates; return; budget; approach token = per-type-buoyancy-bias-creeping-front).
- Hardening workflow wf_8f324a28-81e (7 adversarial lenses [canon-fidelity, determinism-checksum, settle-kpeff,
  scan-completeness, boundary-scope, symbol-accuracy, call-hygiene] → per-finding refute-verify → synth): 24 raised → 20
  survived adversarial verify (3 must-fix, 9 should-fix/nit folded) → 4 refuted. ZERO lock-change, ZERO re-design.
- Every load-bearing symbol VERIFIED first-hand at GasCoopGame main @7d08882 (Sc-types merged): CoarseSpecies.cs:46
  EffectiveDensity = max(1, MW − (T>>shift)), Weights={64,32,16,8}, BuoyancyTempShift=2; CoarseBandStep.cs:186-251 Settle =
  the FORBIDDEN densest-first capacity-fill SORT; VoxelFaceFlow.cs:85 kpEff = EffectiveSpreadKp(s)*spfClamped, :119-120 the
  per-face move; GasParentParams.cs:27-31 DensityPacking + RatioToAir reserved inert «Sc-weight»; GasMetaType.cs:20 /
  GasType.cs:30 carry only SpreadKpOverride; GasTypeRegistry.cs:146-160 ComputeContentHash folds parent.RatioToAir + per-index
  (TypeId,MetaTypeId,EffectiveKp) ONLY; MeaningMembers.cs:36 max bit TypeId=1<<5; VoxelFaces.cs:23,40 geometry switch(face).

### the 3 must-fix folded
1. **ContentHash gap (LINCHPIN; 5 lenses converged).** The draft's DERIVED-checksum rationale falsely claimed «RatioToAir is
   already in the registry ContentHash via Sc-types» — but ComputeContentHash folds only the PARENT default, NOT the per-type/
   meta weight OVERRIDE this slice adds. Two peers identical in (TypeId,MetaTypeId,EffectiveKp) but differing in a weight
   override → identical ContentHash → pass the lockstep session-start handshake → desync on buoyancy under a GREEN checksum
   (Факт-1/§9.5 «зелёный чексумм, мусор физика»). FOLD: a dedicated «registry ContentHash fold» section + done_when #6(a):
   the resolved per-index weight MUST fold into ComputeContentHash exactly as effectiveKp[i] does, with a RED control (two
   registries differing only in a weight override DIVERGE the hash).
2. **Band-lexicon leak.** The settle endpoint was phrased «reaches a FIXED POINT (heavy-below-light)» / «once a column is
   sorted» — the buried §7 2-band notion, most directly satisfied by CoarseBandStep.Settle's sort. FOLD: re-phrased to
   «Z-bias-flux QUIESCENCE (no net per-tick Z-flux; heavy-class COM below light-class) — NOT a fully-stratified sorted column»
   (rep-neutral under sparse-dominant Факт-4).
3. **Scan false-positive + array-by-TypeId evasion.** Option (b) «broaden the scan to Core/Field/Voxel» as a blind
   directory-append would RED-fail on the frozen geometry switch(face) (VoxelFaces.cs:23,40) and the [Flags] enum
   MeaningMembers; and a const array indexed by TypeId (the exact CoarseSpecies.Weights[] shape the PORT risks) evades the
   enum/switch token AND option (a)'s «zero control flow» (array indexing isn't control flow). FOLD: option (b) must broaden
   BY SYMBOL (TypeId-keyed dispatch) + whitelist legitimate non-TypeId enums/switches + self-test mustPass; option (a) must
   also forbid an id-keyed array.

### the 9 should-fix/nit folded
- Acknowledge the sibling reserved slot DensityPacking stays inert/untouched (RatioToAir is the named carrier — its own
  member-comment names it the weight class — not handed back to the PLAN as ambiguous).
- Buoyancy MUST NOT bank into the Mass-folded per-face carry (re-fires at zero gradient; strictly worse than S1 — persistent).
- STORED checksum member folds via the BIAS-style SKIP-ZERO precedent, NOT the TypeId !IsDefault rep-conditional (else a
  zero-buoyancy multi-type run breaks byte-identity).
- Replaced the unsourced magic «~2.4x at spf=4» with the conductivity-dependent factor (1× at a full face where spf cancels,
  up to spf× at a 1-sub-face slit); corrected the backwards «raw Kp wrong by spf factor» framing — derive against the TRUE
  per-tick term mag·cond/(Kp·spf).
- The persistent-bias fixed point comes from the per-tick magnitude bound vs kpEff (anti-overshoot), NOT back-pressure alone
  (which only enforces non-negativity).
- The far-tier law is RELATIVE/UNSIGNED → the PLAN must define an ABSOLUTE NEUTRAL weight reference for the signed Z-bias, and
  record it; disambiguate done_when #2's two «weight-neutral» senses (a middle type in a mixed run vs an all-same/default run).
- done_when #7 cross-references #5 (float/overflow coverage of Voxel ≠ the type-hardcode no-dispatch hole) + restored the
  c-exec-019 template's inoculating «$DefaultRoots already identical — forward-discipline» NOTE.
- Corrected the visual RiseSinkBias provenance (already on main, reserved by c-visual-001; c-visual-002 S2 will later drive
  it) — not «c-visual-002 S2 on dev2».

### refuted (NOT folded)
- goal-realization-paraphrase — the goal's «integer bias on flow / creeping front» is the canon-§3 OUTCOME anchor (bias-not-
  sort), NOT a play-procedure paraphrase; the writer's hygiene bounce does not fire; stripping it would remove the guard
  keeping the builder off the forbidden sort. KEPT.
- temperature-reserve-is-correct — confirms reserving the T-coupling term does not gut the visible deliverable (carried by
  the weight-class term; the slice ships at uniform T). No change.
- settle-red-oracle-wellposed — confirms the forever-slosh-but-loopback-green RED oracle is correct; G5 note (a) fully folded.
- settle-spf-cancels-for-full-face — its substance (raw Kp is exact for a full face; over-protection is conductivity-
  dependent) was INCORPORATED via the should-fix rewrite of the settle-floor section (the verifier errored on this one, but
  its claim agreed with the upheld settle-24x finding, so the correction was made anyway).

## state_changes

- CREATE live/indie-game-development/work/c-exec-020-call.md = the hardened Sc-weight CALL (END_OF_FILE trailer present).
- NOW.md open_calls: ADD `c-exec-020` (status: framed) + note.
- NOW.md active_tasks Sc-weight: APPEND the FRAMED+HARDENED record to the status note; status STAYS `active` (awaiting the
  GasCoopGame_dev executor return).
- NOW.md next: UPDATE «IMMEDIATE NEXT» from «FRAME + harden» → «OPEN c-exec-020 (FRAMED+HARDENED)»; ADD the s-work-032 PUSH
  commit line.
- LOG.md: APPEND the s-work-032 line.
- history/s-work-032.md: this RESULT.

## captures

(none — the type-hardcode-scan «strongest guarantee» honest-overclaim is folded into the CALL as a build obligation, not a
separate capture.)

## decisions_needed

(none — framing is complete; the realization decisions [DERIVED vs STORED checksum; absolute-neutral value; scan option a/b;
temperature included/reserved] are the GasCoopGame_dev PLAN's, owner present then.)

## play_check

1. Recite — DONE: restated Sc-weight goal (per-type Z-bias buoyancy, creeping front) + done_when + the bet (g-9c41 character
   road) from NOW.md active_tasks.
2. Owner inputs (owner) — SKIPPED + why: the artifact is an engineering CALL, NOT owner-content (not something the owner
   personally lives by/operates/sends as his own); no owner question needed — the design is the GasCoopGame_dev PLAN where the
   owner is present. (The owner's task input «оформить, НЕ строить» = frame to completion.)
3. Do the work — DONE: drafted the CALL from canon §3/§7/§8 + the c-exec-019 template + the 2 G5 notes + first-hand code, then
   adversarially hardened it via wf_8f324a28-81e (7 lenses → refute-verify → synth); folded 3 must-fix + 9 should-fix/nit.
   call:executor recorded in NOW.md open_calls (c-exec-020).
4. Self-check — DONE: the CALL covers every Sc-weight done_when (per-type Z-bias; RED non-monotone-conservation + no-pop;
   determinism loopback + both scan roots; -Deliver GREEN + mutation ≥70 + fresh-session G5; ZERO-LEGACY; owner-eye; STOP =
   per-column instant sort / float / ADR-0002) + the approach token + both G5 notes as hard obligations + the linchpin
   ContentHash must-fix.
5. Close — DONE: this RESULT; next = open c-exec-020 in a fresh GasCoopGame_dev session.

## log

work (g-9c41 / Sc-weight / c-exec-020): FRAMED + adversarially HARDENED the Sc-weight executor CALL (per-type vertical
buoyancy, integer Z-face bias / creeping front, ENGINE-ONLY) → work/c-exec-020-call.md; wf_8f324a28-81e (24→20 survived, 3
must-fix + 9 should-fix/nit folded, 4 refuted); every cited symbol verified first-hand @7d08882; linchpin must-fix = fold the
new per-type weight override into the registry ContentHash; Sc-weight stays ACTIVE; next = open c-exec-020 in GasCoopGame_dev.

## next

CALL c-exec-020 (executor → GasCoopGame_dev, opens with a PLAN, owner present):
- goal: near-tier gas acquires per-type vertical buoyancy — a heavy-class type's mass sinks, a light-class type's rises,
  tunable per meta-type, as an integer bias on Z-face flow producing a creeping front; the owner sees a heavy test gas pool
  low and a light test gas collect high, creeping. ENGINE-ONLY.
- context / boundaries / done_when / return / budget: work/c-exec-020-call.md (self-contained; §Re-sync GasCoopGame contract
  FIRST; base = main at-or-after @7d08882).
- return: a RESULT routed HOME; dev→main merge + push owner-gated; on GREEN the road rolls to Sc-reactions.

END_OF_FILE: live/indie-game-development/history/s-work-032.md
