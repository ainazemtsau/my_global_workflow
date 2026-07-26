RESULT s-repair-canon-frame-v2-eight-player-001 (call: c-repair-canon-frame-v2-eight-player-001)
direction: indie-game-development   play: repair   node/task: g-d3a8

outcome: |
  Владелец дословно одобрил ограниченную поправку верхнего закона канона:
  «ОДОБРЯЮ КАНОН-ПОПРАВКУ».

  После применения этого RESULT mechanical writer:

  - действующий столп 1 больше не задаёт "1–4" как максимум и не требует
    solo-startable;
  - действующий canon-law содержит только принятое направление состава:
    меняющиеся группы 4–8 — основной текущий диапазон; поддержка полной
    восьмёрки обязательна; точный нижний предел ниже четырёх OPEN; соло не
    является текущей дизайн-целью;
  - прежняя формулировка сохраняется в AMENDMENTS.md как исторически
    заменённая норма, а не параллельный активный закон;
  - Minimum Game Frame v2 целиком не становится каноном;
  - CORE.md, INDEX.md, c-001 и все остальные карточки остаются без изменений;
  - c-repair-eight-player-live-consistency-sweep-001 становится
    READY PARALLEL;
  - c-research-q-coop-interdependence-002 остаётся
    READY PARALLEL / PAPER-ONLY;
  - c-shape-sc-damage-001 остаётся HELD.

evidence: |
  1. Owner verdict in this session, verbatim:
     «ОДОБРЯЮ КАНОН-ПОПРАВКУ»

  2. Fresh current canon bases:
     - gas_coop_game_canon/CONSTITUTION.md
       SHA: 705e8bbf76766ec9492e84644fe3715cd4f3e000
       Active pillar 1 still reads:
       "1–4 игрока, соло-стартуемо, но петля не соло-оптимальна."
     - gas_coop_game_canon/AMENDMENTS.md
       SHA: 5a57dc75b9b854c6895e9b0bb57841bbbcf7c9dc
       Current journal is empty.

  3. Accepted higher/current design authority:
     - live/indie-game-development/work/minimum-game-frame-v2.md
       SHA: 680b93582249336d4ac31629574bed15bc5f2bed
       status: FRAME READY
       authority: current owner-approved whole-game design basis; not canon
       accepted composition direction:
       changing 4–8-player groups are the primary current range;
       eight-player support is mandatory;
       the lower bound below four is OPEN;
       solo is not a current design target.
     - live/indie-game-development/knowledge/
       g9c41-players-8-owner-requirement.md
       SHA: d82f2cc6cd6b60e8fdd755fc5da92d3a2c4ed9c8
       contains the owner's binding eight-player requirement and explicit
       statement that solo is outside present design competence.

  4. Canon lineage:
     - commit 715727c854db9fbfab9b156f5114a52371d52f1b introduced the
       Constitution with the "1–4 / solo-startable" wording;
     - commit 87a05a733444f6eabb3a72d2c11f545f49e71f2c ratified the
       Constitution while leaving pillar 1 unchanged;
     - commit 324a30ed3726a73c44751b37aae35609f39007f1 admitted c-001 and
       updated INDEX, but did not repair pillar 1;
     - therefore this is an explicit top-law amendment, not a card rewrite.

  5. Exact no-change canon bases:
     - CORE.md SHA:
       c2fe9c3dc156b91d1f684d490e04d9ea4c85f1b2
     - INDEX.md SHA:
       f1e793c8a9ef94e47f8dd65f211c21a6cbcba47b
     - canon/c-001-investigation-readiness.md SHA:
       65a0b69cb6c662dd83d2482890f1fe003a57e2aa
     - c-001 explicitly leaves co-op roles, Bubble behavior, damage,
       economy, progression, networking and implementation outside scope.

  6. Current routing base:
     - live/indie-game-development/NOW.md
       SHA: fe68202a4e4be4f0d7958429aec8ae8c0cb13361
     - c-repair-canon-frame-v2-eight-player-001 is currently READY;
     - c-repair-eight-player-live-consistency-sweep-001 is currently HELD
       until this repair closes;
     - c-research-q-coop-interdependence-002 is READY PARALLEL / PAPER-ONLY;
     - c-shape-sc-damage-001 is HELD.

  7. Done-when coverage:
     - contradiction stated: exact active top-law text versus accepted
       Frame-v2/eight-player direction;
     - exact canon-law and amendment diff shown before approval;
     - explicit approval obtained verbatim;
     - postconditions remove active four-player maximum and solo-startable
       requirement;
     - only the four accepted player-count statements enter current law;
     - no unresolved mechanics or whole Frame v2 are canonized;
     - c-001 and unrelated canon content are preserved;
     - consistency sweep is released to READY only on application;
     - owner verdict is preserved verbatim in this RESULT.

