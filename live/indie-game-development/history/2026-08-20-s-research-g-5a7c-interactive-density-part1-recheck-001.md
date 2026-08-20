RESULT s-research-g-5a7c-interactive-density-part1-recheck-001
direction: indie-game-development   play: research   node/task: c-research-g-5a7c-interactive-density-001
outcome: |
  Часть 1 ресёрча повторена по текущему product main
  `75b770df1d646eb93ff4cbbcc37be58234ac772c`, без слота и без продуктовых правок.

  Настроенная частота — 30 тактов/с. Каждый такт один aggregate ObserversRpc по-прежнему несёт
  полный CargoSnapshot[] каждому удалённому клиенту; собственный экран хоста применяет тот же
  массив локально. RPC надёжен при ЛЮБОМ размере, а на 27-м малом cargo-record меняется не канал,
  а форма доставки: одно reliable-сообщение начинает дробиться на reliable-фрагменты.

  Статическая оценка текущего пакета на одного клиента, до transport/IP/UDP headers,
  retransmits и другого трафика: 50 предметов — около 2,355 B/тик, 70.7 KB/s и минимум 2
  фрагмента; 200 — 9,241 B/тик, 277 KB/s и 8; 500 — 23,041 B/тик, 691 KB/s и 19. Это НЕ
  runtime-замер. При 500 предметах один cargo-stream заполняет окно LiteNetLib из 64 пакетов за
  3.37 такта, около 112 мс; потеря задерживает последующие ordered reliable данные.

  Старый аудит устарел ещё в двух местах. CargoBody.Find на current main уже словарный, поэтому
  квадрат на стороне физики повторно чинить нельзя; линейный Find остался в
  NetworkCargoPresentation и даёт N(N+1)/2 сравнений на каждый полный snapshot. CargoBody.Step
  теперь всегда шагает глобальный physics world, даже когда весь груз спит; старое полное
  замирание мира снято. Точные потолки физики и рендера из кода не следуют.

  Прямой ответ про решение «не слать неизменившееся»: оно делает цену пропорциональной числу
  одновременно dirty items и вероятнее всего достаточно для обычной плотности 50–120 предметов,
  когда меняются единицы или десятки. Но это условный вывод, не доказательство «с запасом»:
  текущий single-datagram envelope около 26 dirty records, после заявленного сжатия около 41,
  а распределение одновременно движущихся/меняющихся предметов в массовом каскаде неизвестно.
  Поэтому клиентский локальный полёт сейчас не строится, но runtime-часть 2 законно снять нельзя.

  Порядок уточнён: B0 (реестр + безголовые тесты + теневые метрики без изменения поведения) можно
  готовить параллельно ремонту A; B1 подключается только после A и возврата луча; затем C; затем D.
  Глобально наблюдаемые игровые состояния нельзя фильтровать комнатным interest вместе с позой.
  Для них нужен живой start/change/end + catch-up контракт либо атомарный потребитель в том же
  wire-record. Текущий ThingRemainingSeconds уменьшается каждый такт, поэтому compare-all-fields
  будет слать неподвижный звонящий предмет 30 раз/с; мёртвым заделом это оставлять нельзя.

  Статический корпус мебели + отдельная интерактивная дверца остаётся правильным разрезом цены,
  но не готовой реализацией. Текущая дверь намеренно лишена физики: collider прежде блокировал
  груз, пока игрок и хозяин проходили по двум другим моделям. Возврата Rigidbody недостаточно —
  open/closed должен одинаково отражаться в cargo physics, player walk-space и householder
  graph/sight, плюс в сети и late join.
evidence: |
  Product commit и прямые якоря:
  - NetworkWalkerCourier.cs:471-496,531-590 — tick, полный массив, host-local apply и ObserversRpc.
  - CargoSnapshot.cs:7-31 — 10 float, четыре int и bool; Writer.cs:341-350,388-399,
    472-484,1128-1152 — 45 B для малых id и второй байт CargoId после 63.
  - RpcProcessor.cs:451-464 — отсутствие Channel-параметра означает Channel.Reliable.
  - Tugboat.cs:115,576-583; NetConstants.cs:37,40-49; TransportManager.cs:128-137,
    174-197,344-358,572-621 — 1280 B effective MTU, 1270 B split segment, reliable split,
    окно 64.
  - NetworkCargoPresentation.cs:43,63-132 — omission сегодня уничтожает view и Find остаётся
    линейным; при 50/200/500 это 38,250 / 603,000 / 3,757,500 сравнений/с при 30 Hz.
  - CargoBody.cs:58-59,439-491,555-557 — словарь уже есть, world шагается независимо от active.
  - AlarmClockCargoThing.cs:67-76 — RemainingSeconds уменьшается каждый такт.
  - IntegratedHouse.unity:4-12; FirstHouse.prefab — baked occlusion отсутствует; 132
    MeshRenderer, 0 LODGroup, 296 объектов со static flags 0. NetworkCargoPresentation.cs:45-60
    пишет transform каждого view каждый frame, включая покой.
  - HouseBuilder.cs:718-755 — hinge/leaf уже разнесены, но вся физика двери намеренно снята из-за
    трёх расходящихся путей столкновения/навигации.

  Официальные первичные документы:
  - FishNet TimeManager:
    https://fish-networking.gitbook.io/docs/fishnet-building-blocks/components/managers/time-manager
  - FishNet RPC/channels:
    https://fish-networking.gitbook.io/docs/guides/features/network-communication/remote-procedure-calls
  - FishNet SyncTypes, SyncList и observers:
    https://fish-networking.gitbook.io/docs/guides/features/network-communication/synchronizing
    https://fish-networking.gitbook.io/docs/guides/features/network-communication/synchronizing/synclist
    https://fish-networking.gitbook.io/docs/guides/features/observers
  - Unity manual: script-driven physics, sleeping, solver cost, CCD, occlusion and SRP Batcher:
    https://docs.unity3d.com/ja/2023.2/ScriptReference/SimulationMode.Script.html
    https://docs.unity3d.com/ja/current/Manual/physics-optimization-cpu-rigidbody-sleeping.html
    https://docs.unity3d.com/jp/current/Manual/physics-optimization-cpu-rigidbody-solver.html
    https://docs.unity3d.com/cn/current/ScriptReference/Rigidbody-collisionDetectionMode.html
    https://docs.unity3d.com/es/current/Manual/OcclusionCulling.html
    https://docs.unity3d.com/cn/2021.2/Manual/SRPBatcher.html

  Сравнительные приёмы, отделённые от проектного решения:
  - GDC, affordance через форму/ручку:
    https://media.gdcvault.com/GDC%2B2022/Speaker%2BSlides/VFXasagamedesignlanguage_Nguyen_An-Tim.pdf
  - Rare, prompt только при взгляде и в радиусе:
    https://athsupport-rare-prd.web.msrareservices.com/articles/360011910520-Support-for-Locking-Interact-Prompts-into-View
  - Xbox XAG 103, не полагаться на один цвет и дублировать канал:
    https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103

  Пять независимых read-only разборов: current-code recheck, FishNet/transport, Unity physics/render,
  comparative signifiers, strategic alternatives; шестой fresh-context same-family validator пытался
  опровергнуть пять claims. Он опроверг снятие runtime-части и строгую очередь A-before-all-B;
  достаточность решения A, готовность дверцы и совместимость state lifecycle оставил INCONCLUSIVE.
