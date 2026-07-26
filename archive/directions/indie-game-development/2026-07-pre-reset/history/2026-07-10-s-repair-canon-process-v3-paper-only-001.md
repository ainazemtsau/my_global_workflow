RESULT s-repair-canon-process-v3-paper-only-001 (call: owner-message-2026-07-10-canon-process-v3-paper-only)
direction: indie-game-development   play: repair   node/task: g-d3a8/canon-process-v3-paper-only

outcome: |
  The process-v3 route is corrected to the owner's hard production boundary: all design variants
  are generated, filtered and compared only in text. There will be no playable prototype, Unity
  scene, greybox, visual probe, A/B build, implementation, setup, playtest, test, tuning or other
  separate work on variants.

  Owner chose exact option «А». Game-wide laws — game first, simple-not-primitive, real co-op,
  voluntary depth, serious horror and player-emergent comedy — are checked at game/core-loop
  altitude. A small mechanic receives only the criteria relevant to its actual design question;
  the process does not force every pillar into every micro-action.

  The paper-only process now determines variants through a visible funnel:
  - define one player decision and one common imagined scene;
  - privately generate a rough text pool from game-specific action/system/consequence levers;
  - kill ideas that are unclear, procedural, dominant, unreadable, mandatory-stuffy,
    forced-comic, anchor-destructive or dependent on a major new subsystem;
  - merge cosmetic/prose duplicates;
  - show the owner only 2–3 structurally different, equally rendered paper cards, or an honest
    BLOCKED outcome.

  Research RESULT s-research-canon-design-process-v3-001 remains immutable evidence, but its
  prototype/playtest/visual-evidence lanes are explicitly superseded for this direction. A
  paper-only pilot is ready. The repair does not answer core-0/core-1, freeze canon, install the
  process or rebuild the full question graph.

evidence: |
  - Owner hard correction: «Нет, такого не будет. Мы только текстом» and «никакой отдельной работы
    по настройке разных вариантов нельзя»; paper planning is allowed, mini-versions are not.
  - Owner priority: «в первую очередь это ИГРА, не симулятор», interesting in co-op and not stuffy;
    greater difficulty/depth should be chosen by hardcore players themselves; the ideal tone is
    eerie with funny moments created by players, without weakening the horror for a joke.
  - Owner identified the missing process mechanism: hundreds of mechanics exist, but the route did
    not explain how variants would be generated and rejected against these game-specific demands
    and current-engine feasibility.
  - Two-level correction was presented explicitly: A = game/core-loop laws plus relevant local
    filters; B = force every pillar into every mechanic. Owner verdict was exactly: «А».
  - Existing research history already diagnoses arbitrary/premature option generation and unequal
    comparison. This repair keeps that diagnosis and replaces all build-dependent evidence lanes
    with paper scenes, hard rejection rules and explicit uncertainty.
  - Current fixed foundations, DESIGN ANCHORS and core-0/core-1 HOLD status are preserved unchanged.

state_changes: |
  live/indie-game-development/NOW.md:
  - Header updated to s-repair-canon-process-v3-paper-only-001.
  - Removed returning open_call c-research-canon-design-process-v3-001 after consuming its RESULT.
  - Added open_call c-pilot-canon-design-process-v3-paper-001 with the hard text-only boundary and
    owner-verdict requirement.
  - Replaced only g-d3a8.state: prototype/playtest/visual lanes are superseded; owner choice «А» and
    the paper-only pilot route are now active.
  - Replaced only the canon-process NOW.next pointer with the new paper-only pilot CALL.
  - Preserved engine work, visual c-visual-009, c-shape-sc-damage-001, decisions, other tracks and
    all concurrent state unchanged.

  live/indie-game-development/work/:
  - Added canon-process-v3-paper-only-pilot-brief.md: the hard boundary, two-level criteria,
    variant-generation funnel, hard kills, engine-fit classes, equal paper-card format and pilot
    pass/fail rules.
  - Added c-pilot-canon-design-process-v3-paper-001-call.md as the self-contained next CALL.

  live/indie-game-development/LOG.md:
  - Appended the log line below before its END_OF_FILE trailer.

  live/indie-game-development/history/:
  - Added 2026-07-10-s-repair-canon-process-v3-paper-only-001.md containing this full RESULT.

  os/FRICTION.md:
  - Unchanged. This is a newly explicit direction constraint and one-off interpretation correction,
    not a repeated Direction-OS rule defect.

  Canon repository:
  - Unchanged. No game decision or process rule is frozen.

  TREE.md:
  - Unchanged.

  CHARTER.md:
  - Unchanged.

