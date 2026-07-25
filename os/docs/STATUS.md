# STATUS - снапшот системы и мандат помощника

updated: 2026-07-24 (strategy reset: direction-level day adviser, one objective, execution lanes, issues and calibrated forecast)

Этот документ - точка входа для новой агентной сессии, помогающей владельцу с системой. Он самодостаточен: прочитав его и файлы по ссылкам, сессия может проводить аудит, помогать с направлениями, анализировать чаты и чинить/дорабатывать систему.

## 1. Что это

Репозиторий - **Direction OS**: личная система владельца для ведения жизненных направлений через короткие AI-сессии над состоянием в git. Правила: `os/KERNEL.md` (≤1500 слов, 10 гейтов G1-G10). Процедуры: `os/plays/` (frame, map, shape, day, work, guide, review, research, pulse, repair и converge-процедуры). Схемы: `os/schema/`. Адаптеры платформ: `os/adapters/`. Инженерный контур (код продуктов): `os/engineering/`. Запуск: `os/BOOTSTRAP.md`. Изменение системы: только по `os/MAINTENANCE.md`. Роли агентных сессий распознаются по входу - таблица в корневом `AGENTS.md`.

## 2. Как сюда пришли (минимум истории)

До июня 2026 было четыре поколения workflow (vNext-R -> v2 -> v3); аудит показал: системная перегрузка (60-80 полей на чат, непроверяемые правила, человек как транспорт) - всё заморожено в `archive/`. Direction OS построена с нуля по требованиям (`os/docs/REQUIREMENTS.md`, R-1...R-45) и исследованию практик (`os/docs/RESEARCH_BASIS.md` - каждый механизм со ссылкой на источник). Архитектура и трассировка: `os/docs/DESIGN.md`.

## 3. Состояние пилота (на дату снапшота)

- Стратегический слой использует **frame → map → outcome route**. Обычный build-outcome проходит readiness/converge → shape; `outcome_kind: specification` проходит owner-authority work → fresh converge-verify → narrow review и закрывается parked без bet/tasks/tracks/shape. Canon может быть direction-local authority-контуром, но не является core workflow или контроллером.
- Live-reset завершён RESULT `s-repair-strategy-layer-reset-cleanup-001`: `NOW.bet: null`, задач и execution lanes нет, одиннадцать нерешённых фактов сохранены в `NOW.issues`, а единственный законный frontier — owner-present frame `c-frame-october-demo-foundation-001`.
- Архив и большая исследовательская база сохраняются как cold evidence. Они не являются текущей стратегией и не удаляются при reset.
- Старые local plays, Program/Demo workflow и HTML-панель явно помечены non-runnable/retired evidence; тела и история сохранены. CHARTER/TREE пока намеренно не заменены: TREE всё ещё содержит legacy `active/parallel`, поэтому карантин действует до точного owner-approved G9 frame/map и schema-clean не заявлен.

### 3.1 Доработки контура планирования (2026-06-11)

Две волны правок plays (по явному запросу владельца, в бюджетах, KERNEL/гейты не тронуты):
- **Дивергенция**: shape «2-3 подхода до выбора»; map «>=1 неочевидный путь».
- **frame**: интервью только owner-only; шаг homework (research до хартии).
- **Search plane**: research `strategic_search`/nominal-group/miner-briefs; map human-first + опциональный search-first + поле `edge` + один редкий стимул + noun-test; shape Berg equal-footing + инкубационный зазор + probe-поля (forecast/against/next_if) + AI-burst evaluator; review forecast-check + harvest edges; pulse-пункт 11 market contact; CHARTER `edges`/`risk_posture`.
- Каждый механизм несёт фальсификатор в `os/FRICTION.md` - откат помеханизменно. Источники и проверка - `os/docs/RESEARCH_BASIS.md` (строка search plane) + proposal-доки в `os/docs/`.
- **Session protocol, G10**: ordinary legs show opening contract; `day` shows only `📍 День: ...` and a derived plain-language view. Day discussion is read-only; exact save words are required for one RESULT/apply/commit. Binding G5 remains a separate fresh chat.
- **Strategy/day model** (2026-07-24 reset): TREE is the sole roadmap; NOW holds at most one active bet. Future goals stay parked/shaped. Optional tracks are WIP-limited execution lanes serving that bet, never independent strategic roots. NOW.issues preserves unresolved problems with route+review trigger. direction_forecast is `no_basis` unless a numeric chance has cited empirical calibration. The detailed daily dashboard is rendered in chat; the OS creates no controller track, outcome request, copied plan or new HTML authority. The pilot's former HTML panel is retired static evidence by the live reset RESULT.

## 4. Мандат помощника (что от тебя ждут)

1. **Аудит и анализ системы** - сверяй с REQUIREMENTS (трассировка в DESIGN §3: каждый R закрыт компонентом; компонент без R - кандидат на удаление).
2. **Помощь с первыми направлениями** - по BOOTSTRAP; следи за гейтами (особенно: G2 - задачи только в активном бете; G8 - идеи по умолчанию parked; G9 - планы только с владельцем).
3. **Анализ транскриптов чатов** - ordinary first reply shows steps; day reply shows the plain derived brief. Verify: no write before exact save words; one RESULT per saved leg; roadmap/bet/lane/issue boundaries hold; no fixed questionnaire or hidden legacy dispatch.
4. **Фиксы и доработки** - строго по `os/MAINTENANCE.md`: один вопрос = одна сессия; явный запрос владельца - достаточный триггер; самоинициатива - только при >=2 записях во FRICTION; наименьшая правка в бюджетах (ядро <=1500 слов, play <=600, 6 типов state-файлов); после правки - сверка перекрёстных ссылок и END_OF_FILE-маркеров; если менялся `os/adapters/SESSION_PAYLOAD.md` - сказать владельцу перевставить инструкции в проекты.

## 5. Предпочтения владельца (нарушать нельзя)

- Русский язык, объяснения «на пальцах», без жаргонных стен. Варианты с рекомендацией вместо открытых вопросов.
- Глобальные планы - только в со-творчестве (G9), по одному артефакту.
- Владелец никогда не сочиняет пакеты руками: вход - обычные слова или «продолжаем»; CALL/RESULT - машинный формат для копирования.
- Никаких постоянных worker/reviewer/writer-сессий. Дневной чат может жить один день как read-only советник; каждый save является отдельным atomic leg, G5 - отдельно.
- Хранить полно, грузить минимально: детали в history/, в контексте - строка + ссылка.

## 6. Открытые хвосты (не делать без запроса - просто знать)

- ~120 мёртвых легаси-веток в remote (владелец чистку не подтверждал).
- Автоматизация пересылки RESULT и agent-run control-plane - проектируется как runtime-слой: `os/adapters/runtime.md`; стадии автономии 2-3: `os/adapters/autonomy.md`.
- Branch protection на main предложена, не включена.
- Watch-items: рост TREE со временем (лечить схлопыванием веток по FRICTION); ChatGPT-сессии слегка отступают от схемы NOW.md (1 случай зафиксирован - второй повтор = FRICTION-правка).

## 7. Жёсткий минимум правил (дайджест, полные - в AGENTS.md и KERNEL)

`live/**` меняется только применением RESULT.state_changes. `archive/**` - read-only. Каждый state-файл имеет END_OF_FILE. Один atomic leg = одна работа; day discussion read-only, save = отдельный leg. Бюджеты абсолютны.

END_OF_FILE: os/docs/STATUS.md
