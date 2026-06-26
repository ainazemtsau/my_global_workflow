RESULT s-canon-015 (call: c-mechanic-expedition-002)
direction: indie-game-development   play: local/mechanic-forge   node/task: g-d3a8/q-expedition-loop

outcome: |
  `q-expedition-loop` checkpointed before playable-loop generation.

  The session did not freeze a mechanic card and did not define floor gameplay. The owner and session converged that the
  original question is still too low-level: before defining one expedition or one floor, the project needs a higher-level
  game-structure pass that separates:
  1. full-game descent arc / what it means to go to the end;
  2. between-expedition progression / what a completed or failed run changes;
  3. depth grammar / why deeper is qualitatively different and necessary;
  4. one expedition macrocycle / lift, floors, continuation or extraction;
  5. one floor loop / what happens after the lift doors open;
  6. concrete mechanics / verbs, gas tasks, co-op actions, seconds and consequences.

  The lift model remains a promising hypothesis, not frozen canon:
  - one floor is loaded at a time;
  - one expedition may include multiple floors;
  - the team can choose to go deeper or return to the surface between floors;
  - results are not truly saved until the lift returns to the surface;
  - the lift/equipment/floor details and all inside-floor actions remain unresolved.

  All prior concrete inside-floor proposals from this session — gas fronts, stabilizing a result, route-making verbs,
  working sectors, valves, breach/vent actions, etc. — are explicitly downgraded to placeholders / non-canon raw material.
  They must not be treated as accepted mechanics.

evidence: |
  Owner rejected the premature inside-floor assumptions:
  - "ты немного определил то, что будет сама экспедиция, то, что мы проходим, там, как газовый фронт движется,
    но это выглядит как твоё предположение"
  - "всё, что ты в принципе пишешь внутри уровня, это можно использовать только как заглушки"
  - "Многое, что ты написал, это будет точно не так"

  Owner identified the missing parent layer:
  - "глобальный цикл сначала надо проработать"
  - "зачем вообще идти до конца"
  - "зачем ниже спускается, какие сложности"
  - "тут даже не один, а несколько всё-таки есть более высокоуровневых вопросов"
  - "надо вообще пересмотреть само дерево"

  Session researched and proposed three compositions; owner chose option B:
  - B = checkpoint `q-expedition-loop`, then run a separate concept architecture session for concept spine + loop ladder
    and only then minimally alter the mechanics branch.
  - Owner approval: "B"

state_changes: |
  Apply the following OS-state changes only; do not edit the canon repo from this RESULT.

  1. `live/indie-game-development/LOG.md`: append:
     2026-06-26 — mechanic-forge checkpoint (g-d3a8/q-expedition-loop, s-canon-015): c-mechanic-expedition-002 stopped before worked-loop generation. Owner rejected premature inside-floor assumptions (gas fronts / stabilizing / route verbs are placeholders, not canon) and chose B: pause q-expedition-loop, run a separate concept-architecture pass first. Need concept spine + loop ladder + missing parent questions: full-game descent arc, between-expedition progression, depth grammar, expedition macrocycle, floor loop, concrete mechanics. Lift model remains a promising non-frozen hypothesis (one loaded floor at a time; one expedition may span multiple floors; surface return saves result). Canon repo untouched; NOW/TREE/CHARTER untouched.

  2. `live/indie-game-development/history/s-canon-015.md`: save this full RESULT as a new history file.

  3. `NOW.md` / `TREE.md` / `CHARTER.md`: untouched by this checkpoint.

  4. Direction `knowledge/`: untouched.

  5. Canon repo `gas_coop_game_canon`: untouched. No mechanic card frozen. No MOC update. No child question files written by this session.

captures:
  - `q-expedition-loop` should not be resumed until the project has a concept-architecture pass: concept spine + loop ladder + missing parent questions.
  - The likely missing parent questions are: `q-full-game-descent-arc`, `q-between-expeditions-progression`, `q-depth-grammar`, then revised `q-expedition-loop`, then `q-floor-loop`.
  - Lift-based expedition structure is a promising hypothesis only: one floor loaded at a time, multi-floor expedition possible, save on surface return, state carried between floors.
  - Inside-floor design from this session is non-canon raw material only; especially gas-front / stabilize-result / route-making details must not be inherited as accepted mechanics.
  - Future process guard: when a mechanic question lacks parent loops, stop at decomposition instead of filling the gap with plausible verbs.

decisions_needed: []

