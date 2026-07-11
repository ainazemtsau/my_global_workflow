CALL c-repair-gate-q-investigation-readiness-001
to: session
direction: indie-game-development
play: repair
node: g-d3a8
parent: s-repair-minimum-game-frame-001
surface: any

goal: |
  Gate Q returns the owner's verbatim QUESTION READY or QUESTION BLOCKED verdict
  for the first detailed design question derived from the FRAME READY Minimum Game
  Frame, without answering that question.

context: |
  Read:
  - live/indie-game-development/NOW.md
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/work/minimum-game-frame-v1.md
  - live/indie-game-development/work/canon-process-v3-paper-only-pilot-brief.md
  - live/indie-game-development/history/2026-07-11-s-repair-minimum-game-frame-001.md
  - live/indie-game-development/knowledge/mechanic-lenses.md

  Gate F is closed under the owner's exact verdict:
  "FRAME READY"

  Accepted whole-game spine:
  investigation of nearly invisible gas
  → plan
  → extraction/mining/operation
  → evacuation/return through a potentially changed environment.

  The recommended first question is q-investigation-readiness.

  Frame location:
  the transition from investigation/planning into extraction/mining/operation.

  Immediate upstream:
  the crew has entered, gathered incomplete information and formed some model of
  the nearly invisible gas and intended route.

  Immediate downstream:
  the crew commits actions that may extract value, activate gas and change the
  evacuation situation.

  Exact unresolved player decision:
  "В этой ситуации игроки должны решить, достаточно ли они поняли почти невидимый
  газ и путь, чтобы начинать добычу/операцию сейчас, или продолжить расследование
  либо отступить."

  Source:
  - the owner-approved three-phase frame;
  - the owner-approved high-level principle that gas is initially nearly or
    completely invisible and detection is a separate mechanic;
  - the owner-approved high-level principle that careless action may activate it
    before investigation is complete;
  - the explicit decision to defer exact detection and operation details to
    separate analysis.

  Why current:
  this is the first unresolved joint between two accepted phases.

  What it blocks:
  - a trustworthy statement of what investigation must output;
  - later detection-mechanic requirements;
  - the contents of a usable operation/evacuation plan;
  - the legitimate entry point for detailed phase-two design.

  Independent blockers:
  - exact extraction/mining mechanic;
  - Bubble's role;
  - gas-state and activation semantics;
  - exact co-op roles and anti-solo proof;
  - damage/consequences;
  - UI/instruments;
  - implementation and empirical evidence.

boundaries: |
  Text only.

  Do not answer q-investigation-readiness.
  Do not generate local criteria, a shared scene or candidate mechanics before
  the owner returns QUESTION READY.
  Do not design detection instruments, evidence types, gas states, Bubble,
  extraction, damage, UI, economy, controls or implementation.
  Do not freeze or amend canon.
  Do not install the canon/design process.
  Do not rebuild the question graph.
  Do not claim fun, actual co-op, runtime legibility or engine cost.
  Do not silently substitute another question if this one is blocked.

  Preserve the current active bet, tasks, unrelated open calls, decisions and
  global NOW.next exactly as read at session start.

done_when: |
  One owner-readable Gate-Q brief establishes all six facts:

  1. exact game/frame location, including upstream and downstream play;
  2. the exact unresolved player decision;
  3. traceable source of the question;
  4. why it is current, what it blocks and every independent blocker;
  5. provenance and meaning of every introduced entity;
  6. explicit non-scope.

  The owner returns one verbatim verdict:
  - QUESTION READY;
  - QUESTION BLOCKED.

  On QUESTION READY:
  the question may be routed to a later, separate design session, but is not
  answered in this session and no candidates are generated here.

  On QUESTION BLOCKED:
  the same question and missing basis remain open; no substitute is selected.

  NOW consumes this call and registers only the continuation implied by the
  owner's verdict. Current engineering/visual state remains unchanged.

return: |
  Russian owner-readable Gate-Q brief, source/provenance table, exact question,
  blockers and non-scope, the owner's verbatim verdict, exact state diff and one
  RESULT.

budget: one owner-present session

END_OF_FILE: live/indie-game-development/work/c-repair-gate-q-investigation-readiness-001-call.md
