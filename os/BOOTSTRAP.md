# BOOTSTRAP — запуск направления, по шагам

Точная инструкция первого запуска. Вариант A — ChatGPT Project (основной для владельца), вариант B — всё в одной Claude Code-сессии. Проблемы с самим воркфлоу — не здесь: `os/MAINTENANCE.md`.

## Вариант A: ChatGPT Project

**Шаг 0. Предусловие.** `os/**` лежит в `main` этого репозитория.

**Шаг 1. Writer-сессия.** Открой Claude Code (или Codex) на репо `my_global_workflow` и оставь сессию открытой. Это «писатель»: сюда будешь вставлять RESULT'ы чатов. Больше ничего настраивать в ней не нужно.

**Шаг 2. Проект.** ChatGPT → New Project → имя направления (например, «Indie Game Dev»).

**Шаг 3. Инструкции.** Открой `os/adapters/SESSION_PAYLOAD.md` на GitHub, скопируй блок в Project Instructions, замени `<direction-id>` (например, `indie-game-dev`). Всё.

**Шаг 4. Доступ к репо.** Подключи GitHub-коннектор проекта к `ainazemtsau/my_global_workflow`. Нет коннектора → загрузи как Project Files: `os/KERNEL.md`, `os/schema/packets.md`, `os/schema/direction-files.md`, все файлы `os/plays/`. Файлы из `live/**` не загружать никогда (протухнут).

**Шаг 5. Первый чат.** Вставь, заполнив `<...>`:

```
CALL c-001
to: session
direction: <direction-id>
play: frame
goal: |
  Создать направление: <одно предложение о твоей амбиции>.
context: |
  Правила: os/KERNEL.md. Процедура: os/plays/frame.md.
  Схемы файлов: os/schema/direction-files.md.
  Это новое направление, live/<direction-id>/ ещё не существует.
boundaries: |
  Только CHARTER и корень дерева. Никаких задач и детальных планов.
done_when: |
  CHARTER.md и TREE.md составлены и приняты мной;
  в NOW.md лежит CALL на первый shape.
return: RESULT по os/schema/packets.md
budget: one session
```

**Шаг 6. Контрольные точки** (так выглядит «всё по плану»):
- первая строка ответа: `📍 <direction-id>/—/— — frame: ...`;
- вопросы — одним батчем, ≤7;
- дальше по порядку: хартия → пре-мортем (≥5 причин провала) → outside view → дерево из 2–5 целей (все `parked`, без задач) → рекомендация первого узла с вариантами;
- в конце — блок `RESULT` со `state_changes` и `next`.
Нет 📍-строки или RESULT'а — чат не прочитал правила: проверь шаги 3–4.

**Шаг 7. Применение.** Скопируй RESULT целиком → в writer-сессию со словами: `Apply per os/adapters/coding-agent.md, role: writer`. Ожидаемо: writer создаёт `live/<direction-id>/...`, коммитит, возвращает готовый CALL следующего чата.

**Шаг 8. Цикл.** Новый чат в том же проекте → вставь CALL из шага 7 (это будет shape). Дальше всегда одинаково: чат → RESULT → writer → следующий CALL → новый чат. Раз в неделю — pulse (удобнее прямо в writer-сессии: `play: pulse, все направления`).

**Если что-то разъехалось:** новый чат, одна строка `play: repair, direction: <id>` + вставь текущий NOW.md.

## Вариант B: всё в Claude Code

Один шаг: открой сессию Claude Code на этом репо и вставь тот же CALL из шага 5 с припиской «работай по os/KERNEL.md; ты сам себе writer — применяй state_changes и коммить сам». Сессия проведёт frame и закоммитит направление без пересылок. Для state-тяжёлых plays (shape, review, pulse, repair) этот вариант всегда дешевле по твоим действиям.

## Чего НЕ делать

- Не создавай направления «про запас» — направление создаётся, когда есть амбиция (gate G8).
- Не редактируй `live/**` руками — только через RESULT/writer.
- Проблема или хотелка к самому воркфлоу — не чини в чате направления: новая Claude Code-сессия + `os/MAINTENANCE.md` (один запрос = одна сессия).

END_OF_FILE: os/BOOTSTRAP.md
