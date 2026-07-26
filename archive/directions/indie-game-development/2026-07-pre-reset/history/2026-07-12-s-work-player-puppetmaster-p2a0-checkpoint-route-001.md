# RESULT s-work-player-puppetmaster-p2a0-checkpoint-route-001

call: c-exec-player-puppetmaster-p2a0-002-build-continuation-001 (returned checkpoint)
direction: indie-game-development
play: work (checkpoint-route)
node/task: g-9c41 / M1-P2a0
date: 2026-07-12

## outcome

Возвращённый Claude Code builder-checkpoint по M1-P2a0 обработан и заведён в состояние без
фабрикации закрытия. Продвижение ноги (чистый live PuppetMaster import + подтверждённая на реальном
вендоре цель «замороженного маппера» `BehaviourPuppet.state {Puppet|Unpinned|GetUp}` + перечисленный
closed-world exclusion set) зафиксировано как evidence; остановка на venue-блокере (headless PlayMode
loop stall на settled-smoke; правильная площадка = PlayMode test runner) записана без снижения
доказательности. Терминальный статус остаётся **CHECKPOINT / NOT DELIVERED** — нет `-Deliver`/merge/PR/
G5/owner verdict. Owner steer «ок» (owner chat, 2026-07-12) записан как **материал** (не заморожен):
машинное доказательство сохраняется; обязательные два A/B MP4-клипа + два контактных листа заменяются
живой single-machine Odin-`[Button]` A/B/C песочницей как owner-eye (никогда не гейт); multiplayer
остаётся inventory-only. Оба build-CALL'а свёрнуты в один owner-present PLAN-amend; M1-P2a0 остаётся
`active`.

## evidence

**Первая рука по git продукта** (read-only; продукт НЕ изменён — Direction-OS guard):
- worktree `C:\projects\Unity\GasCoopGame_p2a0_002`, branch `codex/c-exec-player-puppetmaster-p2a0-002-build @ b9aea60c`;
  коммиты поверх base `a2d50c2a`:
  - `04fad5dd` — checkpoint: live import + stand/mapper/closed-world mapping;
  - `b9aea60c` — docs: record owner steer for next p2a0-002 PLAN (sandbox, no video);
- `git merge-base --is-ancestor b9aea60c origin/main` = **NO** → **NOT MERGED** (product `origin/main @ a644e5db`);
  `git branch -a --contains b9aea60c` = только build-ветка;
- vendor `Assets/Plugins/RootMotion/` **untracked** (чистый импорт; вендор не в трекинге);
- immutable RED `c73b0195` и frozen PLAN `b90b7205` присутствуют на ветке.

**Executor handback (checkpoint packet):**
- Preflight GREEN на `a2d50c2a`; immutable 37/37 hashes byte-identical до и после Unity-работы;
  package SHA-256 `03E126…BED3` точный; worktree/editor/lock/RAM инвентаризированы.
- MCP привязан к p2a0_002 через `npx unity-mcp-cli run-tool <tool> --path <worktree>` → port 25655
  (in-session bridge был на owner-dev; dev не мутировался).
- Чистый PuppetMaster import + vendor readback в default assembly `Assembly-CSharp-firstpass`.
- Frozen-mapper target подтверждён на реальном вендорном API: `BehaviourPuppet.state {Puppet|Unpinned|GetUp}`;
  стенд = префаб Pilot Root / сцена «Puppet Extended»; closed-world exclusion set перечислен.
- **НЕ построены** (многочасовое, вне бюджета): `P2A0002RigBridge`, test-owned observer/publisher/attempt-tree,
  A/B/C, collision transaction, captures. Bare-stand settle smoke заблокирован headless PlayMode loop stall
  → корректная площадка = PlayMode test runner (без снижения fidelity, ничего не подделано).

**Findings to dispose (вне scope этой ноги):** `tools/check.ps1 = 1529/1531`, 2 pre-existing fail —
(a) immutable-001 `full_runtime_cycle_green=false` RED (честный, никогда не редактировать);
(b) `CoarseArtifactTests.L19` digest drift на frozen-ветке (git-clean `43550f8e…` vs test-hardcoded
`cc54c166…`, old `7c73cb51`) — принадлежит g9c41/coarse-ноге.

**Product RESULT / measurements:**
- `docs/results/c-exec-player-puppetmaster-p2a0-002.md` (cumulative RESULT, incl. Owner steer);
- `docs/measurements/c-exec-player-puppetmaster-p2a0-002-build-continuation-001.md`.

## owner steer (recorded as material — NOT frozen here)

Owner chat «ок» (2026-07-12). Нуждается в отдельной PLAN-сессии с owner для заморозки:
- **KEEP** машинное доказательство корректности (observer/payload/attempt-tree/collision atomicity) —
  owner согласился: одним глазом на одной сцене скрытую authority/collision-state не проверить.
- **REPLACE** обязательные два A/B MP4-клипа + два контактных листа на **живую single-machine playable
  A/B/C песочницу** (Odin `[Button]`: owner жмёт Play, применяет камень/точечный импульс, смотрит передачу
  контроллер↔таз, с пошаговой инструкцией) как owner-eye слой. **DROP** видео-захват (owner-eye only,
  никогда не гейт; автоматический one-machine capture оказался хрупким).
- **Multiplayer — inventory-only** (уже замороженная позиция): двух-машинный тест сейчас низкий приоритет;
  выживший A/B всё равно оставляет будущее двух-пировое FishNet-доказательство обязательным.
