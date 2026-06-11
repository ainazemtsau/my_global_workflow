# NOW — indie-game-development

direction_id: indie-game-development
updated: 2026-06-11

## Current state

active_bet: none
active_tasks: []
open_calls: []
decision_inbox: []
recurring: []

## Routing

current_route: >
  New live direction bootstrap completed by frame RESULT. Next step is shape/setup verification before any product execution.

next:
  call_id: c-2026-06-11-indie-shape-setup-verification-001
  to: session
  play: shape
  node: g-setup-live-loop
  task: none
  summary: >
    Shape the first verification bet for the live-shell and CALL/RESULT/writer loop.

## Ready next CALL

CALL c-2026-06-11-indie-shape-setup-verification-001
to: session
direction: indie-game-development
play: shape
node: g-setup-live-loop  task: none
goal: |
  Сформировать первый approved bet, который проверяет setup/live-loop для нового direction `indie-game-development`: live files, CALL/RESULT/writer loop, route clarity, and continuation through state.
context: |
  Read:
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/TREE.md
  - live/indie-game-development/NOW.md
  - live/indie-game-development/LOG.md

  This is a new clean live direction. `archive/directions/indie-game-development` was not imported and must not be treated as current state.
boundaries: |
  Do not import `archive/directions/indie-game-development`.
  Do not restore legacy state.
  Do not launch Codex/product execution.
  Do not create Unity project.
  Do not transfer old code.
  Do not start product implementation.
  Mention archive only as a future evidence source for separate later transfer/import work.
done_when: |
  NOW.md contains one approved active bet for setup/live-loop verification, passing gates G1-G6.
  TREE.md marks `g-setup-live-loop` active or split into valid child outcomes.
  The next CALL is ready and still points to setup/writer verification, not product execution.
return: |
  RESULT packet with exact state_changes for TREE.md, NOW.md, LOG.md. Include evidence that no archive import or product execution happened.
budget: one session
surface: chatgpt

END_OF_FILE: live/indie-game-development/NOW.md
