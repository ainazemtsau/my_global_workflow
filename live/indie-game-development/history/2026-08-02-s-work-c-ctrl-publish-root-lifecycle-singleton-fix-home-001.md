# RESULT — s-work-c-ctrl-publish-root-lifecycle-singleton-fix-home-001

call: c-ctrl-publish-root-lifecycle-singleton-fix-001
direction: indie-game-development
track: переноска
play: work
node/task: g-6b13/c-1b
date: 2026-08-02

## outcome

Исправление singleton frozen entries опубликовано отдельно от feature-задачи: actual product
`origin/main` указывает на standalone tooling-коммит `2a19cb40`, а U3 на `7ef702ae` включает его
merge-коммитом поверх неизменённой принятой PLAN-линии. Задача c-1b закрыта. Родитель a-1b не
закрыт и не запущен: он лишь снова готов к отдельному запуску со стадии `PAIR-CANDIDATE`.

## evidence

- Done_when 1 — actual main: удалённый readback `git ls-remote origin refs/heads/main` вернул
  `2a19cb40fbf6be3b9791c8c2d25c9861401f964d`; его единственный родитель — `c75015a8`.
  `c75015a8..2a19cb40 -- tools/** validation.config` меняет только
  `tools/root-lifecycle-check.ps1` (+26/-3), а stable patch-id
  `0eb1d19688e96f136430722715f55b898b31b027` совпадает с `ad42b2d8`.
- Done_when 2 — чистая U3-линия: `7ef702ae` имеет родителей `f7387751` и `2a19cb40`;
  `7c5fc5a6` и `f7387751` разрешаются и являются предками. `f7387751..7ef702ae` полностью пуст,
  `2a19cb40..7ef702ae -- tools/** validation.config` пуст.
- Done_when 3 — проверки и custody: повторно на U3 GREEN
  `tools/root-lifecycle-check.ps1 -SelfTest`, `-Repo . -Scan` и `tools/check.ps1`
  (`OK: all active gates green`). U3 и main checkout прочитаны чистыми. HOME дополнительно
  сообщает independent read-only PASS, `integrating: 0`, `preparing: 0`, все WIN-U1..WIN-U4
  `CLEAN / AVAILABLE / lease none / endpoint unrecorded`, а WIN-CTRL и WIN-MAIN чистыми.
- `check.ps1 -Deliver` в HOME остановился только на обязательном feature RESULT-файле; CALL запрещал
  feature REPORT и любые изменения сверх exact fix, поэтому это не cut и не незакрытый done_when.
- review-evidence: n/a — light standalone tooling publication; HOME при этом несёт отдельную
  independent read-only сверку PASS.

## state_changes

- `NOW.md`: c-1b `active → done` с точными main/U3 SHA и проверками; a-1b `blocked → open`, потому
  что единственный технический prerequisite выполнен, но никакой product-run не запущен.
- `NOW.md/open_calls`: удалить возвращённый child
  `c-ctrl-publish-root-lifecycle-singleton-fix-001`; у его прямого родителя удалить `waiting_on`,
  добавить эту history-квитанцию и поставить `ready`, так как иных child waits нет. Обновить basis,
  U3 tip и note; сохранить все чужие calls без изменений.
- `work/c-exec-rules-layer-and-single-walker-001-call.md`: редакция 4 фиксирует принятый HOME,
  standalone main commit и U3 merge-tip; следующий отдельный запуск начинается с
  `PAIR-CANDIDATE`, не с BUILD.
- `LOG.md`: добавить одну строку этой ноги. CHARTER, TREE, knowledge, archive, os/** и product bytes
  не менять.

## captures

None.

## decisions_needed

None.

## play_check

- 1 Recite: done — задача c-1b служит текущей ставке g-6b13 и отделяет tooling prerequisite от
  feature-задачи a-1b.
- 2 Owner inputs (owner): skipped — владелец уже передал полный HOME с точными SHA; нового
  продуктового решения или разрешения на запуск эта нога не требует.
- 3 Do the work: done — HOME сопоставлен с CALL; remote SHA, ancestry, patch-id, scoped diffs и
  активные проверки перепроверены read-only.
- 4 Self-check: done — у каждого из трёх done_when есть отдельная evidence-линия; принятые PLAN/ADR
  и receipts не изменены, feature stages и BUILD не запускались.
- 5 Close: done — возвращённый child очищается один раз, его receipt добавляется прямому родителю,
  который становится ready без автоматического запуска.

## log

g-6b13/c-1b: singleton-fix опубликован отдельно на main; U3 очищен без переписывания PLAN, родитель готов к отдельному PAIR-CANDIDATE

## next

return-to-parent c-exec-rules-layer-and-single-walker-001 — родитель ready; ждать явных слов
владельца на запуск, ничего продуктового автоматически не начинать.

END_OF_FILE: live/indie-game-development/history/2026-08-02-s-work-c-ctrl-publish-root-lifecycle-singleton-fix-home-001.md
