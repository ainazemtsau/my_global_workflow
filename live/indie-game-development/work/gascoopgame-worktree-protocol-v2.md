# GasCoopGame worktree protocol v2 — owner-approved audit and migration contract

date: 2026-07-16
owner_verdict: `A`
status: accepted Direction dispatch rule; product installation is a separate HELD executor CALL
read_by: any Direction session preparing a GasCoopGame executor CALL; product-protocol installation and cleanup sessions

## Короткий вердикт

Код NearGas L1a и product `main` не потеряны. Рассинхронизировалась диспетчеризация: старая Direction-карта
назначает постоянные feature-worktrees, тогда как current product authority v26 назначает один persistent `dev`
и integration-only `main`. Владелец выбрал **A — product-owned single mutable venue v2**.

С этого решения `knowledge/g9c41-lanes-venues.md` — историческая карта и **не launch authority**. Файл этой
repair-сессией не переписывается: play `repair` не пишет `knowledge/`. Его dispatch-смысл superseded фактическим
owner verdict `A`, KERNEL-правилом «Direction не диктует branches/paths/SHAs» и этим сохранённым артефактом.
Формальная пометка/компакция knowledge остаётся следующему подходящему knowledge-writing play.

## Разделение authority

1. **Direction OS** хранит outcome, conflict surface, dependencies и состояние CALL `READY/HELD/LOCKED`; новые
   executor-CALL не назначают local path, branch или SHA.
2. **GasCoopGame** через root `AGENTS.md` и product-local registry владеет checkout topology, branch mechanics,
   Unity/MCP identity, clean preflight и lifecycle worktree.
3. **Durable truth** — commit + committed evidence. Имя папки не доказывает branch или статус работы.
4. `main` — clean/read-only integration, без product edits и без Unity. `dev` — единственный долгоживущий
   mutable Unity+MCP workspace.
5. Одновременно мутирует продукт ровно один product leg. Короткоживущий clean evidence checkout допустим только
   для fresh review/mutation evidence и удаляется после возврата evidence; это не постоянный feature-worktree.
6. Legacy checkout получает один статус: `ACTIVE-EXCEPTION`, `FROZEN`, `FORENSIC` или `RETIRE-CANDIDATE`.
   Reset/delete/move/rebase/merge разрешены только после lossless preservation proof и отдельного owning CALL.

## Fresh inventory на момент решения

Счётчики `+/-` — commits относительно fresh `origin/main@c4409e7b`; dirty counts получены через porcelain `-uall`.

| checkout | фактическая ветка/HEAD | +/- | dirty | editor | статус / единственное допустимое следующее действие |
|---|---|---:|---:|---|---|
| `GasCoopGame` | `main@c4409e7b` | 0/0 | 0 | нет | integration-only; не редактировать |
| `GasCoopGame_dev` | `dev@c4409e7b` | 0/0; local dev на 5 commits впереди remote dev | 0 tracked + 2 untracked | Unity+MCP реально открыт | persistent workspace, но preflight не clean до disposition двух folder `.meta` |
| `GasCoopGame_core` | `codex/c-exec-near-gas-core-authority-001-red-freeze-002@94de0489` | +2/-49 | 1 tracked + 33 untracked | нет | `FORENSIC/FROZEN`; forbidden v22 RED, сначала полный snapshot |
| `GasCoopGame_dev_2` | `codex/c-visual-009-build@a0db28a2` | +1/-130 | 6 tracked + 17 untracked | нет | `FROZEN`; preserved visual WIP, fresh visual plan владеет disposition |
| `GasCoopGame_exp` | `exp/neargas-skeleton-test@93039442` | +10/-49 | 0 | нет | `RETIRE-CANDIDATE`; все 10 commits patch-equivalent уже в main |
| `GasCoopGame_lab` | `lab@b90b7205` | +9/-130 | 8 tracked + 819 untracked | нет | `FORENSIC`; explicit byte-for-byte PuppetMaster snapshot |
| `GasCoopGame_p2a0_002` | `c-exec-char-v2-reaction-core-build-001@b6c6f2b7` | +8/-50 | 7 tracked + 5 untracked | Unity process нет; lockfile stale-candidate | `ACTIVE-EXCEPTION`; exact repair-002 forbids rebase/clean/merge |
| `GasCoopGame_pgg_spike` | `codex/c-spike-pgg-001@c2f99b66` | +2/-130 | 8 tracked + 11 untracked | нет | `FORENSIC`; closed FAIL_STAGE, input для Level Standard |
| `GasCoopGame_policy` | `codex/retire-obsolete-ultracode-policy@19b10bc0` | +1/-131 | 0 | нет | `RETIRE-CANDIDATE`; remote branch exists, intent already carried into main |

