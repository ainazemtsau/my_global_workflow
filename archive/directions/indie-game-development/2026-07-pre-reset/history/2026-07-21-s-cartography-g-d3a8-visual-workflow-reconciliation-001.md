RESULT s-cartography-g-d3a8-visual-workflow-reconciliation-001 (call: c-cartography-g-d3a8-visual-workflow-reconciliation-001)
direction: indie-game-development
track: canon
play: local/canon-cartography
node/task: g-d3a8 / visual-workflow reconciliation

outcome: |
  Владелец утвердил точный простой маршрут:

  «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge,
  формат ответа определяется типом вопроса; dashboard позже как
  представление тех же данных.»

  После применения writer-транзакции законный рабочий маршрут будет таким:

  one topic/question graph
  → one Canon Forge
  → answer format follows the question
  → exact owner selection
  → paper/visual authority
  → separate canon admission
  → later empirical evidence.

  Механические и структурные вопросы могут использовать текст, diagram или
  sequence. Явно выбранные визуальные вопросы могут использовать форматы
  c-003 внутри того же Canon Forge.

  Не создаются отдельный visual Forge, отдельный process node или второй
  источник канона.

  V0 закрывается как RESOLVED / ADMITTED AS c-003. После применения
  reconciliation V1 становится следующим готовым owner-present CALL, но в
  этой сессии V1 не запускался и не получил никакого design answer.

  Owner selection, paper/visual authority, отдельный canon admission и
  runtime/playtest/performance/market evidence остаются разными переходами.

  Ни одно изображение не создано. Ни один внешний вид, canon answer,
  Frame, TREE, CHARTER или product state не изменён этой сессией.

evidence: |
  EXACT OWNER SIGN

  «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge,
  формат ответа определяется типом вопроса; dashboard позже как
  представление тех же данных.»

  FRESH SOURCE CHECKS

  - Active Canon Forge:
    live/indie-game-development/plays/canon-forge.md
    observed blob: 2a7b56d5979bdde4036b339900dd0aa02b260935
    verified conflict: hard boundary `Text only`; Step 4 is paper-only.

  - Current canon map:
    live/indie-game-development/work/canon-maps/
    g-d3a8-current-question-front-v3.md
    observed blob: f60f01b4812ce3bb0f89e0e1b40818913ec2174f
    verified route: V0 precedes V1; gap rule returns a text-only/image-work
    process conflict to cartography.

  - Current c-003:
    ainazemtsau/gas_coop_game_canon/
    canon/c-003-visual-development-contract.md
    observed blob: 97f364663fdc9c264929f3321458de0d945f24fa
    verified END_OF_FILE marker.
    c-003 permits bounded visual formats while preserving explicit
    placeholders, accidental-detail non-authority, owner selection, separate
    canon admission and later empirical evidence.

  - Current NOW:
    live/indie-game-development/NOW.md
    observed blob: 979c0ca54550428942c398a38b7a1f00b6662835
    returning canon root is still
    c-cartography-g-d3a8-visual-workflow-reconciliation-001.
    NOW.next remains c-work-grid-v1-executor-plan-001.

  - Current canon QUEUE:
    ainazemtsau/gas_coop_game_canon/QUEUE.md
    observed blob: b3be804770299866fd69d6f925fc780a6b94ac25
    verified that V1 remains ineligible until this reconciliation is applied.

  - No image-generation tool was invoked.
  - No repository was edited by this session.
  - Every relied-on governing file had its declared END_OF_FILE marker.

