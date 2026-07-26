# CALL c-visual-006 — Stage 2: Паспорт типа + шипучий режим — RENDER-ONLY

> 🔥 **FIRE-READY 2026-07-06** (s-work-055; owner: «Stage 1 ок, давай визуал дальше — Stage 2»). Second stage of
> gas-visual-plan-v2. Stage 1 (стенд + отсечка) is DONE + owner-tested (delivered via c-visual-005, merged @26dd062).
> **Base = GasCoopGame main @26dd062** (contract v18; includes Sc-rep/Sc-kernel + **W1b c-exec-025 dominant-STAMP
> read-API** + c-visual-005). **dev_2 RESET FIRST:** reset `GasCoopGame_dev_2` to `origin/main` @26dd062 before any
> work (it currently sits at the c-visual-005 dev2 tip @fbab24f; main @26dd062 already carries that work merged).
>
> ✅ **BOTH GATES MET (why this is openable now):** (1) W1b landed — the per-cell dominant-type read-API is merged in
> main @26dd062 (verified: `c-exec-025-w1b` commits + `c-exec-027` archived it); the render side can finally read
> more than one species. (2) Owner check GIVEN 2026-07-06 («Stage 1 ок, давай Stage 2») — the required fresh
> un-hold, not an auto-cascade.
>
> ✅ **STAGE 2 SIGN-OFF CLARIFIED 2026-07-06** (owner): «шипучий режим» is ONLY the owner-facing label for the
> two-colour real multi-type preview, NOT an extra bubbling/particle/boiling effect. The base gas passport is
> REQUIRED for every gas (hue/value/saturation/edge-softness/motion-frequency/buoyancy-silhouette/interior-structure/
> glow-pattern/danger). The passport must reserve an extensible render-only attachment path for later per-gas
> look modules/assets (custom texture, particle accents, special glow/distortion, etc.), but Stage 2 builds NO
> per-gas special modules yet. Everything else in the proposed Stage 2 plan is accepted.

- direction: indie-game-development
- node: g-7e15 (VISUAL track)
- play: work (executor leg — GasCoopGame render/adapter layer; dev_2 → main when green)
- repo: C:\projects\Unity\GasCoopGame_dev_2  (the BUILD worktree — the REAL gas visual; NEVER dev, engine cubes live there)
- runs_in: a FRESH GasCoopGame_dev_2 session (the BUILD session; NOT this OS-worktree session)
- opens_with: an owner-present PLAN. FIRST: reset dev_2 to origin/main @26dd062 + §Re-sync-confirm the contract (repo
  is on v18). Then the schema session (owner signs the 8-channel schema + the 96→128B layout-ADR) BEFORE any build.
- supersedes: nothing — this is the next leg after c-visual-004/005 (Stage 1) in work/gas-visual-plan-v2-2026-07-02.md

## goal (outcome, not method)
Make the gas able to show MORE THAN ONE species honestly, on the ship-quality render path — so that from here on
every per-type look decision (Stage 3/4) is judged on real half-res with a real multi-type feed, never re-litigated
later. Stage 2 is mostly PLUMBING + one owner-signed schema decision; its single visible payoff is a two-colour
multi-type PREVIEW. It does NOT yet give types their character (that is Stage 4) — it lays the rails for it.

## what Stage 2 builds (faithful to plan v2 §Stage 2)
1. **ПАСПОРТ ТИПА — the schema (owner-signed decision, the spine of this leg).** Define the REQUIRED base gas
   passport for EVERY gas as **8 identity channels** + a danger scalar:
   hue · value · saturation · edge-softness · motion-frequency · **buoyancy-silhouette** · interior-structure ·
   glow-pattern  (+ danger 0→1).
   ⚠ `buoyancy-silhouette` is worded strictly as a **read-through of the existing per-type SIM weight** — it is NEVER
   a new render-side vertical bias; `RiseSinkBias` STAYS reserved per ADR-0020. Do not invent sim behaviour render-side.
   The passport remains EXTENSIBLE: reserve a render-only attachment path so a specific gas type can later opt into
   optional look modules/assets (custom texture, particle accents, special glow/distortion, etc.). Stage 2 only
   reserves this path; it does NOT build any per-gas special module.
