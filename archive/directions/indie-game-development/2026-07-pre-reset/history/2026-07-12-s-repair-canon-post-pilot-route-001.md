RESULT s-repair-canon-post-pilot-route-001
call: c-repair-canon-post-pilot-route-001
direction: indie-game-development
play: repair
node/task: g-d3a8 / post-pilot canon process authority repair
revision: writer-bounce-1

outcome: |
  Owner installed Canon Forge v3 as the sole active design-to-canon process
  under the verbatim verdict:

  "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

  Canon Forge v2 is not resumed and is not retained as a live fallback.

  Owner additionally authorized removal of previous live process surfaces
  under the verbatim instruction:

  "Прошлые можно удалить что бы не плодить legacy"

  This authorization is applied narrowly to executable and owner-visible
  process routing:

  - the live v2 OS wrapper is replaced in place;
  - canon-repository START.md, README.md, SESSION.md and QUEUE.md are replaced
    in place with v3 routing;
  - stale v2 routing statements are removed from the otherwise empty INDEX.md;
  - no v2 wrapper, v2 queue, v2 session script, v2 README instruction or
    automatically selected v2 question remains available as a live route;
  - no new legacy/superseded process file is created.

  Immutable Direction OS history, LOG records and git history are not rewritten.
  They remain audit evidence, not executable process authority.

  q-investigation-readiness-paper-decision-v1 remains an
  OWNER-SELECTED PAPER ANSWER and remains non-canon.

  Canon admission remains a separate owner decision. After this repair is
  applied, c-research-q-investigation-readiness-canon-admission-001 becomes
  READY under active Canon Forge v3.

  No ADMIT TO CANON / HOLD PAPER-ONLY / REJECT AS CANON CANDIDATE verdict was
  issued in this repair.

  No canon card, new design question, design answer, implementation task,
  prototype or playtest task is opened.

evidence: |
  - Owner installation verdict, verbatim:

    "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

  - Owner cleanup authorization, verbatim:

    "Прошлые можно удалить что бы не плодить legacy"

  - Writer bounce, current session:

    previous RESULT was rejected because canon-repository README.md remained an
    executable v2 entrypoint. Partial application was fully removed; both
    repositories and indexes were reported clean, with no commits.

  - Current github.com/ainazemtsau/gas_coop_game_canon/README.md before repair:

    README.md declares Кузница v2 to be the process, tells a new chat to launch
    v2, says "что дальше" automatically selects the current queue piece, and
    advertises core-1…core-10 as the live route.

  - live/indie-game-development/history/
    2026-07-10-s-repair-canon-design-process-route-001.md:

    owner verdict «А» suspended Canon Forge v2 as the active design-decision
    route; core-0/core-1 became HOLD material for one pilot.

  - commit 77da91bcc7cdd97487498d54a5f9550a4b96c3d9:

    "indie-game-development repair g-d3a8/canon-process:
    suspend Forge v2 and open process-v3 research"

  - live/indie-game-development/work/
    canon-process-v3-paper-only-pilot-brief.md:

    the corrected paper-only pilot passed under process verdict "ACCEPTED";
    the artifact explicitly says that this verdict did not itself install the
    process, alter canon or admit the paper answer.

  - live/indie-game-development/history/
    2026-07-11-s-review-canon-process-v3-revised-pilot-001.md:

    "ACCEPTED" was a process-pilot verdict only.

  - commit 1a27c2b40f8de725fae13bd626d55ca4a92d16f1:

    "indie-game-development research g-d3a8/Canon-Forge-v3:
    ACCEPTED pilot; route canon-admission verdict"

  - live/indie-game-development/work/
    q-investigation-readiness-paper-decision-v1.md:

    status is OWNER-SELECTED PAPER ANSWER; authority explicitly says not canon;
    fun, actual co-op, runtime legibility, pressure pacing, engine cost and
    commercial proof remain UNVERIFIED.

  - live/indie-game-development/history/
    2026-07-11-s-research-q-investigation-readiness-canon-admission-001.md:

    admission returned BLOCKED without ADMIT/HOLD/REJECT because no explicit
    post-pilot governing process had been selected.

  - Current canon repository before this repair:

    START.md, README.md, QUEUE.md and SESSION.md expose Кузница v2.
    INDEX.md contains no frozen v2 card but still says its first card will come
    from v2 and that old material is transferred through v2.

  - Current live/indie-game-development/NOW.md before this repair:

    c-repair-canon-post-pilot-route-001 is the active canon-process repair CALL.

