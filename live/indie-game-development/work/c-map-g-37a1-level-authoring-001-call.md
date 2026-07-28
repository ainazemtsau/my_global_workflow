CALL c-map-g-37a1-level-authoring-001
to: session
direction: indie-game-development
play: map
node: g-37a1
owner: PRESENT — this leg exists only to take his verdict on exact text.
goal: |
  TWO PARAGRAPHS OF EXACT TEXT, ONE SCREEN, AND HIS `да`. He ruled on 2026-07-28, in the chat that
  followed the cut-check, that the in-game «загрузка другого уровня кнопкой» is not needed and that
  the section's layout is authored as a TEXT FILE changed in the Editor between runs. Both places
  that carry the old wording are under his own exact-text approval, so neither may be edited without
  him. His ruling is already recorded verbatim at `NOW.md` `d-core-level-authoring-001`.
context: |
  THIS IS NOT A DESIGN LEG. Nothing is decided here; the decision is his and it is already made. The
  leg's whole job is to show him the two amended texts, take his word, and hand the consequences to
  `converge`. If he changes his mind on seeing the text, that is his right and the leg records it.

  READ, in this order:
  - `NOW.md` `d-core-level-authoring-001` — his ruling in his own words, including the reason.
  - `TREE.md` `g-37a1` criterion 12 — the clause to amend.
  - `work/core-requirements-g-37a1.md` line 5 and the settings register — the second place.
  - `history/2026-07-28-s-converge-verify-g-37a1-core-rows-cut-check-001.md` — the cut-check, whose
    §AFTER THE RESULT section records how the ruling arrived and what it dissolves.

  WHY THE BUTTON IS DROPPED, so the leg does not re-argue it. The cut-check first recommended KEEPING
  the clause on the ground that a second level is cheap under the file-based reading. That
  recommendation was WITHDRAWN as wrong: a button that loads another level at RUNTIME must tear down
  a live section with the substance simulation running, rebuild the topology, reposition both
  players, and settle whether one player's load reloads the session or splits the world (§SEAM 5) —
  and the engine-fit check established first-hand that topology replacement today RESETS live gas
  rather than migrating it. Loading once at start-up costs nothing. He reached the same answer from
  his own side and independently: «загружать уровни — это отдельно, потом мы будем обсуждать, как
  это делать. Сейчас нужно самое простое решение.»
boundaries: |
  - Show him the exact amended text of BOTH places IN FULL, in the message body. Text placed before
    an option-picker does not render for him, so it must be in the body.
  - Do not amend anything else in criterion 12: «все спорные числа вынесены наружу и меняются без
    пересборки», the start state, the immortality mode, the switches defaulting to OFF and «это
    инструмент эксперимента, а не генератор уровней» all STAY, unchanged and unrenumbered.
  - Do not add a clause about the layout file to the CARD. He accepted the recommendation that it
    lives in the requirements set and in the rows, not in `g-37a1`: «это в карточку не надо,
    технические детали запихивать».
  - Do not choose a file format, a schema, a field list, a path or a tool. «AI can edit it on his
    instructions» is the property; how it is met is `PLAN`/step 4.
  - Do not touch criteria 13, 14 or 15 — he settled them on 2026-07-28: «с критериями согласен, их
    не трогаем».
  - Do not open a bet, a task or a track. Do not answer `d-air-counter-visibility-001`.
  - No verdict may be inferred. Without his actual words the leg checkpoints and reissues.
done_when: |
  1. Criterion 12 amended so the in-game controls are the start state and the immortality mode, with
     the level button removed — his `да` on the exact text, quoted in the RESULT.
  2. `work/core-requirements-g-37a1.md` line 5 amended to match, and the section's layout named as
     AUTHORED CONTENT held in a text file: what it holds (габариты, карманы — сколько, где, каких
     размеров и видов, база), that it is changed between runs in the Editor or by editing the file
     and not from the running game, and that its format must be one an AI can change on his verbal
     instructions and can use to write a second file. His `да` on the exact text.
  3. `TREE.md`'s `owner_approved` line carries the new receipt; the RESULT marks `owner_approved`.
  4. The successor `c-converge-g-37a1-core-rows-cut-repair-001` is released from `waiting` to `ready`.
return: |
  One short `map` RESULT with both exact texts and his verbatim verdicts, and the released successor.
  If he revises either text, the RESULT carries what he actually said, not what was proposed.
budget: one session, short, owner present. FRESH CHAT.

END_OF_FILE: live/indie-game-development/work/c-map-g-37a1-level-authoring-001-call.md
