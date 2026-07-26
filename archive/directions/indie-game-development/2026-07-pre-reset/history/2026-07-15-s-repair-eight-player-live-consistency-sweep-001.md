RESULT s-repair-eight-player-live-consistency-sweep-001 (call: c-repair-eight-player-live-consistency-sweep-001)
direction: indie-game-development   play: repair   node/task: g-d3a8

owner_approved: |
  2026-07-15 — владелец дословно:

  «ОДОБРЯЮ ПАКЕТ CONSISTENCY-ПОПРАВОК, включая G9-правки TREE
  g-9c41 и g-5b07, правку нормативной knowledge-расшифровки,
  player-count/Frame-v2 правки canon-board и синхронизацию
  review-render; историю не менять.»

  Этот вердикт является явным in-session G9-разрешением на две
  перечисленные ниже TREE-операции и одобрением всего bounded пакета.

outcome: |
  Существует полный, owner-approved и mechanically applicable пакет
  текущей eight-player consistency-коррекции.

  Пакет классифицирует все найденные current-authority/live вхождения
  player-count и solo-support утверждений и после применения оставляет
  одну текущую норму:

  - меняющиеся группы 4–8 игроков — основной текущий диапазон;
  - поддержка полной восьмёрки обязательна;
  - точный поддерживаемый нижний предел ниже четырёх остаётся OPEN;
  - соло не является текущей дизайн-целью.

  Две TREE-коррекции явно одобрены по G9:

  1. g-9c41 больше не задаёт четыре как текущий максимум;
  2. g-5b07 сохраняет старое demo wording только как PARKED / DEFERRED
     обязательство с явными owner и wake condition, без преждевременного
     редизайна демо.

  Clean 1-player engine session, 2+ clients, two-machine evidence и
  two-human mechanic grey-box сохраняются как engineering/test hygiene,
  а не как продуктовые обещания solo mode или максимального состава.

  Current canon law не меняется: он уже соответствует Frame v2.
  Исправляется только его stale owner-facing render. Исторические
  evidence, архивы, прежние RESULT, AMENDMENTS, canon cards, CHARTER,
  product repositories и unrelated branches не переписываются.

