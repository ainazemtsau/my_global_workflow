# RESULT — s-work-015 (g-9c41 Wave 2): coarse-Core foundation assessment for the owner vision → do NOTHING to the Core now (keep-open invariant already met); record it (d-corefoundation-001)

direction indie-game-development / bet g-9c41 / Wave 2 / play work (owner architecture question; assessment + forward-constraint recorded; owner present).

## outcome

The owner doubted the coarse sim is too crude / non-extensible for his vision (exact spawn place/size; plausible on-return cloud; no false over-mix in a big room; reactions everywhere). I ran a first-hand Core-foundation assessment (workflow wf_16158bde, 4 agents + red-team).

- **The code map (CORRECT, red-team re-verified) confirms the owner's instinct about the LIMITS:** today the coarse Core keeps gas only per (sector, band, species). NO finer-than-room source POSITION (`Source` struct = {Sector,Band,Species,PerTick}, XY thrown away at `SetSource`); NO intra-room horizontal split (`FromTopology` = 1 sector/room; `RectDecomposition` built+tested but NOT wired; `SubdivisionIntent` carried but ignored); NO advancing front; NO gas-gas reaction (`ReactionLayer` is a toy over the legacy `RoomGraph`). So exact-place / on-return-cloud-place+size / no-false-over-mix / reactions-everywhere-at-fidelity are NOT done by the current Core.
- **BUT the synthesis over-claimed "NEEDS-CORE-CHANGE-NOW"; the RED-TEAM downgraded it to `doNothingNowIsSafe = TRUE` — binding, and consistent with the owner's own signed decisions:**
  - SUPPORTED-NOW: V1 honest-everywhere; V3 no-merge-to-one-number (K species tracked separately); V6 AMOUNT/RATE (always-on coarse + per-room capacity/back-pressure → "left, returned, whole floor filled" is structurally prevented at room granularity).
  - The Wave-3 seams (S4 source-seed / S2 sub-sectors / S3 graph-of-fronts) are the owner's OWN signed deferrals (`d-roomfull-001`(3c): subdivision = "Wave 3+ configurable knob", «2 полосы сейчас сохраняют проверенные числа»; `early_finish`: pull-forward-if-ahead = not now) + the 17-agent `s-research-008` confirms 2-band/1-sector is correct day-one and triages S2/S3/S4 to the Wave-3 shape behind half-day probes NOT yet run.
  - `d-returnfidelity-001`'s forward-constraint is a KEEP-THE-DOOR-OPEN obligation (don't bake in 1-sector/settled-only), tagged "cheap, not code now" — and it is ALREADY MET: the wire/hash key off sector COUNT (not 1/room); the document carries `SubdivisionIntent` + `TopologyAnchor{LocalX,Y,Z}`; `RectDecomposition` is built.
  - Source XY is RECOVERABLE upstream (level generator / the currently-empty `TopologyAnchor`) → the in-Core source-seed is a Wave-3 ADDITION, not an irrecoverable loss → NOT a rewrite. All additions ride ALONGSIDE the LOCKed planes (achievable-on-LOCK = YES; coarse mass stays the single truth, no 2nd fill equation).
  - G1 + "don't break what works": the active bet is t-4 (internal proof) on a gate-green LOCK-frozen baseline — changing the Core for a Wave-3 benefit is out of scope.
- **CONCLUSION:** change NOTHING in the Core for t-4. The structure is a correct day-one foundation that does NOT foreclose the vision; the refinement is a Wave-3 EXTENSION, not a rewrite. HONEST CAVEAT: even with sub-sectors the coarse layer reacts per-(subsector,band) — the literal "must NOT react as if co-located" is delivered only by the FINE per-cell tier (Wave 3).

## evidence

- Workflow wf_16158bde: a first-hand read of CoarseBandStore / CoarseBandStep / CoarseSectorGraph / CoarseField / CoarseSpecies / CoarseGasReadModel / ReactionLayer / Topology, mapped against the owner-signed decisions (d-returnfidelity-001, d-return-reconstruction-001, d-bandhandoff-001, d-roomfull-001, early_finish) + s-research-008.
- Red-team re-verified every code-map claim first-hand and corrected the inference (the seams are owner-deferred + probe-gated; the keep-open invariant already holds; source XY recoverable; G1/baseline guard).

## state_changes

- NOW.md decision_inbox: added **d-corefoundation-001** (answered) — the assessment verdict + the WAVE-2-BINDING KEEP-OPEN INVARIANT (no "1 sector/room" or "settled-only" invariant in any solver/wire/hash; source XY lossy-but-recoverable) as the Wave-3 entry bar.
- LOG.md: appended the s-work-015 line.
- NO Core change; NO change to the bet spine / tasks / gate-green baseline (the verdict is "change nothing now").

## captures

- The keep-open invariant is the genuinely-cheap "make the structure right now" action — it is recorded so the Wave-3 builder cannot bake in a 1-sector/settled-only assumption that would force a rewrite.
- This is also a clean example of the synthesis-over-claims / red-team-corrects pattern (memory: feedback-os-changes-dont-break-what-works) — the owner's own prior deferrals + the prior 17-agent research were the binding authority that downgraded a "change-now" recommendation.

## decisions_needed

- none — the verdict is "do nothing to the Core now"; the keep-open invariant is recorded for the Wave-3 shape.

## play_check

- "1 Recite — done: the owner's doubt that the coarse model is too crude/non-extensible for his vision."
- "2 Owner inputs — architecture question; owner present + explicit ('get the Core structure right so we only extend')."
- "3 Do the work — first-hand Core-foundation assessment (wf_16158bde) + red-team; recorded the keep-open invariant."
- "4 Self-check — red-team re-verified the code map first-hand AND corrected the synthesis's over-claim against the owner's signed deferrals + s-research-008; verdict = do-nothing-now-is-safe."
- "5 Close — RESULT; the Core is untouched; the keep-open invariant is the Wave-3 entry bar."
- "NOTE: read-only assessment + a forward-constraint record; NO Core/baseline change (don't break what works + G1)."

## log

work (g-9c41/Wave2, s-work-015): assessed the coarse Core vs the owner vision (wf_16158bde + red-team). Owner's instinct re the LIMITS is right (no source-XY / no horizontal split / no front / no reactions), but the red-team downgraded "change-now" to do-nothing-now-is-safe: the seams are the owner's own Wave-3 deferrals + s-research-008-confirmed; the keep-open invariant already holds; source XY recoverable upstream → Wave-3 extension not rewrite. Recorded d-corefoundation-001 (keep-open invariant = the Wave-3 entry bar). Core/baseline untouched.

## next

No Core action. t-4 continues as the internal proof (re-issue c-exec-008 to the proof scope per s-work-014). The Wave-3 shape, after the s-research-008 §5 half-day probes, decides S4 source-seed / S2 sub-sectors / S3 graph-of-fronts — all additive on the LOCK, honoring d-corefoundation-001's keep-open invariant. The fine per-cell tier (Wave 3) is what fully delivers exact-place / on-return-cloud / no-false-over-mix / reactions-at-fidelity.

END_OF_FILE: live/indie-game-development/history/s-work-015.md
