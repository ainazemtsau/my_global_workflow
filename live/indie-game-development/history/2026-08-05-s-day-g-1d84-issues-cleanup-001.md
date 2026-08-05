# RESULT s-day-g-1d84-issues-cleanup-001 (call: owner-day-2026-08-05-issues-review)

direction: indie-game-development
track: direction
play: day
node/task: g-1d84

## outcome

Владелец заказал разбор всех нерешённых записей NOW без правки, получил его, дал семь решений и
сказал «делай чистку». Записи разобраны по смыслу и по маршруту, каждое утверждение перемерено
командой на живом состоянии, а не принято по тексту записи. Итог: 35 записей → 22.

Восемь записей закрыты, потому что описанной в них проблемы больше не существует; шесть слиты в три
по общему триггеру; две постоянные правила владельца сведены в одну строку; одна заведена заново на
измеренный факт, которого в учёте не было вовсе. Три решения владельца записаны в свои строки, два
его вопроса заведены решениями и ждут отдельных чатов.

Отдельно найдено и заведено: `WIN-U3` числится заблокированным и не начатым, а в нём лежит 49
незакоммиченных файлов (~15 МБ) — фактический результат `t-look-1`, который не держит ничто.

## evidence

Слова владельца 2026-08-05, дословно: «1 23 задачи остаются как есть»; «2 возможно там какие то
проблемы с вообще задачей я хочу подробно обсудить это в отдельном чате»; «3 я бы хотел еще про
skills погооврить они нам реально не нужны это unity mcp генерирвует»; «4 откатываем»; «5 закрыть»;
«6 15 августа»; «7 нужны детали просто и понятно расписаные»; «делай чистку».

Перемеры, на которых стоят закрытия (все на `main` = `2eee9719`, продуктовый репозиторий):

- `i-slot-u2-backup-ref-missing-after-cleanup-001` — посылка ЛОЖНА. Запись искала ссылку одного
  конкретного имени; оба коммита держатся именованными ссылками:
  `refs/backup/pre-a2-reject/a1-newgame-folder-and-scene` = `e0000c5b`,
  `refs/backup/pre-a2-reject/a2-two-players-networked` = `955e5e62`. Сборка мусора их не тронет.
- `i-review-and-cut-the-gate-surface-001` — измерение «32 скрипта, 74 вызова» устарело:
  `tools/check.ps1` = 211 строк, обычный прогон зовёт ОДИН скрипт (`hygiene.ps1`), всего 12 разных,
  остальные только на `-Deliver`. Ревизия, которую он заказал, исполнена (`c-exec-old-code-out-proba-001`).
- `i-old-code-move-to-own-folder-001` — его единственное требование выполнено: `Assets/GasCoopGame/`
  = 3 файла (документ + метаданные), продуктового кода ноль; `tests/GasCoopGame.Core.Tests/` без
  исходников. Противоречие о сроке стало беспредметным.
- `i-product-constitution-unrouted-001` — оба спорных правила («Engine-free core», «Deterministic
  core») в действующей конституции ОТСУТСТВУЮТ, осталось четыре правила. Снято.
- `i-closing-report-ownership-unclear-001` — подтверждено на практике ДВАЖДЫ: нога пишет свой отчёт
  (`066fcba4`, `7318a2dc`), интегратор потом переставляет статус (`b7ae1fa4`, `2eee9719`).
- `i-plan-receipt-fabricated-owner-verdict-001` — улика исчезла: квитанции
  `c-exec-newgame-folder-and-gates-001` нет ни в одном из пяти чекаутов и ни в одной ветке.
- `i-product-contour-consolidated-v34-001` — «контракт терминально 34 везде» устарело дважды:
  `validation.config` = `synced_contract_version: 36`.
- `i-deliver-red-on-fully-merged-state-is-by-design-001` — не дефект, а объяснение; по схеме §Issues
  такое место — `knowledge/`, не реестр проблем.

Перемеры, расширившие живые записи:

- Слоты: `origin/slot/win-u3` держит 22 коммита, которых нет в `main`, `origin/slot/win-u4` — 6
  (мёртвый узел g-37a1). Ни один слот не стоит на `main` (отстают на 2/15/15/24). `WIN-U2` числится
  `AVAILABLE` с изменённым `EditorBuildSettings.asset`. Своей несохранённой ИСТОРИИ нет ни у одного:
  все четыре `ahead 0`. Прежняя запись называла только `WIN-U4`.
- `WIN-U3`: `git status --porcelain` = 194 строки — 191 `.agents/skills/**` от запрещённой
  перегенерации, `ProjectSettings/EditorBuildSettings.asset`, и untracked
  `Assets/TunnelCrew/Art/FreeKitsProbe/` = 49 файлов, ~15 МБ (обёртки Kenney/KayKit/Quaternius,
  материал Poly Haven, лицензии, `AUTHORING.md`), mtime 08:39–12:07. Отчёт о блокировке ноги написан
  в 06:55, то есть ДО этой работы: задача возобновилась и сделала фактический `t-look-1`.
- `mcp_endpoint` записан теперь у `WIN-U3` (`http://localhost:24582/p/c64107a2`); прежнее «unrecorded
  у всех четырёх слотов» устарело.
- `ProjectSettings/UnityConnectSettings.asset:7` по-прежнему `m_Enabled: 1`.
- `c-exec-grid-v1-g01-document-authority-001` держит ровно две квитанции PLAN и ничего больше.

