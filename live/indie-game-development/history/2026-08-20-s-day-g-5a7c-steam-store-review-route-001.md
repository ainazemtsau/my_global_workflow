RESULT s-day-g-5a7c-steam-store-review-route-001
direction: indie-game-development
play: day
node/task: g-5a7c
outcome: |
  Официальный маршрут на минимальный Steam Store Presence зафиксирован без молчаливой
  подмены пятой волны: сначала отдельный свежий review закрывает волну скриншотов и получает
  слова владельца по обязательным решениям, затем отдельный shape имеет право нарезать
  successor-волну и выдать разработчику технический наряд. В review передан полный минимальный
  контур: AppID и публичное имя, фактический Steamworks checklist, тексты и метаданные, логотип
  и все обязательные графические экспорты, пять gameplay-скриншотов, обязательный трейлер,
  Store Beta preview и отправка на ревью.
evidence:
  - |
    Владелец разрешил сохранение дословно: «запускай». Границу результата уточнил дословно:
    «важно что должно включать все факты и действия которые нужно сделать название логотипы
    все что нужно МИНИМАЛЬНО что бы пройти ревью».
  - |
    Трейлер и способ съёмки заданы его словами: «ВАЖНО что нужно еще и трейлер и тут стоит
    учитывать что уже добавлен хозяин»; «это должно записываться с бесплатными анимациями»;
    «у нас есть плагин Feel ... дрожание камеры когда идет хозяин»; ролик предполагается
    снимать вчетвером, а подключение друзей должно быть простым и заранее проверенным.
  - |
    Fresh Direction OS state @ 24c66006: активен bet-g-5a7c-wave-5 со сроком 2026-08-20;
    t-photoset-1 active, t-frames-1 waiting; i-steam-appid говорит, что имя, base AppID и
    публичная страница не начаты; отдельная четырёхпользовательская съёмка была вырезана из
    этой волны, поэтому добавить трейлер прямым developer CALL нельзя без review.
  - |
    Fresh product read @ C:/projects/Unity/GasCoopGame_dev dev 97ca2c98485f158d3367103b202000481e1e74d7:
    рабочая сцена сборки — Lobby + IntegratedHouse; PhotoSet_LivingRoom ещё отсутствует;
    FishNet 4.7.2/Tugboat использует прямой IP, 127.0.0.1 и UDP 7770; Feel импортирован,
    но в Assets/TunnelCrew его camera shake не подключён; PresentationSettings всё ещё
    использует Kenney_CharacterA как тело хозяина, а не Anton homeowner.
  - |
    Юридический стоп-факт из
    C:/projects/Unity/GasCoopGame_dev/Assets/TunnelCrew/Art/Bodies/Sources/Anton/SOURCE.md:
    Mixamo-анимации разрешены бесплатно для коммерческой игры, но геометрия Anton homeowner
    сделана через Human Generator из репака с неподтверждённой лицензией; сам SOURCE запрещает
    выносить её наружу до покупки коммерческой лицензии. Текущий Kenney_CharacterA имеет
    зафиксированную CC0-лицензию и остаётся законным бесплатным fallback.
  - |
    Официальная база Valve: Store Presence review занимает обычно 3–5 рабочих дней и подаётся
    минимум за 7 рабочих дней; App landing page checklist — фактическая власть; имя после
    pre-release review меняется только через специальный процесс; обязательные размеры графики
    и правила капсул/Library assets заданы Steamworks; требуется минимум пять gameplay screenshots;
    trailer обязателен для release process и должен показать игру в первые 10 секунд даже без звука.
    Источники перечислены в issued CALL.
state_changes:
  - |
    ADD live/indie-game-development/work/2026-08-20-call-review-wave-5-steam-minimum.md —
    самодостаточный CALL свежему review: полная матрица минимального Store Presence, честное
    закрытие Wave 5, юридический gate модели, минимальный trailer/capture contract и owner-verdict
    guard перед downstream shape.
  - |
    ADD card day kind=day date=2026-08-20 with blocks:
    фокус = минимальный Steam Store Presence, принятый Valve, включая трейлер;
    старты = только свежий review CALL, затем shape после слов владельца;
    не делаем = прямой developer CALL, optional Steam assets, Game Build/demo review,
    Steam networking и публичное использование нелицензированной модели;
    передумаю если = фактический App checklist, отзыв Valve либо слова владельца меняют границу.
  - |
    ADD card c-review-g-5a7c-wave-5-steam-minimum-001 kind=call,
    _bet=bet-g-5a7c-wave-5, status=ready, to=session, for=bet-g-5a7c-wave-5, play=review,
    issued=2026-08-20, call=work/2026-08-20-call-review-wave-5-steam-minimum.md.
  - |
    ADD issue i-homeowner-public-license-001, level=objective, route=review,
    blocks=t-frames-1: Anton homeowner нельзя использовать в публичных скриншотах, трейлере
    или внешней сборке без доказанной коммерческой лицензии Human Generator; закрытие —
    лицензия либо замена на проверенно разрешённую геометрию.
  - |
    PRESERVE bet-g-5a7c-wave-5, NOW, все текущие задачи/наряды, background cargo work,
    i-steam-appid и i-steam-demo-gates-unverified: day не судит и не переформировывает волну.
captures:
  - |
    i-homeowner-public-license-001 — новый проверенный legal blocker; не идея и не вывод по памяти.
decisions_needed: []
play_check:
  - "1 Refresh reality: done — fresh Git, working-set cards, due Steam issues and product authority reread."
  - "2 His first: done — Steam name/AppID/page are overdue; 2026-08-20 is the active wave deadline."
  - "3 Derived brief: done — screenshots alone do not exhaust Store Presence; trailer and store/admin assets are missing scope."
  - "4 Sweep: done — passed appetite routes to review; direct trailer/network execution would violate the active cut list; new licensing evidence promoted to an issue."
  - "5 Advise: done — one focus and one collision-free planning start, fresh review."
  - "6 Discuss: done — owner supplied trailer, four-player capture, free-animation, Feel and minimum-review constraints."
  - "7 Save boundary (owner): done — exact save word «запускай»; exact final boundary quoted in evidence."
  - "8 Close: done — one RESULT, writer apply/validate/commit, next is a fresh physical review chat."
log: |
  МИНИМАЛЬНЫЙ STEAM STORE PRESENCE ВМЕСТЕ С ТРЕЙЛЕРОМ ОТПРАВЛЕН В СВЕЖИЙ REVIEW: наряд содержит
  весь обязательный baseline Valve, фактическую сверку Steamworks, простой четырёхпользовательский
  capture route и legal gate хозяина. Пятая волна здесь не переписана и не получила самосуд.
next: |
  CALL c-review-g-5a7c-wave-5-steam-minimum-001 — открыть в отдельном свежем физическом чате.
