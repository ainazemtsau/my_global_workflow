# NOW: indie-game-development

updated: 2026-07-31 by s-review-g-37a1-obsolete-concept-change-001

bet: null

tasks: []

tracks: []

direction_forecast:
  status: no_basis
  target: "Достойное демо на октябрьском Steam Next Fest 2026, затем платный Steam-релиз и повторно используемый solo-release процесс."
  as_of: 2026-07-31
  basis: "Численная вероятность запрещена владельцем и не имеет эмпирического знаменателя. Ставки нет: направление между ставками, и прогнозировать не из чего."
  drivers:
    - "g-37a1 закрыт 2026-07-31 вердиктом obsolete: владелец сменил концепт игры на более простой и меньшего масштаба. Ставки нет, задач нет, полос нет, нарядов нет."
    - "ПРОДУКТОВЫЙ КОД ЖИВ И НЕ ОТМЕНЁН — он и есть главный актив, переживший смену: 30 326 строк продуктового C# в Assets/GasCoopGame/**, газовая симуляция на живом ярусе, четыре газовые сцены, сокет персонажа в main, сетевая основа на FishNet, 1846 зелёных headless-тестов и 117 негативных контролей. Смена концепта меняет, ЧТО строить дальше, а не делает построенное неверным."
    - "За всю жизнь g-37a1 (2026-07-28 .. 07-31) в main не попало ни строки игрового поведения по его задачам: измерено 7 изменённых строк, и это механическое переименование под Unity 6.5.5f1. Это факт о ноге, а не о коде выше."
    - "Инженерный контур перестроен и это переживает смену концепта: контракт v35 «замороженный контракт — код, а не проза», обязанностей 234, обязательное чтение в потолке, все шесть рабочих папок на одном штампе, гейты развязаны по ногам."
    - "Октябрьский Steam Next Fest остаётся жёстким маршрутом CHARTER и от смены концепта не зависит. Публичная страница нужна к 2026-08-31, и это единственный живой срок."
  update_when: "Владелец сформулировал новый концепт и он прошёл frame/map; либо Valve изменила дату; либо наступил 2026-08-15 без выбранной новой ставки."

