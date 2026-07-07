RESULT s-research-concept-pitch-003 (owner dialogue on concept v1.1; no CALL id)
direction: indie-game-development   play: research   node/task: g-a7f2 / concept-pitch v1.2

outcome: |
  Owner corrected my engine overclaim and asked me to define, in general terms, what
  "waking" and "extracting/carrying-out" mean. Delivered as pitch v1.2.

  ENGINE HONESTY CORRECTION (owner right, accepted): the engine's byte-sleep is an
  OPTIMIZATION (a region with no net flux stops computing a front, stored compressed,
  wakes on flux — about equilibrium + CPU), NOT the design "sleeping monster gas". The
  design-sleep is a SEPARATE cheap layer built on top: a dormant game-state (holds its
  area, ~no harm, not reacting) + explicit wake triggers + on-wake activation. Compatible
  (settled gas physically doesn't spread) but not identical; v1.1's "sleep = literally the
  engine state" is retracted.

  WAKING defined: triggers (heat/fire/cold; pressure delta = door/breach/jet = shipped
  forced-flow S1; player disturbance with slow-ok / fast-spikes / some types on a single
  step; starting extraction = flow = wake; chain from a woken neighbor or reaction product;
  pipe/tank rupture dumping an already-active charge). Effects (a front appears = spreads/
  layers/seeks openings; density-bloom / height change; becomes reactive; becomes harmful
  from ~0 dose; may burst a directional jet; may cascade neighbors). Three hard rules:
  telegraphed, attributable, readable-in-advance — else invisible-threat = unfair = the
  genre's death.

  EXTRACT+CARRY defined (the crux "make extraction interesting"): NOT aim-a-vacuum-watch-a-
  bar (The-Cycle fatigue). Instead HERD + HOLD + RACE: (1) extract an active STATE-WINDOW
  not the sleeping copeck-gas → must wake AND hold the profitable state; value = state ×
  amount at peak; (2) HERD the gas into a container using the BUILDING (jets/wind/doors/
  heat-cold gradients/funnel geometry/breach for draft) — spatial puzzle, co-op non-
  separable at 3-4; (3) RACE + seal-at-peak (overfill=rupture, wrong state=contamination);
  (4) CARRY the live-cargo canister out through the floor you woke (your earlier route now
  hostile), banking only at the top, drop-on-down = rescue-or-cargo. Combining two gases =
  deep field-crafting layer, deferred out of the first validated loop.

  POSITIONS/critique: sources/pipes = escalation EVENTS (rupture a fixed charge), not
  steady faucets (a faucet breaks the finite-inventory tension the owner values + mass
  legibility). Recon time-pressure = ENDOGENOUS agitation from player presence (still=slow,
  rushing=spike, floor eventually self-wakes), not a hard egg-timer. Damage = generic-first
  (dose→HP), typed effects later (Sc-damage slice). Two risks flagged loudly: quiet recon
  is a commercial/pacing danger (keep it 2-3 min of tension, not 15 min of cartography);
  scope discipline (first grey-box = one gas, wake, herd, carry, second player — everything
  else post-validation).

evidence: |
  Pitch v1.2 appended verbatim to work/concept-pitch-2026-07-07.md (engine correction +
  waking definition + extract/carry definition + positions + fork resolution). Engine
  grounding first-hand from knowledge/g9c41-gas-engine-SPEC.md (byte-sleep/settled_flag =
  optimization; forced-flow S1 shipped = выброс/ветер/jet; mass conservation + back-
  pressure; dose = coarse time-integrated D6; Sc-damage is a later slice). Fun UNVERIFIED;
  binding gate remains the two-player grey-box.

state_changes: |
  Apply mechanically (self-writer of this session).
  1. Append to live/indie-game-development/work/concept-pitch-2026-07-07.md (before its
     END_OF_FILE trailer) the «v1.2 — Просыпание, добыча, вынос» section as delivered
     (engine correction; waking triggers+effects+3 rules; extract-as-herd/hold/race/carry;
     positions on sources/recon-timer/damage/risks; fork resolution).
  2. Append to live/indie-game-development/LOG.md (before its END_OF_FILE trailer):
     2026-07-07 — research (g-a7f2/concept-pitch v1.2, s-research-concept-pitch-003): owner corrected my engine overclaim — byte-sleep = OPTIMIZATION (settled/no-flux), NOT the design "sleeping monster gas"; design-sleep = separate cheap layer (dormant state + wake triggers + on-wake activation). Defined "waking" (triggers: heat/pressure-delta/movement-speed/extraction/chain/rupture; effects: front appears/density-bloom/reactive/harmful/jet-burst/cascade; 3 rules telegraph+attributable+readable-ahead) and "extract+carry" (herd-into-container-with-the-building + hold/seal-at-peak + carry live cargo out through the mess; not aim-a-vacuum). Positions: sources = escalation events not faucets; recon pressure = endogenous agitation not egg-timer; damage generic-first. Risks flagged: quiet-recon is a commercial/pacing danger (keep it 2-3 min loud); scope discipline (first grey-box = one gas, wake, herd, carry, 2 players). Forks: (1) sleep not-safe/per-type wake threshold ACCEPTED; (2) sink DEFERRED to playtest; (3) paid-only-awake ACCEPTED. d-concept-hook-001 still open. → history/s-research-concept-pitch-003.md
  3. Create live/indie-game-development/history/s-research-concept-pitch-003.md
     containing this full RESULT.
  4. live/indie-game-development/NOW.md:
     4.1 Update header line to: updated: 2026-07-07 by s-research-concept-pitch-003
     4.2 In decisions/d-concept-hook-001: update the accept-pitch option to reference
         v1.2 (sleep-as-design-layer with per-type wake triggers, extract-as-herd,
         live-canister carry-out through the woken floor; sources = escalation events;
         recon pressure = endogenous agitation). Decision stays OPEN (owner converging,
         top verdict pending).
     4.3 Nothing else changes (bet, tasks, open_calls, recurring, parallel_tracks, next).
  5. TREE.md, CHARTER.md, knowledge/ untouched.

captures:
  - ENGINE GUARDRAIL (do not repeat): byte-sleep/settled_flag = optimization (no-flux equilibrium), NOT a design "dormant monster" primitive. Design-sleep is a built state-machine layer riding env-conditioned typing on the Sc road. Keep this distinction in any future concept/canon work.
  - Wake trigger "movement-speed accumulates agitation" doubles as the endogenous recon clock (floor self-wakes from cumulative player activity) — one mechanic, two jobs.
  - Emergent situations owner values (cloud-behind-cloud; flee into another invisible sleeper; one gas knocks another loose or gets absorbed) = free sim stories, the attributable/physical kind; affirm as a strength, do not script.
  - Extraction anti-pattern named for canon-forge: aim-a-vacuum-watch-a-bar (harvest fatigue). Extraction MUST be herd+hold+race using the building, or it collapses to grind.
  - Combining/reacting two gases to a richer product = deep mastery layer; explicitly DEFER out of the first validated loop.
  - Sources/pipes = escalation events (rupture a fixed charge), never steady faucets — protects finite-inventory tension + mass legibility.
  - Sc-damage slice inherits: generic dose→HP first; typed effects (freeze/blind/corrode) as the bestiary matures. Feed this into the Sc-damage PLAN when it opens.

decisions_needed:
  - d-concept-hook-001 (open): top verdict pending — accept pitch v1.2 as the canon-forge
    frame (rec: yes; grey-box stays binding). Three sub-forks now resolved in v1.2 (sleep
    not-safe/per-type; sink deferred; paid-only-awake yes).

play_check:
  - 1 Recite: done — job = integrate owner's corrections/questions, define "waking" and "extract/carry-out" in general terms, keep sparring; canon not-law this dialogue.
  - 2 Investigate: done — no new fan-out; engine facts re-read first-hand to CORRECT my prior overclaim (the substantive move of this turn); comparables reused.
  - 3 Confidence: done — engine-fact vs design-proposal split kept explicit; my v1.1 error named and retracted; damage numbers deferred; fun UNVERIFIED.
  - 4 Close: done — v1.2 appended, forks resolved + one top decision batched with recommendation, log line, next = awaiting_decision.

log: 2026-07-07 — research concept-pitch v1.2: engine overclaim retracted (sleep=optimization≠design-sleep); defined waking (triggers/effects/3 rules) + extract-carry (herd/hold/race, not aim-a-vacuum); sources=escalation, recon=endogenous, damage generic-first; d-concept-hook-001 still open.

next: awaiting_decision (d-concept-hook-001 top verdict; primary NOW.next remains work/c-exec-021-continuation-call.md).

END_OF_FILE: live/indie-game-development/history/s-research-concept-pitch-003.md
