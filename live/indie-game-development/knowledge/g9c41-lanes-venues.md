# g9c41 — Параллельные линии: карта площадок и правила запуска

updated: 2026-07-10 (s-lanes-install-001; owner «подтверждаю» + жёсткое правило worktree)
readers: любая сессия, формирующая или запускающая CALL в g-9c41/g-7e15; play `local/lanes-board`; писарь при заполнении `open_calls`.

## Линии и площадки

| Линия | Зона кода (conflict surface) | Worktree / ветка | Unity Editor | Машина |
|---|---|---|---|---|
| A · ядро | `Core/Field/**` (горячие: VoxelField.cs, VoxelFaceFlow.cs) | `C:\projects\Unity\GasCoopGame_dev` (dev) — ПОСЛЕ мержа Phase 0 | НЕ нужен (headless dotnet + tools/check.ps1); только owner-eye | ПК; OS/G5-сессии — можно MacBook |
| B · рендер/визуал | `Assets/GasCoopGame/Adapters/GasView/**`, `Render/**` | `C:\projects\Unity\GasCoopGame_dev_2` (dev2) | нужен (редактор №2) | ПК |
| C · стенд (прототип-лента) | НОВАЯ lab-сборка (отдельный asmdef; только публичный API ядра) | `C:\projects\Unity\GasCoopGame_lab` (lab) — создаётся при первом старте | нужен (редактор №3) | ПК |
| D · уровни / DA | `Adapters/LevelIngestion/**`, сцены | сейчас: `GasCoopGame_dev` (Phase 0 in flight); после мержа Phase 0 → свой worktree `GasCoopGame_levels` (levels) | нужен (DA-авторинг = владелец) | ПК |
| E · сеть/доза | `Core/Field/Determinism/**`, FishNet-адаптер | headless; спайк = 2 машины | не нужен до спайка | ПК + MacBook/облачная VM |
| МЕРЖИ + owner-eye | main | `C:\projects\Unity\GasCoopGame` (main) | редактор №1 | ПК |

## Жёсткие правила

1. **Правило владельца (2026-07-10): параллельный трек стартует ТОЛЬКО с назначенным и ПРОВЕРЕННЫМ worktree.** Перед запуском сессия обязана проверить: (а) worktree существует (`git -C C:\projects\Unity\GasCoopGame worktree list`) и назначен этой линии в таблице выше — или создать по §Создание и записать назначение через RESULT; (б) в нём НЕТ другого in-flight лега (сверить с NOW.open_calls); (в) project-folder не открыт другим редактором (признак: `Temp/UnityLockfile`). Провал любой проверки = STOP, не запускаться.
2. Один project-folder = один Unity Editor. Никогда.
3. Один мутирующий core-лег одновременно: `VoxelField.cs`/`VoxelFaceFlow.cs` трогает только линия A и только один лег за раз (дайджест и свёртка НЕ параллелятся между собой).
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

## Создание нового worktree (пример — lab)

1. `git -C C:\projects\Unity\GasCoopGame worktree add ..\GasCoopGame_lab -b lab origin/main`
2. Открыть `C:\projects\Unity\GasCoopGame_lab` через Unity Hub. Первый импорт Library долгий (десятки минут, десятки ГБ диска); лимит параллельных редакторов — RAM (4–8+ ГБ на редактор).
3. До первого изменения: `tools/check.ps1` в новом worktree зелёный.
4. Записать назначение worktree→линия в таблицу выше (писарь, через RESULT).

## Чек-листы лега

Пред-полётный (до любой работы): линия свободна по NOW? → deps MERGED (по git, не по словам)? → worktree проверен (правило 1)? → §Re-sync сделан? → редактор свободен? → только потом BUILD.
Пост-полётный: RESULT → писарь (re-sync before apply) → G5-CALL встаёт в NOW → мерж-слот → полный check на main → борд отражает разблокировки.

## MacBook

Роли: (1) OS-сессии / писарь / G5-опровержения — готов сейчас, Unity не нужен; (2) headless-ядро — установить dotnet SDK + pwsh (~30 мин, отдельная настройка); (3) кандидат «машина №2» интернет-спайка (mac-билд vs облачная Windows-VM — решается в c-prep-net-spike-001). Активацию Unity Personal на второй машине проверить при настройке.

END_OF_FILE: live/indie-game-development/knowledge/g9c41-lanes-venues.md