state_changes: |
  Apply against fresh current state using stable paths, call ids, headings and
  exact replacement anchors. This session performed no repository writes.

  PRE-FLIGHT AND TRANSACTION RULE

  Preflight every target in both repositories before writing. Apply the
  Direction play/map/route changes and canon QUEUE route change as one bounded
  reconciliation transaction.

  If any exact target has a materially incompatible concurrent meaning, any
  required END_OF_FILE marker is missing, or the successor CALL path collides,
  apply nothing: do not clear the returning call and do not register V1.

  Preserve all concurrent changes outside the declared semantic targets.

  A. DIRECTION REPOSITORY — ainazemtsau/my_global_workflow

  1. UPDATE THE SINGLE CANON FORGE IN PLACE

     Path:
     live/indie-game-development/plays/canon-forge.md

     Observed base blob:
     2a7b56d5979bdde4036b339900dd0aa02b260935

     Keep the title, status, installation metadata, Steps 1–3, Steps 6–7 and
     END_OF_FILE marker unless an exact replacement below says otherwise.

     1.1 REPLACE THE COMPLETE `Purpose:` BLOCK

     Replace the block beginning exactly at:

     Purpose: |

     and ending immediately before:

     Authority:

     with:

     Purpose: |
       Управлять единым переходом от текущей Minimum Game Frame к
       owner-selected answer и далее к отдельному owner-present canon
       admission. Тип вопроса определяет формат ответа. Selection,
       paper/visual authority, canon admission и later evidence остаются
       разными переходами.

     1.2 REPLACE THE COMPLETE `Authority:` BLOCK

     Replace from `Authority:` through the line immediately before `Reads:`
     with:

     Authority:
       - This play is the sole active design-to-canon route.
       - Canon Forge v2 is removed from live routing and is not a fallback.
       - Gate F, Gate Q and text-candidate discipline come from:
         live/indie-game-development/work/
         canon-process-v3-paper-only-pilot-brief.md
       - Visual questions follow the current canon card:
         canon/c-003-visual-development-contract.md
       - For an explicit visual question, c-003 replaces only the pilot
         brief's text-only format restriction. Both gates and all authority
         transitions remain unchanged.
       - Current owner instruction and Direction OS state outrank stale
         sources.

     1.3 UPDATE THE CANON-REPOSITORY READ ENTRY

     Replace exactly:

       - canon repository:
         CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md and directly relevant
         canon cards

     with:

       - canon repository:
         CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md,
         canon/c-003-visual-development-contract.md and directly relevant
         canon cards

     1.4 REPLACE THE COMPLETE `Hard boundaries:` BLOCK

     Replace from `Hard boundaries:` through the line immediately before
     `Steps:` with:

     Hard boundaries:
       - One Forge handles every design question; format follows the question.
       - Use text, diagram or sequence when sufficient. A visual question
         named by the active CALL may use c-003 formats and must obey c-003.
       - No Unity scene, greybox, runtime A/B build, setup, playtest, tuning,
         implementation or production-asset work.
       - No candidate generation before both FRAME READY and QUESTION READY.
       - A blocked gate stays on the same missing basis or question.
       - An OWNER-SELECTED PAPER ANSWER or OWNER-SELECTED PLATE is not canon.
       - Canon admission requires a separate owner-present verdict on the
         exact selected artifact.
       - No question auto-starts from QUEUE.md.
       - No process or canon mutation occurs before its owner verdict.
       - Stale v2 files, old chats and git-history text have no live authority.

     1.5 REPLACE STEPS 4–5 ONLY

     Replace the complete current Step 4 and Step 5 blocks, from:

       4. Paper comparison:

     through the line immediately before:

       6. Canon admission:

     with:

       4. Candidate comparison:
          only after both gates pass, choose the minimum useful format.
          Define local criteria and a shared situation when needed; generate
          privately, hard-kill weak directions and show the smallest useful
          bounded set: one explanatory artifact or 2–3 comparable candidates.
          Visual work follows c-003. Otherwise return BLOCKED honestly.

       5. Owner selection:
          record the owner's exact words. Save the selected text answer or
          plate with its rules, placeholders, non-binding details, production
          check and unverified dimensions. It is paper/visual authority, not
          canon.

     1.6 REPLACE THE COMPLETE `Done when:` BLOCK

     Replace from `Done when:` through the line immediately before the
     END_OF_FILE marker with:

     Done when:
       The active CALL reaches its bounded owner verdict; its format matches
       the question; Frame and Question gates, owner selection, paper/visual
       authority, separate canon admission and later evidence remain explicit;
       no stale route auto-starts; the RESULT cites every owner step verbatim.

     Postconditions:

     - The play remains the single Canon Forge.
     - The play remains within the local-play 600-word budget.
     - The paper-only pilot brief still governs Gate F, Gate Q and text
       comparison discipline.
     - c-003 changes only the allowed format for an explicit visual question.
     - The exact existing END_OF_FILE marker remains last.

  2. UPDATE THE CURRENT CANON MAP IN PLACE

     Path:
     live/indie-game-development/work/canon-maps/
     g-d3a8-current-question-front-v3.md

     Observed base blob:
     f60f01b4812ce3bb0f89e0e1b40818913ec2174f

     2.1 RECORD THE OWNER-APPROVED RECONCILIATION

     Immediately after the existing `owner_verdict: |` quotation block and
     before `## 1. Authority`, insert exactly once:

     reconciled_on: 2026-07-21
     reconciliation_verdict: |
       «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge,
       формат ответа определяется типом вопроса; dashboard позже как
       представление тех же данных.»

     2.2 ADD c-003 TO THE CURRENT CANON AUTHORITY LIST

     Replace exactly:

         - c-002 gas behavior jobs.

     with:

         - c-002 gas behavior jobs;
         - c-003 visual-development contract.

     2.3 STATE THE SIMPLE GRAPH RULE

     Immediately after:

     This map answers no gameplay- or visual-design question.

     insert exactly once:

     This is one graph of game topics and their sourced questions.
     Dependencies decide what can be discussed now; `answer_shape` selects
     the working format. A visual question stays in the same graph and uses
     the same Canon Forge.

     2.4 UPDATE THE POST-c-002 ROUTE SENTENCE

     Replace exactly:

     The next selected question is the minimal visual-development contract.

     with:

     V0 is RESOLVED / ADMITTED as c-003.

     After the approved Canon Forge reconciliation is applied, V1 is the next
     selected question.

     2.5 REMOVE THE OBSOLETE STANDING VALUE

     Remove exactly one list item:

     - needs_visual_contract

     2.6 REPLACE ONLY THE V0 → V1 GRAPH SLICE

     Replace exactly:

          +--> V0 minimal visual-development contract       [READY / NEXT]
          |       |
          |       v
          |     V1 gas + Sphere visual readability          [NEEDS PREFACE]
          |       |-----------------------------|
          |       v                             v
          |     F2 bounded bad-state scene      C1 later evidence

     with:

          +--> V0 minimal visual-development contract       [CANON RESOLVED /
          |                                                   c-003]
          |       |
          |       | owner-approved simple Forge format reconciliation
          |       v
          |     V1 gas + Sphere visual readability          [READY / NEXT CALL]
          |       |-----------------------------|
          |       v                             v
          |     F2 bounded bad-state scene      C1 later evidence

     2.7 REPLACE THE COMPLETE V0 NODE

     Replace from heading:

     ### V0 — Minimal visual-development contract

     through the line immediately before:

     ### V1 — Gas and Sphere visual readability

     with:

     ### V0 — Minimal visual-development contract

     plain_question:
       What minimum rules let us attach AI-generated images to design
       questions without accidentally treating placeholders, old screenshots
       or random generated details as canon?
     why_it_matters:
       The admitted contract lets visual questions use generated material
       without granting authority to placeholders, historical screenshots or
       accidental details.
     answer_shape: invariant
     status: downstream
     standing: canon_resolved
     dependency_type: hard_prerequisite
     depends_on:
       - current owner visual reset
       - current INDEX authority model
       - historical visual materials as evidence only
     dependency_reason:
       The exact V0 artifact completed Gate F, Gate Q, owner paper selection
       and separate canon admission as c-003.
     blocks: []
     do_not_solve_here:
       - exact environment style
       - exact gas look
       - exact Sphere look
       - character design
       - camera design
       - UI design
       - actual image generation
       - product asset production
     needs_anchor: none
     confusion_traps:
       - old StyleBible treated as current canon
       - one generated image silently fixing many unrelated details
       - selected taste treated as final asset
       - placeholder character becoming character canon
       - low production cost collapsing into cheap-looking art
       - demanding a full art bible before any useful image
     forge_handoff:
       plain_question:
         No current Forge handoff.
       why_now:
         V0 is resolved and admitted as c-003.
       must_decide:
         Nothing unless a formal replacement of c-003 is proposed.
       must_not_decide:
         Any actual appearance or silent extension of c-003.
       parent_locks:
         c-003 in full; old gas visuals remain invalid; only explicitly named
         properties can receive authority.
       expected_answer_shape: invariant
       first_owner_question:
         What exact current evidence justifies replacing c-003?
       return_to_graph_if:
         A future bounded question exposes a direct contradiction with c-003
         rather than an ordinary application of it.

     2.8 REPLACE THE COMPLETE V1 NODE

     Replace from heading:

     ### V1 — Gas and Sphere visual readability

     through the line immediately before:

     ### D0 — Investigation pressure sources

     with:

     ### V1 — Gas and Sphere visual readability

     plain_question:
       What should players see in the gas field and in the filled Sphere so
       they understand that this situation requires Counter, Brake or Time
       before the serious consequence has already happened?
     why_it_matters:
       c-002 defines which decisions differ, but no valid visual language
       exists for reading those differences.
     answer_shape: visual_plate
     status: ready
     standing: ready_design
     dependency_type: visual_anchor
     depends_on:
       - c-003
       - reconciled local/canon-forge
       - c-002
       - accepted Sphere Frame
     dependency_reason:
       c-003 now defines visual authority and the reconciled single Forge
       provides the lawful format route. The actual visual answer remains
       fully open.
     blocks:
       - gas visual language
       - Sphere visual language
       - visual sequence plates
       - field-legibility questions
       - bounded failure scenes
       - visual co-op scenarios
     do_not_solve_here:
       - gas names or final roster
       - exact forces or cycles
       - final VFX implementation
       - renderer
       - final UI
       - character visual design
       - reactions
       - damage
     needs_anchor: visual_plate
     confusion_traps:
       - reusing invalid old gas imagery
       - different colour as the whole answer
       - decorative fog
       - one hero image instead of comparable gameplay situations
       - movement signal visible only after failure
       - placeholder character becoming binding
     forge_handoff:
       plain_question:
         Which field, Sphere and motion signs make Counter, Brake and Time
         visually distinguishable before and during commitment?
       why_now:
         It is the next selected question after the applied reconciliation.
         It opens only through a fresh explicit owner-present CALL.
       must_decide:
         Visual information hierarchy across open gas, growing Sphere, closed
         cargo and near-loss-of-control sequence.
       must_not_decide:
         Final roster, renderer, controls, reactions, damage or
         implementation.
       parent_locks:
         c-002; c-003; universal Sphere; gas movement; volume as strength;
         shell as general endurance; no old gas image authority.
       expected_answer_shape: visual_plate
       first_owner_question:
         In one otherwise identical scene, what must change on screen so you
         can tell which physical obligation the gas creates?
       return_to_graph_if:
         A candidate depends on an undefined gas law, character foundation
         or visual-contract rule.

     2.9 REPLACE THE COMPLETE CURRENT-ROUTE SECTION

     Replace from:

     ## 9. Current owner-selected route

     through the line immediately before:

     ## 10. Gap rule

     with:

     ## 9. Current owner-selected route

     Exactly one current canon-track root after this reconciliation
     transaction:

     V1 — visual readability of Counter / Brake / Time across open gas,
     growing Sphere, closed cargo and near-loss-of-control sequence.

     The fresh V1 CALL is READY but has not been executed. No image was
     generated and no V1 design answer exists from this reconciliation.

     Why now:

     - V0 is admitted as c-003;
     - one Canon Forge now chooses format from the question;
     - c-002 supplies Counter / Brake / Time;
     - old gas visual remains invalid;
     - visual readability is still open.

     Other genuinely ready but not selected questions:

     - D0 investigation pressure sources;
     - F0 current floor-board read;
     - E0 safe-return conversion;
     - C0 paper design of 4–8-player cooperation.

     No question is answered or admitted automatically.

     2.10 REPLACE THE OBSOLETE GAP BULLET

     Replace exactly:

     - a process conflict between text-only Forge and required image work;

     with:

     - a format conflict: visual work is attempted outside an explicit c-003
       question, before FRAME READY and QUESTION READY, or without a bounded
       placeholder/non-scope basis;

     Do not modify any other map node, historical finding or dependency.

  3. CREATE THE FRESH V1 CALL EXACTLY ONCE

     Path:
     live/indie-game-development/work/
     c-forge-g-d3a8-gas-sphere-visual-readability-v1-001-call.md

     If absent, create it with the exact CALL carried in `next` below,
     followed by:

     END_OF_FILE:
     live/indie-game-development/work/
     c-forge-g-d3a8-gas-sphere-visual-readability-v1-001-call.md

     If byte-identical, no-op. If materially different, stop with a semantic
     collision and do not clear the returning call.

  4. UPDATE NOW.md BY STABLE CALL IDS

     Path:
     live/indie-game-development/NOW.md

     Observed base blob:
     979c0ca54550428942c398a38b7a1f00b6662835

     - Set:

       updated: 2026-07-21 by s-cartography-g-d3a8-visual-workflow-reconciliation-001

     - Remove exactly the open_calls entry whose id is:

       c-cartography-g-d3a8-visual-workflow-reconciliation-001

     - Add exactly one new parentless root entry in track `canon`:

       - id: c-forge-g-d3a8-gas-sphere-visual-readability-v1-001
         track: canon
         status: ready
         to: session
         for: "g-d3a8 / V1 controlled visual readability of Counter / Brake / Time"
         issued: 2026-07-21
         call: work/c-forge-g-d3a8-gas-sphere-visual-readability-v1-001-call.md
         receipts:
           - history/2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md
         note: "READY / NON-DEFAULT / OWNER-PRESENT / VISUAL QUESTION / c-003. One graph and one Canon Forge; format follows the question. Begin under the current Forge gates. Old gas visuals remain invalid. Environment, character, camera and UI are non-binding placeholders unless separately selected. No final roster, reactions, damage, controls, renderer, implementation, production assets or empirical claims. Owner selection remains paper/visual authority; canon admission is separate."

     - Preserve every unrelated track, call, receipt, decision and status.
     - Preserve NOW.next exactly as:

       next:
         call: c-work-grid-v1-executor-plan-001

       because the returning canon call was not the global default.

  5. APPEND ONE LOG ENTRY

     Path:
     live/indie-game-development/LOG.md

     Before the current END_OF_FILE marker, add exactly once:

     2026-07-21 — local/canon-cartography reconciliation (g-d3a8/V0→V1, s-cartography-g-d3a8-visual-workflow-reconciliation-001): owner verdict «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge, формат ответа определяется типом вопроса; dashboard позже как представление тех же данных.» keeps one question graph and one Forge, makes visual format lawful under c-003, preserves separate selection/admission/evidence, and registers V1 only after apply; no image or V1 answer was created. → history/2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md

  6. SAVE THIS RESULT VERBATIM

     Path:
     live/indie-game-development/history/
     2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md

     Add only if absent. If identical, no-op. If different, stop with a
     semantic collision.

  B. CANON REPOSITORY — ainazemtsau/gas_coop_game_canon

  7. UPDATE QUEUE.md ROUTING ONLY

     Path:
     QUEUE.md

     Observed base blob:
     b3be804770299866fd69d6f925fc780a6b94ac25

     Replace exactly the block beginning:

     The active local/canon-forge play remains text-only. Therefore V1 is not
     active and no image-generating CALL may be issued directly from this
     admission.

     and ending:

     A future design question may be opened only by a new explicit Direction OS
     CALL under the reconciled Canon Forge route, beginning with the applicable
     Frame and Question gates.

     with:

     The owner approved the simple reconciliation route on 2026-07-21:

     «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge,
     формат ответа определяется типом вопроса; dashboard позже как
     представление тех же данных.»

     Canon Forge remains one process. The question determines the answer
     format; visual questions use c-003. Frame and Question gates still
     precede candidate work. Owner selection, paper/visual authority,
     separate canon admission and later empirical evidence remain separate.

     The applied reconciliation is recorded in:

     `live/indie-game-development/history/
     2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md`

     V1 gas + Sphere visual readability is eligible and registered as the
     fresh owner-present Direction OS CALL:

     `c-forge-g-d3a8-gas-sphere-visual-readability-v1-001`

     It has not been answered; this reconciliation generated no image, and
     no question auto-starts.

     Preserve the existing `status: NO ACTIVE DESIGN QUESTION`: a READY CALL
     is eligible but is not an active running design session.

  8. DO NOT MODIFY

     Direction repository:
     - TREE.md
     - CHARTER.md
     - Minimum Game Frame v2
     - Gas Sphere extraction/custody Frame
     - c-003 source paper artifact
     - any product, Sc-damage or visual asset

     Canon repository:
     - CONSTITUTION.md
     - CORE.md
     - INDEX.md
     - canon/c-001-investigation-readiness.md
     - canon/c-002-gas-behavior-jobs.md
     - canon/c-003-visual-development-contract.md
     - any historical visual file or actual visual asset

