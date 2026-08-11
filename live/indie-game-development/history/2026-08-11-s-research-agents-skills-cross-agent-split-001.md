RESULT s-research-agents-skills-cross-agent-split-001
direction: indie-game-development
track: direction
play: research
node/task: d-agents-skills-belong-in-repo-001

outcome: |
  Владелец принял вариант split: механизм Skills сохраняется, но bulk Unity per-tool skills
  не являются отслеживаемой репозиторной властью. В Git остаются ручные workflow/routing
  skills; Codex и Claude Code используют native MCP как основной транспорт; Pi и другие
  skills-only агенты получают agent-specific generated CLI profile только после проверки
  точного Unity root, совместимой закреплённой версии CLI и slot identity. Переход в
  GasCoopGame этой ногой не выполнялся: удаление текущего bulk допустимо только вместе с
  проверенной заменой.

evidence: |
  - Точный owner verdict после показанной целиком рекомендации: «ок я с тобой согласен»
    (2026-08-11). Принятая рекомендация была названа однозначно: «Нужен вариант split» и
    далее перечисляла tracked ручные skills, native MCP для Codex/Claude, generated CLI
    profile для Pi и запрет удалять 191 файлов до готовой замены.
  - Unity-MCP намеренно генерирует `unity-mcp-cli run-tool`, а не native MCP invocation:
    https://github.com/IvanMurzak/Unity-MCP/blob/7994e952ccd7afa550dbd3b8191795d1a817608b/Unity-MCP-Plugin/Packages/com.ivanmurzak.unity.mcp/Editor/Scripts/Utils/UnitySkillFileGenerator.cs#L20-L24
  - Codex project discovery — `.agents/skills`, полный SKILL.md загружается при выборе:
    https://learn.chatgpt.com/docs/build-skills
  - Claude Code project discovery — `.claude/skills`; native MCP поддерживает dynamic tool
    updates: https://code.claude.com/docs/en/slash-commands#where-skills-live
  - Pi project discovery включает `.agents/skills`, но vanilla Pi не имеет встроенного MCP:
    https://github.com/earendil-works/pi/blob/cd6852a123f2c0cc646a41a2a52f3711a603b822/packages/coding-agent/docs/skills.md
    и https://github.com/earendil-works/pi/blob/cd6852a123f2c0cc646a41a2a52f3711a603b822/packages/coding-agent/README.md#L490-L500
  - Локальная проверка 2026-08-11: в U1 находятся 192 skills — 191 generated-like,
    переписанный на direct-through-Codex bulk, и один ручной `unity-urp-visual-dev`;
    Codex Desktop обнаружил все 192, Claude Code работает через отдельно настроенный native
    MCP, Pi видит `.agents/skills`, но текущие direct-Codex тела исполнить не может.
  - Локальная проверка CLI: Pi на Windows использует Git Bash; из корня U1
    `unity-mcp-cli status` видит Editor/server. Upstream recipe не передаёт project path и
    ломается из подпапки; глобальный CLI 0.84.1 отстаёт от package 0.87.0; `run-tool` не
    использует native `/p/<pin>`, поэтому равная multi-slot safety не доказана.

state_changes: |
  - Close decision card `d-agents-skills-belong-in-repo-001` as resolved by the exact owner
    verdict «ок я с тобой согласен»; disposition: accepted split as stated in outcome and
    evidence, replacing the former default option б.
  - Add `knowledge/agent-skills-runtime-policy.md`, status current, read by work/repair before
    any product-repo agent instructions, Unity MCP setup or generated-skills change. Every
    policy line points to this receipt and the exact owner verdict.
  - Add issue card `i-agent-skills-split-not-applied-001`: current GasCoopGame bulk remains
    tracked and Codex-specific; route the product migration through review before the next
    skills regeneration/change or at current-bet review. This records unfinished application
    without authorizing product mutation or creating an unrelated active task/CALL.
  - Preserve NOW, bet, tasks, tracks, calls, every unrelated decision/question/issue,
    CHARTER and product repository unchanged.
  - Save this full RESULT once as
    `live/indie-game-development/history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md`
    and append the leg log once to the new issue journal. The closed decision already carries
    its complete disposition plus the same history pointer from `card close`; the current
    `osctl leg close` cannot address a card after it moves to `closed/` (the known limitation
    recorded in `os/FRICTION.md`), so no reopen/noise cycle is introduced.

captures:
  - `i-agent-skills-split-not-applied-001`: accepted policy still needs a separately admitted product-repo migration; current bulk must not be deleted before the replacement is verified.

decisions_needed: []

play_check:
  - "1 Recite: done — one bounded question: whether tracked `.agents/skills/**` belong in the repository; return was one cross-agent recommendation and its limits."
  - "2 Investigate: done — upstream Unity-MCP, Codex, Claude Code and Pi contracts, local 192-skill discovery, installed versions and U1-U4 routing were checked; independent refutation was merged."
  - "3 Confidence: done — established discovery/transport facts were separated from the proposed repository arrangement; the remaining unproved boundary is strict CLI project identity under concurrent slots, so CLI support stays gated."
  - "4 Close: done — exact owner verdict received and cited: «ок я с тобой согласен»; decision closes as split with disposition/history pointer in its close journal, while product application remains a routed issue rather than an inferred launch."

log: 2026-08-11 | s-research-agents-skills-cross-agent-split-001 | research | direction | d-agents-skills-belong-in-repo-001: владелец принял split — tracked остаются ручные workflow/routing skills, native MCP является основным для Codex/Claude, agent-specific CLI profile для Pi допускается после проверки пути, версии и slot identity; старая развилка закрыта, а ещё не выполненный переход GasCoopGame сохранён отдельной уликой без продуктовой мутации -> history/2026-08-11-s-research-agents-skills-cross-agent-split-001.md

next: |
  return-to-owner — решение записано; продуктовая миграция не запущена и остаётся issue
  `i-agent-skills-split-not-applied-001`. Независимый вопрос владельцу
  `q-house-hears-20-percent-earlier-001` сохранён без изменений.