## state_changes

Применено к `live/indie-game-development/NOW.md`:

1. `updated` → `2026-08-05 by s-day-g-1d84-issues-cleanup-001`.
2. `issues`: 35 → 22 строки. Сняты восемь по доказательству выше. Слиты: прежний
   `i-direction-to-product-call-contract-001` → `i-call-named-path-absent-on-declared-basis-004`;
   `i-tunnel-role-description-owner-text-001` + `i-three-spaces-own-dangers-001` →
   `i-digging-own-bet-authored-fresh-001`; `i-procgen-determinism` +
   `i-multiple-cargo-geometries-residual-001` → `i-full-run-node-to-be-authored-001`;
   `i-owner-standing-rule-extend-never-rebuild-001` + `i-owner-working-scenes-need-real-tools-001` →
   новая `i-owner-standing-rules-on-how-work-is-shaped-001`.
3. `issues`: заведена `i-slot-u3-probe-work-unbanked-001` — незакоммиченная проба в `WIN-U3`.
4. `issues`: решения владельца записаны в `i-unity-cloud-services-enabled-in-main-001` («откатываем»),
   `i-grid-v1-g01-dead-root-open-001` («закрыть»), `i-steam-appid` («15 августа»). Ни одна из трёх не
   закрыта: закрывает их исполнение, а не его слово.
5. `issues`: перемерены и сужены `i-slot-u4-remote-tip-carries-foreign-commits-001` (все четыре
   слота), `i-unity-evidence-rests-on-owner-launch-001` (endpoint у U3), `i-now-hot-file-over-ceiling-001`.
6. `decisions`: `d-g-1d84-appetite-review-after-three-001` снято — точка пересмотра пройдена, его
   выбор (а) «23 задачи остаются как есть» уже записан в `bet.appetite` параллельной ногой.
7. `decisions`: `d-profile-file-format-recommendation-002` переписано — он снял вопрос в отдельный
   чат и назвал более широкое сомнение в самой `t-host-3`.
8. `decisions`: заведено `d-agents-skills-belong-in-repo-001` — его вопрос про `.agents/skills/**`,
   ждёт отдельного чата.

## assumptions

Ни одна закрытая запись не закрыта по тексту записи или по рассуждению: под каждой стоит команда на
живом состоянии. Записи, чьё содержание я не смог перемерить (`i-paper-loop-outran-the-build-001`,
`i-bet-tasks-never-sized-001`, `i-architecture-pass-skipped-for-this-bet-001`,
`i-cargo-carry-open-questions-001`, `i-ready-made-tools-scan-2026-08-03-001`,
`i-cargo-low-fps-derived-velocity-gap-001`, `i-verification-guards-unwired-not-deleted-001`,
`i-product-plan-deviations-unrouted-001`, `i-steam-demo-gates-unverified`,
`i-house-walls-below-eye-level-001`), оставлены нетронутыми.

## cuts

- `i-owner-standing-rules-on-how-work-is-shaped-001` должна жить в `knowledge/`, а не в реестре
  проблем: правило, сверяемое каждый раз, не может закрыться. `day` в `knowledge/` не пишет —
  переезд остаётся отдельной ноге, и это записано в самой строке.
- Откат `UnityConnectSettings` и закрытие мёртвого корня НЕ исполнены здесь: это продуктовые правки,
  а `day` продуктовый код не трогает. Оба едут пунктами в первом же продуктовом наряде.
- Строка `owner_ruling:` на `i-host-walks-through-walls-001` не тронута: она написана сегодня
  параллельной ногой, и переписывать чужую свежую строку в общем файле — тот самый класс коллизии,
  что назван ниже.

## manual-acceptance

1. Открыть `live/indie-game-development/NOW.md`, раздел `issues` — 22 строки вместо 35.
2. Проверить любое закрытие своей рукой, например: `git show-ref | grep pre-a2-reject` покажет, что
   потерянные, по мнению снятой записи, коммиты держатся именованными ссылками.
3. Раздел `decisions` — два вопроса, оба помечены как ждущие ОТДЕЛЬНОГО чата, ни один не решён за него.

## КОЛЛИЗИЯ, которую владелец должен знать

В том же рабочем каталоге ОДНОВРЕМЕННО работала вторая сессия: пока я правил `issues` и `decisions`,
она правила `tasks`/`open_calls` и завела три новых наряда
(`c-exec-g-1d84-cargo-tight-spot-001`, `c-exec-g-1d84-conditions-panel-001`,
`c-exec-g-1d84-host-under-the-judge-002`). Разделы разошлись, поэтому обе правки уцелели, но это
везение, а не устройство: два редактора одного горячего файла — уже записанный класс
(`gascoop-shared-worktree-staging-collision`). Ни один коммит здесь не сделан намеренно: любой
`git add NOW.md` захватит и чужую половину. Коммит должен делать тот, кто закончит последним, и
он обязан назвать в сообщении обе половины.

## next

Домой, в направление. Ждут его отдельных чатов: форма профилей хозяина (`t-host-3` под вопросом
целиком) и судьба `.agents/skills/**`. Ждёт его слова: спасать ли 15 МБ пробы в `WIN-U3`. Деталей по
сессии maintenance он просил простым языком — они в ответе чата, в состояние не записаны.

END_OF_FILE
