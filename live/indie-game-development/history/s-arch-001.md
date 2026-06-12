# RESULT — s-arch-001 (research, 2026-06-12)

```yaml
RESULT s-arch-001 (call: c-arch-001)
direction: indie-game-development   play: research   node/task: g-9c41
outcome: |
  c-arch-001 closed in ONE session (budget 2-3, hard stop 2026-06-15 beaten).
  Architecture brief delivered to work/research-g-9c41-core-architecture-2026-06-12.md,
  five sub-questions answered so they compose:
  (a) granularity ladder: T1 room-graph backbone (always on, whole level, mass
  authority) + windowed T2 voxels (25/50cm as PER-REGION config, chunk fixed in
  cells => wire format cell-size-invariant) + render-LOD outside authority;
  uniform full-fine field refuted by numbers (25cm: 352MB, 61-154ms/tick);
  established: NO shipped 3D game does sub-meter volumetric gas (finest =
  Stationeers 2m cells).
  (b) owner's "each mechanic in its own layer, synced via the grid" CONFIRMED as
  data plane with 3 amendments: (1) sync = revisioned change-feeds in fixed tick
  phases, not free-form events; (2) single writer per layer, topology only via
  command->validate->commit (A1); (3) grid stays narrow (A1 no-god-object).
  Weighed on equal footing vs pure-ECS (measured anti-pattern for field data;
  ECS kept for entities/ghosts) and service-mesh (O(n^2) contracts, duplicated
  dirty-tracking; its typed-contract discipline imported as amendment 2).
  Buy-vs-build: NO networked authoritative 3D gas product exists for Unity
  (5 independent search angles) -> build core + thin fabric; SS14 atmos MIT
  (LICENSE verified) = algorithm/architecture donor; buy edges only (NfE locked
  by P6, DA/PGG procgen, render assets visual-only behind seam).
  (c) TopologyDocument v0 drafted (volumes, portals, breachable surfaces =
  latent portals for scripted breach, anchors; seal validation at ingest); DA
  fills it from model APIs [established]; PGG verdict (R3): day-one wiring NOT
  recommended (beta ~5y, no public API reference despite active 2026-02-21
  update) — seam proven day-one by TWO providers (DA + hand-authored harness
  scenes), PGG = timeboxed spike <=2-3 days behind the seam.
  (d) huge-level profile (200x200x40m, ~1500 volumes, ~3800 portals): T1
  everywhere = 325KB, <0.5ms; T2 windows 30 rooms @25cm = 307k cells / 7MB /
  1.2-3.1ms tick on min-spec 6-core @10Hz gas tick (worst 4-cluster party
  2-4.9ms); net steady ~90KB/s/client = inside shipped norms; breach burst
  14.4 Mbps x3 clients EXCEEDS 9 Mbps uplink floor (UK FTTC) -> clamps,
  hotness-priority chunk queue (Gas.Interest descendant), 10->5->3Hz rate
  ladder (SS14 ships at 3Hz), T1-only emergency mode — written INTO the stream
  contract; stream = own unreliable-sequenced UTP channel beside NfE (RPC 8KB /
  buffer-ghost x32-history unsuitable — doc-established).
  (e) ARCH-1 hierarchical-field-on-layered-grid RECOMMENDED over ARCH-2 uniform
  chunked field (#2: loses at R1 scale, wins on small levels; shared wire format
  keeps migration cheap) and ARCH-3 service mesh (#3); ARCH-1 contains
  approaches C and A as CONFIGURATIONS — does not pre-empt the owner's approach
  choice; 7 draft contracts; 6 ranked riskiest assumptions, #1 re-confirmed
  with test profile: chunked-delta consistency across a topology change on a
  real uplink under breach wave + 32ms/12ms/2% jitter.
evidence: |
  done_when match, point by point: granularity ladder incl. configurable cell —
  brief §2; grid ownership + communication verdict (hypothesis vs >=2
  alternatives on equal footing) + buy-vs-build sweep with dated sources — §3;
  procgen-ingestion contract draft incl. PGG day-one verdict — §4; scale/network
  arithmetic in numbers, not adjectives (script-checked) — §5; 2-3 ranked
  whole-architecture candidates + recommendation + draft contracts + riskiest
  assumptions — §6; established-vs-inference separated ([факт]/[сообщается]/
  [вывод] tags + §7 ledger), sources dated throughout; every archive import
  carries explicit reason — §8. Investigation: 8 archive docs + 7 parallel web
  research children (nominal group per play note), 40+ dated sources; key
  established anchors: SS14 atmos from code (1m tiles, excited-group dormancy,
  15Hz sim / 3Hz overlay @ 8x8 chunks, client never authoritative, MIT);
  Stationeers 2m cells + transport incident dates verified via Steam news API
  (revert 2026-01-09, re-release 2026-01-28); NfE 6.6 client-hosted first-class,
  UTP fragmentation 4KB / reliable window 32; DA GridDungeonModel/Snap query
  APIs expose rooms+doors; PGG v1.6.6.2.12 (2026-02-21), no public API docs;
  Steam survey May 2026 (16GB 41%, 6-core 28%); uplink floors UK FTTC ~9 Mbps.
state_changes: |
  live/indie-game-development/work/: + research-g-9c41-core-architecture-2026-06-12.md
  (the architecture brief; full text as committed in this commit).
  live/indie-game-development/NOW.md: next replaced with CALL c-shape-003 (resume
  shape on g-9c41 with the brief on the table; full text in NOW.md). Everything
  else unchanged (active_bet none, open_calls keeps c-frame-002, decision_inbox
  empty).
  live/indie-game-development/LOG.md: append research line -> history/s-arch-001.md.
  live/indie-game-development/history/: + s-arch-001.md (this RESULT).
  No TREE.md / CHARTER.md changes (research informs only; R1-vs-node-wording
  stays with c-shape-003 under G9).
captures:
  - "SS14 atmospherics is MIT (LICENSE.TXT verified 2026-06-12) — legally liftable algorithm/architecture donor for the gas core (with attribution); technically a reference, not a drop-in library (woven into RobustToolbox)"
  - "SS14 ships gas visuals at 3 Hz decoupled from 15 Hz sim — established precedent for our stream-rate degradation ladder"
  - "Teardown official MP syncs destruction as deterministic commands, never voxel data (Gustafsson, 2026-03) — supports breach-as-topology-event over geometry sync"
  - "Barotrauma hybrid (client-side field sim + thresholded server corrections, oxygen quantized 8-bit) = prepared fallback stream pattern if chunk-delta clamps fail on real uplinks; changes stream contract, not layer architecture"
  - "DA vendor risk: Unity branch 1.22.0 stale since 2024-11-29, Unity 6 not certified (reviews: fixable script bugs), author active on Unreal side — check at engineering start; generator swap stays behind the adapter seam"
  - "PGG spike (timeboxed <=2-3 days, behind the seam): single question — can its runtime output fill TopologyDocument; promote only on success (asset updated 2026-02-21, beta ~5y, no public API reference)"
  - "determinism policy (float vs fixed-point for host-side harness replay) — open engineering decision, not architecture-blocking; harness needs seeded replay either way"
  - "min-spec CPU pressure precedent: Stationeers recommends 6-8 cores for atmos-heavy servers; our host budget line: gas <=4ms/tick @10Hz on a 6-core — currently met with >=2x margin"
decisions_needed: []
play_check:
  - "1 recite: done — question/return format/budget restated in opening contract; the five sub-questions are the CALL's own bound structure ('answered so they compose'), answered as one program — no silent expansion"
  - "2 investigate: done — 8 archive docs read (each import carries its reason, brief §8); 7 parallel web research children run as a nominal group (play note), merged/deduped by parent; 40+ dated sources; throwaway arithmetic script-verified (allowed by boundaries)"
  - "3 confidence: done — [факт]/[сообщается]/[вывод] tags throughout; §7 established-vs-inference ledger; §9 'what would change the answer' (render-slice verdict, clamp failure -> Barotrauma fallback, DA friction -> vendor swap behind seam, PGG API publication, >x3 level size)"
  - "4 close: done — this RESULT; brief returned for work/ via state_changes + key verdicts summarized; knowledge candidate deliberately not proposed (the brief is the artifact; shape/review decide what graduates to knowledge/); next = c-shape-003 (return to parent track per CALL.return)"
log: "2026-06-12 — research: c-arch-001 closed in one session — architecture brief to work/ (T1+windowed-T2 ladder, per-region 25/50cm cell; owner's grid-layer hypothesis confirmed as data plane with 3 amendments over 2 alternatives; buy-vs-build: nothing to buy, SS14 MIT = donor; TopologyDocument contract, DA fills it, PGG behind seam; huge-level numbers: T2 windows 7MB/1.2-3.1ms, net 90KB/s/client steady, breach burst beats 9Mbps floor -> clamps in stream contract; ARCH-1 of 3 recommended, contains approaches C/A as configurations; riskiest re-confirmed: chunked-delta consistency across topology change). next = c-shape-003. → history/s-arch-001.md"
next: |
  CALL c-shape-003
  to: session
  direction: indie-game-development
  play: shape
  node: g-9c41
  goal: |
    The shaping of g-9c41 paused at s-shape-002 is finished into the direction's
    first owner-approved bet, with the architecture brief on the table: approach
    chosen by the owner (A/B/C/hybrid), R1-vs-node-wording resolved under G9,
    minimal solution with explicit not-included list, real cut list (G6), lens
    sweep verdict per lens (G6), riskiest-assumption task first, <=3 tasks sized
    <=half a focused day, kill_by fixed (G4), g-9c41 -> active with the bet in
    NOW.md.
  context: |
    live/indie-game-development/work/research-g-9c41-core-architecture-2026-06-12.md
    (architecture brief: granularity ladder, grid verdict, TopologyDocument
    contract + PGG verdict, scale/net arithmetic, ARCH-1/2/3 + draft contracts +
    risk ranking; ARCH-1 contains approaches C and A as configurations);
    live/indie-game-development/work/shape-g-9c41-approaches-2026-06-12.md
    (approaches A/B/C + hybrid, glossary);
    live/indie-game-development/history/s-shape-002.md (R1-R4 captures);
    live/indie-game-development/history/s-shape-001.md (appetite FIXED 6w /
    2026-07-24 / clip ~07-10; approaches detail);
    live/indie-game-development/history/s-arch-001.md (research RESULT);
    live/indie-game-development/TREE.md (g-9c41 done_when 1-8);
    live/indie-game-development/history/s-map-002.md (P6/P7/P12 conditions).
  boundaries: |
    Appetite FIXED (G3): 6 weeks to 2026-07-24 — not re-litigated, never
    extended. P6 network model stays locked. Approach choice and any TREE
    wording change are the owner's in-session calls (G9); the brief informs,
    never decides. Shape only g-9c41; no CHARTER edits (c-frame-002 queued
    separately).
  done_when: |
    NOW.md holds the owner-approved bet on g-9c41 (G3/G4 valid: appetite
    6w/2026-07-24, done_when, kill_by) with <=3 tasks <=half a focused day
    each, riskiest assumption first; cut list + lens sweep verdicts recorded
    (G6); R1-vs-node-wording decision recorded (TREE edit only with
    owner_approved, G9); next = first work-session CALL.
  return: |
    RESULT with the approved bet + tasks, log line, next CALL (first work
    session).
  budget: one session
  parent: s-arch-001
  surface: any (Fable 5 window until 2026-06-22 — early engineering CALLs benefit)
```

END_OF_FILE: live/indie-game-development/history/s-arch-001.md
