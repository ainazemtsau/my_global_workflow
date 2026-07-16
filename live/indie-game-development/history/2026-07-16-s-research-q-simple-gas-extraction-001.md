id: s-research-q-simple-gas-extraction-001
call: c-research-q-simple-gas-extraction-001
direction: indie-game-development
play: local/canon-forge
node_task: g-d3a8 / Simple Gas Extraction

outcome: |
  Текущий Canon Forge route остановлен на Gate Q как поставленный
  на неверной высоте.

  Gate F остаётся FRAME READY для дальнейшей работы над добычей:
  владелец ранее выбрал «Вариант A», поэтому bounded P0 economy/artifact
  wording не является prerequisite для extraction work.

  Simple Gas Extraction пока не оформляется как отдельный узкий вопрос.
  Сначала требуется owner-present research высокоуровневой концепции
  добычи: инструмент, роль Шара/Пузыря, базовый физический глагол,
  видимая трансформация газа, общая игровая фантазия, крупные источники
  решений и естественный co-op potential.

  Никакой paper candidate не выбран. OWNER-SELECTED PAPER ANSWER не создан.
  Canon admission не запускался.

evidence: |
  1. Current Frame basis:
     live/indie-game-development/work/minimum-game-frame-v2.md
     фиксирует Шар/Пузырь как principal extraction DESIGN ANCHOR,
     оставляя filling, controls, capacity, stages, helper count и
     rare alternatives OPEN.

  2. Current concept direction:
     gas_coop_game_canon/CORE.md прямо оставляет первым предметом
     обсуждения вопрос о том, как газ попадает в шарик, и требует
     простого входа без обязательной сложной процедуры.

  3. Gate F owner words:
     «Вариант A».

     Normalized Gate F result:
     FRAME READY for extraction concept research; P0 detached from Q1.

  4. Gate Q owner words:
     «Так, я бы сейчас смотрел, не называл это каким-то отдельным
     вопросом.»

     «Я хочу, чтобы мы просто сначала вот как у нас есть концепция,
     чтобы мы в таком же виде обработали так условно высокоуровневую
     концепцию вот именно добычи».

     Normalized Gate Q result:
     QUESTION BLOCKED — wrong altitude / missing high-level extraction
     concept basis.

  5. No paper comparison was generated after the owner's correction.
     No claim of fun, runtime legibility or actual co-op was made.

state_changes: |
  1. NOW.md:
     remove c-research-q-simple-gas-extraction-001 from open_calls as
     CLOSED / QUESTION BLOCKED — wrong altitude.

  2. NOW.md:
     add ready owner-present research call
     c-research-extraction-concept-landscape-001 for g-d3a8.

     note:
       Before another bounded Canon Forge question is opened, explore
       the high-level extraction concept at whole-mechanic altitude:
       tool, Bubble/Ball identity, primary physical verb, gas
       transformation, visible scene, broad decision sources and
       concept families. Simple Suction Bubble remains owner-origin
       input, not selected. No canon or implementation.

  3. NOW.md next:
     CALL:
       live/indie-game-development/work/
       c-research-extraction-concept-landscape-001-call.md

  4. Add this RESULT to history and append the corresponding one-line
     LOG entry.

  5. Do not modify TREE.md, CHARTER.md, current canon, product repositories
     or Sc-damage.

captures:
  - After the extraction-concept research produces an owner-selected
    direction, revisit g-d3a8 current-question cartography and derive the
    first bounded Canon Forge question from that concept rather than
    restoring the current Q1 automatically.

decisions_needed: []

play_check:
  - step_1_authority_and_scope: |
      done; current Frame, CORE, map and canon boundaries were loaded.
  - step_2_gate_f: |
      done; owner words «Вариант A» accepted as FRAME READY for
      extraction work with P0 detached from Q1.
  - step_3_gate_q: |
      blocked by owner correction; owner words:
      «Так, я бы сейчас смотрел, не называл это каким-то отдельным
      вопросом» and «Я хочу, чтобы мы просто сначала ... обработали ...
      высокоуровневую концепцию вот именно добычи».
  - step_4_paper_comparison: |
      skipped because Gate Q did not pass and the owner rejected the
      question-level framing.
  - step_5_paper_verdict: |
      skipped; no candidates were presented and no paper answer exists.
  - step_6_canon_admission: |
      skipped by scope; canon remains unchanged.
  - step_7_close: |
      done; one RESULT emitted and all mutations delegated to the writer.

log: |
  g-d3a8 extraction Canon Forge stopped QUESTION BLOCKED at wrong
  altitude; owner redirected the work to high-level extraction-concept
  research before any bounded paper question.

next:
  CALL:
    id: c-research-extraction-concept-landscape-001
    to: session
    direction: indie-game-development
    play: research
    node: g-d3a8
    parent: s-research-q-simple-gas-extraction-001

    goal: |
      Produce an owner-readable high-level concept landscape for gas
      extraction, at the same broad creative altitude used to establish
      the overall game concept, before deriving any narrow Canon Forge
      question.

    context: |
      Current Frame fixes the Ball/Bubble only as the principal visible
      extraction DESIGN ANCHOR; exact filling and behavior remain OPEN.
      CORE preserves Bubble as central concept direction and explicitly
      says the way gas enters it still requires discussion.

      The owner rejects treating current extraction work as one already
      bounded question. First explore what the extraction tool is, what
      the Bubble/Ball is, what physically happens, what the simple core
      verb and fantasy are, and which broad concept families deserve
      consideration.

      Simple Suction Bubble is owner-origin input only:
      one player may perform basic visible suction into a growing Bubble
      and choose when to stop. It is not selected and may be retained,
      revised, combined or rejected.

    boundaries: |
      Owner-present and text only.
      Research and brainstorm; do not run Gate Q or paper admission.
      Do not alter Frame, canon, TREE, CHARTER or product.
      Do not decide final controls, UI, exact capacity, carry loop,
      helper count, scaling, gas roster, economy, artifact mechanics,
      damage, networking, balance or implementation.
      Do not reward complexity or novelty for their own sake.
      Do not claim paper proves fun, runtime readability or actual co-op.
      Historical material is evidence only and does not constrain the
      new concept landscape.
      Sc-damage remains HELD.

    done_when: |
      1. The high-level extraction design space is explained in plain
         owner-readable language.
      2. The research defines the extraction fantasy, tool/Bubble
         relationship, primary physical action, visible gas/Bubble
         transformation and broad sources of decision pressure.
      3. Three to five mechanically distinct high-level concept families
         are presented at equal depth.
      4. Simple Suction Bubble is represented as owner-origin input,
         not an automatic winner.
      5. Each family names its strongest promise, strongest weakness,
         likely boring/stuffy failure and major unverified dimensions.
      6. Natural co-op potential is considered without fixing helper
         counts or claiming 4–8-player proof.
      7. The owner can select, combine, revise or reject concept
         directions.
      8. No canon, implementation or narrow downstream question is
         silently decided.

    return: |
      Russian high-level extraction concept brief; terminology;
      concept-space map; 3–5 equally rendered concept families;
      comparison and recommendation; unverified dimensions; exact owner
      verdict; one RESULT.

    budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/history/2026-07-16-s-research-q-simple-gas-extraction-001.md
