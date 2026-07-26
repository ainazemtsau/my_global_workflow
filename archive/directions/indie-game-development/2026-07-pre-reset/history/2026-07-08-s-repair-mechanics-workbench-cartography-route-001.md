RESULT s-repair-mechanics-workbench-cartography-route-001 (call: owner-mechanics-workbench-route-question)
direction: indie-game-development   play: repair   node/task: g-d3a8/mechanics-workbench-cartography-route

outcome: |
  Mechanics Workbench route is repaired back to the established map-first process.

  What is now true:
  - active g-d3a8 next step is `c-cartography-mechanics-workbench-questions-001`, not the ad-hoc Q1 Design Lab;
  - `c-designlab-gas-spatial-form-001` is preserved only as a candidate first question until cartography owner-signs the map;
  - `mechanics-workbench-question-map-seed-v0.md` preserves the current idea inventory and blocker graph for the cartography session;
  - `Пузырь`, `ЛЁГКИЕ`, quiet/sleep floor, detection, transfer, carry/co-op, rupture/release, reactions, old canon salvage and title boundary are all explicitly accounted for;
  - no canon card, mechanic card, TREE or CHARTER change is frozen.

evidence: |
  Read and reconciled:
  - `live/indie-game-development/NOW.md`
  - `live/indie-game-development/TREE.md`
  - `live/indie-game-development/LOG.md`
  - `live/indie-game-development/plays/canon-cartography.md`
  - `live/indie-game-development/plays/design-lab.md`
  - `live/indie-game-development/plays/mechanic-forge.md`
  - `live/indie-game-development/work/c-cartography-ono-dyshit-core-frame-001-call.md`
  - `live/indie-game-development/work/mechanics-workbench/*`
  - owner attachment `pasted-text.txt` for the `ЛЁГКИЕ` meta idea

  Contradiction found:
  - previous repair registered `c-designlab-gas-spatial-form-001` as active next;
  - owner correctly objected that the normal process needs maps/route first, with one-question sessions selected through that map.

  New artifacts:
  - `live/indie-game-development/work/canon-maps/mechanics-workbench-question-map-seed-v0.md`
  - `live/indie-game-development/work/c-cartography-mechanics-workbench-questions-001-call.md`

state_changes: |
  1. Add `live/indie-game-development/work/canon-maps/mechanics-workbench-question-map-seed-v0.md`.
     Content: cartography seed, not canon; migration inventory for `Пузырь`, `ЛЁГКИЕ`, required blockers, preserved seeds and banned ready terms; proposed M0→Q8 graph; candidate nodes with `plain_question`, `why_it_matters`, `answer_shape`, `status`, `dependency_type`, `blocks`, `do_not_solve_here`, `needs_anchor`, `confusion_traps`, `forge_handoff`; later parked nodes for `ЛЁГКИЕ`, gas roster/jobs and title.

  2. Add `live/indie-game-development/work/c-cartography-mechanics-workbench-questions-001-call.md`.
     CALL id: `c-cartography-mechanics-workbench-questions-001`.
     play: `local/canon-cartography`.
     goal: an owner-approved Mechanics Workbench question map exists for the current Bubble / floor-proof / meta material, with every idea placed, parked or rejected and the next one-question CALL selected.

  3. Update `live/indie-game-development/NOW.md`:
     - `updated:` becomes `2026-07-08 by s-repair-mechanics-workbench-cartography-route-001`.
     - Replace open_call `c-designlab-gas-spatial-form-001` with open_call `c-cartography-mechanics-workbench-questions-001`.
     - g-d3a8 parallel-track state says current open design CALL is cartography; `c-designlab-gas-spatial-form-001` is candidate Q1 only until owner-signed map.
     - `next` tail says g-d3a8 Mechanics Workbench cartography is ready as `c-cartography-mechanics-workbench-questions-001`.

  4. Append to `live/indie-game-development/LOG.md`:
     `2026-07-08 — repair/cartography route (g-d3a8/mechanics-workbench-cartography-route, s-repair-mechanics-workbench-cartography-route-001): replaced the ad-hoc Q1 Design Lab next with a formal Mechanics Workbench cartography route. Added seed question map preserving Bubble, `ЛЁГКИЕ`, quiet/detection/reactions/carry/co-op/old canon/title ideas; registered c-cartography-mechanics-workbench-questions-001 in NOW; Q1 spatial-form Design Lab remains candidate, not active, until map owner-sign. TREE/CHARTER untouched; no canon freeze. → work/canon-maps/mechanics-workbench-question-map-seed-v0.md`

  5. Add this RESULT file as `live/indie-game-development/history/2026-07-08-s-repair-mechanics-workbench-cartography-route-001.md`.

