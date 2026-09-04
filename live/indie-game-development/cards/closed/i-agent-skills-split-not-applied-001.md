---
id: i-agent-skills-split-not-applied-001
_kind: issue
level: direction
route: review
evidence: history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md
_pos: 45
---

## issue
GasCoopGame всё ещё отслеживает 191 Codex-specific Unity tool-skills; принятый split и безопасный Pi/skills-only профиль ещё не применены.
## review_when
До следующей перегенерации/правки agent skills либо на review текущей ставки отдельно допустить и выдать продуктовую миграцию вместе с проверенной заменой.
## журнал
2026-08-11 · УСТРАНЕНА: принятый cross-agent split применён и опубликован на GasCoopGame dev `eaea80db`; implementation `f7c60cdf` удалил 191 generated tool-skills из Git, оставил curated Codex/Claude routing и добавил ignored hash-bound Pi profile через exact-slot/lease wrapper. Product RESULT, независимый review и чистый `tools/check.ps1 -Deliver` подтверждают замену. · history/2026-08-11-s-repair-i-agent-skills-split-applied-001.md
2026-08-11 · 2026-08-11 | s-repair-i-agent-skills-split-applied-001 | repair | direction | i-agent-skills-split-not-applied-001: принятый cross-agent split применён и опубликован на GasCoopGame dev `eaea80db` — 191 generated tool-skills сняты из Git, curated Codex/Claude routing сохранён, Pi получает ignored hash-bound profile через exact-slot/lease wrapper; full Deliver и независимый review зелёные, поэтому улика «ещё не применено» закрыта, а постоянная runtime policy сохранена -> history/2026-08-11-s-repair-i-agent-skills-split-applied-001.md · history/2026-08-11-s-repair-i-agent-skills-split-applied-001.md
2026-08-11 · 2026-08-11 | s-research-agents-skills-cross-agent-split-001 | research | direction | d-agents-skills-belong-in-repo-001: владелец принял split — tracked остаются ручные workflow/routing skills, native MCP является основным для Codex/Claude, agent-specific CLI profile для Pi допускается после проверки пути, версии и slot identity; старая развилка закрыта, а ещё не выполненный переход GasCoopGame сохранён отдельной уликой без продуктовой мутации -> history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md · history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md
END_OF_FILE: live/indie-game-development/cards/closed/i-agent-skills-split-not-applied-001.md
