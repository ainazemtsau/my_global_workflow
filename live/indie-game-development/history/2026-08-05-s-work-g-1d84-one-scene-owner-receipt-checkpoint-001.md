# RESULT — s-work-g-1d84-one-scene-owner-receipt-checkpoint-001

call: c-exec-g-1d84-one-scene-what-exists-001
direction: indie-game-development
track: сцена
play: work
node/task: g-1d84 / t-scene-1
date: 2026-08-05

## outcome

CHECKPOINT — владелец принял старую сцену как структурную базу новой общей сцены; t-scene-1
остаётся active.

Дословные слова после Play — «вижу старую сцену по которой ношу балку». На показанную ему явную
развилку между принятием этой основы и переделкой отдельной сценой он ответил: «Принимаю базу».
Это закрывает визуальную неоднозначность и даёт owner-eye по Play / ходьбе / балке. Сила токена не
завышается: будущий вид дома, публикацию и binding G5 он не утверждает.

Runtime-candidate остаётся exact и не менялся после проверки владельца. Задача намеренно не
закрывается: продуктовый report всё ещё говорит, что owner Play pending; отдельной свежей binding
G5 не было; candidate не опубликован; в WIN-U1 после Unity появились семь посторонних
незакоммиченных путей. Returning engineering CALL заменён узким same-lane successor, который
дописывает только owner receipt в report и не поглощает этот working-tree diff.

## evidence

1. **Done_when 1 — candidate существует.** На базе
   `839df47e78127fe2ebfba5eabb307bf6bdd61e9b` commit
   `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f` сохранил GUID сцены
   `31d4e989f2353534182e51e1c86ef3e9`, переименовал
   `Assets/TunnelCrew/Scenes/NetworkWalkers.unity` в
   `Assets/TunnelCrew/Scenes/IntegratedHouse.unity` и перевёл две существующие ссылки. Поэтому
   существующие двое сетевых ходоков и физический груз собраны в одном runnable artifact, а не
   переписаны новой механикой.
2. **Done_when 2 — Play ведёт в candidate как judge.** Candidate меняет online-scene ссылку в
   `Assets/TunnelCrew/Network/Prefabs/NetworkRuntime.prefab` и build-settings ссылку на тот же GUID;
   Lobby не удалён. Владелец фактически нажал Play и попал в эту сцену без названного промежуточного
   экрана: «вижу старую сцену по которой ношу балку».
3. **Done_when 3 — слои не смешаны.** Runtime diff не добавляет и не меняет ни одного `.cs`, Core,
   Courier или network-rule файла; это rename scene/meta плюс две ссылки. Никакого нового правила
   игры в курьере нет, а engine/network-free Core остался побайтово на basis.
4. **Done_when 4 — старая папка и старые тесты не тронуты.** Candidate manifest не содержит старую
   папку. Запускался только `tests/TunnelCrew.Core.Tests/TunnelCrew.Core.Tests.csproj -c Release` —
   43/43; старые тесты не запускались. `tools/check.ps1` вернул hygiene OK.
5. **Done_when 5 — exact owner-eye.** Владелец: «вижу старую сцену по которой ношу балку»; затем
   «Принимаю базу». Это прямые слова, не пересказ и не вывод из молчания.
   `owner-ack:s-work-g-1d84-one-scene-owner-receipt-checkpoint-001#accept-base` разрешается в эту
   точную цитату и покрывает только принятие старой геометрии как основания.
6. **Candidate/report identity.** Runtime commit — `9113b24a9a9e753de702101b3dbf1eddcf1e8e0f`;
   первый report commit — `82a6a6c4e88a4d216e8fa1db092118acf66b5fff`. Report status дословно:
   `CANDIDATE on slot/win-u1; owner Play and fresh binding G5 pending`. Первая половина после слов
   владельца устарела; поэтому это checkpoint, а не полный product return.
