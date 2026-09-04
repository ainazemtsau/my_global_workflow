# RESULT — s-frame-g-5a7c-concept-authority-boundary-001

direction: indie-game-development
play: frame
node/task: g-5a7c / —
track: —
date: 2026-09-02

owner_approved: |
  Владелец утвердил точную границу:
  **«утверждаю: концепт хранится только в Concept Lab, Direction закрепляет только неизменяемые
  входы конкретной волны»**.

outcome: |
  **CHARTER БОЛЬШЕ НЕ ЯВЛЯЕТСЯ ВТОРОЙ КОПИЕЙ КОНЦЕПТА.** Полное описание игры удалено из
  направления. Concept Lab назначен единственным домом концепта, а Direction OS хранит только
  производственную власть и короткий `concept_basis` конкретной утверждённой ставки.

  Вход заморожен проверяемо: точный `EXP-*`, `body_sha256`, `source_lab_commit`, когда он есть,
  взятые этой волной пункты и явно не взятые пункты. Более новый черновик или состояние Concept Lab
  не меняет идущую волну задним числом. Полный экспорт в Direction не копируется.

  Из жёстких ограничений устава удалены дублирующие описания нити, хозяина, ядра, числа игроков и
  фокуса качества. Эти свойства теперь обязаны приходить с закреплённым входом ставки. Миссия,
  критерии выпуска, текущая ставка, задачи, продукт и архив этой ногой не менялись.

evidence: |
  - Точное правило утверждено владельцем в этой сессии после показа схемы импорта — цитата в
    `owner_approved`.
  - `C:\projects\concept-lab\exports\EXP-20260830-001-make-them-late-charged-polar-impulse.md`
    несёт `schema: concept-lab/owner-approved-export-v1`, `immutable: true`, `body_sha256`,
    `source_lab_commit` и дословный `owner_approval_quote`.
  - `C:\projects\concept-lab\exports\EXP-20260831-001-physical-homeowner-body.md` несёт тот же
    контракт, неизменяемый body hash и owner approval; отсутствие source commit остаётся явно
    записанным `null`, а не додумывается Direction.
  - До правки `CHARTER.md` содержал отдельный раздел «Что это за игра», ссылки на две локальные копии
    контрактов и повторял конкретные механики ещё в трёх жёстких ограничениях. После правки поиск
    этого заголовка и обеих ссылок пуст.

state_changes: |
  1. PATCH `live/indie-game-development/CHARTER.md`:
     - раздел «Что это за игра» заменён разделом «Граница концепта»;
     - записан immutable intake по `EXP-*` + `body_sha256` + `source_lab_commit`;
     - каждая ставка обязана закреплять взятый и не взятый срез в `concept_basis`;
     - позднее изменение Concept Lab не меняет активную ставку без нового утверждения;
     - из жёстких ограничений удалён локальный пересказ конкретных механик;
     - линза канона заменена проверкой pinned input;
     - роль concept-lab в списке репозиториев уточнена.
  2. ADD этот полный RESULT в
     `live/indie-game-development/history/2026-09-02-s-frame-g-5a7c-concept-authority-boundary-001.md`.
  3. APPEND одну журнальную строку к карточке `g-5a7c` через `osctl leg close`.

  `NOW.md`, ставка, задачи, CALL/decision-карточки, knowledge, work, archive и продукт не меняются.

captures:
  - Следующая repair-нога закрепляет `concept_basis` одиннадцатой волны и выносит локальные копии концепта.
  - Отдельная frame-нога исправляет Steam/Next Fest и цель демо 5 октября.

decisions_needed: []

play_check:
  - 1 interview: done — границу власти дал только владелец своей точной фразой.
  - 2 homework: done — действующий immutable export-контракт проверен на двух экспортированных артефактах.
  - 3 charter draft: done — схема была показана владельцу; он утвердил её дословно.
  - 4 pre-mortem: skipped — риски и меры этой узкой ревизией не меняются.
  - 5 root node: skipped — миссия и корневой outcome этой ревизией не меняются.
  - 6 close: done — продолжение возвращается владельцу отдельной атомарной ногой.

log: |
  Concept Lab закреплён единственным домом концепта; Direction хранит только immutable intake волны

next: |
  return-to-owner — следующий отдельный шаг: repair `concept_basis` активной волны и локальных копий
  концепта.

END_OF_FILE: live/indie-game-development/history/2026-09-02-s-frame-g-5a7c-concept-authority-boundary-001.md