play_check:
  - 1. Frame the REAL question (plain words) + decompose (owner): DONE / CHECKPOINTED. Initial agreed frame from s-canon-014 was "what is an expedition from entry to exit"; this session refined it further after owner pushback. Owner said the real need is higher-level: "глобальный цикл сначала надо проработать", "зачем вообще идти до конца", and "надо вообще пересмотреть само дерево". Owner then chose "B" to checkpoint q-expedition-loop and run a separate concept-architecture pass.
  - 2. Verbs before names: SKIPPED / INTENTIONALLY REJECTED. Some verb-table-like material was drafted, but owner rejected it as premature: "всё, что ты в принципе пишешь внутри уровня, это можно использовать только как заглушки" and "Многое, что ты написал, это будет точно не так." Therefore no verb rows are accepted as canon.
  - 3. Develop a worked loop + spar: SKIPPED. No worked playable loop should be generated until missing parent questions are framed.
  - 4. Gate through mechanic lenses: SKIPPED. No candidate mechanic exists to gate; paper-gating placeholders would be false evidence.
  - 5. Freeze & grow (owner): SKIPPED. Owner did not sign a mechanic; owner signed the checkpoint route by choosing "B". No canon freeze, no rejected_alternatives tail, no MOC update.

log: |
  2026-06-26 — mechanic-forge checkpoint (g-d3a8/q-expedition-loop, s-canon-015): c-mechanic-expedition-002 stopped before worked-loop generation. Owner chose B: pause q-expedition-loop and run concept architecture first. Missing parent layer = full-game descent arc / between-expedition progression / depth grammar before expedition macrocycle and floor loop. Lift model remains non-frozen hypothesis; inside-floor proposals downgraded to placeholders. Canon repo untouched; NOW/TREE/CHARTER untouched.

next: |
  CALL c-concept-architecture-001
  to: session
  direction: indie-game-development
  play: research
  node: g-d3a8
  question: concept-spine-loop-ladder
  parent: s-canon-015
  surface: any / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    The project has a clear concept-architecture map for the game-design/canon branch: a one-page concept spine, a loop
    ladder from full-game arc down to concrete mechanics, and a minimal list of missing parent questions that must exist
    before `q-expedition-loop` can be resumed.

  context: |
    Direction OS repo:
    - `live/indie-game-development/NOW.md`
    - `live/indie-game-development/TREE.md`
    - `live/indie-game-development/history/s-canon-014.md`
    - `live/indie-game-development/history/s-canon-015.md`
    - `live/indie-game-development/plays/mechanic-forge.md`
    - `live/indie-game-development/knowledge/mechanic-lenses.md`
    - `live/indie-game-development/work/research-expedition-loop-foundation-2026-06-19.md`

    Canon repo:
    - `C:\projects\gas_coop_game_canon`
    - `questions/q-north-star.md`
    - `questions/q-gas-role.md`
    - `questions/q-the-city.md`
    - `questions/q-coop-shape.md`
    - `questions/q-base-logistics-labs-factories.md`
    - any current mechanic/world MOCs if present.

    Trigger:
    - During `c-mechanic-expedition-002`, the owner found that `q-expedition-loop` cannot be answered cleanly because
      higher-level game-structure questions are missing.
    - Owner explicitly chose option B: checkpoint `q-expedition-loop` and run a separate concept-architecture pass first.
    - Treat all detailed inside-floor mechanics proposed in that session as placeholders, not accepted canon.

    Current non-frozen hypothesis to preserve as raw material:
    - Lift is likely the physical entry/exit/transition spine.
    - One floor may be loaded at a time.
    - One expedition may span multiple floors.
    - Result may be saved only on surface return.
    - State may carry between floors: loot, tools, damage, contamination, or other risk — exact categories unresolved.

  boundaries: |
    Do not freeze canon cards.
    Do not define exact floor gameplay, gas reactions, co-op actions, economy numbers, UI, balance, or implementation architecture.
    Do not rewrite the whole world/lore graph unless there is a specific conflict; the likely change is local to the
    game-structure / mechanics branch under g-d3a8.
    Do not treat lift details or inside-floor placeholders from s-canon-015 as accepted mechanics.
    Output should be a concept architecture and question graph proposal, not a full GDD.

  done_when: |
    A research/result artifact or RESULT section contains:
    1. a compact concept spine synthesized from frozen canon;
    2. a loop ladder from full-game arc → between-expedition progression → depth grammar → expedition macrocycle →
       floor loop → concrete mechanics;
    3. for each ladder level: the core question, why it must precede lower levels, what it decides, and what it must not decide;
    4. a minimal proposed canon-question diff: which questions to add, rename, defer, or resume;
    5. a recommended first next question to forge after this architecture pass;
    6. explicit handling of `q-expedition-loop`: whether it remains, is renamed, or is split.

  return: |
    RESULT with the concept-architecture summary, proposed question graph diff, captures/decisions_needed, exact
    state_changes, and a ready next CALL for the first selected question. No canon repo edits unless a later owner-signed
    planning session approves them.

  budget: one session

END_OF_FILE: live/indie-game-development/history/s-canon-015.md