captures:
  - `c-designlab-gas-spatial-form-001` is preserved as useful candidate Q1, not deleted; cartography may accept, split or replace it.
  - `ЛЁГКИЕ` is parked as meta/base/economy material until bare floor value, custody and one-more pull are proven.
  - Existing uncommitted Sc-sense files in the worktree are unrelated to this repair and must not be interpreted as g-d3a8 state authority.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — active `NOW.open_calls` jumped straight to Q1 Design Lab while the owner requested a map-first normal process.
  - 2 Reconstruct: done — read current NOW/TREE/LOG, local plays, prior cartography/design-lab artifacts, Workbench drafts and the `ЛЁГКИЕ` attachment; found draft material existed but formal Workbench cartography was missing.
  - 3 Propose corrected state: done — created a seed question map plus `c-cartography-mechanics-workbench-questions-001`; Q1 Design Lab is downgraded to candidate until map sign.
  - 4 Confirm: done — owner requested the transition in this session: "либо можешь составить next call ... либо тут можешь какой-то начальный шаг создать ... чтобы структура вся создалась ... чтобы реально не потерялось".
  - 5 Friction: skipped — no OS rule change is needed here; this was a local route drift repaired through existing `repair` + `canon-cartography` process. If the same g-d3a8 route skips cartography again, open maintenance/friction instead of another silent fix.

log: 2026-07-08 — repair/cartography route (g-d3a8/mechanics-workbench-cartography-route, s-repair-mechanics-workbench-cartography-route-001): replaced the ad-hoc Q1 Design Lab next with a formal Mechanics Workbench cartography route. Added seed question map preserving Bubble, `ЛЁГКИЕ`, quiet/detection/reactions/carry/co-op/old canon/title ideas; registered c-cartography-mechanics-workbench-questions-001 in NOW; Q1 spatial-form Design Lab remains candidate, not active, until map owner-sign. TREE/CHARTER untouched; no canon freeze. → work/canon-maps/mechanics-workbench-question-map-seed-v0.md

next: |
  CALL c-cartography-mechanics-workbench-questions-001
  to: session
  direction: indie-game-development
  play: local/canon-cartography
  node: g-d3a8
  parent: s-repair-mechanics-workbench-cartography-route-001
  surface: chat / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    An owner-approved Mechanics Workbench question map exists for the current Bubble / floor-proof / meta material, with every idea placed, parked or rejected and the next one-question CALL selected.

  context: |
    Read:
    - live/indie-game-development/work/canon-maps/mechanics-workbench-question-map-seed-v0.md
    - live/indie-game-development/work/mechanics-workbench/mechanics-workbench-v0.md
    - live/indie-game-development/work/mechanics-workbench/chat-first-process-v0.md
    - live/indie-game-development/work/mechanics-workbench/route-to-forge-v0.md
    - live/indie-game-development/work/mechanics-workbench/question-queue-v0.md
    - live/indie-game-development/work/mechanics-workbench/idea-ledger-v0.md
    - live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md
    - live/indie-game-development/work/design-labs/minimal-game-discussion-graph-001.md
    - live/indie-game-development/work/design-labs/ono-dyshit-bubble-proof-repair-001.md
    - live/indie-game-development/work/design-labs/ono-dyshit-bubble-variant-001.md
    - live/indie-game-development/work/concept-pitch-2026-07-07.md
    - live/indie-game-development/work/concept-hooks-research-2026-07-07.md
    - live/indie-game-development/work/design-labs/gas-interaction-gameplay-001.md
    - live/indie-game-development/work/canon-maps/gas-interaction-map.md
    - live/indie-game-development/knowledge/mechanic-lenses.md
    - live/indie-game-development/plays/design-lab.md
    - live/indie-game-development/plays/mechanic-forge.md
    - live/indie-game-development/plays/canon-forge.md

    Owner correction:
    - Work must return to the established workflow, not an invented draft process.
    - Maps are needed before choosing the next one-question session.
    - The owner must not hunt through files; the session presents the map in chat.
    - Nothing from drafts should be lost. Every idea must be placed in the map, parked, or explicitly rejected with reason.

    Current route hypothesis to verify, not assume:
    - Design Lab clears unclear blockers.
    - Mechanic Forge later freezes a worked playable mechanic loop.
    - Canon Forge later freezes compact canon only when freeze-ready.

  boundaries: |
    Do not freeze canon.
    Do not answer the gameplay questions yet.
    Do not start Q1 Design Lab inside this cartography session.
    Do not solve exact gas spatial form, transfer action, bubble carry, rupture/reactions, `ЛЁГКИЕ`, economy, roster, title or final VFX.
    Do not treat `c-designlab-gas-spatial-form-001` as automatically accepted; it is only a candidate next CALL until this map chooses it.
    Do not edit TREE/CHARTER unless the session explicitly routes to a separate owner-approved map/frame diff.

  done_when: |
    A local/canon-cartography RESULT contains:
    1. owner-readable question map for Mechanics Workbench;
    2. accounting table proving `Пузырь`, `ЛЁГКИЕ`, quiet floor, detection, reactions/release, carry/co-op, flagship examples, tools, old canon salvage and title boundary are all placed or explicitly rejected;
    3. each active/candidate question has plain_question, why_it_matters, answer_shape, status, dependency_type, blocks, do_not_solve_here, confusion_traps and route;
    4. explicit decision whether first next route is Design Lab, Mechanic Forge, Canon Forge, repair, or another cartography split;
    5. ready next CALL for the selected one-question session;
    6. owner approval / steering words cited for the map;
    7. no canon freeze;
    8. exact state_changes only through RESULT.

  return: |
    RESULT with readable Russian owner summary first, then machine RESULT block.

  budget: one session

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-repair-mechanics-workbench-cartography-route-001.md
