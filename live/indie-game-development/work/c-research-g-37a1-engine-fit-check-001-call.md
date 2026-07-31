> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

CALL c-research-g-37a1-engine-fit-check-001
to: session
direction: indie-game-development
play: research
node: g-37a1
kind: bounded child question (KERNEL §2 `call:research`). NOT an executor CALL — READ-ONLY.
goal: |
  Answer, for each of the seventeen approved core requirements, exactly one of four verdicts:
  SATISFIED TODAY · NEEDS A FIX · NEEDS A REWRITE OF WHICH LAYER · IMPOSSIBLE IN CO-OP ON UNITY
  AND C#. This is the INPUT to the owner's decision ladder (`i-engine-fit-decision-ladder`) and
  nothing more. You do not run the ladder, you do not recommend a verdict on the engine's fate,
  and you do not decide anything.
context: |
  THIS IS STEP 4 OF A SIX-STEP ROUTE THE OWNER SET HIMSELF, recorded verbatim in
  `live/indie-game-development/NOW.md` `d-post-verify-route-001`. His own words about this
  step: it «may run in PARALLEL with steps 2-3 as soon as the requirement list exists, and it
  is the only place where time is genuinely saved». The requirement list now exists, so you
  start now. He restated the instruction on 2026-07-28: «мы должны прям сильно параллельно
  запускать, максимально, что можем».

  WHY THE ORDER MATTERS AND WHY YOU ARE LAST. The requirements were authored deliberately
  ENGINE-BLIND, on his instruction: «мы сейчас пишем требования, что должно быть без привязки к
  нашей технической реализации». You are the first leg permitted to look at the engine, and
  your job is to price the requirements, never to trim them. His standing rule, quoted so you
  do not soften a row: «если нам нужен какой-то прям хорошо видный жест, если его можно
  реализовать, но в нашей симуляции этого нет, то мы должны это реализовывать.» A requirement
  the engine cannot do today is a PRICE, not a defect in the requirement.

  READ, all paths absolute so this CALL is self-contained:
  - THE SUBJECT — the seventeen requirements:
    `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\core-requirements-g-37a1.md`
  - THE CARD they were written into (fifteen criteria, owner-approved on exact text):
    `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\TREE.md`, node `g-37a1`
  - THE RECEIPT, for what each line means and which of his words produced it:
    `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\history\2026-07-28-s-map-g-37a1-core-requirements-001.md`
  - THE LADDER you are feeding, including its two accepted-but-deferred objections:
    `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md`, `i-engine-fit-decision-ladder`
  - PRIOR FIRST-HAND ENGINEERING FINDINGS, to be re-verified rather than trusted:
    the same `NOW.md` (`i-flow-model-unmeasured`, `i-substance-laws-canon-candidate`) and
    `...\history\2026-07-27-s-converge-verify-g-37a1-digging-card-001.md` (V2, V3, V5, V6, V7).
  - THE PRODUCT, read-only: `C:\projects\Unity\GasCoopGame`. Read current `main`. RECORD the
    exact commit you read and cite file and line for every claim. Do NOT create a worktree, do
    NOT branch, do NOT edit, do NOT build, do NOT run Unity.

  THE LAYER DISTINCTION IS MANDATORY, and it is the objection the owner accepted. «Our gas
  simulation» is at least four separable layers: (a) the per-cell transport rule; (b) the
  determinism-and-replication contract that makes two machines agree; (c) the render contract;
  (d) the structure/topology layer. Layer (b) is CONCEPT-INDEPENDENT, is what makes co-op
  possible at all, is the most expensive thing already gate-proven, and would be needed by ANY
  simulation including a liquid. A verdict of «needs a rewrite» that does not name WHICH layer
  overshoots by weeks and is not an acceptable answer.

  THE TWO SORTS OF FACT MUST NEVER BE REPORTED AS ONE — his correction, and it is binding.
  Separate every finding into: TRUE OF THE SOLVER (concept-independent, not tunable) versus
  MERELY THE OLD CONCEPT'S PARAMETERS (inherited from a plan built for roughly 150 large rooms
  and never recomputed after the concept shrank twice — cell sizes, co-resident kind count,
  pocket and room sizes, occupancy, and the step rate, for which no constant exists in the
  product at all). Reporting a stale parameter as an engine limit is the exact error this leg
  exists to stop repeating.

  FOUR REQUIREMENTS ARE KNOWN IN ADVANCE TO BE THE EXPENSIVE ONES. Price them first and give
  them most of your budget: line 9 (behaviour at the moment of breach, and the fact that its
  concrete form must be a SETTING); line 11 (no sinks — substance leaving a pocket must end up
  in the workings); line 3 and line 7 together (a body that digs down and sideways and climbs
  out on steps it cut itself, which needs runtime mutation of solid-to-open); line 5 (every
  contested number reachable and changeable from a BUILT player, without the Editor).
