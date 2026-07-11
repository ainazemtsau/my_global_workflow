# g9c41 — Параллельные линии: карта площадок и правила запуска

updated: 2026-07-10 (s-shape-poligon-m1-001; owner «А» — отдельный core-worktree, quality-first overlap gate)
readers: любая сессия, формирующая или запускающая CALL в g-9c41/g-7e15; play `local/lanes-board`; писарь при заполнении `open_calls`.

## Линии и площадки

| Линия | Зона кода (conflict surface) | Worktree / ветка | Unity Editor | Машина |
|---|---|---|---|---|
| A · ядро | `Core/Field/**` (горячие: VoxelField.cs, VoxelFaceFlow.cs) | `C:\projects\Unity\GasCoopGame_core` (core) — создать/проверить в M1-A0 | НЕ нужен (headless dotnet + tools/check.ps1); Unity только owner-eye | ПК; OS/G5-сессии — можно MacBook |
| B · рендер/визуал | `Assets/GasCoopGame/Adapters/GasView/**`, `Render/**` | `C:\projects\Unity\GasCoopGame_dev_2` (dev2) | нужен (редактор №2) | ПК |
| C · стенд (прототип-лента) | НОВАЯ lab-сборка (отдельный asmdef; только публичный API ядра) | `C:\projects\Unity\GasCoopGame_lab` (lab) — создаётся при первом старте | нужен (редактор №3) | ПК |
| D · уровни / DA | `Adapters/LevelIngestion/**`, сцены | сейчас: `GasCoopGame_dev` (Phase 0 in flight); после мержа Phase 0 → свой worktree `GasCoopGame_levels` (levels) | нужен (DA-авторинг = владелец) | ПК |
| E · сеть/доза | `Core/Field/Determinism/**`, FishNet-адаптер | headless; спайк = 2 машины | не нужен до спайка | ПК + MacBook/облачная VM |
| МЕРЖИ + owner-eye | main | `C:\projects\Unity\GasCoopGame` (main) | редактор №1 | ПК |

## Жёсткие правила

1. **Правило владельца (2026-07-10): параллельный трек стартует ТОЛЬКО с назначенным и ПРОВЕРЕННЫМ worktree.** Перед запуском сессия обязана проверить: (а) worktree существует (`git -C C:\projects\Unity\GasCoopGame worktree list`) и назначен этой линии в таблице выше — или создать по §Создание и записать назначение через RESULT; (б) в нём НЕТ другого in-flight лега (сверить с NOW.open_calls); (в) project-folder не открыт другим редактором (признак: `Temp/UnityLockfile`). Провал любой проверки = STOP, не запускаться.
2. Один project-folder = один Unity Editor. Никогда.
3. Один мутирующий core-лег одновременно: `VoxelField.cs`/`VoxelFaceFlow.cs` трогает только линия A и только один лег за раз (дайджест и свёртка НЕ параллелятся между собой). Узкое исключение M1-A0 во время Phase 0 разрешено владельцем «А» только для НОВЫХ read-only diagnostics/API + tests после документированного нулевого пересечения с текущим Phase-0 diff; любой общий файл или необходимость править hot Core = STOP. M1-A0 не мержится до Phase 0.
4. §Re-sync к `base` из LAUNCH-блока перед стартом каждого лега; база уехала → пересогласовать, не строить на старой.
5. Очередь мержей в main: по одному, полный `tools/check.ps1` на merged main, следующий лег перебазируется. Слоты — в NOW.open_calls.
6. G5 — конвейером: свежая сессия (можно MacBook), параллельно билду следующего лега. Ворота не срезаются никогда; скорость берётся линиями и конвейером.
7. Вердикты владельца — батчем раз в день (секция «ЖДЁТ ТЕБЯ» борда).

## LAUNCH-блок (обязателен в каждом executor-CALL; писарь дублирует кратко в open_calls.note)