Локально 33 refs: 14 уже ancestors `main`, ещё 5 NearGas refs поглощены patch-equivalent commits, 14 имеют
уникальную/смешанную историю. Отдельные refs `core` и `dev2` не являются ветками, checkout'нутыми в одноимённых
папках; path никогда не используется как branch identity.

## Core и mutation score — точная provenance

- `GasCoopGame_core@94de0489` не содержит committed mutation artifact. Его грязь — старый forbidden v22 RED:
  conditional compile mode + 33 untracked acceptance/negative-control files.
- `preserve/neargas-red-freeze-002-wip` сохраняет 34 paths, но текущий working tree отличается в двух файлах:
  `NearGasAcceptanceAssertions.cs` и `NearGasWrongSubjects.cs`. До cleanup нужен новый complete preservation proof.
- `GasCoopGame_exp` содержит ранний committed summary **72.61%** и ignored raw report
  SHA-256 `41B34E8886D02F0F9507AC0826F64C6F7903D790EE009FB520CF17C3A33A1053` (39,930,640 bytes).
- Канонический L1a summary в `main/dev` — **72.78%**, commit `d789ceb6`, Git blob
  `b40a214a60e66bc6b7f9ff0550d3937e1b42cf0f`: 1421 killed, 245 timeout, 313 survived, 310 no-coverage,
  2289 valid. Полный ignored raw report физически сохранён в `dev`, SHA-256
  `1C1D30579219EB5F1877A5A0C5D02E8735C103B768DB000CA71B34F8F2C8675D` (30,135,820 bytes).
- Contract v24 считает L1a exact historical exception: его score не перезапускается и не переиспользуется для
  L1B. L1B получает собственные reviewer-owned H/I/B/D/R и committed artifact после своего review.

## Обязательная миграционная последовательность

1. До завершения character repair-002 все product protocol/cleanup mutations `HELD`. L1B acceptance остаётся
   Direction-only и идёт независимо.
2. Перед первым L1B product executor установить product-owned protocol/registry по
   `c-exec-gascoopgame-worktree-protocol-v2-001`; этот шаг не чистит worktrees.
3. Отдельно disposition'ить два разных `Characters.meta` GUID (`dev` и `p2a0_002`) и `NearGas.meta`; никакая
   repair/cleanup сессия не выбирает GUID сама.
4. Сделать lossless preservation proofs для current Core dirt, `lab`, `dev_2`, `pgg_spike` и при необходимости
   raw L1a report. Paid/vendor/ignored content не коммитится автоматически.
5. Первые кандидаты на физическое снятие после proof — clean `exp` и `policy`. Удаление worktree не означает
   удаление branch; refs disposition'ятся отдельным решением.
6. `p2a0_002` снимается только после Direction close + binding G5 + owning merge/disposition. `dev_2` — только
   после fresh visual plan. `lab` — только после explicit forensic-release. `core` — только после complete snapshot.

## Что эта repair-сессия НЕ делала

Ни один product file, branch, index, worktree, lockfile, `.meta`, raw report, Unity process, remote ref или score
не был изменён. Протокол установлен только как owner-approved Direction dispatch rule; product installation —
отдельный HELD CALL.

END_OF_FILE: live/indie-game-development/work/gascoopgame-worktree-protocol-v2.md
