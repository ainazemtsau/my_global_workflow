# TREE — solmax

root:
  id: g-zara
  goal: |
    Zaratusta — a personal, deeply personalized AI exocortex the owner actually relies on
    deeply across several areas of life and work, built on a tiny, endlessly extensible
    core (the Registry-Ledger Kernel), growing toward the full EXOCORTEX vision.

  why: |
    The direction's top-level outcome: a real personal "second brain" that compounds —
    depth and real daily use on a kernel that stays small while capabilities accrete —
    not a perpetual core draft (the worst-failure this direction guards against).

  done_when: |
    All hold (SC1 ∧ SC2 ∧ SC3), unless the charter is later revised in a review session:

    1. The owner relies on Zaratusta deeply and recurringly in at least 3 distinct
       areas of life/work (real use, not feature count).

    2. At least several live capabilities (orientation: ≥8) span all four extension
       axes — tool, channel, memory, process — each added with ~zero kernel diff.

    3. At least one real, hard process the owner judges clearly better than a plain
       ChatGPT/Claude session (multi-step, personalized, priority-aware).

  status: active

  children:

    - id: g-kernel
      goal: |
        Крошечное ядро RLK существует и доказано расширяемо (3-й плагин = 0 строк диффа ядра).
      done_when: |
        Ровно 5 частей и не больше: (1) Capability Registry; (2) append-only JSONL-ledger
        (schema_version + зарезервированный upcaster); (3) типизир. конверт CALL/RESULT +
        boundary-валидатор; (4) effect-tier gate (0/1/2 → owner-approval); (5) швы Engine + Store.
        Тест 0-дифф зелёный в CI; replay-тест (записать→прочитать→восстановить); gate-тест
        (tier-2 без аппрува отклонён).
      why: механизм SC2 + предохранитель от «вечного черновика» (pre-mortem #1).
      detail: history/s-map-001.md
      appetite: "1 calendar week / 3 focused executor-sized increments; no extension"
      kill_by: "2026-06-22: kill/review if W0 acceptance cannot be made green without a 6th kernel part, if third plugin requires kernel edits, or if repo setup/CI is still absent."
      shaped_detail: history/s-shape-001.md
      status: active
      children: []

    - id: g-engine
      goal: |
        Когнитивный движок на подписках работает надёжно (claude -p + codex за швом Engine)
        с защитой от credit-cliff.
      done_when: |
        Вызовы идут через шов Engine (форс JSON-Schema); учёт бюджета/кредита; failover-тест
        без потери CALL; исчерпание = видимое залогированное событие (не тихий останов);
        подмена адаптера (позже на API) = 0 диффа ядра.
      why: без мозга ничего не живёт; снимает pre-mortem #5 (credit-cliff).
      detail: history/s-map-001.md
      status: parked
      children: []

    - id: g-channel
      goal: |
        Первый лёгкий канал (Telegram/голос) живёт и фиксирует контракт канала.
      done_when: |
        Канал = плагин kind:channel (вход → типизир. конверт → ответ тем же каналом);
        контракт канала заморожен (2-й канал = 0 диффа); всё через ledger + effect-tier gate;
        реальный dogfood-smoke (≥1 живой запрос с телефона).
      why: ранний dogfood вне IDE → старт SC1; открывает ось «канал».
      detail: history/s-map-001.md
      status: parked
      children: []

    - id: g-surface
      goal: |
        Веб-приложение-дом, где живут ассистент и инструменты и где владелец работает
        вместе с ним (общая доска, канбан).
      done_when: |
        Запущенное веб-приложение (общение + ≥1 общий инструмент вживую); зарегистрировано
        как kind:surface (2-я панель = 0 диффа); co-work-smoke (оба меняют один артефакт);
        всё через ledger + gate; реальный dogfood на ≥1 настоящей задаче.
      why: место, где «живёшь» → SC1 + SC3; открывает ось «поверхность» (5-й вид, доп. доказательство SC2).
      detail: history/s-map-001.md
      status: parked
      children: []

    - id: g-cognition
      goal: |
        Когнитивный цикл (сбор контекста + многошаговый цикл) как плагин #1 даёт глубокую
        помощь явно лучше обычного чата.
      done_when: |
        Плагин kind:process (контекст → ресёрч → рассуждение → самопроверка → результат);
        на ≥1 реальной задаче владелец признаёт «явно лучше» обычной сессии (head-to-head,
        записан); многошаговость и персонализация видны из ledger; 2-й процесс = 0 диффа.
      why: прямо SC3 («мега-мозг»), не обёртка чата (pre-mortem #4).
      detail: history/s-map-001.md
      status: parked
      children:

        - id: g-megabrain
          goal: |
            Продвинутый «мега-мозг»: генеративный UI (сам собирает виджеты); обучение на
            реакциях (дофамин / prediction-error); размышление во сне → только хорошие идеи;
            омниканальное «тело».
          done_when: |
            Раскрывается в будущей map при активации (сейчас не детализируется).
          why: полная EXOCORTEX-планка; открываем только после реального использования базы (pre-mortem #7, G8).
          detail: history/s-map-001.md
          status: parked
          children: []

    - id: g-memory
      goal: |
        Память живёт: эпизодическая поверх ledger → семантическая/RAG (→ SQLite-fold по объёму).
      done_when: |
        Эпизодическая (верно ссылается на прошлые сессии); семантическая (recall по смыслу
        без совпадения слов); kind:memory (2-й вид = 0 диффа); smoke: процесс измеримо лучше
        благодаря памяти.
      why: персонализация и накопление; питает g-cognition / g-megabrain; открывает ось «память».
      detail: history/s-map-001.md
      status: parked
      children: []

    - id: g-accrete
      goal: |
        Возможности накапливаются по осям до ≥8 живых при 0 диффе (инструменты + триггеры
        процессов; чтение OS read-only).
      done_when: |
        ≥8 используемых способностей по осям, каждая register()+handler при 0 диффе; живут
        доска + канбан + ≥1 app-коннектор + чтение OS (жёстко read-only, протестировано,
        не пишет); триггеры manual/schedule(cron-MCP)/event; владелец реально пользуется несколькими.
      why: SC2 вширь + бытовые инструменты → SC1.
      detail: history/s-map-001.md
      status: parked
      children: []

END_OF_FILE: live/solmax/TREE.md
