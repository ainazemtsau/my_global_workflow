# CALL — c-work-a4-close-verification-002

to: session
direction: indie-game-development
track: переноска
play: work
node: g-6b13
task: a-4
issued: 2026-08-04 by s-work-g-6b13-a4-publish-return-checkpoint-001
status: ready

## goal

У задачи a-4 есть честный binding fresh-session вердикт на точной опубликованной версии: PASS,
если все исходные обещания действительно подтверждены, либо один точный checkpoint без вывода за
владельца.

## context

- Текущее состояние: `live/indie-game-development/NOW.md`, задача `a-4`, поле
  `close_verification_checkpoint`.
- Исходный инженерный наряд с тремя обязательными пунктами:
  `live/indie-game-development/work/c-exec-two-carry-one-physical-cargo-proba-001-call.md`.
- Честный продуктовый отчёт:
  `docs/results/c-exec-two-carry-one-physical-cargo-proba-001.md`.
- Exact published tip: `origin/main` = `origin/dev` =
  `839df47e78127fe2ebfba5eabb307bf6bdd61e9b`. Merge `c26c2e08` сохраняет обоих родителей:
  актуальный host tip `8da649430e5d9b55baadefc23a01519380863216` и owner-tested stand tip
  `4f3cbc1cfe1bfab9cb211a311415459af0f41565`; `839df47e` добавляет честную правку отчёта.
- Exact runtime-блобы опубликованного стенда: settings
  `f750868c2b8d423ef678b6aedc09f31c808aa952`; scene
  `4c7b224b98b0e98dff508a65eaec4fc9d721c05c`. Комната 14×14, divider `z = 5`, camera minimum 9,
  cargo spawn `z = 2.5`, пол 16×16.
- Четыре movement blobs сохранены:
  `6427b8091e84a92930402d4fc014b67c9dce0715`,
  `2346fe651cff9e79bccdd9502a27b93028664813`,
  `bfe9aa1dd6cb50271e37b8b27027ef3a5cedc21b`,
  `df4a754f6a34940962034fd67b18c0ffcfedc31a`.
- Product evidence: focused tests 38/38; обычный `tools/check.ps1` GREEN; scoped diff чист и
  ограничен двумя runtime-файлами плюс отчётом; WIN-U3 `CLEAN / AVAILABLE / lease none`, без
  `UnityLockfile`, endpoint `unrecorded`.
- Владелец сказал: «Так, проверил в слоте 3, да, действительно есть балка, всё работает, как
  ожидается. Можем закрывать.» Это подтверждает, что исправленный стенд виден и переноска в целом
  работает, но продуктовый отчёт прямо фиксирует: в рассказе нет отдельных наблюдений про разворот
  балки в проёме и про мышь у стены; второй хват после тюнинга отдельно тоже не описан.
- Прежняя Direction-запись, будто общая фраза автоматически покрыла все три наблюдения, отозвана
  `s-work-g-6b13-a4-publish-return-checkpoint-001`. Нельзя восстанавливать этот вывод.

## owner facts still needed

Получить словами владельца ровно три факта — только если он их действительно видел:

1. После тюнинга второй игрок берёт тот же груз без прежней проблемы с хватом.
2. Балка поперёк не проходит через проём, упирается/разворачивается, а вдоль проходит.
3. Мышь упирается в стену и не входит в неё.

Если какой-то факт не наблюдался, это и есть точный checkpoint; общую фразу «всё работает» за ответ
не считать.

## boundaries

- Только read-only проверка exact published `839df47e` и Direction-close задачи a-4. В продуктовый
  репозиторий не писать; интеграцию не повторять.
- Не менять a-4b, первое лицо, вертикальность груза, полосу хозяина, известное low-FPS ограничение
  или текущие продуктовые байты.
- Не подменять owner-eye тестами, report-текстом или выводом из общей фразы. Не придумывать новых
  проверок сверх исходного `done_when`.
- Product delivery, merge/push, зелёные проверки и свободный слот — evidence, но не замена binding
  fresh-session G5.

## done_when

1. Все три пункта исходного инженерного `done_when` сопоставлены с exact published code/history,
   report и проверками и выдержали попытку опровержения; известное low-FPS ограничение и замещение
   Unity MCP не спрятаны.
2. Три перечисленных owner-eye факта имеют явные слова владельца; ни один не выведен из «всё
   работает». Если факта нет, RESULT называет только этот пробел и сохраняет a-4 open.
3. Полный Direction RESULT даёт PASS либо точный checkpoint. Только PASS закрывает a-4, снимает этот
   CALL и выпускает следующий ready same-lane engineering CALL на a-4b с уже записанными границами.

## return

Полный RESULT по play `work`: verdict PASS либо один точный checkpoint; evidence по каждому пункту;
state_changes только для a-4, этого CALL и законного same-lane handoff.

budget: one fresh physical session

END_OF_FILE: live/indie-game-development/work/c-work-a4-close-verification-002-call.md
