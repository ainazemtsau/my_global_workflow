# RESULT — s-repair-g-5a7c-current-contract-001

direction: indie-game-development
track: —
play: repair
node/task: g-5a7c / current-contract
date: 2026-09-02

outcome: |
  Активная цель g-5a7c становится компактным производственным контрактом:
  получить интегрированную играбельную сборку и закрывать результат словом
  владельца. Она больше не хранит собственную версию концепта, старые
  appetite/kill_by волн 2–3 или выбор между экспортами Concept Lab.

  Три пункта, которые сейчас ложно показываются как «ждут слова владельца»,
  перестают блокировать каждую ногу. Их содержание не теряется: будущий
  concept intake и production batch после review волны 11 сохраняются двумя
  idea-карточками, которые не являются требованиями и не входят в обычный
  рабочий набор.

evidence: |
  На свежем HEAD 20752895 рабочее дерево чистое. Blobs до ремонта:
  g-5a7c — 3791a6f8af946b87fde07c0c7587f9901700d717;
  d-which-thread-document-is-the-contract-001 —
  7177c1f3e1ad1826a0abd6ea16fedd3cb82e62a2;
  q-what-concept-lab-must-answer-before-the-next-wave —
  9b12c9f9b0b13c491f180a0dd5455c00a485940b;
  q-fable-audit-decisions-2026-09-02 —
  9496a007e0d2a0b540c00dc5a119b21c75bfe65e.

  Рабочий набор g-5a7c сейчас — 14 файлов / 22 059 слов. Одна карточка
  g-5a7c занимает 12 750 слов: 9 331 — неизменяемый журнал; 1 358 —
  appetite/kill_by завершённых волн 2–3; около 2 025 — собственный пересказ
  концепта и старых механических контрактов. Карточка всё ещё называет
  MAKE HIM LATE, телекинез/нить и прошлые волны, хотя утверждённая граница
  говорит: «концепт хранится только в Concept Lab, Direction закрепляет
  только неизменяемые входы конкретной волны».

  d-which-thread-document-is-the-contract-001 просит Direction выбрать
  между двумя противоречивыми concept exports. После утверждённой границы
  это больше не решение Direction. q-what-concept-lab-must-answer-before-
  the-next-wave — разовый отправленный список 27 августа, а новый процесс
  требует свежий точечный immutable export при shape следующей волны.
  q-fable-audit-decisions-2026-09-02 прямо говорит «после review» и
  «не блокирует», но видом question всё равно показывается каждой ноге как
  ожидающий немедленного слова владельца.

  Владелец утвердил саму границу словами «утверждаю: концепт хранится только
  в Concept Lab, Direction закрепляет только неизменяемые входы конкретной
  волны», а эту очистку — «давай приступать к чистке по плану что ты описал».

state_changes: |
  1. В g-5a7c сохранить id, _kind, _parent, _pos, status, label_by,
     children и весь журнал. Поменять:
     label → «Играбельное ядро текущей игры»;
     hook → «Владелец запускает интегрированную сборку, играет без помощи
     разработчика и решает, что делать дальше»;
     detail →
     history/2026-09-02-s-repair-g-5a7c-current-contract-001.md.

  2. В g-5a7c целиком заменить goal/done_when/why/edge/risk компактными
     блоками:
     - outcome — интегрированная играбельная сборка и фактическая игра
       владельца;
     - Concept Lab — единственный дом концепта;
     - каждая волна использует только owner-approved immutable inputs,
       перечисленные в её concept_basis;
     - закрытие волны и цели опирается на review и явный вердикт владельца;
     - старый развёрнутый текст остаётся восстановимым по blob/этому RESULT,
       но не является authority и не читается по умолчанию.
     Ни одной механики, цифры или новой концептуальной формулировки не
     добавлять.

  3. Штатно снять с g-5a7c блоки appetite и kill_by. Их законченные волны
     и прежний текст остаются в Git/history и старых bet-карточках.

  4. Создать idea-next-wave-concept-lab-intake-001:
     about g-5a7c; from владелец; opened 2026-09-02; source —
     history/2026-09-02-s-frame-g-5a7c-concept-authority-boundary-001.md.
     Смысл: после review волны 11 следующая shape запрашивает в Concept Lab
     только нужный ей свежий owner-approved immutable export; Direction не
     выбирает между прежними экспортами и не переносит старый список вопросов.

  5. Создать idea-production-batch-after-wave-11-review-001:
     about g-5a7c; from владелец; opened 2026-09-02; source —
     history/2026-09-02-s-repair-g-5a7c-hot-state-cleanup-001.md.
     Сохранить шесть отложенных production-тем: Steam page/AppID/имя;
     четыре машины; минимальный звук; ассеты/бюджет; release cleanup/имя;
     форма работы/обслуживание OS. Явно: не требование и не блокер волны 11.

  6. Закрыть как superseded:
     - d-which-thread-document-is-the-contract-001 →
       idea-next-wave-concept-lab-intake-001;
     - q-what-concept-lab-must-answer-before-the-next-wave →
       idea-next-wave-concept-lab-intake-001;
     - q-fable-audit-decisions-2026-09-02 →
       idea-production-batch-after-wave-11-review-001.
     Полный прежний текст и причина остаются в closed/history.

  7. Не менять bet-g-5a7c-wave-11, семь её задач и статусы, g-0c26,
     forecast, work/Fable-материалы, knowledge, archive и os/**.
     Исторический журнал g-5a7c не сокращать этой ногой.

  8. Сохранить RESULT в
     history/2026-09-02-s-repair-g-5a7c-current-contract-001.md и одной
     строкой проиндексировать ногу в g-5a7c и двух новых idea-карточках.

captures:
  - Отдельная OS maintenance-нога должна перестать вручать обычной сессии все 98 записей журнала g-5a7c.
  - Та же maintenance-нога должна показывать подробно только issues маршрута текущего play, а не 107 аннотаций сразу.

decisions_needed: []

play_check:
  - 1 назвать противоречие: done — Direction после принятой границы всё ещё хранит 3 419 слов собственной концептуальной/староволновой authority и три ложных срочных вопроса.
  - 2 восстановить: done — свежие blobs, размеры блоков, provenance трёх карточек и точные слова владельца проверены.
  - 3 предложить исправленное состояние: done — минимальный производственный контракт плюс две отложенные ideas без потери прежних байтов.
  - 4 подтверждение владельца: done — «давай приступать к чистке по плану что ты описал».
  - 5 трение: done — reader-side раздувание журнала/issues выделено в отдельную maintenance-ногу; os/** здесь не меняется.

log: Активная цель сжата до производственного контракта: копия концепта и старые волны сняты, три несрочных вопроса припаркованы идеями

next: |
  return-to-owner: отдельной maintenance-ногой сократить обычное чтение
  журналов и route-неспецифичных issue-аннотаций без изменения live-state.

END_OF_FILE: live/indie-game-development/history/2026-09-02-s-repair-g-5a7c-current-contract-001.md
