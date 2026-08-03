# CALL — c-exec-host-rustle-and-urgent-guard-proba-001

to: executor
kind: engineering
repo: ainazemtsau/GasCoopGame
engineering_contract: 36
mode: ПРОБА — режим по умолчанию контракта 36; ОПОРА здесь не включена.
basis: `37519f526d89d6bb5f8aad658b9e2e3176700bac` — заново подтверждённые
       `origin/main` и `origin/dev` 2026-08-03
direction: indie-game-development
node: g-6b13
task: b-3
track: хозяин
issued: 2026-08-03 by s-work-g-6b13-b3-additional-reactions-issued-001
status: ready

## slot

**WIN-U1**, каталог `C:\projects\Unity\GasCoopGame_win-u1`, ветка `slot/win-u1`.

Непосредственно перед выпуском общий state-authority
`C:\projects\Unity\GasCoopGame_slot-state\gascoop-slot-state.v1.json` показал для WIN-U1
`AVAILABLE / lease none / endpoint unrecorded`. Checkout уже стоит на exact basis `37519f52`,
`git status --porcelain` пуст, `Temp/UnityLockfile` и `Library/EditorInstance.json` отсутствуют,
три разрешённых skip-worktree config-файла на месте. Остальные три слота тоже свободны, но U1
выбран потому, что уже содержит принятый хозяинский стенд и не требует обновления.

До любой записи исполнитель заново запускает настоящий selector для WIN-U1 и берёт только lease
`c-exec-host-rustle-and-urgent-guard-proba-001:BUILD`. Если selector, basis, branch, cleanliness
или Editor state уже отличаются — STOP домой; другой слот самостоятельно не выбирать.

## goal

В существующей сцене `HostWalksHisDay` к принятой реакции b-2 добавлены ровно две выбранные
владельцем реакции. Все три проходят через тот же event → noticed fact → decision policy →
physical action → local memory → return-to-life шов.

**A — тихий шорох → остановиться и прислушаться.** Действие команды создаёт короткий неясный
шорох без координаты. Хозяин запоминает конкретный occurrence, при ближайшей безопасной точке
прерывания останавливается в текущем месте на короткое настраиваемое время, чтобы услышать
повтор, отмечает этот occurrence обработанным и продолжает прежние occupation + step.

**B — серия громких ударов → срочно занять точку и караулить.** Несколько громких повторных
ударов также не несут координату. Этот факт имеет приоритет выше первой реакции b-2 и может
прервать обычную жизнь немедленно, даже вне её безопасной фазы. Хозяин быстрее идёт к уже
существующей сценовой `Listening Point`, ненадолго остаётся там, чтобы перекрыть источник,
отмечает exact occurrence обработанным и возвращается к сохранённым occupation + step.

Обе реакции удобно и честно вызываются из существующего Unity Inspector тем же общим входом,
которым позднее воспользуется игра. Live trace показывает факт, priority/safety, действие с
целью и причиной, активную фазу памяти и возврат. Inspector ничего не командует напрямую.

## owner verdict

Владелец получил три пары с ценой каждой и твёрдую рекомендацию A+B. Выбранные определения были
показаны ему до ответа: A — тихий шорох, безопасная остановка и прислушивание на месте; B — серия
громких ударов, немедленный срочный поход к существующей точке и короткий караул; у обеих exact
occurrence, локальная память и возврат к прежней жизни.

Его фактический ответ дословно: **«принимаю A+B»**.

Это разрешает только эти две реакции и не является разрешением на третью реакцию, игровой объект,
планировщик или общий AI framework.

## context

- Принятая основа b-2: `docs/results/c-exec-host-board-creak-reaction-proba-001.md` на basis
  `37519f52`; binding Direction PASS —
  `live/indie-game-development/history/2026-08-03-s-work-g-6b13-b2-close-verification-001.md`.
- Словарь владельца: `live/indie-game-development/knowledge/host-shared-vocabulary.md` —
  намерение, замеченный факт, правдоподобная смена приоритета, физическое действие, локальная
  память, возвращение к жизни.
- На basis существуют: `Assets/TunnelCrew/Core/Householder/Householder.cs`,
  `Assets/TunnelCrew/World/HouseholderRouteController.cs`,
  `Assets/TunnelCrew/Editor/HouseholderRouteControllerEditor.cs`,
  `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity`, host settings/asset и
  `tests/TunnelCrew.Core.Tests/HouseholderTests.cs`.
- `validation.config` несёт `synced_contract_version: 36`; ПРОБА — default. Unity —
  6000.5.5f1. Existing b-2 report, selector, scene, Core, controller, editor, settings и tests
  разрешены из exact Git tree непосредственно перед выпуском.

## invariant preserved

- `BoardCreaked → SuspiciousNoise → WalkToward(ListeningPoint) → return` остаётся первой
  production-реакцией с прежним безопасным прерыванием, acknowledgement, expiry и no-loop.
