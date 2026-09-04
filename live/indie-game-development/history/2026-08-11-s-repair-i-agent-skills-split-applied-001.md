RESULT s-repair-i-agent-skills-split-applied-001
direction: indie-game-development
track: direction
play: repair
node/task: i-agent-skills-split-not-applied-001

outcome: |
  Улика больше не соответствует реальности и закрыта: принятый владельцем cross-agent
  split применён в GasCoopGame на dev и опубликован. В Git остались только ручные
  routing/workflow skills и точные Claude adapters; Codex/Claude используют native MCP,
  а Pi получает игнорируемый воспроизводимый профиль через fail-closed wrapper.

evidence: |
  - Владелец запустил исправление словами «ну так реализовывай решение» и выбрал venue
    точными словами «давай в dev работать так как это структурная работа а не работа по игре».
  - Product implementation commit `f7c60cdfb88962f47828c83b542de28a1ebcf055` удаляет
    191 tracked generated skill, добавляет curated routing/adapters, Pi wrapper, lease
    verification и hygiene boundary.
  - Closing evidence commit `eaea80dbdbce2a7fcd86534df01a9248a3e5a820` содержит
    `docs/results/c-maint-agent-skills-runtime-001.md` со статусом DELIVERED on dev и
    `docs/reviews/review-c-maint-agent-skills-runtime-001.md`; независимое трёхраундовое
    review завершилось `Ready. No actionable findings remain.`
  - На чистом product dev `tools/check.ps1 -Deliver` завершился exit 0: hygiene OK,
    committed-tree parity и closing RESULT honesty прошли, `OK: all active gates green`.
    Focused self-tests отдельно подтвердили exact lease/no-view-mutation, exact-project
    Unity PID, version/pin/fingerprint, template-drift rejection и content hashes.
  - После non-force push и fetch `origin/dev` и локальный dev равны
    `eaea80dbdbce2a7fcd86534df01a9248a3e5a820`; working tree чист.
  - close: light — все строки закрытия заново выведены из опубликованных commit ids/bytes,
    текущего remote readback и собственных gate outputs этой ноги; owner-content verdict
    или непроверяемое продуктовое утверждение для закрытия не требуются.

state_changes: |
  - Close issue card `i-agent-skills-split-not-applied-001` as discharged. Its close journal
    states that the accepted split is published on product dev at `eaea80db...`, names the
    implementation and result/review artifacts, and points to this history receipt.
  - Preserve `knowledge/agent-skills-runtime-policy.md` as current; its runtime policy remains
    the authority for later skill/MCP changes even though the one-time migration issue closes.
  - Preserve NOW, current bet, every task/call/decision/question/other issue, forecast,
    CHARTER and all product/gameplay state unchanged.
  - Save this full RESULT once as
    `live/indie-game-development/history/2026-08-11-s-repair-i-agent-skills-split-applied-001.md`
    and append the leg log once to the closed issue journal.

captures: []

decisions_needed: []

play_check:
  - "1 Name: done — the issue says the migration is unapplied, while published product dev now contains the verified replacement."
  - "2 Reconstruct: done — exact product commits, tracked skill inventory, review artifact, full Deliver output and origin/dev readback were re-derived first-hand."
  - "3 Correct: done — close only the contradicted issue; keep the durable policy and every unrelated direction surface unchanged."
  - "4 Confirm (owner): done — exact launch words were «ну так реализовывай решение» and exact venue words were «давай в dev работать так как это структурная работа а не работа по игре»."
  - "5 Friction: done — no new OS hole; the temporary product-write lease was revoked after push/readback."

log: 2026-08-11 | s-repair-i-agent-skills-split-applied-001 | repair | direction | i-agent-skills-split-not-applied-001: принятый cross-agent split применён и опубликован на GasCoopGame dev `eaea80db` — 191 generated tool-skills сняты из Git, curated Codex/Claude routing сохранён, Pi получает ignored hash-bound profile через exact-slot/lease wrapper; full Deliver и независимый review зелёные, поэтому улика «ещё не применено» закрыта, а постоянная runtime policy сохранена -> history/2026-08-11-s-repair-i-agent-skills-split-applied-001.md

next: |
  return-to-owner — structural migration опубликована на product dev; эта issue закрыта.
  Игровая ставка, её фронтир и независимый вопрос владельцу не менялись.