```
launch:
  lane: A|B|C|D|E
  venue: <worktree + ветка + редактор №N | headless>
  machine: ПК | MacBook | 2 машины
  base: origin/main @<SHA> (§Re-sync обязателен)
  conflict_surface: <зоны/файлы>
  depends_on: [<что должно быть MERGED>]
  merge_queue: слот N
  gates: G5 = свежая сессия; owner-eye = <где>
```

## Создание core-worktree (M1-A0)

1. Проверить `git -C C:\projects\Unity\GasCoopGame worktree list`; если назначения ещё нет:
   `git -C C:\projects\Unity\GasCoopGame worktree add ..\GasCoopGame_core -b core origin/main`.
2. Убедиться, что branch/path не заняты, worktree clean, `Temp/UnityLockfile` отсутствует; до изменений
   полный `tools/check.ps1` green.
3. Read-only сравнить текущий Phase-0 diff/status в `GasCoopGame_dev`. Только нулевое пересечение
   разрешает A0 BUILD; иначе STOP/checkpoint.
4. A0 merge ждёт Phase 0 MERGED: fetch/rebase на свежий origin/main, полный check, затем слот 2.

## Создание нового worktree (пример — lab)

1. `git -C C:\projects\Unity\GasCoopGame worktree add ..\GasCoopGame_lab -b lab origin/main`
2. Открыть `C:\projects\Unity\GasCoopGame_lab` через Unity Hub. Первый импорт Library долгий (десятки минут, десятки ГБ диска); лимит параллельных редакторов — RAM (4–8+ ГБ на редактор).
3. До первого изменения: `tools/check.ps1` в новом worktree зелёный.
4. Записать назначение worktree→линия в таблицу выше (писарь, через RESULT).

## Чек-листы лега

Пред-полётный (до любой работы): линия свободна по NOW? → deps MERGED (по git, не по словам)? → worktree проверен (правило 1)? → §Re-sync сделан? → редактор свободен? → только потом BUILD.
Пост-полётный: RESULT → писарь (re-sync before apply) → G5-CALL встаёт в NOW → мерж-слот → полный check на main → борд отражает разблокировки.

## Ночная линия R (рефакторинг) + панель владельца

- Ночной рефакторинг: триггер «делай рефакторинг» → `plays/refactor-night.md`; бэклог `work/refactor/backlog.md`. Ночью только headless-доказуемые зоны (Core/tests/tools/docs) в СВОБОДНЫХ по NOW зонах; ветки `refactor/<slug>` от origin/main; **в main ночью не мержится ничего** — мерж только владельческим утренним батчем через очередь (правило 5).
- Панель владельца: `work/board/dashboard.html` — РЕНДЕР поверх NOW+git (истина всегда NOW; расхождение = баг рендера). **Обязанность писаря: после каждого apply, меняющего open_calls/tasks/next, перегенерировать секции панели «📋 Борд», «Журнал» (LOG.md за последние 3 дня, сегодняшний день раскрыт `<details open>`, старше — с панели уходит) и «Проблемы» (открытые находки work/review/findings.md по приоритету)** (остальные секции — зафиксированные обсуждения, их правят только сессии, менявшие план).
- Дневное ревью: расписанный запуск (Codex scheduled task) или «дневное ревью» в чате → `plays/daily-review.md`; находит — не чинит; леджер `work/review/findings.md`; ночная линия берёт из леджера только класс `night`. Файл открывается в Chrome с диска. **Панель живёт ТОЛЬКО в репо** (правило владельца 2026-07-11): обновления только в репо, внешние зеркала (claude.ai-артефакты и т.п.) не ведутся и не обновляются.

## MacBook

Роли: (1) OS-сессии / писарь / G5-опровержения — готов сейчас, Unity не нужен; (2) headless-ядро — установить dotnet SDK + pwsh (~30 мин, отдельная настройка); (3) кандидат «машина №2» интернет-спайка (mac-билд vs облачная Windows-VM — решается в c-prep-net-spike-001). Активацию Unity Personal на второй машине проверить при настройке.

END_OF_FILE: live/indie-game-development/knowledge/g9c41-lanes-venues.md