captures:
  - Later candidate: a read-only HTML canon dashboard generated from the same topic/question graph and canon sources; it must remain a presentation layer, never independent authority.

decisions_needed: []

play_check:
  - 1 Frame cluster: done — bounded cluster was the process conflict between admitted c-003 visual work and active text-only Canon Forge; no V1 answer was included.
  - 2 Inventory: done — inventoried admitted V0/c-003, active Forge boundary, V1 dependency, current map gap rule, owner corrections and prohibited design dimensions.
  - 3 Plain questions: done — reduced the issue to one owner-readable question: whether visual questions use the same Forge with a question-selected format or require a separate process.
  - 4 Classify graph: done — V0 is canon_resolved; the reconciliation is a process edge rather than a new design node; V1 becomes ready only after apply; empirical claims remain proof_later.
  - 5 Route: done — presented one-Forge/simple-format route, full process rewrite and dashboard-only concealment; recommended the one-Forge route because it removes the conflict without adding another authority or handoff.
  - 6 Owner sign: done — owner words cited verbatim: «ПРИНИМАЮ ПРОСТОЙ МАРШРУТ: один граф тем, один Canon Forge, формат ответа определяется типом вопроса; dashboard позже как представление тех же данных.»

log: |
  canon/local-canon-cartography g-d3a8:
  owner approved one topic/question graph and one Canon Forge with
  question-selected answer format; exact play/map/QUEUE reconciliation makes
  V1 ready after writer apply while preserving separate owner selection,
  canon admission and later evidence.

