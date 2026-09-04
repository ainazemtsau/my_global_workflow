# RESULT — s-repair-i-householder-core-journal-dedup-001

direction: indie-game-development
track: —
play: repair
node/task: g-5a7c / i-householder-core-has-no-memory-carrier-001
date: 2026-09-02

outcome: |
  Карточка `i-householder-core-has-no-memory-carrier-001` снова читается всеми
  читателями: повторный заголовок `## журнал` снят, а все прежние записи и текст
  журнала сохранены без изменения.

evidence: |
  До ремонта `rg -n "^## "` показал два раздела `журнал` на строках 42 и 50, а
  `uv run --locked python panel/test_readers.py` загрузил 458 из 459 карточек.
  После точечной правки та же приёмка принята: «загружаются обе папки: живых 177,
  закрытых 282, загружено 459». Дифф целевой карточки удаляет ровно строку второго
  заголовка; `git diff --check` чист.

state_changes: |
  1. В `live/indie-game-development/cards/i-householder-core-has-no-memory-carrier-001.md`
     слить два последовательных блока `## журнал` в один: удалить только второй
     заголовок, сохранить весь текст обоих блоков байт-в-байт и оставить трейлер.
  2. Добавить в журнал этой карточки одну строку этой ноги через `osctl leg close`;
     сохранить полный RESULT в `history/2026-09-02-s-repair-i-householder-core-journal-dedup-001.md`.
  3. Добавить одну строку в `os/FRICTION.md`: повтор уже открытого
     `watch:osctl-accepts-what-it-cannot-rewrite`; `osctl.py` этой ногой не менять.

captures:
  - Повтор известной OS-дыры направлен в отдельный MAINTENANCE REQUEST; лечение здесь не расширяется.

decisions_needed: []

play_check:
  - 1 назвать противоречие: done — карточка против схемы с одним `## журнал`; панель отказывается её читать.
  - 2 восстановить: done — git и текст карточки подтверждают, что второй заголовок отделяет позднюю запись, а не дублирует её.
  - 3 предложить исправленное состояние: done — убрать единственный повторный заголовок, не удаляя записи.
  - 4 подтверждение владельца: не требуется — `dedup` и schema-shape fix прямо отнесены repair к гигиене; запуск дан словами владельца «давай исправим проблему».
  - 5 трение: done — повтор занесён под уже существующим watch без правки OS.

log: repair i-householder-core-has-no-memory-carrier-001: второй заголовок «журнал» снят без потери записей; test_readers снова читает карточку

next: |
  От владельца по этому ремонту ничего не нужно. Отдельный MAINTENANCE REQUEST остаётся только для отказа `osctl` на повторном имени блока.

END_OF_FILE: live/indie-game-development/history/2026-09-02-s-repair-i-householder-core-journal-dedup-001.md
