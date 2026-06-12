# RESULT — s-arch-002 (research, 2026-06-12) — re-verify c-arch-001 at max effort

```yaml
RESULT s-arch-002 (call: c-arch-002, owner live instruction: re-verify c-arch-001 at max effort under new voice requirements)
direction: indie-game-development   play: research   node/task: g-9c41
outcome: |
  c-arch-001 re-verified at maximum effort per owner instruction; new voice
  requirements echo-numbered R5-R11 (meta/special gases incl. driver-backed;
  sim everywhere never frozen; vertical stratification in the coarse tier;
  hangars/corridors/shafts subdivide; resolution open below 25cm; plausible
  leak-side refinement; reactions everywhere with proximity-independent
  events). Verdict: v1 PARTIALLY REFUTED and superseded by brief v2
  (work/research-g-9c41-core-architecture-2026-06-12-v2.md):
  (1) coarse truth tier replaced — room-scalar T1 refuted under R7/R8 (hangar
  teleports gas x270-800 vs real fronts; node-average reactions wrong both
  ways); new T1s = geometry-conforming sector-band graph (archetype
  sectorization with fire-engineering thresholds; 2-3 vertical bands SHARED
  across density classes; buoyancy from combined mixture density; interface
  heights derived, never stored truth); donor family v1 missed: NIST
  CFAST/CONTAM zone models (public domain, CFAST 7.7.7 of 2026-05-28).
  (2) red team on the MERGED design (critic-mandated, never-attacked-before)
  found and fixed 2 fatal flaws: missing pressure/flow closure (added:
  algebraic per-sector pressure + quasi-steady orifice network solve pinned
  at base 10 Hz, exempt from rate ladders) and unsatisfiable window
  reconciliation invariant (added: per-band remainder-bucket, conservative
  cell<->remainder transfer); settling moved to unconditionally stable
  exponential-relaxation integrators (dt-independent).
  (3) R11 designed: one declarative reaction registry, intensive thresholds +
  hysteresis, tier exclusivity (no double evaluation), atomic multi-layer
  commit with joint deterministic arbiter, event plane contract #8
  (proximity-independent, self-contained events, client via NfE never gas
  stream); breach latency sim <=100ms / perceived 100-300ms. R5 designed:
  species-driver contract #9 (scalar source/sink day-one, twice precedented;
  velocity-intent spike-gated; AGENT_SUBSTRATE for non-field specials).
  (4) numbers corrected by independent audit: T2 budget 75-100k cells (gas
  <=4ms) until anchor re-bench (anchor is already-jobbed + K-multiplier);
  honest dirty chunk 0.6-6 KB (measure first); MISSING aggregate host clamp
  added (~250-300 KB/s total gas); far summaries need own deadband (all-dirty
  floor 79 KB/s); wake burn-in <=1 tick/frame.
  (5) anti-god-object audit vs A1: six-component boundary map (TopologyCore /
  FieldFabric kernel / GasDomain / Interest-LOD / NetAdapter / UnityAdapters),
  full 13-contract set incl. new #12 SnapshotState and #13 ReplayJournal
  (window-placement journaled as inputs — else deterministic replay impossible).
  (6) appetite reality: full day-one surface was ~2x the 6-week appetite —
  staged cut delivered (day-one with stub-not-skip contracts; net spike weeks
  1-2.5 over approach-A primitive field BY NAME as load generator; bands
  strictly AFTER stream lock with degrade-to-scalars fallback; clip ~07-10
  from band state, NO T2 dependency; bet-2 and parked lists explicit).
  Judges: 3 independent lenses all pick sector-band graph (8.5-8.7) over
  macro-voxel (3.5-4: walls inside cells in generator-agnostic geometry) and
  room-graph patch (5.5-6: corridors stay one node — advancing front dies).
  ARCH-1v2 still contains approaches C and A as configurations.
evidence: |
  Process: 26 agents across two workflows (wf_f1c81b92: 6 refuters — ALL
  holds_with_amendments high-confidence; 5 gap researchers with dated
  sources; 3 judges unanimous A; completeness critic. wf_ba1c4d71: 4 hostile
  red-teamers on the merged design — RT1 numerics needs_rework (2 fatal,
  fixed), RT2 contracts sound_with_fixes (god-object drift mapped out), RT3
  appetite needs_rework (day-one 2x — cut delivered), RT4 arithmetic (5
  number clusters corrected, 1 missing binding constraint found)). Parent
  arithmetic script-checked twice. done_when of c-arch-001 re-matched by v2:
  ladder incl. configurable cell (§3.1/3.5, R9 incl. sub-25cm); grid verdict
  + buy-vs-build updated (§3.9/§6: donor re-scope, building-science sweep
  added); procgen contract v0.2 + PGG verdict re-checked same-day (§3.7);
  scale/net arithmetic corrected in numbers (§4); ranked candidates +
  recommendation + 13 draft contracts + risk ranking with named tests
  (§6/§3.9/§7); established-vs-inference + dated sources (§9); archive
  imports with reasons (§10). Owner's new requirements quoted/echo-numbered
  in brief §1; design-vs-architecture scope split honored (gas taxonomy ->
  g-d3a8).
state_changes: |
  live/indie-game-development/work/: + research-g-9c41-core-architecture-2026-06-12-v2.md
  (supersedes v1 for decision use; v1 file stays as precedent/source base).
  live/indie-game-development/NOW.md: next CALL c-shape-003 updated — context
  now leads with the v2 brief (v1 demoted to precedent base), riskiest-
  assumption wording updated (breach-load + dirty-chunk measurement);
  decision_inbox += one entry: 5 batched requirement clarifications (brief v2
  §8, each with recommendation) to answer at or before c-shape-003.
  Everything else unchanged (active_bet none, open_calls keeps c-frame-002).
  live/indie-game-development/LOG.md: append research line -> history/s-arch-002.md.
  live/indie-game-development/history/: + s-arch-002.md (this RESULT).
  No TREE.md / CHARTER.md changes (G9 untouched).
captures:
  - "donor family correction: coarse stratified tier donors = NIST CFAST (7.7.7, 2026-05-28, public-domain-class) / CONTAM / EnergyPlus AFN (BSD-3) / Modelica Buildings (BSD-3) — MATH not code; SS14 (MIT) re-scoped to fine tier + reaction/hotspot/explosion-queue SEMANTICS; excited-groups imported as wake/sleep triggers only, sleep representation must keep full band state (never average)"
  - "novel-synthesis risk line (no direct donor anywhere): game-tick stratified multi-species zone solver with networked delta — carried as risk #2 with named harness tests (sealed-room+source, cold-rung checkerboard, interface crossing, hot-CO2 inversion, Steckler room)"
  - "first net spike MUST measure dirty-chunk wire size (honest range 0.6-6 KB) before any stream budgeting; aggregate host gas clamp ~250-300 KB/s is the binding uplink constraint (was missing in v1)"
  - "clip recipe needs NO T2: scripted breach -> heavy gas fills rooms bottom-up across the interface line, quantized volumetrics over band state — render proof slice weeks 2-4 owns the ~07-10 milestone"
  - "DA vertical data NOT extractable from queryable models (Cell.Bounds is 2D X-Z) — ceilings/sillZ via theme conventions + occupancy voxelization (bet-2); naive adapter day-one ~1 agent-week; DA now a schedule-critical-path candidate, not a cheap seam"
  - "approach-A primitive field adopted BY NAME as day-one load generator: Stage-0 band summaries alone cannot exercise the chunk-stream risk — relevant to the owner's approach choice in c-shape-003"
  - "maintenance candidate reinforced: standing owner requirements again arrived by voice mid-research (R5-R11) with no home in live state — second occurrence; work/maintenance-request-2026-06-12-standing-requirements.md still pending owner launch"
  - "fp16 mass storage (2K+6 B/cell) viable only with T1 reconciliation absorbing drift — noted for engineering, not day-one"
decisions_needed:
  - "(a) R6 intent: cold rung 1 Hz still counts as 'never frozen' (day-one runs whole coarse tier at 10 Hz anyway)? Recommendation: yes — floor rules (reactions >=1 Hz, breach 10 Hz) make the ladder safe"
  - "(b) far-consequence latency: sim <=100 ms / perceived 100-300 ms acceptable? Recommendation: yes — tighter is an order of magnitude costlier"
  - "(c) R7 representation: 2-3 shared bands + derived interface heights = 'stratification represented' (N bands stays a config escalation)? Recommendation: yes"
  - "(d) special gases day-one = scalar source/sink drivers only; velocity-intent spike-gated under net risk #1? Recommendation: yes"
  - "(e) perception ceiling: is far spatial structure visible in horror lighting at all (decides how wide far fidelity must be)? Recommendation: answer empirically inside the render proof slice"
play_check:
  - "1 recite: done — owner's live instruction restated (re-verify at max effort, v1 as base, redo not required if coverage holds); honest coverage answer given (R7/R8/R11/R5 were v1 gaps); voice requirements echo-numbered R5-R11 per owner communication rule; design-vs-architecture split declared (gas taxonomy -> g-d3a8)"
  - "2 investigate: done — workflow 1 (15 agents: 6 refuters, 5 gap researchers, 3 judges, 1 critic), workflow 2 (4 hostile red-teamers on the merged design, closing the critic's 'never attacked' gap), parent arithmetic script-verified; all dated sources carried into brief §9"
  - "3 confidence: done — [факт]/[сообщается]/[вывод] tags; corrected-numbers table with explicit assumptions and uncertainty ranges; every unmeasured load-bearing quantity named with its measurement (dirty-chunk size, throughput anchor, dirty-rate); §11 what-would-change-the-answer incl. judges' flip conditions"
  - "4 close: done — this RESULT; brief v2 via state_changes; owner decision points batched with recommendations (G7) into decision_inbox; knowledge candidate not proposed (shape/review will graduate); next = c-shape-003 per CALL.return"
log: "2026-06-12 — research (№2, max effort, owner-ordered re-verify): v1 partially refuted, brief v2 delivered — coarse truth = sector-band graph (owner's R7/R8 killed room-scalar T1; CFAST/CONTAM donor family found), red team fixed 2 fatal flaws of the merged design (pressure closure, remainder-bucket invariant), reactions/events/species-drivers designed (R11/R5), numbers corrected (T2 budget 75-100k cells, dirty chunk 0.6-6 KB, aggregate host clamp added), 13 contracts + 6-component anti-god-object map, staged day-one/bet-2/parked cut fits 6w appetite; 3 judges unanimous; 5 owner clarifications -> decision_inbox. next = c-shape-003. → history/s-arch-002.md"
next: |
  CALL c-shape-003
  to: session
  direction: indie-game-development
  play: shape
  node: g-9c41
  goal: |
    The shaping of g-9c41 paused at s-shape-002 is finished into the direction's
    first owner-approved bet, with the architecture brief v2 on the table:
    approach chosen by the owner (A/B/C/hybrid), the 5 batched requirement
    clarifications answered (decision_inbox), R1-vs-node-wording resolved under
    G9, minimal solution with explicit not-included list, real cut list (G6),
    lens sweep verdict per lens (G6), riskiest-assumption task first, <=3 tasks
    sized <=half a focused day, kill_by fixed (G4), g-9c41 -> active with the
    bet in NOW.md.
  context: |
    live/indie-game-development/work/research-g-9c41-core-architecture-2026-06-12-v2.md
    (the architecture brief, SUPERSEDES v1: sector-band coarse tier, 13
    contracts, corrected numbers, staged day-one/bet-2/parked cut, §8 = the 5
    owner questions with recommendations; ARCH-1v2 contains approaches C and A
    as configurations; day-one includes approach A's primitive field by name);
    live/indie-game-development/work/research-g-9c41-core-architecture-2026-06-12.md
    (v1 — precedent/source base only);
    live/indie-game-development/work/shape-g-9c41-approaches-2026-06-12.md
    (approaches A/B/C + hybrid, glossary);
    live/indie-game-development/history/s-shape-002.md (R1-R4),
    history/s-arch-002.md (this RESULT, R5-R11 echo),
    history/s-shape-001.md (appetite FIXED 6w / 2026-07-24 / clip ~07-10),
    TREE.md (g-9c41 done_when 1-8), history/s-map-002.md (P6/P7/P12).
  boundaries: |
    Appetite FIXED (G3): 6 weeks to 2026-07-24 — not re-litigated, never
    extended. P6 network model stays locked. Approach choice, the 5
    clarifications, and any TREE wording change are the owner's in-session
    calls (G9); the brief informs, never decides. Shape only g-9c41; no
    CHARTER edits (c-frame-002 queued separately).
  done_when: |
    NOW.md holds the owner-approved bet on g-9c41 (G3/G4 valid) with <=3 tasks
    <=half a focused day each, riskiest assumption first (candidate per brief:
    net spike over primitive field measuring dirty-chunk size under breach
    load); cut list + lens sweep verdicts recorded (G6); decision_inbox items
    answered and recorded; R1-vs-node-wording decision recorded (TREE edit only
    with owner_approved, G9); next = first work-session CALL.
  return: |
    RESULT with the approved bet + tasks, log line, next CALL (first work
    session).
  budget: one session
  parent: s-arch-002
  surface: any (Fable 5 window until 2026-06-22 — the net-spike CALLs benefit most)
```

END_OF_FILE: live/indie-game-development/history/s-arch-002.md
