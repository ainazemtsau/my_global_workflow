# RESULT — s-work-g-6b13-a4-close-verification-checkpoint-002

call: c-work-a4-close-verification-002
direction: indie-game-development
track: переноска
play: work
node/task: g-6b13 / a-4
date: 2026-08-04

## outcome

verdict: CHECKPOINT

Binding fresh G5 в отдельной физической Direction-сессии сопоставила все три пункта исходного
инженерного `done_when` с exact published `839df47e`, попыталась их опровергнуть и нашла один
последний owner-eye разрыв. Задача a-4 остаётся open.

Пункты 1 и 3 выдержали refutation. В пункте 2 код и история подтверждают физическое тело, стены,
проём и плоскую сцену; владелец теперь явно подтвердил столкновение балки и упор мыши в стену. Но
он не сказал, что видел обе ориентации: поперёк балка не прошла/упёрлась или развернулась, а вдоль
прошла. Его прямое пожелание «давай как бы там сильно не душнить, как бы закрывать» сохранено как
owner verdict, но не превращено в отсутствующее наблюдение.

Returning CALL снят. Один same-lane root переведён в `waiting` только на это наблюдение; нового
немедленного вопроса, продуктовой работы или повторной интеграции нет.

## evidence

1. **Owner words — второй хват после тюнинга.** В ответ на точный вопрос владелец сказал:
   «У второй, ну я не заметил проблем. Ну не сказать, что я там прям супер тестировал.» В контексте
   заданного пункта это явное наблюдение отсутствия прежней проблемы у второго игрока, без усиления
   до более тщательного теста, чем он описал.
2. **Owner words — стена и балка.** Владелец сказал: «банк упёрлась просто как физический объект,
   мышь упёрлась тоже в стену». Ответ дан на пункты о балке и мыши: он явно подтверждает физическое
   столкновение и то, что мышь не вошла в стену. Фраза не называет ни поперечное положение, ни
   продольный проход, поэтому полное различие ориентаций из неё не выведено.
3. **Owner close verdict не подменяет факт.** Его слова: «Ну всё, ну то есть я посмотрел, эти примерно
   работает, давай как бы там сильно не душнить, как бы закрывать, что да, если проблемы будут,
   потом дальше будем смотреть.» Это настоящий owner-readable вердикт и он процитирован как есть;
   G5 всё равно не может закрыть составной owner-eye пункт, которого в рассказе нет.
4. **Exact publication/history.** Fresh local refs: `origin/main` = `origin/dev` =
   `839df47e78127fe2ebfba5eabb307bf6bdd61e9b`. Merge `c26c2e08` имеет parents
   `8da649430e5d9b55baadefc23a01519380863216` и
   `4f3cbc1cfe1bfab9cb211a311415459af0f41565`; `4f3cbc1c` имеет parent `dc5d48b0`.
   Относительно host-parent merge меняет ровно
   `Assets/TunnelCrew/Network/NetworkPlaySettings.asset` и
   `Assets/TunnelCrew/Scenes/NetworkWalkers.unity`; `839df47e` меняет только честный report.
5. **Exact published stand.** Settings blob =
   `f750868c2b8d423ef678b6aedc09f31c808aa952`, scene blob =
   `4c7b224b98b0e98dff508a65eaec4fc9d721c05c`. Прочитанные значения: half-extent 7
   (комната 14×14), divider `z=5`, doorway 2, cargo 2.4×0.5, cargo spawn `z=2.5`, camera minimum 9;
   Floor transform имеет scale 1.6, то есть 16×16. `git diff --check` для merge и report чист.
6. **Пункт 1 — двое, одно тело, хват и срыв.** `CargoHaul.Reduce` сводит список любой длины в одну
   силу/точку/остаточный torque; `AuthoritativeCargoRoster` берёт разные концы, ограничивает число
   держателей настройкой, разрывает растянутую связь и никогда не задаёт позицию мыши. Один server
   `CarryWorld` отдаёт ходоков и cargo одним snapshot; host и client применяют ту же позу. Тесты
   `TwoCarriersTakeHoldOfTheEndsTheyAreStandingAt`,
   `WalkingTooFarLetsGo_AndTheWalkerNeverStumbles`, `AGripNeverMovesItsHolder` и тесты сведения
   существуют на candidate; их blobs не менялись до published tip. Product report фиксирует
   owner-eye первого круга и recorded focused run 38/38.
7. **Пункт 2 — физика/стены/плоскость и точный пробел.** Только серверный `CargoBody` создаёт
   Rigidbody с ContinuousDynamic и замораживает Y, наклон X/Z; `CarryStand` строит четыре стены и
   divider из двух сегментов вокруг проёма; те же стены читает аналитический `WalkSpaceProbe` для
   кинематической мыши. Код опровергает проход насквозь как задуманную форму, а нынешние слова
   владельца подтверждают столкновение балки и стены мыши. Но ни код, ни tests, ни общий вердикт не
   заменяют его глаза на различие «поперёк не проходит / вдоль проходит» — это единственный gap.
