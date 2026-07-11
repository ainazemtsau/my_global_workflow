CALL c-repair-canon-post-pilot-route-001
to: session
direction: indie-game-development
play: repair
node: g-d3a8
surface: any

goal: |
  Восстановить однозначный и owner-confirmed маршрут канона после
  завершённого paper-only пилота: определить, какой процесс сейчас
  управляет design-to-canon переходом, и привести Direction OS state в
  соответствие с этим решением до любого admission verdict по
  q-investigation-readiness.

context: |
  2026-07-10 владелец выбрал «А»:

  - Canon Forge v2 / Кузница v2 была приостановлена как активный
    design-decision route;
  - core-0 и core-1 были поставлены на HOLD для одного пилота;
  - было разрешено исследование process v3 и один owner-evaluated pilot.

  Исправленный paper-only pilot завершён.

  Дословный process verdict владельца:

  "ACCEPTED"

  Но этот verdict:

  - не установил Canon Forge v3;
  - не возобновил Canon Forge v2;
  - не изменил канон;
  - не допустил q-investigation-readiness-paper-decision-v1.

  При этом:

  - canon repo всё ещё показывает START/QUEUE/SESSION Кузницы v2;
  - Direction OS history говорит считать этот маршрут suspended;
  - NOW открыл отдельный canon-admission CALL.

  Admission-сессия остановлена владельцем со словами:

  "если есть конфликт или какие-то проблемы, то сначала их исправить
  и потом уже определять остальное"

  Эти слова не являются ADMIT / HOLD / REJECT verdict.

  Exact contradiction to repair:

  1. visible canon-repo entrypoint still describes v2;
  2. higher-authority direction state suspended v2;
  3. v3 passed one pilot but remains uninstalled;
  4. canon admission was routed without an explicit post-pilot governing
     process.

  Read:

  - os/KERNEL.md
  - os/plays/repair.md
  - live/indie-game-development/NOW.md
  - live/indie-game-development/TREE.md
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/LOG.md tail
  - live/indie-game-development/history/
    2026-07-10-s-repair-canon-design-process-route-001.md
  - live/indie-game-development/history/
    2026-07-11-s-review-canon-process-v3-revised-pilot-001.md
  - live/indie-game-development/history/
    2026-07-11-s-research-q-investigation-readiness-001.md
  - live/indie-game-development/history/
    2026-07-11-s-research-q-investigation-readiness-canon-admission-001.md
  - live/indie-game-development/work/
    canon-process-v3-paper-only-pilot-brief.md
  - live/indie-game-development/work/
    q-investigation-readiness-paper-decision-v1.md
  - current github.com/ainazemtsau/gas_coop_game_canon:
    START.md, CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md, SESSION.md,
    templates/card.md and AMENDMENTS.md
  - relevant git history of both repositories.

boundaries: |
  Do not decide ADMIT / HOLD / REJECT for the paper answer.

  Do not:
  - revise «Цель стоит запуска»;
  - generate another game-design question;
  - design detection, activation, extraction, Bubble, damage, economy,
    inventory, UI, co-op roles or implementation;
  - install or modify a process before the owner's repair confirmation;
  - change canon;
  - treat "ACCEPTED" as process installation;
  - treat the owner's repair-first instruction as HOLD PAPER-ONLY;
  - infer authority from stale visible files when higher-authority state
    explicitly suspended them.

done_when: |
  1. The contradiction is stated in exactly two owner-readable lines.

  2. The timeline is reconstructed from current artifacts and commits:
     - why v2 was suspended;
     - what the one-pilot mandate authorized;
     - what "ACCEPTED" established;
     - what it did not establish;
     - why the admission CALL was opened.

  3. A corrected hot-state proposal is shown, including:
     - the active/suspended status of v2;
     - the accepted-but-uninstalled status of v3;
     - the status of the paper answer;
     - whether admission remains blocked;
     - the exact next governing route.

  4. If more than one post-pilot route remains valid, the owner receives
     2–3 options with consequence, downside and recommendation.

  5. The owner confirms one corrected state in verbatim words.

  6. RESULT cites that verdict verbatim and applies only the approved
     state/process routing diff.

  7. No canon card, design answer or implementation task is opened.

  8. If this gap is systemic rather than one-off, one precise
     os/FRICTION.md entry is proposed.

return: |
  Короткий русский repair brief:

  - contradiction;
  - reconstructed cause;
  - corrected current truth;
  - 2–3 route options only if needed;
  - recommendation;
  - exact proposed state diff;
  - owner verdict verbatim.

  Then one RESULT. No canon admission and no new design topic.

budget: one owner-present text-only session

END_OF_FILE: live/indie-game-development/work/c-repair-canon-post-pilot-route-001-call.md
