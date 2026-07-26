# RESULT s-work-055 — frame c-visual-006 (g-7e15 Stage 2: Паспорт типа + шипучий режим)

session: s-work-055
direction: indie-game-development
node: g-7e15 (VISUAL track)
play: shape (frame an executor CALL)
for: c-visual-006 (Stage 2 of gas-visual-plan-v2)

## outcome
Owner asked — pointedly — for the VISUAL next CALL (not the engine one; c-021 he already launched himself). Framed
**c-visual-006** = Stage 2 of the visual plan, RENDER-ONLY, fire-ready in a fresh GasCoopGame_dev_2 session.
CALL = work/c-visual-006-stage2-call.md.

## what it builds (faithful to plan v2 §Stage 2)
- (a) ПАСПОРТ ТИПА — owner-signed per-type visual profile as 8 identity channels (hue · value · saturation ·
  edge-softness · motion-frequency · buoyancy-silhouette · interior-structure · glow-pattern) + a danger scalar.
  buoyancy-silhouette is a READ-THROUGH of the existing per-type SIM weight, NEVER a new render vertical bias
  (RiseSinkBias stays reserved, ADR-0020).
- (b) The 96→128-byte LAYOUT-ADR decided HERE (only 5 reserved scalars free; ~8–10 needed) — render-adapter
  (GpuGasParams/GasParamsLayout), owner-signed, C#↔HLSL stride gate stays green. Decided before any per-type polish
  (the manufactured-regression guard for an owner burned twice by «стало хуже»).
- (c) W1b CONSUME — engine side is DONE (c-exec-025, verified merged in product main @26dd062); this leg wires
  RealGasViewSource to read the real per-cell dominant-STAMP (stops hardcoding G=0/TypeCount=1).
- (d) REAL half-res + depth-aware bilateral upsample pulled forward (resolutionScale is a no-op today) so all later
  owner-eye verdicts are on the ship-quality path.
- Visible payoff = a two-colour multi-type PREVIEW (two real gases, distinct colours, meeting), labelled PREVIEW
  («colours only; character arrives at Stage 4»).

## pre-frame verification (did NOT hand a blocked CALL)
Checked the product repo first-hand before framing: W1b (c-exec-025) IS merged in GasCoopGame main @26dd062
(`c-exec-025-w1b` review commits + `c-exec-027` archived it) — the dominant-STAMP read-API exists, so Stage 2 is
genuinely unblocked. dev_2 HEAD is @fbab24f (c-visual-005 dev2 tip); main @26dd062 carries that merged → the CALL's
step 0 resets dev_2 to origin/main @26dd062.

## scope discipline folded in
- RENDER-ONLY (R13): zero Core/** edit; the W1b engine side is already merged, this leg only READS it; if the
  read-API turns out insufficient → STOP (new engine mini-CALL in dev, never a silent dev_2 Core edit).
- OUT: per-type character / 3 archetypes / 3-channel separation / blind lineup / danger ladder = Stage 4;
  natural-jet fix / hero polish / LP1 re-test = Stage 3.
- Contract v18 honored: RESULT-per-leg (docs/results/c-visual-006.md), v17 wiring-smoke existence-only (no source
  scan as behaviour evidence), v16 tool-unavailable-STOP, v18 cited-artifact existence.
- «шипучий режим» in the title is carried as the owner-facing name of the effervescent multi-type preview; if it
  means a specific extra look, it is confirmed at the owner-present PLAN, not invented in the CALL.

## state_changes
- NOW.md: opened c-visual-006 as an active open_call (after the c-visual-005 closed comment); next-section VISUAL
  line → Stage 2 FRAMED + FIRE-READY as c-visual-006; g-7e15 track_state → Stage 2 FRAMED (was "to be framed").
  updated → s-work-055.
- work/c-visual-006-stage2-call.md: the CALL (new).

## play_check
- shape: DONE — framed Stage 2 from plan v2 §Stage 2 (authoritative), verified the W1b dependency exists first-hand,
  folded the render-only + contract-v18 + cross-track (dev_2-not-dev) discipline. NO product change, NO TREE/CHARTER
  change; the g-7e15 track continues.
- next: FIRE c-visual-006 in a FRESH GasCoopGame_dev_2 session (reset dev_2 to @26dd062 first), owner-present PLAN.

## log
g-7e15 shape/frame — c-visual-006 (Stage 2: Паспорт типа + шипучий режим) FRAMED + FIRE-READY. Render-only: owner-signed
8-channel per-type schema + 96→128B layout-ADR + consume the merged W1b read-API (c-exec-025 verified in main @26dd062)
+ real half-res + a two-colour multi-type PREVIEW. dev_2 reset to @26dd062 first; NEVER dev; per-type character = Stage 4
(OUT); zero Core edit. Fires in a fresh GasCoopGame_dev_2 session, owner-present PLAN, PARALLEL to c-021 (engine).

## next
FIRE c-visual-006 in a FRESH GasCoopGame_dev_2 session: work/c-visual-006-stage2-call.md. Reset dev_2 to origin/main
@26dd062 first; opens with an owner-present PLAN (sign the schema before build). dev_2→main merge + push OWNER-GATED.
On GREEN + owner-eye → Stage 3 (Одна жемчужина). Engine track continues in parallel at c-exec-021 (Sc-reactions).

END_OF_FILE: live/indie-game-development/history/2026-07-06-s-work-055-frame-c-visual-006-stage2.md