evidence: |
  A. Preconditions and current authority

  1. Canon and Direction prerequisite publication is complete:

     - canon commit:
       8527af9d6e36fdfac4dfda53c50e3020f657ec77
       "canon: reconcile co-op pillar with mandatory eight-player direction";

     - workflow Direction repair payload:
       7b944866dd069eda72bd50c9340a095cdd1e83b0;

     - publication RESULT:
       live/indie-game-development/history/
       2026-07-15-s-work-publish-canon-eight-player-main-001.md.

  2. Whole-game frame:

     - path:
       live/indie-game-development/work/minimum-game-frame-v2.md
     - fetched SHA:
       680b93582249336d4ac31629574bed15bc5f2bed
     - status:
       FRAME READY
     - authority:
       current owner-approved whole-game design basis; not canon
     - current composition:
       changing 4–8-player groups; full eight mandatory; exact lower bound
       below four OPEN; solo not a current design target.

  3. Current TREE design branch:

     - path:
       live/indie-game-development/TREE.md
     - fetched SHA:
       3ccf9e3529f1c41140c77d888aa30fd603038e6b
     - g-d3a8 already states the exact Frame-v2 player-count direction.

  4. Current canon top law:

     - repository:
       ainazemtsau/gas_coop_game_canon
     - path:
       CONSTITUTION.md
     - fetched SHA:
       4ef650a71a658a0b23c688047f711057afaddbab
     - pillar 1 already states the exact current direction.

  5. Binding owner-requirement evidence:

     - path:
       live/indie-game-development/knowledge/
       g9c41-players-8-owner-requirement.md
     - fetched SHA:
       d82f2cc6cd6b60e8fdd755fc5da92d3a2c4ed9c8
     - the owner quote is preserved verbatim and is not edited.

  B. Complete occurrence and disposition list

  | Current surface / occurrence | Classification | Disposition |
  |---|---|---|
  | `work/minimum-game-frame-v2.md`: 4–8, mandatory eight, lower bound OPEN, solo not target | correct now | Preserve unchanged. |
  | `TREE.md` g-d3a8 goal/done_when/detail: same current norm | correct now | Preserve substantive player-count text unchanged. |
  | `gas_coop_game_canon/CONSTITUTION.md` pillar 1 | correct now | Preserve canon law unchanged. |
  | Canon `CORE.md`, `INDEX.md`, `README.md`, `START.md`, `QUEUE.md`, `SESSION.md`, current c-001 | correct now / no active count claim | No player-count edit. Admission/process drift remains outside this bounded repair except where the board finding is narrowed. |
  | `NOW.md` co-op research and consistency routing | correct now | Remove only this completed sweep call; preserve all unrelated routes. |
  | `TREE.md` g-9c41 goal: `2–4 players` | minimal correction required | Replace only the player-count clause through owner-approved G9. Do not consolidate the rest of the old architecture palimpsest. |
  | `TREE.md` g-9c41 criterion 11: `4–8 co-op session` | correct now | Preserve unchanged. |
  | `TREE.md` g-9c41 criterion 7: clean `1-player session`, player count config | engineering hygiene, not a design promise | Preserve unchanged. |
  | `TREE.md` g-9c41 `2+ networked clients` | engineering hygiene, not a design promise | Preserve as minimum synchronization evidence, not a maximum. |
  | M1 shape/route/current evidence: same scenario on two real machines | engineering hygiene, not a design promise | Preserve as a lower evidence threshold; it does not discharge the later eight-peer requirement. |
  | `knowledge/g9c41-gas-engine-SPEC.md`: visible S0 proof with one player | engineering hygiene, not a design promise | Preserve unchanged. |
  | `knowledge/mechanic-lenses.md`: two-human grey-box | engineering/test hygiene, not a supported-range claim | Preserve unchanged; it tests one mechanic and cannot certify eight-player value. |
  | TREE root `solo-developed`; CHARTER `solo developer` / `solo-shippable`; g-6d4e `Solo-maintainable`; NOW `solo-scope` | engineering/production hygiene | Preserve unchanged; these describe team size or maintainability. |
  | `knowledge/g9c41-players-8-owner-requirement.md` normative claim `design optimum = 8` and `2–7 work parametrically` | minimal correction required | Align normative interpretation with Frame v2; do not promise 2–3 or reduce the primary range to only eight. |
  | The same knowledge file’s verbatim owner quote | historical/decision evidence, no edit | Preserve exactly. |
  | The same knowledge file’s dated `grep 2026-07-11` list containing old 2–4 / 1–4 / solo-startable text | historical evidence, no edit | Preserve as a dated pre-repair occurrence snapshot. |
  | `TREE.md` g-5b07 `solo-startable co-op demo` in goal/done_when, status parked | parked/deferred until branch wakes | Preserve wording; add explicit non-current disposition, wake condition and owner. |
  | `gas_coop_game_canon/board/dashboard.html`: current-looking Frame v1 / 1–4 / solo-startable render | minimal correction required | Show current Frame-v2/pillar-1 norm and explicitly label detailed Frame-v1 map/matrix as superseded render. Do not change canon law. |
  | `work/review/findings.md` dr-20260712-002 still `in-fix` | minimal correction required | Close as fixed by this package. |
  | `work/review/findings.md` dr-20260711-004 mixes player-count drift with separate admission-render drift | minimal correction required | Mark player-count half disposed; retain only admission/render remainder under the existing ID. |
  | Direction `work/board/dashboard.html`: open sweep card and stale player-count problem cards | minimal correction required | Regenerate only named cards/stamps/journal from repaired state. |
  | `AMENDMENTS.md`: old `1–4 / solo-startable` wording explicitly replaced | historical evidence, no edit | Preserve as required supersession trail. |
  | Frame v1, dated pitches, old audits, old work snapshots, LOG/history RESULTs and archive material containing 1–4/2–4/solo-startable | historical evidence, no edit | Do not rewrite. |
  | Uploaded `Indie Game Development.txt` transcript | prior-chat material, not authority | No state change is based on it. |

  C. Owner verdict

  Verbatim:

  «ОДОБРЯЮ ПАКЕТ CONSISTENCY-ПОПРАВОК, включая G9-правки TREE
  g-9c41 и g-5b07, правку нормативной knowledge-расшифровки,
  player-count/Frame-v2 правки canon-board и синхронизацию
  review-render; историю не менять.»

  D. Done-when coverage

  1. Complete current-authority occurrence list:
     covered by section B.

  2. Every occurrence classified:
     correct now; minimal correction required; engineering hygiene;
     parked/deferred; or historical evidence.

  3. Exact minimal corrections shown together and approved:
     all operations below were shown as one package and approved verbatim.

  4. Historical evidence and unrelated branches:
     explicit preserve list is included below.

  5. No unclassified current player-count contradiction after apply:
     g-9c41, knowledge normative text, owner-facing boards and findings
     will align with Frame v2 and current canon.

  6. Deferred item names wake condition and owner:
     g-5b07 detail operation below does both.

