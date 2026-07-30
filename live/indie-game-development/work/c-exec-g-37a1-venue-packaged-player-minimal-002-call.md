# CALL c-exec-g-37a1-venue-packaged-player-minimal-002

> **DRAFT — NOT DISPATCHABLE.** Its premature `ready` registration was removed by
> `s-repair-g-37a1-venue-replacement-wait-001`. The exact final replacement CALL will be issued only after Re-sync v34
> and committed `REPLACED` HOME for the old root, with a current pin, clean committed `basis`, and exact `carry` / `stale`
> dispositions. Do not execute this draft or treat its pin-31 text as launch authority.

direction: indie-game-development
track: t-venue
for: t-3
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u3
issued: 2026-07-30 by s-work-g-37a1-venue-packaged-player-plan-reset-001

engineering_contract: 31
stage: PLAN
session_scope: PLAN-only
slot: WIN-U3
target: Local
change_id: c-exec-g-37a1-venue-packaged-player-minimal-002
replaces: c-exec-g-37a1-venue-packaged-player-001
resume_from: PLAN
budget: одна отдельная planning session; после предъявления плана — STOP для owner approval

## goal

Подготовить минимальный и проверяемый путь к Windows-сборке игры: собрать Windows bundle, один раз запустить созданный
`.exe` без аргументов, дождаться видимого рабочего окна без немедленного падения, нормально закрыть окно и получить
успешное завершение процесса.

Эта корневая линия начинается только с отдельной PLAN-only сессии. План должен быть достаточно конкретным для
последующего исполнения, но никакое исполнение не начинается до точного owner approval.

## context

- Обслуживаемая Direction-задача — t-3 активного узла g-37a1. Этот CALL даёт только ограниченное свидетельство для
  t-3: он намеренно НЕ доказывает повторный запуск и сам по себе не закрывает полную task done_when.
- Прежняя линия `c-exec-g-37a1-venue-packaged-player-001` дошла до binding PAIR-FREEZE rejection, записанного коммитом
  `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`:
  `docs/measurements/c-exec-g-37a1-venue-packaged-player-001-pair-freeze-r1-refutation.json` и
  `docs/reviews/pair-freeze-c-exec-g-37a1-venue-packaged-player-001-r1.md`.
- Прежний PLAN, carrier, RED, receipts, review и commits сохраняются как история. Они не являются PLAN или evidence
  нового change id, не ремонтируются и не дают BUILD authority.
- Владелец явно задал для новой линии `engineering_contract: 31`, `WIN-U3`, Target `Local` и новый change id.
- Рабочее место — только `C:\projects\Unity\GasCoopGame_win-u3` на постоянной ветке `slot/win-u3`. Не создавать,
  не удалять и не перемещать worktree; не создавать, не переключать, не переименовывать, не сбрасывать и не удалять
  ветки. Несовпадение слота, ветки, Target Local или недоступный слот — STOP.

## boundaries

### Немедленная PLAN-only сессия

- Пишет только новый самостоятельный planning packet с новым change id в разрешённых plan/docs/receipt поверхностях.
- Не пишет production code, tests, test-support или tools; не запускает BUILD и не чинит прежний PAIR-CANDIDATE.
- Предъявляет владельцу точный owner-readable план и останавливается для его явного approval. Без этого approval
  следующий stage не открывается.
- Не удаляет и не переписывает старые plan/pair/review/receipt artifacts. Если для будущего исполнения нельзя назвать
  простой недеструктивный basis без ремонта старого кандидата или сложного rollback, это STOP для владельца.

### Scope будущего исполнения, который обязан зафиксировать план

- Ровно одна Windows-сборка и ровно один запуск созданного `.exe` без аргументов.
- Проверка минимально полного bundle до запуска: `.exe` и все обязательные runtime-файлы/каталоги, которые план
  выводит из фактического Windows build output и авторитетов продукта.
- Ожидание видимого рабочего окна, отсутствие немедленного падения, нормальное закрытие и ожидание завершения
  процесса с успешным exit code.
- Обычные fail-closed исходы: ошибка сборки; отсутствие обязательного файла/каталога bundle; окно не появилось;
  немедленное падение; зависание при закрытии; процесс завершился ошибочно.
- Риск stale-success-marker закрывается просто: временный результат/маркер удаляется перед сборкой, а признак успеха
  создаётся только после полностью успешной сборки.

### Явно исключено

- второй запуск и сравнение кадров;
- независимые builder/validator evidence sets;
- защита от намеренной подделки доказательств;
- actor/capture provenance;
- полный environment fingerprint;
- PlayerPrefs provenance;
- 47-path authority binding;
- before/between/after byte snapshots всего bundle;
- сложный rollback.

Не возвращать исключённое под другим названием и не переносить audit-grade доказательную архитектуру старого change
в новый минимальный план.

## done_when

1. В PLAN-only сессии создан новый самостоятельный owner-readable план для
   `c-exec-g-37a1-venue-packaged-player-minimal-002`; в нём поимённо сопоставлены цель, шесть обычных failure modes,
   простой stale-marker rule и все десять групп исключений.
2. План не переносит authority из прежнего PLAN/PAIR-CANDIDATE и не предлагает ремонтировать старый candidate;
   старые commits/receipts/reviews остаются историческим evidence.
3. План определяет проверяемый будущий результат: Windows build успешен; минимально обязательный bundle существует;
   `.exe` один раз запущен без аргументов; видимое рабочее окно появилось; немедленного падения нет; окно нормально
   закрыто; процесс завершился успешно.
4. В planning session не изменены production code, tests, test-support или tools и не выполнялись BUILD/launch.
5. Точный план предъявлен владельцу; session STOP и ждёт его явного approve/revise/reject verdict. Без owner approval
   никакой PAIR-CANDIDATE, BUILD или иной downstream stage не запущен.

## return

В этой planning session: короткий owner-readable brief, точные пути нового planning packet, полный список cuts и один
вопрос approve/revise/reject. До owner verdict — только checkpoint того же PLAN; не REPORT о delivery и не successor.

После отдельного будущего исполнения под pin 31 корень возвращается HOME только по правилам своего contract pin;
PAIR-CANDIDATE/BUILD eligibility сама по себе не закрывает Direction t-3.

END_OF_FILE: live/indie-game-development/work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md
