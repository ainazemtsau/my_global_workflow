# RESULT — s-repair-g-5a7c-hot-state-cleanup-001

direction: indie-game-development
track: —
play: repair
node/task: g-5a7c / live-hygiene
date: 2026-09-02

outcome: |
  Горячее состояние направления освобождается от неактуального концепта
  Only Vermin Know и одиннадцати бесхозных задач прежних волн. Экспертиза
  не уничтожается: карточки уходят в closed, а единственный смешанный
  knowledge-файл — в защищённый архив, который не читается без отдельного
  подтверждения владельца.

  Concept Lab остаётся единственным домом концепта. В Direction закрепляется
  только квитанция неизменяемых входов текущей волны 11. Текущая волна,
  её задачи, статусы, вырезы и полные материалы Fable-аудита не меняются.

evidence: |
  На свежем HEAD 73d007d2 рабочее дерево чистое. Параллельный коммит меняет
  только i-householder-core-has-no-memory-carrier-001, его history и
  os/FRICTION.md; пересечения с этим пакетом нет.

  Все 11 перечисленных задач остаются живыми, не имеют track и не имеют
  одноимённых карточек в closed. Их суммарный объём — 6 821 слово.
  Knowledge-файл the-game-changed-to-only-vermin-know.md по-прежнему имеет
  blob d53a1275f1e518c1d766db151ff36261d911389b и ложную область чтения для
  любой ноги, планирующей содержание.

  Свежие blobs целевых карточек:
  bet-g-5a7c-wave-11 — 3bfafbce365ad93d0af32d17b8f087013754d2b5;
  q-fable-audit-decisions-2026-09-02 —
  7bf9bc2d198fd1f08be3862129d2a4aaf148bf0f;
  direction_forecast — 5f89e8c3293d267532a6859569ffd2c88aa963c0f.

  Неизменяемый вход волны подтверждён квитанцией Concept Lab:
  schema concept-lab/owner-approved-export-v1; EXP-20260831-001;
  candidate CAND-0010; immutable true; body_sha256
  cf3bd95a6b11c44d449f06bfa570a081d91ee1b76ce0997927f379cd3ed29f55;
  owner quote «принмаю». Спека давления
  work/2026-09-01-spec-time-pressure-from-concept-lab.md имеет SHA-256
  4AF16FD958D6AF7C9E12DF8FCA3FF038A7D6680A2B4619D671639BEC8115581A
  и принята владельцем словами «Так, я утверждаю», но не имеет EXP-квитанции,
  поэтому допустима только как legacy-вход уже идущей волны.

  Владелец сначала выбрал пакет словами «давай пункт 1», затем утвердил
  показанный точный состав ответом «да».

state_changes: |
  1. Переместить без изменения байтов
     live/indie-game-development/knowledge/the-game-changed-to-only-vermin-know.md
     в archive/directions/indie-game-development/2026-09-managed-reset/knowledge/
     the-game-changed-to-only-vermin-know.md.
     Архив не становится обычным источником чтения.

  2. Закрыть как superseded карточку t-irritation-1, указав
     superseded_by: t-the-morning-has-a-reserve-1.

  3. Закрыть как dropped следующие десять карточек:
     t-basement-1, t-cargo-delta-1, t-cargo-state-lifecycle-1,
     t-cargo-tuning-safety-1, t-dropmodel-1, t-handlers-1, t-hands-1,
     t-house-asset-1, t-loot-models-1, t-rooms-content-1.
     Причина для каждой: задача не допущена в волну 11 и не входит в текущий
     concept basis; технические улики остаются в закрытой карточке, history
     и существующих issue, а будущая shape обязана вывести потребность заново.

  4. В bet-g-5a7c-wave-11 добавить блок concept_basis:
     - EXP-20260831-001-physical-homeowner-body.md — единственный
       owner-approved immutable export Concept Lab, с id/candidate/body hash
       и точной owner quote;
     - спека давления 2026-09-01 — только legacy in-flight input этой волны
       с её SHA-256 и owner quote, не authority для новой волны;
     - шесть задач и cuts текущей волны остаются без изменения;
     - следующая волна не переиспользует концепт без нового подходящего EXP.

  5. В q-fable-audit-decisions-2026-09-02 удалить решённый вопрос о Next Fest
     и все вопросы, содержание которых обязан дать Concept Lab. Оставить один
     будущий production batch: фактический статус Steam page/AppID/name;
     порог сети и четырёх машин; минимальный звук; ассеты и бюджет; release
     cleanup и имя; форма работы и обслуживание OS. Явно отметить, что этот
     batch не блокирует волну 11 и возвращается после её review.

  6. Сжать direction_forecast, сохранив status: no_basis:
     рабочая цель — готовое демо к 2026-10-05, публичное демо к 2026-10-26,
     затем платный Steam-релиз и повторно используемый solo-release процесс;
     Steam Next Fest оставить только закрытым фактом; обновлять прогноз после
     review волны 11 либо при датированном свидетельстве готовности/публикации.

  7. Не менять никакую задачу с track, текущие статусы волны 11, её cuts,
     полные Fable-аудит и release-plan, два других открытых вопроса и OS.

  8. Сохранить этот RESULT в
     history/2026-09-02-s-repair-g-5a7c-hot-state-cleanup-001.md и одной
     строкой проиндексировать ногу в журналах g-5a7c, bet-g-5a7c-wave-11,
     q-fable-audit-decisions-2026-09-02 и direction_forecast.

captures:
  - Предложенную Fable структуру будущих волн разбирать только после завершения и review текущей волны.
  - Полные материалы Fable-аудита пока остаются live как материал этого будущего разбора.

decisions_needed: []

play_check:
  - 1 назвать противоречие: done — старые concept/task carriers объявлены текущими и попадают в обычное чтение после смены authority.
  - 2 восстановить: done — проверены свежий Git, карточки, их связи, действующий архивный барьер и Concept Lab receipts.
  - 3 предложить исправленное состояние: done — точечное закрытие/перемещение плюс компактные basis, question и forecast без переписывания экспертизы.
  - 4 подтверждение владельца: done — «давай пункт 1» и, после показа полного перечня, «да».
  - 5 трение: done — новой дыры OS не обнаружено; штатные card close/block и защищённый archive покрывают изменение.

log: Горячее состояние очищено: 11 бесхозных задач закрыты, Only Vermin Know вынесен, forecast/Fable-вопрос сжаты, basis волны закреплён

next: |
  return-to-owner: продолжить текущую волну 11 и довести прежде всего слоты;
  к разбору предложенных Fable волн вернуться после её review.

END_OF_FILE: live/indie-game-development/history/2026-09-02-s-repair-g-5a7c-hot-state-cleanup-001.md
