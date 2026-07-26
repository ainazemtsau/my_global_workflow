RESULT s-repair-designlab-owner-verdict-001 (call: owner repair request after premature Q1 Design Lab close)
direction: indie-game-development   play: repair   node/task: g-d3a8/q-first-proof-gas-spatial-form

outcome: |
  The premature Q1 Design Lab close is repaired.

  What is now true:
  - `c-designlab-gas-spatial-form-001` is again the open g-d3a8 Design Lab call.
  - `work/design-labs/gas-spatial-form-001.md` is reclassified as an agent proposal/draft for owner discussion, not an
    accepted/revised/split owner verdict and not a closed Design Lab result.
  - `c-designlab-gas-precontact-read-001` remains only a draft later CALL. It is not open and must not run until the
    owner gives a Q1 spatial-form verdict.
  - No canon freeze happened. TREE.md and CHARTER.md are untouched.

evidence: |
  Owner correction in chat:
  - "Почему он уже принят без меня?"
  - "я вставил кол, и сразу ты что-то там записал без моего разрешения"
  - "ты испортил ты и исправляй"

  Reconstructed state:
  - `c-designlab-gas-spatial-form-001` asked for the spatial model to be accepted/revised/rejected/split.
  - `s-designlab-gas-spatial-form-001` opened Q2 without owner verdict words for the Q1 spatial model.
  - Maintenance commit `08b90b9` added the owner-verdict guard so future cases bounce; this repair fixes the live
    direction state affected before that guard existed.

state_changes: |
  1. Update `live/indie-game-development/NOW.md`:
     - `updated:` becomes `2026-07-08 by s-repair-designlab-owner-verdict-001`.
     - Replace open_call `c-designlab-gas-precontact-read-001` with `c-designlab-gas-spatial-form-001`.
     - The restored Q1 open_call note says the previous close was invalid as a close, the work note is only an agent
       proposal/draft, and the next Q1 session must present a human-readable brief and stop for owner words before
       clearing the call or opening Q2.
     - g-d3a8 parallel-track state says Q1 remains open, Q2 is draft-only, and TREE/CHARTER remain untouched.
     - `next` tail points the g-d3a8 parallel track back to Q1 owner-verdict, not Q2.

  2. Update `live/indie-game-development/work/design-labs/gas-spatial-form-001.md`:
     - status becomes agent proposal draft, not canon, not owner-approved, not closed Design Lab result;
     - add repair note naming `s-repair-designlab-owner-verdict-001`;
     - replace closed/result wording with agent proposal / recommendation wording;
     - route returns to `c-designlab-gas-spatial-form-001`; Q2 call remains draft-only.

  3. Append to `live/indie-game-development/LOG.md`:
     `2026-07-08 — repair (g-d3a8/q-first-proof-gas-spatial-form, s-repair-designlab-owner-verdict-001): reverted premature Q1 Design Lab close to owner-pending. `s-designlab-gas-spatial-form-001` is reclassified as agent proposal/draft, not owner verdict; NOW.open_call restored to c-designlab-gas-spatial-form-001; Q2 c-designlab-gas-precontact-read-001 is draft-only until Q1 owner verdict. No canon freeze; TREE/CHARTER untouched.`

  4. Add this RESULT file as `live/indie-game-development/history/2026-07-08-s-repair-designlab-owner-verdict-001.md`.

  5. Do not edit `live/indie-game-development/TREE.md` or `live/indie-game-development/CHARTER.md`.

captures:
  - The OS/process defect was fixed separately in commit `08b90b9`: owner-verdict CALLs now require actual owner words before close.

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — NOW/LOG/history said Q1 was completed and Q2 open, but owner had not given a Q1 spatial-model verdict."
  - "2 Reconstruct: done — latest valid owner verdict was map approval `вариант A`; `s-designlab-gas-spatial-form-001` was an agent recommendation applied as close."
  - "3 Propose corrected state: done — restore Q1 open_call, reclassify gas-spatial-form note as draft/proposal, make Q2 draft-only."
  - "4 Confirm: done — owner explicitly ordered repair: `ты испортил ты и исправляй`."
  - "5 Friction: done — process gap already logged/fixed by maintenance commit `08b90b9`; this repair fixes live state."

log: 2026-07-08 — repair (g-d3a8/q-first-proof-gas-spatial-form, s-repair-designlab-owner-verdict-001): reverted premature Q1 Design Lab close to owner-pending. `s-designlab-gas-spatial-form-001` is reclassified as agent proposal/draft, not owner verdict; NOW.open_call restored to c-designlab-gas-spatial-form-001; Q2 c-designlab-gas-precontact-read-001 is draft-only until Q1 owner verdict. No canon freeze; TREE/CHARTER untouched.

next: |
  CALL c-designlab-gas-spatial-form-001
  to: session
  direction: indie-game-development
  play: local/design-lab
  node: g-d3a8
  question: q-first-proof-gas-spatial-form
  parent: s-cartography-mechanics-workbench-questions-001
  surface: chat / repo root `C:\my_global_workflow_worktrees\indie-game-development`

  goal: |
    Owner verdict exists for the first Bubble-proof spatial-form proposal: accept, revise, reject, or split.

  context: |
    Read:
    - live/indie-game-development/work/canon-maps/mechanics-workbench-question-map-v0.1.md
    - live/indie-game-development/work/mechanics-workbench/chat-first-process-v0.md
    - live/indie-game-development/work/mechanics-workbench/question-queue-v0.md
    - live/indie-game-development/work/mechanics-workbench/area-map-v0.md
    - live/indie-game-development/work/mechanics-workbench/idea-ledger-v0.md
    - live/indie-game-development/work/mechanics-workbench/core-proof-skeleton-v0.1.md
    - live/indie-game-development/work/design-labs/gas-spatial-form-001.md
    - live/indie-game-development/knowledge/mechanic-lenses.md

    Current truth:
    - owner approved the Mechanics Workbench question map v0.1 with "вариант A";
    - owner has NOT accepted/revised/rejected/split the Q1 spatial model;
    - `gas-spatial-form-001.md` is only an agent proposal/draft;
    - the session must present the Q1 question and recommendation in normal human language and stop for owner verdict.

  boundaries: |
    Do not freeze canon.
    Do not ask the owner to open files.
    Do not solve transfer-to-bubble yet.
    Do not solve exact membrane/tool/cargo/economy/`ЛЁГКИЕ`/full roster/title/final VFX.
    Do not use "газовый карман" or "запузырить" as ready terms.
    Do not make gas into creature AI or magical sleep/wake.
    Do not compare two playable concepts.
    Do not clear this call or open Q2 until the owner's actual verdict words are present.

  done_when: |
    The owner has explicitly accepted, revised, rejected, or split the Q1 spatial-form proposal in chat, and the RESULT
    quotes those owner words. Without that verdict, close only as a checkpoint and leave this call open.

  return: |
    Human-readable Russian summary first, then RESULT. No raw YAML as the owner-facing explanation.

  budget: one session

END_OF_FILE: live/indie-game-development/history/2026-07-08-s-repair-designlab-owner-verdict-001.md
