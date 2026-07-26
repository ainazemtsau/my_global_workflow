# Knowledge — Sc-sense delivered as an UNWIRED foundation (g-9c41)

read_by: the Sc-damage shape session (c-shape-sc-damage-001) and its executor; any later leg that consumes
player dose. Read BEFORE framing/wiring Sc-damage.

## Fact

Sc-sense (c-exec-035, DELIVERED + close-verified 2026-07-09 at GasCoopGame @defade72) built the engine-free
player↔gas exposure/dose FOUNDATION, but it is **not wired into the live simulation loop (`SimInstance`)**.
The dose read + integration are proven byte-identical and deterministic **only at the headless
`PlayerSenseContractHarness` level** and via the FishNet loopback witness. The only thing currently *driving*
the sense/dose in a running scene is the Unity debug adapter `GasSenseCapsuleDebug`, which paces sense ticks by
`Time.deltaTime` (wall-clock cadence) — that is owner-eye confidence, NOT the authoritative sim loop.

## Why it matters / how to apply (for Sc-damage)

Sc-damage is the first CONSUMER of dose. When it wires Sc-sense into the real loop it MUST:

1. **Feed the COMMITTED post-step field once per sim tick** — read exposure from the authoritative near field
   *after* the gas tick commit boundary, exactly once per committed tick per actor. Do NOT inherit the debug
   adapter's `Time.deltaTime` cadence (that can coalesce/skip ticks under frame hitches and is not the
   per-committed-tick dose semantic).
2. **Keep the dose invariant end-to-end** — the harness proves byte-identical dose for identical lockstep actor
   streams; wiring it into `SimInstance` must preserve that (same committed-field read, canonical actor fold,
   the separate `PlayerSenseDigest` as the parity surface — never fold player/dose into gas `MeaningChecksum`).
3. **Consume via the socket, don't re-derive** — read per-actor `{DominantTypeId, exposure rows, dose rows}`
   from the existing snapshot; the socket is generic per-TypeId. Sc-damage owns thresholds/gas-id policy;
   Sc-sense deliberately hardcodes none.

## Contract anchors (product, GasCoopGame @defade72)

- `Assets/GasCoopGame/Core/Field/Sense/PlayerSense.cs` — NearActorExposureQuery / PlayerGasSenseState /
  PlayerSenseDigest / ClampAdd (saturating at long.MaxValue); dose accumulates once per committed tick,
  replaces (not re-adds) in Commit.
- `Assets/GasCoopGame/Core/Sim/TickInput.cs` — explicit actor-pose fields (HasActorPose/ActorId/Min*/Size*),
  not packed into Arg. `SimInstance.SubmitInput` uses `WithPeerId` to preserve pose.
- `docs/adr/ADR-E-0008-c-exec-035-sc-sense-player-gas-exposure-dose-foundation.md`.

## Residuals carried (non-blocking, hardening candidates for the next leg)

Saturating dose clamp is silent (a loud/observed clamp signal is optional if ever wanted); RED-first authorship
attested only in RESULT prose (squashed commit); mutation line-report not committed; order-independence /
boundary-biased / loopback-byte-identity assertions lack a dedicated planted-violation negative control;
in-grid empty-cell no-vivify rests on code reasoning (a one-line assert would harden it).

END_OF_FILE: live/indie-game-development/knowledge/g9c41-sc-sense-delivered-unwired.md