- Добавляются данные двух фактов/приоритетов, две policy-ветки и только необходимые action phases
  и tuning. Центральный переход остаётся одним `Householder.Step`; event ingress, occurrence
  memory, policy boundary, action execution и ReturnToLife не обходятся и не дублируются.
- Unity-controller может получить только необходимые authoring/input поля и Inspector triggers.
  Его роль неизменна: поставить event, передать scene/tuning в Core, сохранить возвращённую память
  и показать возвращённую позицию. Веток выбора, priority, expiry, acknowledgement и return в
  MonoBehaviour/Editor нет.

## boundaries

- Ровно две новые реакции A+B. Не менять смысл или видимое поведение b-2 и не добавлять четвёртую.
- Никаких Behavior Tree, GOAP/planner, utility system, action catalog, preconditions/effects/costs,
  очереди планов, общего склада фактов, обучения, профилей хозяев или универсального behavior
  framework.
- ПРОБА не расширяет память до нескольких одновременных facts. A и B принимаются независимо на
  обычной жизни; владелец не выбирал, какая из разных реакций должна победить другую. Не строить
  очередь/арбитраж и не придумывать этот игровой ответ: если без него A+B нельзя добавить через
  текущий однофактовый шов, STOP HOME с точным вопросом владельцу.
- Никаких игроков, сети, груза, тоннеля, копания, арта, новых игровых объектов, комнат/регионов,
  зрения, анимации, NavMeshAgent, Rigidbody/physics movement или runtime debug UI. A использует
  текущее место, B — существующую `Listening Point`.
- Не менять `Packages/**`, `ProjectSettings/**`, `tools/**`, `validation.config`, `AGENTS.md` или
  полосу переноски. Odin не импортировать.
- Разрешённая поверхность: `Assets/TunnelCrew/Core/Householder/**`,
  `Assets/TunnelCrew/World/Householder*`, `Assets/TunnelCrew/Editor/Householder*`, только
  `Assets/TunnelCrew/Scenes/HostWalksHisDay.unity`, `Assets/TunnelCrew/Settings/Householder*`,
  `tests/TunnelCrew.Core.Tests/Householder*.cs`, обязательные `.meta` и собственный
  `docs/results/c-exec-host-rustle-and-urgent-guard-proba-001.md`.
- Время прислушивания, скорость срочного движения, время караула и lifetimes — tuning fields,
  а не константы и не значения, зацементированные тестами.
- Видимое проверяет владелец глазами. Headless evidence проверяет только невидимые priority/safety,
  occurrence/expiry/handled/no-loop, phases, exact return и прохождение всех трёх реакций через
  один seam. Unity Editor/import/Play недоступны — STOP, не заменять source scan-ом.

## done_when

1. В Unity Editor владелец во время обычного маршрута вызывает тихий шорох: факт виден сразу,
   хозяин ждёт ближайшего безопасного прерывания, останавливается и прислушивается на месте, затем
   продолжает exact сохранённые occupation + step; live trace показывает priority/safety,
   occurrence, action/cause/target, handled/expiry и return.
2. Владелец вызывает серию громких ударов во время небезопасной фазы обычной жизни: хозяин
   немедленно прерывается, заметно быстрее идёт к существующей `Listening Point`, коротко караулит
   и возвращается к exact сохранённым occupation + step; факт не несёт координату и не запускается
   по кругу.
3. Принятая реакция b-2 по-прежнему проходит без изменения смысла, а engine-free evidence
   подтверждает, что все три реакции используют один event/fact/policy/action/memory/return seam и
   Unity-adapter не принимает решений; focused tests, Unity 6000.5.5f1 import/compile, обычный
   `tools/check.ps1` и scoped diff зелёные.

## return

Возврат ДОМОЙ в `indie-game-development`, g-6b13 / b-3 / хозяин, только после полного живого цикла
ПРОБЫ в продукте. Тюнинг после первого Play остаётся внутри этой продуктовой сессии.

Terminal HOME называет candidate/merge/published commits, результаты focused tests, Unity
import/compile, обычного check и diff-check, пути сцены и собственного отчёта, exact слова
владельца после проверки обеих реакций и повторной проверки b-2, а также terminal selector
evidence `WIN-U1 CLEAN / AVAILABLE / lease none`. Собственный report до интеграции честно не
называет себя `DELIVERED on dev`; статус меняет интеграция после exact-parent merge и publish.

Product delivery, owner-eye, merge и зелёные проверки сами по себе не закрывают b-3. Direction
оставляет задачу open до отдельной fresh physical G5-рефутации всех трёх пунктов done_when.

budget: one small visible PROBA root; two additional reactions on one existing host stand. If it
requires a framework, new world dependency or wider surface, STOP HOME with one exact blocker.

END_OF_FILE: live/indie-game-development/work/c-exec-host-rustle-and-urgent-guard-proba-001-call.md
