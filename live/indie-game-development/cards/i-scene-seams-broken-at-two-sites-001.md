---
id: i-scene-seams-broken-at-two-sites-001
_kind: issue
_pos: 26
level: execution
route: work
---

## issue
Критерий 8 закрытой волны опровергнут в двух местах, оба измерены на `352f96b0`. (1) СКРЫТАЯ ССЫЛКА МЕЖДУ КОРНЯМИ: `World/DeliveryPoint.cs:14` держит `static readonly List<DeliveryPoint> ActivePoints`, заполняет его в `Awake`, а судья читает его в `Network/NetworkWalkerCourier.cs:48-49`; реестра не видно ни в файле сцены, ни в инспекторе, и он подберёт любую точку из любой загруженной сцены. (2) Полоса доставки вписала продуктовую геометрию ПРЯМО В СЦЕНУ (правка экземпляра восточной стены плюс сценовый ребёнок `Outer East South`), поэтому `World/ThreeRoomHouse.prefab` в одиночку больше НЕ воспроизводит сданный дом — из заготовки выходит глухая коробка без выхода.

## review_when
Когда появится вторая точка доставки, ЛИБО когда узел настоящего ядра заново соберёт дом: тогда статический реестр заменяется сериализованным полем, а выход переезжает в заготовку. Отдельной ноги на это не заводить — прямое решение владельца 2026-08-07.

## evidence
history/2026-08-07-s-review-g-1d84-integrated-house-partial-001.md §evidence; `352f96b0:Assets/TunnelCrew/World/DeliveryPoint.cs:14,68`, `Network/NetworkWalkerCourier.cs:48-49`, `Scenes/IntegratedHouse.unity`.

END_OF_FILE: live/indie-game-development/cards/i-scene-seams-broken-at-two-sites-001.md
