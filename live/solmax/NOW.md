# NOW — solmax

active_bet:
  node: none
  note: |
    Дерево целей построено и утверждено владельцем по карточкам (s-map-001, G9).
    Активной ставки пока нет — следующий шаг shape оформляет Wave-0 (ядро RLK,
    g-kernel) в активируемую ставку. Архитектура уже решена (RLK + волны), поэтому
    shape прямой.

active_tasks: []

recurring: []

open_calls:
  - id: c-shape-001
    status: ready
    note: |
      Shape g-kernel (Wave-0, ядро RLK) в активируемую ставку. Полная карточка и
      детали — в history/s-map-001.md; RLK = 5 частей из дизайна wf_d1ea25b7.

decision_inbox: []

next: |
  CALL c-shape-001
  to: session (shape play)
  direction: solmax   node: g-kernel
  goal: |
    Оформить Wave-0 — ядро RLK (g-kernel) — в активируемую ставку, готовую к работе.
  context: |
    - TREE.md g-kernel + полная карточка в history/s-map-001.md (goal/done_when/why/edge/risk).
    - CHARTER.md (линзы, edges, pre-mortem); risk_posture = explore.
    - RLK = 5 частей: (1) Capability Registry; (2) append-only JSONL-ledger
      (schema_version + зарезервированный upcaster); (3) типизир. конверт CALL/RESULT +
      boundary-валидатор; (4) effect-tier gate (0/1/2 → owner); (5) швы Engine + Store.
      Источник дизайна: design workflow wf_d1ea25b7.
    - Движок = подписки (claude -p + codex), API позже за швом Engine. Build mode =
      фоновые агенты, мелкие проверяемые инкременты.
    - Новый репозиторий Zaratusta (предложен github.com/ainazemtsau/zaratusta, локально
      C:\projects\Zaratusta) — его создание = вероятный первый инженерный инкремент.
  boundaries: |
    Исходы зафиксированы в map — shape НЕ перепланирует дерево. Ядро держать крошечным
    (5 частей, без 6-й). OS никогда не target записи. Новые идеи по умолчанию parked (G8).
  done_when: |
    g-kernel оформлен как ставка по shape-play (G6: cut_list обязателен); NOW.bet
    установлен; готовы первые ≤3 задачи; → next = work/executor CALL.
  return: |
    Shaped g-kernel со всеми полями ставки (appetite/done_when/cut_list/kill_by/
    lens_verdicts) + первые ≤3 задачи + next CALL.
  budget: one shape session.

END_OF_FILE: live/solmax/NOW.md
