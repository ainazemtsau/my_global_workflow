# RESULT — s-shape-002 (shape, 2026-06-12) — checkpoint

```yaml
RESULT s-shape-002 (call: c-shape-002) — checkpoint
direction: indie-game-development   play: shape   node/task: g-9c41
outcome: |
  Shape paused at step 3 (approach choice) by design. The owner reviewed the full
  plain-language approach brief (A / B / C + sharpened A+C hybrid) and surfaced two
  findings: (1) the core's field/grid architecture is genuinely undecided — the
  tabled approaches embed an untested granularity assumption; (2) four standing
  owner requirements existed only in his head / read-only archive, not in live
  state (R1-R4 in captures). Per the shape play note ("stalls on an unknown →
  spawn call:research, do not pad the bet with guesses") the approach choice is
  deferred to c-shape-003 and a comprehensive architecture research c-arch-001 is
  queued with an owner-approved program: (a) gas-field model / granularity ladder,
  (b) grid as integration fabric, (c) procgen ingestion contract (DA/PGG),
  (d) scale & network arithmetic for a huge-level profile, (e) integration brief
  with 2-3 ranked candidates + draft contracts. Appetite stays FIXED 6w /
  2026-07-24 (G3) — research burns 2-3 days of build runway, cost acknowledged by
  owner. The incubation boundary dissolved by construction (choice now happens
  >=1 night after s-shape-001). Maintenance request draft prepared (standing
  requirements have no home in state) for the owner to launch separately.
evidence: |
  Owner decisions in-session (his words): research need — «я как бы сейчас вижу,
  что нам стоит прям реально запустить ресёрч вот на эту архитектуру», scope —
  «надо на всё, что в коре, и достаточно глубоко ещё, чтобы это вместе как бы
  работало», not in-session — «естественно, сейчас ресёрч запускать не надо…
  будем его запускать отдельно»; approval of the 5-block program + maintenance
  draft (two-question close): «на все до» [= да на всё].
  Requirements in owner's words: «какая нахер мне одна комната, это не доказывает
  всю симуляцию… симуляция должна работать на огроменном уровне» (R1); «в идеале
  так, чтобы мы могли менять, насколько клетку делать газа, 25 или 50» (R2);
  «я как бы хотел бы, чтобы сразу Dungeon Architect использовался… PGG…
  возможно, чтобы сразу её тоже прикрутить» (R3); «она может пережить концепт
  игры» (R4). Pre-mortem #3 framing corrected in-session: hypothetical tripwire,
  not a verdict; old-project T1+T2 working single-player recorded as evidence FOR
  feasibility (archive import with reason, into research context).
  Artifacts: work/shape-g-9c41-approaches-2026-06-12.md (full plain-language
  brief, created mid-session on owner instruction «объясни здесь или создай
  файл»); work/maintenance-request-2026-06-12-standing-requirements.md
  (paste-ready draft). No approach chosen, no bet, no tasks — G1/G9 untouched.
state_changes: |
  live/indie-game-development/NOW.md: next replaced with CALL c-arch-001
  (research; full text in NOW.md). Everything else unchanged (active_bet none,
  open_calls keeps c-frame-002, decision_inbox empty).
  live/indie-game-development/work/: + shape-g-9c41-approaches-2026-06-12.md,
  + maintenance-request-2026-06-12-standing-requirements.md.
  live/indie-game-development/LOG.md: append checkpoint line → history/s-shape-002.md.
  live/indie-game-development/history/: + s-shape-002.md (this RESULT).
  No TREE.md / CHARTER.md changes (R1 vs node wording "small representative
  scene" — rewording deferred to c-shape-003 under G9 with research evidence).
captures:
  - "R1 (owner requirement): sim+grid designed for a huge procedurally generated level; scale proof must enter the core's evidence base — collides with node g-9c41 wording 'small representative scene'; rewording decision at c-shape-003 (G9) after research"
  - "R2 (owner requirement): gas cell size is a config parameter, 25/50 cm working points"
  - "R3 (owner requirement): Dungeon Architect from day one; PGG evaluated for day-one wiring (asset link already in s-map-002 captures)"
  - "R4 (owner requirement): the simulation is an asset that may outlive the game concept → product-grade contracts/API (matches s-map-002 fallback-value capture)"
  - "approaches A/B/C + hybrid stay tabled for c-shape-003 (full brief: work/shape-g-9c41-approaches-2026-06-12.md); the preliminary A+C recommendation is superseded by the pending architecture brief"
  - "maintenance candidate (drafted, owner decides when to launch): standing owner technical requirements have no home in state — work/maintenance-request-2026-06-12-standing-requirements.md"
  - "owner communication rule observed twice this session: decision briefs must be full-detail, simple language, previews marked as previews; compressed briefs caused both misunderstandings"
decisions_needed: []
play_check:
  - "1 recite: done (s-shape-001, carried)"
  - "2 appetite (owner): done (s-shape-001: «6 недель, до 24.07» — fixed, untouched here)"
  - "3 approaches + pick (owner): paused — full plain-language brief delivered (work/shape-g-9c41-approaches-2026-06-12.md); owner raised undecided field/grid architecture + R1-R4; pick deferred per play note 'stalls on an unknown → spawn call:research, do not pad the bet with guesses'; owner: «нам стоит прям реально запустить ресёрч вот на эту архитектуру», program+close approval: «на все до»"
  - "4 scope hammer: deferred to c-shape-003 (awaits architecture brief)"
  - "5 lens sweep: deferred to c-shape-003"
  - "6 riskiest assumption: deferred to c-shape-003 (brief will re-rank; net-consistency candidate stands)"
  - "7 tasks: deferred to c-shape-003"
  - "8 kill criteria: deferred to c-shape-003 (date anchor 2026-07-24 fixed)"
  - "9 close: this checkpoint RESULT (play note: checkpoint close is a valid result); no bet in NOW — G1/G9 untouched"
log: "2026-06-12 — shape (checkpoint №2): approach choice paused — owner surfaced undecided field/grid architecture + standing requirements R1-R4 (huge-level scale proof, configurable cell 25/50cm, DA day-one + PGG eval, sim outlives concept); research queued per play note: next = c-arch-001 (core architecture at contract level, hard stop 2026-06-15); approaches stay tabled for c-shape-003; maintenance draft prepared (standing-requirements home). → history/s-shape-002.md"
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
```

END_OF_FILE: live/indie-game-development/history/s-shape-002.md
