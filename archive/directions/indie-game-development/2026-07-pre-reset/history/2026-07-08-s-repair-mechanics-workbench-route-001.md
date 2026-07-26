RESULT s-repair-mechanics-workbench-route-001
direction: indie-game-development
play: repair
node/task: g-d3a8/mechanics-workbench-route
date: 2026-07-08
status: REPAIRED

owner_summary: |
  Исправлен не костыль, а route/state.

  Проблема:
    Mechanics Workbench и следующий CALL уже были созданы, но `NOW.md` не нес их как актуальный g-d3a8 open call.
    Из-за этого процесс существовал рядом со state, а не внутри Direction OS.

  Исправление:
    - `NOW.open_calls` теперь содержит `c-designlab-gas-spatial-form-001`;
    - `NOW.parallel_tracks.g-d3a8` теперь указывает на chat-first Workbench route;
    - stale decision "approve Bubble-first" убрана как главный вход, потому что теперь работа идет не через разовый approve, а через Q-by-Q Design Lab;
    - добавлен route note: Design Lab -> Mechanic Forge -> Canon Forge;
    - `TREE.md` не изменен, потому что g-d3a8 уже покрывает design/canon track, а структурное дерево можно менять только отдельным owner-approved map diff.

outcome: |
  Direction state now matches the intended process:
    - Mechanics Workbench is active as a g-d3a8 parallel track route, not a loose draft packet.
    - The next owner-facing design session is registered in NOW as `c-designlab-gas-spatial-form-001`.
    - Canon Forge is no longer treated as the immediate play for unresolved mechanics.
    - `local/mechanic-forge` is explicitly named as the correct later play for worked gameplay loops.

evidence: |
  Sources checked:
    - `NOW.md`: g-d3a8 still pointed to the older Bubble-first approval decision and had no Workbench open call.
    - `TREE.md`: g-d3a8 already describes the design truth / canon track and local canon process; no new top-level node is required for this repair.
    - `live/indie-game-development/plays/design-lab.md`: Design Lab is for unclear design/canon questions and routes next steps; it does not freeze canon.
    - `live/indie-game-development/plays/mechanic-forge.md`: mechanic-forge is specifically for one game-mechanic question as a worked playable loop, verb-first, mechanic-lens gated.
    - `live/indie-game-development/plays/canon-forge.md`: canon-forge freezes one canon card and checkpoints to cartography if hidden prerequisites appear.
    - `work/mechanics-workbench/*`: existing Workbench packet and chat-first process.

  Owner instruction:
    "никаких костылей нельзя"
    "если надо ... поменять вообще само дерево ... или ... мапы ... без костылей настраиваем"
    "now ... не применен. То есть это надо применить"
    "как вообще вот наш Canon Forge соответствует нашей работе, которую мы собираемся делать?"

diagnosis: |
  The previous setup was incomplete:
    Workbench artifacts existed, but `NOW.md` did not register the next g-d3a8 call.

  This was route drift, not a need for a new TREE node:
    `TREE.md` already has g-d3a8 as the design/canon truth node.
    Changing TREE would be a separate map-level decision requiring explicit owner approval under G9.

  Canon Forge correspondence:
    - Current unresolved Bubble mechanics are not canon-forge-ready.
    - Design Lab handles one unclear blocker at a time.
    - Mechanic Forge later freezes the worked playable loop if/when the mechanic is clear enough.
    - Canon Forge later freezes compact canon cards / question graph entries only after the loop/invariant is ready.