7. **Чужой working-tree diff не присвоен.** После Play отдельно наблюдались семь modified paths:
   четыре NuGet/MCP DLL/receipt, два Packages-файла и `ProjectSettings/EditorBuildSettings.asset`;
   изменения показывали MCP/NuGet 0.86.2 → 0.87.0 и editor-сериализацию. Они не staged, не committed,
   не reverted и не включены в evidence candidate. WIN-U1 остаётся `CLAIMED`, lease
   `c-exec-g-1d84-one-scene-what-exists-001:BUILD`, endpoint `unrecorded`.
8. **Открытые гейты.** Fresh physical binding G5 отсутствует; `main` остаётся на
   `839df47e`; terminal report receipt отсутствует. Ни product commits, ни owner-eye, ни зелёные
   checks по отдельности не использованы как Direction-close.
9. **review:** n/a — light change. Отдельная свежая binding G5 остаётся обязательной после честного
   report receipt.

## state_changes

- `NOW.md`: по stable task id `t-scene-1` оставить задачу незакрытой, установить `status: active` и
  записать компактный checkpoint с exact owner words, candidate ids и тремя оставшимися гейтами;
  `updated` перевести на эту сессию.
- `NOW.md/open_calls`: удалить returning
  `c-exec-g-1d84-one-scene-what-exists-001`; зарегистрировать один ready same-lane successor
  `c-exec-g-1d84-one-scene-owner-receipt-001`, legacy lineage исходного CALL, для report-only
  owner receipt. Все другие tracks/calls сохранить по stable id без изменений.
- Создать полный CALL
  `live/indie-game-development/work/c-exec-g-1d84-one-scene-owner-receipt-001-call.md`.
- Препендить один LOG receipt и сохранить этот полный RESULT в history. CHARTER, TREE, knowledge,
  issues, decisions, forecast, соседние полосы, product repo и slot registry не менять.

## captures

- «Принимаю базу» означает принятие старой геометрии как основания. Это не обещание, что отдельный
  новый визуальный дом уже построен, и не разрешение приписать задаче Unity/MCP auto-upgrade.
- Текущая sandbox-authority этой физической сессии не разрешает запись в product checkout. Поэтому
  report не был тайно исправлен из Direction: выпущен точный successor, а семь чужих изменений
  сохранены нетронутыми.

## decisions_needed

Нет. Происхождение и судьба постороннего Unity/MCP diff этим RESULT не решаются; successor обязан
его сохранить и вернуть фактическое состояние, а не спрашивать разрешение на очистку.

## play_check

- 1 recite: done — исходный CALL, t-scene-1, candidate commits и обязательный owner-eye перечитаны.
- 2 owner inputs (owner): done — владелец сказал дословно «вижу старую сцену по которой ношу балку»
  и на явную развилку ответил «Принимаю базу».
- 3 do the work: done — точные owner words сопоставлены с пятью done_when; runtime candidate, report,
  checks, working-tree diff и slot lease разделены без присвоения чужих байтов.
- 4 self-check: done — report после owner words не терминален, fresh G5 и publication отсутствуют;
  поэтому t-scene-1 не помечена done.
- 5 close: done — returning engineering root заменён одним same-lane report-only successor; другие
  полосы и продуктовые байты не менялись.

## log

g-1d84/t-scene-1: владелец увидел старую сцену, походил с балкой и дословно «Принимаю базу»;
runtime-candidate 9113b24a принят глазами, но task оставлена active до честного report receipt,
fresh binding G5 и публикации, посторонний Unity/MCP diff не присвоен.

## next

CALL `c-exec-g-1d84-one-scene-owner-receipt-001` — в новой продуктовой задаче записать дословную
приёмку только в report поверх exact candidate, не трогая посторонний working-tree diff. Его
terminal HOME открывает отдельную свежую binding G5; task до этого не закрывать.

END_OF_FILE: live/indie-game-development/history/2026-08-05-s-work-g-1d84-one-scene-owner-receipt-checkpoint-001.md