next: |
  CALL c-forge-g-d3a8-gas-sphere-visual-readability-v1-001
  to: session
  direction: indie-game-development
  track: canon
  play: local/canon-forge
  node: g-d3a8
  surface: chatgpt

  goal: |
    The owner reaches a bounded visual-design verdict on which visible field,
    Sphere and motion signs let players distinguish Counter, Brake and Time
    before serious consequence.

  context: |
    Read:

    - os/KERNEL.md
    - os/schema/packets.md
    - live/indie-game-development/NOW.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/plays/canon-forge.md
    - live/indie-game-development/plays/canon-cartography.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/work/
      gas-sphere-extraction-custody-frame-v1.md
    - live/indie-game-development/work/canon-maps/
      g-d3a8-current-question-front-v3.md
    - live/indie-game-development/history/
      2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md
    - current gas_coop_game_canon CONSTITUTION.md, CORE.md, INDEX.md,
      QUEUE.md, canon/c-002-gas-behavior-jobs.md and
      canon/c-003-visual-development-contract.md.

    Current truth:

    - c-002 establishes Counter / Brake / Time, movement-first, volume as
      strength, shell as general endurance and universal Sphere capture;
    - c-003 governs visual formats, placeholders, accidental details,
      owner-selected plates, production envelope and separate canon admission;
    - the owner approved one graph and one Canon Forge, with format selected
      from the question;
    - no current environment, gas, Sphere, character, camera or UI appearance
      is selected by this reconciliation;
    - old gas visual material is INVALID TARGET / NEGATIVE EVIDENCE ONLY;
    - V1 is the next selected question and has not yet been answered.

  boundaries: |
    Owner-present.

    Governed by the current local/canon-forge and c-003. Do not generate
    candidates outside the play's Frame and Question gates.

    Do not redesign, replace or extend c-002, c-003, Minimum Game Frame v2 or
    the Gas Sphere extraction/custody Frame.

    Old gas imagery is not a prompt anchor, baseline, candidate or selected
    reference.

    Environment, character, camera and UI are outside this question. When
    unavoidable in a candidate, they remain explicit non-binding placeholders.

    Do not decide the final gas roster, reactions, damage, controls, renderer,
    networking, implementation or production assets. Do not turn a bounded
    visual sign into a whole-game final palette by implication.

    Any owner-selected result remains paper/visual authority. Canon admission
    requires a separate later owner-present CALL over the exact artifact.

    Images do not prove runtime legibility, fun, real co-op behaviour,
    implementation cost, performance, production feasibility or market
    response.

  done_when: |
    The owner gives an exact bounded V1 verdict or an honest blocked verdict.

    Any selected artifact has a c-003 rule card naming its purpose, binding
    rules and relations, selected references, placeholders, important
    non-binding details, production check, replacements and unverified claims.

    No adjacent design dimension, empirical claim or canon admission is
    silently included.

    One RESULT closes the session and states whether a separate canon-admission
    CALL is eligible.

  return: |
    Owner-readable V1 brief; exact owner verdict; selected plate and rule-card
    paths or exact block; explicit paper/canon/evidence status; one RESULT.

  budget: one owner-present session

writer_apply:
  canon_main_commit: 0018045c21b1997d70b8b54357c5ee90b52bd67a
  canon_main_readback: verified

END_OF_FILE: live/indie-game-development/history/2026-07-21-s-cartography-g-d3a8-visual-workflow-reconciliation-001.md