2. **96→128-byte LAYOUT-ADR (decide it HERE, before any per-type polish).** Only 5 reserved scalars are genuinely free
   today; ~8–10 new per-type scalars are needed — so the `GpuGasParams` upload layout grows 96→128 B. This is a
   render-adapter change (the GasParams buffer / GasParamsLayout), owner-signed as an ADR, keeping the C#↔HLSL stride
   gate GREEN. Deciding it now avoids re-tuning polish later (the owner has been burned twice by "стало хуже" — this
   is the manufactured-regression guard).
3. **W1b CONSUME — wire the real multi-type feed.** The engine side is DONE (c-exec-025, merged @26dd062). This leg
   CONSUMES it render-side: `RealGasViewSource` stops hardcoding `G=0`/`TypeCount=1` and reads the merged per-cell
   dominant-STAMP read-API, so two real gases can render with distinct profiles. Verify the read-API surface exists on
   the base tip before wiring (it does — c-exec-025). If it turns out insufficient and needs an ENGINE change → STOP
   (that is a new engine mini-CALL in dev, never a silent Core/** edit from dev_2).
4. **REAL HALF-RES + depth-aware bilateral upsample (pulled forward from Stage 6).** The `resolutionScale` knob is a
   declared no-op today; make it real (measured elsewhere: ~7–11 ms full-res vs ~1 ms half-res on a GTX1060 — half-res
   is not optional at ship quality). Add the depth-aware bilateral upsample so half-res does not smear edges. From here
   on, every owner-eye verdict is judged on THIS ship-quality path.
5. **ШИПУЧИЙ РЕЖИМ / the visible payoff = a two-colour multi-type PREVIEW.** Owner sees two real gases, distinct
   colours, meeting — explicitly LABELLED "PREVIEW: colours only; character arrives at Stage 4". Per owner
   clarification, «шипучий режим» is the LABEL for this real multi-type preview; it is NOT an extra bubbling,
   particle, boiling, or other special effect. Same visual quality, confirmed still-good on the real half-res path.

## explicitly OUT of Stage 2 (later stages, not dropped)
- Per-type CHARACTER / the 3 canon archetypes / 3-channel minimum-separation / blind lineup / danger LADDER → Stage 4.
- Natural-jet fix (curl-noise advection, plasticine-capsule kill) / hero one-gas polish / LP1 re-test → Stage 3.
- Per-gas special render-only look modules/assets (custom texture, particle accents, special glow/distortion, etc.) —
  Stage 2 reserves the passport extension path only; actual modules/assets are later, explicit legs.
- Any NEW sim behaviour, any `RiseSinkBias`/reserved-field CONSUMPTION beyond the layout-ADR's declared per-type
  scalars, any Core/** edit → STOP + escalate (engine mini-CALL in dev, never dev_2).

## process discipline (owner-required, unchanged)
- NEVER-WORSE: `GoodSampleAsset` baseline kept; every change shown A/B vs it; worse = discarded, baseline unchanged.
  The half-res path MUST prove still-good vs the full-res baseline before it becomes the new baseline.
- ONE THING AT A TIME: state in plain words what the owner will see and why it's better before each sub-step.
- VERDICTS FROM THE PRIMARY BOOKMARK ONLY (the Stage-1 stand's primary preset); the open-space pad + free orbit are
  exploratory notes, not verdicts.
- UNCERTAINTY COMES HOME: a confusing visual or a schema ambiguity → STOP and bring it home; no blind knob-thrashing.

## reading set (self-contained)
- live/indie-game-development/work/gas-visual-plan-v2-2026-07-02.md §Stage 2 (the authoritative content of this leg)
  + the "what exists / what's absent" inventory (half-res no-op, per-type-data-is-colour-only, reserved-scalar count).
- docs/gas-visual-stage-plan.md §S2/§S6+ in the product repo (the look-lever menu) + ADR-0020 (`RiseSinkBias` reserved)
  + the existing `GpuGasParams`/`GasParamsLayout` + C#↔HLSL stride gate.
- REUSE, do NOT rebuild: `RealGasViewSource`, `VoxelSandboxDirector`, the Stage-1 `GasRoomScene` stand + camera
  bookmarks, `GasUber.shader`, `GoodSampleAsset` (Odin v1 stays — no tooling rebuild this leg).

## boundaries (STOP-and-escalate if hit — never a silent substitute)
- RENDER-ONLY (R13): ZERO `Core/**` edit; sim untouched; its tests stay green & UNCHANGED; UPLOAD-ONLY, no readback.
  The W1b engine side is already merged — this leg only READS it.
- The 96→128B layout-ADR is the ONE structural change; it is render-adapter (GasParams upload), owner-signed, stride
  gate stays green. Anything that would push it into `Core/**` or the sim struct → STOP.
- Runs in GasCoopGame_dev_2 ONLY. Reset dev_2 to origin/main @26dd062 first. dev_2 → main merge owner-gated.
- A blocked/infeasible named approach or a reduced-fidelity crutch = mandatory STOP + escalate (v16: name the tool;
  Unity/MCP unavailable → STOP + ask owner, no workaround).
- v17: NO source-text scan as behaviour evidence; the only legal text check is a declared wiring-smoke
  (File.Exists + trivial substring). Behaviour = a real EditMode/PlayMode or live-MCP run; look = owner-eye.

## done_when
- Opened with the owner-present PLAN; dev_2 reset to @26dd062 + §Re-sync-confirm done first; baseline saved.
- SCHEMA owner-SIGNED: the REQUIRED base gas passport for every gas is defined as hue/value/saturation/edge-softness/
  motion-frequency/buoyancy-silhouette/interior-structure/glow-pattern/danger; the passport reserves a render-only
  extension path for later per-gas look modules/assets but builds none; the 96→128B layout-ADR is written (docs/adr/*)
  and the C#↔HLSL stride gate GREEN with the new layout.
- W1b CONSUMED: `RealGasViewSource` reads the real per-cell dominant type (no longer hardcoded G=0/TypeCount=1);
  demonstrated with a real two-species scenario on the stand.
- REAL HALF-RES: `resolutionScale` is genuinely half-res + bilateral upsample; owner-eye A/B confirms half-res still
  reads as good as full-res (never-worse); no edge smear.
- OWNER SEES the two-colour multi-type PREVIEW (two real gases, distinct colours, meeting) — labelled PREVIEW; judged
  IN MOTION from the primary bookmark; owner-eye sign. No self-marking.
- HEADLESS «точно»: tools/check.ps1 -Deliver GREEN; git diff Core/** EMPTY; sim tests UNCHANGED; stride gate green;
  RESULT-per-leg docs/results/c-visual-006.md (RESULT-per-leg live since c-030); v18 cited artifacts exist; v17
  wiring-smoke existence-only. RED-first only where there is genuine new mechanical surface (layout stride math,
  upsample reconstruction); else say so honestly.
- RESULT comes HOME to OS (state_changes applied by a separate writer). dev_2 → main owner-gated.

## return
A RESULT routed home: outcome + evidence (the signed 8-channel schema + layout-ADR; the two-colour preview owner-eye
sign; the half-res A/B; the updated `GoodSampleAsset` baseline) + the next look slice (Stage 3 = одна жемчужина —
hero-polish one gas, natural-jet fix, LP1 re-test).

## budget & rigor
Secondary visual-track cadence (~1 visual : ~2 engine while Sc-reactions is in flight). Fresh GasCoopGame_dev_2
session. Binding gate = the owner's EYE + the render-only regression invariants + the stride gate (no heavy
multi-agent refutation — render-only). May split at the PLAN if the schema/layout decision and the half-res work turn
out to have different natural checkpoints (the schema is a clean sign-then-build seam).

parent: s-work-055

END_OF_FILE: live/indie-game-development/work/c-visual-006-stage2-call.md
