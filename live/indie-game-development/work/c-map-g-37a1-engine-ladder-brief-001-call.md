> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

CALL c-map-g-37a1-engine-ladder-brief-001
to: session
direction: indie-game-development
play: map
node: g-37a1
goal: |
  PREPARE AND PUT TO THE OWNER STEP 5 OF HIS OWN ROUTE — his ladder verdict on the completed engine
  check (`i-engine-fit-decision-ladder`). The engineering evidence is finished and priced; what is
  missing is HIS decision, and it is his alone. Bring him a readable Russian brief with real options
  and one recommendation, then STOP for his actual words.
context: |
  THE ROUTE. `NOW.md` `d-post-verify-route-001`: (1) minimal core — COMPLETE; (2) converge into rows
  — COMPLETE; (3) independent verification — the rows were verified twice and the owner then CUT the
  acceptance apparatus on 2026-07-28 (`d-core-acceptance-format-001`), leaving one short cut-check
  running in parallel; (4) the technical check — COMPLETE; (5) **THIS LEG — his ladder verdict**;
  (6) shape. **Step 5 is no longer gated on step 3**: he amended the sequencing himself when he cut
  the acceptance format and said to go to step 5 and then step 6.

  HIS LADDER, verbatim in `i-engine-fit-decision-ladder`, is the option set — do not invent another:
  (1) requirements first, engine-blind — done; (2) the engine fits, or needs fixing — fine; (3) it
  needs replacing entirely and the existing code actively gets in the way → a different concept is on
  the table, possibly a different game; (4) a requirement is impossible AT ALL in co-op on Unity/C#
  → the requirement is cut; (5) implementable but not with our gas simulation → the gas simulation
  comes out and we look again.

  READ:
  - `history/2026-07-28-s-research-g-37a1-engine-fit-check-001.md` — step 4's answer at product
    commit `1a6373b8`: 1 row satisfied today, 10 need fixes, 6 need a rewrite of the
    structure/topology layer (d) only, 0 impossible in co-op on Unity/C#; determinism-and-replication
    layer (b) is NOT a rewrite target and is the reusable co-op foundation; deduplicated price
    50–90 focused engineering days plus at least two owner-play calendar days; row 9 (breach
    behaviour) is the largest single row at 30–54 days.
  - `history/2026-07-28-s-research-g-37a1-engine-ecosystem-001.md` — no current engine migration has
    an evidenced time advantage; the recommended evidence path preserves the existing C# gas /
    determinism / FishNet layers and compares Digger PRO, Voxel Play 4 and a narrow Core-owned grid
    under one two-machine topology-gas-reset contract; Godot + Voxel Tools is the strongest
    open-source fallback and Unreal + Voxel Plugin the strongest commercial one, both with port tax.
  - `work/converge-g-37a1-core-rows.md` — the sixteen live rows as they stand after the cut.
  - `NOW.md` `i-engine-fit-decision-ladder` (its `review_when` carries the whole delta list),
    `i-card-clauses-unverifiable`, `i-core-acceptance-instrument-unpriced`.

  **WHAT THE 50–90 DAYS DOES NOT INCLUDE, and the brief must say so plainly** — four amendment items
  the owner added after step 4 measured (ROW 7 retired; death restarts the level IN FULL; a BASE that
  refills air; three in-game rig controls), plus the parameter home's refusal to write the
  level-authoring inputs, plus the SECOND authored level, plus the machine budget («не требует
  ядерного реактора»), which no row carries. Each is small in kind — a scene reload, a trigger
  volume, three switches, a second set of authored numbers — and none was priced.
boundaries: |
  **THIS IS AN OWNER-VERDICT LEG. You prepare and present; he decides.** Do not choose a branch, do
  not record a verdict he has not spoken, and do not derive one from anything he said before. If he
  does not answer, checkpoint and reissue — never infer.

  HOW THE BRIEF MUST READ, because the format has failed before:
  - **Russian, plain, full detail — do not compress.** He is an enterprise developer with no gamedev
    or Unity depth: explain in waves and analogies, not in play names, layer letters or OS jargon.
    Any term of art gets a one-line glossary entry the first time it appears.
  - **Numbers get their basis.** 50–90 days is a range for a reason; say what makes it 50 and what
    makes it 90, and say what is outside it (the seven unpriced items above).
  - **Every option carries what it costs, what it buys, and what it risks** — including branch 3,
    which collides with CHARTER's mission to finish THIS game and would be a `frame` decision, not
    this leg's.
  - **One recommendation, stated as a recommendation.** G7.
  - Text placed BEFORE an option-picker widget does not render for him: the brief must be complete
    in the message body itself.

  OUT OF SCOPE: no bet, no task, no track, no shape. Do not touch `TREE.md` or either card (G9). Do
  not reopen the sixteen requirement lines, the fifteen criteria or the acceptance format — the first
  are his approved text and the last is his decision of 2026-07-28. Do not re-run the engine check
  or read the product repository: step 4's receipt is first-hand and current at `1a6373b8`.
  Do not answer `d-air-counter-visibility-001`.
done_when: |
  1. The brief is delivered to him in full, with his five ladder branches as the options, the
     evidence behind each, the seven unpriced items named, and one recommendation.
  2. HIS WORDS are captured verbatim as the verdict, and the RESULT cites them.
  3. `i-engine-fit-decision-ladder` records the verdict and what it releases; if branch 3 fires it
     routes to `frame` and this leg does not act on it.
  4. On no answer: a checkpoint RESULT and a fresh continuation CALL for the same pending decision.
return: |
  One `map` RESULT carrying his verdict, then step 6 — `shape` — whose first task is the scene he
  asked for: a man digs a hole and walks into it. `shape` is the first leg that may open a bet, and
  it is the only place the PRE-BUILD stretch can be guarded, by `appetite` and `kill_by`.
budget: one session, OWNER PRESENT.
surface: a fresh chat.

END_OF_FILE: live/indie-game-development/work/c-map-g-37a1-engine-ladder-brief-001-call.md