captures:
  - Whether an owner-approved paper decision may enter canon with an explicit “fun not verified”
    limitation is unresolved; the pilot must not invent that policy. Ask for a separate owner
    verdict after the process pilot.
  - Rough-pool size (pilot target about 10–15), card count (2–3) and local-filter count (3–6) are
    pilot parameters, not permanent process constants.
  - Paper analysis can reject bad fits and expose uncertainty, but cannot establish that a mechanic
    is fun. The process must carry that limitation rather than reopening implementation work.
  - Fear/greed, true co-op, horror and emergent comedy are global/core-loop obligations. A local
    question uses them only when it can materially affect them.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — the research recommendation allowed prototype/playtest/visual evidence, while the owner explicitly prohibits every separate built or tuned variant and permits text/paper only.
  - 2 Reconstruct: done — the owner needs a game-first selection funnel that explains where alternatives come from, why most are rejected, how engine fit is bounded, and how global principles avoid becoming a suffocating checklist on every micro-action.
  - 3 Propose corrected state: done — hard paper-only boundary; one shared imagined scene; internal text pool; hard kills; structural dedupe; 2–3 equal survivor cards; global laws at game/core-loop altitude plus local question filters.
  - 4 Confirm: done — owner hard boundary is cited verbatim and the exact architecture verdict is «А».
  - 5 Friction: skipped — this is a newly explicit direction constraint and a one-off process-interpretation correction, not evidence of a repeated OS-level rule defect.

log: |
  2026-07-10 — repair (g-d3a8/canon-process-v3, s-repair-canon-process-v3-paper-only-001): owner prohibited all playable/visual/implementation variant work and chose «А» — game-wide laws at game/core-loop altitude plus only relevant question-specific filters; superseded prototype-inclusive evidence lanes and opened one text-only selection-process pilot with internal generation, hard kills and 2–3 paper candidate cards. → history/2026-07-10-s-repair-canon-process-v3-paper-only-001.md

next: |
  CALL c-pilot-canon-design-process-v3-paper-001
  to: session
  direction: indie-game-development
  play: research
  node: g-d3a8
  parent: s-repair-canon-process-v3-paper-only-001
  surface: any

  goal: |
    One owner-evaluated paper-only pilot demonstrates whether the corrected design-selection process
    produces understandable, game-first and engine-feasible mechanic candidates without losing
    design anchors or forcing unrelated game-wide principles into every micro-decision.

  context: |
    Read NOW.md, work/canon-process-v3-paper-only-pilot-brief.md,
    history/2026-07-10-s-research-canon-design-process-v3-001.md and
    history/2026-07-10-s-repair-canon-process-v3-paper-only-001.md.

    Owner hard boundary: «Нет, такого не будет. Мы только текстом» and «никакой отдельной работы по
    настройке разных вариантов нельзя». Owner game-first requirement: «в первую очередь это ИГРА,
    не симулятор», interesting and unstuffy in co-op, with optional self-chosen depth for hardcore
    players, eerie atmosphere and player-created funny moments that do not weaken the horror.

    Owner chose «А»: apply global laws at game/core-loop altitude; use only relevant local criteria
    for each small mechanic. Fixed foundations and DESIGN ANCHORS keep their current status.
    core-0/core-1 are HOLD source material for the pilot, not active canon questions.

  boundaries: |
    Text only. No Unity scene, greybox, prototype, visual probe, A/B build, implementation, setup,
    playtest, test, tuning or separate variant work.
    Do not answer or freeze core-0/core-1, Bubble-first or an alternative concept.
    Do not edit canon, install the process or rebuild the full graph.
    Do not force every micro-mechanic to express every game-wide pillar.
    Do not claim that paper analysis proves fun.

  done_when: |
    The owner can explain where the variants came from and why the survivors were selected.
    The paper output contains 2–3 structurally different, equally rendered mechanic candidates or an
    honest BLOCKED outcome; separates global laws from question-specific filters; states engine fit,
    anchor treatment, base simplicity versus voluntary mastery, and the strongest boring/stuffy risk;
    and names exactly what remains unknown on paper.
    The owner gives an actual accepted/revised/rejected verdict on the process. A gameplay preference,
    if voiced, is captured only as pilot evidence and is not written to canon.

  return: |
    Short Russian paper pilot, owner-readable candidate cards, discarded-family kill reasons, the
    owner's process verdict, and a RESULT. No canon or process installation.

  budget: one owner-present session

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-repair-canon-process-v3-paper-only-001.md