state_changes: |
  1. Knowledge — repair only the normative interpretation.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/knowledge/
       g9c41-players-8-owner-requirement.md

     fetched_base_sha:
       d82f2cc6cd6b60e8fdd755fc5da92d3a2c4ed9c8

     stable_target:
       section `## Нормативная расшифровка`

     operation_a — replace exactly:

       - Игра поддерживает **до 8 игроков включительно**; дизайн-оптимум и целевой опыт = **полная группа из 8** (владельческая компания — и она же готовая плейтест-группа).

     with exactly:

       - Игра проектируется прежде всего для меняющейся группы **4–8 игроков**; поддержка полной группы из **8** — жёсткое требование (владельческая компания — и она же готовая плейтест-группа).

     operation_b — preserve exactly:

       - **Соло — вне компетенции сейчас**: не проектируем, не оптимизируем, не сертифицируем. (Инженерный критерий «чистая 1-player сессия, player count = config» из TREE #7 остаётся как гигиена движка, не как игровой режим.)

     operation_c — replace exactly:

       - Меньшие составы (2–7) работают параметрически, но не являются дизайн-целью.

     with exactly:

       - Составы **4–7** входят в основной меняющийся диапазон. Точный поддерживаемый нижний предел ниже четырёх остаётся **OPEN**; эта запись не обещает поддержку 2–3 игроков.

     preserve:
       - the complete verbatim owner quote;
       - the complete dated `grep 2026-07-11` section;
       - all engineering consequence text;
       - exact END_OF_FILE marker.

  2. TREE — g-9c41 player-count correction, owner-approved G9.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/TREE.md

     fetched_base_sha:
       3ccf9e3529f1c41140c77d888aa30fd603038e6b

     stable_target:
       root.children[id=g-9c41].goal

     owner_approval:
       exact verdict in this RESULT; explicitly names `G9-правки TREE g-9c41`.

     replace exactly:

       A representative networked co-op scene runs and holds, on a core architected for
       huge procedural levels: 2–4 players on a player-hosted session (one player hosts; no
       dedicated server), host-authoritative multi-gas simulation on sector-band grid/room

     with exactly:

       A representative networked co-op scene runs and holds, on a core architected for
       huge procedural levels: changing 4–8-player groups on a player-hosted session
       (one player hosts; no dedicated server), with mandatory support for the full group
       of eight, the exact supported lower bound below four OPEN, and solo not a current
       design target; host-authoritative multi-gas simulation on sector-band grid/room

     preserve:
       - all following g-9c41 goal text;
       - all g-9c41 done_when criteria, including clean 1-player criterion 7;
       - current supersession/consolidation notes;
       - every other g-9c41 architecture statement;
       - sibling nodes;
       - root.map_order;
       - END_OF_FILE.

     postconditions:
       - current g-9c41 goal no longer contains `2–4 players`;
       - it does not select a lower bound below four;
       - it does not convert the 1-player engine check into a game mode;
       - no unrelated architecture consolidation is performed.

  3. TREE — g-5b07 parked/deferred disposition, owner-approved G9.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/TREE.md

     stable_target:
       root.children[id=g-5b07].detail

     owner_approval:
       exact verdict in this RESULT; explicitly names `G9-правки TREE g-5b07`.

     replace exactly:

       detail: history/s-map-002.md

     with exactly:

       detail: |
         history/s-map-002.md

         Player-count disposition (2026-07-15): PARKED / DEFERRED.
         The preserved “solo-startable” demo wording is not a current
         design target and is not an active implementation or storefront
         promise.

         Wake condition: before g-5b07 changes from parked, before demo
         or storefront scope or public copy is accepted, or before a
         related PLAN or BUILD is issued, an owner-present g-5b07
         frame/shape/review must reconcile the demo promise with Minimum
         Game Frame v2 and mandatory support for eight players.

         Owner: the direction owner through the first owner-present
         g-5b07 frame/shape/review that wakes this branch.

     preserve:
       - g-5b07 goal;
       - g-5b07 done_when;
       - status: parked;
       - all dates, commercial gates and unrelated wording;
       - sibling nodes and END_OF_FILE.

     postconditions:
       - old demo wording remains visible as a deferred obligation;
       - it cannot be read as a current design target or runnable promise;
       - wake condition and owner are explicit;
       - no demo design, scaling rule or implementation is invented.

  4. Canon repository — correct only the current player-count/frame render.

     repository:
       ainazemtsau/gas_coop_game_canon

     path:
       board/dashboard.html

     fetched_base_sha:
       51096f0b97bf80f6d6671cd0012f6098121eddc9

     operation_a — replace the header eyebrow:

       ОНО ДЫШИТ · канон-борд · сгенерировано 2026-07-12

     with:

       ОНО ДЫШИТ · канон-борд · обновлено 2026-07-15 · player-count consistency

     operation_b — in the hero lead, replace the current frame-source
     sentence so it reads exactly:

       <p class="lead"><b>Единственный дом борда — канон-репозиторий</b> (board/dashboard.html, открывается в Chrome с диска, обновляется только в репо). Борд — рендер: истина всегда в файлах канона (CONSTITUTION · CORE · INDEX · QUEUE) и в текущем слое рамки OS-репо (minimum-game-frame-v2). Подробные Frame-v1 карта и матрица ниже — <b>SUPERSEDED render</b>, а не текущая design truth; полная регенерация admission/process-слоя остаётся отдельной находкой dr-20260711-004.</p>

     operation_c — immediately after the header closing tag, insert:

       <div class="callout ok"><b>Текущая норма состава (15.07):</b> игра проектируется прежде всего для меняющейся группы 4–8 игроков; поддержка полной группы из восьми обязательна; точный поддерживаемый нижний предел ниже четырёх остаётся OPEN; соло не является текущей дизайн-целью. Источники: действующий столп 1 CONSTITUTION.md и Minimum Game Frame v2.</div>

     operation_d — replace the current-frame item in `✅ Решено (закон)`:

       <li class="done">Рамка целой игры: FRAME READY 11.07 (spine ниже) — основа дизайна, НЕ канон</li>

     with:

       <li class="done">Minimum Game Frame v2: FRAME READY 14.07 — 4–8 игроков, поддержка полной восьмёрки обязательна, нижний предел ниже четырёх OPEN, соло не текущая цель; подробный spine ниже — SUPERSEDED Frame-v1 render</li>

     operation_e — replace the map section tag text:

       рамка целой игры + исторический core-материал + связи · рендер от 12.07 · live-очереди нет

     with:

       legacy Frame-v1 map · SUPERSEDED by Frame v2 (14.07) · исторический core-материал · live-очереди нет

     operation_f — replace the map lane label:

       РАМКА ЦЕЛОЙ ИГРЫ — FRAME READY 11.07 (глобальная петля)

     with:

       LEGACY FRAME-v1 RENDER — SUPERSEDED BY FRAME v2 (14.07)

     operation_g — replace the frame-matrix tag:

       статусы узлов F/P/A/E/L/C/M/R/O · из minimum-game-frame-v1

     with:

       legacy Frame-v1 matrix · SUPERSEDED by minimum-game-frame-v2

     operation_h — replace the current pillar-1 render:

       <div class="track"><h3>1 · Кооп-первый</h3><ul><li class="done">1–4 игрока, соло-стартуемо, петля не соло-оптимальна; роли из рук, не из меню</li></ul></div>

     with exactly:

       <div class="track"><h3>1 · Кооп-первый</h3><ul><li class="done">Игра проектируется прежде всего для меняющейся группы 4–8 игроков. Поддержка полной группы из восьми — жёсткое требование. Точный нижний поддерживаемый предел ниже четырёх остаётся OPEN. Соло не является текущей дизайн-целью. Роли рождаются из рук, не из меню.</li></ul></div>

     postconditions:
       - no unqualified current-authority `1–4` or `solo-startable`
         statement remains in the board;
       - any old Frame-v1 detail that remains is visibly marked
         SUPERSEDED / legacy render;
       - CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md, c-001 and every
         canon card remain byte-unchanged;
       - unrelated admission/render drift is not silently declared fixed.

  5. Review ledger — close player-count finding and retain only the
     separate admission remainder.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/work/review/findings.md

     fetched_base_sha:
       3456eb709f2f43a0c4dbc09fbeab8428d9f72549

     operation_a — set the header to:

       updated: 2026-07-15 (s-repair-eight-player-live-consistency-sweep-001 — 6 открытых: 1 new, 5 known; dr-20260712-002 fixed)

     operation_b — replace only the fact/status content of
     `dr-20260711-004` with:

       **Player-count half disposed 15.07; admission/render drift remains:** current canon-board now presents Minimum Game Frame v2, the exact current pillar-1 player-count norm and explicit SUPERSEDED labels on the retained Frame-v1 map/matrix. The remaining P1 under this ID is separate: INDEX/QUEUE/card c-001 and several board statements still disagree about the completed `ADMIT TO CANON` state. A future bounded canon-board regeneration owns that remainder; canon content itself is not changed by this finding.

       status: known

     operation_c — remove `dr-20260712-002` from `## Открытые находки`.

     operation_d — replace the live-route subsection for
     `dr-20260712-002` with:

       ### dr-20260712-002 — owner requirement «до 8»

       CLOSED / FIXED by
       `s-repair-eight-player-live-consistency-sweep-001`.
       The obsolete proposed
       `c-repair-daily-player-count-routing-20260712-001`
       remains non-runnable and must not be launched.

     operation_e — append to `## Закрытые / отклонённые`:

       | dr-20260712-002 | 2026-07-12 | repair | P1 | 15.07 Frame v2, g-d3a8, canon law, active g-9c41 player-count and owner-facing player-count renders received one explicit disposition: primary range 4–8, full eight mandatory, lower bound below four OPEN, solo not current target. Clean 1-player, 2+ client, two-machine and two-human grey-box checks remain engineering/test hygiene. g-5b07 remains parked with an explicit wake condition and owner. Historical evidence was not rewritten. | fixed |

     preserve:
       - every other finding and repair CALL;
       - all existing evidence wording unrelated to player-count;
       - END_OF_FILE.

  6. Direction owner panel — regenerate only the bounded consistency
     surfaces.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/work/board/dashboard.html

     fetched_base_sha:
       ce081dc33f65566b2108b5a1c960bf061ba3c517

     operations:
       a. Change the hero updated date to 15.07.

       b. Add a top stamp stating:

          g-d3a8: Frame v2 + canon + live player-count consistency
          CLOSED owner-approved · 4–8 · mandatory eight · lower bound
          below four OPEN · solo not current target

       c. Replace the open card for
          `c-repair-eight-player-live-consistency-sweep-001`
          with a closed card containing:

          - status:
            `✓ CLOSED · OWNER-APPROVED`;
          - exact owner verdict from this RESULT;
          - disposition summary:
            g-9c41 corrected; clean 1-player/2-machine/two-human checks
            retained as engineering/test hygiene; g-5b07 parked with
            owner+wake condition; knowledge and current renders synced;
            history untouched.

       d. Regenerate the Problems section from the repaired findings:
          - `dr-20260712-002` no longer appears as open;
          - `dr-20260711-004` says
            `PLAYER-COUNT HALF DISPOSED` and describes only the remaining
            admission/render drift.

       e. Append one 15 July journal item recording this owner-approved
          close and the exact no-change boundaries.

     preserve:
       - M1 route, tasks, open calls and technical truth;
       - all unrelated problem cards;
       - all earlier journal entries verbatim;
       - CSS, layout and other fixed discussion sections.

  7. NOW — close only this completed repair call.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/NOW.md

     fetched_base_sha:
       e0adbafd630f59e1c08c690733f747d53a93eab9

     operations:
       a. Set:

          updated: 2026-07-15 by s-repair-eight-player-live-consistency-sweep-001

       b. Remove the complete `open_calls` entry with stable id:

          c-repair-eight-player-live-consistency-sweep-001

     preserve:
       - current bet;
       - every task and task status;
       - every other open call;
       - decisions;
       - `next: work/c-review-poligon-m1-route-reset-001-call.md`;
       - CHARTER and product state.

  8. LOG — append exactly one one-line repair close.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/LOG.md

     append:

       2026-07-15 — repair/close (g-d3a8/c-repair-eight-player-live-consistency-sweep-001, s-repair-eight-player-live-consistency-sweep-001): owner approved the bounded live consistency package — g-9c41 corrected from active 2–4 to the Frame-v2 4–8/mandatory-eight/lower-bound-OPEN/no-current-solo direction; g-5b07 solo-demo wording explicitly parked with owner+wake condition; normative knowledge and current renders synchronized; 1-player/two-machine/two-human checks retained as engineering/test hygiene; history, canon law/cards, CHARTER and product unchanged. → history/2026-07-15-s-repair-eight-player-live-consistency-sweep-001.md

  9. History — save this complete RESULT verbatim.

     repository:
       ainazemtsau/my_global_workflow

     path:
       live/indie-game-development/history/
       2026-07-15-s-repair-eight-player-live-consistency-sweep-001.md

     postcondition:
       terminate with exactly:

       END_OF_FILE: live/indie-game-development/history/2026-07-15-s-repair-eight-player-live-consistency-sweep-001.md

  10. Explicit no-change surfaces.

      Do not modify:

      - live/indie-game-development/CHARTER.md;
      - Frame-v2 accepted design content;
      - any historical RESULT or existing history file;
      - archive/**;
      - old dated work evidence merely because it contains 1–4, 2–4
        or solo-startable;
      - gas_coop_game_canon/CONSTITUTION.md;
      - gas_coop_game_canon/CORE.md;
      - gas_coop_game_canon/INDEX.md;
      - gas_coop_game_canon/QUEUE.md;
      - gas_coop_game_canon/SESSION.md;
      - gas_coop_game_canon/canon/**;
      - gas_coop_game_canon/AMENDMENTS.md;
      - product repositories, mechanics, roles, scaling formulas,
        networking, Bubble behavior, controls, damage or implementation;
      - unrelated TREE nodes or any TREE text beyond the two exact
        owner-approved operations above;
      - os/FRICTION.md.

captures: []

decisions_needed: []

play_check:
  - "1 Name the contradiction: done — current Frame v2/canon/g-d3a8 require 4–8 with mandatory eight and no current solo target, while active g-9c41, normative knowledge and current renders retained incompatible 2–4/1–4/solo-startable meanings."
  - "2 Reconstruct: done — read current NOW, CHARTER, TREE, Frame v2, owner-requirement knowledge, both prerequisite history RESULTs, current canon entrypoints/index/card/amendment trail, live boards, findings and current work/CALL surfaces; historical evidence was separated from current authority."
  - "3 Propose corrected state: done — every occurrence received one disposition; exact bounded knowledge, two TREE, canon-board, findings, Direction-board and NOW/LOG/history operations are listed with preserve boundaries."
  - "4 Confirm (owner): done — owner approved the whole package and both G9 TREE changes with the actual words: «ОДОБРЯЮ ПАКЕТ CONSISTENCY-ПОПРАВОК, включая G9-правки TREE g-9c41 и g-5b07, правку нормативной knowledge-расшифровки, player-count/Frame-v2 правки canon-board и синхронизацию review-render; историю не менять.»"
  - "5 Friction: skipped — this was the explicitly planned second reconciliation phase after a deliberately bounded TREE and canon repair, not evidence of a recurring OS protocol hole; os/FRICTION.md remains unchanged."

log: "repair/close g-d3a8 eight-player live consistency: owner approved exact G9 TREE + knowledge + render package; post-apply active player-count truth is 4–8, full eight mandatory, lower bound below four OPEN, solo not current target; history/product/canon law unchanged."

next: |
  CALL: work/c-review-poligon-m1-route-reset-001-call.md

END_OF_FILE: live/indie-game-development/history/2026-07-15-s-repair-eight-player-live-consistency-sweep-001.md
