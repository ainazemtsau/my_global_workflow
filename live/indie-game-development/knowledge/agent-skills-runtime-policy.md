# Unity agent skills: repository and runtime policy

accepted: 2026-08-11   read_by: work/repair before changing product-repo agent instructions, Unity MCP setup or generated skills   status: current

Владелец принял показанный вариант `split` точными словами «ок я с тобой согласен»: tracked остаются ручные workflow/routing skills, а bulk Unity per-tool skills являются agent-specific generated output, не репозиторной властью (`history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md`).

Codex и Claude Code используют native MCP как основной транспорт; Pi и другие skills-only агенты получают CLI profile только после проверки exact Unity root, совместимой закреплённой версии CLI и slot identity (`history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md`).

Bulk удаляется только вместе с проверенной заменой; skill сам не регистрирует MCP tools, поэтому дефект регистрации чинится в MCP/session setup, а не сохранением bulk snapshot (`history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md`).

END_OF_FILE: live/indie-game-development/knowledge/agent-skills-runtime-policy.md
