CALL c-work-grid-v1-critical-path-plan-002

to: session
direction: indie-game-development
track: grid
play: work
node: g-4b92
task: v1-critical-path-plan
issued: 2026-07-21 (s-work-grid-v1-critical-path-plan-scope-checkpoint-001)

goal: |
  У владельца есть один понятный, принятый и исполнимый Grid V1 master plan: Grid даёт общий
  пространственный/commit каркас и универсальные Object↔Layer и Layer↔Layer boundaries, а Gas,
  Water, Wind, Character, Loot и другие consumer behaviors остаются у своих треков и подключаются
  через явные handoffs.

context: |
  Это same-position продолжение `c-work-grid-v1-critical-path-plan-001` после двух correction rounds.
  Receipt: `history/2026-07-21-s-work-grid-v1-critical-path-plan-scope-checkpoint-001.md`.

  Принятая factual/priority основа остаётся `work/grid-current-authority-audit-2026-07-20.md` и
  owner route `A`; planning input — `work/grid-object-layer-interaction-resolver-brief.md`.
  Fresh product authority перед exact source disposition перечитать заново.

  Первая коррекция владельца: `сильно много информации, всё путано, очень сложно технически` и
  нужен план `очень-очень просто, без терминов, без кодов`. Вторая коррекция: `газ, про игрока это
  отдельные треки`, `Я не вижу то, что мы обсуждали вот в резолвер`, и Grid-план не должен звучать
  так, будто он реализует `симуляцию газа и Character`.

  Correct ownership boundary:
  - Grid owns shared stable spatial addressing/projection, committed revision/change transport and
    the generic Object↔Layer Resolver/index/subscription mechanism.
  - Every layer owns its data, simulation, typed read and behavior. Player/Loot/other objects own
    their identity, footprint and declared layer interests.
  - Object↔Layer Resolver finds only affected subscribed pairs and emits deterministic contact
    changes; it owns no layer physics or gameplay consequences.
  - Layer↔Layer interaction is a separate consumer-driven boundary: a layer may consume another
    layer's committed typed read/change information, but Grid does not calculate Gas↔Wind,
    Water↔Wind or any other behavior.
  - Gas/Water/Wind and Player/Loot are examples used to explain combinations, not implementations,
    stubs or Grid-owned adapters. Real adapters/proofs are handed to their owning tracks.
  - NearGas and Character may appear only in dependency/handoff/acceptance sections, never as Grid
    implementation legs. Exact aperture remains its own defect-line.

  Dashboard question remains secondary. The current Direction owner dashboard already has a Grid
  card and M3/M5 milestones; do not create or modify a dedicated Grid dashboard before the plan is
  accepted. The accepted plan should recommend whether one simple existing-dashboard section is
  enough or a separate render is justified.

boundaries: |
  PLAN discussion only. Do not change product code/tests/assets/scenes; do not run Unity/tests/build/
  Deliver; do not create product branches/worktrees or any BUILD CALL.

  Do not implement or design consumer behavior for Gas, Water, Wind, Character, Loot, damage, dose,
  balance, presentation, multiplayer session or Integration Lab. Do not create Water/Wind layers,
  fixtures, adapters, stubs or future-framework placeholders.

  Do not treat generic examples as current product authority. Do not merge Object↔Layer coordination
  with Layer↔Layer physics. Do not fold exact aperture into the Resolver. Do not create a dashboard
  before owner verdict.

done_when: |
  1. One owner-readable artifact `work/grid-v1-critical-path-plan.md` opens with a concrete plain-language
     picture of what Grid itself will provide; no ids, source paths or implementation jargon are needed
     to understand the main plan.
  2. A simple responsibility map distinguishes Grid, Layer, Object and Resolver, and explicitly says
     that Gas/Water/Wind/Character/Loot behavior remains outside Grid.
  3. The plan visibly includes both generic paths: Object↔Layer contact and consumer-driven Layer↔Layer
     interaction, using examples only to explain behavior and never as implementation scope.
  4. A plain matrix says `GRID BUILDS`, `OTHER TRACK HANDOFF`, `DEFERRED` and makes every NearGas/
     Character/Structure/Lab mention unambiguous. Any necessary exact legacy/source matrix lives in a
     subordinate executor appendix, not in the owner brief.
  5. Grid-owned work is split into dependency-ordered cohesive legs no larger than a focused half-day;
     real consumer adapters and gameplay proofs are separate named handoffs to their owning tracks.
  6. Synthetic layers may refute the generic Grid contract, but they are not Water/Wind stubs and do
     not claim real consumer completion. The acceptance chain says which downstream track-owned proofs
     must return before M3/M5/Lab may accept the Grid drop.
  7. The owner can see, without technical translation, what is sequential, what can be parallel after
     contract freeze, what blocks other tracks, the cuts/risks and the first planning-only handoff.
  8. The plan recommends either a small section in the existing owner dashboard or a separate Grid
     render, with maintenance cost explained; no dashboard is built before verdict.
  9. The owner receives the plan in conversation and accepts or corrects it in actual words. Without
     those words, keep the same planning position and do not open product execution.

return: |
  Один work RESULT: принятый или ожидающий verdict Grid V1 plan; owner words; простая ownership/scope
  matrix; Grid-owned legs; Object↔Layer и Layer↔Layer paths; consumer handoffs; sequence/parallel/blockers;
  cuts/risks; dashboard recommendation; один planning-only next или точный blocker. Отдельно перечислить
  всё, что не запускалось.

budget: one fresh owner-present planning session
surface: owner-present

END_OF_FILE: live/indie-game-development/work/c-work-grid-v1-critical-path-plan-002-call.md