issues:
  - id: i-direction-to-product-call-contract-001
    issue: "Direction-root CALL в продукт обязан назвать фактически проверенные слот, lease, HEAD, engineering_contract и вход. БУНС №2 случился 2026-07-30: c-exec-g-37a1-simple-gas-rest-001 v1 назвал путь tests/.../G37Fixtures.cs, которого на базе назначения нет. БУНС №3 случился тем же днём: c-control-g-37a1-venue-packaged-player-replace-close-001 знал, что старый root остаётся ACTIVE / PAIR-CANDIDATE, но одновременно требовал WIN-U3 AVAILABLE и фиксировал исторический published Re-sync commit как текущий basis; исполнитель законно вернул ESCALATE без изменений. Общий корень: наряд утверждает факт о венью или допустимости запуска, который не согласован с реальным состоянием этого венью. Maintenance уже обязателен; до него каждый named path проверяется на объявленной базе, а каждое lease/availability/basis утверждение — против селектора и точной семантики стадии."
    level: execution
    route: maintenance
    review_when: "MAINTENANCE ОБЯЗАН по собственному правилу этого issue (второй бунс). Отдельная сессия по os/MAINTENANCE.md; live/** она не трогает. До неё — ручная поштучная сверка путей в каждом выпускаемом CALL."
    evidence: "history/2026-07-28-s-repair-g-37a1-exec-call-contract-001.md; history/2026-07-30-s-repair-g-37a1-simple-gas-call-base-fix-001.md; history/2026-07-30-s-repair-g-37a1-venue-replacement-preflight-correction-001.md; текущие executor CALL-файлы."
  - id: i-live-tier-dead-islands-001
    issue: "В продукте есть dead islands и built-but-unwired части; это ориентация для live-tier работы, не разрешение на удаление. NearGasSimulation и PlayerSense требуют проверки fitness."
    level: execution
    route: work
    review_when: "Первая инженерная нога, меняющая структуру live tier, ожидаемо t-7."
    evidence: "work/topology-boundary-g-37a1.md §6; history/2026-07-28-s-work-g-37a1-topology-boundary-001.md."
  - id: i-product-plan-deviations-unrouted-001
    issue: "Замороженный PLAN t-6 записал два отклонения от done_when наряда в разделе «для Направления» (мёртвая зона НЕ параметр; у выбранного закона нет Θ) — и Направление их не обработало: возврат PLAN был отмечен в open_calls одной строкой «заморожен коммитом». Оба отклонения умерли вместе с опровергнутым законом, но класс остался: продукт пишет отклонения в свой PLAN, а не в RESULT домой, и они не видны."
    level: execution
    route: work
    review_when: "На каждом возврате продуктовой стадии PLAN: раздел отклонений читается вслух и попадает в RESULT, либо класс переводится в maintenance."
    evidence: "openspec/changes/c-exec-g-37a1-gas-rest-and-checksum-001/PLAN.md §9 в C:/projects/Unity/GasCoopGame_win-u4; NOW.md open_calls до 2026-07-30; work/c-exec-g-37a1-gas-rest-amend-001-call.md §context."
  - id: i-g37-cond-zero-release-deferred-to-t7-001
    issue: "Правило выброса накопленного остатка в G37-BAND-004 объявлено полным по трём веткам, но ветка «cond == 0 при ранее накопленном ненулевом остатке» в t-6 недостижима ПО ПОСТРОЕНИЮ: _faceConductivity readonly и пишется один раз в конструкторе (VoxelField.cs:47,320,333), NotifyConductivityChanged только будит грань (:818-827), а при cond == 0 накопитель равен carry, поэтому копиться нечему. Владелец выбрал «B» 2026-07-30 и ветка передана t-7/D1. Долг настоящий: ненулевой остаток держит грань активной (:838), то есть застрявший остаток на закрывшейся грани = вечная сетевая дельта, удар по единственному жёсткому требованию владельца (мультиплеер)."
    level: execution
    route: work
    review_when: "Перед выпуском CALL по t-7, ЕСЛИ t-7 будет строить топологию поверх СТАРОГО закона. Для нового простого закона долг не возникает: у него нет накопителя остатка, поэтому терять его при закрытии грани нечего. Проверить это первым делом, а не наследовать долг по инерции."
    evidence: "openspec/changes/c-exec-g-37a1-gas-rest-and-checksum-001/specs/sim-core/spec.md:251,264 в C:/projects/Unity/GasCoopGame_win-u4; work/c-exec-g-37a1-gas-rest-band-scope-001-call.md (СНЯТ, сохранён как улика) §done_when 2; дословный токен владельца «B» 2026-07-30."
  - id: i-conductivity-snapshot-vs-live-checksum-001
    issue: "Старая контрольная сумма MeaningChecksum складывает ЖИВУЮ проводимость с сетки (VoxelField.cs:1052), а течение газа считает по СНИМКУ из конструктора (:1669). Сегодня безвредно — менять проводимость на живом поле нечем. Но t-7 ломает ровно этот шов: две машины смогут совпасть по контрольной сумме и разойтись по поведению, либо разойтись по сумме при одинаковом поведении. Тихая расстыковка именно в мультиплеере."
    level: execution
    route: work
    review_when: "Перед выпуском CALL по t-7, ЕСЛИ t-7 будет менять топологию на СТАРОМ законе. Наряд громкого отказа, который это закрывал, снят вместе с путём ремонта; для нового закона вопрос ставится заново при его первой встрече с изменяемой топологией."
    evidence: "Assets/GasCoopGame/Core/Field/Voxel/VoxelField.cs:1052,1669 в C:/projects/Unity/GasCoopGame_win-u4; work/c-exec-g-37a1-gas-rest-band-scope-001-call.md (СНЯТ, сохранён как улика) §done_when 4."
  - id: i-product-contour-consolidated-v34-001
    issue: "Продуктовый контур консолидирован 2026-07-30 по прямому указанию владельца («запускай полную чистку… вырежи бюрократическое»). ЧТО ИЗМЕНИЛОСЬ, чтобы никто не переделывал и не спотыкался: (1) расщепление контракта 31/33/34 по шести рабочим папкам устранено — терминально 34 везде, всё чисто; корень путаницы найден и назван — ДВА независимых ресинка 31→33 в 09:34 на разных ветках (6069024b на линии main, 498b609d в win-u3), их validation.config совпал побайтово, поэтому переносилась только дельта v34. (2) Класс-починка развязки ног доведена до конца: tools/delivering-scope.ps1 был написан 2026-07-29 как «ОДНА производная, подключаемая КАЖДЫМ местом обхода», но подключён к двум; теперь к восьми — добавлены negative-control-check, escape-class-check, fix-class-check, refuted-register-check, review-check, result-check. (3) Гейт закрывающих отчётов: незавершённый корень больше не обязан рапортовать DELIVERED, и ветка С изменениями, но без своего отчёта, больше не считается «ветвью без изменений» и не проверяет чужие исторические отчёты. Аварийное поведение сохранено везде: невыводимая область действия по-прежнему проверяет ВСЁ. Ослаблений нет — все посевные ловушки (R1-R9 result-check, derivation/closing/negative-control) по-прежнему краснеют."
    level: execution
    route: work
    review_when: "На первой же инженерной ноге в любом слоте: сверить, что заявленное здесь совпадает с фактом, и не переоткрывать сделанное. Раньше — если гейт снова упадёт на ЧУЖОМ пакете: это рецидив класса и повод для maintenance, а не для очередной точечной правки."
    evidence: "Продуктовые коммиты 7dd09147, 7245d269, a79fb27f, 2b3d5afe в C:/projects/Unity/GasCoopGame; исходные позиции всех шести веток сохранены в refs/backup/pre-v34-cleanup/*; батарея на main зелёная ('OK: all gates green'); t-sim 23 красных из 2013 и t-body 16 из 1863 — оба совпадают со своими квитанциями."
  - id: i-grid-v1-g01-dead-root-open-001
    issue: "Корень c-exec-grid-v1-g01-document-authority-001 числится ACTIVE на стадии PLAN с 2026-07-21, реализации у него нет вообще (две квитанции: 00-plan.json, 01-plan-route-fix.json). Именно его замороженная спека дважды роняла c-exec-v31-venue-authority-binding-fix-001 на REPORT, когда вся собственная работа той ноги была зелёной, а её квитанция при этом ЗАПРЕЩАЛА ей чинить чужой пакет. После развязки гейтов он больше никого не блокирует, но остаётся активным и занимает место в учёте корней. Решение о его судьбе — закрыть или припарковать — за владельцем: это lifecycle-действие, а не гигиена."
    level: execution
    route: work
    review_when: "Владелец назвал этот корень и выбрал закрытие либо парковку; раньше — если он снова появится в блокировке любой ноги."
    evidence: "docs/measurements/root-receipts/c-exec-grid-v1-g01-document-authority-001/ в C:/projects/Unity/GasCoopGame; docs/measurements/root-receipts/c-exec-v31-venue-authority-binding-fix-001/06-report-blocked-r1.json и 08-report-blocked-r2.json (поле blocker.forbidden_here)."
  - id: i-topology-commit-direction-001
    issue: "Контракт реза односторонний: дедуплицированный НАБОР открытых клеток. Его идемпотентность и догон отставшей машины объединением верны только потому, что открытия коммутируют; копание и постановка блока не коммутируют. Двусторонняя упорядоченная дельта конечного состояния возможна, но платит идемпотентностью, union-replay и появлением первой отклоняемой команды игрока. В продукте seq отсутствует, буфер задержки ввода описан в ADR-0002 и не построен."
    level: execution
    route: work
    review_when: "Перед выпуском CALL по t-7: там форма замерзает, и на t-7 висят t-5, t-9, t-10 и t-11."
    evidence: "work/topology-boundary-g-37a1.md §4; work/2026-07-29-core-grid-and-building-decisions.md §2."
  - id: i-subface-mask-ceiling-001
    issue: "Маска открытости грани — одно 64-битное число, MaxSubFacesPerFace = 63, то есть не более 7 делений на сторону. Крошка 4×4×4 (16 подграней) проходит; 8³ (64) и 16³ (256) не проходят без расширения хранилища, а оно меняет формат состояния и контрольную сумму. Владелец 2026-07-29 просил максимальную маску ради вида разрушения."
    level: execution
    route: work
    review_when: "Перед выпуском CALL по t-7 либо раньше, если t-11 упрётся в вид разрушения."
    evidence: "Core/Field/Voxel/VoxelResolution.cs:84 в C:/projects/Unity/GasCoopGame; work/2026-07-29-core-grid-and-building-decisions.md §3."
  - id: i-g5e8c-written-under-old-concept
    issue: "g-5e8c частично переписан, но устройство перехода между участками намеренно не решено и не должно наследоваться из старого концепта."
    level: roadmap
    route: map
    review_when: "После игры в первое ядро и до shape g-5e8c."
    evidence: "history/2026-07-28-s-map-g-37a1-core-requirements-001.md; TREE.md g-5e8c."
  - id: i-procgen-determinism
    issue: "Процедурная сборка обязательна для g-5e8c, не для g-37a1; сетевой перенос, детерминизм и совместимость с runtime-мутацией топологии не доказаны."
    level: execution
    route: work
    review_when: "Перед первым level-build CALL и не позже shape g-5e8c."
    evidence: "work/pgg-analysis-2026-07-10.md; history/2026-07-26-s-work-october-demo-basis-v3-revision-001.md."
  - id: i-steam-appid
    issue: "Название, base AppID и публичная Steam-страница не начаты; для Next Fest публичная страница нужна к 2026-08-31 23:59 PDT."
    level: roadmap
    route: work
    review_when: "2026-08-15 либо раньше в день появления названия."
    evidence: "work/marketing/assets/checkpoint-2026-07-12/steamworks-no-app-one-credit.png; TREE.md g-2b7f."
  - id: i-steam-demo-gates-unverified
    issue: "У Valve нужно подтвердить: относится ли 30-дневное ожидание к demo app и возвращается ли единственный Next Fest slot после снятия регистрации."
    level: roadmap
    route: work
    review_when: "До сохранения регистрации и не позже 2026-08-20."
    evidence: "https://partner.steamgames.com/doc/gettingstarted/onboarding; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest; history/2026-07-27-s-map-october-demo-order-reset-001.md."
open_calls: []

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
