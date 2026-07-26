# RESULT — s-shape-001 (shape, 2026-06-12) — checkpoint

```yaml
RESULT s-shape-001 (call: c-shape-001) — checkpoint
direction: indie-game-development   play: shape   node/task: g-9c41
outcome: |
  Shape of g-9c41 half-done by design (two-session shape per play note — appetite
  exceeds a week). Fixed this session: appetite 6 weeks, hard end 2026-07-24, internal
  clip-milestone target ~2026-07-10 (owner-picked from 4w/6w/8w with 3 comparables).
  Three structurally different approaches tabled, each with its one bet-assumption,
  kill condition and repo implication: A net-first greenfield on the G4A foundation
  (build), B sim-port from TheLastExit then netcode (reuse), C thin-slice T1-only
  room-graph (make-most-work-unnecessary). Repo finding: all three land in
  GasCoopGame@236bc30e as canonical product repo (fresh start dominated — G4A accepted
  2026-05-23; TheLastExit = evidence mine only); the approach choice decides only what
  gets imported. Approach choice deliberately NOT made (incubation >=1 night).
approaches_tabled: |
  A — «Сеть первой: greenfield на фундаменте G4A» (build).
    Repo: GasCoopGame@236bc30e (accepted 2026-05-23 foundation: harness, composition
    seam, validation entry, topology-interface, domain-first).
    Mechanism: first ~2 weeks lock the replication model in hardware — NfE
    listen-server + custom chunked-delta stream over a deliberately primitive field
    (trivial diffusion on room-graph), 2 clients, headless runs on MTS-pattern scenes.
    Stream contract locked -> behind it grows the real sim: T1 room-mass multi-gas
    with declarative two-level types + MINIMAL T2 (in-room detail for the clip and
    the moat proof), DA adapter, scripted breach, render proof slice <=2 weeks.
    Bet-assumption: the schedule is eaten by the network model, not sim richness — a
    new minimal sim behind a locked contract beats any port. Old code = reference
    only (A1: no direct transfer).
    Killed if: chunked-delta cannot hold 2-client consistency on min-spec early
    (~2 weeks in) — then the P6 timeboxed rollback/lockstep spike (1-2w) or bet death.
  B — «Порт сима из TheLastExit, сеть второй» (reuse).
    Repo: GasCoopGame + transfer of the named starting set (Gas.Config/Foundation/
    Topology/T1/T2 + legacy Grid substrate) per clean-start boundary.
    Mechanism: mature single-player gas behavior in the harness from ported code
    first, then NfE + chunked-delta on top.
    Bet-assumption: maturity of the old sim's behavior outweighs its architecture
    debt — porting within A1 constraints beats rewriting.
    Honest against (from own audits): A1 forbade direct code transfer, legacy room
    ids as identity, and monolith carry-over; the multiplayer-readiness guardrail
    demands command/commit, version/change-set, snapshot/delta seams the old code
    lacks; network risk slides to the end of the appetite (anti-pattern — Stationeers
    lost a cycle swapping transport alone); the FishNet brief of that generation is
    superseded by P6 (NfE default, model locked / vendor swappable).
  C — «Тонкий срез: строится только то, что меряет done_when»
    (make-most-work-unnecessary).
    Repo: GasCoopGame@236bc30e.
    Mechanism: room-graph T1-only (containers + portals; T2 entirely behind a seam —
    NOT in this bet), 2 meta-gases + a third as pure config, breach = scripted
    topology event (no destruction system), DA-minimum (PGG cut), NfE chunked-delta
    at room granularity, render slice per criterion 6.
    Bet-assumption: "representative" and the spectacular clip (criterion 8) are
    reachable at room-level granularity with render interpolation — no in-room detail.
    Risk: if the render proof slice shows mush instead of flows, T2 returns to scope
    mid-appetite.
  Preliminary recommendation for incubation (not a decision): A with C's scope
  instincts applied at the scope-hammer step; B dominated by the direction's own
  audit evidence.
evidence: |
  Appetite (owner step, his selection): «6 недель, до 24.07 (Recommended)» —
  in-session answer 2026-06-12. Comparables used: own G4A pace (~3 weeks,
  closed 2026-05-23), Stationeers transport-swap cycle (revert 2026-01-09 ->
  re-release 2026-01-28), Noita Entangled Worlds (solo modder, months part-time).
  Calendar arithmetic: core worth <=6-7 weeks counted back from press-preview demo
  2026-09-21 / asset-lock ~2026-08-08 (demo is built FROM the core, needs ~6-8 weeks).
state_changes: |
  live/indie-game-development/NOW.md: next replaced with CALL c-shape-002 (continue
  shape on g-9c41: choose approach, steps 4-9, owner-approved bet; appetite FIXED
  6w/2026-07-24 in boundaries). Everything else unchanged (active_bet none, open_calls
  keeps c-frame-002, decision_inbox empty).
  live/indie-game-development/LOG.md: append checkpoint line -> history/s-shape-001.md.
  live/indie-game-development/history/: + s-shape-001.md (this RESULT).
  No TREE.md / CHARTER.md changes (no owner-approved tree artifact yet — G9 untouched;
  appetite rides the continuation CALL until the bet is approved).
captures:
  - "repo canonization rider for queued c-frame-002: once c-shape-002 approves the bet, CHARTER 'Canonical repos' must encode GasCoopGame@236bc30e as product repo (TheLastExit = evidence-only source)"
decisions_needed: []
play_check:
  - "1 recite: done — node goal (outcome-phrased, no fix), 8 done_when criteria, parent g-a7f2 restated"
  - "2 appetite (owner): done — proposed 6w over 4w/8w with 3 comparables; owner: «6 недель, до 24.07 (Recommended)» -> 6 weeks, end 2026-07-24, clip target ~2026-07-10"
  - "3 approaches: tabled (A build / B reuse / C make-unnecessary, each with one bet-assumption + repo implication + kill condition); PICK deferred to c-shape-002 per play note (appetite > week => two-session shape, >=1 night incubation); preliminary recommendation recorded: A with C's scope instincts"
  - "4 scope hammer: deferred to c-shape-002 (play note)"
  - "5 lens sweep: deferred to c-shape-002 (play note)"
  - "6 riskiest assumption: deferred to c-shape-002 (candidate named in CALL: networked chunked-delta gas slice on min-spec)"
  - "7 tasks: deferred to c-shape-002 (<=3 per CALL, rolling wave)"
  - "8 kill criteria: deferred to c-shape-002 (kill_by date anchor = appetite end 2026-07-24)"
  - "9 close: this checkpoint RESULT (play note: close with checkpoint once approaches are on the table); no bet in NOW yet — G1/G9 untouched"
log: "2026-06-12 — shape (checkpoint): g-9c41 appetite owner-fixed — 6 weeks to 2026-07-24, clip-milestone target ~07-10; 3 approaches tabled (A net-first greenfield on G4A / B sim-port TheLastExit / C thin-slice T1-only), repo finding: all land in GasCoopGame@236bc30e; choice + steps 4-9 -> c-shape-002 after >=1 night incubation. -> history/s-shape-001.md"
next: |
  CALL c-shape-002
  to: session
  direction: indie-game-development
  play: shape
  node: g-9c41
  goal: |
    The shaping of g-9c41 started in s-shape-001 is finished into the direction's first
    owner-approved bet: approach chosen from the three tabled (or a sharper hybrid),
    minimal solution sketched with explicit not-included list, real cut list (G6), lens
    sweep verdict per lens (G6), riskiest-assumption task first, <=3 tasks sized <=half
    a focused day, kill_by fixed (G4), product-repo decision sealed in the bet,
    g-9c41 -> active with the bet in NOW.md.
  context: |
    live/indie-game-development/history/s-shape-001.md (FIXED appetite 6w / end
    2026-07-24 / clip target ~2026-07-10; approaches A/B/C with bet-assumptions and
    kill conditions; repo finding: GasCoopGame@236bc30e canonical in all three,
    preliminary recommendation A+C-scope);
    live/indie-game-development/TREE.md (g-9c41 + root map_order);
    live/indie-game-development/history/s-map-002.md (amendments P1/P6/P7/P11 + captures);
    live/indie-game-development/work/audit-tree-2026-06-12.md §5 (shape tactics);
    archive evidence (read-only): clean-start set, multiplayer-readiness guardrail,
    old nucleus functional spec (MTS scenes), A1 audit, FishNet brief (superseded by P6).
  boundaries: |
    Appetite is FIXED (G3): 6 weeks to 2026-07-24 — not re-litigated, never extended.
    Shape only g-9c41; no CHARTER edits (c-frame-002 queued; repo canonization rides it
    after bet approval). Approach choice is the owner's call this session, >=1 night
    after s-shape-001 (2026-06-12).
  done_when: |
    NOW.md holds the owner-approved bet on g-9c41 (appetite 6w/2026-07-24, done_when,
    kill_by — G3/G4) with <=3 tasks <=half a focused day each, riskiest assumption
    first; cut list recorded; lens sweep verdict per lens; G1-G6 pass; next = first
    work-session CALL.
  return: |
    RESULT with the approved bet + tasks, log line, next CALL (first work session).
  budget: one session
```

END_OF_FILE: live/indie-game-development/history/s-shape-001.md
