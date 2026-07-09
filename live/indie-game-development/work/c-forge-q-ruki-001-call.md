CALL c-forge-q-ruki-001
to: session
direction: indie-game-development
play: local/canon-forge (Кузница v2)
node: g-d3a8
cluster: q-ruki (+ q-prostranstvo as co-frame if capacity)

goal: |
  Owner has a clear, sparred answer (or an honest «обсуждается») to the FIRST map node: which 1–3 verbs are the
  player's hands on the gas world in the moment. The answer is a seconds-level working loop with players separated
  (МЕХАНИКА mode), passed through the mechanic lenses — not a slogan and not a tool.

context: |
  The session reads the canon repo itself per START.md — CONSTITUTION.md + INDEX.md + QUEUE.md + SESSION.md
  (github.com/ainazemtsau/gas_coop_game_canon, clone C:\projects\gas_coop_game_canon), base @b77571b.
  - CONSTITUTION.md is RATIFIED (owner verdict «Б», edits П1/П2/П3): fixed foundations = gas sim, reactions
    (material, not a required optimization — П1), destructible/changeable space; 7 pillars are the filter; NEGATIVE
    list is law («не предлагать снова»).
  - QUEUE.md is the owner-SIGNED map (verdict «А»). Node 1 = q-ruki, МЕХАНИКА mode. Node 2 = q-prostranstvo,
    co-frame, admissible only if the session has room (max 1–3 linked questions).
  - INDEX.md is still empty — there is no v2 canon card yet; this session may create the first.
  - Full-field map (dependency order, what each node does NOT solve, forge_handoff per node):
    OS-repo live/indie-game-development/work/canon-maps/core-concept-rebuild-question-map-v0.1.md.
  - Mechanic gate (BINDING): live/indie-game-development/knowledge/mechanic-lenses.md — MECHANIC cards run the six
    lenses in order; lens 6 (two-player greybox) is the only fun certificate; paper never certifies fun.
  - Material only (not decisions): canon repo sources/pitch-ono-dyshit-2026-07.md; the engine tie («что уже есть в
    движке» — cellular deterministic sim, mass-conserving layers, flow through openings, reactions with
    telegraph+wave, jets/wind/valves, breach) tells you which verbs the sim can already back (П3 test).
  - Candidate verbs for the SPAR (not a menu, not an answer): читать следы · направить поток · перекрыть/открыть ·
    пробить · поджечь/погасить · взять часть.

boundaries: |
  МЕХАНИКА mode: verbs table (глагол / объект / ввод / видимое следствие в секундах / сколько игроков) BEFORE
  candidates; answer = seconds-level loop with players separated, gated by the lenses. Do NOT decide: tools list,
  bubble mechanic (parked — it is a candidate ANSWER to «взять часть», not the question), roster, roles, economy,
  ЛЁГКИЕ, title. No engine beyond the existing sim + already-planned road (П3). Verdict = owner's verbatim words;
  no card without a filled `вердикт_владельца`. Side ideas → harvest (улов ≤5), never solved in-thread. Stop-words:
  «рамка» → back to SESSION.md step 0; «парковка» → branch to harvest. If node 1 hides a prerequisite / unclear
  plain question / wrong answer-shape, or owner says «не туда» → checkpoint a gap_event back to the map, do not
  invent canon.

done_when: |
  Session closed by a RESULT: a q-ruki card with the owner's verbatim verdict (or an honest «обсуждается» status),
  QUEUE.md/INDEX.md updated, harvest triaged by owner, mechanic-lenses verdict per lens recorded (lens 6 = greybox
  status honest), LOG line + history file. No paper sweep masquerades as a fun verdict.

return: |
  Russian readable summary (verbs table + chosen loop + honest minuses + what old material it touches), then RESULT.

budget: one session