state_changes: |
  Apply atomically against fresh current state using stable ids and exact paths.

  This session did not directly edit either repository.

  The writer reported that the rejected partial application was fully removed.
  Therefore apply this RESULT as a complete change set, not as a delta over the
  rejected attempt.

  ======================================================================
  A. DIRECTION OS HOT STATE
  ======================================================================

  1. Edit:

     live/indie-game-development/NOW.md

     1.1 Set the last-applier-wins header to:

         updated: 2026-07-12 by s-repair-canon-post-pilot-route-001

     1.2 Remove exactly the open_calls entity with stable id:

         c-repair-canon-post-pilot-route-001

     1.3 Upsert exactly one open_calls entity:

         - id: c-research-q-investigation-readiness-canon-admission-001
           to: session
           for: g-d3a8 / q-investigation-readiness paper-answer canon admission
           issued: 2026-07-12
           note: "READY under active Canon Forge v3 installed by owner verdict «УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС». Evaluate only the exact existing OWNER-SELECTED PAPER ANSWER «Цель стоит запуска» for ADMIT TO CANON / HOLD PAPER-ONLY / REJECT AS CANON CANDIDATE. No answer revision, new design question, implementation or automatic canon change. work/c-research-q-investigation-readiness-canon-admission-001-call.md."

     1.4 Preserve every other fresh-current NOW.md field and entity unchanged,
         including:

         - the active Poligon M1 bet;
         - all tasks and statuses;
         - every unrelated open_call;
         - every pending decision;
         - recurring entries.

     1.5 Preserve NOW.next unchanged after semantic rebase.

         Reopening the canon-admission CALL does not replace or reorder the
         current global engineering next.

  ======================================================================
  B. INSTALL CANON FORGE V3 AS THE ACTIVE LOCAL PLAY
  ======================================================================

  2. Replace the entire content of:

     live/indie-game-development/plays/canon-forge.md

     with exactly:

     FILE_CONTENT_BEGIN

     # Play: local/canon-forge — Canon Forge v3

     status: ACTIVE
     installed_on: 2026-07-12
     owner_verdict: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

     Purpose: |
       Управлять paper-only переходом от текущей Minimum Game Frame к
       owner-selected paper answers и далее к отдельному owner-present canon
       admission. Design discovery, paper selection и canon authority остаются
       разными переходами.

     Authority:
       - This play is the sole active design-to-canon route.
       - Canon Forge v2 is removed from live routing and is not a fallback.
       - The accepted process specification is:
         live/indie-game-development/work/
         canon-process-v3-paper-only-pilot-brief.md
       - Current owner instruction and Direction OS state outrank stale
         repository labels, old chat context and git-history process text.

     Reads:
       - live/indie-game-development/NOW.md
       - live/indie-game-development/CHARTER.md
       - live/indie-game-development/TREE.md
       - live/indie-game-development/work/
         canon-process-v3-paper-only-pilot-brief.md
       - the current Minimum Game Frame and exact question artifacts named by
         the active CALL
       - canon repository:
         CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md and directly relevant
         canon cards

     Hard boundaries:
       - Text only.
       - No Unity scene, greybox, prototype, visual probe, A/B build, setup,
         playtest, tuning or implementation of candidate variants.
       - No candidate generation before both FRAME READY and QUESTION READY.
       - A blocked gate stays on the same missing basis or question.
       - An OWNER-SELECTED PAPER ANSWER is not canon.
       - Canon admission requires a separate owner-present verdict on the exact
         existing paper artifact.
       - No design question is automatically selected from QUEUE.md.
       - No process or canon mutation occurs before the corresponding owner
         verdict.
       - A stale v2 file, old chat or git-history text has no live authority.

     Steps:
       1. Authority and scope:
          load the active CALL, current frame, process specification and current
          canon sources; state exactly what is and is not being decided.

       2. Gate F:
          establish or verify the current owner-readable Minimum Game Frame.
          Return FRAME READY, FRAME REVISED or FRAME BLOCKED with the owner's
          words recorded verbatim.

       3. Gate Q:
          for one sourced current question, establish frame location, exact
          unresolved player decision, provenance, why-now, blockers, entity
          meanings and non-scope. Return QUESTION READY or QUESTION BLOCKED with
          the owner's words recorded verbatim.

       4. Paper comparison:
          only after both gates pass, define local criteria and one shared
          imagined situation; generate privately, hard-kill weak directions,
          merge prose duplicates and show only 2–3 mechanically distinct,
          equally rendered paper candidates, or an honest BLOCKED result.

       5. Paper verdict:
          record the owner's exact paper-selection words. The resulting artifact
          is OWNER-SELECTED PAPER ANSWER and must name all unverified dimensions.
          It does not modify canon.

       6. Canon admission:
          run only as a separate owner-present CALL over one exact existing paper
          artifact. Allowed verdicts are ADMIT TO CANON, HOLD PAPER-ONLY or
          REJECT AS CANON CANDIDATE. No branch opens another design topic or
          implementation task.

       7. Close:
          emit one RESULT. The session never edits repositories directly.
          A writer applies only the owner-approved state/process/canon diff.

     Done when:
       The active CALL reaches its bounded owner verdict; paper authority and
       canon authority remain explicit and separate; no stale queue or process
       can auto-start; the RESULT cites every owner step verbatim.

     END_OF_FILE: live/indie-game-development/plays/canon-forge.md

     FILE_CONTENT_END

     Do not retain the previous v2 text in this file.

     Do not create canon-forge-v2.md, legacy-canon-forge.md or another
     superseded wrapper.

  ======================================================================
  C. PROMOTE THE ACCEPTED PILOT SPECIFICATION TO GOVERNING STATUS
  ======================================================================

  3. Edit:

     live/indie-game-development/work/
     canon-process-v3-paper-only-pilot-brief.md

     3.1 Replace the current status line with:

         status: ACTIVE PROCESS V3 — installed 2026-07-12 by owner verdict "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"; paper-only; owner-selected paper answers require separate canon admission

     3.2 Insert exactly once immediately before END_OF_FILE:

         ## Active-process installation — 2026-07-12

         owner_installation_verdict:
           "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

         owner_cleanup_instruction:
           "Прошлые можно удалить что бы не плодить legacy"

         governing_status: ACTIVE
         prior_process: Canon Forge v2 REMOVED FROM LIVE ROUTING
         evidence_mode: PAPER ONLY
         canon_transition: SEPARATE OWNER-PRESENT ADMISSION

         The completed revised pilot is the evidence basis for installation.
         The earlier process verdict "ACCEPTED" remains process-pilot evidence;
         installation authority comes from the separate 2026-07-12 owner
         verdict above.

         The former v2 process is not preserved as a live fallback, wrapper,
         queue, README instruction or legacy process copy. Its audit record
         remains recoverable from Direction OS history and git history.

         An OWNER-SELECTED PAPER ANSWER remains non-canon until a separate
         admission verdict names the exact artifact.

     3.3 Keep the completed-pilot evidence and pass/fail record already present
         in this file.

     3.4 Do not duplicate the specification into a second active-process file.

  ======================================================================
  D. REPLACE CANON-REPOSITORY LIVE ENTRYPOINTS IN PLACE
  ======================================================================

  4. In repository:

     github.com/ainazemtsau/gas_coop_game_canon

     replace the entire content of START.md with exactly:

     FILE_CONTENT_BEGIN

     # START — Canon Forge v3

     status: ACTIVE
     installed_on: 2026-07-12
     owner_verdict: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

     Canon Forge v3 is the sole active design-to-canon route.

     Кузница v2 is not a fallback and must not be started from git history,
     old chat context or removed queue text.

     Before any work, read:

     1. Direction OS:
        - live/indie-game-development/NOW.md
        - live/indie-game-development/plays/canon-forge.md
        - live/indie-game-development/work/
          canon-process-v3-paper-only-pilot-brief.md

     2. This canon repository:
        - CONSTITUTION.md
        - CORE.md
        - INDEX.md
        - QUEUE.md
        - SESSION.md
        - only the canon cards directly required by the active CALL

     The active route comes only from the exact current Direction OS CALL.

     QUEUE.md does not automatically select an old design question.

     An OWNER-SELECTED PAPER ANSWER is not canon.

     Canon admission requires a separate owner-present verdict on the exact
     existing artifact.

     Sessions do not write repositories directly. They end with one RESULT;
     a writer applies only the approved diff.

     END_OF_FILE: START.md

     FILE_CONTENT_END

  ----------------------------------------------------------------------
  D2. README.md — WRITER-BOUNCE CORRECTION
  ----------------------------------------------------------------------

  5. Replace the entire content of:

     github.com/ainazemtsau/gas_coop_game_canon/README.md

     in place with exactly:

     FILE_CONTENT_BEGIN

     # gas_coop_game_canon

     Канон игры «ОНО ДЫШИТ» — рабочее название — для направления
     `indie-game-development`.

     status: Canon Forge v3 ACTIVE
     installed_on: 2026-07-12
     owner_verdict: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

     ## Где живёт истина

     - Канон игры живёт в этом репозитории:
       `CONSTITUTION.md`, `CORE.md`, `INDEX.md` и карточки `canon/`.
     - Действующий design-to-canon процесс живёт в Direction OS:
       `live/indie-game-development/plays/canon-forge.md`.
     - Полная paper-only спецификация процесса:
       `live/indie-game-development/work/
       canon-process-v3-paper-only-pilot-brief.md`.
     - Кузница v2 удалена из живой маршрутизации и не является fallback.
     - Старый чат, удалённый текст или git history не создают действующий
       процесс.

     ## Как начать работу

     1. Прочитать `START.md`.
     2. Прочитать текущий Direction OS `NOW.md`, активный
        `local/canon-forge` и точный активный CALL.
     3. Прочитать `CONSTITUTION.md`, `CORE.md`, `INDEX.md`, `QUEUE.md`,
        `SESSION.md` и только непосредственно нужные канон-карточки.
     4. Выполнять только точный текущий CALL.

     Фраза владельца «продолжаем» или «что дальше» разрешается через текущий
     Direction OS state. Она не поднимает автоматически старый вопрос из
     `QUEUE.md`.

     ## Порядок Canon Forge v3

     1. Gate F — текущая Minimum Game Frame.
     2. Gate Q — происхождение, текущесть и границы одного точного вопроса.
     3. Только после `FRAME READY` и `QUESTION READY` — paper-only сравнение
        2–3 структурно разных кандидатов в одной общей ситуации.
     4. Дословный owner-verdict создаёт OWNER-SELECTED PAPER ANSWER.
     5. Paper answer остаётся неканоническим до отдельного owner-present
        canon-admission verdict.
     6. Допустимые admission-вердикты:
        `ADMIT TO CANON`, `HOLD PAPER-ONLY`,
        `REJECT AS CANON CANDIDATE`.

     Бумага не доказывает fun, runtime legibility, реальный co-op, pacing,
     engine feasibility или коммерческий результат.

     ## Текущее состояние

     Активного design-вопроса сейчас нет.

     По `q-investigation-readiness` существует точный
     OWNER-SELECTED PAPER ANSWER «Цель стоит запуска».

     Он не является каноном.

     Его единственный разрешённый следующий маршрут — отдельный Direction OS
     CALL:

     `c-research-q-investigation-readiness-canon-admission-001`

     Этот CALL не имеет права переписывать ответ, генерировать другой
     design-вопрос или открывать implementation.

     ## Файлы репозитория

     - `START.md` — вход и authority order.
     - `README.md` — краткая карта действующего процесса и репозитория.
     - `SESSION.md` — локальное зеркало маршрута v3; не второй источник
       процедуры.
     - `QUEUE.md` — только явно открытый текущим CALL маршрут; ничего не
       автостартует.
     - `CONSTITUTION.md` — верхние законы и фильтры канона.
     - `CORE.md` — owner-originated design anchors и их provenance.
     - `INDEX.md` — индекс отдельно допущенных канон-карточек.
     - `canon/` — канон-карточки.
     - `templates/card.md` — формат карточки.
     - `AMENDMENTS.md` — замены уже существующих канон-карточек.
     - `sources/`, `visuals/`, `assets/` и прочие материалы — evidence или
       production material, но не автоматический канон и не process authority.

     ## Запись

     Сессия не редактирует репозитории напрямую.

     Она завершает работу одним RESULT. Писатель применяет только точный
     owner-approved diff.

     END_OF_FILE: README.md

     FILE_CONTENT_END

     Do not preserve the former README v2 instructions below the replacement.

     Do not create README-v2.md, README-legacy.md or another process copy.

  ----------------------------------------------------------------------
  D3. SESSION.md
  ----------------------------------------------------------------------

  6. Replace the entire content of:

     github.com/ainazemtsau/gas_coop_game_canon/SESSION.md

     with exactly:

     FILE_CONTENT_BEGIN

     # Canon Forge v3 — session route

     status: ACTIVE
     installed_on: 2026-07-12

     The authoritative operating procedure is:

     - Direction OS:
       live/indie-game-development/plays/canon-forge.md
     - accepted paper-only specification:
       live/indie-game-development/work/
       canon-process-v3-paper-only-pilot-brief.md

     This file is the canon-repository entry mirror. It does not maintain a
     second divergent process copy.

     Mandatory order:

     0. Load the exact active CALL and current authority.
     1. Gate F — current Minimum Game Frame.
     2. Gate Q — sourced current question and why-now.
     3. Only after both gates pass: local criteria and one shared paper scene.
     4. Private generation, hard kills and structural deduplication.
     5. Show 2–3 equally rendered paper candidates or BLOCKED.
     6. Record the owner's exact paper verdict.
     7. Keep the result non-canon until a separate canon-admission verdict.
     8. End with one RESULT; no direct repository write.

     Stop conditions:

     - FRAME not ready;
     - QUESTION not ready;
     - undefined or untraceable entity;
     - candidate generation before both gates;
     - silent switch to another question;
     - claim that paper proves fun, runtime legibility or actual co-op;
     - attempted implementation or prototype work;
     - attempted canon change without separate owner admission;
     - attempted revival of removed Кузница v2 routing.

     END_OF_FILE: SESSION.md

     FILE_CONTENT_END

  ----------------------------------------------------------------------
  D4. QUEUE.md
  ----------------------------------------------------------------------

  7. Replace the entire content of:

     github.com/ainazemtsau/gas_coop_game_canon/QUEUE.md

     with exactly:

     FILE_CONTENT_BEGIN

     # QUEUE — Canon Forge v3

     status: NO ACTIVE DESIGN QUESTION
     governing_process: Canon Forge v3
     installed_on: 2026-07-12
     owner_verdict: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

     ## Current route

     No design question is active.

     q-investigation-readiness has one existing OWNER-SELECTED PAPER ANSWER:

     «Цель стоит запуска»

     It is not canon.

     Its only permitted next action is the separate Direction OS CALL:

     c-research-q-investigation-readiness-canon-admission-001

     That CALL may decide only:

     - ADMIT TO CANON;
     - HOLD PAPER-ONLY;
     - REJECT AS CANON CANDIDATE.

     It may not revise the answer, generate another question or open
     implementation.

     ## Removed live route

     The former core-0/core-1 and Кузница v2 sequential queue is removed from
     live routing.

     It is not retained below as a legacy section and cannot be automatically
     started.

     Relevant owner material remains recoverable from CORE.md, Direction OS
     history and git history.

     A future design question may be opened only by a new explicit Direction OS
     CALL under Canon Forge v3, beginning with Gate F and Gate Q.

     END_OF_FILE: QUEUE.md

     FILE_CONTENT_END

  ----------------------------------------------------------------------
  D5. INDEX.md — REMOVE THE REMAINING V2 ROUTING CLAIMS
  ----------------------------------------------------------------------

  8. Edit:

     github.com/ainazemtsau/gas_coop_game_canon/INDEX.md

     by exact replacement, preserving any fresh canon-card rows if concurrent
     state differs.

     8.1 Replace the exact line:

         (пока пусто — первая карточка появится из первой сессии Кузницы v2)

         with:

         (пока пусто — ни один owner-selected paper answer ещё не получил отдельный ADMIT TO CANON verdict)

     8.2 Replace the exact block:

         ## Legacy
         Старый канон (questions/*.md со status: frozen, maps/World.md, maps/StyleBible.md и история OS-репо) — СВИДЕТЕЛЬСТВА старого концепта, не закон: см. LEGACY.md. Переносится в новый канон только через сессию Кузницы v2.

         with:

         ## Historical evidence
         Старые questions/, maps/, материалы и история OS-репо — свидетельства, не текущий закон и не очередь. Они рассматриваются только когда точный активный CALL Canon Forge v3 прямо называет их источником; сами по себе они не входят в канон и не запускают работу.

     8.3 Preserve:

         - the `# INDEX` title;
         - the rule that past canon decisions are cited from INDEX/cards;
         - every fresh-current canon-card row, if any;
         - the existing END_OF_FILE marker.

     8.4 Do not create a separate legacy index.

  ----------------------------------------------------------------------
  D6. NO PARALLEL PROCESS COPIES
  ----------------------------------------------------------------------

  9. Do not create:

     - START-v2.md;
     - SESSION-v2.md;
     - QUEUE-v2.md;
     - README-v2.md;
     - README-legacy.md;
     - canon-forge-v2.md;
     - LEGACY-PROCESS.md;
     - any equivalent superseded process wrapper or duplicate v3
       specification.

  ----------------------------------------------------------------------
  D7. CANON BOARD RENDER
  ----------------------------------------------------------------------

  10. Regenerate only the process/status portions of:

      github.com/ainazemtsau/gas_coop_game_canon/board/dashboard.html

      Required visible truth:

      - Canon Forge v3: ACTIVE, installed 2026-07-12;
      - owner installation verdict:
        «УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС»;
      - Кузница v2: removed from live routing;
      - q-investigation-readiness:
        OWNER-SELECTED PAPER ANSWER, not canon;
      - separate canon admission: READY;
      - no active design question;
      - no core-0/core-1 live queue;
      - no text suggesting that «что дальше» automatically selects an old
        queue item.

      Do not change any game-design claim, canon pillar, owner anchor or visual
      design content in the board.

      Browser visual QA is not a prerequisite for this repair because the
      writer reported local file:// navigation blocked and all rejected
      uncommitted changes removed. The writer must still perform textual
      readback of the generated status statements before commit.

  ======================================================================
  E. EXPLICITLY UNCHANGED CANON AND DESIGN ARTIFACTS
  ======================================================================

  11. Leave unchanged:

      - github.com/ainazemtsau/gas_coop_game_canon/CONSTITUTION.md
      - github.com/ainazemtsau/gas_coop_game_canon/CORE.md
      - github.com/ainazemtsau/gas_coop_game_canon/templates/card.md
      - github.com/ainazemtsau/gas_coop_game_canon/AMENDMENTS.md
      - github.com/ainazemtsau/gas_coop_game_canon/canon/**
      - live/indie-game-development/work/
        q-investigation-readiness-paper-decision-v1.md
      - live/indie-game-development/TREE.md
      - live/indie-game-development/CHARTER.md
      - every product repository.

  12. Do not delete or rewrite:

      - live/indie-game-development/history/**
      - existing live/indie-game-development/LOG.md history lines
      - git history in either repository
      - owner statements
      - accepted design-anchor evidence.

      These are audit records, not executable legacy routes.

  ======================================================================
  F. SESSION RECORD
  ======================================================================

  13. Append exactly once before END_OF_FILE in:

      live/indie-game-development/LOG.md

      the line:

      2026-07-12 — repair/install (g-d3a8/canon-process, s-repair-canon-post-pilot-route-001): owner verdict «УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС» installed Canon Forge v3 as the sole paper-only design-to-canon route; owner also authorized deleting prior live process surfaces to avoid legacy, so Кузница v2 is replaced in place across OS play and canon START/README/SESSION/QUEUE, with stale v2 claims removed from the empty INDEX. q-investigation-readiness remains an owner-selected non-canon paper answer, and its separate admission CALL is reopened without ADMIT/HOLD/REJECT or any new design topic. → history/2026-07-12-s-repair-canon-post-pilot-route-001.md

  14. Create exactly once:

      live/indie-game-development/history/
      2026-07-12-s-repair-canon-post-pilot-route-001.md

      containing this full corrected RESULT verbatim.

      If the history path is absent, create it.

      If a byte-identical corrected RESULT already exists, no-op.

      A different file at this path is a semantic collision and must bounce
      rather than overwrite.

  ======================================================================
  G. SYSTEMIC FRICTION
  ======================================================================

  15. Append exactly once before END_OF_FILE in:

      os/FRICTION.md

      the line:

      2026-07-12 indie-game-development repair: an owner-evaluated process pilot could finish ACCEPTED without a mandatory post-pilot authority transition — install the candidate, resume the prior process, authorize an explicit one-shot bridge, or remain blocked — so a downstream canon-admission CALL opened while no governing design-to-canon process existed.

  16. This repair does not modify KERNEL.md or repair.md.

      The friction entry is evidence for a future maintenance decision; no OS
      rule is changed in this direction session.

  ======================================================================
  H. WRITER READBACK / COMPLETENESS GATE
  ======================================================================

  17. Before committing, the writer must read back current fresh versions of:

      Direction OS:
      - live/indie-game-development/NOW.md
      - live/indie-game-development/plays/canon-forge.md
      - live/indie-game-development/work/
        canon-process-v3-paper-only-pilot-brief.md

      Canon repository:
      - START.md
      - README.md
      - SESSION.md
      - QUEUE.md
      - INDEX.md
      - board/dashboard.html

  18. The writer must reject rather than commit if any live file still says or
      implies any of the following:

      - Кузница v2 is the active process;
      - a new chat should launch Кузница v2;
      - core-0/core-1/core-1…core-10 is the live automatic queue;
      - «что дальше» automatically selects a question from the old queue;
      - q-investigation-readiness-paper-decision-v1 is already canon;
      - "ACCEPTED" alone installed v3;
      - this repair issued ADMIT/HOLD/REJECT;
      - another design question or implementation task is now active.

  19. Preserve unrelated concurrent modifications byte-for-byte and apply by
      stable semantic fields/paths rather than by overwriting fresh unrelated
      state.

captures: []

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — exactly two owner-readable lines stated that the canon repo still launched v2 despite higher-authority suspension, while v3 was accepted-but-uninstalled and admission had no governing process.
  - 2 Reconstruct: done — v2 suspension, one-pilot mandate, corrected pilot, process-only "ACCEPTED", non-canon paper answer and premature admission routing were reconstructed from current artifacts and commits.
  - 3 Propose corrected state: done — v2 removed from live routing; v3 active; paper answer non-canon; admission separate; exact next governing route shown.
  - 4 Confirm: done — owner installation verdict cited verbatim: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС". Owner cleanup authorization also cited verbatim: "Прошлые можно удалить что бы не плодить legacy".
  - 5 Friction: done — one precise post-pilot authority-transition gap is appended to os/FRICTION.md; no OS rule is modified.
  - Writer bounce: done — current README.md was read first-hand; its executable v2 route is now covered by an exact in-place replacement, and the full RESULT is reissued from the writer-reported clean repositories.

log: |
  repair/install g-d3a8: owner installed Canon Forge v3 as the sole active
  paper-only design-to-canon process; corrected writer bounce additionally
  replaces the omitted executable v2 README and removes the empty INDEX's stale
  v2 routing claims. The selected paper answer remains non-canon and only its
  separate admission decision is reopened.

next: |
  Reopen the existing CALL:

  c-research-q-investigation-readiness-canon-admission-001

  Source:

  live/indie-game-development/work/
  c-research-q-investigation-readiness-canon-admission-001-call.md

  Governing process:

  local/canon-forge — Canon Forge v3

  Scope:

  Decide only one of:

  - ADMIT TO CANON;
  - HOLD PAPER-ONLY;
  - REJECT AS CANON CANDIDATE;

  for the exact existing artifact:

  live/indie-game-development/work/
  q-investigation-readiness-paper-decision-v1.md

  Prohibited:

  - revising or reinterpreting «Цель стоит запуска»;
  - generating another design question;
  - designing detection, activation, extraction, Bubble, damage, economy,
    inventory, UI or co-op roles;
  - opening prototype, playtest or implementation work;
  - treating the process installation verdict as canon admission.

END_OF_FILE: live/indie-game-development/history/2026-07-12-s-repair-canon-post-pilot-route-001.md
