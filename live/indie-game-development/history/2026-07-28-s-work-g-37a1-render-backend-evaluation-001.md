# RESULT s-work-g-37a1-render-backend-evaluation-001

RESULT s-work-g-37a1-render-backend-evaluation-001 (call: c-work-g-37a1-render-backend-decision-001)
direction: indie-game-development
track: t-render
play: work
node/task: g-37a1/t-4

outcome: |
  Основание денежного решения готово: по буквальному порогу владельца Voxel Play 4 закрывает
  целиком 0 фич и набирает 0 рабочих дней, поэтому расчёт рекомендует не покупать пакет и сделать
  собственный минимальный кубический мешер. Это checkpoint, а не решение: t-4 и
  d-topology-backend-purchase-001 остаются открыты до точных слов владельца.

evidence: |
  - live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28.md
  - Цена $149.99 проверена 2026-07-28 на канонической странице:
    https://assetstore.unity.com/packages/tools/game-toolkits/voxel-play-4-391842
  - Первичные страницы документации по chunks/lifecycle, colliders, save format, multiplayer и API
    перечислены в артефакте; они подтверждают функции пакета и одновременно остаток интеграции.
  - По done_when: список целиком закрытых фич и сумма — § «Что именно считается»; незакрытое,
    отключаемое, авторитетность, детерминизм и engine-free boundary — две таблицы и § «Что не
    отдаём пакету»; цена — § «Короткий ответ» и источники; месячный downside — § «Если через месяц».
  - Точного вердикта владельца в этой ноге нет; рекомендация не выдана за его решение.

state_changes: |
  - Create live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28.md with the
    complete price/feature/threshold evaluation and END_OF_FILE trailer.
  - Create live/indie-game-development/work/c-work-g-37a1-render-backend-owner-verdict-002-call.md
    as the same-track continuation for the exact owner verdict.
  - NOW.md:
    - set updated to 2026-07-28 by s-work-g-37a1-render-backend-evaluation-001;
    - preserve bet, tasks, tracks, all unrelated calls/decisions/issues and t-4 status active;
    - clear open_calls[c-work-g-37a1-render-backend-decision-001];
    - add open_calls[c-work-g-37a1-render-backend-owner-verdict-002] ready in t-render for t-4,
      pointing to its CALL file and the evaluation;
    - keep decisions[d-topology-backend-purchase-001] open and replace only its recommendation
      with the evidenced 0-day threshold recommendation, explicitly pending owner verdict.
  - LOG.md: append the exact log line once.
  - Save this full RESULT once as
    live/indie-game-development/history/2026-07-28-s-work-g-37a1-render-backend-evaluation-001.md.
  - No CHARTER.md, TREE.md, product repository, purchase, install, other task or other lane changes.

captures: []

decisions_needed:
  - q: "Покупаем Voxel Play 4 или делаем свой минимальный мешер?"
    options:
      - "Не покупаем Voxel Play 4; делаем свой минимальный мешер."
      - "Покупаем Voxel Play 4 и ставим его под нашу логическую сетку."
    recommendation: "Не покупать: буквальная зачётная сумма 0 дней, а мягкий лучший край текущего ядра не превышает примерно 2 дней против порога примерно 5."

play_check:
  - "1 Recite: done — goal/done_when сверены с active bet g-37a1, task t-4 и lane t-render."
  - "2 Owner inputs (owner): done — использованы уже записанные точные слова владельца «если это закрывает какую-то фичу … и нам не надо это делать» и его порог около недели; нового факта от него не требовалось, а вердикт не выведен."
  - "3 Do the work: done — цена и возможности проверены по официальной странице и документации; расчёт записан в versioned work artifact."
  - "4 Self-check: done — все пять bullets done_when имеют именованный раздел evidence; продукт, покупка и установка не затронуты."
  - "5 Close: done as checkpoint — returning call cleared, same-track owner-verdict continuation registered; t-4 and decision remain open."

log: 2026-07-28 | s-work-g-37a1-render-backend-evaluation-001 | t-render | work | direction | g-37a1/t-4: Voxel Play 4 набирает 0 дней целиком закрытых фич при цене $149.99; даже мягкий лучший край текущего ядра не превышает примерно 2 дней, поэтому рекомендация — не покупать, а решение остаётся за владельцем -> history/2026-07-28-s-work-g-37a1-render-backend-evaluation-001.md

next: |
  CALL c-work-g-37a1-render-backend-owner-verdict-002
  to: session
  direction: indie-game-development
  track: t-render
  play: work
  node: g-37a1
  task: t-4
  goal: Владелец зафиксировал окончательный выбор между Voxel Play 4 и собственным минимальным мешером.
  context: evaluation at live/indie-game-development/work/voxel-play-4-backend-evaluation-2026-07-28.md;
    score 0 days at $149.99; recommendation no-buy; exact owner words required.
  boundaries: no inferred verdict; no purchase/install; preserve F3 and all other lanes.
  done_when: exact owner verdict closes d-topology-backend-purchase-001 and t-4 and routes the
    corresponding next render step.
  return: RESULT with the owner's exact words.
  budget: one short owner answer

END_OF_FILE: live/indie-game-development/history/2026-07-28-s-work-g-37a1-render-backend-evaluation-001.md
