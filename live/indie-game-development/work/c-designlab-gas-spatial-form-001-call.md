CALL c-designlab-gas-spatial-form-001
to: session
direction: indie-game-development
play: local/design-lab
node: g-d3a8
question: q-first-proof-gas-spatial-form
parent: s-designlab-mechanics-workbench-process-001
surface: chat / repo root `C:\my_global_workflow_worktrees\indie-game-development`

goal: |
  Run a chat-first Design Lab for ONE question:

  In the first playable Bubble proof, what does "gas is here" mean spatially?

  The session must present the question in chat with why-now, blockers, options, bad-because, boundaries and expected result.
  The owner must not be asked to browse files to find the question.

context: |
  Agent reads backend context before answering in chat:
  - live/indie-game-development/work/mechanics-workbench/chat-first-process-v0.md
  - live/indie-game-development/work/mechanics-workbench/question-queue-v0.md
  - live/indie-game-development/work/mechanics-workbench/area-map-v0.md
  - live/indie-game-development/work/mechanics-workbench/idea-ledger-v0.md
  - live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md
  - live/indie-game-development/work/design-labs/minimal-game-discussion-graph-001.md
  - live/indie-game-development/work/design-labs/ono-dyshit-bubble-proof-repair-001.md
  - live/indie-game-development/knowledge/mechanic-lenses.md

  Owner process correction:
  - Work happens through chat, not by owner walking through files.
  - One session = one question.
  - The chat packet must immediately say why this question matters and what it blocks.
  - Maps/ledgers are backend for the agent, not owner homework.

  Current queue:
  Q1 = what gas spatial form exists in first proof.
  This blocks detection/read, transfer-to-bubble, carry, release/reactions and co-op.

boundaries: |
  Do not freeze canon.
  Do not ask the owner to open files.
  Do not solve transfer-to-bubble yet.
  Do not solve exact membrane/tool/cargo/economy/`ЛЁГКИЕ`/full roster/title/final VFX.
  Do not use "газовый карман" or "запузырить" as ready terms.
  Do not make gas into creature AI or magical sleep/wake.
  Do not compare two playable concepts.

done_when: |
  A local/design-lab RESULT contains:
  1. owner-readable chat summary of the spatial-form question;
  2. options considered, each with "good because" and "bad because";
  3. explicit recommendation or narrowed decision;
  4. what the answer blocks/unblocks;
  5. what remains parked;
  6. whether a draft update is owner-approved or only captured;
  7. no canon freeze;
  8. exact state_changes only through RESULT.

return: |
  RESULT with readable Russian owner summary first, then machine RESULT block.

budget: one session

END_OF_FILE: live/indie-game-development/work/c-designlab-gas-spatial-form-001-call.md
