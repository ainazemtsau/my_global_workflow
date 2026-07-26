# RESULT — s-work-022 (work · g-9c41/S1 · resolve c-exec-015 spike-report D1+D4; reconcile vs concurrent s-work-021)

play: work
direction: indie-game-development
node: g-9c41
task: S1 (c-exec-015, in_flight)
date: 2026-06-26

## outcome

The owner pasted the c-exec-015 Step-0 spike report (`docs/c-exec-015-spike-findings.md`, dev) with four routed-home
decisions D1–D4. RECONCILE: a CONCURRENT session (s-work-021) had already decided D2 + D3 (the 2 Codex P2s) and put the
leg in_flight — so I did NOT re-decide them; I added only the genuinely new delta: D1 (the substantive directionality
call, resolved live with the owner) and D4 (scene strategy). The leg stays cheap TIER-1 with a sharpened owner-eye
target (a visible jet on the cubes); the velocity-tier stays reserved.

## evidence

- First-hand reconcile: HEAD `185b886`; the spike report read in full (dev `docs/c-exec-015-spike-findings.md`); dev tip
  `bbc70df` (primitive committed, 843 tests), spike consolidation uncommitted on dev — all verified first-hand.
- Found my in-flight edits this turn had re-decided D2/D3 (contradicting the committed `d-bias-quantum-001` ±1-floor
  decision) and collided on the `s-work-021` label → reverted them and rewrote as a clean `s-work-022` delta
  (memory: [[workflow-stale-call-reverify-committed-state]]).

## D1 resolution (the substantive owner call, resolved in-session)

Owner CONFIRMED the game needs gameplay-meaningful directional JETS that deal more damage (by concentration; "gas can
spawn anywhere, in different conditions" — e.g. loot with gas breaks mid-room), BUT chose cheap TIER-1 WITHOUT inertia
NOW and revisit. CRUX correction surfaced this turn: the spike's open-space ≈2:1 lean measured forward-bias on ONE face
only — it NEVER tried LATERAL CONFINEMENT. So TIER 1 stays, with a sharpened owner-eye target = a VISIBLE directional
JET on the debug CUBES, via a jet-emitter that pushes forward AND clamps the lateral faces (emitter-born one-way valves
/ inward bias — travels WITH the jet wherever it fires; NOT level walls). Tune tightness on the cubes. If even with
confinement it cannot read as a tight open-space jet → the concrete trigger to escalate to TIER 3 (fixed-point velocity,
lock-crack ADR-0010). NO coasting/inertia this leg (accepted). Damage = concentration is a later combat slice.

## state_changes

- NOW.md d-gas-richness-tiers-001: prepend the D1 SPIKE RESOLUTION note (cheap tier + jet-on-cubes target; references
  the committed D2/D3 + D4 decisions).
- NOW.md decision_inbox: ADD d-scene-one-polygon-001 (answered, planner spec-amendment = ONE curated sandbox scene +
  forced-flow MODE, not scene-per-feature; standing convention).
- NOW.md next: extend the in_flight relay with D1 (jet-emitter + lateral confinement target) + D4. NOW.md phase: prepend
  the s-work-022 entry.
- work/c-exec-015-call.md: §AMENDMENT (D1 jet target + D4; references committed D2/D3). LOG.md: one line.

## captures

- FEEDBACK (durable): do NOT pitch building a throwaway test-rig/demo to settle a head/design decision — a real feature
  ≠ a demo crutch. And the gas model is OPEN-SPACE-FIRST: gas spawns anywhere, in any condition; drop the
  walls/level-geometry assumption. (Owner corrected this sharply this turn.)
- The jet-emitter "lateral confinement" insight: the spike's 2:1 open-space verdict is INCOMPLETE — it only pushed
  forward; clamping the lateral faces (valves/inward bias) should yield a tight jet without a velocity field. This is the
  next concrete thing to build + tune on the cubes.

## decisions_needed

None blocking. D1 resolved with the owner (cheap tier now, jet-on-cubes target, velocity-tier reserved with a concrete
trigger). D4 decided (spec amend). D2/D3 already decided (s-work-021). The build session resumes with all four relayed.

## play_check (play: work)

1. Recite — DONE: the spike returned; the four decisions; reconciled against the concurrent s-work-021.
2. Owner inputs (owner) — DONE: D1 is the owner's own design call, resolved live this turn (he confirmed directional
   damaging jets, chose no-inertia-now); his words drove it.
3. Do the work — DONE: reconciled (reverted colliding edits), resolved D1 + D4, relayed to the build session, amended
   the CALL; deferred to the committed D2/D3.
4. Self-check — DONE: verified the committed D2/D3 first-hand before deferring; the new delta does not duplicate or
   contradict committed state.
5. Close — DONE: this RESULT; next = the build session resumes c-exec-015 with D1–D4 relayed.

## log

2026-06-26 — work (g-9c41/S1, s-work-022): c-exec-015 spike-report D1+D4 resolved with owner; reconciled vs concurrent
s-work-021 (D2/D3 already decided, not re-decided). D1 = cheap tier, jet-on-cubes via lateral confinement, no inertia,
velocity-tier reserved with a concrete trigger. D4 = ONE-scene spec amend. → history/s-work-022.md

## next

The c-exec-015 build session (GasCoopGame_dev, dev) resumes with all four decisions relayed: D1 (jet-emitter with
lateral confinement → visible jet on the cubes; no inertia), D2 (±1 floor, RED-first), D3 (RW3 ledger honesty,
independent author), D4 (one curated scene + forced-flow mode). Then STEP-0 close → выброс/выдавливание/ветер/valve.
RESULT applied home by a separate OS writer.

END_OF_FILE: live/indie-game-development/history/s-work-022.md