state_changes: |
  1. Canon repository — amend exactly one Constitution pillar.

     repository:
       ainazemtsau/gas_coop_game_canon

     path:
       CONSTITUTION.md

     base_sha:
       705e8bbf76766ec9492e84644fe3715cd4f3e000

     operations:

       a. Immediately after the existing status line:

          Статус: РАТИФИЦИРОВАНА владельцем 2026-07-09 — вердикт «Б» (= ратифицировать с правками П1–П3) в сессии-картографии c-cartography-core-concept-rebuild-001.

          insert exactly:

          Поправки: 2026-07-15 — столп 1 (состав группы); история замены и дословный вердикт владельца — `AMENDMENTS.md`.

       b. Replace exactly:

          1. **Кооп-первый.** 1–4 игрока, соло-стартуемо, но петля не соло-оптимальна. Роли рождаются из рук, не из меню.

          with exactly:

          1. **Кооп-первый.** Игра проектируется прежде всего для меняющейся группы 4–8 игроков. Поддержка полной группы из восьми — жёсткое требование. Точный нижний поддерживаемый предел ниже четырёх остаётся OPEN. Соло не является текущей дизайн-целью. Роли рождаются из рук, не из меню.

     preserve:
       - all other Constitution text;
       - pillars 2–7;
       - palette and canon-process rules;
       - END_OF_FILE: CONSTITUTION.md.

     postconditions:
       - active Constitution text contains no "1–4 игрока";
       - active Constitution text contains no "соло-стартуемо";
       - pillar 1 retains "Роли рождаются из рук, не из меню";
       - pillar 1 states all and only the accepted player-count direction;
       - no mechanics, scaling formula or lower bound below four is selected;
       - the file retains exactly one END_OF_FILE marker.

  2. Canon repository — install the explicit constitutional
     amendment/supersession trail.

     repository:
       ainazemtsau/gas_coop_game_canon

     path:
       AMENDMENTS.md

     base_sha:
       5a57dc75b9b854c6895e9b0bb57841bbbcf7c9dc

     operation:
       Replace the complete current file with exactly:

       # AMENDMENTS — журнал поправок конституции и замен карточек

       ## Поправки конституции

       - **2026-07-15 · `CONSTITUTION.md` · столп 1**
         - Прежняя активная норма — **ЗАМЕНЕНА; больше не действует**: «1–4 игрока, соло-стартуемо, но петля не соло-оптимальна».
         - Текущая активная норма: «Игра проектируется прежде всего для меняющейся группы 4–8 игроков. Поддержка полной группы из восьми — жёсткое требование. Точный нижний поддерживаемый предел ниже четырёх остаётся OPEN. Соло не является текущей дизайн-целью. Роли рождаются из рук, не из меню.»
         - Основание: owner-present repair `c-repair-canon-frame-v2-eight-player-001`; вердикт владельца: «ОДОБРЯЮ КАНОН-ПОПРАВКУ». Поправка согласует только принятое направление по составу группы из `Minimum Game Frame v2` и обязательное требование поддержки восьми; Frame v2 целиком в канон не принят.
         - Затронутые карточки: нет; `c-001` без изменений.

       ## Замены карточек

       Формат строки: дата — c-YYY заменяет c-XXX — причина одной фразой — задетые дети (id, перепроверяются в свои сессии).

       (пусто)

       END_OF_FILE: AMENDMENTS.md

     postconditions:
       - the old wording remains recoverable as historical provenance;
       - it is explicitly marked replaced and non-active;
       - the exact owner verdict is present verbatim;
       - no card replacement is invented;
       - the file retains exactly one END_OF_FILE marker.

  3. Canon repository — explicit no-change surfaces.

     Preserve after semantic rebase:

       - CORE.md
       - INDEX.md
       - canon/c-001-investigation-readiness.md
       - every other canon card and canon entrypoint
       - QUEUE.md, SESSION.md, board output and process files
       - all historical/source material

     In particular:

       - do not create a new canon card;
       - do not stamp c-001 as replaced;
       - do not expand c-001;
       - do not import Minimum Game Frame v2 wholesale;
       - do not modify Bubble, roles, anti-solo mechanics, scaling, lower
         bound, join/leave, networking, damage, economy or progression.

  4. Direction repository — close the completed repair CALL and release the
     existing consistency sweep.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/NOW.md

     base_sha:
       fe68202a4e4be4f0d7958429aec8ae8c0cb13361

     operations:

       a. Set the header marker to:

          updated: 2026-07-15 by s-repair-canon-frame-v2-eight-player-001

       b. Remove the complete open_calls entry with stable id:

          c-repair-canon-frame-v2-eight-player-001

       c. Preserve all fields of the existing open_calls entry
          c-repair-eight-player-live-consistency-sweep-001, but replace its
          note with exactly:

          note: |
            READY PARALLEL / SECOND g-d3a8 CONSISTENCY PHASE:
            c-repair-canon-frame-v2-eight-player-001 closed owner-approved
            with verdict «ОДОБРЯЮ КАНОН-ПОПРАВКУ». Current canon top law now
            uses the accepted 4–8 / mandatory-eight / lower-bound-OPEN /
            no-current-solo-target direction, with the old wording preserved
            only in AMENDMENTS.md.
            Scan current authoritative/live surfaces for stale "1–4",
            "2–4", "solo-startable" and equivalent meanings; classify each
            as correct-now, engineering hygiene, parked/deferred or
            historical evidence, and propose only minimal owner-approved
            corrections. Never rewrite history.
            Read the completed repair RESULT:
            history/2026-07-15-s-repair-canon-frame-v2-eight-player-001.md.
            Full CALL definition remains preserved in:
            history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md.

       d. Preserve open_calls[id=c-research-q-coop-interdependence-002]
          unchanged as READY PARALLEL / PAPER-ONLY.

       e. Preserve open_calls[id=c-shape-sc-damage-001] unchanged and HELD.

       f. Preserve all tasks, bet data, recurring entries, decisions,
          unrelated open_calls and the current direction-level NOW.next after
          semantic rebase.

     postconditions:
       - c-repair-canon-frame-v2-eight-player-001 no longer appears in
         open_calls;
       - c-repair-eight-player-live-consistency-sweep-001 appears exactly
         once and is unambiguously READY PARALLEL;
       - the engineering PRIMARY route and NOW.next remain unchanged;
       - no new active task or second active bet is created;
       - NOW.md retains its END_OF_FILE marker.

  5. Direction repository — append one LOG line.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/LOG.md

     base_sha:
       53fabca64dcf2345bd93eb1454cc09613b5bd00b

     append immediately before the END_OF_FILE marker:

       2026-07-15 — repair/close (g-d3a8/c-repair-canon-frame-v2-eight-player-001, s-repair-canon-frame-v2-eight-player-001): owner «ОДОБРЯЮ КАНОН-ПОПРАВКУ» approved the bounded canon top-law correction — active "1–4 / solo-startable" is superseded by changing 4–8 groups, mandatory eight support, OPEN lower bound below four and no current solo target; amendment trail explicit, Frame v2 not canonized wholesale, c-001/unrelated canon unchanged, live consistency sweep READY PARALLEL, co-op paper research still READY and Sc-damage HELD. → history/2026-07-15-s-repair-canon-frame-v2-eight-player-001.md

     postconditions:
       - append exactly one new session line;
       - preserve all existing LOG entries and archive pointer;
       - retain exactly one END_OF_FILE marker.

  6. Direction repository — save this complete RESULT verbatim.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/history/
       2026-07-15-s-repair-canon-frame-v2-eight-player-001.md

     operation:
       Create the file containing this complete RESULT verbatim, followed by:

       END_OF_FILE: live/indie-game-development/history/2026-07-15-s-repair-canon-frame-v2-eight-player-001.md

     postconditions:
       - owner verdict appears verbatim;
       - exact canon diffs and no-change surfaces are recoverable;
       - the file ends with the exact END_OF_FILE marker above.

  7. Explicit no-change Direction and product surfaces.

     Preserve unchanged after semantic rebase:

       - live/indie-game-development/TREE.md
       - live/indie-game-development/CHARTER.md
       - live/indie-game-development/work/minimum-game-frame-v2.md
       - live/indie-game-development/knowledge/
         g9c41-players-8-owner-requirement.md
       - every unrelated NOW route
       - product repositories and implementation
       - historical RESULTs, archives and source evidence
       - the uploaded q-floor-loop transcript

  8. Writer verification and commit boundaries.

     a. In gas_coop_game_canon:
        - apply only CONSTITUTION.md and AMENDMENTS.md changes above;
        - read both files back from the resulting commit;
        - verify no other path changed;
        - suggested commit message:
          canon: reconcile co-op pillar with mandatory eight-player direction

     b. In my_global_workflow:
        - apply only NOW.md, LOG.md and the new history RESULT;
        - read them back from the resulting commit;
        - verify TREE.md, CHARTER.md and direction-level NOW.next unchanged;
        - suggested commit message:
          repair: close canon eight-player reconciliation

     c. The consistency sweep becomes runnable only after both repository
        commits and readbacks satisfy these postconditions.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — active canon pillar 1 says «1–4 игрока, соло-стартуемо», while current owner-approved Frame direction requires primary changing 4–8 groups, mandatory support for eight, an OPEN lower bound below four and no current solo design target."
  - "2 Reconstruct: done — newest-first reconstruction used current canon blobs, Frame v2, the owner-requirement knowledge file, current NOW routing and canon commits 715727c / 87a05a7 / 324a30e; the old wording was introduced and ratified before the later player-count direction, while c-001 never repaired or owned this issue."
  - "3 Propose corrected state: done — exact bounded diffs were shown for CONSTITUTION.md and AMENDMENTS.md; impact/non-impact map preserved Frame-v2/canon separation, c-001 and unrelated content."
  - "4 Confirm (owner): done — owner verdict verbatim: «ОДОБРЯЮ КАНОН-ПОПРАВКУ»."
  - "5 Friction: skipped — this was an explicit staged authority reconciliation after a newer owner direction, already routed by the prior map session; no recurring OS mechanism failure or second repair of the same state seam was established."