8. **Пункт 3 — расслоение и checks.** На basis и published tip четыре movement blobs одинаковы:
   `6427b8091e84a92930402d4fc014b67c9dce0715`,
   `2346fe651cff9e79bccdd9502a27b93028664813`,
   `bfe9aa1dd6cb50271e37b8b27027ef3a5cedc21b`,
   `df4a754f6a34940962034fd67b18c0ffcfedc31a`. Courier сохранил один NetworkObject и прежние RPC,
   а порядок/правила живут в `CarryWorld`; cargo test blobs candidate→tip неизменны. Report фиксирует
   focused tests 38/38, обычный `tools/check.ps1` GREEN и scoped diff целиком в разрешённой
   поверхности. На exact tip добавлены пять disjoint host-тестов (43 `[Test]` в source), а 38
   candidate-тестов и оба cargo test blobs сохранены без изменений.
9. **Ограничения не спрятаны.** `AuthoritativeCargoRoster.DeriveVelocity` по-прежнему выводит скорость
   из разницы поз; два тика в одном low-FPS кадре могут потерять гашение — отдельное решение не
   принималось. Unity MCP не подключался: shared slot-state даёт `mcp_endpoint: unrecorded`; evidence
   import/compile заменено фактическим запуском и игрой владельца, как прямо разрешённая эскалация.
10. **Terminal read-only state.** WIN-U3 стоит на exact `839df47e`, Git status clean; shared state
    `AVAILABLE / lease none / endpoint unrecorded`, `Temp/UnityLockfile` отсутствует. Продуктовый
    репозиторий этой G5 не менялся, проверки с записью `bin/obj` не перезапускались; сверены committed
    run evidence и exact source/history.

## state_changes

- `NOW.md`: по stable task id `a-4` сохранить `status: open`; заменить
  `close_verification_checkpoint` на этот exact binding CHECKPOINT с owner words, verified
  tip/blobs, low-FPS/MCP оговорками и единственным пробелом ориентаций; обновить `updated`.
- `NOW.md/open_calls`: удалить returning `c-work-a4-close-verification-002`; зарегистрировать один
  same-lane root `c-work-a4-doorway-orientation-verification-003` со статусом `waiting` и точным
  `waiting_on` только на owner-eye различие поперёк/вдоль.
- `NOW.md/decisions[d-first-person-before-the-build-001].when`: заменить устаревший current-root id
  на waiting continuation; содержание решения и границы a-4b сохранить.
- Создать полный
  `live/indie-game-development/work/c-work-a4-doorway-orientation-verification-003-call.md`.
- Препендить один LOG receipt и сохранить этот полный RESULT в
  `history/2026-08-04-s-work-g-6b13-a4-close-verification-checkpoint-002.md`.
- CHARTER.md, TREE.md, knowledge, issues, forecast, соседнюю полосу и product repo не менять.

## captures

Нет.

## decisions_needed

Нет.

## play_check

- 1 recite: done — текущая задача a-4 активной ставки, exact returning CALL и исходный инженерный
  done_when перечитаны из fresh state.
- 2 owner inputs (owner): done — владелец фактически сказал «У второй, ну я не заметил проблем»,
  «мышь упёрлась тоже в стену», про балку — «банк упёрлась просто как физический объект», и вынес
  вердикт «давай как бы там сильно не душнить, как бы закрывать»; ни одна фраза не усилена.
- 3 do the work: done — read-only сопоставлены exact refs/graph/blobs, settings/scene, core/network
  source, committed tests/check report и terminal slot state; продуктовый репозиторий не менялся.
- 4 self-check: done — пункты 1 и 3 выдержали refutation; пункт 2 выдержал по коду и двум названным
  столкновениям, но не получил owner-eye различие поперёк/вдоль; low-FPS и MCP substitution видимы.
- 5 close: done — PASS не выдан, a-4 сохранена open, returning CALL снят, один same-lane root ждёт
  только отсутствующее наблюдение; a-4b не открыт преждевременно.

## log

g-6b13/a-4: binding fresh G5 выдержала exact code/history/report/checks и получила явные слова про
второй хват и стену, но не получила различие «поперёк не проходит / вдоль проходит»; a-4 остаётся
open, same-lane root ждёт только это наблюдение.

## next

CALL `c-work-a4-doorway-orientation-verification-003` (`waiting`) — после фактического наблюдения
владельца получить только последнее различие балки поперёк/вдоль. Никакой немедленной новой проверки
или продуктовой работы; только явные слова могут дать PASS и выпустить a-4b.

END_OF_FILE: live/indie-game-development/history/2026-08-04-s-work-g-6b13-a4-close-verification-checkpoint-002.md
