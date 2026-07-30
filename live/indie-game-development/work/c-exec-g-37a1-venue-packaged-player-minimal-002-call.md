# CALL c-exec-g-37a1-venue-packaged-player-minimal-002

> **READY — FRESH CONTRACT-34 PLAN ROOT.** The old rejected root is terminally `RELEASED / REPLACED`, WIN-U3 is clean
> and `AVAILABLE`, and the committed replacement receipt binds this exact id, clean basis, empty carry and 29 stale
> paths. This root begins at PLAN and does not restore or repair the old candidate.

direction: indie-game-development
track: t-venue
for: t-3
node: g-37a1
to: executor
kind: engineering
repo: C:\projects\Unity\GasCoopGame_win-u3
issued: 2026-07-30 by s-repair-g-37a1-venue-replacement-home-consume-001

engineering_contract: 34
stage: PLAN
session_scope: PLAN-only
slot: WIN-U3
target: Local
change_id: c-exec-g-37a1-venue-packaged-player-minimal-002
replaces: c-exec-g-37a1-venue-packaged-player-001
resume_from: PLAN
replacement_basis: 9ba0791b42444444ec0cad2df19780d81cb63a8f
start_head: e4eba767898ffee774cfde428094b729f7bf3e81
replacement_receipt: docs/measurements/root-receipts/c-exec-g-37a1-venue-packaged-player-001/02-replacement.json
replacement_receipt_sha256: 7e90b0b30df0e925d996a65057b0d9aeedebf41be999e784923273565e12b544
replacement_receipt_git_blob: 691f5adf6ba86f9327ac8c2dbfaf245eda25d76d
preserved_ref: refs/gascoop-preserved/roots/c-exec-g-37a1-venue-packaged-player-001/pre-replacement
carry: []
stale:
  - Assets/GasCoopGame/Editor/PackagedPlayerBuild.cs
  - Assets/GasCoopGame/Editor/PackagedPlayerBuild.cs.meta
  - Assets/Tests/EditMode/PackagedPlayer.meta
  - Assets/Tests/EditMode/PackagedPlayer/GasCoopGame.PackagedPlayer.EditorMode.Tests.asmdef
  - Assets/Tests/EditMode/PackagedPlayer/GasCoopGame.PackagedPlayer.EditorMode.Tests.asmdef.meta
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerBuildContractTests.cs
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerBuildContractTests.cs.meta
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerContractTestSupport.cs
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerContractTestSupport.cs.meta
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerEvidenceContractTests.cs
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerEvidenceContractTests.cs.meta
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerEvidenceNegativeControlTests.cs
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerEvidenceNegativeControlTests.cs.meta
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerNegativeControlTests.cs
  - Assets/Tests/EditMode/PackagedPlayer/PackagedPlayerNegativeControlTests.cs.meta
  - docs/adr/ADR-E-0019-c-exec-g-37a1-venue-packaged-player-001-repeatable-packaged-player-venue.md
  - docs/g-37a1-venue-packaged-player-decisions.md
  - docs/measurements/c-exec-g-37a1-venue-packaged-player-001-pair-red-r1-manifest.json
  - docs/measurements/pair-candidate-runs/c-exec-g-37a1-venue-packaged-player-001/r1/assetdatabase-refresh.mcp.json
  - docs/measurements/pair-candidate-runs/c-exec-g-37a1-venue-packaged-player-001/r1/focused-editmode-red.mcp.json
  - docs/measurements/pair-candidate-runs/c-exec-g-37a1-venue-packaged-player-001/r1/importer-compile.mcp.json
  - docs/measurements/pair-candidate-runs/c-exec-g-37a1-venue-packaged-player-001/r1/project-identity.mcp.json
  - openspec/changes/c-exec-g-37a1-venue-packaged-player-001/PLAN.md
  - openspec/changes/c-exec-g-37a1-venue-packaged-player-001/proposal.md
  - openspec/changes/c-exec-g-37a1-venue-packaged-player-001/specs/unity-platform/spec.md
  - openspec/changes/c-exec-g-37a1-venue-packaged-player-001/tasks.md
  - tools/packaged-player-evidence-check.ps1
  - tools/packaged-player-evidence-check.selftest.ps1
  - tools/verify-packaged-player.ps1
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
- Прежняя линия `c-exec-g-37a1-venue-packaged-player-001` получила binding PAIR-FREEZE rejection
  `2a66cd10756ae17dff709a85d2e6f499f31e3dd4`, затем была process-closed по v34. Terminal receipt commit
  `e4eba767898ffee774cfde428094b729f7bf3e81` опубликован и read back; receipt имеет blob
  `691f5adf6ba86f9327ac8c2dbfaf245eda25d76d`, root `RELEASED / REPLACED`, replacement pin 34 и exact
  `replaced_by`, равный id этого CALL.
- `replacement_basis` и `salvage_commit` равны `9ba0791b42444444ec0cad2df19780d81cb63a8f`. Текущий HEAD
  `e4eba767…` добавляет только terminal root/stage receipts поверх clean basis; не сбрасывать checkout к basis.
- Прежние PLAN, carrier, RED, review и tool paths имеют disposition `stale`: они отсутствуют в текущем HEAD и доступны
  только через `refs/gascoop-preserved/roots/c-exec-g-37a1-venue-packaged-player-001/pre-replacement` и Git history.
  Они не являются PLAN/evidence нового change id, не восстанавливаются и не дают BUILD authority.
- Owner-approved минимальный scope, failure modes, cuts, stale-marker rule и PLAN-only STOP сохранены из
  `history/2026-07-30-s-work-g-37a1-venue-packaged-player-plan-reset-001.md`. Единственное contract-изменение —
  обязательный current replacement pin 34, записанный committed v34 receipt; бизнес-цель и cuts не менялись.
- Рабочее место — только `C:\projects\Unity\GasCoopGame_win-u3` на постоянной ветке `slot/win-u3`. На выпуске CALL
  checkout clean, локальный HEAD и `origin/slot/win-u3` равны `e4eba767…`, а продуктовый HOME записал selector
  `AVAILABLE / none / unrecorded`. Первый product write — штатный atomic claim нового root.

## boundaries

### Немедленная PLAN-only сессия

- Пишет только новый самостоятельный planning packet с новым change id в разрешённых plan/docs/receipt поверхностях.
- Не пишет production code, tests, test-support или tools; не запускает BUILD и не чинит прежний PAIR-CANDIDATE.
- Предъявляет владельцу точный owner-readable план и останавливается для его явного approval. Без этого approval
  следующий stage не открывается.
- Не восстанавливает и не переписывает stale plan/pair/review/tool artifacts старого root; читает их только через
  preserved ref, если нужно проверить историю. Новый packet строится на текущем clean checkout и replacement basis.

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

После отдельного будущего исполнения под pin 34 корень возвращается HOME только по правилам своего contract pin;
PAIR-CANDIDATE/BUILD eligibility сама по себе не закрывает Direction t-3.

END_OF_FILE: live/indie-game-development/work/c-exec-g-37a1-venue-packaged-player-minimal-002-call.md