state_changes:
  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/route-to-forge-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/work/mechanics-workbench/mechanics-workbench-v0.md
    summary: |
      Added route-to-forge-v0.md to the Workbench index.

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/work/mechanics-workbench/question-queue-v0.md
    summary: |
      Added the route rule: Design Lab clears blockers, Mechanic Forge freezes worked loops, Canon Forge freezes compact canon only when ready.

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/work/c-designlab-gas-spatial-form-001-call.md
    summary: |
      Repaired CALL hygiene: goal is outcome-focused; parent updated to this repair; context names mechanic-forge/canon-forge route.

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/NOW.md
    operations:
      - set_updated: "2026-07-08 by s-repair-mechanics-workbench-route-001"
      - add_open_call:
          id: c-designlab-gas-spatial-form-001
          to: session
          for: g-d3a8 / Mechanics Workbench Q1
          call: work/c-designlab-gas-spatial-form-001-call.md
      - replace_parallel_track_state:
          id: g-d3a8
          summary: |
            g-d3a8 active in parallel via Mechanics Workbench, with current open call c-designlab-gas-spatial-form-001.
            Route: Design Lab -> Mechanic Forge -> Canon Forge when freeze-ready.
      - remove_decision:
          id: d-ono-dyshit-core-frame-fork-001
          reason: |
            Superseded by chat-first Q-by-Q Workbench route; Bubble-first remains current candidate, but not a one-shot approval decision.
      - update_next_tail:
          summary: |
            Primary next remains c-exec-034. Parallel g-d3a8 Workbench ready as c-designlab-gas-spatial-form-001.

  - repo: ainazemtsau/my_global_workflow
    action: do_not_edit
    paths:
      - live/indie-game-development/TREE.md
      - live/indie-game-development/CHARTER.md
    reason: |
      TREE/CHARTER changes require explicit owner-approved map/frame diff. Current g-d3a8 node already covers this route.

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/history/2026-07-08-s-repair-mechanics-workbench-route-001.md
    content_source: this_full_RESULT_block

  - repo: ainazemtsau/my_global_workflow
    action: append_line
    path: live/indie-game-development/LOG.md
    content: |-
      2026-07-08 — repair/route (g-d3a8/mechanics-workbench-route, s-repair-mechanics-workbench-route-001): fixed Mechanics Workbench route drift. Workbench drafts and Q1 CALL existed but NOW did not carry the g-d3a8 open_call, leaving the process beside state. Added `c-designlab-gas-spatial-form-001` to NOW.open_calls, updated g-d3a8 parallel track to chat-first Workbench route, removed stale one-shot Bubble-first decision, and documented the correct path: Design Lab clears blockers → Mechanic Forge freezes worked playable loops → Canon Forge freezes compact canon only when ready. TREE/CHARTER untouched; no canon freeze. → work/mechanics-workbench/route-to-forge-v0.md

captures:
  - id: no-tree-change-yet
    text: |
      No TREE change is needed for this repair. If g-d3a8 needs explicit child nodes for minimal proof / bubble / meta /
      greybox, run a separate owner-approved map/canon-cartography session.

  - id: canon-forge-role
    text: |
      Canon Forge corresponds to this work only after blockers are clear. It freezes compact canon, not unclear mechanics.

  - id: mechanic-forge-role
    text: |
      The repo already has `local/mechanic-forge` for worked playable mechanics; Bubble loop should go there before compact canon if it survives Design Lab.

decisions_needed: []

play_check:
  - "1 Name contradiction: done — Workbench/Q1 CALL existed in work/, but NOW did not register it; owner explicitly called this out."
  - "2 Reconstruct: done — read NOW/TREE/recent work/play files; current truth = Workbench route exists and must be in NOW."
  - "3 Propose corrected state: done — NOW open_call + g-d3a8 state + stale decision removal; TREE not edited because no owner-approved map diff is needed."
  - "4 Confirm: done — owner approval words: 'now ... не применен. То есть это надо применить'; 'никаких костылей нельзя'."
  - "5 Friction: skipped — one-off repair; if route drift repeats here, add OS friction."

log: |
  2026-07-08 — repair/route (g-d3a8/mechanics-workbench-route, s-repair-mechanics-workbench-route-001): fixed Mechanics Workbench route drift. Workbench drafts and Q1 CALL existed but NOW did not carry the g-d3a8 open_call, leaving the process beside state. Added `c-designlab-gas-spatial-form-001` to NOW.open_calls, updated g-d3a8 parallel track to chat-first Workbench route, removed stale one-shot Bubble-first decision, and documented the correct path: Design Lab clears blockers → Mechanic Forge freezes worked playable loops → Canon Forge freezes compact canon only when ready. TREE/CHARTER untouched; no canon freeze. → work/mechanics-workbench/route-to-forge-v0.md

next: |
  CALL c-designlab-gas-spatial-form-001
  to: session
  direction: indie-game-development
  play: local/design-lab
  node: g-d3a8
  question: q-first-proof-gas-spatial-form
  parent: s-repair-mechanics-workbench-route-001

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-repair-mechanics-workbench-route-001.md
