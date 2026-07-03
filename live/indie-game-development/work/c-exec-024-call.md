# CALL c-exec-024 — Sc-kernel P2/P3 cleanup (binding-G5 follow-up; ENGINE byte-identical + DOCS)

> Opens after: BINDING fresh-session G5 of c-exec-023 (s-work-039, 2026-07-03) = runtime SOUND (0 P1), with
> 2 P2 completeness/reproducibility gaps + 5 P3 honesty/precision nits on the already-merged Sc-kernel.
> Base = GasCoopGame main @b7d4226 (Sc-kernel merged, pushed). Fires in a FRESH GasCoopGame_dev session in the
> Sc-kernel→Sc-reactions GAP, BEFORE c-exec-021 (Sc-reactions) — so the storage guard and the SPEC/measurement
> wording are correct before Sc-reactions builds on the field. A fix is a CHANGE through the gated contour: the
> slice is on main, no silent edits.

Direction: indie-game-development / g-9c41 / Sc-kernel (cleanup). Owner-approved 2026-07-03 («да по всем»).

## goal (outcome, not method)

The Sc-kernel measurement numbers are reproducible/falsifiable from a clean clone, the field-storage guard's
guarantee matches its stated purpose, and every c-exec-023 artifact's wording matches what the code actually does.

## done_when

1. **P2 #1 — measurement reproducibility.** EITHER (preferred) commit the scaling benchmark as a real compiled
   test under `tests/` so `dotnet test --filter FullyQualifiedName~ScKernelScalingBenchmark` runs and regenerates
   `docs/measurements/c-exec-023-kernel-scaling-matrix.json` (numbers reproducible/falsifiable), OR — if it must
   stay measure-only — correct the false "committed/reproducible/sanctioned reproduce path" prose in the generator
   header, the JSON, and `ScKernelScalingMatrixSchemaTests.cs:6-7` to state plainly the numbers are captured-once,
   not committed-reproducible, and log the gap as a known limitation. Prefer (i): the flooded 70.788 ms number
   feeds owner decision d-hangar-flood-fallback-001 AND the SPEC §6 п.2 ceiling — it should be reproducible.
2. **P2 #2 — field-storage guard completeness.** EITHER make `SparseDominantGuardrails.cs`
   `AssertContiguousArrayAuthority` recurse into nested reference-type fields (and flatten base-class private
   fields) with NEW nested-object AND base-class-private negative controls (RED-first, independent-author), OR
   explicitly narrow the guard's stated purpose AND `spec.md:120-124` to "top-level authority containers only" so
   the claim matches the mechanism. Additive only — the existing passing direct-field controls MUST NOT weaken.
3. **P3 sweep (docs-only, no measurement re-fire):**
   (a) SPEC SHALL `spec.md:108-110` + JSON note + RESULT wording → "the scaling gates time Step (the production
       authoritative path); the O(domain) MeaningChecksum is measured and disclosed as a SEPARATE fixed floor"
       (the "FULL path (Step + MeaningChecksum)" wording is false; Step-only is the correct production ceiling);
   (b) `store_memory` note (json:238) → reattribute the resident bytes to the roster-independent sparse per-face
       pair arrays; drop the false "still-ctor-allocated dense scratch int[species][cell]" clause;
   (c) buoyancy wording (ADR-E-0002 / claim) → reword from "wake-registry entry" to "internal _buoyStamp wake
       reason", OR add buoyancy as a named registry row;
   (d) `CoarseGuardTests.cs:1352-1353` → correct/delete the false "NO InternalsVisibleTo" comment.
4. **Process (future legs, not a repair here):** land RED tests and build-to-green in SEPARATE commits so
   RED→GREEN is git-verifiable; commit negative-control probes rather than leaving them as in-session claims.
5. **Gates:** `check.ps1 -Deliver` GREEN (unchanged battery); ENGINE byte-identity MUST hold (this is docs +
   test-only + a bounded guard-widening — NO behavior change); independent-author REDs for any new guard control;
   fresh-session G5 + owner-eye ONLY if the guard is actually widened (docs-only P3s need no G5).

## boundaries / STOP

NO kernel behavior change (byte-identity must hold). NO reactions/typing/waves/damage. NO golden rebaseline. If
widening the guard forces a real authority-storage change — STOP and surface (it must not; the field is already
contiguous-array). This is a cleanup slice, not a kill-test.

## return

RESULT routed HOME: commits, `-Deliver` transcript, the committed benchmark (or the corrected honesty wording),
the widened guard + its new negative controls (or the narrowed spec wording), the P3 doc diffs. dev→main merge +
push OWNER-GATED. On GREEN → the Sc-kernel ledger is FULLY closed; the gap's other item is W1b
(d-w1b-window-001), then §Re-sync + full re-hardening + fire c-exec-021 (Sc-reactions).

## budget

One small slice (docs + a test + a bounded guard edit). Not a kill-test.

END_OF_FILE: live/indie-game-development/work/c-exec-024-call.md
