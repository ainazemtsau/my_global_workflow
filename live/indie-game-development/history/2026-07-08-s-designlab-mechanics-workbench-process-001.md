RESULT s-designlab-mechanics-workbench-process-001
direction: indie-game-development
play: local/design-lab
node/task: g-d3a8/mechanics-workbench-process
date: 2026-07-08
status: CHECKPOINT_PROCESS

owner_summary: |
  Процесс исправлен под chat-first.

  Владелец не должен ходить по файлам и искать, какой вопрос обсуждать.
  Карты и ledger остаются backend для агента.
  Рабочая сессия теперь должна начинаться с одного вопроса в чате: почему он сейчас, что блокирует, какие варианты, что не обсуждаем, какой результат нужен.

  Следующий готовый CALL:
    `c-designlab-gas-spatial-form-001`

  Первый вопрос:
    В первом Bubble-proof, когда мы говорим "здесь есть газ", что именно существует в пространстве?

outcome: |
  Added a chat-first process note and a question queue.

  Created a ready next Design Lab CALL for one question:
    `work/c-designlab-gas-spatial-form-001-call.md`

  Updated the review guide so it no longer tells the owner to browse files as the main workflow.

evidence: |
  Owner correction:
    - work must happen through the earlier process;
    - maps are needed, but owner should not browse files to find questions;
    - one question per session;
    - session starts with why this question matters;
    - Design Lab / process must cover the question from all sides;
    - internal setup should be convenient, but owner-facing work is through chat.

state_changes:
  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/chat-first-process-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/mechanics-workbench/question-queue-v0.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/work/c-designlab-gas-spatial-form-001-call.md
    content_source: drafted_work_file

  - repo: ainazemtsau/my_global_workflow
    action: edit_file
    path: live/indie-game-development/work/mechanics-workbench/review-guide-v0.md
    summary: |
      Updated owner process to chat-first: agent brings one question into chat; files are backend, not owner homework.

  - repo: ainazemtsau/my_global_workflow
    action: create_file
    path: live/indie-game-development/history/2026-07-08-s-designlab-mechanics-workbench-process-001.md
    content_source: this_full_RESULT_block

  - repo: ainazemtsau/my_global_workflow
    action: append_line
    path: live/indie-game-development/LOG.md
    content: |-
      2026-07-08 — design-lab/process checkpoint (g-d3a8/mechanics-workbench-process, s-designlab-mechanics-workbench-process-001): owner corrected Mechanics Workbench workflow to chat-first: maps/ledgers are backend, not owner homework; every session must present one question in chat with why-now, blockers, options, boundaries and needed result. Added chat-first process note, question queue, and ready next CALL `c-designlab-gas-spatial-form-001` for Q1: what "gas is here" means spatially in the first Bubble proof. No canon freeze; NOW/TREE/CHARTER untouched. → work/mechanics-workbench/chat-first-process-v0.md

  - repo: ainazemtsau/my_global_workflow
    action: do_not_edit
    paths:
      - live/indie-game-development/NOW.md
      - live/indie-game-development/TREE.md
      - live/indie-game-development/CHARTER.md

captures:
  - id: owner-does-not-browse-map
    text: |
      Owner-facing workflow is chat/CALL first. Files are agent memory and evidence, not the place where the owner hunts
      for the next question.

  - id: one-question-per-session
    text: |
      Every Design Lab session discusses one main question. Side ideas are captured and parked.

next: |
  CALL c-designlab-gas-spatial-form-001
  question: q-first-proof-gas-spatial-form
  owner-facing first question:
    "В первом proof, когда мы говорим 'здесь есть газ', что именно существует в пространстве?"

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-designlab-mechanics-workbench-process-001.md