- **Тяжёлая часть не меняется**: развести Кандидат A (владеет контроллер) и Кандидат B
  (контроллер→таз→контроллер handoff) на реальном риге PuppetMaster — многочасовая стройка.

## state_changes

**NOW.md:**
- `updated:` → `s-work-player-puppetmaster-p2a0-checkpoint-route-001`.
- task `M1-P2a0`: без изменений (`status: active`; `done_when` не трогается — акцептанс-подход = PLAN-уровень,
  в task done_when видео и не было).
- `open_calls`:
  - УДАЛИТЬ `c-exec-player-puppetmaster-p2a0-002-build-continuation-001` (вернулась чекпоинтом — валидный
    возврат по её собственному done_when bullet 5);
  - УДАЛИТЬ `c-exec-player-puppetmaster-p2a0-002-build-001` (свёрнут амендментом акцептанс-подхода: его
    umbrella done_when с видео-слоем меняется, свежий BUILD пойдёт под переморожённым PLAN);
  - ДОБАВИТЬ `c-exec-player-puppetmaster-p2a0-002-plan-amend-001` (to: executor, kind: engineering,
    phase: PLAN-amend, owner-present; venue p2a0_002 @ b9aea60c).
- `next:` → `work/c-exec-player-puppetmaster-p2a0-002-plan-amend-001-call.md`.

**work/:** + `c-exec-player-puppetmaster-p2a0-002-plan-amend-001-call.md` (self-contained CALL).

**LOG.md:** + одна строка checkpoint-route (после `s-daily-review-20260712-001`).

**history/:** + `2026-07-12-s-work-player-puppetmaster-p2a0-checkpoint-route-001.md` (этот файл).

**work/board/dashboard.html:** перегенерированы hero-eyebrow + tag секции «Борд» + карточка P2a0
(статус «CHECKPOINT ОБРАБОТАН → PLAN-правка») + добавлена строка журнала за 12.07. «Проблемы» не менялись
(`findings.md` не менялся). `knowledge/g9c41-lanes-venues.md` lane-C staleness («001») оставлена dedicated
repair CALL `c-repair-daily-product-routing-20260712-001` (вне scope этой сессии).

## captures

- immutable-001 `full_runtime_cycle_green=false` RED — честный immutable RED, никогда не редактировать;
  диспозиция принадлежит immutable-001.
- `CoarseArtifactTests.L19` digest drift на frozen-ветке (git-clean `43550f8e…` vs test-hardcoded
  `cc54c166…`, old `7c73cb51`) — принадлежит g9c41/coarse-ноге; отдельная диспозиция, не эта нога.

## decisions_needed

(нет — маршрут задан executor-запросом + owner steer «ок»; дословный вердикт по амменд-спеке берётся
в PLAN-amend-сессии)

## play_check

- 1 orient/recite: done — прочитаны NOW/LOG/`os/schema/packets.md`/`knowledge/g9c41-lanes-venues.md`
  panel-rules и вернувшийся continuation CALL; работа распознана = builder checkpoint handback для
  M1-P2a0 → work/checkpoint-route.
- 2 verify handback first-hand: done — git продукта прочитан напрямую (ветка/коммиты/NOT-MERGED/vendor-
  untracked/RED/PLAN); чекпоинт честен; никакого close/G5/verdict не заявляется.
- 3 reconcile + route: done — два build-CALL'а свёрнуты в owner-present PLAN-amend; M1-P2a0 остаётся
  active; NOW.next → plan-amend; панель перегенерирована.
- 4 close (checkpoint): done — checkpoint RESULT; owner steer «ок» записан как материал (owner-verdict
  guard: заморозка амменд-подхода и дословное «да» берутся в PLAN-amend-сессии, не здесь).

## log

2026-07-12 — work/checkpoint-route (g-9c41/M1-P2a0, s-work-player-puppetmaster-p2a0-checkpoint-route-001):
Claude Code builder continuation вернулась CHECKPOINT / NOT DELIVERED (product
codex/c-exec-player-puppetmaster-p2a0-002-build@b9aea60c, verified NOT MERGED) — чистый live PuppetMaster
import + BehaviourPuppet.state{Puppet|Unpinned|GetUp} mapper + closed-world set готовы, но
rig-bridge/observer/A-B-C/settled-smoke не построены (headless PlayMode loop stall → venue = PlayMode
test runner). По owner steer «ок» 12.07 (machine correctness proof остаётся; обязательные A/B видео-клипы
+ контактные листы → живая single-machine Odin-[Button] A/B/C песочница как owner-eye, не гейт; multiplayer
inventory-only) оба build-CALL'а свёрнуты в owner-present PLAN-amend
c-exec-player-puppetmaster-p2a0-002-plan-amend-001; M1-P2a0 остаётся active, next = PLAN-amend.

## next

```
CALL c-exec-player-puppetmaster-p2a0-002-plan-amend-001
to: executor   kind: engineering   phase: PLAN-amend (owner-present)
direction: indie-game-development   node: g-9c41   task: M1-P2a0
repo: C:\projects\Unity\GasCoopGame_p2a0_002
→ work/c-exec-player-puppetmaster-p2a0-002-plan-amend-001-call.md
```

END_OF_FILE: live/indie-game-development/history/2026-07-12-s-work-player-puppetmaster-p2a0-checkpoint-route-001.md
