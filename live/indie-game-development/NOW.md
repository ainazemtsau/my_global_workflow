# NOW — indie-game-development

active_bet: none

active_tasks: []

recurring: []

open_calls:
  - id: c-frame-002
    status: queued
    note: |
      Frame touch-up — encode the owner's 2026-06-12 money-gate clarification into
      CHARTER.md: December mark = small income OR credible potential (matches the
      charter's existing reframe letter); NEW hard wall = the game earning for real by
      ~12 months (EA no later than ~Q2 2027). Map session s-map-002 could not edit the
      charter (play boundary).

decision_inbox: []

next: |
  CALL c-arch-001
  to: session
  direction: indie-game-development
  play: research
  node: g-9c41
  goal: |
    The g-9c41 core architecture is decided at contract level, ready to feed the
    approach choice in c-shape-003. Five bound sub-questions, answered so they
    compose: (a) gas-field model — granularity ladder with configurable cell size
    (25/50cm working points, R2) and the role of a T1/T2-style hierarchy; (b) grid
    as integration fabric — what the grid owns; how mechanics communicate (owner's
    "each mechanic in its own layer, synced via the grid" hypothesis weighed as
    candidate #1 against >=2 alternatives on equal footing) + buy-vs-build sweep of
    existing solutions; (c) procgen ingestion — the adapter contract (what the core
    consumes), how DA/PGG geometry becomes sim topology, PGG day-one verdict (R3);
    (d) scale & network arithmetic — a huge procedurally generated level profile
    (R1): memory / tick cost / bandwidth on min-spec CPU and a listen-server
    uplink, dormancy of inactive regions, chunked-delta stream shape under the
    chosen model; (e) integration brief — 2-3 ranked whole-architecture candidates,
    recommendation, draft contracts, riskiest assumptions for the future bet.
  context: |
    live/indie-game-development/work/shape-g-9c41-approaches-2026-06-12.md (plain-
    language state of the shape: approaches A/B/C + hybrid, glossary, what is
    already locked);
    live/indie-game-development/history/s-shape-002.md (captures R1-R4 — the
    owner's standing requirements; this CALL's origin);
    live/indie-game-development/TREE.md (g-9c41 done_when 1-8; note: node wording
    "small representative scene" collides with R1 — rewording belongs to
    c-shape-003 under G9, not to this research);
    live/indie-game-development/history/s-map-002.md (P6/P7/P12 judge conditions;
    PGG asset link in captures); history/s-shape-001.md (appetite FIXED 6w to
    2026-07-24);
    archive evidence (read-only; import only with explicit reason per clean-start):
    old grid substrate, nucleus T1/T2 functional spec — T1+T2 worked single-player,
    evidence FOR feasibility; A1 audit (adapter boundary, no direct code transfer);
    multiplayer-readiness guardrail;
    precedent internals: SS14 atmos (open source), Stationeers, Noita Entangled
    Worlds, ONI; Unity DOTS/NfE docs; Dungeon Architect / PGG (beta) docs.
  boundaries: |
    P6 network MODEL is not re-litigated: host-authoritative sim, custom
    chunked-delta gas stream, ghosts only for players/objects, GPU never
    authoritative, rollback/lockstep at most a future timeboxed spike — this
    research shapes WHAT flows through that model. Informs, never decides:
    approach choice (A/B/C/hybrid) and any TREE/CHARTER wording stay with the
    owner in c-shape-003. No production code (throwaway arithmetic allowed).
    Appetite end 2026-07-24 is fixed — the hard stop below is real.
  done_when: |
    An architecture brief exists (returned via RESULT for work/) holding: the
    granularity ladder incl. configurable cell size; grid ownership +
    communication verdict (owner hypothesis vs alternatives, buy-vs-build sweep
    with sources); procgen-ingestion contract draft incl. PGG day-one verdict;
    scale/network arithmetic for the huge-level profile in numbers, not
    adjectives; 2-3 ranked whole-architecture candidates + recommendation + draft
    contracts + riskiest assumptions; established-vs-inference separated, sources
    dated; every archive import carries its explicit reason.
  return: |
    RESULT with the brief (file for work/ via state_changes) + key verdicts
    summarized; captures; log line; next = c-shape-003 (resume shape on g-9c41
    with the brief on the table).
  budget: 2-3 deep sessions (children allowed per play), hard stop 2026-06-15 EOD
  parent: s-shape-002
  surface: cli (Fable 5 window until 2026-06-22)

END_OF_FILE: live/indie-game-development/NOW.md
