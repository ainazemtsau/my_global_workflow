# s-visual-008 — triage the R&D-center Unity-tech note (VFX Graph / FEEL / Unity-upgrade decisions)

date: 2026-06-29
play: research/triage (owner-pasted the read-only Gas-Visual R&D Center's note while c-visual-002 builds; assess + decide)
node: g-7e15 (VISUAL track — G1 intact, g-9c41 untouched/running its own S2→S3 work)
owner-present: yes (directed: install VFX Graph; reminded FEEL is owned, Pro; offered to buy more)

## Input

The read-only Gas-Visual R&D Center (Codex-side, 1b3ea58) produced a disciplined note on modern Unity 6 / URP 17 / VFX
Graph tech for "hero gas" compatible with the read-only GridView seam. Owner: «посмотри есть что-то полезное» + «VFX
Graph не установлен но нужно установить» + «у нас есть FEEL (Pro), можем купить ещё если нужно».

## Assessment

The R&D is sound and INDEPENDENTLY reaches the same conclusion as the s-visual-007 validation: keep GasUber raymarch as
the load-bearing BODY; VFX/particles must NOT become a second source of truth over GridView. Its "URP has no built-in
volumetrics (HDRP-only)" finding corroborates that our custom raymarch is justified. Its blind spot = the SAME as the
dev plan: body+flair-focused, light on the owner's headline (per-type CHARACTER + spawn/jet MOMENTS).

VERIFIED in repo (first-hand): VFX Graph (com.unity.visualeffectgraph) NOT in Packages/manifest.json; built-in Particle
System IS present (the fallback is real); GasVisualRenderFeature.injectionPoint = BeforeRenderingPostProcessing and the
body is transparent → decals/post/VFX do NOT automatically see the gas (the R&D's render-order caution is real — a
mask/proxy is required).

## Decisions (owner-directed)

- LAYERING STRATEGY CONFIRMED: BODY = GridView→GasUber raymarch (load-bearing) | ACCENT = VFX Graph / Six-way (sparse,
  compute-gated, fallback = built-in Particle System / zero accents, reads visual data/events ONLY — never gas-position
  authority) | CONTACT = URP decals on opaque geometry | FINISH = fullscreen post (glow/distortion/warning pulse).
  Reject "VFX flipbook + six-way AS the core body" (= a second visual truth).
- INSTALL VFX Graph: YES (owner-directed) — but as a SEPARATE, deliberate, compute-gated ACCENT leg AFTER the
  c-visual-002 body checkpoint. NOT folded into the render-only c-visual-002 (a package install triggers a reimport/
  recompile that risks the running build). Guardrails: compute-gated + fallback; no gas authority in VFX.
- FEEL (owner owns, Pro): it does NOT help the gas BODY. It is the MOMENT/orchestration layer — on a spawn/jet/reaction
  event it fires a bundle of feedbacks (VFX/particle burst + post pulse + camera shake + sound + warning bloom). Pairs
  with VFX Graph (FEEL = conductor, VFX = the particles); also covers the R&D's fullscreen-finish/warning-bloom. Keep
  for the moment layer, not the body.
- NO purchases now: the body is custom (no asset buys it); accents/moments are covered by VFX Graph (free) + Particle
  System (free) + FEEL (owned). Flag a specific gap honestly if one appears later; default = don't buy.
- Unity 6.3 → 6.5 upgrade DEFERRED: no concrete gas-lab payoff (6.5 still has no URP volumetrics; its wins are
  shader-authoring niceties); don't mix an engine upgrade into a visual probe. Revisit only if a specific feature earns it.
- The ACCENT leg is REFRAMED (vs the R&D's generic-flair framing) as a per-type CHARACTER + spawn/jet MOMENT
  differentiator — closing the R&D's blind spot.

## state_changes

NOW.md g-7e15.next: appended the R&D-center triage block (layering confirmed + the 4 decisions + the accent-leg reframe).
LOG append. history/s-visual-008.md. NO TREE/CHARTER change (G9 not triggered); G1 intact; the running c-visual-002 body
leg is untouched.

## next

c-visual-002 body checkpoint (running) → then frame the ACCENT leg: install VFX Graph (compute-gated) + wire FEEL for the
moment layer, designed as a per-type character + spawn/jet differentiator. Timing of the install = after the body
checkpoint (owner to confirm).

END_OF_FILE: live/indie-game-development/history/s-visual-008.md