boundaries: |
  READ-ONLY. Nothing in the product repository is written, built, branched or run. No worktree
  is created — reuse nothing, spawn nothing. No Unity Editor. No Steam state.

  You do not touch `live/**` in the direction repository — your output is a RESULT that comes
  HOME, and only Direction issues successor CALLs.

  YOU DO NOT DECIDE. Not the ladder, not whether a requirement should be cut, not whether the
  engine stays. If a requirement looks unaffordable, that is a PRICE with a number of days
  beside it and a named layer, and it goes to the owner. Do not recommend dropping a
  requirement; his rule is that a needed visible effect gets implemented, not dropped.

  Do not read `archive/**` or the frozen canon repository `C:\projects\gas_coop_game_canon`.

  IF A TOOL OR VENUE YOU NEED IS UNAVAILABLE — the repository is missing, a build is required to
  answer a row, Unity must be running — STOP and say so, and name what the owner would have to
  run. Do not write a substitute check, a scanner or any other workaround. That is a standing
  rule in this direction with no exception short of his written «да».
done_when: |
  1. Seventeen rows, one per requirement, each carrying: the verdict (satisfied / fix / rewrite
     of layer X / impossible in co-op on Unity and C#), the evidence with file and line at a
     named commit, and — for anything above «satisfied» — a size in days with what it depends on.
  2. Every «rewrite» verdict names WHICH of the four layers, and says explicitly whether layer
     (b), the determinism-and-replication contract, is or is not implicated.
  3. Every claim is split into TRUE-OF-THE-SOLVER versus OLD-CONCEPT-PARAMETER, and no stale
     parameter is presented as an engine limit.
  4. The four prior first-hand findings named above are RE-VERIFIED first-hand at your commit,
     not carried over. Any that no longer reproduce are reported as refuted, with the receipt.
  5. A single roll-up the owner can read in two minutes: how many rows are satisfied today, how
     many need a fix, which layers are implicated, the total in days with its spread, and the
     single most expensive row.
  6. A NAMED BUDGET is respected — see below. Anything not answerable inside it is marked
     UNKNOWN with the one thing that would settle it, rather than the budget being extended.
     The recorded symmetric risk is arriving in month three with neither a game nor an engine.
return: |
  One `research` RESULT that comes HOME to `indie-game-development` and feeds
  `i-engine-fit-decision-ladder`. It ends with the roll-up, not with a recommendation on the
  engine's fate.
budget: |
  ONE session, read-only. If the seventeen rows are not all answerable in it, answer the four
  expensive ones plus as many others as fit, and mark the rest UNKNOWN with what would settle
  each. Do not open a second session on your own authority — return and let the owner decide.
surface: a FRESH chat with read access to both repositories. No owner required.

after: |
  Step 5 — the owner's ladder verdict (`i-engine-fit-decision-ladder`): keep the engine, fix it,
  remove a named layer, cut requirements, or a different concept — which would be `frame`.
  Step 6 — `shape`. Steps 2 and 3 (converge and converge-verify over the same seventeen lines)
  run independently of you and neither waits for this.

END_OF_FILE: live/indie-game-development/work/c-research-g-37a1-engine-fit-check-001-call.md
