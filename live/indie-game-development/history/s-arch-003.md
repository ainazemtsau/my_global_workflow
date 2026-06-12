# RESULT — s-arch-003 (research, 2026-06-12) — exploratory: analytic gas representations

```yaml
RESULT s-arch-003 (call: c-arch-003, owner live instruction: exploratory side-research — analytic/functional gas representations, "collapse on observation")
direction: indie-game-development   play: research   node/task: g-9c41
outcome: |
  Owner's exploratory idea (parametric closed-form gas state evaluated lazily
  on observation, QM-collapse style) researched and adversarially tested
  against the v2 baseline. Verdict: NOT a replacement architecture (3 refuters,
  all "niche" high-confidence, two with numeric probes), BUT real findings:
  (1) the idea has an established scientific identity — Gaussian puff
  dispersion models (state vector 6-13 floats per puff, concentration = on-
  demand Green's function; exact closed-form sheared puff advanced without
  ticking until re-anchor events [Yamartino 2008]); indoors the established
  form is the multizone linear-ODE family — exactly the v2 sector-band graph,
  so the math independently confirms v2's position; the owner's "collapse"
  intuition is ALREADY in v2 as lazy T2 window materialization.
  (2) GH-1 lazy exact evolution: dead at runtime (whole-level tick already
  0.2-2.5 ms; frozen-matrix closed form measured 160-350x LESS accurate than
  slow ticking of the true nonlinear system while composition stratifies;
  re-anchor economics inverted: eigh 300 cells ~25 ms ~ 12 min of island
  ticking; threshold detection = multi-root trap, 66/67 double crossings;
  expm breaks replay determinism; KSP patched-conics precedent fails all four
  load-bearing conditions for our case). Survivors: offline exactness ORACLE
  for integrator unit tests + rate-ladder calibration with proven error
  bounds (adopt into harness now); equilibrium-clamping for sealed settled
  islands (parked, trigger: >=10x level scale + telemetry); QSS-style
  conservative wake-horizon bounds.
  (3) GH-2 puff wire: wire format dead (competes with band-summary fog at
  1-2 KB/update — nothing to save; walls eat simplicity; ranged ignition
  extends render-truth consistency to sightline range — CS2 lesson maps
  worse for us). Survivor = CLIENT-SIDE VFX PUFFS for transient breach/leak
  fronts spawned from already-broadcast event plane + inflow hints — a 1-2
  day render-slice spike with kill criteria, plausibly the cheapest path to
  the spectacular ~07-10 clip; plus two free policy borrowings for the
  NetAdapter contract: DIS update discipline (threshold + heartbeat, IEEE
  1278) and continuous client-side fog interpolation.
  (4) GH-3 modal in-sector state: dead as truth (numpy probe: truncated modes
  negative over 31% of sector width in exactly the leak-side regime targeted;
  positivity fixes destroy linearity; reactions on reconstructions produce
  false ignitions; best positive 2-DOF enrichment beats 2 bands by only 7%).
  Survivor: slope-limited lateral first moment as HINT-layer-only upgrade,
  parked behind a half-day numpy A/B with a pre-agreed decision rule; bonus:
  band (mass, centroid, spread) = degenerate puff parameters -> free emission
  adapter to the VFX puffs if both ship.
  Note delivered to work/research-g-9c41-analytic-representations-2026-06-12.md;
  v2 architecture unchanged; c-shape-003 not blocked.
evidence: |
  Workflow wf_22fa26e4 (8 agents): 5 explorers (puff/plume dispersion incl.
  Yamartino 2008 exact sheared-puff Eq.38 and Jia et al. Sci Reports
  2025-05-28 real-time costs; closed-form/QSS math; modal/ROM incl. OSTI
  positivity findings; game precedents incl. KSP on-rails and CS2
  billboard->voxel counter-precedent; parametric netcode incl. IEEE 1278
  dead reckoning) -> 3 refuters with structured verdicts, two backed by
  numeric probes (RF-A: buoyancy-coupled toy, frozen-A error 38-43% vs
  0.12-0.26% slow-tick; rate-ladder error curve 11%/1.4%/3e-7; RF-C: numpy
  mode-truncation probe, 31% negative width, +7.6-12.3% mass inflation from
  clipping). Every survivor carries an explicit cheapest probe with kill
  criteria. Owner's ask honored verbatim: "не обязательно... если что-то
  нащупал — напишешь, продолжим долбить" — the note's §0 answers exactly
  that, §5 names the two probes to continue with.
state_changes: |
  live/indie-game-development/work/: + research-g-9c41-analytic-representations-2026-06-12.md
  (exploratory note; informs only, v2 brief unchanged).
  live/indie-game-development/NOW.md: c-shape-003 context += one optional
  line pointing at the note (relevant to the render-slice plan: VFX-puff
  probe candidate; and to the NetAdapter contract: DIS discipline /
  interpolation borrowings). Everything else unchanged (active_bet none,
  open_calls keeps c-frame-002, decision_inbox keeps d-arch-001).
  live/indie-game-development/LOG.md: append research line -> history/s-arch-003.md.
  live/indie-game-development/history/: + s-arch-003.md (this RESULT).
  No TREE.md / CHARTER.md changes.
captures:
  - "render-slice candidate: client-side VFX Gaussian puffs for transient breach fronts (from event plane + inflow hints, zero host/net changes) — 1-2 day A/B spike vs interpolated sector fog, kill criteria written; plausibly the cheapest path to the spectacular ~07-10 clip"
  - "NetAdapter contract borrowings (free, adopt regardless): DIS-style update discipline (ship-on-perceptual-drift + heartbeat/timeout, IEEE 1278 lineage) and continuous client-side interpolation of sector-fog summaries (no snapping)"
  - "harness addition (adopt now, zero runtime risk): closed-form exactness oracle (expm/eigh of linearized settling subsystem) as unit-test reference + rate-ladder calibration with proven error bounds (measured curve: 0.5 Hz -> 1.4% @2min -> 3e-7 @10min)"
  - "parked with trigger: analytic equilibrium-clamping of sealed settled islands ('frozen with proof') — trigger: coarse tick becomes a real budget item (>=10x level scale) AND telemetry shows long sealed quiescent windows"
  - "parked behind half-day numpy A/B with decision rule (>25% seeded-error reduction or any reaction-crossing-time shift): slope-limited lateral first moment per band as hint-layer upgrade; if adopted, doubles as free emission adapter to VFX puffs (band mass+centroid+spread = degenerate puff)"
  - "conceptual validation for the owner: his 'collapse on observation' intuition is already implemented in v2 (lazy T2 wake-seeding); his 'few numbers + function' is the literal state vector of regulatory Gaussian puff models — the instinct was sound, the established indoor form of it (multizone linear ODEs) is exactly the v2 sector-band graph"
  - "negative result worth keeping: lazy closed-form evolution of coupled indoor gas fields is measurably WORSE than slow ticking while composition stratifies (frozen-A surrogate 160-350x error) — do not revisit without the named trigger conditions"
decisions_needed: []
play_check:
  - "1 recite: done — owner's exploratory ask echoed (parametric functions + lazy collapse, optional, 'if something is found we keep digging'); interpretation stated in opening contract; scope: graft candidates onto v2 baseline, not re-litigation of v2"
  - "2 investigate: done — workflow wf_22fa26e4: 5 explorers (nominal group) -> 3 refuters on the three graft hypotheses, two with numeric probes; dated sources throughout"
  - "3 confidence: done — [факт]/[сообщается]/[вывод] tags in the note; measured probe numbers quoted; every survivor carries its cheapest probe + kill criteria; honest negative results stated as findings"
  - "4 close: done — this RESULT; note via state_changes; verdict to the owner's exact question ('нащупали?') in §0; next = c-shape-003 unchanged (this research does not block or redirect it)"
log: "2026-06-12 — research (№3, owner-initiated exploration): analytic/functional gas representations tested — replacement architecture refuted with measurements (lazy closed form 160-350x worse while stratifying; modal truth negative over 31% width; puff wire loses to band-summary fog), but three survivors delivered: client-side VFX puffs for breach fronts (render-slice probe, clip candidate), DIS update discipline + client fog interpolation (free NetAdapter borrowings), closed-form exactness oracle for harness/rate-ladder calibration; owner's collapse intuition validated as already-implemented (lazy T2 seeding); note to work/. next = c-shape-003 (unchanged). → history/s-arch-003.md"
next: |
  CALL c-shape-003 — unchanged, full text in NOW.md (resume shape on g-9c41
  with brief v2 + decision_inbox d-arch-001; this note added to context as
  optional reading for the render-slice and NetAdapter parts).
```

END_OF_FILE: live/indie-game-development/history/s-arch-003.md
