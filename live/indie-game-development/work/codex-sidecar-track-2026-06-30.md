# Codex Sidecar / Lab Track (PROCESS)

**Что это:** направление-специфичный процесс для активного использования Codex рядом с Cloud Code. Это НЕ новая build-задача, НЕ второй active bet и НЕ замена основному инженерному контуру. Это способ безопасно тратить Codex-емкость: где-то как строгий executor, где-то как pair-programming/copilot в Unity.

**Дата:** 2026-06-30. **Узел-носитель:** `g-9c41` + параллельные визуальные/сценовые нужды. **Статус:** процесс заведён; конкретные задачи не назначены.

## 0. Решение в одну строку

Codex работает как sidecar-track с тремя режимами: read-only scout, owner-present Pair-Lab для маленьких Unity-итераций, и Formal Leg для любых load-bearing изменений через обычный engineering contour/OpenSpec.

## 1. Зачем это нужно

- У Cloud Code может закончиться лимит, а разработку останавливать нельзя.
- Codex не должен вслепую брать большие размытые Unity-задачи вроде "улучши сцену".
- В игре много работы, которую можно делать малыми обратимыми шагами: сцены, камеры, debug UI, player sandbox, capture setup, проектная санитария, red tests, проверки.
- Идеи из таких шагов не должны теряться в чате: каждая lab-сессия оставляет след в `work/codex-sidecar/board.md`, а продуктовые находки повышаются до Formal Leg.

## 2. Режимы

### A. Scout / status

Read-only режим. Codex смотрит repo/state/сцены/планы, отвечает что безопасно делать дальше, называет риски и границы. Ничего не пишет. Подходит для "посмотри, где можно влезть" и "что сейчас не трогать".

### B. Pair-Lab / copilot

Owner-present режим для Unity. Один цикл = один маленький видимый эффект:

1. выбрать target: сцена/объект/видимый аспект;
2. Codex называет файлы, которые собирается тронуть, и rollback/checkpoint;
3. делает маленький патч;
4. Unity компилируется / сцена проверяется;
5. владелец глазами решает: keep / tweak / revert;
6. результат записывается в lab board;
7. если изменение стало reusable или продуктовым, оно повышается до Formal Leg.

Pair-Lab НЕ объявляет продуктовое `done`. Это лаборатория: сохранить удачное, откатить неудачное, вытащить формальные задачи.

### C. Formal Leg

Для всего, что становится архитектурой, reusable behavior, player controller, input contract, scene harness, network/multiplayer, gas semantics, shader contract, package/project setting или публичным deliverable.

Правила:

- обычный engineering contour: PLAN / RED / BUILD / VALIDATE / RESULT;
- если это существенная engineering-задача в product repo, Codex сначала использует `ultracode` по правилам product `AGENTS.md`;
- задача режется меньше обычного: полдня human-equivalent максимум;
- отдельный worktree или явно выданный файл-lock;
- закрытие только через evidence, runnable checks и, где нужно, owner-eye.

## 3. Границы по умолчанию

Если владелец явно не сказал иначе, Codex Sidecar НЕ трогает:

- активные Cloud Code worktree/file ranges;
- `Core/**`, netcode, checksum/content-hash, gas-law semantics;
- shader/render contracts активного visual-лега;
- `ProjectSettings/**`, `Packages/manifest.json`;
- текущие OpenSpec/proposal files, которые принадлежат другой активной сессии;
- существующие сцены, где сейчас работает Cloud Code, кроме owner-present Pair-Lab.

Codex Sidecar МОЖЕТ брать в Pair-Lab:

- отдельные sandbox/demo scenes;
- camera/light/floor/room composition;
- scene presets, gizmos, inspector knobs;
- debug overlays and capture helpers;
- small adapter-side scripts that do not change sim authority;
- read-only probes, screenshots, reports, tests.

Если safe target не назначен, режим автоматически понижается до Scout.

## 4. Worktree / locking rule

Рекомендованный default: Codex работает в отдельном явно выделенном worktree. Если отдельного worktree нет, Pair-Lab допускается только когда владелец явно говорит, что Cloud Code paused for that area.

Перед любым edit Codex пишет в чат:

- mode;
- target scene/files;
- forbidden files;
- expected visible change;
- rollback/checkpoint.

Без этого edit не начинается.

## 5. Promotion rule

Pair-Lab немедленно повышается до Formal Leg, если появляется хотя бы одно:

- изменение нужно переиспользовать за пределами одной сцены;
- нужны tests/fixtures/contracts;
- затрагиваются Core/netcode/gas semantics/render shader/package settings;
- владелец хочет считать это product behavior, а не WIP;
- три и более lab-итерации крутятся вокруг одного и того же устойчивого механизма;
- "маленькая правка" начинает требовать архитектурного решения.

Promotion outcome = capture/CALL draft, not silent continuation.

## 6. End states одной sidecar-сессии

- `checkpoint` — маленькое изменение оставлено, evidence записан.
- `promote` — найден продуктовый кусок, нужен Formal Leg.
- `discard` — изменение откатили или признали тупиком; урок записан.
- `blocked` — нужен выбор владельца или конфликт с активной Cloud Code работой.
- `scout-only` — был только анализ, без файловых изменений.

## 7. Ledger

Журнал sidecar-сессий живёт в `work/codex-sidecar/board.md`.

Минимальная запись:

- date / mode / target;
- product repo worktree or `read-only`;
- files touched or `none`;
- visible intent;
- validation/evidence;
- owner verdict if Pair-Lab;
- end state;
- promotion/captures.

## 8. Как не потерять идеи

- Любая идея, которая не делается прямо сейчас, идёт в `captures` RESULT или в `work/codex-sidecar/board.md`.
- Любой reusable кусок получает promotion candidate.
- `NOW.next` не меняется только ради sidecar: основной ход Sc-weight/visual сохраняется.
- При digest/audit процесс виден через `NOW.parallel_tracks`.

## 9. Примеры подходящих будущих работ (НЕ задачи сейчас)

- сцена-лаборатория с нормальной комнатой/светом/полом для газа;
- player sandbox: ходить, камера, jump/gravity, без multiplayer promises;
- debug overlay / inspector knobs для плотности, источников, capture states;
- capture pipeline для коротких clips/screenshots;
- scene hygiene: naming, staging objects, reset buttons;
- тесты/validators для уже написанных Cloud Code legs.

END_OF_FILE: live/indie-game-development/work/codex-sidecar-track-2026-06-30.md