state_changes: |
  1. Сохранить этот полный RESULT в history.
  2. В c-research-g-5a7c-interactive-density-001 записать receipt части 1 и оставить status ready:
     часть 2 с runtime-профилем всё ещё нужна после волны; слот сейчас не берётся.
  3. Обновить i-all-cargo-travels-every-tick-001 по current main: 45 B для малого id вместо
     57-60, configured 30 Hz, статические 50/200/500 числа и точная граница «полный baseline /
     sparse lifecycle»; evidence = этот RESULT. Issue остаётся открытым до B1 и runtime-замера.
  4. В журнал i-three-snapshot-fields-ride-and-nobody-reads-them-001 записать найденную мину:
     compare-all-fields с уменьшающимся RemainingSeconds сохраняет тиковый трафик; до C/D нужен
     глобальный lifecycle + catch-up или атомарный клиентский потребитель, а room interest не может
     скрывать игровые start/end.
  5. NOW, ставка, статусы других CALL, слоты и продуктовый репозиторий не менять.
captures: |
  - B0 может идти параллельно A; B1 ждёт A + beam. Клиентский dictionary логично входит в B0/B1,
    потому что серверная половина старого «двух словарей» уже сделана.
  - C не должна просто «сравнить все текущие поля»: RemainingSeconds создаёт 30 dirty updates/с.
    Нужен глобальный жизненный цикл игрового состояния с baseline/catch-up, отделимый от будущего
    комнатного потока поз; конкретный wire HOW остаётся инженерии.
  - Решение B (локальный косметический полёт) остаётся contingency только после красного runtime
    порога: p95/p99 dirty records, split queue/latency и settle correction.
  - Приёмы различения интерактивного от фона: семантическая форма как база, тихий focus cue как
    однозначность, optional scan как второй канал, действие/звук/след как подтверждение. Постоянный
    контур всего и отдельная физика каждой детали отвергнуты.
decisions_needed: []
confidence_and_limits: |
  Высокая уверенность в current code flow, configured 30 Hz, serializer arithmetic, MTU/split,
  O(N^2) presentation и отсутствии текущего client state consumer. Средняя — что sparse delta
  достаточно обычной плотности. Не установлены настоящие wire bytes, tick retention под нагрузкой,
  simultaneous movers, physics ceiling, final-photo-model render ceiling и target-hardware frame time.
  Это и есть обязательная runtime-часть 2 после освобождения слота волной.
play_check:
  - 1 Recite: done — обслужены восемь вопросов CALL в части 1; runtime-часть явно не подменена арифметикой.
  - 2 Investigate: done — только чтение current product main, embedded FishNet, официальных Unity/FishNet источников и сравнительных материалов; пять независимых генераторов сведены и дедуплицированы.
  - 3 Confidence: done — STATED/DERIVED/INFERRED/UNKNOWN разделены; перечислены измерения, способные изменить ответ.
  - 4 Close: checkpoint — часть 1 возвращена родителю, но CALL не закрыт: fresh-context refutation доказал необходимость части 2. Binding G5 не заявлен и не нужен для незакрытого claim.
log: часть 1 перепроверена на current main — 50/200/500 дают статически 70.7/277/691 KB/s на клиента, exact-delta вероятно хватает обычной плотности, но массовый каскад и потолки требуют runtime; B0 можно вести параллельно A
next: |
  return-to-g-5a7c; research CALL остаётся ready только на runtime-часть 2 после волны.
  В отдельной продуктовой ноге B0 может готовиться параллельно ремонту A; B1 ждёт A + beam.

END_OF_FILE: live/indie-game-development/history/2026-08-20-s-research-g-5a7c-interactive-density-part1-recheck-001.md
