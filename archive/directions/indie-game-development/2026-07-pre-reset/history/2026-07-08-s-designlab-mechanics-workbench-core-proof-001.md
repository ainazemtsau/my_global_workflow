RESULT s-designlab-mechanics-workbench-core-proof-001
direction: indie-game-development
play: local/design-lab
node/task: g-d3a8/mechanics-workbench-core-proof
date: 2026-07-08
status: CHECKPOINT_DRAFTS

owner_summary: |
  Подготовлена не-каноничная рабочая зона `mechanics-workbench`, чтобы начать нормальную проработку минимальной игры.

  Что сделано:
    - создана карта областей и blocker graph;
    - создан ledger идей, где `Пузырь` лежит как текущий candidate proof, а `ЛЁГКИЕ` сохранены как later meta и не потеряны;
    - создан исправленный skeleton минимального proof без мутных терминов вроде "газовый карман" и "запузырить";
    - reactions/release явно внесены в минимальный proof как обязательный вопрос;
    - создан review guide: с чего владельцу начинать и как не утонуть в тексте.

  Canon не заморожен. `NOW.md`, `TREE.md`, `CHARTER.md` не менялись.

outcome: |
  Created a non-canon Mechanics Workbench packet for owner review:
    - `work/mechanics-workbench/mechanics-workbench-v0.md`
    - `work/mechanics-workbench/area-map-v0.md`
    - `work/mechanics-workbench/idea-ledger-v0.md`
    - `work/mechanics-workbench/core-proof-skeleton-v0.1.md`
    - `work/mechanics-workbench/review-guide-v0.md`

  The packet reframes the next discussion around one minimal playable proof skeleton, not around choosing two concepts.

  Current recommended owner review start:
    read `core-proof-skeleton-v0.1.md`, sections 2, 3 and 7.

  Current first discussion question:
    Is the promise "gas -> visible bubble -> carry -> rupture returns gas to world" acceptable as a temporary skeleton,
    if the exact transfer-to-bubble action is explicitly TBD?

evidence: |
  Local sources read/used:
    - `history/s-repair-ono-dyshit-routing-001.md`
    - `history/s-cartography-ono-dyshit-core-frame-001.md`
    - `history/s-canon-gas-interaction-playable-anchors-001.md`
    - `work/design-labs/minimal-game-discussion-graph-001.md`
    - `work/design-labs/ono-dyshit-bubble-proof-repair-001.md`
    - `work/concept-pitch-2026-07-07.md`
    - `work/concept-hooks-research-2026-07-07.md`
    - `work/design-labs/gas-interaction-gameplay-001.md`
    - `work/canon-maps/gas-interaction-map.md`
    - `knowledge/mechanic-lenses.md`
    - attachment `C:\Users\Anton\.codex\attachments\976317cc-a1f0-47f9-8850-cde0245764ce\pasted-text.txt`
    - `NOW.md`
    - `work/c-exec-034-sc-catalog-call.md`

  External process research used lightly:
    - GitBook GDD guidance: living, searchable, broad-to-specific docs.
    - MDA paper: mechanics create dynamics which create player experience.
    - Design Council Double Diamond: diverge/converge, test at small scale.

  Note:
    The requested canon repo files `questions/...` / `maps/World.md` were not found in this workspace through `rg --files`,
    so this packet does not claim first-hand direct reads of those canon repo files.

captures:
  - id: unclear-terms-banned
    text: |
      `газовый карман`, `запузырить`, `мембранное кольцо`, магический `спящий газ` и субъектность газа явно запрещены
      как готовые термины. Если они нужны, их надо определять через отдельные blockers.

  - id: lungs-preserved
    text: |
      `ЛЁГКИЕ` is preserved as a strong meta-loop candidate in the ledger and area map. It is parked until floor value,
      custody and replay pull exist at least on paper.

  - id: bubble-current-skeleton
    text: |
      `Пузырь` is the current candidate for first proof discussion, but not canon. The transfer action, carrying model,
      damage/leak rules and reactions are all explicitly unresolved.

  - id: reactions-not-forgotten
    text: |
      Bubble failure must discuss released gas, external gas, and reactions. Failure is a world-state change, not a score
      penalty.

  - id: old-canon-salvage-only
    text: |
      Old canon/design material can be salvaged only when it answers the current blocker. It is not authority for the new
      concept pass.

decisions_needed:
  - id: d-core-proof-skeleton-review-001
    q: |
      Is the `core-proof-skeleton-v0.1.md` promise acceptable as the temporary skeleton for discussion?
    options:
      - accept_as_skeleton: |
          Continue with blockers B1-B3: what gas is spatially, what players read, and what transfer-to-bubble means.
      - revise_skeleton: |
          Rewrite the minimal promise before discussing carry, reactions, co-op, meta or canon.
      - reject_bubble_currently: |
          Move Bubble back to parked idea and choose a different single minimal proof skeleton; do not build two branches.
    recommendation: |
      Start by reviewing the skeleton, not the whole packet. If acceptable, discuss B1 first.

state_changes:
  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/mechanics-workbench-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/area-map-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/idea-ledger-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/review-guide-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/history/2026-07-08-s-designlab-mechanics-workbench-core-proof-001.md
    content_source: this_full_RESULT_block

  - repo: ainazemtsau/my_global_workflow
    action: append_line
    path: live/indie-game-development/LOG.md
    content: |-
      2026-07-08 — design-lab/checkpoint drafts (g-d3a8/mechanics-workbench-core-proof, s-designlab-mechanics-workbench-core-proof-001): created non-canon Mechanics Workbench packet for the reset minimal-game discussion: area map + blocker graph, idea ledger preserving `Пузырь` as current proof candidate and `ЛЁГКИЕ` as parked meta, corrected core-proof skeleton with undefined terms banned (`газовый карман`, `запузырить`, exact membrane), reactions/release explicitly included, and owner review guide. No canon freeze; NOW/TREE/CHARTER untouched. → work/mechanics-workbench/mechanics-workbench-v0.md

  - repo: ainazemtsau/my_global_workflow
    action: do_not_edit
    paths:
      - live/indie-game-development/NOW.md
      - live/indie-game-development/TREE.md
      - live/indie-game-development/CHARTER.md

play_check:
  - step: "Frame"
    status: done
    evidence: |
      Workbench states the process and boundaries: minimal game first, ideas parked, no canon freeze.

  - step: "Inventory"
    status: done
    evidence: |
      Sources and current engine/design status gathered; untracked `c-exec-035-sc-sense-call.md` observed but not staged or treated as authority.

  - step: "Draft"
    status: done
    evidence: |
      Five owner-readable work files created.

  - step: "Gate"
    status: done
    evidence: |
      Undefined terms are flagged/banned; `ЛЁГКИЕ` parked; reactions included; title boundary preserved.

next: |
  Owner review should begin with:
    `live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md`

  First question:
    accept / revise / reject the skeleton promise before discussing exact carry, reactions, `ЛЁГКИЕ`, economy, canon or title.

log_summary: |
  Mechanics Workbench draft packet created; no canon freeze; ready for owner review of the core proof skeleton.

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-designlab-mechanics-workbench-core-proof-001.md
