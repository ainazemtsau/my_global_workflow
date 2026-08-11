---
id: d-agents-skills-belong-in-repo-001
_kind: decision
_bet: g-5a7c
_pos: 0
track: direction
---

## q
Нужны ли репозиторию отслеживаемые `.agents/skills/**` вообще. Слова владельца 2026-08-05: «они нам реально не нужны это unity mcp генерирвует». Он снял вопрос в отдельный чат и решения здесь не принимал.
## options
```yaml
- а) убрать `.agents/skills/**` из отслеживаемых совсем — их источник и так генератор
  Unity MCP
- б) оставить как есть и держать продуктовый запрет на перегенерацию (`AGENTS.md`)
- в) оставить, но перестать отслеживать (игнорировать), чтобы перегенерация не пачкала
  слот
```
## recommendation
Рекомендации нет — ждёт его отдельного разбора. Довод для него, измеренный 2026-08-05: перегенерация в `WIN-U3` не была безобидным шумом — она заменила прямой вызов инструмента на рецепт через `unity-mcp-cli`, то есть ровно тот сторонний транспорт, который продуктовый `AGENTS.md` запрещает. 191 файл отброшен его словом «почисти skills», запрет восстановлен. Пока запись живёт, вариант (б) действует по умолчанию.
## журнал
2026-08-11 · Владелец принял показанный вариант split точными словами «ок я с тобой согласен»: tracked остаются ручные workflow/routing skills, bulk Unity tool-skills становятся agent-specific generated output; Codex/Claude используют native MCP, а Pi/skills-only CLI профиль допускается после проверки exact project path, pinned compatible version и slot identity. Продуктовая миграция этой ногой не запускалась; она сохранена как i-agent-skills-split-not-applied-001. · history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md
2026-08-05 · проба спасена, перегенерация skills отброшена · history/2026-08-05-s-day-g-1d84-probe-banked-skills-cleaned-001.md
END_OF_FILE: live/indie-game-development/cards/closed/d-agents-skills-belong-in-repo-001.md
