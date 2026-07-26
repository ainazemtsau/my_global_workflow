# s-visual-007 — adversarially validate the gas-visual plan (don't adopt on trust) + revise c-visual-002

date: 2026-06-29
play: research/validate → fold the surviving findings into the c-visual-002 CALL (owner-approved)
node: g-7e15 (VISUAL track — G1 intact, g-9c41 untouched)
owner-present: yes (challenged the adopted plan + the "small" framing; «ок» + asked for an unclipped test scene)

## Trigger

Owner (frustrated, losing trust): «что значит шаг 0+1 маленький? там по визуалу достаточно много. ты просто взял их
план? ты не убедился что он актуальный, как его улучшить?» — a correct call-out: I had ADOPTED the dev plan
(docs/gas-visual-stage-plan.md §S6+) and re-dressed it without independently verifying it is current/correct or trying
to improve it, and I mislabeled the work as "small".

## What I did

Ran an adversarial validation workflow (wf_de8a9945) against the REAL dev2 code instead of trusting the plan:
ground-truth-premises + skeptical-critique + a refute referee (the strategic-search agent failed on schema — re-run if
deeper "biggest jewel lever" analysis is wanted; its partial lead was "light-through-the-volume, not more form/noise").

## Findings (verdict = KEEP the spine; fix 2 holes; flag perf)

- **Plan is CURRENT** — it matches the committed dev2 tip dc4c225 (plan file committed in the same commit).
- **Root cause of «блекло» VERIFIED in code** = (a) coarse sim grid (OpenArena 5x16x5 / rooms 3x3x4, cellSize 1.0)
  trilinearly upsampled + (b) the HARD axis-aligned BOX-AABB clip (GasVisualRenderFeature `_GasVolMin/Max` from
  `WorldBounds`; GasUber.shader discards rays outside the box). NOT a weak shader — GasUber already implements FBM +
  inverted-Worley + self-shadow + gradient-normal key light + fresnel + toon-band + per-type colour ramp + curl motion
  (~40 knobs). "~3/10 levers" = genuine NOT-YET-BUILT headroom (baked noise, smootherstep, detail-volume, scatter-glow,
  analytical transmittance — all grep-confirmed absent), not a primitive shader.
- **Two real holes (survived refutation) → owner-approved changes folded into the CALL:**
  1. The lab as written ("free puff in a void") would polish a FROZEN sphere (FakeGasViewSource authors only static
     spheres; the shader curl is cosmetic billow). OUR gas's identity is motion-borne (spawn/jet/creep) → the lab must
     show the gas IN CHARACTERISTIC MOTION.
  2. Per-type CHARACTER (the owner's headline) is deferred to the finale AND is globally-impossible today: every
     shape/motion/light lever is a GLOBAL uniform; only colour is per-type; the "4 concepts" are mutually-exclusive
     whole-screen presets (can't show toxic next to ethereal). BUT it's a BOUNDED fix, not a rewrite — the GasParams
     buffer is already per-type-indexed and the 96B layout has reserved fields (RiseSinkBias/Temperature/State/…). →
     front-load an EARLY two-type-character probe (two different-character gases in one volume via a reserved field).
- **Owner additions:** a SEPARATE convenient UNCLIPPED test scene (no rectangular cut — owner-requested); revisit the
  SKIPPED "unique" levers (light-through-volume / emissive cores / flow-anisotropy along velocity) now that TOON is
  revoked; and perf is UNVERIFIED (resolutionScale is identity; weak-HW cost unmeasured) — don't treat "optimize later"
  as settled.
- **Rejected as overstated by the referee:** "per-type character is architecturally impossible / must re-spine"; "the
  wrong '9-cell' number invalidates the diagnosis"; "the shader is weak". The spine does NOT need a re-architecture.

## RESULT

```
RESULT
session: s-visual-007
direction: indie-game-development
play: research/validate + fold into the CALL
node: g-7e15 (VISUAL parallel track — G1 intact, g-9c41 untouched)

outcome: |
  Validated the borrowed gas-visual plan against the REAL dev2 code (not adopted on trust). Verdict: the plan's SPINE is
  SOUND (KEEP, no re-spine) and current; the «блекло» root cause is the coarse grid + the hard box-AABB rectangle clip,
  NOT a weak shader. Two real holes survived refutation and became owner-approved revisions to c-visual-002: (1) the lab
  must show the gas IN MOTION (spawn/jet/creep), not a frozen puff; (2) per-type CHARACTER (the owner's headline) is
  front-loaded as an early two-type probe (cheap via reserved GasParams fields) instead of deferred to the finale. Plus
  an owner-requested SEPARATE UNCLIPPED test scene (no rectangle), a "reconsider the skipped unique levers" flag (toon
  revoked), and a perf-UNVERIFIED flag. The "small step" framing was corrected (real work; may split at PLAN).

evidence: |
  Workflow wf_de8a9945 (ground-truth-vs-code + skeptical critique + refute referee; strategic-search agent failed on
  schema). Code-grounded: GasUber.shader (~40 knobs), GasVisualRenderFeature box-AABB clip (lines 317-319 + shader
  227/288-297), FakeGasViewSource static spheres, GasParams per-type buffer + reserved 96B fields. Plan==committed code
  at dc4c225. c-visual-002 CALL rewritten (work/c-visual-002-call.md).

state_changes: |
  NOW.md: open_calls c-visual-002 status comment + note REVISED to the validated scope (unclipped lab + in-motion +
  early two-type probe + differentiating levers + perf-unverified; "small" corrected). g-7e15.next: validation note +
  the 3 changes. LOG append. history/s-visual-007.md. work/c-visual-002-call.md rewritten (product, not state).
  NO TREE/CHARTER change (G9 not triggered); G1 intact.

captures:
  - "Per-type CHARACTER is globally-impossible today (all shape/motion levers are GLOBAL uniforms; concept presets are
    mutually-exclusive) — but a BOUNDED fix via reserved GasParams fields; this is the owner's headline, schedule it EARLY."
  - "The 'jewel' levers (light-through-volume/multiple-scatter glow-through, emissive cores, flow-anisotropy along a jet)
    were SKIPPED as photoreal-overkill under a now-REVOKED toon assumption — reconsider; the failed strategic-search agent
    is worth re-running for 'the single biggest jewel lever'."
  - "Perf is UNVERIFIED for the visual: resolutionScale is identity, weak-HW cost unmeasured — name a min-spec GPU + measure
    once the lab exists; do not treat 'optimize later' as proven."
  - "Process lesson: do NOT adopt a borrowed plan as 'source of truth' without an adversarial validation vs the real code —
    even an internally-honest plan can carry holes (here: still-puff eval + deferred-impossible character)."

play_check:
  - "Validate the plan against real code (the owner's ask), separate established from inference: DONE (code-grounded;
    overstated critiques refuted by the referee)."
  - "(owner) owner challenged the adopted plan + the 'small' framing, said «ок» to the changes, and asked for a separate
    unclipped test scene — folded as his actual words/decision."

log: adversarially validated the gas-visual plan vs real dev2 code (owner challenged blind adoption) — KEEP the spine,
  root cause = coarse grid + box-AABB clip (not a weak shader); folded 2 surviving holes + owner asks into c-visual-002
  (unclipped in-motion lab + early two-type-character probe + differentiating levers + perf-unverified); "small" framing
  corrected.

next:
  call: c-visual-002 (work/c-visual-002-call.md, REVISED) — owner opens it in a FRESH GasCoopGame_dev_2 session, opens
  with a PROPER PLAN (may split).
END_OF_RESULT
```

END_OF_FILE: live/indie-game-development/history/s-visual-007.md