log: "repair/close g-d3a8 canon law: owner «ОДОБРЯЮ КАНОН-ПОПРАВКУ» approved the exact eight-player top-law amendment and supersession trail; Frame v2 remains non-canon as a whole, c-001/unrelated canon stay unchanged, and the live consistency sweep is released READY PARALLEL."

next: |
  BRANCH CONTINUATION — READY PARALLEL after writer application and readback.
  This existing CALL does not replace the current direction-level NOW.next.

  CALL c-repair-eight-player-live-consistency-sweep-001
  to: session
  direction: indie-game-development
  play: repair
  node: g-d3a8
  surface: any
  parent: s-map-g-d3a8-frame-v2-reconciliation-001

  goal: |
    Every current authoritative/live surface either reflects accepted
    Frame v2 and mandatory support for eight players or has an explicit,
    evidence-backed disposition, without rewriting historical evidence
    or unrelated branches.

  context: |
    Run only after the writer has applied and read back:
    - gas_coop_game_canon changes from
      live/indie-game-development/history/
      2026-07-15-s-repair-canon-frame-v2-eight-player-001.md;
    - the corresponding Direction-state close.

    Read:
    - live/indie-game-development/NOW.md
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - live/indie-game-development/work/minimum-game-frame-v2.md
    - live/indie-game-development/knowledge/
      g9c41-players-8-owner-requirement.md
    - live/indie-game-development/history/
      2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
    - live/indie-game-development/history/
      2026-07-15-s-repair-canon-frame-v2-eight-player-001.md
    - current gas_coop_game_canon entrypoints and canon index
    - current live work/CALL surfaces whose wording makes an active
      player-count or solo-support claim.

    Search current authoritative/live material for:
    - "1–4"
    - "2–4"
    - "solo-startable"
    - equivalent claims that make four the maximum or solo a current
      design target.

    Historical RESULTs, archived sources and superseded evidence are
    provenance, not active text to rewrite.

  boundaries: |
    Owner-present, text only.
    Do not generate mechanics, roles, scaling formulas, networking
    design, Bubble controls, damage or implementation.
    Do not reopen Frame v2 or the mandatory eight-player requirement.
    Do not rewrite history, archives or old evidence.
    Do not silently change TREE: every TREE correction requires the
    owner's explicit in-session G9 approval.
    Do not alter unrelated goals merely to normalize wording.
    Preserve a clean one-player engine test when it is explicitly
    engineering hygiene rather than a promised solo game mode.
    Parked commercial/demo wording may be deferred with an explicit
    owner-readable reason rather than prematurely redesigned.

  done_when: |
    1. A complete current-authority occurrence list exists.
    2. Every occurrence is classified as one of:
       - correct now;
       - minimal correction required;
       - engineering hygiene, not a design promise;
       - parked/deferred until its branch wakes;
       - historical evidence, no edit.
    3. Exact minimal corrections are shown together and the owner
       explicitly approves them or blocks them.
    4. No historical evidence or unrelated branch is rewritten.
    5. Current live state has no unclassified contradiction with Frame v2
       or mandatory eight-player support.
    6. Any remaining deferred item names its wake condition and owner.

  return: |
    Short Russian consistency brief;
    occurrence/disposition table;
    exact minimal diffs;
    verbatim owner verdict;
    one RESULT.

  budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/history/2026-07-15-s-repair-canon-frame-v2-eight-player-001.md

